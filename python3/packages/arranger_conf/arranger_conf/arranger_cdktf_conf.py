class BasicConf:
    DEFAULT_TIMEOUTS = {"create": "45m", "delete": "45m"}
    AWS_GLOBAL_REGION = "us-east-1"
    VALID_STACKS = {
        "tf": {
            "acm-stack": {
                "class_name": "AcmStack",
                "description": "AWS certificates.",
                "depends_on": ["route53-zone-stack"],
            },
            "vpc-stack": {
                "class_name": "VpcStack",
                "description": "AWS VPC.",
                "depends_on": [],
            },
        }
    }
    ALL_STACKS = []
    MAX_RETRIES = 100

    @classmethod
    @property
    def TENANT(cls):
        return cls.__name__.lower()


class TfConf:
    class Development1(BasicConf):
        ALL_STACKS = ["vpc-stack"]

    class Local(BasicConf):
        ALL_STACKS = []

    class Staging1(BasicConf):
        ALL_STACKS = []
