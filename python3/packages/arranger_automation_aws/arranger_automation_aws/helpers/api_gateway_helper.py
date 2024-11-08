from urllib.parse import urlparse

from boto3 import session as ses


class ApiGatewayHelper:
    @classmethod
    def client(cls, profile, aws_region):
        return ses.Session(profile_name=profile, region_name=aws_region).client(
            "apigatewayv2"
        )

    @classmethod
    def api_object(cls, api_name: str, profile: str, region: str):
        paginator = cls.client(profile=profile, aws_region=region).get_paginator(
            "get_apis"
        )
        for page in paginator.paginate():
            for api in page.get("Items"):
                if api.get("Name") == api_name:
                    return api
        return None

    @classmethod
    def api_endpoint(
        cls, api_name: str, profile: str, region: str, schema: bool = False
    ):
        paginator = cls.client(profile=profile, aws_region=region).get_paginator(
            "get_apis"
        )
        for page in paginator.paginate():
            for api in page.get("Items"):
                if api.get("Name") == api_name:
                    if schema:
                        return api.get("ApiEndpoint")
                    return urlparse(api.get("ApiEndpoint")).netloc
        return None
