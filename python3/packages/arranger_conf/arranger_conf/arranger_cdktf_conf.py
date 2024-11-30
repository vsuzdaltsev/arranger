from .basic_cdktf_conf import BasicTfConf


class TfConf:
    class Development1(BasicTfConf):
        ALL_STACKS = ["demo-iam-user-stack", "vpc-stack", "eks-stack"]
        EKS_NODE_GROUPS_CONFIG = [
            {
                "node_group_name": "node-group-1",
                "capacity_type": "SPOT",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.medium"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 3,
                    "desired_size": 2,
                },
                "disk_size": 50,
            },
        ]

    class Local(BasicTfConf):
        ALL_STACKS = []

    class Staging1(BasicTfConf):
        ALL_STACKS = ["vpc-stack"]
