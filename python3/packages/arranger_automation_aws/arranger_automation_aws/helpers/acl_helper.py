from typing import List

from boto3 import session as ses


class AclHelper:
    @classmethod
    def client(cls, profile, aws_region):
        return ses.Session(profile_name=profile, region_name=aws_region).client("ec2")

    @classmethod
    def network_acls(cls, profile: str, region: str, subnets: List[str]) -> List[str]:
        """Discover list of acl ids by subnet ids."""
        result = set()
        paginator = cls.client(profile=profile, aws_region=region).get_paginator(
            "describe_network_acls"
        )
        page_iterator = paginator.paginate(
            Filters=[
                {"Name": "association.subnet-id", "Values": subnets},
            ]
        )

        for item in page_iterator:
            for acl in item.get("NetworkAcls"):
                result.add(acl.get("NetworkAclId"))

        return list(result)


if __name__ == "__main__":
    acls = AclHelper().network_acls(
        region="eu-west-2",
        profile="WS-015M-role_AUTOMATION",
        subnets=[
            "subnet-04597d56ef24f5bdb",
            "subnet-074913688791c0cd4",
            "subnet-04860226b27e69cfd",
        ],
    )
    print(acls)
