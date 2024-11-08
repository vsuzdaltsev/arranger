"""Build Docker image and push it to the given AWS ECR repo. Python on Whales version."""

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union

from python_on_whales import docker

from arranger_automation.log import Log


class BasicDockerImageOnWhales(ABC):
    """Manipulate Docker images: build, push to the Container Registry repos."""

    DOCKER_API_CLIENT_BASE_URL = "unix://var/run/docker.sock"

    def __repr__(self) -> str:
        """Object string representation."""
        return f"{super().__repr__()}: {self.__dict__}"

    @abstractmethod
    def _platforms(self) -> List[str]:
        return self.kwargs.get("platforms") or [
            "linux/amd64",
            "linux/amd64/v2",
            "linux/arm64",
        ]

    def _setup_buildargs(
        self, input_buildargs: Union[Dict[str, str], Dict[None, None], None]
    ) -> Dict[str, str]:
        if not input_buildargs:
            return {}

        return input_buildargs

    def __init__(
        self,
        image_name: str,
        tag: str = "latest",
        context: str = ".",
        dockerfile: str = "Dockerfile",
        buildargs: Union[Dict, None] = None,
        **kwargs,
    ):
        self.log = Log.logger(desc=type(self).__name__)
        self.image_name = image_name
        self.tag = tag
        self.context = context
        self.dockerfile = dockerfile
        self.buildargs = self._setup_buildargs(input_buildargs=buildargs)
        self.kwargs = kwargs
        self.additional_tags = self.kwargs.get("additional_tags", [])
        self.platforms = self._platforms()

        self.image = None


class MultiPlatformDockerImageOnWhales(BasicDockerImageOnWhales):
    def _platforms(self) -> List[str]:
        return self.kwargs.get("platforms") or [
            "linux/amd64",
            "linux/amd64/v2",
            "linux/arm64",
        ]

    def build(
        self,
        docker_credentials: List[Tuple[str, str, str]],
        show_build_log: bool = True,
    ) -> Dict[str, Union[str, List, Dict]]:
        self.log.warning(
            f">> Building {self.image_name} image(s) for the following platform(s): {self.platforms}.."
        )

        _context = docker.buildx.create(driver="docker-container", use=True)

        self.log.debug(f">> Docker credentials: {docker_credentials}.")

        for _creds in docker_credentials:
            login_server, username, token = _creds
            docker.login(server=login_server, username=username, password=token)

            tags = []
            for tag in [*self.additional_tags, "latest", self.tag]:
                tags.append(f"{login_server}/{self.image_name}:{tag}")
            tags = list(set(tags))

            _image = docker.buildx.build(
                context_path=self.context,
                file=f"{self.context}/{self.dockerfile}",
                platforms=self.platforms,
                tags=tags,
                progress=show_build_log,
                build_args=self.buildargs,
                builder=_context,
                provenance=False,
                output={"type": "registry"},
            )

            docker.logout(server=login_server)

        _context.remove()

        return {
            "image_name": self.image_name,
            "platforms": self.platforms,
            "tags": list({*self.additional_tags, "latest", self.tag}),
            "build_args": self.buildargs,
            "image": self.image,
        }


if __name__ == "__main__":
    from arranger_automation_aws.ecr import EcrAccessCredentials

    docker_credentials = [
        EcrAccessCredentials(cluster_name_alias="dev1").ecr_access_credentials()
    ]

    image = MultiPlatformDockerImageOnWhales(
        image_name="on_whales",
        tag="release1",
        context="text_build/",
        dockerfile="Dockerfile",
        additional_tags=["2.2.2"],
    )
    image.build(docker_credentials=docker_credentials)
