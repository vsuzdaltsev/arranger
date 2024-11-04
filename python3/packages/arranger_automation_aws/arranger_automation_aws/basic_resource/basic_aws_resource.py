"""Basic functionality for any AWS resource."""

from logging import Logger
from typing import Union

from boto3 import client

from eusy_automation.log import Log


class BasicAwsResource:
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def _setup_logger(self):
        """Create default logger object to handle logs if none passed in the constructor."""
        return Log().logger(desc=type(self).__name__)

    def __init__(self, boto_client: type(client), logger: Union[Logger, None] = None):
        self._logger = logger or self._setup_logger()
        self._client = boto_client

    @property
    def logger(self):
        return self._logger

    @property
    def client(self) -> type(client):
        return self._client
