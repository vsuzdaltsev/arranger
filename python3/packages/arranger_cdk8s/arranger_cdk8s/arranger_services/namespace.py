"""
K8s objects generator for the K8s namespace.

Source code:
    https://github.com
"""

from ._basic_service import BasicService, Construct, Dict, K8sConf


class Namespace(BasicService):
    """Generate all related K8s manifests for the Namespace."""

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        config: K8sConf,
        kwargs: Dict[str, str] = None
    ):
        super().__init__(scope=scope, id=id, config=config, kwargs=kwargs)

        self._generate_namespace()
        self._default_limit_range()
