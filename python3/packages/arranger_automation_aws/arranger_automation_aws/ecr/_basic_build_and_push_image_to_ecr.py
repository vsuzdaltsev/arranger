from abc import ABC, abstractmethod
from datetime import datetime
import os
import pathlib
import shutil
import tempfile
from typing import Any, Dict, List, Tuple, Union

from eusy_automation.log import Log
from eusy_automation_aws.codeartifactory import MvnCodeartifactory
from eusy_conf.app_conf import AppConf


def build_dockerfile() -> str:
    def _base_image():
        if os.getenv("BASE_IMAGE_OVERRIDE"):
            return os.getenv("BASE_IMAGE_OVERRIDE")

        return "public.ecr.aws/docker/library/openjdk:21-jdk"

    return (
        f"FROM {_base_image()}\n"
        "EXPOSE 8080\n"
        "RUN mkdir /app\n"
        "ARG JAR_PATH\n"
        "ARG GIT_REF\n"
        "RUN echo ${GIT_REF} > /git_ref.txt\n"
        "COPY ${JAR_PATH} /app/application.jar\n"
        'CMD ["java", "-jar", "/app/application.jar"]\n'
    )


class BasicBuildAndPushImageToEcrMixin(ABC):
    DEFAULT_BUILD_ROOT = "build_dir"
    DEFAULT_DOCKERFILE = "Dockerfile"
    UPDATE_SUBMODULES = True

    def __repr__(self) -> str:
        """Object string representation."""
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(self, **kwargs):
        self.log = Log().logger(desc=self.__class__.__name__)
        self.now = datetime.utcnow()
        self.kwargs = kwargs

        self._setup_params()
        self._validate_params()

    @abstractmethod
    def _setup_params(self) -> type(None):
        pass

    @abstractmethod
    def _build_and_publish_to_ecr(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def run(self, *args, **kwargs) -> type(None):
        pass

    def _validate_params(self) -> type(None):
        assert self.cluster_name_alias in AppConf.CLUSTERS
        assert isinstance(self.image_name, str)
        assert isinstance(self.debug, bool)

    @staticmethod
    def _additional_tags(additional_tags: str) -> Union[List[str], List]:
        if additional_tags:
            return additional_tags.strip().split(",")

        return []

    def _create_temp_dir(self) -> type(None):
        pathlib.Path(self.build_root).mkdir(parents=True, exist_ok=True)
        self.build_dir = tempfile.mkdtemp(
            prefix=f"{self.image_name}-build", dir=self.build_root
        )

    def _aws_region(self) -> str:
        from eusy_globals.cdktf_globals import CdktfGlobals

        _globals = CdktfGlobals(cluster_name_alias=self.cluster_name_alias)

        return _globals.aws_region

    def _aws_profile(self) -> str:
        from eusy_globals.cdktf_globals import CdktfGlobals

        _globals = CdktfGlobals(cluster_name_alias=self.cluster_name_alias)

        return _globals.aws_profile

    def _accounts_to_create_ecr_within(self) -> List[str]:
        if self._aws_profile() == AppConf.ORCHESTRA_ACCOUNT:
            return [
                self._aws_profile(),
            ] + AppConf.ORCHESTRA_SUBORDINATE_ACCOUNTS
        return [self._aws_profile()]

    def _create_ecr_repo(self) -> Any:
        from eusy_automation_aws.ecr import BasicEcr

        if self.create_ecr_repo:
            for aws_profile in self._accounts_to_create_ecr_within():
                self.log.debug(f">> Create ECR for AWS profile: {aws_profile}.")

                BasicEcr(
                    repository_name=self.image_name,
                    region_name=self._aws_region(),
                    aws_profile=aws_profile,
                ).prepare_repository()

    def _cleanup(self) -> type(None):
        if self.cleanup:
            if os.path.exists(self.build_dir):
                self.log.warning(
                    f">> Remove temporary build directory: {self.build_dir}."
                )
                shutil.rmtree(self.build_dir, ignore_errors=False, onerror=None)


class BasicBuildAndPushImageToEcrBack(BasicBuildAndPushImageToEcrMixin):
    def _setup_params(self) -> type(None):
        self.create_ecr_repo = self.kwargs.get("create_ecr_repo")
        self.cluster_name_alias = self.kwargs.get("cluster_name_alias")
        self.mvn = self.kwargs.get("mvn")
        self.image_name = self.kwargs.get("image_name")
        self.dockerfile = self.kwargs.get("dockerfile", self.DEFAULT_DOCKERFILE)
        self.tag = self.kwargs.get("tag")
        self.build_root = self.kwargs.get("build_root", self.DEFAULT_BUILD_ROOT)
        self.build_args = (
            self.kwargs.get("build_args") if self.kwargs.get("build_args") else {}
        )
        self.secret = self.kwargs.get("secret")
        self.debug = self.kwargs.get("debug")
        self.cleanup = self.kwargs.get("cleanup")
        self.additional_tags = self._additional_tags(
            additional_tags=self.kwargs.get("additional_tags")
        )

        self.build_dir = None

    def _download_jar(self, output_file: str = None) -> str:
        if not output_file:
            output_file = f"{self.build_dir}/default.jar"

        mvn = MvnCodeartifactory(
            aws_profile=self.cluster_name_alias,
            region=self._aws_region(),
            domain=self.cluster_name_alias,
        )
        jar_name = mvn.download_jar(
            namespace=self.mvn.get("namespace"),
            package=self.mvn.get("package"),
            package_version=self.mvn.get("package_version"),
            output_file=output_file,
        )

        return jar_name

    def _build_and_publish_to_ecr(
        self, docker_credentials: List[Tuple[str, str, str]]
    ) -> Any:
        from eusy_automation.docker import MultiPlatformDockerImageOnWhales

        image = MultiPlatformDockerImageOnWhales(
            image_name=self.image_name,
            dockerfile=self.dockerfile,
            context=self.build_dir,
            buildargs=self.build_args,
            tag=self.tag,
            debug=self.debug,
            additional_tags=self.additional_tags,
            docker_credentials=docker_credentials,
        )
        image_metadata = image.build(
            show_build_log=self.debug, docker_credentials=docker_credentials
        )

        return image_metadata

    def run(self, docker_credentials: List[Tuple[str, str, str]]) -> Dict:
        from eusy_automation_aws.ecr.ecr_credentials import EcrAccessCredentials

        if not docker_credentials:
            docker_credentials = EcrAccessCredentials(
                cluster_name_alias=self.cluster_name_alias
            )

        self._create_temp_dir()
        self._create_dockerfile()
        jar = self._download_jar()
        self._create_ecr_repo()
        output = self._build_and_publish_to_ecr(
            docker_credentials=docker_credentials
        ) | {"mvn": self.mvn | {"resolved_asset": jar}}
        self._cleanup()

        self.log.debug(f">> Build params: {output}.")

        return output

    def _create_dockerfile(self) -> type(None):
        with open(f"{self.build_dir}/{self.dockerfile}", "w") as dockerfile:
            dockerfile.write(build_dockerfile())


class BasicBuildAndPushImageToEcrFront(BasicBuildAndPushImageToEcrMixin):
    def _setup_params(self) -> type(None):
        self.create_ecr_repo = self.kwargs.get("create_ecr_repo")
        self.cluster_name_alias = self.kwargs.get("cluster_name_alias")
        self.app = self.kwargs.get("app")
        self.git_ref = self.kwargs.get("git_ref")
        self.image_name = self.kwargs.get("image_name")
        self.dockerfile = self.kwargs.get("dockerfile", self.DEFAULT_DOCKERFILE)
        self.tag = self.kwargs.get("tag")
        self.build_root = self.kwargs.get("build_root", self.DEFAULT_BUILD_ROOT)
        self.build_args = (
            self.kwargs.get("build_args") if self.kwargs.get("build_args") else {}
        )
        self.secret = self.kwargs.get("secret")
        self.debug = self.kwargs.get("debug")
        self.cleanup = self.kwargs.get("cleanup")
        self.additional_tags = self._additional_tags(
            additional_tags=self.kwargs.get("additional_tags")
        )

        self.build_dir = None
        self.current_commit_sha = None

    def run(self, docker_credentials: List[Tuple[str, str, str]]) -> Dict:
        from eusy_automation_aws.ecr.ecr_credentials import EcrAccessCredentials

        if not docker_credentials:
            docker_credentials = [
                EcrAccessCredentials(cluster_name_alias=self.cluster_name_alias)
            ]

        self._create_temp_dir()
        self._git_clone_checkout()
        self._create_ecr_repo()
        output = self._build_and_publish_to_ecr(
            docker_credentials=docker_credentials
        ) | {"app": self.app}
        self._cleanup()

        self.log.debug(f">> Build params: {output}.")

        return output

    def _git_clone_checkout(self) -> type(None):
        from eusy_automation.arranger_git.basic_git_repo import BasicGitcommitRepo

        _git = BasicGitcommitRepo(
            repo_name="switch-fronts", aws_region=self._aws_region()
        )
        _git.clone(where=self.build_dir)
        _git.checkout(git_ref=self.git_ref)

        self.current_commit_sha = _git.current_commit_sha(short_notation=True)

    def _build_and_publish_to_ecr(
        self, docker_credentials: List[Tuple[str, str, str]]
    ) -> Dict:
        from eusy_automation.docker import MultiPlatformDockerImageOnWhales

        image = MultiPlatformDockerImageOnWhales(
            image_name=self.app,
            dockerfile=self.dockerfile,
            context=self.build_dir,
            buildargs=self.build_args,
            tag=self.tag,
            debug=self.debug,
            additional_tags=list(set(self.additional_tags + [self.current_commit_sha])),
            platforms=self.kwargs.get("platforms"),
            docker_credentials=docker_credentials,
        )
        image_metadata = image.build(
            show_build_log=self.debug, docker_credentials=docker_credentials
        )

        return image_metadata
