# from arranger_globals.cdktf_globals import CdktfGlobals


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
            "api-gateway-rest-stack": {
                "class_name": "ApiGatewayRestStack",
                "description": "AWS REST API Gateway.",
                "depends_on": ["vpc-stack", "acm-stack", "eks-stack", "istio-stack"],
            },
            "api-gateway-stack": {
                "class_name": "ApiGatewayStack",
                "description": "AWS API Gateway.",
                "depends_on": ["vpc-stack", "acm-stack", "eks-stack", "istio-stack"],
            },
            "automation-endpoints-stack": {
                "class_name": "AutomationEndpointsStack",
                "description": "Automation endpoints.",
                "depends_on": ["trust-orchestrating-account-iam-stack"],
            },
            "aux-vpc-stack": {
                "class_name": "AuxVpcStack",
                "description": "Autotests VPC stack. Needed to use static origin white IP for CodeBuilds.",
                "depends_on": None,
            },
            "aws-iam-stack": {
                "class_name": "AwsIamStack",
                "description": "AWS IAM resources.",
                "depends_on": None,
            },
            "aws-keyspaces-stack": {
                "class_name": "AwsKeyspacesStack",
                "description": "AWS Managed Cassandra DB. Not used in favour of cassandra-stack.",
                "depends_on": ["vpc-stack"],
            },
            "backup-stack": {
                "class_name": "BackupStack",
                "description": "Backups.",
                "depends_on": None,
            },
            "cassandra-stack": {
                "class_name": "CassandraStack",
                "description": "Self managed Cassandra DB.",
                "depends_on": ["eks-stack", "create endpoints namespace"],
            },
            "codeartifact-stack": {
                "class_name": "CodeartifactStack",
                "description": "Maven repository.",
                "depends_on": None,
            },
            "codebuild-stack": {
                "class_name": "CodebuildStack",
                "description": "Manage AWS CodeBuild pipelines.",
                "depends_on": None,
            },
            "codecommit-stack": {
                "class_name": "CodecommitStack",
                "description": "AWS CodeCommit repositories.",
                "depends_on": None,
            },
            "ecr-stack": {
                "class_name": "EcrStack",
                "description": (
                    "AWS ECR repositories. "
                    "NB: the repos for the microservices are being created with the build-and-push invoke task."
                ),
                "depends_on": None,
            },
            "eks-stack": {
                "class_name": "EksStack",
                "description": "AWS EKS cluster.",
                "depends_on": ["eks-stack"],
            },
            "free-ipa-stack": {
                "class_name": "FreeIpaStack",
                "description": "FreeIPA.",
                "depends_on": [],
            },
            "istio-stack": {
                "class_name": "IstioStack",
                "description": "Istio service mesh.",
                "depends_on": ["eks-stack"],
            },
            "kafka-stack": {
                "class_name": "KafkaStack",
                "description": "AWS MSK stack.",
                "depends_on": ["vpc-stack"],
            },
            "kafka-ui-stack": {
                "class_name": "KafkaUiStack",
                "description": "Kafka-UI.",
                "depends_on": ["eks-stack"],
            },
            "keycloak-resources-stack": {
                "class_name": "KeycloakResourcesStack",
                "description": "Self managed Keycloak resources.",
                "depends_on": ["eks-stack", "keycloak-stack"],
            },
            "keycloak-stack": {
                "class_name": "KeycloakStack",
                "description": "Self managed Keycloak.",
                "depends_on": ["eks-stack", "ldap-stack"],
            },
            "loki-stack": {
                "class_name": "LokiStack",
                "description": "https://grafana.github.io/helm-charts",
                "depends_on": ["eks-stack", "rds-stack"],
            },
            "n8n-vm-stack": {
                "class_name": "N8nStack",
                "description": "",
                "depends_on": ["route53-zone-stack"],
            },
            "ldap-stack": {
                "class_name": "LdapStack",
                "description": "OpenLDAP service for hosting keycloak users/groups.",
                "depends_on": ["eks-stack"],
            },
            "prometheus-grafana-stack": {
                "class_name": "PrometheusGrafanaStack",
                "description": "https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack",
                "depends_on": ["eks-stack", "rds-stack"],
            },
            "rds-stack": {
                "class_name": "RdsStack",
                "description": "Aurora postgres.",
                "depends_on": ["vpc-stack"],
            },
            "route53-zone-stack": {
                "class_name": "Route53ZoneStack",
                "description": "AWS Route53 zone.",
                "depends_on": None,
            },
            "secrets-manager-stack": {
                "class_name": "SecretsManagerStack",
                "description": "AWS Secrets Manager.",
                "depends_on": None,
            },
            "tempo-stack": {
                "class_name": "TempoStack",
                "description": "Grafana tempo.",
                "depends_on": ["vpc-stack", "eks-stack"],
            },
            "trust-orchestrating-account-iam-stack": {
                "class_name": "TrustOrchestratingAccountIamStack",
                "description": "Trust relationships between Orchestration account and the others.",
                "depends_on": None,
            },
            "vpc-stack": {
                "class_name": "VpcStack",
                "description": "Main VPC for placing EKS.",
                "depends_on": None,
            },
        }
    }
    ALL_STACKS = []
    MAX_RETRIES = 100


class TfConf:
    class Local(BasicConf):
        pass
