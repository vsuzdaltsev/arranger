import re
from typing import List, Dict

from boto3 import session as ses


class VpcEndpointHelper:
    def __init__(self, aws_profile, aws_region):
        self.aws_profile = aws_profile
        self.aws_region = aws_region
        self.client = self._client()

    def _client(self):
        return ses.Session(
            profile_name=self.aws_profile, region_name=self.aws_region
        ).client("ec2")

    def vpc_endpoints(self, filter_by: str) -> List[Dict[str, str]]:
        """Discover list of public subnets by postfix of name."""
        result = []
        paginator = self.client.get_paginator("describe_vpc_endpoints")
        page_iterator = paginator.paginate()

        def get_tag_name(tags: List[Dict[str, str]]) -> str:
            for tag in tags:
                if tag.get("Key") == "Name":
                    return tag.get("Value")

            return ""

        for item in page_iterator:
            for vpc_endpoint in item.get("VpcEndpoints"):
                endpoint_name = get_tag_name(vpc_endpoint.get("Tags", {}))
                res = re.search(rf"{filter_by}", endpoint_name)

                if res:
                    result.append(vpc_endpoint)

        return result

    def dns_entries(self, filter_by: str) -> List:
        dns_records = []
        for item in self.vpc_endpoints(filter_by=filter_by):
            dns_records.extend(item.get("DnsEntries"))

        return sorted([next(iter(dns.values())) for dns in dns_records])


if __name__ == "__main__":
    import json

    helper = VpcEndpointHelper(
        aws_region="eu-west-2",
        aws_profile="development1",
    )
    dns_entries = helper.dns_entries(filter_by="aws-keyspaces-vpc-endpoint-development1")
    print(
        f">> VPC ENDPOINTS: {json.dumps(helper.vpc_endpoints(filter_by=''), default=str)}"
    )
    print(f">> DNS ENTRIES: {json.dumps(dns_entries, default=str)}")
