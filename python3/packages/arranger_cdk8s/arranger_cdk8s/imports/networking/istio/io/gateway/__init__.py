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


class Gateway(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioiogateway.Gateway",
):
    """
    :schema: Gateway
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["GatewaySpec"] = None,
    ) -> None:
        """Defines a "Gateway" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration affecting edge load balancer. See more details at: https://istio.io/docs/reference/config/networking/gateway.html
        """
        options = GatewayOptions(spec=spec)

        jsii.create(Gateway, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioiogateway.GatewayOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class GatewayOptions:
    def __init__(self, *, spec: typing.Optional["GatewaySpec"] = None) -> None:
        """
        :param spec: Configuration affecting edge load balancer. See more details at: https://istio.io/docs/reference/config/networking/gateway.html

        :schema: Gateway
        """
        if isinstance(spec, dict):
            spec = GatewaySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["GatewaySpec"]:
        """Configuration affecting edge load balancer.

        See more details at: https://istio.io/docs/reference/config/networking/gateway.html

        :schema: Gateway#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiogateway.GatewaySpec",
    jsii_struct_bases=[],
    name_mapping={"selector": "selector", "servers": "servers"},
)
class GatewaySpec:
    def __init__(
        self,
        *,
        selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        servers: typing.Optional[typing.List["GatewaySpecServers"]] = None,
    ) -> None:
        """Configuration affecting edge load balancer.

        See more details at: https://istio.io/docs/reference/config/networking/gateway.html

        :param selector: 
        :param servers: A list of server specifications.

        :schema: GatewaySpec
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if selector is not None:
            self._values["selector"] = selector
        if servers is not None:
            self._values["servers"] = servers

    @builtins.property
    def selector(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: GatewaySpec#selector
        """
        result = self._values.get("selector")
        return result

    @builtins.property
    def servers(self) -> typing.Optional[typing.List["GatewaySpecServers"]]:
        """A list of server specifications.

        :schema: GatewaySpec#servers
        """
        result = self._values.get("servers")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiogateway.GatewaySpecServers",
    jsii_struct_bases=[],
    name_mapping={
        "bind": "bind",
        "default_endpoint": "defaultEndpoint",
        "hosts": "hosts",
        "name": "name",
        "port": "port",
        "tls": "tls",
    },
)
class GatewaySpecServers:
    def __init__(
        self,
        *,
        bind: typing.Optional[builtins.str] = None,
        default_endpoint: typing.Optional[builtins.str] = None,
        hosts: typing.Optional[typing.List[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional["GatewaySpecServersPort"] = None,
        tls: typing.Optional["GatewaySpecServersTls"] = None,
    ) -> None:
        """
        :param bind: 
        :param default_endpoint: 
        :param hosts: One or more hosts exposed by this gateway.
        :param name: An optional name of the server, when set must be unique across all servers.
        :param port: 
        :param tls: Set of TLS related options that govern the server's behavior.

        :schema: GatewaySpecServers
        """
        if isinstance(port, dict):
            port = GatewaySpecServersPort(**port)
        if isinstance(tls, dict):
            tls = GatewaySpecServersTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if bind is not None:
            self._values["bind"] = bind
        if default_endpoint is not None:
            self._values["default_endpoint"] = default_endpoint
        if hosts is not None:
            self._values["hosts"] = hosts
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def bind(self) -> typing.Optional[builtins.str]:
        """
        :schema: GatewaySpecServers#bind
        """
        result = self._values.get("bind")
        return result

    @builtins.property
    def default_endpoint(self) -> typing.Optional[builtins.str]:
        """
        :schema: GatewaySpecServers#defaultEndpoint
        """
        result = self._values.get("default_endpoint")
        return result

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """One or more hosts exposed by this gateway.

        :schema: GatewaySpecServers#hosts
        """
        result = self._values.get("hosts")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """An optional name of the server, when set must be unique across all servers.

        :schema: GatewaySpecServers#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def port(self) -> typing.Optional["GatewaySpecServersPort"]:
        """
        :schema: GatewaySpecServers#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def tls(self) -> typing.Optional["GatewaySpecServersTls"]:
        """Set of TLS related options that govern the server's behavior.

        :schema: GatewaySpecServers#tls
        """
        result = self._values.get("tls")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecServers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiogateway.GatewaySpecServersPort",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class GatewaySpecServersPort:
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

        :schema: GatewaySpecServersPort
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

        :schema: GatewaySpecServersPort#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """A valid non-negative integer port number.

        :schema: GatewaySpecServersPort#number
        """
        result = self._values.get("number")
        return result

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        """The protocol exposed on the port.

        :schema: GatewaySpecServersPort#protocol
        """
        result = self._values.get("protocol")
        return result

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        """
        :schema: GatewaySpecServersPort#targetPort
        """
        result = self._values.get("target_port")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecServersPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiogateway.GatewaySpecServersTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "cipher_suites": "cipherSuites",
        "credential_name": "credentialName",
        "https_redirect": "httpsRedirect",
        "max_protocol_version": "maxProtocolVersion",
        "min_protocol_version": "minProtocolVersion",
        "mode": "mode",
        "private_key": "privateKey",
        "server_certificate": "serverCertificate",
        "subject_alt_names": "subjectAltNames",
        "verify_certificate_hash": "verifyCertificateHash",
        "verify_certificate_spki": "verifyCertificateSpki",
    },
)
class GatewaySpecServersTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        cipher_suites: typing.Optional[typing.List[builtins.str]] = None,
        credential_name: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[builtins.bool] = None,
        max_protocol_version: typing.Optional["GatewaySpecServersTlsMaxProtocolVersion"] = None,
        min_protocol_version: typing.Optional["GatewaySpecServersTlsMinProtocolVersion"] = None,
        mode: typing.Optional["GatewaySpecServersTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.List[builtins.str]] = None,
        verify_certificate_hash: typing.Optional[typing.List[builtins.str]] = None,
        verify_certificate_spki: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """Set of TLS related options that govern the server's behavior.

        :param ca_certificates: REQUIRED if mode is ``MUTUAL``.
        :param cipher_suites: Optional: If specified, only support the specified cipher list.
        :param credential_name: 
        :param https_redirect: 
        :param max_protocol_version: Optional: Maximum TLS protocol version.
        :param min_protocol_version: Optional: Minimum TLS protocol version.
        :param mode: 
        :param private_key: REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.
        :param server_certificate: REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.
        :param subject_alt_names: 
        :param verify_certificate_hash: 
        :param verify_certificate_spki: 

        :schema: GatewaySpecServersTls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if cipher_suites is not None:
            self._values["cipher_suites"] = cipher_suites
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if max_protocol_version is not None:
            self._values["max_protocol_version"] = max_protocol_version
        if min_protocol_version is not None:
            self._values["min_protocol_version"] = min_protocol_version
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if server_certificate is not None:
            self._values["server_certificate"] = server_certificate
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names
        if verify_certificate_hash is not None:
            self._values["verify_certificate_hash"] = verify_certificate_hash
        if verify_certificate_spki is not None:
            self._values["verify_certificate_spki"] = verify_certificate_spki

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: GatewaySpecServersTls#caCertificates
        """
        result = self._values.get("ca_certificates")
        return result

    @builtins.property
    def cipher_suites(self) -> typing.Optional[typing.List[builtins.str]]:
        """Optional: If specified, only support the specified cipher list.

        :schema: GatewaySpecServersTls#cipherSuites
        """
        result = self._values.get("cipher_suites")
        return result

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        """
        :schema: GatewaySpecServersTls#credentialName
        """
        result = self._values.get("credential_name")
        return result

    @builtins.property
    def https_redirect(self) -> typing.Optional[builtins.bool]:
        """
        :schema: GatewaySpecServersTls#httpsRedirect
        """
        result = self._values.get("https_redirect")
        return result

    @builtins.property
    def max_protocol_version(
        self,
    ) -> typing.Optional["GatewaySpecServersTlsMaxProtocolVersion"]:
        """Optional: Maximum TLS protocol version.

        :schema: GatewaySpecServersTls#maxProtocolVersion
        """
        result = self._values.get("max_protocol_version")
        return result

    @builtins.property
    def min_protocol_version(
        self,
    ) -> typing.Optional["GatewaySpecServersTlsMinProtocolVersion"]:
        """Optional: Minimum TLS protocol version.

        :schema: GatewaySpecServersTls#minProtocolVersion
        """
        result = self._values.get("min_protocol_version")
        return result

    @builtins.property
    def mode(self) -> typing.Optional["GatewaySpecServersTlsMode"]:
        """
        :schema: GatewaySpecServersTls#mode
        """
        result = self._values.get("mode")
        return result

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.

        :schema: GatewaySpecServersTls#privateKey
        """
        result = self._values.get("private_key")
        return result

    @builtins.property
    def server_certificate(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.

        :schema: GatewaySpecServersTls#serverCertificate
        """
        result = self._values.get("server_certificate")
        return result

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: GatewaySpecServersTls#subjectAltNames
        """
        result = self._values.get("subject_alt_names")
        return result

    @builtins.property
    def verify_certificate_hash(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: GatewaySpecServersTls#verifyCertificateHash
        """
        result = self._values.get("verify_certificate_hash")
        return result

    @builtins.property
    def verify_certificate_spki(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: GatewaySpecServersTls#verifyCertificateSpki
        """
        result = self._values.get("verify_certificate_spki")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecServersTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiogateway.GatewaySpecServersTlsMaxProtocolVersion"
)
class GatewaySpecServersTlsMaxProtocolVersion(enum.Enum):
    """Optional: Maximum TLS protocol version.

    :schema: GatewaySpecServersTlsMaxProtocolVersion
    """

    TLS_AUTO = "TLS_AUTO"
    """TLS_AUTO."""
    TLSV1_0 = "TLSV1_0"
    """TLSV1_0."""
    TLSV1_1 = "TLSV1_1"
    """TLSV1_1."""
    TLSV1_2 = "TLSV1_2"
    """TLSV1_2."""
    TLSV1_3 = "TLSV1_3"
    """TLSV1_3."""


@jsii.enum(
    jsii_type="networkingistioiogateway.GatewaySpecServersTlsMinProtocolVersion"
)
class GatewaySpecServersTlsMinProtocolVersion(enum.Enum):
    """Optional: Minimum TLS protocol version.

    :schema: GatewaySpecServersTlsMinProtocolVersion
    """

    TLS_AUTO = "TLS_AUTO"
    """TLS_AUTO."""
    TLSV1_0 = "TLSV1_0"
    """TLSV1_0."""
    TLSV1_1 = "TLSV1_1"
    """TLSV1_1."""
    TLSV1_2 = "TLSV1_2"
    """TLSV1_2."""
    TLSV1_3 = "TLSV1_3"
    """TLSV1_3."""


@jsii.enum(jsii_type="networkingistioiogateway.GatewaySpecServersTlsMode")
class GatewaySpecServersTlsMode(enum.Enum):
    """
    :schema: GatewaySpecServersTlsMode
    """

    PASSTHROUGH = "PASSTHROUGH"
    """PASSTHROUGH."""
    SIMPLE = "SIMPLE"
    """SIMPLE."""
    MUTUAL = "MUTUAL"
    """MUTUAL."""
    AUTO_PASSTHROUGH = "AUTO_PASSTHROUGH"
    """AUTO_PASSTHROUGH."""
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    """ISTIO_MUTUAL."""


__all__ = [
    "Gateway",
    "GatewayOptions",
    "GatewaySpec",
    "GatewaySpecServers",
    "GatewaySpecServersPort",
    "GatewaySpecServersTls",
    "GatewaySpecServersTlsMaxProtocolVersion",
    "GatewaySpecServersTlsMinProtocolVersion",
    "GatewaySpecServersTlsMode",
]

publication.publish()
