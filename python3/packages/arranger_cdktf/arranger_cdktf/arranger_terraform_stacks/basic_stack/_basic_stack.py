from typing import Any, List

from cdktf import S3Backend, TerraformResourceLifecycle, TerraformStack
from constructs import Construct

from arranger_automation.log import Log
from arranger_cdktf.imports.aws.data_aws_subnets import (
    DataAwsSubnets,
    DataAwsSubnetsFilter,
)
from arranger_cdktf.imports.aws.data_aws_vpc import DataAwsVpc, DataAwsVpcFilter
from arranger_conf.arranger_cdktf_conf import TfConf
from arranger_globals.cdktf_globals import CdktfGlobals


class BasicStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str, config: TfConf):
        super().__init__(scope, ns)

        self.log = Log().logger(desc=self.__class__.__name__)
        self.config = config
        self.globals = CdktfGlobals(tenant=self.config.TENANT, config=self.config)
        self.backend = self._setup_backend()
        self.stack_tags = self.globals.common_tags() | {
            "stack": self.__class__.__name__
        }

    def _name(self, object_type: str) -> str:
        return f"{self._name_prefix}-{object_type}-{self.globals.tenant}"

    def lifecycle_policy(
        self, ignore_changes: List[str] = None, create_before_destroy: bool = None
    ) -> TerraformResourceLifecycle:
        if ignore_changes is None:
            ignore_changes = ["tags"]

        return TerraformResourceLifecycle(
            create_before_destroy=create_before_destroy,
            ignore_changes=ignore_changes,
            prevent_destroy=self.globals.prevent_destroy,
        )

    @property
    def _name_prefix(self) -> str:
        raise NotImplementedError(
            f"Need to implement {self.__class__.__name__}#_name_prefix property."
        )

    def _setup_backend(self) -> Any:
        raise NotImplementedError(
            f"Need to implement {self.__class__.__name__}#_setup_backend."
        )


class AwsBasicStack(BasicStack):
    def _setup_backend(self) -> S3Backend:
        return self.globals.aws_backend(scope=self)

    def _aws_eks_main_vpc(self) -> DataAwsVpc:
        name = f"vpc-main-{self.globals.tenant}"
        uniq_name = self._name(object_type="data-vpc-main")

        return DataAwsVpc(
            scope=self,
            id_=uniq_name,
            filter=[
                DataAwsVpcFilter(
                    name="tag:Name",
                    values=[name],
                ),
            ],
        )

    def _subnets(
        self, provider, vpc_id: str, type_tag: str = "private"
    ) -> DataAwsSubnets:
        name = self._name(object_type="data-vpc-subnets")

        return DataAwsSubnets(
            scope=self,
            id_=name,
            filter=[
                DataAwsSubnetsFilter(
                    name="vpc-id",
                    values=[vpc_id],
                ),
                DataAwsSubnetsFilter(
                    name="tag:type",
                    values=[type_tag],
                ),
            ],
            provider=provider,
        )
