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


class DestinationRule(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioiodestinationrule.DestinationRule",
):
    """
    :schema: DestinationRule
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["DestinationRuleSpec"] = None,
    ) -> None:
        """Defines a "DestinationRule" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration affecting load balancing, outlier detection, etc. See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html
        """
        options = DestinationRuleOptions(spec=spec)

        jsii.create(DestinationRule, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class DestinationRuleOptions:
    def __init__(self, *, spec: typing.Optional["DestinationRuleSpec"] = None) -> None:
        """
        :param spec: Configuration affecting load balancing, outlier detection, etc. See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html

        :schema: DestinationRule
        """
        if isinstance(spec, dict):
            spec = DestinationRuleSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["DestinationRuleSpec"]:
        """Configuration affecting load balancing, outlier detection, etc.

        See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html

        :schema: DestinationRule#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpec",
    jsii_struct_bases=[],
    name_mapping={
        "export_to": "exportTo",
        "host": "host",
        "subsets": "subsets",
        "traffic_policy": "trafficPolicy",
    },
)
class DestinationRuleSpec:
    def __init__(
        self,
        *,
        export_to: typing.Optional[typing.List[builtins.str]] = None,
        host: typing.Optional[builtins.str] = None,
        subsets: typing.Optional[typing.List["DestinationRuleSpecSubsets"]] = None,
        traffic_policy: typing.Optional["DestinationRuleSpecTrafficPolicy"] = None,
    ) -> None:
        """Configuration affecting load balancing, outlier detection, etc.

        See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html

        :param export_to: A list of namespaces to which this destination rule is exported.
        :param host: The name of a service from the service registry.
        :param subsets: 
        :param traffic_policy: 

        :schema: DestinationRuleSpec
        """
        if isinstance(traffic_policy, dict):
            traffic_policy = DestinationRuleSpecTrafficPolicy(**traffic_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if export_to is not None:
            self._values["export_to"] = export_to
        if host is not None:
            self._values["host"] = host
        if subsets is not None:
            self._values["subsets"] = subsets
        if traffic_policy is not None:
            self._values["traffic_policy"] = traffic_policy

    @builtins.property
    def export_to(self) -> typing.Optional[typing.List[builtins.str]]:
        """A list of namespaces to which this destination rule is exported.

        :schema: DestinationRuleSpec#exportTo
        """
        result = self._values.get("export_to")
        return result

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        """The name of a service from the service registry.

        :schema: DestinationRuleSpec#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def subsets(self) -> typing.Optional[typing.List["DestinationRuleSpecSubsets"]]:
        """
        :schema: DestinationRuleSpec#subsets
        """
        result = self._values.get("subsets")
        return result

    @builtins.property
    def traffic_policy(self) -> typing.Optional["DestinationRuleSpecTrafficPolicy"]:
        """
        :schema: DestinationRuleSpec#trafficPolicy
        """
        result = self._values.get("traffic_policy")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsets",
    jsii_struct_bases=[],
    name_mapping={
        "labels": "labels",
        "name": "name",
        "traffic_policy": "trafficPolicy",
    },
)
class DestinationRuleSpecSubsets:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        traffic_policy: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicy"] = None,
    ) -> None:
        """
        :param labels: 
        :param name: Name of the subset.
        :param traffic_policy: Traffic policies that apply to this subset.

        :schema: DestinationRuleSpecSubsets
        """
        if isinstance(traffic_policy, dict):
            traffic_policy = DestinationRuleSpecSubsetsTrafficPolicy(**traffic_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if traffic_policy is not None:
            self._values["traffic_policy"] = traffic_policy

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: DestinationRuleSpecSubsets#labels
        """
        result = self._values.get("labels")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Name of the subset.

        :schema: DestinationRuleSpecSubsets#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def traffic_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicy"]:
        """Traffic policies that apply to this subset.

        :schema: DestinationRuleSpecSubsets#trafficPolicy
        """
        result = self._values.get("traffic_policy")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port_level_settings": "portLevelSettings",
        "tls": "tls",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicy:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection"] = None,
        port_level_settings: typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings"]] = None,
        tls: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTls"] = None,
    ) -> None:
        """Traffic policies that apply to this subset.

        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port_level_settings: Traffic policies specific to individual ports.
        :param tls: TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy
        """
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecSubsetsTrafficPolicyConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection(**outlier_detection)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecSubsetsTrafficPolicyTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port_level_settings is not None:
            self._values["port_level_settings"] = port_level_settings
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPool"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicy#connectionPool
        """
        result = self._values.get("connection_pool")
        return result

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer"]:
        """Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy#loadBalancer
        """
        result = self._values.get("load_balancer")
        return result

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicy#outlierDetection
        """
        result = self._values.get("outlier_detection")
        return result

    @builtins.property
    def port_level_settings(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings"]]:
        """Traffic policies specific to individual ports.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy#portLevelSettings
        """
        result = self._values.get("port_level_settings")
        return result

    @builtins.property
    def tls(self) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTls"]:
        """TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy#tls
        """
        result = self._values.get("tls")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp"] = None,
    ) -> None:
        """
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPool
        """
        if isinstance(http, dict):
            http = DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp"]:
        """HTTP connection pool settings.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPool#http
        """
        result = self._values.get("http")
        return result

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp"]:
        """Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPool#tcp
        """
        result = self._values.get("tcp")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        """HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"]:
        """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#h2UpgradePolicy
        """
        result = self._values.get("h2_upgrade_policy")
        return result

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#http1MaxPendingRequests
        """
        result = self._values.get("http1_max_pending_requests")
        return result

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#http2MaxRequests
        """
        result = self._values.get("http2_max_requests")
        return result

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        """The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#idleTimeout
        """
        result = self._values.get("idle_timeout")
        return result

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#maxRequestsPerConnection
        """
        result = self._values.get("max_requests_per_connection")
        return result

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#maxRetries
        """
        result = self._values.get("max_retries")
        return result

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        """If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#useClientProtocol
        """
        result = self._values.get("use_client_protocol")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy(
    enum.Enum,
):
    """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy
    """

    DEFAULT = "DEFAULT"
    """DEFAULT."""
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    """DO_NOT_UPGRADE."""
    UPGRADE = "UPGRADE"
    """UPGRADE."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        """Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp
        """
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        """TCP connection timeout.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp#connectTimeout
        """
        result = self._values.get("connect_timeout")
        return result

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        """Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp#maxConnections
        """
        result = self._values.get("max_connections")
        return result

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive"]:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp#tcpKeepalive
        """
        result = self._values.get("tcp_keepalive")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """The time duration between keep-alive probes.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive#probes
        """
        result = self._values.get("probes")
        return result

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive#time
        """
        result = self._values.get("time")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"] = None,
    ) -> None:
        """Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer
        """
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#consistentHash
        """
        result = self._values.get("consistent_hash")
        return result

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#localityLbSetting
        """
        result = self._values.get("locality_lb_setting")
        return result

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#simple
        """
        result = self._values.get("simple")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash
        """
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie"]:
        """Hash based on HTTP cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#httpCookie
        """
        result = self._values.get("http_cookie")
        return result

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#httpHeaderName
        """
        result = self._values.get("http_header_name")
        return result

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#httpQueryParameterName
        """
        result = self._values.get("http_query_parameter_name")
        return result

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#minimumRingSize
        """
        result = self._values.get("minimum_ring_size")
        return result

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        """Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#useSourceIp
        """
        result = self._values.get("use_source_ip")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        """Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Name of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Path to set for the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie#path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        """Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie#ttl
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover"]] = None,
    ) -> None:
        """
        :param distribute: Optional: only one of distribute or failover can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]]:
        """Optional: only one of distribute or failover can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#distribute
        """
        result = self._values.get("distribute")
        return result

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        """enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#enabled
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover"]]:
        """Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#failover
        """
        result = self._values.get("failover")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        """
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating region.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple(enum.Enum):
    """
    :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple
    """

    ROUND_ROBIN = "ROUND_ROBIN"
    """ROUND_ROBIN."""
    LEAST_CONN = "LEAST_CONN"
    """LEAST_CONN."""
    RANDOM = "RANDOM"
    """RANDOM."""
    PASSTHROUGH = "PASSTHROUGH"
    """PASSTHROUGH."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5xx_errors": "consecutive5xxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5xx_errors is not None:
            self._values["consecutive5xx_errors"] = consecutive5xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        """Minimum ejection duration.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#baseEjectionTime
        """
        result = self._values.get("base_ejection_time")
        return result

    @builtins.property
    def consecutive5xx_errors(self) -> typing.Optional[jsii.Number]:
        """Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutive5xxErrors
        """
        result = self._values.get("consecutive5xx_errors")
        return result

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutiveErrors
        """
        result = self._values.get("consecutive_errors")
        return result

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        """Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutiveGatewayErrors
        """
        result = self._values.get("consecutive_gateway_errors")
        return result

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#maxEjectionPercent
        """
        result = self._values.get("max_ejection_percent")
        return result

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#minHealthPercent
        """
        result = self._values.get("min_health_percent")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "tls": "tls",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection"] = None,
        port: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort"] = None,
        tls: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls"] = None,
    ) -> None:
        """
        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port: 
        :param tls: TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings
        """
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection(**outlier_detection)
        if isinstance(port, dict):
            port = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort(**port)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#connectionPool
        """
        result = self._values.get("connection_pool")
        return result

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer"]:
        """Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#loadBalancer
        """
        result = self._values.get("load_balancer")
        return result

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#outlierDetection
        """
        result = self._values.get("outlier_detection")
        return result

    @builtins.property
    def port(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls"]:
        """TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#tls
        """
        result = self._values.get("tls")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp"] = None,
    ) -> None:
        """
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool
        """
        if isinstance(http, dict):
            http = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp"]:
        """HTTP connection pool settings.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool#http
        """
        result = self._values.get("http")
        return result

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp"]:
        """Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool#tcp
        """
        result = self._values.get("tcp")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        """HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"]:
        """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#h2UpgradePolicy
        """
        result = self._values.get("h2_upgrade_policy")
        return result

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#http1MaxPendingRequests
        """
        result = self._values.get("http1_max_pending_requests")
        return result

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#http2MaxRequests
        """
        result = self._values.get("http2_max_requests")
        return result

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        """The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#idleTimeout
        """
        result = self._values.get("idle_timeout")
        return result

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRequestsPerConnection
        """
        result = self._values.get("max_requests_per_connection")
        return result

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRetries
        """
        result = self._values.get("max_retries")
        return result

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        """If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#useClientProtocol
        """
        result = self._values.get("use_client_protocol")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy(
    enum.Enum,
):
    """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy
    """

    DEFAULT = "DEFAULT"
    """DEFAULT."""
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    """DO_NOT_UPGRADE."""
    UPGRADE = "UPGRADE"
    """UPGRADE."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        """Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp
        """
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        """TCP connection timeout.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp#connectTimeout
        """
        result = self._values.get("connect_timeout")
        return result

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        """Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp#maxConnections
        """
        result = self._values.get("max_connections")
        return result

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"]:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp#tcpKeepalive
        """
        result = self._values.get("tcp_keepalive")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """The time duration between keep-alive probes.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#probes
        """
        result = self._values.get("probes")
        return result

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#time
        """
        result = self._values.get("time")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"] = None,
    ) -> None:
        """Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer
        """
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#consistentHash
        """
        result = self._values.get("consistent_hash")
        return result

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#localityLbSetting
        """
        result = self._values.get("locality_lb_setting")
        return result

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#simple
        """
        result = self._values.get("simple")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash
        """
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"]:
        """Hash based on HTTP cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpCookie
        """
        result = self._values.get("http_cookie")
        return result

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpHeaderName
        """
        result = self._values.get("http_header_name")
        return result

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpQueryParameterName
        """
        result = self._values.get("http_query_parameter_name")
        return result

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#minimumRingSize
        """
        result = self._values.get("minimum_ring_size")
        return result

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        """Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#useSourceIp
        """
        result = self._values.get("use_source_ip")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        """Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Name of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Path to set for the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        """Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#ttl
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]] = None,
    ) -> None:
        """
        :param distribute: Optional: only one of distribute or failover can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]]:
        """Optional: only one of distribute or failover can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#distribute
        """
        result = self._values.get("distribute")
        return result

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        """enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#enabled
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]]:
        """Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#failover
        """
        result = self._values.get("failover")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        """
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating region.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple(
    enum.Enum,
):
    """
    :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple
    """

    ROUND_ROBIN = "ROUND_ROBIN"
    """ROUND_ROBIN."""
    LEAST_CONN = "LEAST_CONN"
    """LEAST_CONN."""
    RANDOM = "RANDOM"
    """RANDOM."""
    PASSTHROUGH = "PASSTHROUGH"
    """PASSTHROUGH."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5xx_errors": "consecutive5xxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5xx_errors is not None:
            self._values["consecutive5xx_errors"] = consecutive5xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        """Minimum ejection duration.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#baseEjectionTime
        """
        result = self._values.get("base_ejection_time")
        return result

    @builtins.property
    def consecutive5xx_errors(self) -> typing.Optional[jsii.Number]:
        """Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutive5xxErrors
        """
        result = self._values.get("consecutive5xx_errors")
        return result

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveErrors
        """
        result = self._values.get("consecutive_errors")
        return result

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        """Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveGatewayErrors
        """
        result = self._values.get("consecutive_gateway_errors")
        return result

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#maxEjectionPercent
        """
        result = self._values.get("max_ejection_percent")
        return result

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#minHealthPercent
        """
        result = self._values.get("min_health_percent")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """
        :param number: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        mode: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#caCertificates
        """
        result = self._values.get("ca_certificates")
        return result

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#clientCertificate
        """
        result = self._values.get("client_certificate")
        return result

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#credentialName
        """
        result = self._values.get("credential_name")
        return result

    @builtins.property
    def mode(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#mode
        """
        result = self._values.get("mode")
        return result

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#privateKey
        """
        result = self._values.get("private_key")
        return result

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        """SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#sni
        """
        result = self._values.get("sni")
        return result

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#subjectAltNames
        """
        result = self._values.get("subject_alt_names")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode(enum.Enum):
    """
    :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode
    """

    DISABLE = "DISABLE"
    """DISABLE."""
    SIMPLE = "SIMPLE"
    """SIMPLE."""
    MUTUAL = "MUTUAL"
    """MUTUAL."""
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    """ISTIO_MUTUAL."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        mode: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#caCertificates
        """
        result = self._values.get("ca_certificates")
        return result

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#clientCertificate
        """
        result = self._values.get("client_certificate")
        return result

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#credentialName
        """
        result = self._values.get("credential_name")
        return result

    @builtins.property
    def mode(self) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTlsMode"]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#mode
        """
        result = self._values.get("mode")
        return result

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#privateKey
        """
        result = self._values.get("private_key")
        return result

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        """SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#sni
        """
        result = self._values.get("sni")
        return result

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#subjectAltNames
        """
        result = self._values.get("subject_alt_names")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecSubsetsTrafficPolicyTlsMode"
)
class DestinationRuleSpecSubsetsTrafficPolicyTlsMode(enum.Enum):
    """
    :schema: DestinationRuleSpecSubsetsTrafficPolicyTlsMode
    """

    DISABLE = "DISABLE"
    """DISABLE."""
    SIMPLE = "SIMPLE"
    """SIMPLE."""
    MUTUAL = "MUTUAL"
    """MUTUAL."""
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    """ISTIO_MUTUAL."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port_level_settings": "portLevelSettings",
        "tls": "tls",
    },
)
class DestinationRuleSpecTrafficPolicy:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecTrafficPolicyOutlierDetection"] = None,
        port_level_settings: typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettings"]] = None,
        tls: typing.Optional["DestinationRuleSpecTrafficPolicyTls"] = None,
    ) -> None:
        """
        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port_level_settings: Traffic policies specific to individual ports.
        :param tls: TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicy
        """
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecTrafficPolicyConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecTrafficPolicyLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecTrafficPolicyOutlierDetection(**outlier_detection)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecTrafficPolicyTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port_level_settings is not None:
            self._values["port_level_settings"] = port_level_settings
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPool"]:
        """
        :schema: DestinationRuleSpecTrafficPolicy#connectionPool
        """
        result = self._values.get("connection_pool")
        return result

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancer"]:
        """Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecTrafficPolicy#loadBalancer
        """
        result = self._values.get("load_balancer")
        return result

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyOutlierDetection"]:
        """
        :schema: DestinationRuleSpecTrafficPolicy#outlierDetection
        """
        result = self._values.get("outlier_detection")
        return result

    @builtins.property
    def port_level_settings(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettings"]]:
        """Traffic policies specific to individual ports.

        :schema: DestinationRuleSpecTrafficPolicy#portLevelSettings
        """
        result = self._values.get("port_level_settings")
        return result

    @builtins.property
    def tls(self) -> typing.Optional["DestinationRuleSpecTrafficPolicyTls"]:
        """TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicy#tls
        """
        result = self._values.get("tls")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecTrafficPolicyConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcp"] = None,
    ) -> None:
        """
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPool
        """
        if isinstance(http, dict):
            http = DestinationRuleSpecTrafficPolicyConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecTrafficPolicyConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttp"]:
        """HTTP connection pool settings.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPool#http
        """
        result = self._values.get("http")
        return result

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcp"]:
        """Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPool#tcp
        """
        result = self._values.get("tcp")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecTrafficPolicyConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        """HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"]:
        """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#h2UpgradePolicy
        """
        result = self._values.get("h2_upgrade_policy")
        return result

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#http1MaxPendingRequests
        """
        result = self._values.get("http1_max_pending_requests")
        return result

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests to a backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#http2MaxRequests
        """
        result = self._values.get("http2_max_requests")
        return result

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        """The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#idleTimeout
        """
        result = self._values.get("idle_timeout")
        return result

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#maxRequestsPerConnection
        """
        result = self._values.get("max_requests_per_connection")
        return result

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#maxRetries
        """
        result = self._values.get("max_retries")
        return result

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        """If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#useClientProtocol
        """
        result = self._values.get("use_client_protocol")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy(enum.Enum):
    """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy
    """

    DEFAULT = "DEFAULT"
    """DEFAULT."""
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    """DO_NOT_UPGRADE."""
    UPGRADE = "UPGRADE"
    """UPGRADE."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecTrafficPolicyConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        """Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp
        """
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        """TCP connection timeout.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp#connectTimeout
        """
        result = self._values.get("connect_timeout")
        return result

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        """Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp#maxConnections
        """
        result = self._values.get("max_connections")
        return result

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive"]:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp#tcpKeepalive
        """
        result = self._values.get("tcp_keepalive")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """The time duration between keep-alive probes.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive#probes
        """
        result = self._values.get("probes")
        return result

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive#time
        """
        result = self._values.get("time")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
    },
)
class DestinationRuleSpecTrafficPolicyLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerSimple"] = None,
    ) -> None:
        """Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer
        """
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#consistentHash
        """
        result = self._values.get("consistent_hash")
        return result

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#localityLbSetting
        """
        result = self._values.get("locality_lb_setting")
        return result

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerSimple"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#simple
        """
        result = self._values.get("simple")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash
        """
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie"]:
        """Hash based on HTTP cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#httpCookie
        """
        result = self._values.get("http_cookie")
        return result

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#httpHeaderName
        """
        result = self._values.get("http_header_name")
        return result

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#httpQueryParameterName
        """
        result = self._values.get("http_query_parameter_name")
        return result

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#minimumRingSize
        """
        result = self._values.get("minimum_ring_size")
        return result

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        """Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#useSourceIp
        """
        result = self._values.get("use_source_ip")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        """Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Name of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Path to set for the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie#path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        """Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie#ttl
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
    },
)
class DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover"]] = None,
    ) -> None:
        """
        :param distribute: Optional: only one of distribute or failover can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]]:
        """Optional: only one of distribute or failover can be set.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#distribute
        """
        result = self._values.get("distribute")
        return result

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        """enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#enabled
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover"]]:
        """Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#failover
        """
        result = self._values.get("failover")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        """
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating region.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyLoadBalancerSimple"
)
class DestinationRuleSpecTrafficPolicyLoadBalancerSimple(enum.Enum):
    """
    :schema: DestinationRuleSpecTrafficPolicyLoadBalancerSimple
    """

    ROUND_ROBIN = "ROUND_ROBIN"
    """ROUND_ROBIN."""
    LEAST_CONN = "LEAST_CONN"
    """LEAST_CONN."""
    RANDOM = "RANDOM"
    """RANDOM."""
    PASSTHROUGH = "PASSTHROUGH"
    """PASSTHROUGH."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5xx_errors": "consecutive5xxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
    },
)
class DestinationRuleSpecTrafficPolicyOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5xx_errors is not None:
            self._values["consecutive5xx_errors"] = consecutive5xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        """Minimum ejection duration.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#baseEjectionTime
        """
        result = self._values.get("base_ejection_time")
        return result

    @builtins.property
    def consecutive5xx_errors(self) -> typing.Optional[jsii.Number]:
        """Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutive5xxErrors
        """
        result = self._values.get("consecutive5xx_errors")
        return result

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutiveErrors
        """
        result = self._values.get("consecutive_errors")
        return result

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        """Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutiveGatewayErrors
        """
        result = self._values.get("consecutive_gateway_errors")
        return result

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#maxEjectionPercent
        """
        result = self._values.get("max_ejection_percent")
        return result

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#minHealthPercent
        """
        result = self._values.get("min_health_percent")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettings",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "tls": "tls",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettings:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection"] = None,
        port: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsPort"] = None,
        tls: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTls"] = None,
    ) -> None:
        """
        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port: 
        :param tls: TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings
        """
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection(**outlier_detection)
        if isinstance(port, dict):
            port = DestinationRuleSpecTrafficPolicyPortLevelSettingsPort(**port)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecTrafficPolicyPortLevelSettingsTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#connectionPool
        """
        result = self._values.get("connection_pool")
        return result

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer"]:
        """Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#loadBalancer
        """
        result = self._values.get("load_balancer")
        return result

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#outlierDetection
        """
        result = self._values.get("outlier_detection")
        return result

    @builtins.property
    def port(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsPort"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTls"]:
        """TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#tls
        """
        result = self._values.get("tls")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp"] = None,
    ) -> None:
        """
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool
        """
        if isinstance(http, dict):
            http = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp"]:
        """HTTP connection pool settings.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool#http
        """
        result = self._values.get("http")
        return result

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp"]:
        """Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool#tcp
        """
        result = self._values.get("tcp")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        """HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"]:
        """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#h2UpgradePolicy
        """
        result = self._values.get("h2_upgrade_policy")
        return result

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#http1MaxPendingRequests
        """
        result = self._values.get("http1_max_pending_requests")
        return result

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests to a backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#http2MaxRequests
        """
        result = self._values.get("http2_max_requests")
        return result

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        """The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#idleTimeout
        """
        result = self._values.get("idle_timeout")
        return result

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        """Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRequestsPerConnection
        """
        result = self._values.get("max_requests_per_connection")
        return result

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRetries
        """
        result = self._values.get("max_retries")
        return result

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        """If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#useClientProtocol
        """
        result = self._values.get("use_client_protocol")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy(
    enum.Enum,
):
    """Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy
    """

    DEFAULT = "DEFAULT"
    """DEFAULT."""
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    """DO_NOT_UPGRADE."""
    UPGRADE = "UPGRADE"
    """UPGRADE."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        """Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp
        """
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        """TCP connection timeout.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp#connectTimeout
        """
        result = self._values.get("connect_timeout")
        return result

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        """Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp#maxConnections
        """
        result = self._values.get("max_connections")
        return result

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"]:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp#tcpKeepalive
        """
        result = self._values.get("tcp_keepalive")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        """If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """The time duration between keep-alive probes.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#probes
        """
        result = self._values.get("probes")
        return result

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#time
        """
        result = self._values.get("time")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"] = None,
    ) -> None:
        """Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer
        """
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#consistentHash
        """
        result = self._values.get("consistent_hash")
        return result

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#localityLbSetting
        """
        result = self._values.get("locality_lb_setting")
        return result

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#simple
        """
        result = self._values.get("simple")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash
        """
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"]:
        """Hash based on HTTP cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpCookie
        """
        result = self._values.get("http_cookie")
        return result

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpHeaderName
        """
        result = self._values.get("http_header_name")
        return result

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        """Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpQueryParameterName
        """
        result = self._values.get("http_query_parameter_name")
        return result

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#minimumRingSize
        """
        result = self._values.get("minimum_ring_size")
        return result

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        """Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#useSourceIp
        """
        result = self._values.get("use_source_ip")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        """Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Name of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Path to set for the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#path
        """
        result = self._values.get("path")
        return result

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        """Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#ttl
        """
        result = self._values.get("ttl")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]] = None,
    ) -> None:
        """
        :param distribute: Optional: only one of distribute or failover can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]]:
        """Optional: only one of distribute or failover can be set.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#distribute
        """
        result = self._values.get("distribute")
        return result

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        """enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#enabled
        """
        result = self._values.get("enabled")
        return result

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]]:
        """Optional: only failover or distribute can be set.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#failover
        """
        result = self._values.get("failover")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        """
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        """Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        """Originating region.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#from
        """
        result = self._values.get("from_")
        return result

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#to
        """
        result = self._values.get("to")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple(enum.Enum):
    """
    :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple
    """

    ROUND_ROBIN = "ROUND_ROBIN"
    """ROUND_ROBIN."""
    LEAST_CONN = "LEAST_CONN"
    """LEAST_CONN."""
    RANDOM = "RANDOM"
    """RANDOM."""
    PASSTHROUGH = "PASSTHROUGH"
    """PASSTHROUGH."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5xx_errors": "consecutive5xxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5xx_errors is not None:
            self._values["consecutive5xx_errors"] = consecutive5xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        """Minimum ejection duration.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#baseEjectionTime
        """
        result = self._values.get("base_ejection_time")
        return result

    @builtins.property
    def consecutive5xx_errors(self) -> typing.Optional[jsii.Number]:
        """Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutive5xxErrors
        """
        result = self._values.get("consecutive5xx_errors")
        return result

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveErrors
        """
        result = self._values.get("consecutive_errors")
        return result

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        """Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveGatewayErrors
        """
        result = self._values.get("consecutive_gateway_errors")
        return result

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        """Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#interval
        """
        result = self._values.get("interval")
        return result

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#maxEjectionPercent
        """
        result = self._values.get("max_ejection_percent")
        return result

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#minHealthPercent
        """
        result = self._values.get("min_health_percent")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """
        :param number: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        mode: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#caCertificates
        """
        result = self._values.get("ca_certificates")
        return result

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#clientCertificate
        """
        result = self._values.get("client_certificate")
        return result

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#credentialName
        """
        result = self._values.get("credential_name")
        return result

    @builtins.property
    def mode(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#mode
        """
        result = self._values.get("mode")
        return result

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#privateKey
        """
        result = self._values.get("private_key")
        return result

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        """SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#sni
        """
        result = self._values.get("sni")
        return result

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#subjectAltNames
        """
        result = self._values.get("subject_alt_names")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode(enum.Enum):
    """
    :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode
    """

    DISABLE = "DISABLE"
    """DISABLE."""
    SIMPLE = "SIMPLE"
    """SIMPLE."""
    MUTUAL = "MUTUAL"
    """MUTUAL."""
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    """ISTIO_MUTUAL."""


@jsii.data_type(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecTrafficPolicyTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        mode: typing.Optional["DestinationRuleSpecTrafficPolicyTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.List[builtins.str]] = None,
    ) -> None:
        """TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecTrafficPolicyTls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyTls#caCertificates
        """
        result = self._values.get("ca_certificates")
        return result

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyTls#clientCertificate
        """
        result = self._values.get("client_certificate")
        return result

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        """
        :schema: DestinationRuleSpecTrafficPolicyTls#credentialName
        """
        result = self._values.get("credential_name")
        return result

    @builtins.property
    def mode(self) -> typing.Optional["DestinationRuleSpecTrafficPolicyTlsMode"]:
        """
        :schema: DestinationRuleSpecTrafficPolicyTls#mode
        """
        result = self._values.get("mode")
        return result

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        """REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyTls#privateKey
        """
        result = self._values.get("private_key")
        return result

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        """SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecTrafficPolicyTls#sni
        """
        result = self._values.get("sni")
        return result

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: DestinationRuleSpecTrafficPolicyTls#subjectAltNames
        """
        result = self._values.get("subject_alt_names")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="networkingistioiodestinationrule.DestinationRuleSpecTrafficPolicyTlsMode"
)
class DestinationRuleSpecTrafficPolicyTlsMode(enum.Enum):
    """
    :schema: DestinationRuleSpecTrafficPolicyTlsMode
    """

    DISABLE = "DISABLE"
    """DISABLE."""
    SIMPLE = "SIMPLE"
    """SIMPLE."""
    MUTUAL = "MUTUAL"
    """MUTUAL."""
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    """ISTIO_MUTUAL."""


__all__ = [
    "DestinationRule",
    "DestinationRuleOptions",
    "DestinationRuleSpec",
    "DestinationRuleSpecSubsets",
    "DestinationRuleSpecSubsetsTrafficPolicy",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPool",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple",
    "DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode",
    "DestinationRuleSpecSubsetsTrafficPolicyTls",
    "DestinationRuleSpecSubsetsTrafficPolicyTlsMode",
    "DestinationRuleSpecTrafficPolicy",
    "DestinationRuleSpecTrafficPolicyConnectionPool",
    "DestinationRuleSpecTrafficPolicyConnectionPoolHttp",
    "DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecTrafficPolicyConnectionPoolTcp",
    "DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecTrafficPolicyLoadBalancer",
    "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash",
    "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecTrafficPolicyLoadBalancerSimple",
    "DestinationRuleSpecTrafficPolicyOutlierDetection",
    "DestinationRuleSpecTrafficPolicyPortLevelSettings",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsPort",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsTls",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode",
    "DestinationRuleSpecTrafficPolicyTls",
    "DestinationRuleSpecTrafficPolicyTlsMode",
]

publication.publish()
