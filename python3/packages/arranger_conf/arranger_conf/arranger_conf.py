"""Main configuration file."""


class ArrangerConf:
    """Globals."""

    PROJECT_NAME = "my_first_arranger_project"  # Global randomizer

    TENANTS = {
        "development1": {
            "aws_account_id": "<>",
            "aws_region": "us-east-1",
            "cluster_name": "arn:aws:eks:<>>:<>:cluster/development1",
            "aws_profile": "development1",
            "context": "",
            "description": "Development account #1.",
            "sub_environments": [f"d{i}" for i in range(1, 20)],
            "domain": "development1.io",
            "cloud_attributes": {
                "cloud": "aws",
                "tags": {},
            },
        },
        "local": {
            "cluster_name": "local-k8s",
        },
        "staging1": {
            "cluster_name": "local-k8s",
        },
    }

    CDK8S_KUBERNETES_VERSION = "1.27"

    HEAD_ACCOUNT = None
    SUBORDINATE_ACCOUNTS = ["staging1", "development1"]
    DEFAULT_ALPINE_IMAGE = "3.16"
