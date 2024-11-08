from time import sleep
from typing import Dict, List

from boto3 import client

from arranger_automation_aws.basic_resource import BasicAwsResource
from arranger_automation_aws.client import AwsClient


# TODO: refactor. Use built-in waiters?
# TODO: use logger instead of print()
class RedisHelper(BasicAwsResource):
    def _cluster_status_waiter(self, retries: int):
        status = None

        while status != "available":
            retries = retries - 1
            if retries != 0:
                sleep(15)
                status = self._response_handler().get("CacheClusterStatus")
                print(f"Retries left: {retries}. Status: {status}")
            else:
                print(
                    f"{self.cluster_id} reboot taking longer than expected. Please check cluster manually."
                )

        print(f"{self.cluster_id} data dropped successfully.")

    def _response_handler(self) -> Dict:
        response_iterator = self.paginator.paginate(
            CacheClusterId=self.cluster_id, ShowCacheNodeInfo=True
        )

        for item in response_iterator:
            if item.get("CacheClusters"):
                return item.get("CacheClusters")[0]

    def __init__(self, boto_client: type(client), cluster_id: str):
        super().__init__(boto_client=boto_client)

        self.cluster_id = cluster_id
        self.paginator = self.client.get_paginator("describe_cache_clusters")

    def get_list_node_endpoints(self) -> List[str]:
        cluster_data = self._response_handler()
        nodes = cluster_data.get("CacheNodes", [])
        list_endpoints = []

        for node in nodes:
            endpoint = f"{node.get('Endpoint').get('Address')}:{node.get('Endpoint').get('Port')}"
            list_endpoints.append(endpoint)

        return sorted(list_endpoints)

    def get_redis_cache_servers(self, custom_url_path: str = "") -> str:
        list_endpoints = self.get_list_node_endpoints()

        if custom_url_path and not custom_url_path.startswith("/"):
            custom_url_path = f"/{custom_url_path}"

        redis_cache_servers = [
            f"redis://{endpoint}{custom_url_path}" for endpoint in list_endpoints
        ]

        return ",".join(sorted(redis_cache_servers))

    def reboot_cluster(self, cache_nodes_ids: List[str]):
        self.client.reboot_cache_cluster(
            CacheClusterId=self.cluster_id, CacheNodeIdsToReboot=cache_nodes_ids
        )

        return self._cluster_status_waiter(retries=15)

    def get_node_ids(self):
        cluster_data = self._response_handler()
        nodes = cluster_data.get("CacheNodes", [])

        return sorted([f"{node.get('CacheNodeId')}" for node in nodes])


if __name__ == "__main__":
    test = RedisHelper(
        cluster_id="develop3-redis-d9",
        boto_client=AwsClient(
            name="elasticache",
            region="eu-west-2",
            aws_profile="WS-015M-role_AUTOMATION",
        ).client,
    )

    print(test.get_list_node_endpoints())
    print(test.get_node_ids())
