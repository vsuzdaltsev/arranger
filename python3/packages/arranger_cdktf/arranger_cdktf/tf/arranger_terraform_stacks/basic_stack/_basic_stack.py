import base64
import subprocess
from typing import Any, Dict, List, Union

import yaml

from cdktf import Fn, TerraformLocal, TerraformResourceLifecycle, TerraformStack
from constructs import Construct

from arranger_automation.log import Log

from arranger_cdktf.imports.aws.data_aws_subnets import (
    DataAwsSubnets,
    DataAwsSubnetsFilter,
)
from arranger_cdktf.imports.aws.data_aws_vpc import DataAwsVpc, DataAwsVpcFilter

from arranger_cdktf.imports.aws.data_aws_secretsmanager_secret import (
    DataAwsSecretsmanagerSecret,
)
from arranger_cdktf.imports.aws.data_aws_secretsmanager_secret_version import (
    DataAwsSecretsmanagerSecretVersion,
)

from arranger_cdktf.imports.null import Resource as NullResource
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

    @property
    def _name_prefix(self) -> str:
        raise NotImplementedError(
            f"Need to implement {self.__class__.__name__}#_name_prefix property."
        )

    def _setup_backend(self, scope):
        raise NotImplementedError("")


class AWSBasicStack(BasicStack):
    def _setup_backend(self):
        return self.globals.aws_backend(scope=self)
