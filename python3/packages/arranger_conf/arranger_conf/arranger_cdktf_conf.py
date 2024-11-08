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
        }
    }
    ALL_STACKS = []
    MAX_RETRIES = 100


class TfConf:
    class Develop1(BasicConf):
        ALL_STACKS = ["acm-stack"]

    class Local(BasicConf):
        ALL_STACKS = ["acm-stack"]

    class Staging1(BasicConf):
        ALL_STACKS = ["acm-stack"]
