from typing import Dict

import arranger_globals

from ._basic_conf import BasicConf, cluster_name_alias_from_module_name
from ._basic_service import BasicService


def _eg(env: str) -> type(arranger_globals.BySubEnvironment):
    return arranger_globals.BySubEnvironment(sub_environment=env)


def _cg(tenant: str) -> type(arranger_globals.ByTenant):
    return arranger_globals.ByTenant(tenant=tenant)


def _ecr_image(name: str) -> str:
    return _cg(tenant=cluster_name_alias_from_module_name()).ecr(repository=name)


class Development1(BasicConf):
    ALL_SERVICES = {
        name: metadata
        for name, metadata in BasicService.valid_services().items()
        if metadata.get("labels", {}).get("service_type") in ["arranger_app"]
        and name in ["httpbin"]
    }

    class Httpbin(BasicService):
        REPLICAS = 1
        IMAGE = "httpbin"
        SERVICE_PORT = 8080
        CONTAINER_PORT = 8080
        RESOURCES = {
            "requests": {"memory": "50Mi", "cpu": "20m"},
            "limits": {"memory": "600Mi"},
        }

        def CONFIG_MAP_DATA(self, attr: Dict[str, str]):
            cg = _eg(env=attr.get("environment"))
            # secret = cg.secret(service_name=self.service_name)

            return {
                "ENV_NAME": cg.sub_environment,
            }
