"""
K8s objects generator for the Httpbin service.

Source code:
    https://github.com
"""

from ._basic_service import BasicService, Construct, Dict, K8sConf


class Httpbin(BasicService):
    """Generate all related K8s manifests for the Httpbin service."""

    service_name = "httpbin"

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        config: K8sConf,
        kwargs: Dict[str, str] = None,
    ):
        super().__init__(scope=scope, id=id, config=config, kwargs=kwargs)

        self._generate_config_map()
        self._generate_deployment()
        self._generate_service_account(namespace=self.environment)
        self._generate_service()
        self._generate_virtual_service(
            http_match_prefix=f"/{self.service_name}/",
            rewrite="/",
            hosts=[f"api.{self.environment}.{self.globals.hosted_zone_domain_name}"],
            destination_host=self.service_name,
            add_request_headers={"X-Forwarded-Prefix": f"/{self.service_name}"},
        )
