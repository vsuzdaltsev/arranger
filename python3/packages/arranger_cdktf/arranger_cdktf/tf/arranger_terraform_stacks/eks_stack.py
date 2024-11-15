import json
from typing import Dict, List, Union

from cdktf import TerraformResourceLifecycle

from arranger_cdktf.imports.aws.eks_addon import EksAddon
from arranger_cdktf.imports.aws.eks_cluster import (
    EksCluster,
    EksClusterTimeouts,
    EksClusterVpcConfig,
    EksClusterKubernetesNetworkConfig,
)
from arranger_cdktf.imports.aws.eks_node_group import (
    EksNodeGroup,
    EksNodeGroupScalingConfig,
    EksNodeGroupTimeouts,
)
from arranger_cdktf.imports.aws.iam_openid_connect_provider import (
    IamOpenidConnectProvider,
)
from arranger_cdktf.imports.aws.iam_policy import IamPolicy
from arranger_cdktf.imports.aws.iam_role import (
    IamRole,
    IamRoleInlinePolicy,
)
from arranger_cdktf.imports.aws.iam_role_policy_attachment import (
    IamRolePolicyAttachment,
)
from arranger_cdktf.imports.aws.iam_user_policy_attachment import (
    IamUserPolicyAttachment,
)
from arranger_cdktf.imports.external import DataExternal

from python3.packages.arranger_conf.arranger_conf import ArrangerConf
from .basic_stack import AwsBasicStack, Construct, TfConf


# TODO: add metrics-server installation
#  $ kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


