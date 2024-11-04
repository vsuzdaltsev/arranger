"""Manipulate Kubernetes Job objects."""

import json
import os
import time
from typing import Any, Dict, List, NoReturn, Union

from kubernetes import client, config

from arranger_automation.log import Log


class BasicJob:
    """Create and delete a Kubernetes Job object."""

    BACKOFF_LIMIT = 5
    DEFAULT_IMAGE = "python:3.9-alpine"
    DELETE_GRACE_PERIOD_SECONDS = 10
    PARALLELISM = 10
    SLEEP_BETWEEN_STATUS_READS = 1

    @staticmethod
    def _setup_env_variables(env_variables: Union[List, None]) -> List:
        """Environment variables for the Kubernetes Job."""
        return env_variables or []

    @staticmethod
    def _volume_type(volume: Dict) -> str:
        """
        Volume type.

        Available types are:
            secret, config_map.
        """
        return volume.get("type")

    def __repr__(self) -> str:
        """Class instance representation."""
        return f"{super().__repr__()}: {self.__dict__}"

    def _setup_labels(self, labels: Dict[str, str]) -> Dict[str, str]:
        """Labels for the Kubernetes Job."""
        default_label = {"app": self.name}
        if labels is None:
            return default_label

        self.log.debug(">> Add custom label: %s", labels)

        custom_labels = default_label
        custom_labels.update(labels)

        return custom_labels

    def _setup_volume_mounts(
        self, volume_mounts: Union[List[Dict[str, str]], None]
    ) -> List:
        """Setup volume mounts for given container."""
        if volume_mounts is None:
            self.log.debug(">> Volume mounts absent")
            return []

        vm_objects = []
        for volume in volume_mounts:
            name = volume.get("name")
            mount_path = volume.get("mount_path")
            self.log.debug(">> Add Volume Mount: %s -> %s", name, mount_path)
            vm_client = client.V1VolumeMount(name=name, mount_path=mount_path)
            vm_objects.append(vm_client)

        return vm_objects

    # TODO: add typing
    def _status(self):
        return self.instance.read_namespaced_job_status(
            name=self.name, namespace=self.namespace
        )

    def _wait_until_succeeded(self) -> NoReturn:
        """Wait until all pods of the job are in succeeded state."""
        status = self._status()
        active = status.status.active
        succeeded = status.status.succeeded
        while not isinstance(succeeded, int) and not succeeded == BasicJob.PARALLELISM:
            while active is not None:
                status = self._status()
                active = status.status.active
                succeeded = status.status.succeeded
                self.log.debug(">> Active: %s", active)
                self.log.debug(">> Succeeded: %s", succeeded)
                self.log.debug(
                    ">> Succeeded eq All: %s", BasicJob.PARALLELISM == succeeded
                )

                time.sleep(self.SLEEP_BETWEEN_STATUS_READS)

    def _container(self) -> type(client.V1Container):
        """Kubernetes Container object."""
        return client.V1Container(
            name=self.name,
            image=self.image,
            command=self.command,
            args=self.args,
            env=self.env_variables,
            volume_mounts=self._setup_volume_mounts(self.raw_volume_mounts),
        )

    def _template(self) -> type(client.V1PodTemplateSpec):
        """Pod template."""
        return client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels=self.labels),
            spec=client.V1PodSpec(
                restart_policy="Never",
                volumes=self._volumes(),
                containers=[self._container()],
            ),
        )

    def _spec(self) -> type(client.V1JobSpec):
        """Kubernetes Job object spec."""
        return client.V1JobSpec(
            template=self._template(),
            backoff_limit=self.BACKOFF_LIMIT,
            parallelism=self.PARALLELISM,
        )

    def _create_job_object(self) -> type(client.V1Job):
        """Kubernetes Job object."""
        return client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=client.V1ObjectMeta(name=self.name, labels=self.labels),
            spec=self._spec(),
        )

    def _volumes(self) -> List:
        """List of volumes."""
        volumes = []
        for volume in self.raw_volume_mounts:
            volume_type = self._volume_type(volume)
            volumes.append(getattr(self, f"_{volume_type}")(volume))

        return volumes

    def _config_map(self, volume) -> Dict:
        """To be dynamically called with getattr."""
        return {
            "name": volume.get("name"),
            "configMap": {"name": volume.get("name"), "defaultMode": self.default_mode},
        }

    def _secret(self, volume) -> Dict:
        """To be dynamically called with getattr."""
        return {
            "name": volume.get("name"),
            "secret": {
                "secretName": volume.get("name"),
                "defaultMode": self.default_mode,
            },
        }

    def __init__(
        self,
        name: str,
        command: List,
        args: List,
        image: str = DEFAULT_IMAGE,
        namespace: str = "default",
        labels: Union[Dict, None] = None,
        env_variables: Union[List, None] = None,
        volume_mounts: Union[List[Dict[str, str]], None] = None,
        default_mode: int = 384,
    ):
        """
        :param name: Kubernetes job name.
        :param command: Container's entrypoint command.
        :param args: Container's entrypoint command arguments.
        :param image: Docker image to use while running container.
        :param namespace: Kubernetes namespace to run the job in.
        :param labels: Pod labels to add.
        :param env_variables: Environment variables to pass to the job's pod.
        :param volume_mounts: Secrets to mount into the pod \
            E.g.:
                [
                    {
                        "type": "secret",
                        "name": "jumphost-id-rsa",
                        "mount_path": "/root/.ssh"
                    }
                ]
        :param default_mode: Default mode (decimal or octal, \
            see example: https://github.com/stephenmoloney/flux/commit/4ad833bdeddbaabcf0787b4fa4418b54711a849e) \
            for the mounted volumes.
        """
        self.log = Log.logger(desc=type(self).__name__)
        self.name = name
        self.image = image
        self.command = command
        self.args = args
        self.namespace = namespace
        self.labels = self._setup_labels(labels)
        self.env_variables = self._setup_env_variables(env_variables)
        self.raw_volume_mounts = volume_mounts
        self.default_mode = default_mode
        self.instance = client.BatchV1Api()
        self.job = self._create_job_object()

    @classmethod
    def auth(cls) -> Any:
        """Authorize Kubernetes client."""
        if os.getenv("KUBECONFIG"):
            config.load_kube_config()
        else:
            config.load_incluster_config()

    def create(self) -> NoReturn:
        """Apply Kubernetes Job."""
        api_response = self.instance.create_namespaced_job(
            body=self.job, namespace=self.namespace
        )
        self.log.debug(
            ">> Job created. Status: %s", json.dumps(str(api_response.status))
        )

    def delete(self, wait_until_succeeded: bool = False) -> NoReturn:
        """Delete Kubernetes Job."""

        if wait_until_succeeded:
            self._wait_until_succeeded()

        try:
            response = self.instance.delete_namespaced_job(
                name=self.name,
                namespace=self.namespace,
                body=client.V1DeleteOptions(
                    propagation_policy="Foreground",
                    grace_period_seconds=self.DELETE_GRACE_PERIOD_SECONDS,
                ),
            )
        except client.exceptions.ApiException:
            self.log.debug(">> Job %s already deleted", self.name)
            response = "Job already deleted"

        self.log.debug(">> Job deleted. Api response: %s", str(response))


if __name__ == "__main__":
    BasicJob.auth()
    BasicJob.PARALLELISM = 3

    job = BasicJob(
        name="worker",
        command=["python"],
        args=["-V"],
        env_variables=[
            {"name": "REQUEST_ID", "value": "737d64b9-2a29-4555-8ea1-39153b57d010"}
        ],
        labels={"environment": "dev"},
        volume_mounts=[
            {"type": "secret", "name": "jumphost-id-rsa", "mount_path": "/root/.ssh"},
            {
                "type": "config_map",
                "name": "worker-main",
                "mount_path": "/opt/build/app/main",
            },
        ],
        # decimal file mode permissions = 0600
        default_mode=384,
    )
    job.create()
    job.delete()
