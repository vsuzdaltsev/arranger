import inspect
import pathlib
from typing import Dict

from ._basic_service import BasicService


# TODO: replace with globals
def cluster_name_alias_from_module_name():
    filename = inspect.stack()[1].filename
    module_name = pathlib.Path(filename).stem

    return module_name


class BasicConf:
    @classmethod
    def env_globals(cls):
        from arranger_globals import ByEnvironment

        return ByEnvironment(environment=f"{cls.environment}")

    @classmethod
    @property
    def ENVIRONMENT(cls) -> str:
        return cls.__name__

    @classmethod
    @property
    def environment(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    @property
    def ALL_SERVICES(cls) -> Dict[str, Dict]:
        return {
            name: metadata
            for name, metadata in BasicService.valid_services().items()
            if metadata.get("labels", {}).get("service_type") in ["arranger_app"]
        }

    SERVICES_WITH_POSTGRES_SWITCH = {
        "config-service-ms": {"pg_extensions": ["pgcrypto", "plpgsql"]},
    }
