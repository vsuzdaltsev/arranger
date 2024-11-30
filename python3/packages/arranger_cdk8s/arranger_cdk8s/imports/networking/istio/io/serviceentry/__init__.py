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


class ServiceEntry(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioioserviceentry.ServiceEntry",
):
    """
    :schema: ServiceEntry
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["ServiceEntrySpec"] = None,
    ) -> None:
        """Defines a "ServiceEntry" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration affecting service registry. See more details at: https://istio.io/docs/reference/config/networking/service-entry.html
        """
        options = ServiceEntryOptions(spec=spec)

        jsii.create(ServiceEntry, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioioserviceentry.ServiceEntryOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class ServiceEntryOptions:
    def __init__(self, *, spec: typing.Optional["ServiceEntrySpec"] = None) -> None:
        """
        :param spec: Configuration affecting service registry. See more details at: https://istio.io/docs/reference/config/networking/service-entry.html

        :schema: ServiceEntry
        """
        if isinstance(spec, dict):
            spec = ServiceEntrySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["ServiceEntrySpec"]:
        """Configuration affecting service registry.

        See more details at: https://istio.io/docs/reference/config/networking/service-entry.html

        :schema: ServiceEntry#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioserviceentry.ServiceEntrySpec",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "endpoints": "endpoints",
        "export_to": "exportTo",
        "hosts": "hosts",
        "location": "location",
        "ports": "ports",
        "resolution": "resolution",
        "subject_alt_names": "subjectAltNames",
        "workload_selector": "workloadSelector",
    },
)
class ServiceEntrySpec:
    def __init__(
        self,
        *,
        addresses: typing.Optional[typing.List[builtins.str]] = None,
        endpoints: typing.Optional[typing.List["ServiceEntrySpecEndpoints"]] = None,
        export_to: typing.Optional[typing.List[builtins.str]] = None,
        hosts: typing.Optional[typing.List[builtins.str]] = None,
        location: typing.Optional["ServiceEntrySpecLocation"] = None,
        ports: typing.Optional[typing.List["ServiceEntrySpecPorts"]] = None,
        resolution: typing.Optional["ServiceEntrySpecResolution"] = None,
        subject_alt_names: typing.Optional[typing.List[builtins.str]] = None,
        workload_selector: typing.Optional["ServiceEntrySpecWorkloadSelector"] = None,
    ) -> None:
        """Configuration affecting service registry.

        See more details at: https://istio.io/docs/reference/config/networking/service-entry.html

        :param addresses: The virtual IP addresses associated with the service.
        :param endpoints: One or more endpoints associated with the service.
        :param export_to: A list of namespaces to which this service is exported.
        :param hosts: The hosts associated with the ServiceEntry.
        :param location: 
        :param ports: The ports associated with the external service.
        :param resolution: Service discovery mode for the hosts.
        :param subject_alt_names: 
        :param workload_selector: Applicable only for MESH_INTERNAL services.

        :schema: ServiceEntrySpec
        """
        if isinstance(workload_selector, dict):
            workload_selector = ServiceEntrySpecWorkloadSelector(**workload_selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if addresses is not None:
            self._values["addresses"] = addresses
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if export_to is not None:
            self._values["export_to"] = export_to
        if hosts is not None:
            self._values["hosts"] = hosts
        if location is not None:
            self._values["location"] = location
        if ports is not None:
            self._values["ports"] = ports
        if resolution is not None:
            self._values["resolution"] = resolution
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names
        if workload_selector is not None:
            self._values["workload_selector"] = workload_selector

    @builtins.property
    def addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        """The virtual IP addresses associated with the service.

        :schema: ServiceEntrySpec#addresses
        """
        result = self._values.get("addresses")
        return result

    @builtins.property
    def endpoints(self) -> typing.Optional[typing.List["ServiceEntrySpecEndpoints"]]:
        """One or more endpoints associated with the service.

        :schema: ServiceEntrySpec#endpoints
        """
        result = self._values.get("endpoints")
        return result

    @builtins.property
    def export_to(self) -> typing.Optional[typing.List[builtins.str]]:
        """A list of namespaces to which this service is exported.

        :schema: ServiceEntrySpec#exportTo
        """
        result = self._values.get("export_to")
        return result

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """The hosts associated with the ServiceEntry.

        :schema: ServiceEntrySpec#hosts
        """
        result = self._values.get("hosts")
        return result

    @builtins.property
    def location(self) -> typing.Optional["ServiceEntrySpecLocation"]:
        """
        :schema: ServiceEntrySpec#location
        """
        result = self._values.get("location")
        return result

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["ServiceEntrySpecPorts"]]:
        """The ports associated with the external service.

        :schema: ServiceEntrySpec#ports
        """
        result = self._values.get("ports")
        return result

    @builtins.property
    def resolution(self) -> typing.Optional["ServiceEntrySpecResolution"]:
        """Service discovery mode for the hosts.

        :schema: ServiceEntrySpec#resolution
        """
        result = self._values.get("resolution")
        return result

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: ServiceEntrySpec#subjectAltNames
        """
        result = self._values.get("subject_alt_names")
        return result

    @builtins.property
    def workload_selector(self) -> typing.Optional["ServiceEntrySpecWorkloadSelector"]:
        """Applicable only for MESH_INTERNAL services.

        :schema: ServiceEntrySpec#workloadSelector
        """
        result = self._values.get("workload_selector")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioioserviceentry.ServiceEntrySpecEndpoints",
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
class ServiceEntrySpecEndpoints:
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
        """
        :param address: 
        :param labels: One or more labels associated with the endpoint.
        :param locality: The locality associated with the endpoint.
        :param network: 
        :param ports: Set of ports associated with the endpoint.
        :param service_account: 
        :param weight: The load balancing weight associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints
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
        :schema: ServiceEntrySpecEndpoints#address
        """
        result = self._values.get("address")
        return result

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """One or more labels associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#labels
        """
        result = self._values.get("labels")
        return result

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        """The locality associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#locality
        """
        result = self._values.get("locality")
        return result

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        """
        :schema: ServiceEntrySpecEndpoints#network
        """
        result = self._values.get("network")
        return result

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Set of ports associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#ports
        """
        result = self._values.get("ports")
        return result

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        """
        :schema: ServiceEntrySpecEndpoints#serviceAccount
        """
        result = self._values.get("service_account")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """The load balancing weight associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpecEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="networkingistioioserviceentry.ServiceEntrySpecLocation")
class ServiceEntrySpecLocation(enum.Enum):
    """
    :schema: ServiceEntrySpecLocation
    """

    MESH_EXTERNAL = "MESH_EXTERNAL"
    """MESH_EXTERNAL."""
    MESH_INTERNAL = "MESH_INTERNAL"
    """MESH_INTERNAL."""


@jsii.data_type(
    jsii_type="networkingistioioserviceentry.ServiceEntrySpecPorts",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class ServiceEntrySpecPorts:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: ServiceEntrySpecPorts
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

        :schema: ServiceEntrySpecPorts#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """A valid non-negative integer port number.

        :schema: ServiceEntrySpecPorts#number
        """
        result = self._values.get("number")
        return result

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        """The protocol exposed on the port.

        :schema: ServiceEntrySpecPorts#protocol
        """
        result = self._values.get("protocol")
        return result

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        """
        :schema: ServiceEntrySpecPorts#targetPort
        """
        result = self._values.get("target_port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpecPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="networkingistioioserviceentry.ServiceEntrySpecResolution")
class ServiceEntrySpecResolution(enum.Enum):
    """Service discovery mode for the hosts.

    :schema: ServiceEntrySpecResolution
    """

    NONE = "NONE"
    """NONE."""
    STATIC = "STATIC"
    """STATIC."""
    DNS = "DNS"
    """DNS."""


@jsii.data_type(
    jsii_type="networkingistioioserviceentry.ServiceEntrySpecWorkloadSelector",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class ServiceEntrySpecWorkloadSelector:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """Applicable only for MESH_INTERNAL services.

        :param labels: 

        :schema: ServiceEntrySpecWorkloadSelector
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: ServiceEntrySpecWorkloadSelector#labels
        """
        result = self._values.get("labels")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpecWorkloadSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ServiceEntry",
    "ServiceEntryOptions",
    "ServiceEntrySpec",
    "ServiceEntrySpecEndpoints",
    "ServiceEntrySpecLocation",
    "ServiceEntrySpecPorts",
    "ServiceEntrySpecResolution",
    "ServiceEntrySpecWorkloadSelector",
]

publication.publish()
