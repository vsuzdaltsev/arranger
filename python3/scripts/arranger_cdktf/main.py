#!/usr/bin/env python3

import sys
from typing import Type

from cdktf import App

from arranger_automation.log import Log
from arranger_cdktf.arranger_terraform_stacks import *
from arranger_conf.arranger_cdktf_conf import TfConf


TENANT = sys.argv[1]
STACK = sys.argv[2]

if __name__ == "__main__":
    app = App(stack_traces=True)
    log = Log().logger(desc=str(app.__class__.__qualname__))

    env_config = getattr(TfConf, TENANT.capitalize())

    def _tf_stack_class() -> Type:
        if STACK not in env_config.ALL_STACKS:
            raise ValueError(
                f"Stacks suitable for '{TENANT}' tenant "
                f"are listed within the '{TENANT}' config. "
                f"Please ensure {env_config.__qualname__}.ALL_STACKS value contains '{STACK}'."
            )

        default_class_name = env_config.VALID_STACKS[STACK]["class_name"]

        try:
            custom_class_name = f"{env_config.TENANT.capitalize()}{default_class_name}"
            log.warning(">> Trying to use class: %s.", custom_class_name)

            return globals()[custom_class_name]
        except KeyError:
            log.warning(
                ">> Class %s%s not found, falling back to %s.",
                env_config.TENANT.capitalize(),
                default_class_name,
                default_class_name,
            )

            return globals()[default_class_name]

    _tf_stack_class()(scope=app, ns=STACK, config=env_config)
    app.synth()
