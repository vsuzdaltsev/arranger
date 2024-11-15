import json
import sys

from arranger_automation_aws.client import AwsClient
from arranger_automation_aws.helpers.eks_helper import EksHelper
from arranger_conf import ArrangerConf
from arranger_globals import ByTenant


if __name__ == "__main__":
    tenant = sys.argv[1]

    assert tenant in ArrangerConf.TENANTS

    _globals = ByTenant(tenant=tenant)
    eks = AwsClient(name="eks", region=_globals.aws_region, aws_profile=tenant).client
    result = EksHelper(boto_client=eks, cluster_name=tenant)

    print(json.dumps({"ENDPOINT_ID": result.endpoint_id}))
