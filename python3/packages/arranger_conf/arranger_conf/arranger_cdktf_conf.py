from .basic_conf import BasicConf


class TfConf:
    class Development1(BasicConf):
        ALL_STACKS = ["vpc-stack", "eks-stack"]
        EKS_NODE_GROUPS_CONFIG = [
            {
                "node_group_name": "node-group-1",
                "capacity_type": "SPOT",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.xlarge"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 3,
                    "desired_size": 2,
                },
                "disk_size": 50,
            },
        ]

    class Local(BasicConf):
        ALL_STACKS = []

    class Staging1(BasicConf):
        ALL_STACKS = ["vpc-stack"]
