from typing import Dict, List, Union

from arranger_automation_aws.basic_resource import BasicAwsResource
from arranger_automation_aws.client import AwsClient


class MskHelper(BasicAwsResource):
    def __init__(self, boto_client: AwsClient, cluster_name: str):
        super().__init__(boto_client=boto_client)

        self._cluster_name = cluster_name

        self._cluster_metadata = self._cluster_metadata()
        self.broker_endpoints = self._list_broker_endpoints()

    @property
    def kafka_addr(self) -> str:
        return ",".join(self.broker_endpoints)

    def kafka_brokers(
        self, port: Union[str, int] = 9092, protocol_prefix: bool = True
    ) -> str:
        prefix = "kafka://" if protocol_prefix else ""

        return ",".join([f"{prefix}{item}:{port}" for item in self.broker_endpoints])

    def kafka_zookeeper_connect_string(self):
        return sorted(
            self._cluster_metadata.get("ZookeeperConnectString", "").split(",")
        )

    def _cluster_metadata(self) -> Dict:
        paginator = self.client.get_paginator("list_clusters")
        response_iterator = paginator.paginate(ClusterNameFilter=self._cluster_name)

        for item in response_iterator:
            cluster_data = item.get("ClusterInfoList")[0]
            self._cluster_arn = cluster_data.get("ClusterArn")

            return cluster_data

    def _list_broker_endpoints(self) -> List[str]:
        broker_endpoints = []
        broker_nodes = self.client.list_nodes(ClusterArn=self._cluster_arn).get(
            "NodeInfoList"
        )
        for node in broker_nodes:
            broker_endpoints.append(*node.get("BrokerNodeInfo").get("Endpoints"))

        return sorted(broker_endpoints)

    @property
    def bootstrap_broker_string(self):
        return self.client.get_bootstrap_brokers(ClusterArn=self._cluster_arn).get(
            "BootstrapBrokerString"
        )


if __name__ == "__main__":
    client = AwsClient(
        name="kafka", region="eu-west-2", aws_profile="development1"
    ).client
    result = MskHelper(
        boto_client=client, cluster_name="kafka-cluster-development1"
    ).kafka_brokers(protocol_prefix=False)
    print(result)
