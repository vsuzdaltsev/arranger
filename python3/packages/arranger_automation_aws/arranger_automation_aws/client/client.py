"""AWS Client configuration."""

from logging import Logger
from typing import Dict, Union

from botocore.config import Config
from boto3 import client
from boto3 import session

from arranger_automation.log import Log


class AwsClient:
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def _setup_logger(self):
        """Create default logger object to handle logs if none passed in the constructor."""
        return Log().logger(desc=type(self).__name__)

    def __init__(
        self,
        name: str,
        region: str,
        credentials: Union[Dict, None] = None,
        aws_profile: Union[str, None] = None,
        config: Union[Config, None] = None,
        logger: Union[Logger, None] = None,
    ):
        """
        Instantiate a boto3 client with provided settings, error handling and proper logging capabilities.

        :param name: The name of a service, e.g. 's3' or 'ec2'.
        :param region: The name of the region associated with the client. A client is associated with a single region.
        :param credentials: access key id, secret access key, session token, if not provided,
            caller identity credentials will be used.
        :param config: Advanced client configuration options. If region_name is specified in the client config.
        :param logger: Custom logger object, if not provided default one will be used.
        """
        self._logger = logger or self._setup_logger()
        self._name = name
        self._region = region
        self._config = self._setup_client_config(config=config)
        self._aws_profile = aws_profile
        self._credentials = credentials
        self._client = self._setup_client()

    @property
    def client(self):
        return self._client

    @property
    def region(self):
        return self._region

    def _setup_client_config(self, config: Config) -> Union[Config, None]:
        """Configuration for the client."""
        if config:
            self._logger.debug(">> Apply custom config: %s for client.", config)
            return config

    def caller_identity(self) -> str:
        """Get account_id for given credentials."""
        self._logger.debug(">> Providing caller identity for given credentials.")

        return client(
            service_name="sts", **self._setup_credentials()
        ).get_caller_identity()

    def _setup_client(self) -> client:
        """Setup boto3 client."""

        self._logger.debug(">> Creating %s client.", self._name)
        if self._aws_profile:
            return session.Session(profile_name=self._aws_profile).client(
                service_name=self._name, region_name=self._region, config=self._config
            )

        return client(
            service_name=self._name,
            region_name=self._region,
            config=self._config,
            **self._setup_credentials(),
        )

    def _setup_credentials(self) -> Dict:
        """
        Setup AWS credentials. If None passed, caller-identity credentials are used.
        {
            "aws_access_key_id": None,
            "aws_secret_access_key": None,
            "aws_session_token": None
        }.
        """
        if not self._credentials:
            self._logger.debug(">> No credentials passed. Using caller identity.")
            self._credentials = {
                "aws_access_key_id": None,
                "aws_secret_access_key": None,
                "aws_session_token": None,
            }

        return self._credentials
