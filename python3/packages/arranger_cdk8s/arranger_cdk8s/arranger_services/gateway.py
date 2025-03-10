"""
K8s objects generator for the Istio Gateway.

Source code:
    https://github.com
"""

from ._basic_gateway import BasicGateway
from ._basic_service import Construct, Dict, K8sConf


class Gateway(BasicGateway):
    """Generate all related K8s manifests for Istio Gateway."""

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        config: K8sConf,
        kwargs: Dict[str, str] = None,
    ):
        super().__init__(scope=scope, id=id, config=config, kwargs=kwargs)

        self.config = config
        self.kwargs = kwargs
        self.environment = self.kwargs.get("environment")

        hosts = [f"*.{self.environment}.{self.globals.hosted_zone_domain_name}"]

        self._generate_gateway(
            hosts=hosts,
            patches=[
                self._add("/metadata/name", self.environment),
            ],
        )
