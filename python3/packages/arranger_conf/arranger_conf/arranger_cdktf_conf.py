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


class TfConf:
    class Development1(BasicConf):
        ALL_STACKS = ["vpc-stack"]
        TENANT = "development1"

    class Local(BasicConf):
        ALL_STACKS = []
        TENANT = "local"

    class Staging1(BasicConf):
        ALL_STACKS = []
        TENANT = "staging1"