class EksStack(AwsBasicStack):
    VPC_CNI_ADDON_VERSION = "v1.13.4-eksbuild.1"
    EBS_CSI_ADDON_VERSION = "v1.21.0-eksbuild.1"
    RESOLVE_CONFLICTS_ON_ADDON_UPDATE = "OVERWRITE"
    SERVICES_IP_RANGE = "172.20.0.0/16"
    K8S_VERSION = ArrangerConf.CDK8S_KUBERNETES_VERSION

    @property
    def _name_prefix(self) -> str:
        return "eks"

    @property
    def sso_permission_sets_with_allowed_kubectl_access(self):
        return [
            f"{self.globals.cluster_name_alias.capitalize()}Developers",
            "AdministratorAccess",
        ]

    def __init__(self, scope: Construct, ns: str, config: TfConf):
        super().__init__(scope, ns, config=config)

        self.aws_provider = self.globals.automation(scope=self)
        self.k8s_provider = self.globals.k8s_provider(scope=self)
        self.external_provider = self.globals.external_provider(scope=self)

        self.vpc = self._aws_eks_main_vpc()
        self.subnets = self._subnets(
            provider=self.aws_provider, vpc_id=self.vpc.id, type_tag="private"
        )
        self.role = self._role()
        self.eks_management_policy_attachment = self._eks_management_policy_attachment()
        self.policy_attachments = self._policy_attachments()

        self.cluster = self._cluster()
        self.eks_addon_cni = self._eks_addon_cni()

        self.cluster_identity_oidc_issuer = self._cluster_identity_oidc_issuer()
        self.eks_oidc_fingerprints = self._eks_oidc_fingerprints()
        self.oidc_connect_provider = self._oidc_connect_provider()
        self.role_ebs_csi = self._role_ebs_csi()
        self.eks_addon_ebs_csi = self._eks_addon_ebs_csi()

        self.eks_node_groups = self._eks_node_groups()

        self.eks_kubectl_sso_developers_access_policy = (
            self._eks_kubectl_sso_developers_access_policy()
        )
        self.eks_kubectl_sso_developers_access_role = (
            self._eks_kubectl_sso_developers_access_role()
        )
        self.eks_kubectl_sso_developers_access_role_policy_attachment = (
            self._eks_kubectl_sso_developers_access_role_policy_attachment()
        )

    def _role(self) -> type(IamRole):
        name = self._name(object_type="iam-role-management")

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=self.globals.eks_assume_role_policy(),
            description="EKS management.",
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
        )

    def _eks_management_policy_attachment(
        self,
    ) -> type(IamUserPolicyAttachment):
        name = self._name(object_type="iam-role-management-policy-attachment")

        return IamRolePolicyAttachment(
            scope=self,
            id_=name,
            policy_arn="arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
            role=self.role.name,
            provider=self.aws_provider,
            depends_on=[self.role],
        )

    def _policy_attachments(self) -> List[type(IamRolePolicyAttachment)]:
        attachments = []

        for policy in self.cluster_role_policies():
            attachments.append(
                IamRolePolicyAttachment(
                    scope=self,
                    id_=f"{policy.get('PolicyName')}-attachment-{self.globals.cluster_name_alias}",
                    policy_arn=policy.get("PolicyArn"),
                    role=self.role.name,
                    depends_on=[self.role],
                    provider=self.aws_provider,
                )
            )

        return attachments

    @staticmethod
    def cluster_role_policies() -> List[Dict[str, str]]:
        return [
            {
                "PolicyName": "AmazonEC2RoleforSSM",
                "PolicyArn": "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM",
            },
            {
                "PolicyName": "AmazonEKSClusterPolicy",
                "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
            },
            {
                "PolicyName": "AmazonEKSWorkerNodePolicy",
                "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
            },
            {
                "PolicyName": "AmazonEC2ContainerRegistryReadOnly",
                "PolicyArn": "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
            },
            {
                "PolicyName": "CloudWatchAgentServerPolicy",
                "PolicyArn": "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy",
            },
            {
                "PolicyName": "AmazonEKSServicePolicy",
                "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKSServicePolicy",
            },
            {
                "PolicyName": "AmazonEKS_CNI_Policy",
                "PolicyArn": "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
            },
            {
                "PolicyName": "EC2InstanceProfileForImageBuilderECRContainerBuilds",
                "PolicyArn": "arn:aws:iam::aws:policy/EC2InstanceProfileForImageBuilderECRContainerBuilds",
            },
        ]

    @property
    def _eks_encryption_config(self):
        return None

    def _cluster(self) -> type(EksCluster):
        name = self._name(object_type="cluster")

        return EksCluster(
            scope=self,
            id_=name,
            name=self.globals.cluster_name_short,
            role_arn=self.role.arn,
            version=self.K8S_VERSION,
            enabled_cluster_log_types=[
                "api",
                "audit",
                "authenticator",
                "controllerManager",
                "scheduler",
            ],
            encryption_config=self._eks_encryption_config,
            kubernetes_network_config=EksClusterKubernetesNetworkConfig(
                service_ipv4_cidr=self.SERVICES_IP_RANGE
            ),
            vpc_config=EksClusterVpcConfig(
                subnet_ids=self.subnets.ids,
                endpoint_private_access=False,
                endpoint_public_access=True,
            ),
            timeouts=EksClusterTimeouts(**self.globals.default_timeouts()),
            tags=self.stack_tags,
            lifecycle=TerraformResourceLifecycle(ignore_changes=["vpc_config", "tags"]),
            provider=self.aws_provider,
        )

    def _cluster_identity_oidc_issuer(self) -> type(DataExternal):
        return DataExternal(
            scope=self,
            id="cluster-identity-oidc-issuer",
            program=[
                "python",
                f"{self.globals.cli_container_root}/python3/scripts/eks_stack/eks_cluster_identity_oidc_issuer.py",
                self.globals.cluster_name_alias,
            ],
            provider=self.external_provider,
            depends_on=[self.cluster],
        )

    def _eks_oidc_fingerprints(self) -> type(DataExternal):
        return DataExternal(
            scope=self,
            id="eks-oidc-fingerprints",
            program=[
                "bash",
                f"{self.globals.cli_container_root}/python3/scripts/eks_stack/oidc_fingerprints.sh",
                self.globals.aws_region,
            ],
            provider=self.external_provider,
            depends_on=[self.cluster],
        )

    def _oidc_connect_provider(self) -> type(IamOpenidConnectProvider):
        name = self._name(object_type="oidc-connect-provider")
        url = (
            f"https://oidc.eks.{self.globals.aws_region}.amazonaws.com"
            f"/id/"
            f"{self.cluster_identity_oidc_issuer.result(key='ENDPOINT_ID')}"
        )
        fp = self.eks_oidc_fingerprints.result(key="FINGERPRINT")

        return IamOpenidConnectProvider(
            scope=self,
            id_=name,
            client_id_list=["sts.amazonaws.com"],
            thumbprint_list=[fp],
            url=url,
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[self.eks_addon_cni],
        )

    def _eks_addon_cni(self) -> type(EksAddon):
        name = "vpc-cni"
        uniq_name = self._name(object_type=name)

        return EksAddon(
            scope=self,
            id_=uniq_name,
            addon_name=name,
            cluster_name=self.globals.cluster_name_short,
            addon_version=self.VPC_CNI_ADDON_VERSION,
            resolve_conflicts=self.RESOLVE_CONFLICTS_ON_ADDON_UPDATE,
            configuration_values=self._eks_addon_cni_configuration_values,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[self.cluster],
        )

    def _role_ebs_csi(self) -> type(IamRole):
        # TODO: replace with the managed AmazonEBSCSIDriverPolicy
        inline_policy = json.dumps(
            {
                "Statement": [
                    {
                        "Action": [
                            "ec2:*",
                        ],
                        "Effect": "Allow",
                        "Resource": "*",
                    }
                ],
                "Version": "2012-10-17",
            }
        )

        return IamRole(
            scope=self,
            id_=self.globals.cluster_ebs_csi_role_name(),
            name=self.globals.cluster_ebs_csi_role_name(),
            assume_role_policy=self.globals.iam_assume_role_policy_ebs_csi(
                eks_endpoint_id=self.cluster_identity_oidc_issuer.result(
                    key="ENDPOINT_ID"
                )
            ),
            inline_policy=[
                IamRoleInlinePolicy(
                    name="ebs_csi",
                    policy=inline_policy,
                ),
            ],
            description="EKS EBS CSI driver.",
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
        )

    @property
    def _eks_addon_cni_configuration_values(self) -> Union[str, None]:
        # https://aws.amazon.com/blogs/containers/amazon-eks-add-ons-advanced-configuration/
        return json.dumps({"env": {"ENABLE_PREFIX_DELEGATION": "true"}})

    def _eks_addon_ebs_csi(self) -> type(EksAddon):
        name = "aws-ebs-csi-driver"
        uniq_name = self._name(object_type=name)

        return EksAddon(
            scope=self,
            id_=uniq_name,
            addon_name=name,
            cluster_name=self.globals.cluster_name_short,
            addon_version=self.EBS_CSI_ADDON_VERSION,
            service_account_role_arn=self.role_ebs_csi.arn,
            resolve_conflicts=self.RESOLVE_CONFLICTS_ON_ADDON_UPDATE,
            tags=self.globals.common_tags(),
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
            depends_on=[self.oidc_connect_provider],
        )

    def _eks_node_groups(self) -> List[EksNodeGroup]:
        eks_node_groups = []
        for node_group_conf in self.globals.eks_get_node_groups_config():
            capacity_type = node_group_conf["capacity_type"]
            tags = (
                self.stack_tags
                | {"capacity_type": capacity_type}
                | {f"kubernetes.io/cluster/{self.globals.cluster_name}": "owned"}
            )

            eks_node_groups.append(
                EksNodeGroup(
                    scope=self,
                    disk_size=node_group_conf.get("disk_size")
                    or self.globals.eks_node_default_disk_size,
                    id_=node_group_conf["node_group_name"],
                    node_group_name=node_group_conf["node_group_name"],
                    cluster_name=self.globals.cluster_name_short,
                    subnet_ids=node_group_conf.get("subnet_ids", self.subnets.ids),
                    scaling_config=EksNodeGroupScalingConfig(
                        **node_group_conf["autoscale_config"]
                    ),
                    node_role_arn=self.role.arn,
                    instance_types=node_group_conf["instance_types"],
                    timeouts=EksNodeGroupTimeouts(**self.globals.default_timeouts()),
                    capacity_type=capacity_type,
                    depends_on=[self.cluster],
                    taint=node_group_conf.get("taints", None),
                    tags=tags,
                    lifecycle=self.lifecycle_policy(),
                    provider=self.aws_provider,
                )
            )

        return eks_node_groups

    def _eks_kubectl_sso_developers_access_policy(self) -> type(IamPolicy):
        name = self._name(object_type="kubectl-sso-policy")

        return IamPolicy(
            scope=self,
            id_=name,
            name=name,
            policy=json.dumps(
                {
                    "Statement": [
                        {
                            "Action": [
                                "eks:*",
                                "ec2:*",
                                "autoscaling:*",
                                "sts:GetCallerIdentity",
                            ],
                            "Effect": "Allow",
                            "Resource": "*",
                        }
                    ],
                    "Version": "2012-10-17",
                }
            ),
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
        )

    def _eks_kubectl_sso_developers_access_role(self) -> type(IamRole):
        name = self.globals.eks_kubectl_sso_role

        return IamRole(
            scope=self,
            id_=name,
            name=name,
            assume_role_policy=self._eks_kubectl_sso_developers_access_role_assume_policy(
                permission_sets=self.sso_permission_sets_with_allowed_kubectl_access,
            ),
            tags=self.stack_tags,
            lifecycle=self.lifecycle_policy(),
            provider=self.aws_provider,
        )

    def _allow_sso_users_statement(self, permission_set: str):
        return {
            "Effect": "Allow",
            "Principal": {"AWS": ["*"]},
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": (
                        f"arn:aws:iam::{self.globals.aws_account_id}:"
                        f"role/aws-reserved/sso.amazonaws.com/"
                        f"{self.globals.aws_region}/AWSReservedSSO_{permission_set}_*"
                    )
                },
                "ForAllValues:StringEquals": {
                    "aws:PrincipalAccount": [self.globals.aws_account_id]
                },
            },
        }

    def _eks_kubectl_sso_developers_access_role_assume_policy(
        self, permission_sets: List[str]
    ) -> str:
        return json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    self._allow_sso_users_statement(permission_set=ps)
                    for ps in permission_sets
                ]
                + [
                    {
                        "Sid": "Statement1",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": f"arn:aws:iam::{self.globals.aws_account_id}:user/vsevolod.suzdaltsev"
                        },
                        "Action": "sts:AssumeRole",
                    }
                ],
            }
        )

    def _eks_kubectl_sso_developers_access_role_policy_attachment(
        self,
    ) -> type(IamUserPolicyAttachment):
        name = self._name(object_type="kubectl-sso-role-policy-attachment")

        return IamRolePolicyAttachment(
            scope=self,
            id_=name,
            policy_arn=self.eks_kubectl_sso_developers_access_policy.arn,
            role=self.eks_kubectl_sso_developers_access_role.name,
            provider=self.aws_provider,
            depends_on=[
                self.eks_kubectl_sso_developers_access_policy,
                self.eks_kubectl_sso_developers_access_role,
            ],
        )
