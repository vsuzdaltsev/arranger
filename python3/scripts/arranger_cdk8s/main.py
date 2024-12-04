#!/usr/bin/env python3

import base64
import json
import sys
from argparse import ArgumentError
from typing import Any, Dict, List, NoReturn, Union

from awscli.customizations.datapipeline import ParameterDefinitionError
from cdk8s import App, Chart
from constructs import Construct

from arranger_cdk8s.arranger_services import *
from arranger_conf.arranger_conf import ArrangerConf
from arranger_conf.arranger_cdk8s_conf import K8sConf


INPUT_SERVICES = sys.argv[1]
ENVIRONMENT = sys.argv[2]
OVERRIDES = sys.argv[3]


class ArrangerApp(Chart):
    def __init__(
        self,
        scope: Construct,
        ns: str,
        config: Union[type(K8sConf), None] = None,
    ):
        super().__init__(scope, ns)

        self.ns = ns
        self.config = config

        if not config:
            raise ValueError("'Config' can't be None")

    @property
    def all_services(self) -> Dict[str, Any]:
        from arranger_conf.arranger_cdk8s_conf_lib._basic_service import BasicService

        return BasicService.valid_services()

    def render_service(self) -> NoReturn:
        try:
            _cdk8s_manifest_class = globals()[
                f"{self.config.ENVIRONMENT}{self.all_services[self.ns]['class_name']}"
            ]
        except KeyError:
            _cdk8s_manifest_class = globals()[
                f"{self.all_services[self.ns]['class_name']}"
            ]

        _cdk8s_manifest_class(
            self,
            self.ns,
            config=getattr(self.config, self.all_services[self.ns]["class_name"]),
            kwargs={"environment": ENVIRONMENT},
        )


if __name__ == "__main__":
    app = App(outdir="dist")

    if OVERRIDES != "None":
        message_bytes = base64.b64decode(OVERRIDES)
        overrides = json.loads(message_bytes)

        for override in overrides:
            obj_name = ".".join(override.split(".")[0:-1])
            attr_name = override.split(".")[-1]
            new_attr_value = overrides[override]
            setattr(eval(obj_name), attr_name, new_attr_value)

    env_config = getattr(K8sConf, ENVIRONMENT.capitalize())

    def services() -> List[str]:
        if "all-services" in INPUT_SERVICES:
            if INPUT_SERVICES == "all-services":
                return env_config.ALL_SERVICES

            raise ParameterDefinitionError(
                "'all-services' should not be combined with other service names."
            )

        return [s.rstrip().lstrip() for s in INPUT_SERVICES.split(",")]

    for service in services():
        ArrangerApp(app, ns=service, config=env_config).render_service()

    app.synth()
