"""Authenticate using AWS STS mechanism."""

from typing import Any, Dict
import uuid

from arranger_automation_aws.basic_resource import BasicAwsResource
from arranger_automation_aws.client import AwsClient


class StsCredentials(BasicAwsResource):
    """Get STS credentials to call API on behalf of given role."""

    def __init__(
        self,
        role_arn: str,
        client: AwsClient.client,
        duration_seconds: int = 3600,
    ):
        """
        :param role_arn: AWS Role ARN to use for getting credentials.
        :param duration_seconds: Credentials duration in seconds.
        """
        super().__init__(boto_client=client)

        self.__role_arn = role_arn
        self.__uuid = str(uuid.uuid4())
        self.__duration_seconds = duration_seconds

    def credentials(self) -> Dict:
        """Credentials dict."""
        credentials = self.credentials_raw()

        return {
            "aws_access_key_id": credentials["AccessKeyId"],
            "aws_secret_access_key": credentials["SecretAccessKey"],
            "aws_session_token": credentials["SessionToken"],
        }

    def credentials_raw(self) -> Dict:
        """Raw credentials."""
        return self.response()["Credentials"]

    def response(self) -> Dict:
        """Assume role."""
        self._logger.debug(">> Get Sts credentials")
        return self._client.assume_role(
            RoleArn=self.__role_arn,
            RoleSessionName="sts-" + self.__uuid,
            DurationSeconds=self.__duration_seconds,
        )

    def write_to_env_file(self, path_to_file: str = ".envrc") -> None:
        """
        Write credentials to environment file.

        :param path_to_file: Path to environment file.
        """
        contents = self.credentials()

        try:
            with open(path_to_file, "w") as file:
                for string in contents.items():
                    file.write(f'export {string[0].upper()}="{string[1]}"\n')
        except BaseException as err:
            self._logger.error(
                ">> Can't write credentials to file: %s. Error: %s",
                path_to_file,
                str(err),
            )
            raise RuntimeError from err
