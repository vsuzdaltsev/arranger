from boto3 import session as ses


class Route53Helper:
    @classmethod
    def client(cls, profile: str):
        return ses.Session(profile_name=profile).client("route53")

    @classmethod
    def hosted_zone_id(cls, zone_name, profile):
        paginator = cls.client(profile=profile).get_paginator("list_hosted_zones")

        for page in paginator.paginate():
            for zone in page.get("HostedZones"):
                if zone.get("Name") == f"{zone_name}.":
                    return zone.get("Id")

        return None

    @classmethod
    def hosted_zone_nameservers(cls, zone_name: str, profile: str):
        response = cls.client(profile=profile).get_hosted_zone(
            Id=cls.hosted_zone_id(zone_name=zone_name, profile=profile)
        )
        return response.get("DelegationSet", []).get("NameServers")
