"""Main configuration file."""


class AppConf:
    """Globals."""

    CLUSTERS = {
        "develop1": {
            "cluster_name": "local-k8s",
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
    ORCHESTRA_SUBORDINATE_ACCOUNTS = ["staging1", "develop1"]
