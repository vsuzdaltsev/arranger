from typing import List, Union

from arranger_automation_aws.basic_resource import BasicAwsResource
from arranger_automation_aws.client import AwsClient


class CloudFrontHelper(BasicAwsResource):
    def __init__(self, boto_client: type(AwsClient)):
        super().__init__(boto_client=boto_client)
        self._distributions = self._get_distributions()

    def distribution_id_by_description(self, description: str) -> Union[str, None]:
        for distribution in self._distributions:
            if description == distribution.get("Comment"):
                return distribution.get("Id")

    def distribution_id_by_alternative_domain(
        self, alternative_domain: str
    ) -> Union[str, None]:
        for distribution in self._distributions:
            if alternative_domain in distribution.get("Aliases", {}).get("Items", []):
                return distribution.get("Id")

    def url_by_description(self, description: str) -> Union[str, None]:
        for distribution in self._distributions:
            if description == distribution.get("Comment"):
                return distribution.get("DomainName")

    def url_by_alternative_domain(self, alternative_domain: str) -> Union[str, None]:
        for distribution in self._distributions:
            if alternative_domain in distribution.get("Aliases", {}).get("Items", []):
                return distribution.get("DomainName")

    def _get_distributions(self) -> List[dict]:
        paginator = self.client.get_paginator("list_distributions")
        response_iterator = paginator.paginate()

        distributions = []
        for item in response_iterator:
            distributions += item.get("DistributionList")["Items"]

        return distributions

    def _get_public_keys(self):
        return self.client.list_public_keys()["PublicKeyList"]["Items"]

    def public_key_id_by_name(self, name):
        for key in self._get_public_keys():
            if key.get("Name") == name:
                return key.get("Id")

        raise RuntimeError(f"Can't find public key with name {name}.")


if __name__ == "__main__":
    client = AwsClient(
        name="cloudfront", region="eu-west-2", aws_profile="WS-011C-role_AUTOMATION"
    ).client
    result = CloudFrontHelper(boto_client=client).url_by_description(
        "Dealer portal for uat3."
    )
    print(result)
    result = CloudFrontHelper(boto_client=client).url_by_alternative_domain(
        "orders-service.somedomain.cc"
    )
    print(result)
    result = CloudFrontHelper(boto_client=client).public_key_id_by_name(
        name="billing-cloudfront-pubkey-uat3"
    )
    print(result)
