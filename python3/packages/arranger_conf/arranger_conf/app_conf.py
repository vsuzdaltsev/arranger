"""Main configuration file."""


class AppConf:
    """Globals."""

    PROJECT_NAME = "my_project" # Randomizer

    TENANTS = {
        "development1": {
            "aws_account_id": "<>",
            "aws_region": "eu-west-2",
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

    ORCHESTRA_ACCOUNT = "head1"
    ORCHESTRA_SUBORDINATE_ACCOUNTS = ["staging1", "development1"]
