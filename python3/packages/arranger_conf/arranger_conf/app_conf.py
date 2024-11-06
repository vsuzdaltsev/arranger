"""Main configuration file."""


class AppConf:
    """Globals."""

    CLUSTERS = {
        "local": {
            "cluster_name": "local-k8s",
        },
    }

    CDK8S_KUBERNETES_VERSION = "1.27"
    SLACK_CHANNELS = {}



    ORCHESTRA_ACCOUNT = "head1"
    ORCHESTRA_SUBORDINATE_ACCOUNTS = ["staging1", "develop1"]
