"""K8s objects generator for Abstract service."""

from typing import Any, Dict, List, Union

from cdk8s import JsonPatch, ApiObjectMetadata
from constructs import Construct

from arranger_conf import ArrangerConf, K8sConf
from arranger_globals.cdk8s_globals import Cdk8sGlobals

from arranger_cdk8s.imports.com.coreos.monitoring import (
    ServiceMonitor,
    ServiceMonitorSpec,
    ServiceMonitorSpecEndpoints,
    ServiceMonitorSpecSelector,
)
from arranger_cdk8s.imports import k8s
from arranger_cdk8s.imports.networking.istio.io.virtualservice import (
    VirtualService,
    VirtualServiceSpec,
    VirtualServiceSpecHttp,
    VirtualServiceSpecHttpMatch,
    VirtualServiceSpecHttpMatchUri,
    VirtualServiceSpecHttpRewrite,
    VirtualServiceSpecHttpRoute,
    VirtualServiceSpecHttpRouteDestination,
    VirtualServiceSpecHttpRouteDestinationPort,
    VirtualServiceSpecHttpRouteHeaders,
    VirtualServiceSpecHttpRouteHeadersRequest,
)


from ._basic_mixin import BasicMixin


def camel_to_snake(s: str) -> str:
    return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")


def camel_to_kebab(s: str) -> str:
    return "".join(
        "-" + char.lower() if char.isupper() and i > 0 else char.lower()
        for i, char in enumerate(s)
    )


