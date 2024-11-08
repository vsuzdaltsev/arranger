import re
from typing import List, Dict

from boto3 import session as ses


class SubnetHelper:
    FIREWALL_SUBNET_PREFIX = "AWSFirewallManagerManagedResource"

    @classmethod
    def client(cls, profile, aws_region):
        return ses.Session(profile_name=profile, region_name=aws_region).client("ec2")

    @classmethod
    def list_subnets_by_name_filter(
        cls, profile: str, region: str, filter_by: str
    ) -> List[Dict[str, str]]:
        """Discover list of public subnets by postfix of name."""
        result = []
        paginator = cls.client(profile=profile, aws_region=region).get_paginator(
            "describe_subnets"
        )
        page_iterator = paginator.paginate()

        def get_tag_name(tags: List[Dict[str, str]]) -> str:
            for tag in tags:
                if tag.get("Key") == "Name":
                    return tag.get("Value")

            return ""

        for item in page_iterator:
            for subnet in item.get("Subnets"):
                subnet_name = get_tag_name(subnet.get("Tags", {}))

                res = re.search(rf"{filter_by}", subnet_name)

                if res:
                    result.append(subnet)

        return result

    @classmethod
    def public_subnet_ids(cls, profile: str, region: str, filter_by: str) -> List[str]:
        subnets = cls.list_subnets_by_name_filter(profile, region, filter_by)

        return [subnet.get("SubnetId") for subnet in subnets]


if __name__ == "__main__":
    public_subnet_ids = SubnetHelper().public_subnet_ids(
        region="eu-west-2",
        profile="switchdev1",
        filter_by="vpc-main-subnet-.*-switchdev1-private",
    )
    print(public_subnet_ids)
