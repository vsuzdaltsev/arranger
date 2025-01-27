import pytest

from arranger_automation.parse import PatchK8sManifest

MANIFESTS = [
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
                            "envFrom": [{"configMapRef": {"name": "identity-config"}}],
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
IMAGE_TAG_PATCH_1 = {
    "key": "image",
    "value": "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service",
    "new_value": "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service:1.1.1",
}
IMAGE_TAG_PATCH_2 = {
    "key": "image",
    "value": "xxx.dkr.ecr.eu-west-2.amazonaws.com/web-backoffice-identity",
    "new_value": "xxx.dkr.ecr.eu-west-2.amazonaws.com/web-backoffice-identity:2.2.2",
}


class TestPatchK8sManifest:
    @staticmethod
    def test_add_valid_manifest_1():
        resulting_manifest = PatchK8sManifest(
            struct=MANIFESTS[0], patch=IMAGE_TAG_PATCH_1
        ).add()

        assert (
            resulting_manifest["spec"]["template"]["spec"]["containers"][0]["image"]
            == "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service:1.1.1"
        )

    @staticmethod
    def test_add_valid_manifest_2():
        resulting_manifest = PatchK8sManifest(
            struct=MANIFESTS[0], patch=IMAGE_TAG_PATCH_2
        ).add()

        assert (
            resulting_manifest["spec"]["template"]["spec"]["containers"][1]["image"]
            == "xxx.dkr.ecr.eu-west-2.amazonaws.com/web-backoffice-identity:2.2.2"
        )

    @staticmethod
    @pytest.mark.xfail(raises=BaseException)
    def test_add_invalid_manifest_1():
        resulting_manifest = PatchK8sManifest(
            struct=MANIFESTS[0], patch=IMAGE_TAG_PATCH_1
        ).add()

        assert (
            resulting_manifest["spec"]["template"]["spec"]["containers"][0]["image"]
            == "xxx.dkr.ecr.eu-west-2.amazonaws.com/identity-service"
        )

    @staticmethod
    @pytest.mark.xfail(raises=BaseException)
    def test_add_invalid_manifest_2():
        resulting_manifest = PatchK8sManifest(
            struct=MANIFESTS[0], patch=IMAGE_TAG_PATCH_2
        ).add()

        assert (
            resulting_manifest["spec"]["template"]["spec"]["containers"][1]["image"]
            == "xxx.dkr.ecr.eu-west-2.amazonaws.com/web-backoffice-identity"
        )
