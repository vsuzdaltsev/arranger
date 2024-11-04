from typing import Dict
from urllib.parse import urlparse

from arranger_automation_aws.client import AwsClient
from arranger_automation_aws.basic_resource import BasicAwsResource


class EksHelper(BasicAwsResource):
    def __init__(self, boto_client: type(AwsClient), cluster_name: str):
        super().__init__(boto_client=boto_client)

        self.cluster_name = cluster_name
        self.cluster_metadata = self._cluster_metadata()

    def _cluster_metadata(self) -> Dict:
        return self.client.describe_cluster(name=self.cluster_name)

    @property
    def identity_oidc_issuer(self):
        return self.cluster_metadata["cluster"]["identity"]["oidc"]["issuer"]

    @property
    def endpoint(self):
        return self.cluster_metadata["cluster"]["endpoint"]

    @property
    def endpoint_id(self):
        return urlparse(self.endpoint).netloc.split(".")[0]


if __name__ == "__main__":
    import json

    client = AwsClient(name="eks", region="eu-west-2", aws_profile="switchdev1").client
    result = EksHelper(boto_client=client, cluster_name="switchdev1")

    print(json.dumps({"URL": result.endpoint_id}))
