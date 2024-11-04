#!/usr/bin/env python3

import sys
from typing import Type

from cdktf import App

from eusy_automation.log import Log
from eusy_cdktf.tf.eusy_terraform_stacks import *
from eusy_conf.eusy_cdktf_conf import TfConf


CLUSTER_NAME_ALIAS = sys.argv[1]
STACK = sys.argv[2]
PROJECT_NAME = "tf"


if __name__ == "__main__":
    app = App(stack_traces=True)
    log = Log().logger(desc=str(app.__class__.__qualname__))

    env_config = getattr(TfConf, CLUSTER_NAME_ALIAS.capitalize())

    def _class() -> Type:
        if STACK not in env_config.ALL_STACKS:
            raise ValueError(
                f"Stacks suitable for '{CLUSTER_NAME_ALIAS}' cluster name alias "
                f"are listed within the '{CLUSTER_NAME_ALIAS}' config. "
                f"Please ensure {env_config.__qualname__}.ALL_STACKS value contains '{STACK}'."
            )

        default_class_name = env_config.VALID_STACKS[PROJECT_NAME][STACK]["class_name"]

        try:
            custom_class_name = (
                f"{env_config.CLUSTER_NAME_ALIAS.capitalize()}{default_class_name}"
            )
            log.warning(">> Trying to use class: %s.", custom_class_name)

            return globals()[custom_class_name]
        except KeyError:
            log.warning(
                ">> Class %s%s not found, falling back to %s.",
                env_config.CLUSTER_NAME_ALIAS.capitalize(),
                default_class_name,
                default_class_name,
            )

            return globals()[default_class_name]

    _class()(scope=app, ns=STACK, config=env_config)
    app.synth()
