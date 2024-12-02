from arranger_automation_aws.client import AwsClient
from arranger_automation_aws.basic_resource import BasicAwsResource


class GlobalAcceleratorVpnHelper(BasicAwsResource):
    def __init__(self, boto_client: AwsClient):
        super().__init__(boto_client=boto_client)
        self.all_lbs = self.all_load_balancers()

    def all_load_balancers(self):
        all_lbs = []
        for page in self.client.get_paginator("describe_load_balancers").paginate():
            all_lbs += page["LoadBalancers"]

        return all_lbs

    def lb_tag(self, lb):
        try:
            return self.client.describe_tags(ResourceArns=[lb["LoadBalancerArn"]])[
                "TagDescriptions"
            ][0]["Tags"]
        # TODO: too broad exception
        except Exception as err:
            raise Exception(f"Can't get tags for lb, {err}.")

    def is_lb_vpn(self, lb):
        for tag in self.lb_tag(lb):
            if (
                tag["Key"] == "kubernetes.io/service-name"
                and "openvpn-external" in tag["Value"]
            ):
                return True

        return False

    def vpn_lb_arns(self, cluster_name: str):
        cluster_tag = {"Key": f"kubernetes.io/cluster/{cluster_name}", "Value": "owned"}
        all_lb_in_clusters = list(
            filter(lambda lb: cluster_tag in self.lb_tag(lb=lb), self.all_lbs)
        )
        all_vpn_lbs = list(filter(lambda lb: self.is_lb_vpn(lb=lb), all_lb_in_clusters))

        return [lb["LoadBalancerArn"] for lb in all_vpn_lbs]


if __name__ == "__main__":
    client = AwsClient(
        name="elbv2", region="eu-west-2", aws_profile="WS-01GF-role_AUTOMATION"
    ).client
    vpn_vb_arns = GlobalAcceleratorVpnHelper(boto_client=client).vpn_lb_arns(
        cluster_name="spec1"
    )
    print(vpn_vb_arns)
