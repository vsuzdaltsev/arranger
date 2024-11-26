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


class Sidecar(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioiosidecar.Sidecar",
):
    """
    :schema: Sidecar
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["SidecarSpec"] = None,
    ) -> None:
        """Defines a "Sidecar" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        """
        options = SidecarOptions(spec=spec)

        jsii.create(Sidecar, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class SidecarOptions:
    def __init__(self, *, spec: typing.Optional["SidecarSpec"] = None) -> None:
        """
        :param spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html

        :schema: Sidecar
        """
        if isinstance(spec, dict):
            spec = SidecarSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["SidecarSpec"]:
        """Configuration affecting network reachability of a sidecar.

        See more details at: https://istio.io/docs/reference/config/networking/sidecar.html

        :schema: Sidecar#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpec",
    jsii_struct_bases=[],
    name_mapping={
        "egress": "egress",
        "ingress": "ingress",
        "outbound_traffic_policy": "outboundTrafficPolicy",
        "workload_selector": "workloadSelector",
    },
)
class SidecarSpec:
    def __init__(
        self,
        *,
        egress: typing.Optional[typing.List["SidecarSpecEgress"]] = None,
        ingress: typing.Optional[typing.List["SidecarSpecIngress"]] = None,
        outbound_traffic_policy: typing.Optional["SidecarSpecOutboundTrafficPolicy"] = None,
        workload_selector: typing.Optional["SidecarSpecWorkloadSelector"] = None,
    ) -> None:
        """Configuration affecting network reachability of a sidecar.

        See more details at: https://istio.io/docs/reference/config/networking/sidecar.html

        :param egress: 
        :param ingress: 
        :param outbound_traffic_policy: Configuration for the outbound traffic policy.
        :param workload_selector: 

        :schema: SidecarSpec
        """
        if isinstance(outbound_traffic_policy, dict):
            outbound_traffic_policy = SidecarSpecOutboundTrafficPolicy(**outbound_traffic_policy)
        if isinstance(workload_selector, dict):
            workload_selector = SidecarSpecWorkloadSelector(**workload_selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if egress is not None:
            self._values["egress"] = egress
        if ingress is not None:
            self._values["ingress"] = ingress
        if outbound_traffic_policy is not None:
            self._values["outbound_traffic_policy"] = outbound_traffic_policy
        if workload_selector is not None:
            self._values["workload_selector"] = workload_selector

    @builtins.property
    def egress(self) -> typing.Optional[typing.List["SidecarSpecEgress"]]:
        """
        :schema: SidecarSpec#egress
        """
        result = self._values.get("egress")
        return result

    @builtins.property
    def ingress(self) -> typing.Optional[typing.List["SidecarSpecIngress"]]:
        """
        :schema: SidecarSpec#ingress
        """
        result = self._values.get("ingress")
        return result

    @builtins.property
    def outbound_traffic_policy(
        self,
    ) -> typing.Optional["SidecarSpecOutboundTrafficPolicy"]:
        """Configuration for the outbound traffic policy.

        :schema: SidecarSpec#outboundTrafficPolicy
        """
        result = self._values.get("outbound_traffic_policy")
        return result

    @builtins.property
    def workload_selector(self) -> typing.Optional["SidecarSpecWorkloadSelector"]:
        """
        :schema: SidecarSpec#workloadSelector
        """
        result = self._values.get("workload_selector")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecEgress",
    jsii_struct_bases=[],
    name_mapping={
        "bind": "bind",
        "capture_mode": "captureMode",
        "hosts": "hosts",
        "port": "port",
    },
)
class SidecarSpecEgress:
    def __init__(
        self,
        *,
        bind: typing.Optional[builtins.str] = None,
        capture_mode: typing.Optional["SidecarSpecEgressCaptureMode"] = None,
        hosts: typing.Optional[typing.List[builtins.str]] = None,
        port: typing.Optional["SidecarSpecEgressPort"] = None,
    ) -> None:
        """
        :param bind: 
        :param capture_mode: 
        :param hosts: 
        :param port: The port associated with the listener.

        :schema: SidecarSpecEgress
        """
        if isinstance(port, dict):
            port = SidecarSpecEgressPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if bind is not None:
            self._values["bind"] = bind
        if capture_mode is not None:
            self._values["capture_mode"] = capture_mode
        if hosts is not None:
            self._values["hosts"] = hosts
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def bind(self) -> typing.Optional[builtins.str]:
        """
        :schema: SidecarSpecEgress#bind
        """
        result = self._values.get("bind")
        return result

    @builtins.property
    def capture_mode(self) -> typing.Optional["SidecarSpecEgressCaptureMode"]:
        """
        :schema: SidecarSpecEgress#captureMode
        """
        result = self._values.get("capture_mode")
        return result

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: SidecarSpecEgress#hosts
        """
        result = self._values.get("hosts")
        return result

    @builtins.property
    def port(self) -> typing.Optional["SidecarSpecEgressPort"]:
        """The port associated with the listener.

        :schema: SidecarSpecEgress#port
        """
        result = self._values.get("port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecEgress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="networkingistioiosidecar.SidecarSpecEgressCaptureMode")
class SidecarSpecEgressCaptureMode(enum.Enum):
    """
    :schema: SidecarSpecEgressCaptureMode
    """

    DEFAULT = "DEFAULT"
    """DEFAULT."""
    IPTABLES = "IPTABLES"
    """IPTABLES."""
    NONE = "NONE"
    """NONE."""


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecEgressPort",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class SidecarSpecEgressPort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        """The port associated with the listener.

        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: SidecarSpecEgressPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Label assigned to the port.

        :schema: SidecarSpecEgressPort#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """A valid non-negative integer port number.

        :schema: SidecarSpecEgressPort#number
        """
        result = self._values.get("number")
        return result

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        """The protocol exposed on the port.

        :schema: SidecarSpecEgressPort#protocol
        """
        result = self._values.get("protocol")
        return result

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        """
        :schema: SidecarSpecEgressPort#targetPort
        """
        result = self._values.get("target_port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecEgressPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecIngress",
    jsii_struct_bases=[],
    name_mapping={
        "bind": "bind",
        "capture_mode": "captureMode",
        "default_endpoint": "defaultEndpoint",
        "port": "port",
    },
)
class SidecarSpecIngress:
    def __init__(
        self,
        *,
        bind: typing.Optional[builtins.str] = None,
        capture_mode: typing.Optional["SidecarSpecIngressCaptureMode"] = None,
        default_endpoint: typing.Optional[builtins.str] = None,
        port: typing.Optional["SidecarSpecIngressPort"] = None,
    ) -> None:
        """
        :param bind: The IP to which the listener should be bound.
        :param capture_mode: 
        :param default_endpoint: 
        :param port: The port associated with the listener.

        :schema: SidecarSpecIngress
        """
        if isinstance(port, dict):
            port = SidecarSpecIngressPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if bind is not None:
            self._values["bind"] = bind
        if capture_mode is not None:
            self._values["capture_mode"] = capture_mode
        if default_endpoint is not None:
            self._values["default_endpoint"] = default_endpoint
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def bind(self) -> typing.Optional[builtins.str]:
        """The IP to which the listener should be bound.

        :schema: SidecarSpecIngress#bind
        """
        result = self._values.get("bind")
        return result

    @builtins.property
    def capture_mode(self) -> typing.Optional["SidecarSpecIngressCaptureMode"]:
        """
        :schema: SidecarSpecIngress#captureMode
        """
        result = self._values.get("capture_mode")
        return result

    @builtins.property
    def default_endpoint(self) -> typing.Optional[builtins.str]:
        """
        :schema: SidecarSpecIngress#defaultEndpoint
        """
        result = self._values.get("default_endpoint")
        return result

    @builtins.property
    def port(self) -> typing.Optional["SidecarSpecIngressPort"]:
        """The port associated with the listener.

        :schema: SidecarSpecIngress#port
        """
        result = self._values.get("port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="networkingistioiosidecar.SidecarSpecIngressCaptureMode")
class SidecarSpecIngressCaptureMode(enum.Enum):
    """
    :schema: SidecarSpecIngressCaptureMode
    """

    DEFAULT = "DEFAULT"
    """DEFAULT."""
    IPTABLES = "IPTABLES"
    """IPTABLES."""
    NONE = "NONE"
    """NONE."""


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecIngressPort",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class SidecarSpecIngressPort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        """The port associated with the listener.

        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: SidecarSpecIngressPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Label assigned to the port.

        :schema: SidecarSpecIngressPort#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """A valid non-negative integer port number.

        :schema: SidecarSpecIngressPort#number
        """
        result = self._values.get("number")
        return result

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        """The protocol exposed on the port.

        :schema: SidecarSpecIngressPort#protocol
        """
        result = self._values.get("protocol")
        return result

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        """
        :schema: SidecarSpecIngressPort#targetPort
        """
        result = self._values.get("target_port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecIngressPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecOutboundTrafficPolicy",
    jsii_struct_bases=[],
    name_mapping={"egress_proxy": "egressProxy", "mode": "mode"},
)
class SidecarSpecOutboundTrafficPolicy:
    def __init__(
        self,
        *,
        egress_proxy: typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxy"] = None,
        mode: typing.Optional["SidecarSpecOutboundTrafficPolicyMode"] = None,
    ) -> None:
        """Configuration for the outbound traffic policy.

        :param egress_proxy: 
        :param mode: 

        :schema: SidecarSpecOutboundTrafficPolicy
        """
        if isinstance(egress_proxy, dict):
            egress_proxy = SidecarSpecOutboundTrafficPolicyEgressProxy(**egress_proxy)
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_proxy is not None:
            self._values["egress_proxy"] = egress_proxy
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def egress_proxy(
        self,
    ) -> typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxy"]:
        """
        :schema: SidecarSpecOutboundTrafficPolicy#egressProxy
        """
        result = self._values.get("egress_proxy")
        return result

    @builtins.property
    def mode(self) -> typing.Optional["SidecarSpecOutboundTrafficPolicyMode"]:
        """
        :schema: SidecarSpecOutboundTrafficPolicy#mode
        """
        result = self._values.get("mode")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecOutboundTrafficPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecOutboundTrafficPolicyEgressProxy",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class SidecarSpecOutboundTrafficPolicyEgressProxy:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxyPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy
        """
        if isinstance(port, dict):
            port = SidecarSpecOutboundTrafficPolicyEgressProxyPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        """The name of a service from the service registry.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def port(
        self,
    ) -> typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxyPort"]:
        """Specifies the port on the host that is being addressed.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        """The name of a subset within the service.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy#subset
        """
        result = self._values.get("subset")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecOutboundTrafficPolicyEgressProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecOutboundTrafficPolicyEgressProxyPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class SidecarSpecOutboundTrafficPolicyEgressProxyPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """Specifies the port on the host that is being addressed.

        :param number: 

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxyPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: SidecarSpecOutboundTrafficPolicyEgressProxyPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecOutboundTrafficPolicyEgressProxyPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="networkingistioiosidecar.SidecarSpecOutboundTrafficPolicyMode")
class SidecarSpecOutboundTrafficPolicyMode(enum.Enum):
    """
    :schema: SidecarSpecOutboundTrafficPolicyMode
    """

    REGISTRY_ONLY = "REGISTRY_ONLY"
    """REGISTRY_ONLY."""
    ALLOW_ANY = "ALLOW_ANY"
    """ALLOW_ANY."""


@jsii.data_type(
    jsii_type="networkingistioiosidecar.SidecarSpecWorkloadSelector",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class SidecarSpecWorkloadSelector:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param labels: 

        :schema: SidecarSpecWorkloadSelector
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: SidecarSpecWorkloadSelector#labels
        """
        result = self._values.get("labels")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecWorkloadSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Sidecar",
    "SidecarOptions",
    "SidecarSpec",
    "SidecarSpecEgress",
    "SidecarSpecEgressCaptureMode",
    "SidecarSpecEgressPort",
    "SidecarSpecIngress",
    "SidecarSpecIngressCaptureMode",
    "SidecarSpecIngressPort",
    "SidecarSpecOutboundTrafficPolicy",
    "SidecarSpecOutboundTrafficPolicyEgressProxy",
    "SidecarSpecOutboundTrafficPolicyEgressProxyPort",
    "SidecarSpecOutboundTrafficPolicyMode",
    "SidecarSpecWorkloadSelector",
]

publication.publish()
