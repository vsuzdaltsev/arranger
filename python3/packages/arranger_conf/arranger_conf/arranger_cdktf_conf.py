# from arranger_globals.cdktf_globals import CdktfGlobals
from python3.packages.arranger_automation.arranger_automation.threads.parallel import (
    BasicParallel,
)


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
        pass
    class Local(BasicConf):
        pass


    class Staging1(BasicConf):
        pass
