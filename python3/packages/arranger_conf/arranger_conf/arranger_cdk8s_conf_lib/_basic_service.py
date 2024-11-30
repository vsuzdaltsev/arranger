from functools import reduce
from typing import Any, Dict, List, Union


def labels(service_type: str) -> Dict[str, Any]:
    return {"service_type": service_type}


class BasicService:
    @classmethod
    def environment(cls):
        return cls.outer_class(cls).split(".")[-1].lower()

    @classmethod
    def env_globals(cls):
        from arranger_globals import ByEnvironment

        return ByEnvironment(environment=cls.environment())

    @classmethod
    def valid_services(cls, with_repo_prefixes: bool = True) -> Dict[str, Any]:
        def repo(
            name: str,
            prefix: str = "",
            migrations_image: Union[str, None] = None,
            aux_images: Union[List[Dict[str, str]], None] = None,
            defaults: bool = True,
            image: Union[Dict[str, str], None] = None,
        ):
            """Inject defaults to the repo definition."""
            migrations_dockerfile = "Dockerfile.migrate" if migrations_image else None
            name = f"{prefix}{name}" if with_repo_prefixes else name

            if defaults:
                image_name = name
                dockerfile = "Dockerfile"
            else:
                image_name = image.get("image_name")
                dockerfile = image.get("dockerfile")

            return {
                "name": name,
                "image": {"dockerfile": dockerfile, "image_name": image_name},
                "migrations_image": {
                    "dockerfile": migrations_dockerfile,
                    "image_name": migrations_image,
                },
                "aux_images": aux_images,
            }

        return {
            "gateway": {
                "class_name": "Gateway",
                "repos": [],
                "labels": labels(service_type="arranger_app"),
            },
            "httpbin": {
                "class_name": "Httpbin",
                "repos": [],
                "labels": labels(service_type="arranger_app"),
            },
        }

    RESOURCES = {
        "limits": {"memory": "150Mi"},
        "requests": {"memory": "50Mi", "cpu": "10m"},
    }
    JOB_RESOURCES = {
        "limits": {"memory": "200Mi"},
        "requests": {"memory": "50Mi", "cpu": "10m"},
    }

    @staticmethod
    def outer_class(klass):
        return ".".join(klass.__qualname__.split(".")[0:-1])

    @classmethod
    @property
    def service_name(cls):
        return reduce(
            lambda x, y: x + ("-" if y.isupper() else "") + y, cls.__name__
        ).lower()
