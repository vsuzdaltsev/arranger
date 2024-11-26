from constructs import Construct

from ._basic_gateway import BasicGateway


class Gateway(BasicGateway):
    """Generate all related K8s manifests for Istio Gateways."""

    def __init__(self, scope: Construct, id: str, *, config, kwargs=None):
        super().__init__(scope=scope, id=id, config=config, kwargs=kwargs)

        self.config = config
        self.kwargs = kwargs
        self.environment = self.kwargs.get("environment")

        hosts = (
            [f"*.{self.environment}.{self.globals.hosted_zone_domain_name}"]
            if self.globals.is_sub_environment
            else [f"*.{self.globals.hosted_zone_domain_name}"]
        )

        self._generate_gateway(
            hosts=hosts,
            patches=[
                self._add("/metadata/name", self.environment),
            ],
        )
