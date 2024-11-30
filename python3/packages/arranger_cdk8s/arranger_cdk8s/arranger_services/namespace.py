"""K8s objects generator for the Namespace."""

from constructs import Construct

from ._basic_service import BasicService


class Namespace(BasicService):
    """Generate all related K8s manifests for the Namespace."""

    def __init__(self, scope: Construct, id: str, *, config, kwargs=None):
        super().__init__(scope=scope, id=id, config=config, kwargs=kwargs)

        self._generate_namespace()
        # self._default_limit_range()
