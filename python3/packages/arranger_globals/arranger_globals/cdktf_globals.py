import ipaddress
import time
from typing import Any, Dict, List, Union

import cdktf

import arranger_cdktf
from basic_arranger_globals import ByTenant, validate_subnets


class CdktfGlobals(ByTenant):
    def common_tags(self) -> Dict[str, str]:
        return {
            "created_by": "cdktf",
            "caution": "do not modify manually",
            "code": "git@git.velox-solution.com:eusy/meta-cli-switch.git",
            "tenant": self.tenant,
            "created_at": time.ctime(),
        }

    @staticmethod
    def archive_provider(scope) -> Any:
        from arranger_cdktf.imports.archive.provider import ArchiveProvider

        return ArchiveProvider(scope=scope, id="archive")

    @property
    def cloud(self) -> str:
        return arranger_cdktf.AppConf.CLUSTERS[self.tenant]["cloud_attributes"]["cloud"]

    @staticmethod
    def external_provider(scope: Any) -> Any:
        from arranger_cdktf.imports.external import ExternalProvider

        return ExternalProvider(scope=scope, id="external-provider")

    def k8s_provider(
        self,
        scope: type(cdktf.TerraformStack),
        where_kube_config: Union[str, None] = None,
    ) -> Any:
        from arranger_cdktf.imports.kubernetes.provider import (
            KubernetesProvider,
        )

        return KubernetesProvider(
            scope=scope,
            id="k8s-provider",
            config_path=where_kube_config or self.where_kubeconfig,
            config_context=self.cluster_name,
        )

    @staticmethod
    def null_provider(scope: Any) -> Any:
        from arranger_cdktf.imports.null import NullProvider

        return NullProvider(scope=scope, id="null-provider")

    @property
    def prevent_destroy(self) -> bool:
        if hasattr(self.config, "PREVENT_DESTROY"):
            return self.config.PREVENT_DESTROY

        return False

    @staticmethod
    def _new_subnet(supernet_cidr, subnet_prefix, subnet_index):
        supernet_cidr = ipaddress.ip_network(supernet_cidr)

        return str(list(supernet_cidr.subnets(new_prefix=subnet_prefix))[subnet_index])

    @property
    @validate_subnets
    def ip_ranges(self, tenant: str = None) -> Dict[str, Any]:
        registry = {
            "develop1": {
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

    def aws_backend(self, scope, region=None) -> type(Any):
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
        # FIXME: randomize name
        bucket_name = f"arranger-terraform-remote-states-{self.tenant}"
        BackendHelperAws.BUCKET_NAME = bucket_name
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

    def provider(self, scope, profile: str, provider_id: str, region=None):
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

    def automation(self, scope, region=None, provider_id="aws"):
        return self.provider(
            scope=scope,
            profile=self.aws_profile,
            region=region,
            provider_id=provider_id,
        )

    def default_timeouts(self) -> Dict:
        return self.config.DEFAULT_TIMEOUTS

    @property
    def aws_global_region(self) -> str:
        return self.config.AWS_GLOBAL_REGION

    @property
    def sub_environments(self) -> List[str]:
        from arranger_conf.app_conf import AppConf

        return AppConf.CLUSTERS[self.tenant]["sub_environments"]

    @staticmethod
    def run_cmd(cmds: List[str]):
        import subprocess as sp

        return sp.getoutput("; ".join(cmds))
