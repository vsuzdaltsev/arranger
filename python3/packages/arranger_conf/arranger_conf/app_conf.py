"""Main configuration file."""


class AppConf:
    """Globals."""

    CLUSTERS = {
        "local": {
            "cluster_name": "local-k8s",
        },
        "orchestra2": {
            "aws_account_id": "465525377090",
            "aws_region": "eu-west-2",
            "aws_profile": "orchestra2",
            "context": "",
            "description": "Switch orchestration account.",
            "domain": "",
            "country": "",
            "cloud_attributes": {
                "cloud": "aws",
                "tags": {},
            },
        },
        "sandbox1": {
            "aws_account_id": "724906484045",
            "aws_region": "eu-west-2",
            "cluster_name": "arn:aws:eks:eu-west-2:724906484045:cluster/sandbox1",
            "aws_profile": "sandbox1",
            "context": "",
            "description": "Switch sandbox1 account.",
            "sub_environments": [f"sand{i}" for i in range(1, 3)],
            "domain": "neoswitch.net",
            "country": "",
            "cloud_attributes": {
                "cloud": "aws",
                "tags": {},
            },
        },
        "switchdev1": {
            "aws_account_id": "091969078577",
            "aws_region": "eu-west-2",
            "cluster_name": "arn:aws:eks:eu-west-2:091969078577:cluster/switchdev1",
            "aws_profile": "switchdev1",
            "context": "",
            "description": "Switch development account.",
            "sub_environments": [f"d{i}" for i in range(1, 20)],
            "domain": "switchdev1.com",
            "country": "",
            "cloud_attributes": {
                "cloud": "aws",
                "tags": {},
            },
        },
        "velox": {
            "aws_account_id": "500736630700",
            "aws_region": "eu-west-2",
            "name": "velox",
            "aws_profile": "velox",
            "context": "",
            "description": "Velox account (Management account).",
            "sub_environments": None,
            "domain": "",
            "country": "",
            "cloud_attributes": {
                "cloud": "aws",
                "tags": {},
            },
        },
    }

    CDK8S_KUBERNETES_VERSION = "1.27"
    DEFAULT_ALPINE_IMAGE = "3.16"
    SLACK_CHANNELS = {
        "orchestra2": {
            "test": {"id": "C05GHTN0RLH"},
            "orchestra2-pipelines-public": {
                "id": "C06GMH2DK0D",
            },
        },
        "sandbox1": {
            "test": {"id": "C05GHTN0RLH"},
            "sandbox1-pipelines-public": {
                "id": "C061Z51PC5S",
            },
        },
        "switchdev1": {
            "test": {"id": "C05GHTN0RLH"},
            "switchdev1-pipelines-public": {
                "id": "C05FLJ0DYNA",
            },
        },
    }

    ORCHESTRA_ACCOUNT = "orchestra2"
    ORCHESTRA_SUBORDINATE_ACCOUNTS = ["sandbox1", "switchdev1"]
