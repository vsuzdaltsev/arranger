import os
from typing import NoReturn, Union

from git import exc, Repo, Submodule

from arranger_automation.log import Log


class CannotCheckoutToGivenRef(BaseException):
    pass


class BasicGitRepo:
    UPDATE_SUBMODULES = False

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(self, git_project: str, repo_name: str):
        self.git_pat_env_variable_name = "GITLAB_PAT"
        self.git_pat = os.getenv(self.git_pat_env_variable_name)

        self.log = Log().logger(desc=self.__class__.__name__)
        self.repo = None
        self.git_project = git_project
        self.repo_name = repo_name
        self.git_url = f"{self._base_url()}/{self.repo_name}"

    def clone(self, where: str, update_submodules=None) -> NoReturn:
        if update_submodules is None:
            update_submodules = self.UPDATE_SUBMODULES

        self.log.warning(
            f">> Trying to clone '{self.repo_name}' "
            f"repo with update_submodules={update_submodules}.."
        )
        self.repo = Repo.clone_from(url=self.git_url, to_path=where)
        self._get_submodules(update_submodules=update_submodules)

    def checkout(self, git_ref: str, update_submodules=None) -> NoReturn:
        if update_submodules is None:
            update_submodules = self.UPDATE_SUBMODULES

        try:
            self.log.warning(
                f">> Trying to checkout '{self.repo_name}' repo to '{git_ref}' "
                f"git ref with update_submodules={update_submodules}.."
            )
            result = self.repo.git.checkout(git_ref)
            self._get_submodules(update_submodules=update_submodules)
            self.log.warning(
                f">> Result of checkout '{self.repo_name}' to {git_ref}: {result}."
            )
        except exc.GitCommandError as err:
            raise CannotCheckoutToGivenRef(
                f">> Repo '{self.repo_name}' doesn't have '{git_ref}' git ref. "
                f"Remaining on local branch '{self.repo.active_branch.name}'.. "
                f"Commit sha: {self.current_commit_sha()}."
            ) from err

    def current_commit_sha(self, short_notation: bool = False) -> Union[str, NoReturn]:
        def sha():
            if short_notation:
                return self.repo.head.object.hexsha[0:7]
            return self.repo.head.object.hexsha

        try:
            return sha()
        except ValueError:
            self._notify_repo_is_empty()

    def _clone_from_local_copy(
        self, where_local_repo: str, where: str, update_submodules=None
    ) -> NoReturn:
        """This method should work but not tested yet."""
        if update_submodules is None:
            update_submodules = self.UPDATE_SUBMODULES

        self.repo = Repo.clone_from(url=where_local_repo, to_path=where)

        self._get_submodules(update_submodules=update_submodules)

    def _get_submodules(self, update_submodules: bool) -> NoReturn:
        if update_submodules:
            for submodule in self.repo.submodules:
                submodule._url = self._submodule_url_with_creds(submodule=submodule)
                submodule.update(
                    init=True,
                )

    def _base_url(self) -> str:
        if not self.git_project:
            raise ValueError("Git project should not be None.")

        return f"https://{self._credentials()}git.velox-solution.com/{self.git_project}"

    def _credentials(self) -> str:
        raise NotImplementedError("Not implemented yet..")

    def _submodule_url_with_creds(self, submodule: type(Submodule)) -> str:
        return f"{self._base_url()}/{submodule.url.split('/')[-1]}"

    def _notify_repo_is_empty(self) -> NoReturn:
        self.log.error(
            f">> Repo '{self.repo_name}' doesn't have any commits. The repo is empty."
        )


class BasicGitlabRepo(BasicGitRepo):
    def _credentials(self) -> str:
        self.log.debug(f">> {self.git_pat_env_variable_name} is {self.git_pat}.")

        if not self.git_pat:
            err_msg = (
                f"{self.git_pat_env_variable_name} environment variable is not set."
            )
            self.log.error(err_msg)
            raise EnvironmentError(err_msg)

        return f"gitlab-ci-token:{self.git_pat}@"

    def _base_url(self) -> str:
        if not self.git_project:
            raise ValueError("Git project should not be None.")

        return f"https://{self._credentials()}git.velox-solution.com/{self.git_project}"


class BasicGitcommitRepo(BasicGitRepo):
    def __init__(self, repo_name: str, aws_region: Union[str, None]):
        self.git_pat_env_variable_name = "CODECOMMIT_PAT"
        self.git_pat = os.getenv(self.git_pat_env_variable_name)

        self.log = Log().logger(desc=self.__class__.__name__)
        self.aws_region = self._setup_aws_region(input_aws_region=aws_region)
        self.repo_name = repo_name
        self.git_url = f"{self._base_url()}/{self.repo_name}"

    @staticmethod
    def _setup_aws_region(input_aws_region: str):
        if input_aws_region:
            return input_aws_region

        raise ValueError("AWS region can't be None")

    def _credentials(self) -> str:
        self.log.debug(f">> {self.git_pat_env_variable_name} is {self.git_pat}.")

        if not self.git_pat:
            err_msg = (
                f"{self.git_pat_env_variable_name} environment variable is not set."
            )
            self.log.error(err_msg)
            raise EnvironmentError(err_msg)

        return f"{self.git_pat}@"

    def _base_url(self) -> str:
        return f"https://{self._credentials()}git-codecommit.{self.aws_region}.amazonaws.com/v1/repos"
