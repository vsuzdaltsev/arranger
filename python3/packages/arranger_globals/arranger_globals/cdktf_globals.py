import ipaddress
import time
from typing import Any, Dict, List, Union

from constructs import Construct

from arranger_globals.basic_arranger_globals import (
    to_kebab,
    ByTenant,
    validate_subnets,
)


class CdktfGlobals(ByTenant):
    def common_tags(self) -> Dict[str, str]:
        return {
            "created_by": "cdktf",
            "caution": "do not modify manually",
            "code": "git@github.com:vsuzdaltsev/arranger.git",
            "tenant": self.tenant,
            "created_at": time.ctime(),
        }

    @staticmethod
    def archive_provider(scope: Construct) -> Any:
        from arranger_cdktf.imports.archive.provider import ArchiveProvider

        return ArchiveProvider(scope=scope, id="archive")

    @property
    def cloud(self) -> Union[str, None]:
        from arranger_conf import ArrangerConf

        return (
            ArrangerConf.TENANTS.get(self.tenant, {})
            .get("cloud_attributes", {})
            .get("cloud")
        )

    @staticmethod
    def external_provider(scope: Construct) -> Any:
        from arranger_cdktf.imports.external import ExternalProvider

        return ExternalProvider(scope=scope, id="external-provider")

    def k8s_provider(
        self,
        scope: Construct,
        where_kube_config: Union[str, None] = None,
    ) -> Any:
        from arranger_cdktf.imports.kubernetes.provider import (
            KubernetesProvider,
        )

        return KubernetesProvider(
            scope=scope,
            id="k8s-provider",
            # FIXME: add cluster_name attr & where_kubeconfig attr
            config_path=where_kube_config or self.where_kubeconfig,
            config_context=self.cluster_name,
        )

    @property
    def cluster_name(self) -> Union[str, None]:
        from arranger_conf.arranger_conf import ArrangerConf

        try:
            return ArrangerConf.TENANTS[self.tenant]["cluster_name"]
        except TypeError:
            self.log.error(
                f">> '{self.tenant}' doesn't contain 'cluster_name' attribute."
            )

    @property
    def cluster_name_short(self) -> str:
        return self.cluster_name.split("/")[-1]

    @staticmethod
    def iam_assume_role_policy_custom(principal_services: Union[List[str], str]) -> str:
        import json

        return json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": principal_services,
                    },
                    "Action": "sts:AssumeRole",
                },
            }
        )

    def eks_assume_role_policy(self) -> str:
        return self.iam_assume_role_policy_custom(
            ["ec2.amazonaws.com", "eks.amazonaws.com"]
        )

    def cluster_ebs_csi_role_name(self) -> str:
        return f"eks-ebs-csi-management-role-{self.tenant}"

    def iam_assume_role_policy_ebs_csi(self, eks_endpoint_id: str) -> str:
        import json

        oidc = f"oidc.eks.{self.aws_region}.amazonaws.com"
        string_equals = {
            f"{oidc}/id/{eks_endpoint_id}:aud": "sts.amazonaws.com",
            f"{oidc}/id/{eks_endpoint_id}:sub": "system:serviceaccount:kube-system:ebs-csi-controller-sa",
        }

        return json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": {
                    "Effect": "Allow",
                    "Principal": {
                        "Federated": f"arn:aws:iam::{self.aws_account_id}:oidc-provider/{oidc}/id/{eks_endpoint_id}",
                    },
                    "Action": "sts:AssumeRoleWithWebIdentity",
                    "Condition": {"StringEquals": string_equals},
                },
            }
        )

    def eks_get_node_groups_config(self) -> List[dict]:
        default_configs = [
            {
                "node_group_name": "node-group-1",
                "capacity_type": "SPOT",  # ON_DEMAND ?
                "instance_types": ["t3.large"],
                "autoscale_config": {"min_size": 3, "max_size": 8, "desired_size": 6},
            }
        ]
        if not hasattr(self.config, "EKS_NODE_GROUPS_CONFIG"):
            return default_configs

        return self.config.EKS_NODE_GROUPS_CONFIG

    @property
    def eks_kubectl_sso_role(self) -> str:
        return f"eks-kubectl-sso-role-{self.tenant}"

    @staticmethod
    def null_provider(scope: Construct) -> Any:
        from arranger_cdktf.imports.null import NullProvider

        return NullProvider(scope=scope, id="null-provider")

    @property
    def prevent_destroy(self) -> bool:
        if hasattr(self.config, "PREVENT_DESTROY"):
            return self.config.PREVENT_DESTROY

        return False

    @staticmethod
    def _new_subnet(
        supernet_cidr: ipaddress.ip_network, subnet_prefix: int, subnet_index: int
    ) -> str:
        supernet_cidr = ipaddress.ip_network(supernet_cidr)

        return str(list(supernet_cidr.subnets(new_prefix=subnet_prefix))[subnet_index])

    @property
    @validate_subnets
    def ip_ranges(self, tenant: str = None) -> Dict[str, Any]:
        registry = {
            "development1": {
                "vpc-main": {
                    "cidr": ["10.62.0.0/18"],
                    "subnets": {
                        "snet-eks1": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.62.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=0,
                                )
                            ],
                            "availability-zone": self.aws_region + "a",
                        },
                        "snet-eks2": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.62.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=1,
                                )
                            ],
                            "availability-zone": self.aws_region + "b",
                        },
                        "snet-eks3": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.62.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=2,
                                )
                            ],
                            "availability-zone": self.aws_region + "c",
                        },
                        "snet-eks4": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.62.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=3,
                                )
                            ],
                            "availability-zone": self.aws_region + "a",
                        },
                    },
                },
            },
            "staging1": {
                "vpc-main": {
                    "cidr": ["10.61.0.0/18"],
                    "subnets": {
                        "snet-eks1": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.61.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=0,
                                )
                            ],
                            "availability-zone": self.aws_region + "a",
                        },
                        "snet-eks2": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.61.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=1,
                                )
                            ],
                            "availability-zone": self.aws_region + "b",
                        },
                        "snet-eks3": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.61.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=2,
                                )
                            ],
                            "availability-zone": self.aws_region + "c",
                        },
                        "snet-eks4": {
                            "cidr": [
                                self._new_subnet(
                                    supernet_cidr="10.61.0.0/18",
                                    subnet_prefix=20,
                                    subnet_index=3,
                                )
                            ],
                            "availability-zone": self.aws_region + "a",
                        },
                    },
                },
            },
        }

        if not tenant:
            return registry.get(self.tenant)

        return registry.get(tenant)

    @property
    def _aws_backend_s3bucket_name(self) -> str:
        from arranger_conf import ArrangerConf

        return f"{to_kebab(ArrangerConf.PROJECT_NAME)[:5]}-arranger-tf-remote-states-{self.tenant}"[
            :63
        ]

    def aws_backend(self, scope: Construct, region: Union[str, None] = None) -> Any:
        from cdktf import S3Backend
        from arranger_automation_aws.helpers import BackendHelperAws

        def item_name():
            stack_class_name = scope.__class__.__name__
            config_class_name = self.tenant.capitalize()

            if stack_class_name.startswith(config_class_name):
                return scope.__class__.__name__.split(config_class_name)[1].lower()

            return stack_class_name.lower()

        if region is None:
            region = self.aws_region

        dynamodb_lock = BackendHelperAws.create_table(
            name=f"{item_name()}-lock",
            profile=self.aws_profile,
            region=region,
        )

        BackendHelperAws.BUCKET_NAME = self._aws_backend_s3bucket_name
        state_s3bucket = BackendHelperAws.create_bucket(
            profile=self.aws_profile, location_constraint=region
        )
        BackendHelperAws.enable_s3_versioning(
            profile=self.aws_profile, aws_region=region
        )

        return S3Backend(
            scope=scope,
            bucket=state_s3bucket,
            key=f"{item_name()}/terraform.tfstate",
            region=region,
            dynamodb_table=dynamodb_lock,
            encrypt=True,
            profile=self.aws_profile,
        )

    def provider(self, scope: Construct, profile: str, provider_id: str, region=None):
        from arranger_cdktf.imports.aws.provider import AwsProvider

        if not region:
            region = self.aws_region

        return AwsProvider(
            scope,
            id=provider_id,
            region=region,
            profile=profile,
            max_retries=self.config.MAX_RETRIES,
        )

    def global_automation(self, scope):
        from arranger_cdktf.imports.aws.provider import AwsProvider

        return AwsProvider(
            scope=scope,
            profile=self.aws_profile,
            region=self.config.AWS_GLOBAL_REGION,
            id="aws_global",
            alias="aws_global",
            max_retries=self.config.MAX_RETRIES,
        )

    def automation(self, scope: Construct, region=None, provider_id="aws"):
        return self.provider(
            scope=scope,
            profile=self.aws_profile,
            region=region,
            provider_id=provider_id,
        )

    def default_timeouts(self) -> Dict[str, str]:
        return self.config.DEFAULT_TIMEOUTS

    @property
    def aws_global_region(self) -> str:
        return self.config.AWS_GLOBAL_REGION

    @property
    def sub_environments(self) -> Union[List[str], None]:
        from arranger_conf.arranger_conf import ArrangerConf

        return ArrangerConf.TENANTS.get(self.tenant, {}).get("sub_environments")

    @staticmethod
    def run_cmd(cmds: List[str]):
        import subprocess as sp

        return sp.getoutput("; ".join(cmds))
