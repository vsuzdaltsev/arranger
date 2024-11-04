"""Main configuration file."""


class AppConf:
    """Globals."""

    CLUSTERS = {
        "local": {
            "cluster_name": "local-k8s",
        },
    }

    CDK8S_KUBERNETES_VERSION = "1.27"
    DEFAULT_ALPINE_IMAGE = "3.16"
    SLACK_CHANNELS = {}

    ORCHESTRA_ACCOUNT = "orchestra1"
    ORCHESTRA_SUBORDINATE_ACCOUNTS = ["sandbox1", "develop1"]
