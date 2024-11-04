"""Inject patches to K8s manifests."""

import json
from typing import Dict, List, Union


class PatchK8sManifest:
    """Apply patch to given k8s manifest."""

    def __init__(self, struct: Dict, patch: Union[Dict, None] = None):
        self.struct = struct
        self.patch = patch

    def add(self) -> Dict:
        """
        Add patch.
        This will recursively find occurrences of given key and value and replace old value with given new value.
        """
        if not self.patch:
            return self.struct

        return self._patch(struct=self.struct)

    @property
    def _patch_key(self) -> Union[str, None]:
        return self.patch.get("key")

    @property
    def _patch_value(self) -> Union[str, None]:
        return self.patch.get("value")

    @property
    def _patch_new_value(self) -> Union[str, None]:
        return self.patch.get("new_value")

    def _patch(self, struct: Dict) -> Dict:
        for key, value in struct.items():
            if key == self._patch_key and value == self._patch_value:
                struct[key] = self._patch_new_value
            elif isinstance(value, dict):
                self._patch(struct=value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._patch(struct=item)
        return struct

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"


class PatchK8sManifestImageTag:
    """Apply patch to given k8s manifest."""

    def __init__(
        self,
        struct: Dict,
        image_tag: Union[str, None] = None,
        excludes: Union[List[str], None] = None,
    ):
        self.struct = struct
        self.tag = image_tag
        self.excludes = excludes if excludes else []

    def add(self) -> Dict:
        """
        Add patch.
        This will recursively find occurrences of given key and value and replace old value with given new value.
        """
        if not self.tag:
            return self.struct

        return self._patch(struct=self.struct)

    def _patch(self, struct: Dict) -> Dict:
        for key, value in struct.items():
            if key == "image" and value not in self.excludes:
                struct[key] = f"{value}:{self.tag}"
            elif isinstance(value, dict):
                self._patch(struct=value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._patch(struct=item)
        return struct

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"


if __name__ == "__main__":
    manifests = [
        {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {"name": "identity-deployment"},
            "spec": {
                "replicas": 2,
                "selector": {"matchLabels": {"deployment": "identity-deployment"}},
                "template": {
                    "metadata": {"labels": {"deployment": "identity-deployment"}},
                    "spec": {
                        "containers": [
                            {
                                "name": "api",
                                "image": "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service",
                                "imagePullPolicy": "Always",
                                "ports": [{"containerPort": 3001}],
                                "envFrom": [
                                    {"configMapRef": {"name": "identity-config"}}
                                ],
                                "resources": {"limits": {"memory": "300Mi"}},
                            },
                            {
                                "name": "web",
                                "image": "xxx.dkr.ecr.eu-west-2.amazonaws.com/web-backoffice-identity",
                                "imagePullPolicy": "Always",
                                "ports": [{"containerPort": 80}],
                            },
                        ]
                    },
                },
            },
        },
    ]

    image_patch = {
        "key": "image",
        "value": "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service",
        "new_value": "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service:1.1.1",
    }

    print(
        json.dumps(
            [PatchK8sManifest(struct=m, patch=image_patch).add() for m in manifests]
        )
    )
    print(
        json.dumps(
            [
                PatchK8sManifestImageTag(struct=m, image_tag="7.8.9").add()
                for m in manifests
            ]
        )
    )
