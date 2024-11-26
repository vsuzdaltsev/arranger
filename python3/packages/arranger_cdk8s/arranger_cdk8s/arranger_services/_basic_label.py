class BasicLabel:
    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    def __init__(self, service_name, service_globals, resource_name):
        self.resource_name = resource_name
        self.service_name = service_name
        self.service_globals = service_globals

    @property
    def common_labels(self):
        base = {"service": self.service_name} | self._environment

        return base | {"resource_name": self.resource_name}

    @property
    def _environment(self):
        if hasattr(self.service_globals, "environment"):
            return {"environment": self.service_globals.environment}

        return {}
