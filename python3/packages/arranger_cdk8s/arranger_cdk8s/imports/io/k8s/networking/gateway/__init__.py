import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import cdk8s as _cdk8s_d3d9af27
import constructs as _constructs_77d1e7e8


class Gateway(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iok8snetworkinggateway.Gateway",
):
    '''Gateway represents an instance of a service-traffic handling infrastructure by binding Listeners to a set of IP addresses.

    :schema: Gateway
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        spec: typing.Union["GatewaySpec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a "Gateway" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param spec: Spec defines the desired state of Gateway.
        :param metadata: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cabc98ad409afc45e6aaf13b346e8cb91a2ff88c935a0841bfe8497949111873)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GatewayProps(spec=spec, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        spec: typing.Union["GatewaySpec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Gateway".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param spec: Spec defines the desired state of Gateway.
        :param metadata: 
        '''
        props = GatewayProps(spec=spec, metadata=metadata)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "Gateway".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayProps",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec", "metadata": "metadata"},
)
class GatewayProps:
    def __init__(
        self,
        *,
        spec: typing.Union["GatewaySpec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Gateway represents an instance of a service-traffic handling infrastructure by binding Listeners to a set of IP addresses.

        :param spec: Spec defines the desired state of Gateway.
        :param metadata: 

        :schema: Gateway
        '''
        if isinstance(spec, dict):
            spec = GatewaySpec(**spec)
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68ff39a41520cfbc09e8a40c697f4c39299f0b6ba29623a484142c4fab4ffceb)
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "spec": spec,
        }
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def spec(self) -> "GatewaySpec":
        '''Spec defines the desired state of Gateway.

        :schema: Gateway#spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("GatewaySpec", result)

    @builtins.property
    def metadata(self) -> typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata]:
        '''
        :schema: Gateway#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpec",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_class_name": "gatewayClassName",
        "listeners": "listeners",
        "addresses": "addresses",
    },
)
class GatewaySpec:
    def __init__(
        self,
        *,
        gateway_class_name: builtins.str,
        listeners: typing.Sequence[typing.Union["GatewaySpecListeners", typing.Dict[builtins.str, typing.Any]]],
        addresses: typing.Optional[typing.Sequence[typing.Union["GatewaySpecAddresses", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Spec defines the desired state of Gateway.

        :param gateway_class_name: GatewayClassName used for this Gateway. This is the name of a GatewayClass resource.
        :param listeners: Listeners associated with this Gateway. Listeners define logical endpoints that are bound on this Gateway's addresses. At least one Listener MUST be specified. Each listener in a Gateway must have a unique combination of Hostname, Port, and Protocol. An implementation MAY group Listeners by Port and then collapse each group of Listeners into a single Listener if the implementation determines that the Listeners in the group are "compatible". An implementation MAY also group together and collapse compatible Listeners belonging to different Gateways. For example, an implementation might consider Listeners to be compatible with each other if all of the following conditions are met: 1. Either each Listener within the group specifies the "HTTP" Protocol or each Listener within the group specifies either the "HTTPS" or "TLS" Protocol. 2. Each Listener within the group specifies a Hostname that is unique within the group. 3. As a special case, one Listener within a group may omit Hostname, in which case this Listener matches when no other Listener matches. If the implementation does collapse compatible Listeners, the hostname provided in the incoming client request MUST be matched to a Listener to find the correct set of Routes. The incoming hostname MUST be matched using the Hostname field for each Listener in order of most to least specific. That is, exact matches must be processed before wildcard matches. If this field specifies multiple Listeners that have the same Port value but are not compatible, the implementation must raise a "Conflicted" condition in the Listener status. Support: Core
        :param addresses: Addresses requested for this Gateway. This is optional and behavior can depend on the implementation. If a value is set in the spec and the requested address is invalid or unavailable, the implementation MUST indicate this in the associated entry in GatewayStatus.Addresses. The Addresses field represents a request for the address(es) on the "outside of the Gateway", that traffic bound for this Gateway will use. This could be the IP address or hostname of an external load balancer or other networking infrastructure, or some other address that traffic will be sent to. The .listener.hostname field is used to route traffic that has already arrived at the Gateway to the correct in-cluster destination. If no Addresses are specified, the implementation MAY schedule the Gateway in an implementation-specific manner, assigning an appropriate set of Addresses. The implementation MUST bind all Listeners to every GatewayAddress that it assigns to the Gateway and add a corresponding entry in GatewayStatus.Addresses. Support: Extended

        :schema: GatewaySpec
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c46a4037929c0780bbc611db172de1e56e3cdefa4bdb57ea9298cff19a423a5e)
            check_type(argname="argument gateway_class_name", value=gateway_class_name, expected_type=type_hints["gateway_class_name"])
            check_type(argname="argument listeners", value=listeners, expected_type=type_hints["listeners"])
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_class_name": gateway_class_name,
            "listeners": listeners,
        }
        if addresses is not None:
            self._values["addresses"] = addresses

    @builtins.property
    def gateway_class_name(self) -> builtins.str:
        '''GatewayClassName used for this Gateway.

        This is the name of a GatewayClass resource.

        :schema: GatewaySpec#gatewayClassName
        '''
        result = self._values.get("gateway_class_name")
        assert result is not None, "Required property 'gateway_class_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listeners(self) -> typing.List["GatewaySpecListeners"]:
        '''Listeners associated with this Gateway.

        Listeners define logical endpoints that are bound on this Gateway's addresses. At least one Listener MUST be specified.
        Each listener in a Gateway must have a unique combination of Hostname, Port, and Protocol.
        An implementation MAY group Listeners by Port and then collapse each group of Listeners into a single Listener if the implementation determines that the Listeners in the group are "compatible". An implementation MAY also group together and collapse compatible Listeners belonging to different Gateways.
        For example, an implementation might consider Listeners to be compatible with each other if all of the following conditions are met:

        1. Either each Listener within the group specifies the "HTTP"    Protocol or each Listener within the group specifies either    the "HTTPS" or "TLS" Protocol.
        2. Each Listener within the group specifies a Hostname that is unique    within the group.
        3. As a special case, one Listener within a group may omit Hostname,    in which case this Listener matches when no other Listener    matches.
           If the implementation does collapse compatible Listeners, the hostname provided in the incoming client request MUST be matched to a Listener to find the correct set of Routes. The incoming hostname MUST be matched using the Hostname field for each Listener in order of most to least specific. That is, exact matches must be processed before wildcard matches.
           If this field specifies multiple Listeners that have the same Port value but are not compatible, the implementation must raise a "Conflicted" condition in the Listener status.
           Support: Core

        :schema: GatewaySpec#listeners
        '''
        result = self._values.get("listeners")
        assert result is not None, "Required property 'listeners' is missing"
        return typing.cast(typing.List["GatewaySpecListeners"], result)

    @builtins.property
    def addresses(self) -> typing.Optional[typing.List["GatewaySpecAddresses"]]:
        '''Addresses requested for this Gateway.

        This is optional and behavior can depend on the implementation. If a value is set in the spec and the requested address is invalid or unavailable, the implementation MUST indicate this in the associated entry in GatewayStatus.Addresses.
        The Addresses field represents a request for the address(es) on the "outside of the Gateway", that traffic bound for this Gateway will use. This could be the IP address or hostname of an external load balancer or other networking infrastructure, or some other address that traffic will be sent to.
        The .listener.hostname field is used to route traffic that has already arrived at the Gateway to the correct in-cluster destination.
        If no Addresses are specified, the implementation MAY schedule the Gateway in an implementation-specific manner, assigning an appropriate set of Addresses.
        The implementation MUST bind all Listeners to every GatewayAddress that it assigns to the Gateway and add a corresponding entry in GatewayStatus.Addresses.
        Support: Extended

        :schema: GatewaySpec#addresses
        '''
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.List["GatewaySpecAddresses"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecAddresses",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "type": "type"},
)
class GatewaySpecAddresses:
    def __init__(
        self,
        *,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''GatewayAddress describes an address that can be bound to a Gateway.

        :param value: Value of the address. The validity of the values will depend on the type and support by the controller. Examples: ``1.2.3.4``, ``128::1``, ``my-ip-address``.
        :param type: Type of the address.

        :schema: GatewaySpecAddresses
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f275a6bf24c8a4fed5442c00181fdb061ab84b6daac136d26f49fd21a2b713a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the address.

        The validity of the values will depend on the type and support by the controller.
        Examples: ``1.2.3.4``, ``128::1``, ``my-ip-address``.

        :schema: GatewaySpecAddresses#value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type of the address.

        :schema: GatewaySpecAddresses#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListeners",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "port": "port",
        "protocol": "protocol",
        "allowed_routes": "allowedRoutes",
        "hostname": "hostname",
        "tls": "tls",
    },
)
class GatewaySpecListeners:
    def __init__(
        self,
        *,
        name: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        allowed_routes: typing.Optional[typing.Union["GatewaySpecListenersAllowedRoutes", typing.Dict[builtins.str, typing.Any]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Union["GatewaySpecListenersTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Listener embodies the concept of a logical endpoint where a Gateway accepts network connections.

        :param name: Name is the name of the Listener. This name MUST be unique within a Gateway. Support: Core
        :param port: Port is the network port. Multiple listeners may use the same port, subject to the Listener compatibility rules. Support: Core
        :param protocol: Protocol specifies the network protocol this listener expects to receive. Support: Core
        :param allowed_routes: AllowedRoutes defines the types of routes that MAY be attached to a Listener and the trusted namespaces where those Route resources MAY be present. Although a client request may match multiple route rules, only one rule may ultimately receive the request. Matching precedence MUST be determined in order of the following criteria: - The most specific match as defined by the Route type. * The oldest Route based on creation timestamp. For example, a Route with a creation timestamp of "2020-09-08 01:02:03" is given precedence over a Route with a creation timestamp of "2020-09-08 01:02:04". * If everything else is equivalent, the Route appearing first in alphabetical order (namespace/name) should be given precedence. For example, foo/bar is given precedence over foo/baz. All valid rules within a Route attached to this Listener should be implemented. Invalid Route rules can be ignored (sometimes that will mean the full Route). If a Route rule transitions from valid to invalid, support for that Route rule should be dropped to ensure consistency. For example, even if a filter specified by a Route rule is invalid, the rest of the rules within that Route should still be supported. Support: Core
        :param hostname: Hostname specifies the virtual hostname to match for protocol types that define this concept. When unspecified, all hostnames are matched. This field is ignored for protocols that don't require hostname based matching. Implementations MUST apply Hostname matching appropriately for each of the following protocols: - TLS: The Listener Hostname MUST match the SNI. * HTTP: The Listener Hostname MUST match the Host header of the request. * HTTPS: The Listener Hostname SHOULD match at both the TLS and HTTP protocol layers as described above. If an implementation does not ensure that both the SNI and Host header match the Listener hostname, it MUST clearly document that. For HTTPRoute and TLSRoute resources, there is an interaction with the ``spec.hostnames`` array. When both listener and route specify hostnames, there MUST be an intersection between the values for a Route to be accepted. For more information, refer to the Route specific Hostnames documentation. Hostnames that are prefixed with a wildcard label (``*.``) are interpreted as a suffix match. That means that a match for ``*.example.com`` would match both ``test.example.com``, and ``foo.test.example.com``, but not ``example.com``. Support: Core
        :param tls: TLS is the TLS configuration for the Listener. This field is required if the Protocol field is "HTTPS" or "TLS". It is invalid to set this field if the Protocol field is "HTTP", "TCP", or "UDP". The association of SNIs to Certificate defined in GatewayTLSConfig is defined based on the Hostname field for this listener. The GatewayClass MUST use the longest matching SNI out of all available certificates for any TLS handshake. Support: Core

        :schema: GatewaySpecListeners
        '''
        if isinstance(allowed_routes, dict):
            allowed_routes = GatewaySpecListenersAllowedRoutes(**allowed_routes)
        if isinstance(tls, dict):
            tls = GatewaySpecListenersTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f57af45c000f3b0113b5ceb798cfae33297c7e6d199853aba563e893a17469)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument allowed_routes", value=allowed_routes, expected_type=type_hints["allowed_routes"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "port": port,
            "protocol": protocol,
        }
        if allowed_routes is not None:
            self._values["allowed_routes"] = allowed_routes
        if hostname is not None:
            self._values["hostname"] = hostname
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is the name of the Listener.

        This name MUST be unique within a Gateway.
        Support: Core

        :schema: GatewaySpecListeners#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port is the network port.

        Multiple listeners may use the same port, subject to the Listener compatibility rules.
        Support: Core

        :schema: GatewaySpecListeners#port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Protocol specifies the network protocol this listener expects to receive.

        Support: Core

        :schema: GatewaySpecListeners#protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_routes(self) -> typing.Optional["GatewaySpecListenersAllowedRoutes"]:
        '''AllowedRoutes defines the types of routes that MAY be attached to a Listener and the trusted namespaces where those Route resources MAY be present.

        Although a client request may match multiple route rules, only one rule may ultimately receive the request. Matching precedence MUST be determined in order of the following criteria:

        - The most specific match as defined by the Route type. * The oldest Route based on creation timestamp. For example, a Route with   a creation timestamp of "2020-09-08 01:02:03" is given precedence over   a Route with a creation timestamp of "2020-09-08 01:02:04". * If everything else is equivalent, the Route appearing first in   alphabetical order (namespace/name) should be given precedence. For   example, foo/bar is given precedence over foo/baz.
          All valid rules within a Route attached to this Listener should be implemented. Invalid Route rules can be ignored (sometimes that will mean the full Route). If a Route rule transitions from valid to invalid, support for that Route rule should be dropped to ensure consistency. For example, even if a filter specified by a Route rule is invalid, the rest of the rules within that Route should still be supported.
          Support: Core

        :schema: GatewaySpecListeners#allowedRoutes
        '''
        result = self._values.get("allowed_routes")
        return typing.cast(typing.Optional["GatewaySpecListenersAllowedRoutes"], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Hostname specifies the virtual hostname to match for protocol types that define this concept.

        When unspecified, all hostnames are matched. This field is ignored for protocols that don't require hostname based matching.
        Implementations MUST apply Hostname matching appropriately for each of the following protocols:

        - TLS: The Listener Hostname MUST match the SNI. * HTTP: The Listener Hostname MUST match the Host header of the request. * HTTPS: The Listener Hostname SHOULD match at both the TLS and HTTP   protocol layers as described above. If an implementation does not   ensure that both the SNI and Host header match the Listener hostname,   it MUST clearly document that.
          For HTTPRoute and TLSRoute resources, there is an interaction with the ``spec.hostnames`` array. When both listener and route specify hostnames, there MUST be an intersection between the values for a Route to be accepted. For more information, refer to the Route specific Hostnames documentation.
          Hostnames that are prefixed with a wildcard label (``*.``) are interpreted as a suffix match. That means that a match for ``*.example.com`` would match both ``test.example.com``, and ``foo.test.example.com``, but not ``example.com``.
          Support: Core

        :schema: GatewaySpecListeners#hostname
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls(self) -> typing.Optional["GatewaySpecListenersTls"]:
        '''TLS is the TLS configuration for the Listener.

        This field is required if the Protocol field is "HTTPS" or "TLS". It is invalid to set this field if the Protocol field is "HTTP", "TCP", or "UDP".
        The association of SNIs to Certificate defined in GatewayTLSConfig is defined based on the Hostname field for this listener.
        The GatewayClass MUST use the longest matching SNI out of all available certificates for any TLS handshake.
        Support: Core

        :schema: GatewaySpecListeners#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["GatewaySpecListenersTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListeners(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersAllowedRoutes",
    jsii_struct_bases=[],
    name_mapping={"kinds": "kinds", "namespaces": "namespaces"},
)
class GatewaySpecListenersAllowedRoutes:
    def __init__(
        self,
        *,
        kinds: typing.Optional[typing.Sequence[typing.Union["GatewaySpecListenersAllowedRoutesKinds", typing.Dict[builtins.str, typing.Any]]]] = None,
        namespaces: typing.Optional[typing.Union["GatewaySpecListenersAllowedRoutesNamespaces", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''AllowedRoutes defines the types of routes that MAY be attached to a Listener and the trusted namespaces where those Route resources MAY be present.

        Although a client request may match multiple route rules, only one rule may ultimately receive the request. Matching precedence MUST be determined in order of the following criteria:

        - The most specific match as defined by the Route type. * The oldest Route based on creation timestamp. For example, a Route with   a creation timestamp of "2020-09-08 01:02:03" is given precedence over   a Route with a creation timestamp of "2020-09-08 01:02:04". * If everything else is equivalent, the Route appearing first in   alphabetical order (namespace/name) should be given precedence. For   example, foo/bar is given precedence over foo/baz.
          All valid rules within a Route attached to this Listener should be implemented. Invalid Route rules can be ignored (sometimes that will mean the full Route). If a Route rule transitions from valid to invalid, support for that Route rule should be dropped to ensure consistency. For example, even if a filter specified by a Route rule is invalid, the rest of the rules within that Route should still be supported.
          Support: Core

        :param kinds: Kinds specifies the groups and kinds of Routes that are allowed to bind to this Gateway Listener. When unspecified or empty, the kinds of Routes selected are determined using the Listener protocol. A RouteGroupKind MUST correspond to kinds of Routes that are compatible with the application protocol specified in the Listener's Protocol field. If an implementation does not support or recognize this resource type, it MUST set the "ResolvedRefs" condition to False for this Listener with the "InvalidRouteKinds" reason. Support: Core
        :param namespaces: Namespaces indicates namespaces from which Routes may be attached to this Listener. This is restricted to the namespace of this Gateway by default. Support: Core

        :schema: GatewaySpecListenersAllowedRoutes
        '''
        if isinstance(namespaces, dict):
            namespaces = GatewaySpecListenersAllowedRoutesNamespaces(**namespaces)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8f2afb6226781697a696dca7925a71469f547b8fba16b42b177a8ee1070def0)
            check_type(argname="argument kinds", value=kinds, expected_type=type_hints["kinds"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kinds is not None:
            self._values["kinds"] = kinds
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def kinds(
        self,
    ) -> typing.Optional[typing.List["GatewaySpecListenersAllowedRoutesKinds"]]:
        '''Kinds specifies the groups and kinds of Routes that are allowed to bind to this Gateway Listener.

        When unspecified or empty, the kinds of Routes selected are determined using the Listener protocol.
        A RouteGroupKind MUST correspond to kinds of Routes that are compatible with the application protocol specified in the Listener's Protocol field. If an implementation does not support or recognize this resource type, it MUST set the "ResolvedRefs" condition to False for this Listener with the "InvalidRouteKinds" reason.
        Support: Core

        :schema: GatewaySpecListenersAllowedRoutes#kinds
        '''
        result = self._values.get("kinds")
        return typing.cast(typing.Optional[typing.List["GatewaySpecListenersAllowedRoutesKinds"]], result)

    @builtins.property
    def namespaces(
        self,
    ) -> typing.Optional["GatewaySpecListenersAllowedRoutesNamespaces"]:
        '''Namespaces indicates namespaces from which Routes may be attached to this Listener.

        This is restricted to the namespace of this Gateway by default.
        Support: Core

        :schema: GatewaySpecListenersAllowedRoutes#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional["GatewaySpecListenersAllowedRoutesNamespaces"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersAllowedRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersAllowedRoutesKinds",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "group": "group"},
)
class GatewaySpecListenersAllowedRoutesKinds:
    def __init__(
        self,
        *,
        kind: builtins.str,
        group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''RouteGroupKind indicates the group and kind of a Route resource.

        :param kind: Kind is the kind of the Route.
        :param group: Group is the group of the Route.

        :schema: GatewaySpecListenersAllowedRoutesKinds
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d8c6aebe14746acdc13aedac61c85f43350c634c7ca2379e01f3def9ffb657f)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kind": kind,
        }
        if group is not None:
            self._values["group"] = group

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind is the kind of the Route.

        :schema: GatewaySpecListenersAllowedRoutesKinds#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the group of the Route.

        :schema: GatewaySpecListenersAllowedRoutesKinds#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersAllowedRoutesKinds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersAllowedRoutesNamespaces",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "selector": "selector"},
)
class GatewaySpecListenersAllowedRoutesNamespaces:
    def __init__(
        self,
        *,
        from_: typing.Optional["GatewaySpecListenersAllowedRoutesNamespacesFrom"] = None,
        selector: typing.Optional[typing.Union["GatewaySpecListenersAllowedRoutesNamespacesSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Namespaces indicates namespaces from which Routes may be attached to this Listener.

        This is restricted to the namespace of this Gateway by default.
        Support: Core

        :param from_: From indicates where Routes will be selected for this Gateway. Possible values are: * All: Routes in all namespaces may be used by this Gateway. * Selector: Routes in namespaces selected by the selector may be used by this Gateway. * Same: Only Routes in the same namespace may be used by this Gateway. Support: Core
        :param selector: Selector must be specified when From is set to "Selector". In that case, only Routes in Namespaces matching this Selector will be selected by this Gateway. This field is ignored for other values of "From". Support: Core

        :schema: GatewaySpecListenersAllowedRoutesNamespaces
        '''
        if isinstance(selector, dict):
            selector = GatewaySpecListenersAllowedRoutesNamespacesSelector(**selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__276beb87cc4d924064af5084f0481aa0719f81f898b75cb969e5dd8fe5a6ab59)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def from_(
        self,
    ) -> typing.Optional["GatewaySpecListenersAllowedRoutesNamespacesFrom"]:
        '''From indicates where Routes will be selected for this Gateway.

        Possible values are: * All: Routes in all namespaces may be used by this Gateway. * Selector: Routes in namespaces selected by the selector may be used by   this Gateway. * Same: Only Routes in the same namespace may be used by this Gateway.
        Support: Core

        :schema: GatewaySpecListenersAllowedRoutesNamespaces#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional["GatewaySpecListenersAllowedRoutesNamespacesFrom"], result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional["GatewaySpecListenersAllowedRoutesNamespacesSelector"]:
        '''Selector must be specified when From is set to "Selector".

        In that case, only Routes in Namespaces matching this Selector will be selected by this Gateway. This field is ignored for other values of "From".
        Support: Core

        :schema: GatewaySpecListenersAllowedRoutesNamespaces#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["GatewaySpecListenersAllowedRoutesNamespacesSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersAllowedRoutesNamespaces(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersAllowedRoutesNamespacesFrom"
)
class GatewaySpecListenersAllowedRoutesNamespacesFrom(enum.Enum):
    '''From indicates where Routes will be selected for this Gateway.

    Possible values are: * All: Routes in all namespaces may be used by this Gateway. * Selector: Routes in namespaces selected by the selector may be used by   this Gateway. * Same: Only Routes in the same namespace may be used by this Gateway.
    Support: Core

    :schema: GatewaySpecListenersAllowedRoutesNamespacesFrom
    '''

    ALL = "ALL"
    '''All.'''
    SELECTOR = "SELECTOR"
    '''Selector.'''
    SAME = "SAME"
    '''Same.'''


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersAllowedRoutesNamespacesSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class GatewaySpecListenersAllowedRoutesNamespacesSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Selector must be specified when From is set to "Selector".

        In that case, only Routes in Namespaces matching this Selector will be selected by this Gateway. This field is ignored for other values of "From".
        Support: Core

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfae7ad6e30bb2c3aba10f88da95e756dc4332b1254eafc521ce1720c89e141)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersAllowedRoutesNamespacesSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a598a4d2ecdfb536ece21d1bea2a5e7a153578dc49183ce5eac7737b178f32d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersTls",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_refs": "certificateRefs",
        "mode": "mode",
        "options": "options",
    },
)
class GatewaySpecListenersTls:
    def __init__(
        self,
        *,
        certificate_refs: typing.Optional[typing.Sequence[typing.Union["GatewaySpecListenersTlsCertificateRefs", typing.Dict[builtins.str, typing.Any]]]] = None,
        mode: typing.Optional["GatewaySpecListenersTlsMode"] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''TLS is the TLS configuration for the Listener.

        This field is required if the Protocol field is "HTTPS" or "TLS". It is invalid to set this field if the Protocol field is "HTTP", "TCP", or "UDP".
        The association of SNIs to Certificate defined in GatewayTLSConfig is defined based on the Hostname field for this listener.
        The GatewayClass MUST use the longest matching SNI out of all available certificates for any TLS handshake.
        Support: Core

        :param certificate_refs: CertificateRefs contains a series of references to Kubernetes objects that contains TLS certificates and private keys. These certificates are used to establish a TLS handshake for requests that match the hostname of the associated listener. A single CertificateRef to a Kubernetes Secret has "Core" support. Implementations MAY choose to support attaching multiple certificates to a Listener, but this behavior is implementation-specific. References to a resource in different namespace are invalid UNLESS there is a ReferenceGrant in the target namespace that allows the certificate to be attached. If a ReferenceGrant does not allow this reference, the "ResolvedRefs" condition MUST be set to False for this listener with the "RefNotPermitted" reason. This field is required to have at least one element when the mode is set to "Terminate" (default) and is optional otherwise. CertificateRefs can reference to standard Kubernetes resources, i.e. Secret, or implementation-specific custom resources. Support: Core - A single reference to a Kubernetes Secret of type kubernetes.io/tls Support: Implementation-specific (More than one reference or other resource types)
        :param mode: Mode defines the TLS behavior for the TLS session initiated by the client. There are two possible modes: - Terminate: The TLS session between the downstream client and the Gateway is terminated at the Gateway. This mode requires certificateRefs to be set and contain at least one element. - Passthrough: The TLS session is NOT terminated by the Gateway. This implies that the Gateway can't decipher the TLS stream except for the ClientHello message of the TLS protocol. CertificateRefs field is ignored in this mode. Support: Core
        :param options: Options are a list of key/value pairs to enable extended TLS configuration for each implementation. For example, configuring the minimum TLS version or supported cipher suites. A set of common keys MAY be defined by the API in the future. To avoid any ambiguity, implementation-specific definitions MUST use domain-prefixed names, such as ``example.com/my-custom-option``. Un-prefixed names are reserved for key names defined by Gateway API. Support: Implementation-specific

        :schema: GatewaySpecListenersTls
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865795c2502624e6577be2833a2c185731b15a1b6ad9762143fd128de2b34ca0)
            check_type(argname="argument certificate_refs", value=certificate_refs, expected_type=type_hints["certificate_refs"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate_refs is not None:
            self._values["certificate_refs"] = certificate_refs
        if mode is not None:
            self._values["mode"] = mode
        if options is not None:
            self._values["options"] = options

    @builtins.property
    def certificate_refs(
        self,
    ) -> typing.Optional[typing.List["GatewaySpecListenersTlsCertificateRefs"]]:
        '''CertificateRefs contains a series of references to Kubernetes objects that contains TLS certificates and private keys.

        These certificates are used to establish a TLS handshake for requests that match the hostname of the associated listener.
        A single CertificateRef to a Kubernetes Secret has "Core" support. Implementations MAY choose to support attaching multiple certificates to a Listener, but this behavior is implementation-specific.
        References to a resource in different namespace are invalid UNLESS there is a ReferenceGrant in the target namespace that allows the certificate to be attached. If a ReferenceGrant does not allow this reference, the "ResolvedRefs" condition MUST be set to False for this listener with the "RefNotPermitted" reason.
        This field is required to have at least one element when the mode is set to "Terminate" (default) and is optional otherwise.
        CertificateRefs can reference to standard Kubernetes resources, i.e. Secret, or implementation-specific custom resources.
        Support: Core - A single reference to a Kubernetes Secret of type kubernetes.io/tls
        Support: Implementation-specific (More than one reference or other resource types)

        :schema: GatewaySpecListenersTls#certificateRefs
        '''
        result = self._values.get("certificate_refs")
        return typing.cast(typing.Optional[typing.List["GatewaySpecListenersTlsCertificateRefs"]], result)

    @builtins.property
    def mode(self) -> typing.Optional["GatewaySpecListenersTlsMode"]:
        '''Mode defines the TLS behavior for the TLS session initiated by the client.

        There are two possible modes:

        - Terminate: The TLS session between the downstream client   and the Gateway is terminated at the Gateway. This mode requires   certificateRefs to be set and contain at least one element. - Passthrough: The TLS session is NOT terminated by the Gateway. This   implies that the Gateway can't decipher the TLS stream except for   the ClientHello message of the TLS protocol.   CertificateRefs field is ignored in this mode.
          Support: Core

        :schema: GatewaySpecListenersTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["GatewaySpecListenersTlsMode"], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Options are a list of key/value pairs to enable extended TLS configuration for each implementation.

        For example, configuring the minimum TLS version or supported cipher suites.
        A set of common keys MAY be defined by the API in the future. To avoid any ambiguity, implementation-specific definitions MUST use domain-prefixed names, such as ``example.com/my-custom-option``. Un-prefixed names are reserved for key names defined by Gateway API.
        Support: Implementation-specific

        :schema: GatewaySpecListenersTls#options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewaySpecListenersTlsCertificateRefs",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "group": "group",
        "kind": "kind",
        "namespace": "namespace",
    },
)
class GatewaySpecListenersTlsCertificateRefs:
    def __init__(
        self,
        *,
        name: builtins.str,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''SecretObjectReference identifies an API object including its namespace, defaulting to Secret.

        The API object must be valid in the cluster; the Group and Kind must be registered in the cluster for this reference to be valid.
        References to objects with invalid Group and Kind are not valid, and must be rejected by the implementation, with appropriate Conditions set on the containing object.

        :param name: Name is the name of the referent.
        :param group: Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.
        :param kind: Kind is kind of the referent. For example "HTTPRoute" or "Service".
        :param namespace: Namespace is the namespace of the backend. When unspecified, the local namespace is inferred. Note that when a namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. Support: Core

        :schema: GatewaySpecListenersTlsCertificateRefs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfafb32b51e4907423918700279f5e9163e14dc3a391ce2408c1a2ae35989047)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is the name of the referent.

        :schema: GatewaySpecListenersTlsCertificateRefs#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the group of the referent.

        For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.

        :schema: GatewaySpecListenersTlsCertificateRefs#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind is kind of the referent.

        For example "HTTPRoute" or "Service".

        :schema: GatewaySpecListenersTlsCertificateRefs#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace is the namespace of the backend.

        When unspecified, the local namespace is inferred.
        Note that when a namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details.
        Support: Core

        :schema: GatewaySpecListenersTlsCertificateRefs#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecListenersTlsCertificateRefs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iok8snetworkinggateway.GatewaySpecListenersTlsMode")
class GatewaySpecListenersTlsMode(enum.Enum):
    '''Mode defines the TLS behavior for the TLS session initiated by the client.

    There are two possible modes:

    - Terminate: The TLS session between the downstream client   and the Gateway is terminated at the Gateway. This mode requires   certificateRefs to be set and contain at least one element. - Passthrough: The TLS session is NOT terminated by the Gateway. This   implies that the Gateway can't decipher the TLS stream except for   the ClientHello message of the TLS protocol.   CertificateRefs field is ignored in this mode.
      Support: Core

    :schema: GatewaySpecListenersTlsMode
    '''

    TERMINATE = "TERMINATE"
    '''Terminate.'''
    PASSTHROUGH = "PASSTHROUGH"
    '''Passthrough.'''


class GatewayV1Beta1(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1",
):
    '''Gateway represents an instance of a service-traffic handling infrastructure by binding Listeners to a set of IP addresses.

    :schema: GatewayV1Beta1
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        spec: typing.Union["GatewayV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a "GatewayV1Beta1" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param spec: Spec defines the desired state of Gateway.
        :param metadata: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd36ce29efb9e8350ca75d0fecf56fe3ee1345122154083eedc218616b9c3dc5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GatewayV1Beta1Props(spec=spec, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        spec: typing.Union["GatewayV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "GatewayV1Beta1".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param spec: Spec defines the desired state of Gateway.
        :param metadata: 
        '''
        props = GatewayV1Beta1Props(spec=spec, metadata=metadata)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "GatewayV1Beta1".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1Props",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec", "metadata": "metadata"},
)
class GatewayV1Beta1Props:
    def __init__(
        self,
        *,
        spec: typing.Union["GatewayV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Gateway represents an instance of a service-traffic handling infrastructure by binding Listeners to a set of IP addresses.

        :param spec: Spec defines the desired state of Gateway.
        :param metadata: 

        :schema: GatewayV1Beta1
        '''
        if isinstance(spec, dict):
            spec = GatewayV1Beta1Spec(**spec)
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6111bfdec888c302c2cfab8e592d78d82210d1bc50e676adc3a57e1bd2e386)
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "spec": spec,
        }
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def spec(self) -> "GatewayV1Beta1Spec":
        '''Spec defines the desired state of Gateway.

        :schema: GatewayV1Beta1#spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("GatewayV1Beta1Spec", result)

    @builtins.property
    def metadata(self) -> typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata]:
        '''
        :schema: GatewayV1Beta1#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_class_name": "gatewayClassName",
        "listeners": "listeners",
        "addresses": "addresses",
    },
)
class GatewayV1Beta1Spec:
    def __init__(
        self,
        *,
        gateway_class_name: builtins.str,
        listeners: typing.Sequence[typing.Union["GatewayV1Beta1SpecListeners", typing.Dict[builtins.str, typing.Any]]],
        addresses: typing.Optional[typing.Sequence[typing.Union["GatewayV1Beta1SpecAddresses", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Spec defines the desired state of Gateway.

        :param gateway_class_name: GatewayClassName used for this Gateway. This is the name of a GatewayClass resource.
        :param listeners: Listeners associated with this Gateway. Listeners define logical endpoints that are bound on this Gateway's addresses. At least one Listener MUST be specified. Each listener in a Gateway must have a unique combination of Hostname, Port, and Protocol. An implementation MAY group Listeners by Port and then collapse each group of Listeners into a single Listener if the implementation determines that the Listeners in the group are "compatible". An implementation MAY also group together and collapse compatible Listeners belonging to different Gateways. For example, an implementation might consider Listeners to be compatible with each other if all of the following conditions are met: 1. Either each Listener within the group specifies the "HTTP" Protocol or each Listener within the group specifies either the "HTTPS" or "TLS" Protocol. 2. Each Listener within the group specifies a Hostname that is unique within the group. 3. As a special case, one Listener within a group may omit Hostname, in which case this Listener matches when no other Listener matches. If the implementation does collapse compatible Listeners, the hostname provided in the incoming client request MUST be matched to a Listener to find the correct set of Routes. The incoming hostname MUST be matched using the Hostname field for each Listener in order of most to least specific. That is, exact matches must be processed before wildcard matches. If this field specifies multiple Listeners that have the same Port value but are not compatible, the implementation must raise a "Conflicted" condition in the Listener status. Support: Core
        :param addresses: Addresses requested for this Gateway. This is optional and behavior can depend on the implementation. If a value is set in the spec and the requested address is invalid or unavailable, the implementation MUST indicate this in the associated entry in GatewayStatus.Addresses. The Addresses field represents a request for the address(es) on the "outside of the Gateway", that traffic bound for this Gateway will use. This could be the IP address or hostname of an external load balancer or other networking infrastructure, or some other address that traffic will be sent to. The .listener.hostname field is used to route traffic that has already arrived at the Gateway to the correct in-cluster destination. If no Addresses are specified, the implementation MAY schedule the Gateway in an implementation-specific manner, assigning an appropriate set of Addresses. The implementation MUST bind all Listeners to every GatewayAddress that it assigns to the Gateway and add a corresponding entry in GatewayStatus.Addresses. Support: Extended

        :schema: GatewayV1Beta1Spec
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee67507f87f5032c1c7344ad95ec863d34ba5233a832e225a042211946293734)
            check_type(argname="argument gateway_class_name", value=gateway_class_name, expected_type=type_hints["gateway_class_name"])
            check_type(argname="argument listeners", value=listeners, expected_type=type_hints["listeners"])
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_class_name": gateway_class_name,
            "listeners": listeners,
        }
        if addresses is not None:
            self._values["addresses"] = addresses

    @builtins.property
    def gateway_class_name(self) -> builtins.str:
        '''GatewayClassName used for this Gateway.

        This is the name of a GatewayClass resource.

        :schema: GatewayV1Beta1Spec#gatewayClassName
        '''
        result = self._values.get("gateway_class_name")
        assert result is not None, "Required property 'gateway_class_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listeners(self) -> typing.List["GatewayV1Beta1SpecListeners"]:
        '''Listeners associated with this Gateway.

        Listeners define logical endpoints that are bound on this Gateway's addresses. At least one Listener MUST be specified.
        Each listener in a Gateway must have a unique combination of Hostname, Port, and Protocol.
        An implementation MAY group Listeners by Port and then collapse each group of Listeners into a single Listener if the implementation determines that the Listeners in the group are "compatible". An implementation MAY also group together and collapse compatible Listeners belonging to different Gateways.
        For example, an implementation might consider Listeners to be compatible with each other if all of the following conditions are met:

        1. Either each Listener within the group specifies the "HTTP"    Protocol or each Listener within the group specifies either    the "HTTPS" or "TLS" Protocol.
        2. Each Listener within the group specifies a Hostname that is unique    within the group.
        3. As a special case, one Listener within a group may omit Hostname,    in which case this Listener matches when no other Listener    matches.
           If the implementation does collapse compatible Listeners, the hostname provided in the incoming client request MUST be matched to a Listener to find the correct set of Routes. The incoming hostname MUST be matched using the Hostname field for each Listener in order of most to least specific. That is, exact matches must be processed before wildcard matches.
           If this field specifies multiple Listeners that have the same Port value but are not compatible, the implementation must raise a "Conflicted" condition in the Listener status.
           Support: Core

        :schema: GatewayV1Beta1Spec#listeners
        '''
        result = self._values.get("listeners")
        assert result is not None, "Required property 'listeners' is missing"
        return typing.cast(typing.List["GatewayV1Beta1SpecListeners"], result)

    @builtins.property
    def addresses(self) -> typing.Optional[typing.List["GatewayV1Beta1SpecAddresses"]]:
        '''Addresses requested for this Gateway.

        This is optional and behavior can depend on the implementation. If a value is set in the spec and the requested address is invalid or unavailable, the implementation MUST indicate this in the associated entry in GatewayStatus.Addresses.
        The Addresses field represents a request for the address(es) on the "outside of the Gateway", that traffic bound for this Gateway will use. This could be the IP address or hostname of an external load balancer or other networking infrastructure, or some other address that traffic will be sent to.
        The .listener.hostname field is used to route traffic that has already arrived at the Gateway to the correct in-cluster destination.
        If no Addresses are specified, the implementation MAY schedule the Gateway in an implementation-specific manner, assigning an appropriate set of Addresses.
        The implementation MUST bind all Listeners to every GatewayAddress that it assigns to the Gateway and add a corresponding entry in GatewayStatus.Addresses.
        Support: Extended

        :schema: GatewayV1Beta1Spec#addresses
        '''
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.List["GatewayV1Beta1SpecAddresses"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecAddresses",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "type": "type"},
)
class GatewayV1Beta1SpecAddresses:
    def __init__(
        self,
        *,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''GatewayAddress describes an address that can be bound to a Gateway.

        :param value: Value of the address. The validity of the values will depend on the type and support by the controller. Examples: ``1.2.3.4``, ``128::1``, ``my-ip-address``.
        :param type: Type of the address.

        :schema: GatewayV1Beta1SpecAddresses
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93674cf130d5dbfd21e90fc3655cdd3def5daa1592cca0e09b70e7f4e25fed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the address.

        The validity of the values will depend on the type and support by the controller.
        Examples: ``1.2.3.4``, ``128::1``, ``my-ip-address``.

        :schema: GatewayV1Beta1SpecAddresses#value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type of the address.

        :schema: GatewayV1Beta1SpecAddresses#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListeners",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "port": "port",
        "protocol": "protocol",
        "allowed_routes": "allowedRoutes",
        "hostname": "hostname",
        "tls": "tls",
    },
)
class GatewayV1Beta1SpecListeners:
    def __init__(
        self,
        *,
        name: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        allowed_routes: typing.Optional[typing.Union["GatewayV1Beta1SpecListenersAllowedRoutes", typing.Dict[builtins.str, typing.Any]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Union["GatewayV1Beta1SpecListenersTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Listener embodies the concept of a logical endpoint where a Gateway accepts network connections.

        :param name: Name is the name of the Listener. This name MUST be unique within a Gateway. Support: Core
        :param port: Port is the network port. Multiple listeners may use the same port, subject to the Listener compatibility rules. Support: Core
        :param protocol: Protocol specifies the network protocol this listener expects to receive. Support: Core
        :param allowed_routes: AllowedRoutes defines the types of routes that MAY be attached to a Listener and the trusted namespaces where those Route resources MAY be present. Although a client request may match multiple route rules, only one rule may ultimately receive the request. Matching precedence MUST be determined in order of the following criteria: - The most specific match as defined by the Route type. * The oldest Route based on creation timestamp. For example, a Route with a creation timestamp of "2020-09-08 01:02:03" is given precedence over a Route with a creation timestamp of "2020-09-08 01:02:04". * If everything else is equivalent, the Route appearing first in alphabetical order (namespace/name) should be given precedence. For example, foo/bar is given precedence over foo/baz. All valid rules within a Route attached to this Listener should be implemented. Invalid Route rules can be ignored (sometimes that will mean the full Route). If a Route rule transitions from valid to invalid, support for that Route rule should be dropped to ensure consistency. For example, even if a filter specified by a Route rule is invalid, the rest of the rules within that Route should still be supported. Support: Core
        :param hostname: Hostname specifies the virtual hostname to match for protocol types that define this concept. When unspecified, all hostnames are matched. This field is ignored for protocols that don't require hostname based matching. Implementations MUST apply Hostname matching appropriately for each of the following protocols: - TLS: The Listener Hostname MUST match the SNI. * HTTP: The Listener Hostname MUST match the Host header of the request. * HTTPS: The Listener Hostname SHOULD match at both the TLS and HTTP protocol layers as described above. If an implementation does not ensure that both the SNI and Host header match the Listener hostname, it MUST clearly document that. For HTTPRoute and TLSRoute resources, there is an interaction with the ``spec.hostnames`` array. When both listener and route specify hostnames, there MUST be an intersection between the values for a Route to be accepted. For more information, refer to the Route specific Hostnames documentation. Hostnames that are prefixed with a wildcard label (``*.``) are interpreted as a suffix match. That means that a match for ``*.example.com`` would match both ``test.example.com``, and ``foo.test.example.com``, but not ``example.com``. Support: Core
        :param tls: TLS is the TLS configuration for the Listener. This field is required if the Protocol field is "HTTPS" or "TLS". It is invalid to set this field if the Protocol field is "HTTP", "TCP", or "UDP". The association of SNIs to Certificate defined in GatewayTLSConfig is defined based on the Hostname field for this listener. The GatewayClass MUST use the longest matching SNI out of all available certificates for any TLS handshake. Support: Core

        :schema: GatewayV1Beta1SpecListeners
        '''
        if isinstance(allowed_routes, dict):
            allowed_routes = GatewayV1Beta1SpecListenersAllowedRoutes(**allowed_routes)
        if isinstance(tls, dict):
            tls = GatewayV1Beta1SpecListenersTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408402aa1faae64caafc9292f4e2186511dadddabdcc284936b1d422c8111d2e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument allowed_routes", value=allowed_routes, expected_type=type_hints["allowed_routes"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "port": port,
            "protocol": protocol,
        }
        if allowed_routes is not None:
            self._values["allowed_routes"] = allowed_routes
        if hostname is not None:
            self._values["hostname"] = hostname
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is the name of the Listener.

        This name MUST be unique within a Gateway.
        Support: Core

        :schema: GatewayV1Beta1SpecListeners#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port is the network port.

        Multiple listeners may use the same port, subject to the Listener compatibility rules.
        Support: Core

        :schema: GatewayV1Beta1SpecListeners#port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Protocol specifies the network protocol this listener expects to receive.

        Support: Core

        :schema: GatewayV1Beta1SpecListeners#protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_routes(
        self,
    ) -> typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutes"]:
        '''AllowedRoutes defines the types of routes that MAY be attached to a Listener and the trusted namespaces where those Route resources MAY be present.

        Although a client request may match multiple route rules, only one rule may ultimately receive the request. Matching precedence MUST be determined in order of the following criteria:

        - The most specific match as defined by the Route type. * The oldest Route based on creation timestamp. For example, a Route with   a creation timestamp of "2020-09-08 01:02:03" is given precedence over   a Route with a creation timestamp of "2020-09-08 01:02:04". * If everything else is equivalent, the Route appearing first in   alphabetical order (namespace/name) should be given precedence. For   example, foo/bar is given precedence over foo/baz.
          All valid rules within a Route attached to this Listener should be implemented. Invalid Route rules can be ignored (sometimes that will mean the full Route). If a Route rule transitions from valid to invalid, support for that Route rule should be dropped to ensure consistency. For example, even if a filter specified by a Route rule is invalid, the rest of the rules within that Route should still be supported.
          Support: Core

        :schema: GatewayV1Beta1SpecListeners#allowedRoutes
        '''
        result = self._values.get("allowed_routes")
        return typing.cast(typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutes"], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Hostname specifies the virtual hostname to match for protocol types that define this concept.

        When unspecified, all hostnames are matched. This field is ignored for protocols that don't require hostname based matching.
        Implementations MUST apply Hostname matching appropriately for each of the following protocols:

        - TLS: The Listener Hostname MUST match the SNI. * HTTP: The Listener Hostname MUST match the Host header of the request. * HTTPS: The Listener Hostname SHOULD match at both the TLS and HTTP   protocol layers as described above. If an implementation does not   ensure that both the SNI and Host header match the Listener hostname,   it MUST clearly document that.
          For HTTPRoute and TLSRoute resources, there is an interaction with the ``spec.hostnames`` array. When both listener and route specify hostnames, there MUST be an intersection between the values for a Route to be accepted. For more information, refer to the Route specific Hostnames documentation.
          Hostnames that are prefixed with a wildcard label (``*.``) are interpreted as a suffix match. That means that a match for ``*.example.com`` would match both ``test.example.com``, and ``foo.test.example.com``, but not ``example.com``.
          Support: Core

        :schema: GatewayV1Beta1SpecListeners#hostname
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls(self) -> typing.Optional["GatewayV1Beta1SpecListenersTls"]:
        '''TLS is the TLS configuration for the Listener.

        This field is required if the Protocol field is "HTTPS" or "TLS". It is invalid to set this field if the Protocol field is "HTTP", "TCP", or "UDP".
        The association of SNIs to Certificate defined in GatewayTLSConfig is defined based on the Hostname field for this listener.
        The GatewayClass MUST use the longest matching SNI out of all available certificates for any TLS handshake.
        Support: Core

        :schema: GatewayV1Beta1SpecListeners#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["GatewayV1Beta1SpecListenersTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListeners(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersAllowedRoutes",
    jsii_struct_bases=[],
    name_mapping={"kinds": "kinds", "namespaces": "namespaces"},
)
class GatewayV1Beta1SpecListenersAllowedRoutes:
    def __init__(
        self,
        *,
        kinds: typing.Optional[typing.Sequence[typing.Union["GatewayV1Beta1SpecListenersAllowedRoutesKinds", typing.Dict[builtins.str, typing.Any]]]] = None,
        namespaces: typing.Optional[typing.Union["GatewayV1Beta1SpecListenersAllowedRoutesNamespaces", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''AllowedRoutes defines the types of routes that MAY be attached to a Listener and the trusted namespaces where those Route resources MAY be present.

        Although a client request may match multiple route rules, only one rule may ultimately receive the request. Matching precedence MUST be determined in order of the following criteria:

        - The most specific match as defined by the Route type. * The oldest Route based on creation timestamp. For example, a Route with   a creation timestamp of "2020-09-08 01:02:03" is given precedence over   a Route with a creation timestamp of "2020-09-08 01:02:04". * If everything else is equivalent, the Route appearing first in   alphabetical order (namespace/name) should be given precedence. For   example, foo/bar is given precedence over foo/baz.
          All valid rules within a Route attached to this Listener should be implemented. Invalid Route rules can be ignored (sometimes that will mean the full Route). If a Route rule transitions from valid to invalid, support for that Route rule should be dropped to ensure consistency. For example, even if a filter specified by a Route rule is invalid, the rest of the rules within that Route should still be supported.
          Support: Core

        :param kinds: Kinds specifies the groups and kinds of Routes that are allowed to bind to this Gateway Listener. When unspecified or empty, the kinds of Routes selected are determined using the Listener protocol. A RouteGroupKind MUST correspond to kinds of Routes that are compatible with the application protocol specified in the Listener's Protocol field. If an implementation does not support or recognize this resource type, it MUST set the "ResolvedRefs" condition to False for this Listener with the "InvalidRouteKinds" reason. Support: Core
        :param namespaces: Namespaces indicates namespaces from which Routes may be attached to this Listener. This is restricted to the namespace of this Gateway by default. Support: Core

        :schema: GatewayV1Beta1SpecListenersAllowedRoutes
        '''
        if isinstance(namespaces, dict):
            namespaces = GatewayV1Beta1SpecListenersAllowedRoutesNamespaces(**namespaces)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb3793d87b96bd02489b896e73e97738b3c214038618c0e9879074c539a155c1)
            check_type(argname="argument kinds", value=kinds, expected_type=type_hints["kinds"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kinds is not None:
            self._values["kinds"] = kinds
        if namespaces is not None:
            self._values["namespaces"] = namespaces

    @builtins.property
    def kinds(
        self,
    ) -> typing.Optional[typing.List["GatewayV1Beta1SpecListenersAllowedRoutesKinds"]]:
        '''Kinds specifies the groups and kinds of Routes that are allowed to bind to this Gateway Listener.

        When unspecified or empty, the kinds of Routes selected are determined using the Listener protocol.
        A RouteGroupKind MUST correspond to kinds of Routes that are compatible with the application protocol specified in the Listener's Protocol field. If an implementation does not support or recognize this resource type, it MUST set the "ResolvedRefs" condition to False for this Listener with the "InvalidRouteKinds" reason.
        Support: Core

        :schema: GatewayV1Beta1SpecListenersAllowedRoutes#kinds
        '''
        result = self._values.get("kinds")
        return typing.cast(typing.Optional[typing.List["GatewayV1Beta1SpecListenersAllowedRoutesKinds"]], result)

    @builtins.property
    def namespaces(
        self,
    ) -> typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespaces"]:
        '''Namespaces indicates namespaces from which Routes may be attached to this Listener.

        This is restricted to the namespace of this Gateway by default.
        Support: Core

        :schema: GatewayV1Beta1SpecListenersAllowedRoutes#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespaces"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersAllowedRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersAllowedRoutesKinds",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "group": "group"},
)
class GatewayV1Beta1SpecListenersAllowedRoutesKinds:
    def __init__(
        self,
        *,
        kind: builtins.str,
        group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''RouteGroupKind indicates the group and kind of a Route resource.

        :param kind: Kind is the kind of the Route.
        :param group: Group is the group of the Route.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesKinds
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f99b0d1388de88cfde6cb51e5170729901ab29efbf22496ac0b8d64130a625a)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kind": kind,
        }
        if group is not None:
            self._values["group"] = group

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind is the kind of the Route.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesKinds#kind
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the group of the Route.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesKinds#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersAllowedRoutesKinds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersAllowedRoutesNamespaces",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "selector": "selector"},
)
class GatewayV1Beta1SpecListenersAllowedRoutesNamespaces:
    def __init__(
        self,
        *,
        from_: typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom"] = None,
        selector: typing.Optional[typing.Union["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Namespaces indicates namespaces from which Routes may be attached to this Listener.

        This is restricted to the namespace of this Gateway by default.
        Support: Core

        :param from_: From indicates where Routes will be selected for this Gateway. Possible values are: * All: Routes in all namespaces may be used by this Gateway. * Selector: Routes in namespaces selected by the selector may be used by this Gateway. * Same: Only Routes in the same namespace may be used by this Gateway. Support: Core
        :param selector: Selector must be specified when From is set to "Selector". In that case, only Routes in Namespaces matching this Selector will be selected by this Gateway. This field is ignored for other values of "From". Support: Core

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespaces
        '''
        if isinstance(selector, dict):
            selector = GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector(**selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d80b84379c1ad3d22b799ea65c1a799c66be69b1c7223e00b44e2e56d0df7d)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def from_(
        self,
    ) -> typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom"]:
        '''From indicates where Routes will be selected for this Gateway.

        Possible values are: * All: Routes in all namespaces may be used by this Gateway. * Selector: Routes in namespaces selected by the selector may be used by   this Gateway. * Same: Only Routes in the same namespace may be used by this Gateway.
        Support: Core

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespaces#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom"], result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector"]:
        '''Selector must be specified when From is set to "Selector".

        In that case, only Routes in Namespaces matching this Selector will be selected by this Gateway. This field is ignored for other values of "From".
        Support: Core

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespaces#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersAllowedRoutesNamespaces(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom"
)
class GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom(enum.Enum):
    '''From indicates where Routes will be selected for this Gateway.

    Possible values are: * All: Routes in all namespaces may be used by this Gateway. * Selector: Routes in namespaces selected by the selector may be used by   this Gateway. * Same: Only Routes in the same namespace may be used by this Gateway.
    Support: Core

    :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom
    '''

    ALL = "ALL"
    '''All.'''
    SELECTOR = "SELECTOR"
    '''Selector.'''
    SAME = "SAME"
    '''Same.'''


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Selector must be specified when From is set to "Selector".

        In that case, only Routes in Namespaces matching this Selector will be selected by this Gateway. This field is ignored for other values of "From".
        Support: Core

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__490fea60321726d8875cb8ae55314c2b161a7dad1c6a326452f127d9b300d71f)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4050b55fe1a77e7bd59c1c86bee9c63b14eb2208853fa8cdaacb65132be9a712)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersTls",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_refs": "certificateRefs",
        "mode": "mode",
        "options": "options",
    },
)
class GatewayV1Beta1SpecListenersTls:
    def __init__(
        self,
        *,
        certificate_refs: typing.Optional[typing.Sequence[typing.Union["GatewayV1Beta1SpecListenersTlsCertificateRefs", typing.Dict[builtins.str, typing.Any]]]] = None,
        mode: typing.Optional["GatewayV1Beta1SpecListenersTlsMode"] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''TLS is the TLS configuration for the Listener.

        This field is required if the Protocol field is "HTTPS" or "TLS". It is invalid to set this field if the Protocol field is "HTTP", "TCP", or "UDP".
        The association of SNIs to Certificate defined in GatewayTLSConfig is defined based on the Hostname field for this listener.
        The GatewayClass MUST use the longest matching SNI out of all available certificates for any TLS handshake.
        Support: Core

        :param certificate_refs: CertificateRefs contains a series of references to Kubernetes objects that contains TLS certificates and private keys. These certificates are used to establish a TLS handshake for requests that match the hostname of the associated listener. A single CertificateRef to a Kubernetes Secret has "Core" support. Implementations MAY choose to support attaching multiple certificates to a Listener, but this behavior is implementation-specific. References to a resource in different namespace are invalid UNLESS there is a ReferenceGrant in the target namespace that allows the certificate to be attached. If a ReferenceGrant does not allow this reference, the "ResolvedRefs" condition MUST be set to False for this listener with the "RefNotPermitted" reason. This field is required to have at least one element when the mode is set to "Terminate" (default) and is optional otherwise. CertificateRefs can reference to standard Kubernetes resources, i.e. Secret, or implementation-specific custom resources. Support: Core - A single reference to a Kubernetes Secret of type kubernetes.io/tls Support: Implementation-specific (More than one reference or other resource types)
        :param mode: Mode defines the TLS behavior for the TLS session initiated by the client. There are two possible modes: - Terminate: The TLS session between the downstream client and the Gateway is terminated at the Gateway. This mode requires certificateRefs to be set and contain at least one element. - Passthrough: The TLS session is NOT terminated by the Gateway. This implies that the Gateway can't decipher the TLS stream except for the ClientHello message of the TLS protocol. CertificateRefs field is ignored in this mode. Support: Core
        :param options: Options are a list of key/value pairs to enable extended TLS configuration for each implementation. For example, configuring the minimum TLS version or supported cipher suites. A set of common keys MAY be defined by the API in the future. To avoid any ambiguity, implementation-specific definitions MUST use domain-prefixed names, such as ``example.com/my-custom-option``. Un-prefixed names are reserved for key names defined by Gateway API. Support: Implementation-specific

        :schema: GatewayV1Beta1SpecListenersTls
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb56c7b05ae43b3d98c09f3e44555634b8ecd4b09cecf49ec8828f088f406731)
            check_type(argname="argument certificate_refs", value=certificate_refs, expected_type=type_hints["certificate_refs"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate_refs is not None:
            self._values["certificate_refs"] = certificate_refs
        if mode is not None:
            self._values["mode"] = mode
        if options is not None:
            self._values["options"] = options

    @builtins.property
    def certificate_refs(
        self,
    ) -> typing.Optional[typing.List["GatewayV1Beta1SpecListenersTlsCertificateRefs"]]:
        '''CertificateRefs contains a series of references to Kubernetes objects that contains TLS certificates and private keys.

        These certificates are used to establish a TLS handshake for requests that match the hostname of the associated listener.
        A single CertificateRef to a Kubernetes Secret has "Core" support. Implementations MAY choose to support attaching multiple certificates to a Listener, but this behavior is implementation-specific.
        References to a resource in different namespace are invalid UNLESS there is a ReferenceGrant in the target namespace that allows the certificate to be attached. If a ReferenceGrant does not allow this reference, the "ResolvedRefs" condition MUST be set to False for this listener with the "RefNotPermitted" reason.
        This field is required to have at least one element when the mode is set to "Terminate" (default) and is optional otherwise.
        CertificateRefs can reference to standard Kubernetes resources, i.e. Secret, or implementation-specific custom resources.
        Support: Core - A single reference to a Kubernetes Secret of type kubernetes.io/tls
        Support: Implementation-specific (More than one reference or other resource types)

        :schema: GatewayV1Beta1SpecListenersTls#certificateRefs
        '''
        result = self._values.get("certificate_refs")
        return typing.cast(typing.Optional[typing.List["GatewayV1Beta1SpecListenersTlsCertificateRefs"]], result)

    @builtins.property
    def mode(self) -> typing.Optional["GatewayV1Beta1SpecListenersTlsMode"]:
        '''Mode defines the TLS behavior for the TLS session initiated by the client.

        There are two possible modes:

        - Terminate: The TLS session between the downstream client   and the Gateway is terminated at the Gateway. This mode requires   certificateRefs to be set and contain at least one element. - Passthrough: The TLS session is NOT terminated by the Gateway. This   implies that the Gateway can't decipher the TLS stream except for   the ClientHello message of the TLS protocol.   CertificateRefs field is ignored in this mode.
          Support: Core

        :schema: GatewayV1Beta1SpecListenersTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["GatewayV1Beta1SpecListenersTlsMode"], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Options are a list of key/value pairs to enable extended TLS configuration for each implementation.

        For example, configuring the minimum TLS version or supported cipher suites.
        A set of common keys MAY be defined by the API in the future. To avoid any ambiguity, implementation-specific definitions MUST use domain-prefixed names, such as ``example.com/my-custom-option``. Un-prefixed names are reserved for key names defined by Gateway API.
        Support: Implementation-specific

        :schema: GatewayV1Beta1SpecListenersTls#options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersTlsCertificateRefs",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "group": "group",
        "kind": "kind",
        "namespace": "namespace",
    },
)
class GatewayV1Beta1SpecListenersTlsCertificateRefs:
    def __init__(
        self,
        *,
        name: builtins.str,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''SecretObjectReference identifies an API object including its namespace, defaulting to Secret.

        The API object must be valid in the cluster; the Group and Kind must be registered in the cluster for this reference to be valid.
        References to objects with invalid Group and Kind are not valid, and must be rejected by the implementation, with appropriate Conditions set on the containing object.

        :param name: Name is the name of the referent.
        :param group: Group is the group of the referent. For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.
        :param kind: Kind is kind of the referent. For example "HTTPRoute" or "Service".
        :param namespace: Namespace is the namespace of the backend. When unspecified, the local namespace is inferred. Note that when a namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. Support: Core

        :schema: GatewayV1Beta1SpecListenersTlsCertificateRefs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f699b2d64fbd6b3e72f042e8aca5a433224f44cba9923bc25d8c8d0743b4d48)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is the name of the referent.

        :schema: GatewayV1Beta1SpecListenersTlsCertificateRefs#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the group of the referent.

        For example, "gateway.networking.k8s.io". When unspecified or empty string, core API group is inferred.

        :schema: GatewayV1Beta1SpecListenersTlsCertificateRefs#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind is kind of the referent.

        For example "HTTPRoute" or "Service".

        :schema: GatewayV1Beta1SpecListenersTlsCertificateRefs#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace is the namespace of the backend.

        When unspecified, the local namespace is inferred.
        Note that when a namespace is specified, a ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details.
        Support: Core

        :schema: GatewayV1Beta1SpecListenersTlsCertificateRefs#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayV1Beta1SpecListenersTlsCertificateRefs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iok8snetworkinggateway.GatewayV1Beta1SpecListenersTlsMode")
class GatewayV1Beta1SpecListenersTlsMode(enum.Enum):
    '''Mode defines the TLS behavior for the TLS session initiated by the client.

    There are two possible modes:

    - Terminate: The TLS session between the downstream client   and the Gateway is terminated at the Gateway. This mode requires   certificateRefs to be set and contain at least one element. - Passthrough: The TLS session is NOT terminated by the Gateway. This   implies that the Gateway can't decipher the TLS stream except for   the ClientHello message of the TLS protocol.   CertificateRefs field is ignored in this mode.
      Support: Core

    :schema: GatewayV1Beta1SpecListenersTlsMode
    '''

    TERMINATE = "TERMINATE"
    '''Terminate.'''
    PASSTHROUGH = "PASSTHROUGH"
    '''Passthrough.'''


__all__ = [
    "Gateway",
    "GatewayProps",
    "GatewaySpec",
    "GatewaySpecAddresses",
    "GatewaySpecListeners",
    "GatewaySpecListenersAllowedRoutes",
    "GatewaySpecListenersAllowedRoutesKinds",
    "GatewaySpecListenersAllowedRoutesNamespaces",
    "GatewaySpecListenersAllowedRoutesNamespacesFrom",
    "GatewaySpecListenersAllowedRoutesNamespacesSelector",
    "GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions",
    "GatewaySpecListenersTls",
    "GatewaySpecListenersTlsCertificateRefs",
    "GatewaySpecListenersTlsMode",
    "GatewayV1Beta1",
    "GatewayV1Beta1Props",
    "GatewayV1Beta1Spec",
    "GatewayV1Beta1SpecAddresses",
    "GatewayV1Beta1SpecListeners",
    "GatewayV1Beta1SpecListenersAllowedRoutes",
    "GatewayV1Beta1SpecListenersAllowedRoutesKinds",
    "GatewayV1Beta1SpecListenersAllowedRoutesNamespaces",
    "GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom",
    "GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector",
    "GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions",
    "GatewayV1Beta1SpecListenersTls",
    "GatewayV1Beta1SpecListenersTlsCertificateRefs",
    "GatewayV1Beta1SpecListenersTlsMode",
]

publication.publish()

def _typecheckingstub__cabc98ad409afc45e6aaf13b346e8cb91a2ff88c935a0841bfe8497949111873(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    spec: typing.Union[GatewaySpec, typing.Dict[builtins.str, typing.Any]],
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68ff39a41520cfbc09e8a40c697f4c39299f0b6ba29623a484142c4fab4ffceb(
    *,
    spec: typing.Union[GatewaySpec, typing.Dict[builtins.str, typing.Any]],
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46a4037929c0780bbc611db172de1e56e3cdefa4bdb57ea9298cff19a423a5e(
    *,
    gateway_class_name: builtins.str,
    listeners: typing.Sequence[typing.Union[GatewaySpecListeners, typing.Dict[builtins.str, typing.Any]]],
    addresses: typing.Optional[typing.Sequence[typing.Union[GatewaySpecAddresses, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f275a6bf24c8a4fed5442c00181fdb061ab84b6daac136d26f49fd21a2b713a(
    *,
    value: builtins.str,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f57af45c000f3b0113b5ceb798cfae33297c7e6d199853aba563e893a17469(
    *,
    name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    allowed_routes: typing.Optional[typing.Union[GatewaySpecListenersAllowedRoutes, typing.Dict[builtins.str, typing.Any]]] = None,
    hostname: typing.Optional[builtins.str] = None,
    tls: typing.Optional[typing.Union[GatewaySpecListenersTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f2afb6226781697a696dca7925a71469f547b8fba16b42b177a8ee1070def0(
    *,
    kinds: typing.Optional[typing.Sequence[typing.Union[GatewaySpecListenersAllowedRoutesKinds, typing.Dict[builtins.str, typing.Any]]]] = None,
    namespaces: typing.Optional[typing.Union[GatewaySpecListenersAllowedRoutesNamespaces, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d8c6aebe14746acdc13aedac61c85f43350c634c7ca2379e01f3def9ffb657f(
    *,
    kind: builtins.str,
    group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__276beb87cc4d924064af5084f0481aa0719f81f898b75cb969e5dd8fe5a6ab59(
    *,
    from_: typing.Optional[GatewaySpecListenersAllowedRoutesNamespacesFrom] = None,
    selector: typing.Optional[typing.Union[GatewaySpecListenersAllowedRoutesNamespacesSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfae7ad6e30bb2c3aba10f88da95e756dc4332b1254eafc521ce1720c89e141(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[GatewaySpecListenersAllowedRoutesNamespacesSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a598a4d2ecdfb536ece21d1bea2a5e7a153578dc49183ce5eac7737b178f32d(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865795c2502624e6577be2833a2c185731b15a1b6ad9762143fd128de2b34ca0(
    *,
    certificate_refs: typing.Optional[typing.Sequence[typing.Union[GatewaySpecListenersTlsCertificateRefs, typing.Dict[builtins.str, typing.Any]]]] = None,
    mode: typing.Optional[GatewaySpecListenersTlsMode] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfafb32b51e4907423918700279f5e9163e14dc3a391ce2408c1a2ae35989047(
    *,
    name: builtins.str,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd36ce29efb9e8350ca75d0fecf56fe3ee1345122154083eedc218616b9c3dc5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    spec: typing.Union[GatewayV1Beta1Spec, typing.Dict[builtins.str, typing.Any]],
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6111bfdec888c302c2cfab8e592d78d82210d1bc50e676adc3a57e1bd2e386(
    *,
    spec: typing.Union[GatewayV1Beta1Spec, typing.Dict[builtins.str, typing.Any]],
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee67507f87f5032c1c7344ad95ec863d34ba5233a832e225a042211946293734(
    *,
    gateway_class_name: builtins.str,
    listeners: typing.Sequence[typing.Union[GatewayV1Beta1SpecListeners, typing.Dict[builtins.str, typing.Any]]],
    addresses: typing.Optional[typing.Sequence[typing.Union[GatewayV1Beta1SpecAddresses, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93674cf130d5dbfd21e90fc3655cdd3def5daa1592cca0e09b70e7f4e25fed2(
    *,
    value: builtins.str,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408402aa1faae64caafc9292f4e2186511dadddabdcc284936b1d422c8111d2e(
    *,
    name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    allowed_routes: typing.Optional[typing.Union[GatewayV1Beta1SpecListenersAllowedRoutes, typing.Dict[builtins.str, typing.Any]]] = None,
    hostname: typing.Optional[builtins.str] = None,
    tls: typing.Optional[typing.Union[GatewayV1Beta1SpecListenersTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3793d87b96bd02489b896e73e97738b3c214038618c0e9879074c539a155c1(
    *,
    kinds: typing.Optional[typing.Sequence[typing.Union[GatewayV1Beta1SpecListenersAllowedRoutesKinds, typing.Dict[builtins.str, typing.Any]]]] = None,
    namespaces: typing.Optional[typing.Union[GatewayV1Beta1SpecListenersAllowedRoutesNamespaces, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f99b0d1388de88cfde6cb51e5170729901ab29efbf22496ac0b8d64130a625a(
    *,
    kind: builtins.str,
    group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d80b84379c1ad3d22b799ea65c1a799c66be69b1c7223e00b44e2e56d0df7d(
    *,
    from_: typing.Optional[GatewayV1Beta1SpecListenersAllowedRoutesNamespacesFrom] = None,
    selector: typing.Optional[typing.Union[GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490fea60321726d8875cb8ae55314c2b161a7dad1c6a326452f127d9b300d71f(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[GatewayV1Beta1SpecListenersAllowedRoutesNamespacesSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4050b55fe1a77e7bd59c1c86bee9c63b14eb2208853fa8cdaacb65132be9a712(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb56c7b05ae43b3d98c09f3e44555634b8ecd4b09cecf49ec8828f088f406731(
    *,
    certificate_refs: typing.Optional[typing.Sequence[typing.Union[GatewayV1Beta1SpecListenersTlsCertificateRefs, typing.Dict[builtins.str, typing.Any]]]] = None,
    mode: typing.Optional[GatewayV1Beta1SpecListenersTlsMode] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f699b2d64fbd6b3e72f042e8aca5a433224f44cba9923bc25d8c8d0743b4d48(
    *,
    name: builtins.str,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
