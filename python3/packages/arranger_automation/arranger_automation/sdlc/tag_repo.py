"""Push tags into repo."""

import os
from typing import Optional

from arranger_automation.log import Log

from .sem_ver import SemVer


class TagRepo:
    """Update repo's tag."""

    GIT_EMAIL = "vsevolod.suzdaltsev@gmail.com"
    GIT_USER = "automation"

    def __init__(
        self,
        sem_ver: SemVer,
        git_ref: str,
        repo_root_dir: Optional[str] = ".",
        split_file_path: Optional[bool] = False,
        force_push: bool = False,
    ):
        self.log = Log().logger(desc=type(self).__name__)
        self.git_ref = git_ref
        self.repo_root_dir = repo_root_dir
        self.sem_ver = sem_ver
        self.file_path = self._file_path(split_file_path=split_file_path)
        self.force_push = force_push

    def _file_path(self, split_file_path) -> str:
        file_path = self.sem_ver.version_file_path

        if split_file_path:
            file_path = file_path.replace(f"{self.repo_root_dir}/", "")

        return file_path

    @property
    def _force_push_prefix(self):
        if self.force_push:
            return "--force"

        return ""

    def with_new_version(self) -> str:
        """Generate new version and tag the repo."""
        os.chdir(self.repo_root_dir)
        self.log.warning(">> Configure git use email")
        os.system(f"git config --global user.email {self.GIT_EMAIL}")
        os.system(f"git config --global user.name {self.GIT_USER}")

        os.system(f"git checkout {self.git_ref}")

        new_ver = ".".join(map(str, list(self.sem_ver.write_new_version().values())))

        self.log.warning(">> Add file to git stage area")
        os.system(f"git add {self.file_path}")

        self.log.warning(">> Git commit")
        os.system(f"git commit -m 'bump to {new_ver}'")

        self.log.warning(">> Git tag")
        os.system(f"git tag {new_ver}")

        self.log.warning(
            ">> Git push origin %s %s.", self.git_ref, self._force_push_prefix
        )
        os.system(f"git push origin {self.git_ref} {self._force_push_prefix}")

        self.log.warning(">> Git push --tags %s.", self._force_push_prefix)
        os.system(f"git push --tags {self._force_push_prefix}")

        return new_ver


if __name__ == "__main__":
    from version_file import GenericVersionFile

    TagRepo(
        sem_ver=SemVer(version_file=GenericVersionFile()), git_ref=""
    ).with_new_version()
