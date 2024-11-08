"""Semantic versioning helper."""

from typing import Dict


class SemVer:
    """
    Update version file according to SemVer.

    Example:
        SemVer(version_file=CommonVersionFile()).write_new_version()
    """

    PATCH_TYPES = ("major", "minor", "patch")

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def _bump(self) -> Dict[str, int]:
        """Update current version according to incoming parameters."""
        self.current_version[self.increment_type] += 1
        if self.increment_type != "patch":
            self.current_version["patch"] = 0
        if self.increment_type == "major":
            self.current_version["minor"] = 0

        return self.current_version

    def _read_current_version(self):
        return self.version_file.get_version()

    def __init__(self, version_file, increment_type="patch"):
        if increment_type not in self.PATCH_TYPES:
            raise ValueError(f"Patch type must be one of: {self.PATCH_TYPES}.")

        self.version_file = version_file
        self.current_version = self._read_current_version()
        self.increment_type = increment_type

    @property
    def version_file_path(self):
        """Path to file with version number."""
        return self.version_file.file

    def write_new_version(self) -> Dict:
        """Write new version to version file."""
        self.version_file.set_version(new_version=self._bump())

        return self.current_version


if __name__ == "__main__":
    from version_file import CommonVersionFile

    SemVer(version_file=CommonVersionFile()).write_new_version()
