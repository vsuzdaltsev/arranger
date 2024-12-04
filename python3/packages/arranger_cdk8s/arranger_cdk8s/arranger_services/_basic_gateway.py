from typing import Any, Dict

from cdk8s import JsonPatch
from constructs import Construct

from arranger_cdk8s.imports.networking.istio.io.gateway import Gateway as IstioGateway
from arranger_cdk8s.imports.networking.istio.io.gateway import (
    GatewaySpec as IstioGatewaySpec,
)
from arranger_cdk8s.imports.networking.istio.io.gateway import (
    GatewaySpecServers as IstioGatewaySpecServers,
)
from arranger_cdk8s.imports.networking.istio.io.gateway import (
    GatewaySpecServersPort as IstioGatewaySpecServersPort,
)

from arranger_conf import K8sConf


class BasicGateway(Construct):
    """Generate all related K8s manifests for Istio Gateways."""

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        config: K8sConf,
        kwargs: Dict[str, str] = None
    ):
        super().__init__(scope=scope, id=id)
        from arranger_globals.cdk8s_globals import Cdk8sGlobals

        self.config = config
        self.kwargs = kwargs
        self.environment = self.kwargs.get("environment")
        self.globals = Cdk8sGlobals(environment=self.environment, config=config)

    def _generate_gateway(
        self,
        name="main",
        selector="ingress",
        hosts=None,
        patches=None,
    ) -> IstioGateway:
        gateway = IstioGateway(
            self,
            name=name,
            spec=IstioGatewaySpec(
                selector={"istio": selector},
                servers=[
                    IstioGatewaySpecServers(
                        hosts=hosts or ["*"],
                        port=IstioGatewaySpecServersPort(
                            number=80, name="http", protocol="HTTP"
                        ),
                    ),
                ],
            ),
        )
        if patches:
            for patch in patches:
                gateway.add_json_patch(patch)

        return gateway

    @staticmethod
    def _add(route: str, value: Any) -> JsonPatch:
        return JsonPatch.add(path=route, value=value)
