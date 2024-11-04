"""Version file management."""

from abc import ABC, abstractmethod
from typing import Dict, Iterator, NoReturn


class BasicVersionFile(ABC):
    """Manage version file."""

    PATCH_TYPES = ("major", "minor", "patch")

    def __init__(self, file=None):
        self.file = self._where_file(file)

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    @abstractmethod
    def _where_file(self, file: str) -> str:
        raise NotImplementedError

    @staticmethod
    def _values(contents: str) -> Iterator:
        return map(int, contents.strip().split('"')[-2].split("."))

    def get_version(self) -> Dict:
        """Read version."""
        with open(self.file, "r") as file:
            contents = file.read()
            keys = self.PATCH_TYPES
            values = self._values(contents)

        return dict(zip(keys, list(values)))


class CommonVersionFile(BasicVersionFile):
    @staticmethod
    def _values(contents: str) -> Iterator:
        return map(int, contents.strip().split("."))

    def set_version(self, new_version: Dict[str, int]) -> NoReturn:
        """Write version."""
        with open(self.file, "w") as file:
            file.write(".".join(list(map(str, new_version.values()))) + "\n")

    def _where_file(self, file):
        return file
