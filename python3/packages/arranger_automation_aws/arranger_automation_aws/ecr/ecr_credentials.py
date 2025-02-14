from typing import Tuple


class EcrAccessCredentials:
    def __init__(
        self,
        tenant: str,
    ):
        self.tenant = tenant

    def ecr_access_credentials(self) -> Tuple[str, str, str]:
        import base64
        from urllib.parse import urlparse

        from arranger_automation_aws.client import AwsClient
        from arranger_globals.cdktf_globals import CdktfGlobals

        _globals = CdktfGlobals(tenant=self.tenant)
        _region = _globals.aws_region
        _aws_profile = _globals.aws_profile

        ecr = AwsClient(name="ecr", region=_region, aws_profile=_aws_profile)

        metadata = ecr.client.get_authorization_token()["authorizationData"][0]

        token = metadata["authorizationToken"]

        username, password = base64.b64decode(token).decode().split(":")
        registry = metadata["proxyEndpoint"]

        login_server = urlparse(registry).netloc
        return login_server, username, password


if __name__ == "__main__":
    creds = EcrAccessCredentials(tenant="development1")
    acr_access_token = creds.ecr_access_credentials()

    print("ECR Access Credentials:", acr_access_token)
