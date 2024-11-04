from eusy_globals.cdktf_globals import CdktfGlobals


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

    class Orchestra2(BasicConf):
        cg = CdktfGlobals(cluster_name_alias=__qualname__.lower().split(".")[-1])
        ALL_STACKS = [
            "automation-endpoints-stack",
            "vpc-stack",
            "codecommit-stack",
            "codebuild-stack",
            "codeartifact-stack",
            "ecr-stack",
            "aws-iam-stack",
            "secrets-manager-stack",
        ]
        CLUSTER_NAME_ALIAS = cg.cluster_name_alias
        CODEBUILD_CONFIG = [
            cg.codebuild_deploy_secrets(),
            cg.codebuild_meta_cli_build(),
            cg.codebuild_universal_build_and_push_back(),
            cg.codebuild_universal_build_and_push_front(),
            cg.codebuild_orchestra_deploy(
                **{
                    "ENVIRONMENT": "d1",
                    "CLUSTER_NAME_ALIAS": "switchdev1",
                    "PROFILE": "switchdev1",
                }
            ),
        ]

    class Sandbox1(BasicConf):
        cg = CdktfGlobals(cluster_name_alias=__qualname__.lower().split(".")[-1])
        ALL_STACKS = [
            "backup-stack",
            "codecommit-stack",
            "codebuild-stack",
            "ecr-stack",
            "aws-iam-stack",
            "secrets-manager-stack",
            "codeartifact-stack",
            "vpc-stack",
            "eks-stack",
            "route53-zone-stack",
            "acm-stack",
            "istio-stack",
            "api-gateway-stack",
            "api-gateway-rest-stack",
            "kafka-stack",
            "cassandra-stack",
            "rds-stack",
            "ldap-stack",
            "keycloak-stack",
            # "keycloak-resources-stack", deprecated in favour of ldap-stack
            "kafka-ui-stack",
            "n8n-vm-stack",
            "prometheus-grafana-stack",
            "loki-stack",
            "tempo-stack",
            "trust-orchestrating-account-iam-stack",
            # "free-ipa-stack",
        ]
        CLUSTER_NAME_ALIAS = cg.cluster_name_alias
        CODEBUILD_CONFIG = [
            cg.codebuild_backup_ldap_objects(),
            cg.codebuild_deploy_secrets(),
            cg.codebuild_meta_cli_build(),
            cg.codebuild_universal_build_and_deploy_front(),
            cg.codebuild_universal_build_back(),
            cg.codebuild_universal_build_front(),
            cg.codebuild_universal_deploy(**{"ENVIRONMENT": "sand1"}),
        ]
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
                "disk_size": 100,
            },
            {
                "node_group_name": cg.eks_node_group_cassandra,
                "capacity_type": "ON_DEMAND",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.xlarge"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 2,
                    "desired_size": 1,
                },
                "disk_size": 100,
                "taints": [
                    {
                        "key": "cassandra-only",
                        "value": "true",
                        "effect": "NO_SCHEDULE",
                    }
                ],
            },
            {
                "node_group_name": cg.eks_node_group_keycloak,
                "capacity_type": "ON_DEMAND",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.medium"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 2,
                    "desired_size": 1,
                },
                "disk_size": 100,
                "taints": [
                    {
                        "key": "keycloak-only",
                        "value": "true",
                        "effect": "NO_SCHEDULE",
                    }
                ],
            },
            {
                "node_group_name": cg.eks_node_group_ldap,
                "capacity_type": "ON_DEMAND",
                "instance_types": ["t3.small"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 2,
                    "desired_size": 1,
                },
                "disk_size": 30,
                "taints": [
                    {
                        "key": "ldap-only",
                        "value": "true",
                        "effect": "NO_SCHEDULE",
                    }
                ],
            },
        ]

        CERT_SUB_ENVIRONMENTS = cg.sub_environments
        KAFKA_INSTANCE_TYPE = "kafka.t3.small"
        RDS_INSTANCE_TYPE = "db.t3.medium"

    class Switchdev1(BasicConf):
        cg = CdktfGlobals(cluster_name_alias=__qualname__.lower().split(".")[-1])
        ALL_STACKS = [
            "backup-stack",
            "codebuild-stack",
            "ecr-stack",
            "aws-iam-stack",
            "codecommit-stack",
            "vpc-stack",
            "aux-vpc-stack",
            "eks-stack",
            "route53-zone-stack",
            "acm-stack",
            "istio-stack",
            "api-gateway-stack",
            "api-gateway-rest-stack",
            "kafka-stack",
            # "aws-keyspaces-stack", # deprecated in favour of the cassandra-stack
            "secrets-manager-stack",
            "cassandra-stack",
            "rds-stack",
            "ldap-stack",
            "keycloak-stack",
            # "keycloak-resources-stack", deprecated in favour of ldap-stack
            "kafka-ui-stack",
            "prometheus-grafana-stack",
            "loki-stack",
            "tempo-stack",
            "trust-orchestrating-account-iam-stack",
        ]
        CLUSTER_NAME_ALIAS = cg.cluster_name_alias
        CODEBUILD_CONFIG = [
            cg.codebuild_backup_ldap_objects(),
            cg.codebuild_auto_tests(
                **{
                    "KITCHEN_SUBNET_ID": "subnet-0e610dbb3cd0c26ed"
                }  # TODO: AUX-VPC private subnet id. Move to globals
            ),
            cg.codebuild_deploy_secrets(),
            cg.codebuild_meta_cli_build(),
            # cg.codebuild_test_project(**{"ENVIRONMENT": "d1"}),
            cg.codebuild_universal_build_back(),
            cg.codebuild_universal_build_front(),
            cg.codebuild_universal_build_and_deploy_front(),
            cg.codebuild_universal_deploy(**{"ENVIRONMENT": "d1"}),
        ]
        EKS_NODE_GROUPS_CONFIG = [
            {
                "node_group_name": "node-group-1",
                "capacity_type": "ON_DEMAND",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.xlarge"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 6,
                    "desired_size": 5,
                },
                "disk_size": 100,
            },
            {
                "node_group_name": cg.eks_node_group_cassandra,
                "capacity_type": "ON_DEMAND",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.xlarge"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 2,
                    "desired_size": 1,
                },
                "disk_size": 100,
                "taints": [
                    {
                        "key": "cassandra-only",
                        "value": "true",
                        "effect": "NO_SCHEDULE",
                    }
                ],
            },
            {
                "node_group_name": cg.eks_node_group_keycloak,
                "capacity_type": "ON_DEMAND",  # TODO: select ON_DEMAND / SPOT ?
                "instance_types": ["t3.medium"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 2,
                    "desired_size": 1,
                },
                "disk_size": 100,
                "taints": [
                    {
                        "key": "keycloak-only",
                        "value": "true",
                        "effect": "NO_SCHEDULE",
                    }
                ],
            },
            {
                "node_group_name": cg.eks_node_group_ldap,
                "capacity_type": "ON_DEMAND",
                "instance_types": ["t3.small"],
                "autoscale_config": {
                    "min_size": 1,
                    "max_size": 2,
                    "desired_size": 1,
                },
                "disk_size": 30,
                "taints": [
                    {
                        "key": "ldap-only",
                        "value": "true",
                        "effect": "NO_SCHEDULE",
                    }
                ],
            },
        ]

        CERT_SUB_ENVIRONMENTS = cg.sub_environments
        KAFKA_INSTANCE_TYPE = "kafka.m5.large"  # "kafka.t3.small"
        RDS_INSTANCE_TYPE = "db.t3.medium"
