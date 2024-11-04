"""Build Docker image and push it to the given AWS ECR repo."""

import json
import os
from typing import Dict, Generator, NoReturn, Union

import docker

from arranger_automation.log import Log


class DockerException(Exception):
    pass


class DockerImage:
    """Manipulate Docker images: build, push to the Container Registry repo, pull from the repo."""

    DOCKER_API_CLIENT_BASE_URL = "unix://var/run/docker.sock"

    def __repr__(self) -> str:
        """Object string representation."""
        return f"{super().__repr__()}: {self.__dict__}"

    def _dockerhub_login(self):
        if not os.getenv("DOCKER_LICENSE_USER"):
            self.log.warning(
                ">> Set 'DOCKER_LICENSE_USER' environment variable to disable Dockerhub download images throttling."
            )
            return
        if not os.getenv("DOCKER_LICENSE_PASSWORD"):
            self.log.warning(
                ">> Set 'DOCKER_LICENSE_PASSWORD' environment variable to disable Dockerhub download images throttling."
            )
            return
        return self.docker_client.login(
            username=os.getenv("DOCKER_LICENSE_USER"),
            password=os.getenv("DOCKER_LICENSE_PASSWORD"),
            registry="https://index.docker.io/v1/",
        )

    def _parse_build_logs(
        self, log_generator: Generator, show_build_log: bool = False
    ) -> NoReturn:
        def print_build_log(js_output, err):
            if "stream" in js_output:
                if show_build_log:
                    self.log.warning(js_output["stream"].strip("\n"))

            if "error" in js_output:
                err.append(js_output["error"])

            if "errorDetail" in js_output:
                err.append(js_output["errorDetail"].get("message"))

                if "code" in js_output["errorDetail"]:
                    error_code = js_output["errorDetail"]["code"]
                    err.append(f"Error code: {error_code}")

        errors = []
        for line in log_generator:
            output = line.decode("utf8").strip("\r\n")
            try:
                # Check if it's multistream logs
                if "}\r\n{" in output:
                    output = "[" + output.replace("}\r\n{", "},{") + "]"
                    json_outputs = json.loads(output)
                    for out in json_outputs:
                        print_build_log(out, errors)
                else:
                    json_output = json.loads(output)
                    print_build_log(json_output, errors)
            except BaseException as err:
                if show_build_log:
                    self.log.warning(
                        f">> ERROR PARSING OUTPUT: '{output}'. Error: {err}."
                    )

        if errors:
            message = f"Docker build for {self.image_name} failed: {'. '.join(errors)}."
            raise DockerException(message)

    @property
    def local_repository(self) -> str:
        """Local Docker repository name."""
        return f"{self.image_name}:{self.tag}"

    def __init__(
        self,
        image_name: str,
        tag: str = "latest",
        context: str = ".",
        dockerfile: str = "Dockerfile",
        buildargs: Union[Dict, None] = None,
        **kwargs,
    ):
        self.log = Log.logger(desc=type(self).__name__)
        self.image_name = image_name
        self.tag = tag
        self.context = context
        self.dockerfile = dockerfile
        self.buildargs = buildargs
        self.docker_client = docker.from_env()
        self.dockerhub_login = self._dockerhub_login()
        self.kwargs = kwargs
        self.additional_tags = self.kwargs.get("additional_tags", [])

        self.image = None
        self.build_log = None

    def build(self, show_build_log: bool = True) -> NoReturn:
        """Build Docker image."""

        self.log.warning(
            ">> Image: %s. Tag: %s. Dockerhub login: %s.",
            self.image_name,
            self.tag,
            self.dockerhub_login,
        )
        docker_cl = docker.APIClient(base_url=self.DOCKER_API_CLIENT_BASE_URL)

        if not os.path.exists(f"{self.context}/{self.dockerfile}"):
            raise RuntimeError(
                f">> Dockerfile '{self.dockerfile}' doesn't exist within the Repo '{self.context}'..\n"
                f">> Please ensure you have provided the proper value for the Dockerfile name."
            )

        generator = docker_cl.build(
            path=self.context,
            dockerfile=self.dockerfile,
            tag=self.local_repository,
            buildargs=self.buildargs,
            rm=True,
        )

        self._parse_build_logs(log_generator=generator, show_build_log=show_build_log)

        self.image = self.docker_client.images.get(self.local_repository)

    def push(
        self, docker_registry: str, username: str = None, password: str = None
    ) -> str:
        """Push Docker image to the Container registry. Image is to be tagged with both given tag and latest tag."""

        self.docker_client.login(
            username=username, password=password, registry=f"https://{docker_registry}"
        )

        for tag in (self.tag, "latest", *self.additional_tags):
            # E.g.: docker tag nginx yaatest.azurecr.io/myrepo
            self.image.tag(f"{docker_registry}/{self.image_name}", tag=tag)
            out = self.docker_client.images.push(
                f"{docker_registry}/{self.image_name}", tag=tag
            )

            if '"errorDetail"' in out:
                message = f"Docker push for {docker_registry} failed: {out}."
                raise DockerException(message)

        return f"{docker_registry}/{self.image_name}"

    def remove_image(self, image: str) -> NoReturn:
        """Remove Docker image from the local Repository."""
        self.docker_client.images.remove(image, force=False)

    # def list_images(self) -> List:
    #     """List local Docker images within the given Repository."""
    #     return self.docker_client.images.list()
