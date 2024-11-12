from typing import List

from cdktf import TerraformResourceLifecycle, TerraformStack
from constructs import Construct

from arranger_automation.log import Log
from arranger_conf.arranger_cdktf_conf import TfConf
from arranger_globals.cdktf_globals import CdktfGlobals


class BasicStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str, config: type(TfConf)):
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
    ) -> type(TerraformResourceLifecycle):
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

    def _setup_backend(self):
        raise NotImplementedError(
            f"Need to implement {self.__class__.__name__}#_setup_backend."
        )


class AwsBasicStack(BasicStack):
    def _setup_backend(self):
        return self.globals.aws_backend(scope=self)