class BasicService(Construct, BasicMixin):
    """Generate all related K8s manifests."""

    service_name = "basic_service"

    DEFAULT_MEMORY_REQUEST = "50Mi"
    DEFAULT_CPU_REQUEST = "30m"

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        config: K8sConf,
        kwargs: Dict[str, str] = None,
    ):
        super().__init__(scope, id)

        self.scope = scope
        self.config = config
        self.kwargs = kwargs
        self.environment = self.kwargs.get("environment")
        self.globals = Cdk8sGlobals(environment=self.environment, config=config)
        self.tf_globals = self._tf_globals()

    @property
    def _tf_globals(self):
        from arranger_conf.arranger_cdktf_conf import TfConf

        return getattr(TfConf, self.globals.tenant.capitalize())

    @staticmethod
    def _args(commands: List[str]) -> Union[List[str], None]:
        if not commands:
            return None

        return ["\n".join(commands)]

    def _generate_config_map(self, name=None) -> k8s.ConfigMap:
        if not name:
            name = self._config_map_name

        variables = {}

        def _stringify_values(_dict: Dict[str, Any]) -> Dict[str, str]:

            output_dict = {}
            for key, value in _dict.items():
                output_dict[key] = str(value)
            return output_dict

        variables.update(
            _stringify_values(
                _dict=self.config.CONFIG_MAP_DATA(
                    self=self.config, attr={"environment": self.environment}
                )
            )
        )

        return k8s.ConfigMap(
            scope=self,
            id=name,
            metadata=k8s.ObjectMeta(name=name),
            data=variables,
        )

    def _patch_virtual_service_name(self, value=None) -> JsonPatch:
        if not value:
            value = self._virtual_service_name

        return JsonPatch.add(path="/metadata/name", value=value)

    def _generate_service_account(
        self,
        service_account_name=None,
        service_account_annotations=None,
        namespace=None,
    ) -> k8s.ServiceAccount:
        return k8s.ServiceAccount(
            self,
            id=self.service_name + "-service-account",
            metadata=k8s.ObjectMeta(
                name=service_account_name or self.service_name,
                annotations=service_account_annotations,
                namespace=namespace,
            ),
        )

    @staticmethod
    def _patch(route: str, value: Any) -> JsonPatch:
        return JsonPatch.replace(path=route, value=value)

    @staticmethod
    def _remove(route: str) -> JsonPatch:
        return JsonPatch.remove(path=route)

    @staticmethod
    def _add(route: str, value: Any) -> JsonPatch:
        return JsonPatch.add(path=route, value=value)

    @property
    def _env_from_config(self) -> List:
        return [
            k8s.EnvFromSource(
                config_map_ref=k8s.ConfigMapEnvSource(name=self._config_map_name)
            )
        ]

    @staticmethod
    def _resource_requirements(memory: str = "400Mi") -> k8s.ResourceRequirements:
        return k8s.ResourceRequirements(
            limits={"memory": k8s.Quantity.from_string(memory)}
        )

    def init_container_resources(self, resources: Union[Dict, None] = None):
        return self._custom_resource_requirements(resources=resources)

    def _custom_resource_requirements(
        self,
        resources: Dict = None,
    ) -> Union[k8s.ResourceRequirements, None]:
        if not resources:
            if not self.config.RESOURCES:
                return None

            resources = self.config.RESOURCES

        resources_quantity = {}
        for k, v in resources.items():
            resources_quantity[k] = {}
            for sub_k, sub_v in v.items():
                resources_quantity[k][sub_k] = k8s.Quantity.from_string(sub_v)

        return k8s.ResourceRequirements(**resources_quantity)

    @property
    def _istio_sidecar_injection(self) -> Dict[str, str]:
        return {"sidecar.istio.io/inject": "false"}

    @property
    def _image_pull_policy(self) -> str:
        return "Always"

    @property
    def _ttl_seconds_after_finish(self) -> int:
        return 30

    @property
    def _command(self) -> List[str]:
        return ["/bin/sh", "-c"]

    @property
    def _virtual_service_name(self) -> str:
        return self.service_name

    @property
    def _config_map_name(self) -> str:
        return f"{self.service_name}-config"

    @property
    def _deployment_label(self) -> Dict[str, str]:
        return {"deployment": self.service_name}

    def _default_limit_range(
        self, namespace_name: Union[str, None] = None
    ) -> k8s.LimitRange:
        if not namespace_name:
            namespace_name = self.environment

        if self.environment == "local":
            return None

        return k8s.LimitRange(
            self,
            id="default-limit",
            metadata=k8s.ObjectMeta(namespace=namespace_name, name="default-limit"),
            spec=k8s.LimitRangeSpec(
                limits=[
                    k8s.LimitRangeItem(
                        type="Container",
                        default_request={
                            "memory": k8s.Quantity.from_string(
                                self.DEFAULT_MEMORY_REQUEST
                            ),
                            "cpu": k8s.Quantity.from_string(self.DEFAULT_CPU_REQUEST),
                        },
                    )
                ]
            ),
        )

    def _generate_namespace(
        self, name: Union[str, None] = None, istio_injection: str = "enabled"
    ) -> k8s.Namespace:
        if not name:
            name = self.environment

        return k8s.Namespace(
            self,
            id=name,
            metadata=k8s.ObjectMeta(
                name=name, labels={"istio-injection": istio_injection}
            ),
        )

    @property
    def _namespace_name(self) -> str:
        return self.environment

    def __repr__(self) -> str:
        return f"{super().__repr__()}: {self.__dict__}"

    @property
    def tenant(self) -> Union[str, None]:
        for cluster_name, cluster_conf in ArrangerConf.TENANTS.items():
            if self.environment == cluster_name:
                return cluster_name

            if cluster_conf.get(
                "environments"
            ) and self.environment in cluster_conf.get("environments"):
                return cluster_name

        return None

    @property
    def default_hosts(self):
        if self.globals.is_environment:
            return self._service_hosts(prefix=f"{self.environment}.")

        return self.config.VIRTUAL_HOSTS

    def _service_hosts(self, prefix: str = ""):
        return [f"{prefix}{host}" for host in self.config.VIRTUAL_HOSTS]

    @property
    def environment_variables(self) -> Union[List[k8s], None]:
        # TODO: please check code sanity.
        if callable(getattr(self.config, "ENVIRONMENT_VARIABLES", None)):
            env_vars = []
            env = self.kwargs.get("environment").lower()
            variables = self.config().ENVIRONMENT_VARIABLES(env=env)
            for name, value in variables.items():
                env_vars.append(k8s.EnvVar(name=name, value=value))

            return env_vars

    def _generate_deployment(
        self,
        name=None,
        patches=None,
        container_name=None,
        service_account_name=None,
        strategy=None,
        container_ports: List[int] = None,
        resources=None,
        init_containers: List[str] = None,
        command=None,
        args=None,
        volumes=None,
        volume_mounts=None,
    ) -> k8s.Deployment:
        name = name or self.service_name
        container_ports = container_ports or [self.config.CONTAINER_PORT]
        container_name = container_name or self.service_name
        service_account_name = service_account_name or self.service_name
        resources = self._custom_resource_requirements(resources=resources)

        if not init_containers:
            init_containers = []

        def _init_containers():
            _containers = []

            _containers.extend(init_containers)
            return _containers

        deployment = k8s.Deployment(
            scope=self,
            id=f"{name}-deployment",
            metadata=k8s.ObjectMeta(name=name),
            spec=k8s.DeploymentSpec(
                strategy=strategy,
                replicas=self.config.REPLICAS,
                selector=k8s.LabelSelector(match_labels=self._deployment_label),
                template=k8s.PodTemplateSpec(
                    metadata=k8s.ObjectMeta(
                        labels={
                            **self._deployment_label,
                            **self._common_labels(resource_name=name),
                        },
                    ),
                    spec=k8s.PodSpec(
                        init_containers=_init_containers(),
                        service_account_name=service_account_name,
                        containers=[
                            k8s.Container(
                                name=container_name,
                                image=self.config.IMAGE,
                                image_pull_policy=self._image_pull_policy,
                                env_from=self._env_from_config,
                                env=[
                                    k8s.EnvVar(
                                        name="POD_UID",
                                        value_from=k8s.EnvVarSource(
                                            field_ref=k8s.ObjectFieldSelector(
                                                field_path="metadata.uid"
                                            )
                                        ),
                                    ),
                                ],
                                ports=[
                                    k8s.ContainerPort(container_port=p)
                                    for p in container_ports
                                ],
                                resources=resources,
                                command=command,
                                args=self._args(commands=args),
                                volume_mounts=volume_mounts,
                            )
                        ],
                        volumes=volumes,
                    ),
                ),
            ),
        )

        if patches:
            for patch in patches:
                deployment.add_json_patch(patch)

        return deployment

    def _generate_service(self, patches=None, port_name=None) -> k8s.Service:
        def _port_name():
            if port_name:
                return port_name

            return f"http-{self.service_name}"

        service = k8s.Service(
            scope=self,
            id=self.service_name + "-service",
            metadata=k8s.ObjectMeta(
                name=self.service_name,
                labels={"app": self.service_name, "service": self.service_name},
            ),
            spec=k8s.ServiceSpec(
                ports=[
                    k8s.ServicePort(
                        name=_port_name(),
                        protocol="TCP",
                        port=self.config.SERVICE_PORT,
                        target_port=k8s.IntOrString.from_number(
                            self.config.CONTAINER_PORT
                        ),
                    )
                ],
                selector=self._deployment_label,
            ),
        )

        if patches:
            for patch in patches:
                service.add_json_patch(patch)

        return service

    def _generate_virtual_service(
        self,
        patches=None,
        hosts=None,
        gateways=None,
        http_match_prefix=None,
        destination_host=None,
        add_request_headers=None,
        rewrite=None,
        name_postfix="",
    ) -> VirtualService:
        gateways = gateways or [self.environment]
        add_request_headers = add_request_headers
        virtual_service = VirtualService(
            scope=self,
            name=f"{self._virtual_service_name}-virtual-service{name_postfix}",
            spec=VirtualServiceSpec(
                hosts=hosts or self.default_hosts,
                gateways=gateways,
                http=[
                    VirtualServiceSpecHttp(
                        match=[
                            VirtualServiceSpecHttpMatch(
                                uri=VirtualServiceSpecHttpMatchUri(
                                    prefix=http_match_prefix
                                )
                            )
                        ],
                        rewrite=(
                            None
                            if not rewrite
                            else VirtualServiceSpecHttpRewrite(uri=rewrite)
                        ),
                        route=[
                            VirtualServiceSpecHttpRoute(
                                destination=VirtualServiceSpecHttpRouteDestination(
                                    host=f"{destination_host}.{self._namespace_name}.svc.cluster.local",
                                    port=VirtualServiceSpecHttpRouteDestinationPort(
                                        number=self.config.CONTAINER_PORT
                                    ),
                                ),
                                headers=VirtualServiceSpecHttpRouteHeaders(
                                    request=VirtualServiceSpecHttpRouteHeadersRequest(
                                        add=add_request_headers
                                    )
                                ),
                            )
                        ],
                    )
                ],
            ),
        )
        virtual_service.add_json_patch(
            self._patch_virtual_service_name(
                value=self._virtual_service_name + name_postfix
            )
        )

        if patches:
            for patch in patches:
                virtual_service.add_json_patch(patch)

        return virtual_service

    def _generate_service_monitor(self, interval="15s", patches=None):
        name = f"{self.service_name}-service-monitor"

        _sm = ServiceMonitor(
            scope=self,
            id=name,
            spec=ServiceMonitorSpec(
                endpoints=[
                    ServiceMonitorSpecEndpoints(
                        scheme="http",
                        path="/actuator/prometheus",
                        port=f"http-{self.service_name}",
                        interval=interval,
                    )
                ],
                selector=ServiceMonitorSpecSelector(
                    match_labels={
                        "app": self.service_name,
                    },
                ),
            ),
            metadata=ApiObjectMetadata(
                labels={"release": self.globals.kube_prometheus_stack_name},
                name=name,
                namespace=self._namespace_name,
            ),
        )

        if patches:
            for patch in patches:
                _sm.add_json_patch(patch)

        return _sm

    def _probe(self, probe_metadata: Dict[str, Any]) -> k8s.Probe:
        if probe_metadata:
            initial_delay_seconds = probe_metadata.get("initial_delay_seconds")
            period_seconds = probe_metadata.get("period_seconds")
            path = probe_metadata.get("path")

            return k8s.Probe(
                http_get=k8s.HttpGetAction(
                    port=k8s.IntOrString.from_number(self.config.CONTAINER_PORT),
                    path=path,
                ),
                initial_delay_seconds=initial_delay_seconds,
                period_seconds=period_seconds,
            )
