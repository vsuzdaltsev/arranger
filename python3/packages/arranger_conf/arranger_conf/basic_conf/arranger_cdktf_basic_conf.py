class BasicConf:
    @classmethod
    @property
    def TENANT(obj) -> str:
        return obj.__name__.lower()

    ALL_STACKS = []
    AWS_GLOBAL_REGION = "us-east-1"
    DEFAULT_TIMEOUTS = {"create": "45m", "delete": "45m"}
    MAX_RETRIES = 100
    VALID_STACKS = {
        "tf": {
            # "acm-stack": {
            #     "class_name": "AcmStack",
            #     "description": "AWS certificates.",
            #     "depends_on": ["route53-zone-stack"],
            # },
            "test-iam-user-stack": {
                "class_name": "TestIamUserStack",
                "description": "Test Terraform stack to create AWS IAM user.",
                "depends_on": [],
            },
            "vpc-stack": {
                "class_name": "VpcStack",
                "description": "AWS VPC.",
                "depends_on": [],
            },
            "eks-stack": {
                "class_name": "EksStack",
                "description": "AWS EKS cluster.",
                "depends_on": ["vpc-stack"],
            },
        }
    }
