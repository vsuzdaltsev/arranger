"""Retrieve items from AWS Secrets Manager."""

import base64
import json
from typing import Dict, Union

from boto3 import client as sm
from boto3 import session as sm_session
from botocore.exceptions import ClientError

from eusy_automation_aws.credentials import DefaultCredentials
from eusy_automation.log import Log


class SecretsManagerItem:
    """
    Retrieve specified item from AWS Secret Manager.

    Example:

        :::python
        sm_item=SecretsManagerItem(
            secret_name='project_creds_identifier',
            region_name='us-east-1',
            profile="WS-00YS-role_AUTOMATION"
        )
        sm_item.retrieve()
    """

    @classmethod
    def log(cls):
        """Setup logger object."""
        return Log().logger(desc=cls.__name__)

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(
        self,
        secret_name: Union[str, None] = None,
        region_name: str = "eu-west-2",
        credentials: Union[Dict, None] = None,
        aws_profile: str = None,
    ):
        """
        Parameters:

        * **secret_name**: Name of a specific item in AWS Secret Manager.
        * **region_name**: Region of AWS Secret Manager.
        """
        self._secret_name = secret_name
        self._region_name = region_name
        self._aws_profile = aws_profile
        self._session_client = self._setup_client(credentials)

    def _setup_client(self, credentials):
        nil_creds = (
            credentials is None or credentials == DefaultCredentials().credentials()
        )

        if not nil_creds:
            return sm("secretsmanager", region_name=self._region_name, **credentials)

        if self._aws_profile:
            return sm_session.Session(profile_name=self._aws_profile).client(
                "secretsmanager", region_name=self._region_name
            )

        raise ValueError(
            ">> Either AWS Creds or AWS Profile must be passed to the SM client."
        )

    def retrieve(self) -> Dict:
        """
        Retrieve **item** by **self._secret_name** from AWS Secret Manager.
        Decode secret string from item.
        Convert item's secret string from json to **dict**.

        Return:
        * **dict**: dict structure depends on item's secret string structure.
        """
        secret_name = self._secret_name
        try:
            get_secret_value_response = self._session_client.get_secret_value(
                SecretId=secret_name
            )
            if "SecretString" in get_secret_value_response:
                secret = get_secret_value_response["SecretString"]
            else:
                secret = base64.b64decode(get_secret_value_response["SecretBinary"])

            if secret is None:
                raise ValueError(f">> {__class__.__name__}: secret not found.")

            return json.loads(secret)

        except ClientError as err:
            if err.response["Error"]["Code"] == "DecryptionFailureException":
                raise err
            if err.response["Error"]["Code"] == "InternalServiceErrorException":
                raise err
            if err.response["Error"]["Code"] == "InvalidParameterException":
                raise err
            if err.response["Error"]["Code"] == "InvalidRequestException":
                raise err
            if err.response["Error"]["Code"] == "ProfileNotFound":
                raise err
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                raise Exception(
                    f">> {__class__.__name__}#retrieve: {self._secret_name}. Error: {str(err)}."
                ) from err
        except BaseException as err:
            raise Exception(
                f">> {__class__.__name__}/{self._secret_name}: {str(err)}."
            ) from err

    def secret_arn(self) -> str:
        """
        Describe secrets and get the secret'sARN

        Return:
        * **string**: secret's ARN.
        """
        secret_name = self._secret_name
        try:
            get_secret_description = self._session_client.describe_secret(
                SecretId=secret_name
            )
            arn = get_secret_description.get("ARN")

            if arn is None:
                raise ValueError(f">> {__class__.__name__}: secret not found.")

            return arn

        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                raise Exception(
                    f">> {__class__.__name__}#retrieve: {self._secret_name}. Error: {str(err)}."
                ) from err
            raise err
