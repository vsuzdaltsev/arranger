import json
from typing import Dict, List, Union

from eusy_automation_aws.client import AwsClient


class CognitoHelper:
    DEFAULT_AWS_REGION = None
    DEFAULT_AWS_PROFILE = None
    DEFAULT_USER_POOL_ID = None

    def __init__(
        self, boto_client: type(AwsClient), user_pool_id: Union[str, None] = None
    ):
        self.cognito_client = boto_client

        if user_pool_id:
            self.default_user_pool_id = user_pool_id
        else:
            self.default_user_pool_id = self.DEFAULT_USER_POOL_ID

    def list_all(self, user_pool_id: Union[str, None] = None) -> List[Dict]:
        if not user_pool_id:
            user_pool_id = self.default_user_pool_id

        paginator = self.cognito_client.get_paginator("list_user_pool_clients")

        all_clients = []
        for response in paginator.paginate(UserPoolId=user_pool_id):
            all_clients += response.get("UserPoolClients")

        return all_clients

    def client_id(self, client_name: str, user_pool_id: str = None) -> Union[str, None]:
        if not user_pool_id:
            user_pool_id = self.default_user_pool_id

        all_clients = self.list_all(user_pool_id=user_pool_id)

        for client in all_clients:
            if client.get("ClientName") == client_name:
                return client.get("ClientId")

        return None

    def client_secret(
        self,
        client_name: str,
        user_pool_id: str = None,
    ):
        if not user_pool_id:
            user_pool_id = self.default_user_pool_id

        describe = self.cognito_client.describe_user_pool_client(
            UserPoolId=user_pool_id,
            ClientId=self.client_id(
                client_name=client_name,
                user_pool_id=user_pool_id,
            ),
        )

        return describe.get("UserPoolClient", {}).get("ClientSecret")

    def user_pool_domain(self, user_pool_id: str = None) -> Union[str, None]:
        if not user_pool_id:
            user_pool_id = self.default_user_pool_id

        describe = self.cognito_client.describe_user_pool(UserPoolId=user_pool_id)
        domain = describe.get("UserPool", {}).get("Domain")

        if domain:
            return f"https://{domain}.auth.{self.cognito_client.meta.region_name}.amazoncognito.com"

        return None


class DevelopCognitoHelper(CognitoHelper):
    DEFAULT_AWS_REGION = "eu-west-2"
    DEFAULT_AWS_PROFILE = "WS-00KN-role_AUTOMATION"
    DEFAULT_USER_POOL_ID = "eu-west-2_gcZsPhl99"


if __name__ == "__main__":
    cognito_idp_client = AwsClient(
        name="cognito-idp", region="eu-west-2", aws_profile="WS-015M-role_AUTOMATION"
    ).client

    print(
        json.dumps(
            CognitoHelper(
                boto_client=cognito_idp_client, user_pool_id="eu-west-2_536n7GwV1"
            ).list_all()
        )
    )
    print(
        CognitoHelper(boto_client=cognito_idp_client).client_id(
            client_name="develop3-cognito-user-pool-client",
            user_pool_id="eu-west-2_536n7GwV1",
        )
    )
    print(
        CognitoHelper(boto_client=cognito_idp_client).client_secret(
            client_name="develop3-cognito-user-pool-client",
            user_pool_id="eu-west-2_536n7GwV1",
        )
    )
