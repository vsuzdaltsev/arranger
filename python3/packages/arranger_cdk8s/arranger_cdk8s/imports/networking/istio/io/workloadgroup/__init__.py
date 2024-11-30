import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


class WorkloadGroup(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioioworkloadgroup.WorkloadGroup",
):
    """
    :schema: WorkloadGroup
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["WorkloadGroupSpec"] = None,
    ) -> None:
        """Defines a "WorkloadGroup" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Describes a collection of workload instances. See more details at: https://istio.io/docs/reference/config/networking/workload-group.html
        """
        options = WorkloadGroupOptions(spec=spec)

        jsii.create(WorkloadGroup, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class WorkloadGroupOptions:
    def __init__(self, *, spec: typing.Optional["WorkloadGroupSpec"] = None) -> None:
        """
        :param spec: Describes a collection of workload instances. See more details at: https://istio.io/docs/reference/config/networking/workload-group.html

        :schema: WorkloadGroup
        """
        if isinstance(spec, dict):
            spec = WorkloadGroupSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["WorkloadGroupSpec"]:
        """Describes a collection of workload instances.

        See more details at: https://istio.io/docs/reference/config/networking/workload-group.html

        :schema: WorkloadGroup#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpec",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "probe": "probe", "template": "template"},
)
class WorkloadGroupSpec:
    def __init__(
        self,
        *,
        metadata: typing.Optional["WorkloadGroupSpecMetadata"] = None,
        probe: typing.Optional["WorkloadGroupSpecProbe"] = None,
        template: typing.Optional["WorkloadGroupSpecTemplate"] = None,
    ) -> None:
        """Describes a collection of workload instances.

        See more details at: https://istio.io/docs/reference/config/networking/workload-group.html

        :param metadata: Metadata that will be used for all corresponding ``WorkloadEntries``.
        :param probe: ``ReadinessProbe`` describes the configuration the user must provide for healthchecking on their workload.
        :param template: Template to be used for the generation of ``WorkloadEntry`` resources that belong to this ``WorkloadGroup``.

        :schema: WorkloadGroupSpec
        """
        if isinstance(metadata, dict):
            metadata = WorkloadGroupSpecMetadata(**metadata)
        if isinstance(probe, dict):
            probe = WorkloadGroupSpecProbe(**probe)
        if isinstance(template, dict):
            template = WorkloadGroupSpecTemplate(**template)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if probe is not None:
            self._values["probe"] = probe
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def metadata(self) -> typing.Optional["WorkloadGroupSpecMetadata"]:
        """Metadata that will be used for all corresponding ``WorkloadEntries``.

        :schema: WorkloadGroupSpec#metadata
        """
        result = self._values.get("metadata")
        return result

    @builtins.property
    def probe(self) -> typing.Optional["WorkloadGroupSpecProbe"]:
        """``ReadinessProbe`` describes the configuration the user must provide for healthchecking on their workload.

        :schema: WorkloadGroupSpec#probe
        """
        result = self._values.get("probe")
        return result

    @builtins.property
    def template(self) -> typing.Optional["WorkloadGroupSpecTemplate"]:
        """Template to be used for the generation of ``WorkloadEntry`` resources that belong to this ``WorkloadGroup``.

        :schema: WorkloadGroupSpec#template
        """
        result = self._values.get("template")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class WorkloadGroupSpecMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """Metadata that will be used for all corresponding ``WorkloadEntries``.

        :param annotations: 
        :param labels: 

        :schema: WorkloadGroupSpecMetadata
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: WorkloadGroupSpecMetadata#annotations
        """
        result = self._values.get("annotations")
        return result

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: WorkloadGroupSpecMetadata#labels
        """
        result = self._values.get("labels")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecProbe",
    jsii_struct_bases=[],
    name_mapping={
        "exec": "exec",
        "failure_threshold": "failureThreshold",
        "http_get": "httpGet",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "tcp_socket": "tcpSocket",
        "timeout_seconds": "timeoutSeconds",
    },
)
class WorkloadGroupSpecProbe:
    def __init__(
        self,
        *,
        exec: typing.Optional["WorkloadGroupSpecProbeExec"] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_get: typing.Optional["WorkloadGroupSpecProbeHttpGet"] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        tcp_socket: typing.Optional["WorkloadGroupSpecProbeTcpSocket"] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        """``ReadinessProbe`` describes the configuration the user must provide for healthchecking on their workload.

        :param exec: Health is determined by how the command that is executed exited.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded.
        :param http_get: 
        :param initial_delay_seconds: Number of seconds after the container has started before readiness probes are initiated.
        :param period_seconds: How often (in seconds) to perform the probe.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed.
        :param tcp_socket: Health is determined by if the proxy is able to connect.
        :param timeout_seconds: Number of seconds after which the probe times out.

        :schema: WorkloadGroupSpecProbe
        """
        if isinstance(exec, dict):
            exec = WorkloadGroupSpecProbeExec(**exec)
        if isinstance(http_get, dict):
            http_get = WorkloadGroupSpecProbeHttpGet(**http_get)
        if isinstance(tcp_socket, dict):
            tcp_socket = WorkloadGroupSpecProbeTcpSocket(**tcp_socket)
        self._values: typing.Dict[str, typing.Any] = {}
        if exec is not None:
            self._values["exec"] = exec
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if http_get is not None:
            self._values["http_get"] = http_get
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if tcp_socket is not None:
            self._values["tcp_socket"] = tcp_socket
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def exec(self) -> typing.Optional["WorkloadGroupSpecProbeExec"]:
        """Health is determined by how the command that is executed exited.

        :schema: WorkloadGroupSpecProbe#exec
        """
        result = self._values.get("exec")
        return result

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        """Minimum consecutive failures for the probe to be considered failed after having succeeded.

        :schema: WorkloadGroupSpecProbe#failureThreshold
        """
        result = self._values.get("failure_threshold")
        return result

    @builtins.property
    def http_get(self) -> typing.Optional["WorkloadGroupSpecProbeHttpGet"]:
        """
        :schema: WorkloadGroupSpecProbe#httpGet
        """
        result = self._values.get("http_get")
        return result

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        """Number of seconds after the container has started before readiness probes are initiated.

        :schema: WorkloadGroupSpecProbe#initialDelaySeconds
        """
        result = self._values.get("initial_delay_seconds")
        return result

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        """How often (in seconds) to perform the probe.

        :schema: WorkloadGroupSpecProbe#periodSeconds
        """
        result = self._values.get("period_seconds")
        return result

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        """Minimum consecutive successes for the probe to be considered successful after having failed.

        :schema: WorkloadGroupSpecProbe#successThreshold
        """
        result = self._values.get("success_threshold")
        return result

    @builtins.property
    def tcp_socket(self) -> typing.Optional["WorkloadGroupSpecProbeTcpSocket"]:
        """Health is determined by if the proxy is able to connect.

        :schema: WorkloadGroupSpecProbe#tcpSocket
        """
        result = self._values.get("tcp_socket")
        return result

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        """Number of seconds after which the probe times out.

        :schema: WorkloadGroupSpecProbe#timeoutSeconds
        """
        result = self._values.get("timeout_seconds")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecProbeExec",
    jsii_struct_bases=[],
    name_mapping={"command": "command"},
)
class WorkloadGroupSpecProbeExec:
    def __init__(
        self,
        *,
        command: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Health is determined by how the command that is executed exited.

        :param command: Command to run.

        :schema: WorkloadGroupSpecProbeExec
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        """Command to run.

        :schema: WorkloadGroupSpecProbeExec#command
        """
        result = self._values.get("command")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecProbeHttpGet",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "http_headers": "httpHeaders",
        "path": "path",
        "port": "port",
        "scheme": "scheme",
    },
)
class WorkloadGroupSpecProbeHttpGet:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.List["WorkloadGroupSpecProbeHttpGetHttpHeaders"]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param host: Host name to connect to, defaults to the pod IP.
        :param http_headers: Headers the proxy will pass on to make the request.
        :param path: Path to access on the HTTP server.
        :param port: Port on which the endpoint lives.
        :param scheme: 

        :schema: WorkloadGroupSpecProbeHttpGet
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        """Host name to connect to, defaults to the pod IP.

        :schema: WorkloadGroupSpecProbeHttpGet#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.List["WorkloadGroupSpecProbeHttpGetHttpHeaders"]]:
        """Headers the proxy will pass on to make the request.

        :schema: WorkloadGroupSpecProbeHttpGet#httpHeaders
        """
        result = self._values.get("http_headers")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Path to access on the HTTP server.

        :schema: WorkloadGroupSpecProbeHttpGet#path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """Port on which the endpoint lives.

        :schema: WorkloadGroupSpecProbeHttpGet#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecProbeHttpGet#scheme
        """
        result = self._values.get("scheme")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeHttpGet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecProbeHttpGetHttpHeaders",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class WorkloadGroupSpecProbeHttpGetHttpHeaders:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param name: 
        :param value: 

        :schema: WorkloadGroupSpecProbeHttpGetHttpHeaders
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecProbeHttpGetHttpHeaders#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecProbeHttpGetHttpHeaders#value
        """
        result = self._values.get("value")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeHttpGetHttpHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecProbeTcpSocket",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class WorkloadGroupSpecProbeTcpSocket:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Health is determined by if the proxy is able to connect.

        :param host: 
        :param port: 

        :schema: WorkloadGroupSpecProbeTcpSocket
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecProbeTcpSocket#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """
        :schema: WorkloadGroupSpecProbeTcpSocket#port
        """
        result = self._values.get("port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeTcpSocket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioworkloadgroup.WorkloadGroupSpecTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "labels": "labels",
        "locality": "locality",
        "network": "network",
        "ports": "ports",
        "service_account": "serviceAccount",
        "weight": "weight",
    },
)
class WorkloadGroupSpecTemplate:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        locality: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        service_account: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Template to be used for the generation of ``WorkloadEntry`` resources that belong to this ``WorkloadGroup``.

        :param address: 
        :param labels: One or more labels associated with the endpoint.
        :param locality: The locality associated with the endpoint.
        :param network: 
        :param ports: Set of ports associated with the endpoint.
        :param service_account: 
        :param weight: The load balancing weight associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if labels is not None:
            self._values["labels"] = labels
        if locality is not None:
            self._values["locality"] = locality
        if network is not None:
            self._values["network"] = network
        if ports is not None:
            self._values["ports"] = ports
        if service_account is not None:
            self._values["service_account"] = service_account
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecTemplate#address
        """
        result = self._values.get("address")
        return result

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """One or more labels associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#labels
        """
        result = self._values.get("labels")
        return result

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        """The locality associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#locality
        """
        result = self._values.get("locality")
        return result

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecTemplate#network
        """
        result = self._values.get("network")
        return result

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Set of ports associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#ports
        """
        result = self._values.get("ports")
        return result

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        """
        :schema: WorkloadGroupSpecTemplate#serviceAccount
        """
        result = self._values.get("service_account")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """The load balancing weight associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "WorkloadGroup",
    "WorkloadGroupOptions",
    "WorkloadGroupSpec",
    "WorkloadGroupSpecMetadata",
    "WorkloadGroupSpecProbe",
    "WorkloadGroupSpecProbeExec",
    "WorkloadGroupSpecProbeHttpGet",
    "WorkloadGroupSpecProbeHttpGetHttpHeaders",
    "WorkloadGroupSpecProbeTcpSocket",
    "WorkloadGroupSpecTemplate",
]

publication.publish()
