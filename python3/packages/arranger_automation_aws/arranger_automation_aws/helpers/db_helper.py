from typing import Dict

from eusy_automation_aws.client import AwsClient
from eusy_automation_aws.basic_resource import BasicAwsResource


class DBHelper(BasicAwsResource):
    def __init__(self, boto_client: type(AwsClient), cluster_name: str):
        super().__init__(boto_client=boto_client)
        self._cluster_name = cluster_name
        self._endpoint = None
        self._cluster_metadata = self._cluster_metadata()

    @property
    def db_host(self) -> str:
        return self._endpoint

    def _cluster_metadata(self) -> Dict:
        paginator = self.client.get_paginator("describe_db_clusters")
        response_iterator = paginator.paginate(DBClusterIdentifier=self._cluster_name)

        for item in response_iterator:
            cluster_data = item.get("DBClusters")[0]
            self._endpoint = cluster_data.get("Endpoint")

            return cluster_data


if __name__ == "__main__":
    client = AwsClient(
        name="rds", region="eu-west-2", aws_profile="WS-011C-role_AUTOMATION"
    ).client
    result = DBHelper(boto_client=client, cluster_name="uat3-cluster").db_host
    print(result)
