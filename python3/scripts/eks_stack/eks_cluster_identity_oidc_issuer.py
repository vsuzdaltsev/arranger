import json
import sys

from eusy_automation_aws.client import AwsClient
from eusy_automation_aws.helpers.eks_helper import EksHelper
from eusy_conf.app_conf import AppConf
from eusy_globals import ByClusterNameAlias


if __name__ == "__main__":
    cluster_name_alias = sys.argv[1]

    assert cluster_name_alias in AppConf.CLUSTERS

    _globals = ByClusterNameAlias(cluster_name_alias=cluster_name_alias)
    eks = AwsClient(
        name="eks", region=_globals.aws_region, aws_profile=cluster_name_alias
    ).client
    result = EksHelper(boto_client=eks, cluster_name=cluster_name_alias)

    print(json.dumps({"ENDPOINT_ID": result.endpoint_id}))
