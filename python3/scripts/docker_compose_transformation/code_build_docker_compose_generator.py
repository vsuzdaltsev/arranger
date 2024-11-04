#!/usr/bin/env python

import os
import sys
from typing import TextIO

import yaml


class DockerComposeTransformator:
    """Transform meta-cli docker-compose file to support AWS CodeBuild pipelines."""

    FILE_NAME = "docker-compose.yaml"
    SERVICE_NAME = "eusy"
    PATTERN_TO_REPLACE = "."
    ROOT_PATH = "/opt/meta"
    IMAGE = (
        "${AWS_ACCOUNT_ID}."
        "dkr.ecr."
        "${AWS_REGION}."
        "amazonaws.com"
        "/meta-cli-switch:${META_SERVICE_CODEBUILD_IMAGE_TAG}"
    )
    REMOVE_SECRETS_BINDING = "FALSE"

    def __init__(self):
        self.yaml_dict = None
        self.read_file()

    def read_file(self):
        with open(f"{self.ROOT_PATH}/{self.FILE_NAME}", "r") as data:
            self.yaml_dict = self.yaml_transform(data_input=data)

    def write_file(self):
        with open(
            f"{self.ROOT_PATH}/{self.SERVICE_NAME}-{self.FILE_NAME}", "w"
        ) as data:
            data.write(yaml.safe_dump(self.yaml_dict))

    def patch_path(self, item_to_patch: str) -> str:
        if item_to_patch[0] == self.PATTERN_TO_REPLACE:
            return item_to_patch.replace(self.PATTERN_TO_REPLACE, self.ROOT_PATH, 1)

        return item_to_patch

    def yaml_transform(self, data_input: TextIO):
        yaml_object = yaml.full_load(data_input)

        yaml_object["services"]["cli"]["image"] = self.IMAGE
        yaml_object["services"]["cli"]["build"]["context"] = self.ROOT_PATH

        clean_volumes = []

        for path in yaml_object["services"]["cli"]["volumes"]:
            if isinstance(path, str):
                clean_volumes.append(self.patch_path(item_to_patch=path))
            else:
                if self.REMOVE_SECRETS_BINDING == "TRUE":
                    if isinstance(path, dict) and not path.get("source", "").startswith(
                        "./.secrets"
                    ):
                        clean_volumes.append(path)
                else:
                    clean_volumes.append(path)

        yaml_object["services"]["cli"]["volumes"] = clean_volumes

        return yaml_object


if __name__ == "__main__":
    DockerComposeTransformator.ROOT_PATH = os.getenv("CODEBUILD_SRC_DIR")
    DockerComposeTransformator.REMOVE_SECRETS_BINDING = os.getenv(
        "REMOVE_SECRETS_BINDING", DockerComposeTransformator.REMOVE_SECRETS_BINDING
    ).upper()
    DockerComposeTransformator().write_file()

    sys.exit(0)
