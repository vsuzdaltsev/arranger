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


class VirtualService(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="networkingistioiovirtualservice.VirtualService",
):
    """
    :schema: VirtualService
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        spec: typing.Optional["VirtualServiceSpec"] = None,
    ) -> None:
        """Defines a "VirtualService" API object.

        :param scope: the scope in which to define this object.
        :param name: a scope-local name for the object.
        :param spec: Configuration affecting label/content routing, sni routing, etc. See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html
        """
        options = VirtualServiceOptions(spec=spec)

        jsii.create(VirtualService, self, [scope, name, options])


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceOptions",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec"},
)
class VirtualServiceOptions:
    def __init__(self, *, spec: typing.Optional["VirtualServiceSpec"] = None) -> None:
        """
        :param spec: Configuration affecting label/content routing, sni routing, etc. See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html

        :schema: VirtualService
        """
        if isinstance(spec, dict):
            spec = VirtualServiceSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def spec(self) -> typing.Optional["VirtualServiceSpec"]:
        """Configuration affecting label/content routing, sni routing, etc.

        See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html

        :schema: VirtualService#spec
        """
        result = self._values.get("spec")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "export_to": "exportTo",
        "gateways": "gateways",
        "hosts": "hosts",
        "http": "http",
        "tcp": "tcp",
        "tls": "tls",
    },
)
class VirtualServiceSpec:
    def __init__(
        self,
        *,
        export_to: typing.Optional[typing.List[builtins.str]] = None,
        gateways: typing.Optional[typing.List[builtins.str]] = None,
        hosts: typing.Optional[typing.List[builtins.str]] = None,
        http: typing.Optional[typing.List["VirtualServiceSpecHttp"]] = None,
        tcp: typing.Optional[typing.List["VirtualServiceSpecTcp"]] = None,
        tls: typing.Optional[typing.List["VirtualServiceSpecTls"]] = None,
    ) -> None:
        """Configuration affecting label/content routing, sni routing, etc.

        See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html

        :param export_to: A list of namespaces to which this virtual service is exported.
        :param gateways: The names of gateways and sidecars that should apply these routes.
        :param hosts: The destination hosts to which traffic is being sent.
        :param http: An ordered list of route rules for HTTP traffic.
        :param tcp: An ordered list of route rules for opaque TCP traffic.
        :param tls: 

        :schema: VirtualServiceSpec
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if export_to is not None:
            self._values["export_to"] = export_to
        if gateways is not None:
            self._values["gateways"] = gateways
        if hosts is not None:
            self._values["hosts"] = hosts
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def export_to(self) -> typing.Optional[typing.List[builtins.str]]:
        """A list of namespaces to which this virtual service is exported.

        :schema: VirtualServiceSpec#exportTo
        """
        result = self._values.get("export_to")
        return result

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        """The names of gateways and sidecars that should apply these routes.

        :schema: VirtualServiceSpec#gateways
        """
        result = self._values.get("gateways")
        return result

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """The destination hosts to which traffic is being sent.

        :schema: VirtualServiceSpec#hosts
        """
        result = self._values.get("hosts")
        return result

    @builtins.property
    def http(self) -> typing.Optional[typing.List["VirtualServiceSpecHttp"]]:
        """An ordered list of route rules for HTTP traffic.

        :schema: VirtualServiceSpec#http
        """
        result = self._values.get("http")
        return result

    @builtins.property
    def tcp(self) -> typing.Optional[typing.List["VirtualServiceSpecTcp"]]:
        """An ordered list of route rules for opaque TCP traffic.

        :schema: VirtualServiceSpec#tcp
        """
        result = self._values.get("tcp")
        return result

    @builtins.property
    def tls(self) -> typing.Optional[typing.List["VirtualServiceSpecTls"]]:
        """
        :schema: VirtualServiceSpec#tls
        """
        result = self._values.get("tls")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttp",
    jsii_struct_bases=[],
    name_mapping={
        "cors_policy": "corsPolicy",
        "delegate": "delegate",
        "fault": "fault",
        "headers": "headers",
        "match": "match",
        "mirror": "mirror",
        "mirror_percent": "mirrorPercent",
        "mirror_percentage": "mirrorPercentage",
        "name": "name",
        "redirect": "redirect",
        "retries": "retries",
        "rewrite": "rewrite",
        "route": "route",
        "timeout": "timeout",
    },
)
class VirtualServiceSpecHttp:
    def __init__(
        self,
        *,
        cors_policy: typing.Optional["VirtualServiceSpecHttpCorsPolicy"] = None,
        delegate: typing.Optional["VirtualServiceSpecHttpDelegate"] = None,
        fault: typing.Optional["VirtualServiceSpecHttpFault"] = None,
        headers: typing.Optional["VirtualServiceSpecHttpHeaders"] = None,
        match: typing.Optional[typing.List["VirtualServiceSpecHttpMatch"]] = None,
        mirror: typing.Optional["VirtualServiceSpecHttpMirror"] = None,
        mirror_percent: typing.Optional[jsii.Number] = None,
        mirror_percentage: typing.Optional["VirtualServiceSpecHttpMirrorPercentage"] = None,
        name: typing.Optional[builtins.str] = None,
        redirect: typing.Optional["VirtualServiceSpecHttpRedirect"] = None,
        retries: typing.Optional["VirtualServiceSpecHttpRetries"] = None,
        rewrite: typing.Optional["VirtualServiceSpecHttpRewrite"] = None,
        route: typing.Optional[typing.List["VirtualServiceSpecHttpRoute"]] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param cors_policy: Cross-Origin Resource Sharing policy (CORS).
        :param delegate: 
        :param fault: Fault injection policy to apply on HTTP traffic at the client side.
        :param headers: 
        :param match: 
        :param mirror: 
        :param mirror_percent: Percentage of the traffic to be mirrored by the ``mirror`` field.
        :param mirror_percentage: Percentage of the traffic to be mirrored by the ``mirror`` field.
        :param name: The name assigned to the route for debugging purposes.
        :param redirect: A HTTP rule can either redirect or forward (default) traffic.
        :param retries: Retry policy for HTTP requests.
        :param rewrite: Rewrite HTTP URIs and Authority headers.
        :param route: A HTTP rule can either redirect or forward (default) traffic.
        :param timeout: Timeout for HTTP requests, default is disabled.

        :schema: VirtualServiceSpecHttp
        """
        if isinstance(cors_policy, dict):
            cors_policy = VirtualServiceSpecHttpCorsPolicy(**cors_policy)
        if isinstance(delegate, dict):
            delegate = VirtualServiceSpecHttpDelegate(**delegate)
        if isinstance(fault, dict):
            fault = VirtualServiceSpecHttpFault(**fault)
        if isinstance(headers, dict):
            headers = VirtualServiceSpecHttpHeaders(**headers)
        if isinstance(mirror, dict):
            mirror = VirtualServiceSpecHttpMirror(**mirror)
        if isinstance(mirror_percentage, dict):
            mirror_percentage = VirtualServiceSpecHttpMirrorPercentage(**mirror_percentage)
        if isinstance(redirect, dict):
            redirect = VirtualServiceSpecHttpRedirect(**redirect)
        if isinstance(retries, dict):
            retries = VirtualServiceSpecHttpRetries(**retries)
        if isinstance(rewrite, dict):
            rewrite = VirtualServiceSpecHttpRewrite(**rewrite)
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if delegate is not None:
            self._values["delegate"] = delegate
        if fault is not None:
            self._values["fault"] = fault
        if headers is not None:
            self._values["headers"] = headers
        if match is not None:
            self._values["match"] = match
        if mirror is not None:
            self._values["mirror"] = mirror
        if mirror_percent is not None:
            self._values["mirror_percent"] = mirror_percent
        if mirror_percentage is not None:
            self._values["mirror_percentage"] = mirror_percentage
        if name is not None:
            self._values["name"] = name
        if redirect is not None:
            self._values["redirect"] = redirect
        if retries is not None:
            self._values["retries"] = retries
        if rewrite is not None:
            self._values["rewrite"] = rewrite
        if route is not None:
            self._values["route"] = route
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def cors_policy(self) -> typing.Optional["VirtualServiceSpecHttpCorsPolicy"]:
        """Cross-Origin Resource Sharing policy (CORS).

        :schema: VirtualServiceSpecHttp#corsPolicy
        """
        result = self._values.get("cors_policy")
        return result

    @builtins.property
    def delegate(self) -> typing.Optional["VirtualServiceSpecHttpDelegate"]:
        """
        :schema: VirtualServiceSpecHttp#delegate
        """
        result = self._values.get("delegate")
        return result

    @builtins.property
    def fault(self) -> typing.Optional["VirtualServiceSpecHttpFault"]:
        """Fault injection policy to apply on HTTP traffic at the client side.

        :schema: VirtualServiceSpecHttp#fault
        """
        result = self._values.get("fault")
        return result

    @builtins.property
    def headers(self) -> typing.Optional["VirtualServiceSpecHttpHeaders"]:
        """
        :schema: VirtualServiceSpecHttp#headers
        """
        result = self._values.get("headers")
        return result

    @builtins.property
    def match(self) -> typing.Optional[typing.List["VirtualServiceSpecHttpMatch"]]:
        """
        :schema: VirtualServiceSpecHttp#match
        """
        result = self._values.get("match")
        return result

    @builtins.property
    def mirror(self) -> typing.Optional["VirtualServiceSpecHttpMirror"]:
        """
        :schema: VirtualServiceSpecHttp#mirror
        """
        result = self._values.get("mirror")
        return result

    @builtins.property
    def mirror_percent(self) -> typing.Optional[jsii.Number]:
        """Percentage of the traffic to be mirrored by the ``mirror`` field.

        :schema: VirtualServiceSpecHttp#mirrorPercent
        """
        result = self._values.get("mirror_percent")
        return result

    @builtins.property
    def mirror_percentage(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpMirrorPercentage"]:
        """Percentage of the traffic to be mirrored by the ``mirror`` field.

        :schema: VirtualServiceSpecHttp#mirrorPercentage
        """
        result = self._values.get("mirror_percentage")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """The name assigned to the route for debugging purposes.

        :schema: VirtualServiceSpecHttp#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def redirect(self) -> typing.Optional["VirtualServiceSpecHttpRedirect"]:
        """A HTTP rule can either redirect or forward (default) traffic.

        :schema: VirtualServiceSpecHttp#redirect
        """
        result = self._values.get("redirect")
        return result

    @builtins.property
    def retries(self) -> typing.Optional["VirtualServiceSpecHttpRetries"]:
        """Retry policy for HTTP requests.

        :schema: VirtualServiceSpecHttp#retries
        """
        result = self._values.get("retries")
        return result

    @builtins.property
    def rewrite(self) -> typing.Optional["VirtualServiceSpecHttpRewrite"]:
        """Rewrite HTTP URIs and Authority headers.

        :schema: VirtualServiceSpecHttp#rewrite
        """
        result = self._values.get("rewrite")
        return result

    @builtins.property
    def route(self) -> typing.Optional[typing.List["VirtualServiceSpecHttpRoute"]]:
        """A HTTP rule can either redirect or forward (default) traffic.

        :schema: VirtualServiceSpecHttp#route
        """
        result = self._values.get("route")
        return result

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        """Timeout for HTTP requests, default is disabled.

        :schema: VirtualServiceSpecHttp#timeout
        """
        result = self._values.get("timeout")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpCorsPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origin": "allowOrigin",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class VirtualServiceSpecHttpCorsPolicy:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[builtins.bool] = None,
        allow_headers: typing.Optional[typing.List[builtins.str]] = None,
        allow_methods: typing.Optional[typing.List[builtins.str]] = None,
        allow_origin: typing.Optional[typing.List[builtins.str]] = None,
        allow_origins: typing.Optional[typing.List["VirtualServiceSpecHttpCorsPolicyAllowOrigins"]] = None,
        expose_headers: typing.Optional[typing.List[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        """Cross-Origin Resource Sharing policy (CORS).

        :param allow_credentials: 
        :param allow_headers: 
        :param allow_methods: List of HTTP methods allowed to access the resource.
        :param allow_origin: The list of origins that are allowed to perform CORS requests.
        :param allow_origins: String patterns that match allowed origins.
        :param expose_headers: 
        :param max_age: 

        :schema: VirtualServiceSpecHttpCorsPolicy
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origin is not None:
            self._values["allow_origin"] = allow_origin
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(self) -> typing.Optional[builtins.bool]:
        """
        :schema: VirtualServiceSpecHttpCorsPolicy#allowCredentials
        """
        result = self._values.get("allow_credentials")
        return result

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpCorsPolicy#allowHeaders
        """
        result = self._values.get("allow_headers")
        return result

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        """List of HTTP methods allowed to access the resource.

        :schema: VirtualServiceSpecHttpCorsPolicy#allowMethods
        """
        result = self._values.get("allow_methods")
        return result

    @builtins.property
    def allow_origin(self) -> typing.Optional[typing.List[builtins.str]]:
        """The list of origins that are allowed to perform CORS requests.

        :schema: VirtualServiceSpecHttpCorsPolicy#allowOrigin
        """
        result = self._values.get("allow_origin")
        return result

    @builtins.property
    def allow_origins(
        self,
    ) -> typing.Optional[typing.List["VirtualServiceSpecHttpCorsPolicyAllowOrigins"]]:
        """String patterns that match allowed origins.

        :schema: VirtualServiceSpecHttpCorsPolicy#allowOrigins
        """
        result = self._values.get("allow_origins")
        return result

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpCorsPolicy#exposeHeaders
        """
        result = self._values.get("expose_headers")
        return result

    @builtins.property
    def max_age(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpCorsPolicy#maxAge
        """
        result = self._values.get("max_age")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpCorsPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpCorsPolicyAllowOrigins",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpCorsPolicyAllowOrigins:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpCorsPolicyAllowOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpDelegate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class VirtualServiceSpecHttpDelegate:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param name: Name specifies the name of the delegate VirtualService.
        :param namespace: Namespace specifies the namespace where the delegate VirtualService resides.

        :schema: VirtualServiceSpecHttpDelegate
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Name specifies the name of the delegate VirtualService.

        :schema: VirtualServiceSpecHttpDelegate#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        """Namespace specifies the namespace where the delegate VirtualService resides.

        :schema: VirtualServiceSpecHttpDelegate#namespace
        """
        result = self._values.get("namespace")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpDelegate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpFault",
    jsii_struct_bases=[],
    name_mapping={"abort": "abort", "delay": "delay"},
)
class VirtualServiceSpecHttpFault:
    def __init__(
        self,
        *,
        abort: typing.Optional["VirtualServiceSpecHttpFaultAbort"] = None,
        delay: typing.Optional["VirtualServiceSpecHttpFaultDelay"] = None,
    ) -> None:
        """Fault injection policy to apply on HTTP traffic at the client side.

        :param abort: 
        :param delay: 

        :schema: VirtualServiceSpecHttpFault
        """
        if isinstance(abort, dict):
            abort = VirtualServiceSpecHttpFaultAbort(**abort)
        if isinstance(delay, dict):
            delay = VirtualServiceSpecHttpFaultDelay(**delay)
        self._values: typing.Dict[str, typing.Any] = {}
        if abort is not None:
            self._values["abort"] = abort
        if delay is not None:
            self._values["delay"] = delay

    @builtins.property
    def abort(self) -> typing.Optional["VirtualServiceSpecHttpFaultAbort"]:
        """
        :schema: VirtualServiceSpecHttpFault#abort
        """
        result = self._values.get("abort")
        return result

    @builtins.property
    def delay(self) -> typing.Optional["VirtualServiceSpecHttpFaultDelay"]:
        """
        :schema: VirtualServiceSpecHttpFault#delay
        """
        result = self._values.get("delay")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpFaultAbort",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_status": "grpcStatus",
        "http2_error": "http2Error",
        "http_status": "httpStatus",
        "percentage": "percentage",
    },
)
class VirtualServiceSpecHttpFaultAbort:
    def __init__(
        self,
        *,
        grpc_status: typing.Optional[builtins.str] = None,
        http2_error: typing.Optional[builtins.str] = None,
        http_status: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional["VirtualServiceSpecHttpFaultAbortPercentage"] = None,
    ) -> None:
        """
        :param grpc_status: 
        :param http2_error: 
        :param http_status: HTTP status code to use to abort the Http request.
        :param percentage: Percentage of requests to be aborted with the error code provided.

        :schema: VirtualServiceSpecHttpFaultAbort
        """
        if isinstance(percentage, dict):
            percentage = VirtualServiceSpecHttpFaultAbortPercentage(**percentage)
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc_status is not None:
            self._values["grpc_status"] = grpc_status
        if http2_error is not None:
            self._values["http2_error"] = http2_error
        if http_status is not None:
            self._values["http_status"] = http_status
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def grpc_status(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpFaultAbort#grpcStatus
        """
        result = self._values.get("grpc_status")
        return result

    @builtins.property
    def http2_error(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpFaultAbort#http2Error
        """
        result = self._values.get("http2_error")
        return result

    @builtins.property
    def http_status(self) -> typing.Optional[jsii.Number]:
        """HTTP status code to use to abort the Http request.

        :schema: VirtualServiceSpecHttpFaultAbort#httpStatus
        """
        result = self._values.get("http_status")
        return result

    @builtins.property
    def percentage(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpFaultAbortPercentage"]:
        """Percentage of requests to be aborted with the error code provided.

        :schema: VirtualServiceSpecHttpFaultAbort#percentage
        """
        result = self._values.get("percentage")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultAbort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpFaultAbortPercentage",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class VirtualServiceSpecHttpFaultAbortPercentage:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        """Percentage of requests to be aborted with the error code provided.

        :param value: 

        :schema: VirtualServiceSpecHttpFaultAbortPercentage
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpFaultAbortPercentage#value
        """
        result = self._values.get("value")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultAbortPercentage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpFaultDelay",
    jsii_struct_bases=[],
    name_mapping={
        "exponential_delay": "exponentialDelay",
        "fixed_delay": "fixedDelay",
        "percent": "percent",
        "percentage": "percentage",
    },
)
class VirtualServiceSpecHttpFaultDelay:
    def __init__(
        self,
        *,
        exponential_delay: typing.Optional[builtins.str] = None,
        fixed_delay: typing.Optional[builtins.str] = None,
        percent: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional["VirtualServiceSpecHttpFaultDelayPercentage"] = None,
    ) -> None:
        """
        :param exponential_delay: 
        :param fixed_delay: Add a fixed delay before forwarding the request.
        :param percent: Percentage of requests on which the delay will be injected (0-100).
        :param percentage: Percentage of requests on which the delay will be injected.

        :schema: VirtualServiceSpecHttpFaultDelay
        """
        if isinstance(percentage, dict):
            percentage = VirtualServiceSpecHttpFaultDelayPercentage(**percentage)
        self._values: typing.Dict[str, typing.Any] = {}
        if exponential_delay is not None:
            self._values["exponential_delay"] = exponential_delay
        if fixed_delay is not None:
            self._values["fixed_delay"] = fixed_delay
        if percent is not None:
            self._values["percent"] = percent
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def exponential_delay(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpFaultDelay#exponentialDelay
        """
        result = self._values.get("exponential_delay")
        return result

    @builtins.property
    def fixed_delay(self) -> typing.Optional[builtins.str]:
        """Add a fixed delay before forwarding the request.

        :schema: VirtualServiceSpecHttpFaultDelay#fixedDelay
        """
        result = self._values.get("fixed_delay")
        return result

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        """Percentage of requests on which the delay will be injected (0-100).

        :schema: VirtualServiceSpecHttpFaultDelay#percent
        """
        result = self._values.get("percent")
        return result

    @builtins.property
    def percentage(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpFaultDelayPercentage"]:
        """Percentage of requests on which the delay will be injected.

        :schema: VirtualServiceSpecHttpFaultDelay#percentage
        """
        result = self._values.get("percentage")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpFaultDelayPercentage",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class VirtualServiceSpecHttpFaultDelayPercentage:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        """Percentage of requests on which the delay will be injected.

        :param value: 

        :schema: VirtualServiceSpecHttpFaultDelayPercentage
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpFaultDelayPercentage#value
        """
        result = self._values.get("value")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultDelayPercentage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpHeaders",
    jsii_struct_bases=[],
    name_mapping={"request": "request", "response": "response"},
)
class VirtualServiceSpecHttpHeaders:
    def __init__(
        self,
        *,
        request: typing.Optional["VirtualServiceSpecHttpHeadersRequest"] = None,
        response: typing.Optional["VirtualServiceSpecHttpHeadersResponse"] = None,
    ) -> None:
        """
        :param request: 
        :param response: 

        :schema: VirtualServiceSpecHttpHeaders
        """
        if isinstance(request, dict):
            request = VirtualServiceSpecHttpHeadersRequest(**request)
        if isinstance(response, dict):
            response = VirtualServiceSpecHttpHeadersResponse(**response)
        self._values: typing.Dict[str, typing.Any] = {}
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def request(self) -> typing.Optional["VirtualServiceSpecHttpHeadersRequest"]:
        """
        :schema: VirtualServiceSpecHttpHeaders#request
        """
        result = self._values.get("request")
        return result

    @builtins.property
    def response(self) -> typing.Optional["VirtualServiceSpecHttpHeadersResponse"]:
        """
        :schema: VirtualServiceSpecHttpHeaders#response
        """
        result = self._values.get("response")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpHeadersRequest",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpHeadersRequest:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.List[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpHeadersRequest
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpHeadersRequest#add
        """
        result = self._values.get("add")
        return result

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpHeadersRequest#remove
        """
        result = self._values.get("remove")
        return result

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpHeadersRequest#set
        """
        result = self._values.get("set")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpHeadersRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpHeadersResponse",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpHeadersResponse:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.List[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpHeadersResponse
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpHeadersResponse#add
        """
        result = self._values.get("add")
        return result

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpHeadersResponse#remove
        """
        result = self._values.get("remove")
        return result

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpHeadersResponse#set
        """
        result = self._values.get("set")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpHeadersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatch",
    jsii_struct_bases=[],
    name_mapping={
        "authority": "authority",
        "gateways": "gateways",
        "headers": "headers",
        "ignore_uri_case": "ignoreUriCase",
        "method": "method",
        "name": "name",
        "port": "port",
        "query_params": "queryParams",
        "scheme": "scheme",
        "source_labels": "sourceLabels",
        "source_namespace": "sourceNamespace",
        "uri": "uri",
        "without_headers": "withoutHeaders",
    },
)
class VirtualServiceSpecHttpMatch:
    def __init__(
        self,
        *,
        authority: typing.Optional["VirtualServiceSpecHttpMatchAuthority"] = None,
        gateways: typing.Optional[typing.List[builtins.str]] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchHeaders"]] = None,
        ignore_uri_case: typing.Optional[builtins.bool] = None,
        method: typing.Optional["VirtualServiceSpecHttpMatchMethod"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        query_params: typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchQueryParams"]] = None,
        scheme: typing.Optional["VirtualServiceSpecHttpMatchScheme"] = None,
        source_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_namespace: typing.Optional[builtins.str] = None,
        uri: typing.Optional["VirtualServiceSpecHttpMatchUri"] = None,
        without_headers: typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchWithoutHeaders"]] = None,
    ) -> None:
        """
        :param authority: 
        :param gateways: Names of gateways where the rule should be applied.
        :param headers: 
        :param ignore_uri_case: Flag to specify whether the URI matching should be case-insensitive.
        :param method: 
        :param name: The name assigned to a match.
        :param port: Specifies the ports on the host that is being addressed.
        :param query_params: Query parameters for matching.
        :param scheme: 
        :param source_labels: 
        :param source_namespace: Source namespace constraining the applicability of a rule to workloads in that namespace.
        :param uri: 
        :param without_headers: withoutHeader has the same syntax with the header, but has opposite meaning.

        :schema: VirtualServiceSpecHttpMatch
        """
        if isinstance(authority, dict):
            authority = VirtualServiceSpecHttpMatchAuthority(**authority)
        if isinstance(method, dict):
            method = VirtualServiceSpecHttpMatchMethod(**method)
        if isinstance(scheme, dict):
            scheme = VirtualServiceSpecHttpMatchScheme(**scheme)
        if isinstance(uri, dict):
            uri = VirtualServiceSpecHttpMatchUri(**uri)
        self._values: typing.Dict[str, typing.Any] = {}
        if authority is not None:
            self._values["authority"] = authority
        if gateways is not None:
            self._values["gateways"] = gateways
        if headers is not None:
            self._values["headers"] = headers
        if ignore_uri_case is not None:
            self._values["ignore_uri_case"] = ignore_uri_case
        if method is not None:
            self._values["method"] = method
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if query_params is not None:
            self._values["query_params"] = query_params
        if scheme is not None:
            self._values["scheme"] = scheme
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if source_namespace is not None:
            self._values["source_namespace"] = source_namespace
        if uri is not None:
            self._values["uri"] = uri
        if without_headers is not None:
            self._values["without_headers"] = without_headers

    @builtins.property
    def authority(self) -> typing.Optional["VirtualServiceSpecHttpMatchAuthority"]:
        """
        :schema: VirtualServiceSpecHttpMatch#authority
        """
        result = self._values.get("authority")
        return result

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        """Names of gateways where the rule should be applied.

        :schema: VirtualServiceSpecHttpMatch#gateways
        """
        result = self._values.get("gateways")
        return result

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchHeaders"]]:
        """
        :schema: VirtualServiceSpecHttpMatch#headers
        """
        result = self._values.get("headers")
        return result

    @builtins.property
    def ignore_uri_case(self) -> typing.Optional[builtins.bool]:
        """Flag to specify whether the URI matching should be case-insensitive.

        :schema: VirtualServiceSpecHttpMatch#ignoreUriCase
        """
        result = self._values.get("ignore_uri_case")
        return result

    @builtins.property
    def method(self) -> typing.Optional["VirtualServiceSpecHttpMatchMethod"]:
        """
        :schema: VirtualServiceSpecHttpMatch#method
        """
        result = self._values.get("method")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """The name assigned to a match.

        :schema: VirtualServiceSpecHttpMatch#name
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """Specifies the ports on the host that is being addressed.

        :schema: VirtualServiceSpecHttpMatch#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchQueryParams"]]:
        """Query parameters for matching.

        :schema: VirtualServiceSpecHttpMatch#queryParams
        """
        result = self._values.get("query_params")
        return result

    @builtins.property
    def scheme(self) -> typing.Optional["VirtualServiceSpecHttpMatchScheme"]:
        """
        :schema: VirtualServiceSpecHttpMatch#scheme
        """
        result = self._values.get("scheme")
        return result

    @builtins.property
    def source_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpMatch#sourceLabels
        """
        result = self._values.get("source_labels")
        return result

    @builtins.property
    def source_namespace(self) -> typing.Optional[builtins.str]:
        """Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecHttpMatch#sourceNamespace
        """
        result = self._values.get("source_namespace")
        return result

    @builtins.property
    def uri(self) -> typing.Optional["VirtualServiceSpecHttpMatchUri"]:
        """
        :schema: VirtualServiceSpecHttpMatch#uri
        """
        result = self._values.get("uri")
        return result

    @builtins.property
    def without_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchWithoutHeaders"]]:
        """withoutHeader has the same syntax with the header, but has opposite meaning.

        :schema: VirtualServiceSpecHttpMatch#withoutHeaders
        """
        result = self._values.get("without_headers")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchAuthority",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchAuthority:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchAuthority
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchAuthority#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchAuthority#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchAuthority#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchAuthority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchHeaders",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchHeaders:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchHeaders
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchHeaders#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchHeaders#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchHeaders#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchMethod",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchMethod:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchMethod
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchMethod#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchMethod#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchMethod#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchQueryParams",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchQueryParams:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchQueryParams
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchQueryParams#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchQueryParams#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchQueryParams#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchScheme",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchScheme:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchScheme
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchScheme#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchScheme#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchScheme#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchScheme(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchUri",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchUri:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchUri
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchUri#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchUri#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchUri#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchUri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMatchWithoutHeaders",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchWithoutHeaders:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchWithoutHeaders
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchWithoutHeaders#exact
        """
        result = self._values.get("exact")
        return result

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpMatchWithoutHeaders#prefix
        """
        result = self._values.get("prefix")
        return result

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        """RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchWithoutHeaders#regex
        """
        result = self._values.get("regex")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchWithoutHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMirror",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecHttpMirror:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecHttpMirrorPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecHttpMirror
        """
        if isinstance(port, dict):
            port = VirtualServiceSpecHttpMirrorPort(**port)
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

        :schema: VirtualServiceSpecHttpMirror#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecHttpMirrorPort"]:
        """Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecHttpMirror#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        """The name of a subset within the service.

        :schema: VirtualServiceSpecHttpMirror#subset
        """
        result = self._values.get("subset")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMirror(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMirrorPercentage",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class VirtualServiceSpecHttpMirrorPercentage:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        """Percentage of the traffic to be mirrored by the ``mirror`` field.

        :param value: 

        :schema: VirtualServiceSpecHttpMirrorPercentage
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpMirrorPercentage#value
        """
        result = self._values.get("value")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMirrorPercentage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpMirrorPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecHttpMirrorPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecHttpMirrorPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpMirrorPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMirrorPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "authority": "authority",
        "redirect_code": "redirectCode",
        "uri": "uri",
    },
)
class VirtualServiceSpecHttpRedirect:
    def __init__(
        self,
        *,
        authority: typing.Optional[builtins.str] = None,
        redirect_code: typing.Optional[jsii.Number] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        """A HTTP rule can either redirect or forward (default) traffic.

        :param authority: 
        :param redirect_code: 
        :param uri: 

        :schema: VirtualServiceSpecHttpRedirect
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if authority is not None:
            self._values["authority"] = authority
        if redirect_code is not None:
            self._values["redirect_code"] = redirect_code
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def authority(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpRedirect#authority
        """
        result = self._values.get("authority")
        return result

    @builtins.property
    def redirect_code(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpRedirect#redirectCode
        """
        result = self._values.get("redirect_code")
        return result

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpRedirect#uri
        """
        result = self._values.get("uri")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRetries",
    jsii_struct_bases=[],
    name_mapping={
        "attempts": "attempts",
        "per_try_timeout": "perTryTimeout",
        "retry_on": "retryOn",
        "retry_remote_localities": "retryRemoteLocalities",
    },
)
class VirtualServiceSpecHttpRetries:
    def __init__(
        self,
        *,
        attempts: typing.Optional[jsii.Number] = None,
        per_try_timeout: typing.Optional[builtins.str] = None,
        retry_on: typing.Optional[builtins.str] = None,
        retry_remote_localities: typing.Optional[builtins.bool] = None,
    ) -> None:
        """Retry policy for HTTP requests.

        :param attempts: Number of retries to be allowed for a given request.
        :param per_try_timeout: Timeout per retry attempt for a given request.
        :param retry_on: Specifies the conditions under which retry takes place.
        :param retry_remote_localities: Flag to specify whether the retries should retry to other localities.

        :schema: VirtualServiceSpecHttpRetries
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if attempts is not None:
            self._values["attempts"] = attempts
        if per_try_timeout is not None:
            self._values["per_try_timeout"] = per_try_timeout
        if retry_on is not None:
            self._values["retry_on"] = retry_on
        if retry_remote_localities is not None:
            self._values["retry_remote_localities"] = retry_remote_localities

    @builtins.property
    def attempts(self) -> typing.Optional[jsii.Number]:
        """Number of retries to be allowed for a given request.

        :schema: VirtualServiceSpecHttpRetries#attempts
        """
        result = self._values.get("attempts")
        return result

    @builtins.property
    def per_try_timeout(self) -> typing.Optional[builtins.str]:
        """Timeout per retry attempt for a given request.

        :schema: VirtualServiceSpecHttpRetries#perTryTimeout
        """
        result = self._values.get("per_try_timeout")
        return result

    @builtins.property
    def retry_on(self) -> typing.Optional[builtins.str]:
        """Specifies the conditions under which retry takes place.

        :schema: VirtualServiceSpecHttpRetries#retryOn
        """
        result = self._values.get("retry_on")
        return result

    @builtins.property
    def retry_remote_localities(self) -> typing.Optional[builtins.bool]:
        """Flag to specify whether the retries should retry to other localities.

        :schema: VirtualServiceSpecHttpRetries#retryRemoteLocalities
        """
        result = self._values.get("retry_remote_localities")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRetries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRewrite",
    jsii_struct_bases=[],
    name_mapping={"authority": "authority", "uri": "uri"},
)
class VirtualServiceSpecHttpRewrite:
    def __init__(
        self,
        *,
        authority: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        """Rewrite HTTP URIs and Authority headers.

        :param authority: rewrite the Authority/Host header with this value.
        :param uri: 

        :schema: VirtualServiceSpecHttpRewrite
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if authority is not None:
            self._values["authority"] = authority
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def authority(self) -> typing.Optional[builtins.str]:
        """rewrite the Authority/Host header with this value.

        :schema: VirtualServiceSpecHttpRewrite#authority
        """
        result = self._values.get("authority")
        return result

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        """
        :schema: VirtualServiceSpecHttpRewrite#uri
        """
        result = self._values.get("uri")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRoute",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "headers": "headers",
        "weight": "weight",
    },
)
class VirtualServiceSpecHttpRoute:
    def __init__(
        self,
        *,
        destination: typing.Optional["VirtualServiceSpecHttpRouteDestination"] = None,
        headers: typing.Optional["VirtualServiceSpecHttpRouteHeaders"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param destination: 
        :param headers: 
        :param weight: 

        :schema: VirtualServiceSpecHttpRoute
        """
        if isinstance(destination, dict):
            destination = VirtualServiceSpecHttpRouteDestination(**destination)
        if isinstance(headers, dict):
            headers = VirtualServiceSpecHttpRouteHeaders(**headers)
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if headers is not None:
            self._values["headers"] = headers
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def destination(self) -> typing.Optional["VirtualServiceSpecHttpRouteDestination"]:
        """
        :schema: VirtualServiceSpecHttpRoute#destination
        """
        result = self._values.get("destination")
        return result

    @builtins.property
    def headers(self) -> typing.Optional["VirtualServiceSpecHttpRouteHeaders"]:
        """
        :schema: VirtualServiceSpecHttpRoute#headers
        """
        result = self._values.get("headers")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpRoute#weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRouteDestination",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecHttpRouteDestination:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecHttpRouteDestinationPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecHttpRouteDestination
        """
        if isinstance(port, dict):
            port = VirtualServiceSpecHttpRouteDestinationPort(**port)
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

        :schema: VirtualServiceSpecHttpRouteDestination#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecHttpRouteDestinationPort"]:
        """Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecHttpRouteDestination#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        """The name of a subset within the service.

        :schema: VirtualServiceSpecHttpRouteDestination#subset
        """
        result = self._values.get("subset")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRouteDestinationPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecHttpRouteDestinationPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecHttpRouteDestinationPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecHttpRouteDestinationPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteDestinationPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRouteHeaders",
    jsii_struct_bases=[],
    name_mapping={"request": "request", "response": "response"},
)
class VirtualServiceSpecHttpRouteHeaders:
    def __init__(
        self,
        *,
        request: typing.Optional["VirtualServiceSpecHttpRouteHeadersRequest"] = None,
        response: typing.Optional["VirtualServiceSpecHttpRouteHeadersResponse"] = None,
    ) -> None:
        """
        :param request: 
        :param response: 

        :schema: VirtualServiceSpecHttpRouteHeaders
        """
        if isinstance(request, dict):
            request = VirtualServiceSpecHttpRouteHeadersRequest(**request)
        if isinstance(response, dict):
            response = VirtualServiceSpecHttpRouteHeadersResponse(**response)
        self._values: typing.Dict[str, typing.Any] = {}
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def request(self) -> typing.Optional["VirtualServiceSpecHttpRouteHeadersRequest"]:
        """
        :schema: VirtualServiceSpecHttpRouteHeaders#request
        """
        result = self._values.get("request")
        return result

    @builtins.property
    def response(self) -> typing.Optional["VirtualServiceSpecHttpRouteHeadersResponse"]:
        """
        :schema: VirtualServiceSpecHttpRouteHeaders#response
        """
        result = self._values.get("response")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRouteHeadersRequest",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpRouteHeadersRequest:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.List[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpRouteHeadersRequest
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpRouteHeadersRequest#add
        """
        result = self._values.get("add")
        return result

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpRouteHeadersRequest#remove
        """
        result = self._values.get("remove")
        return result

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpRouteHeadersRequest#set
        """
        result = self._values.get("set")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteHeadersRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecHttpRouteHeadersResponse",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpRouteHeadersResponse:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.List[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpRouteHeadersResponse
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpRouteHeadersResponse#add
        """
        result = self._values.get("add")
        return result

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpRouteHeadersResponse#remove
        """
        result = self._values.get("remove")
        return result

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecHttpRouteHeadersResponse#set
        """
        result = self._values.get("set")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteHeadersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTcp",
    jsii_struct_bases=[],
    name_mapping={"match": "match", "route": "route"},
)
class VirtualServiceSpecTcp:
    def __init__(
        self,
        *,
        match: typing.Optional[typing.List["VirtualServiceSpecTcpMatch"]] = None,
        route: typing.Optional[typing.List["VirtualServiceSpecTcpRoute"]] = None,
    ) -> None:
        """
        :param match: 
        :param route: The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTcp
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if match is not None:
            self._values["match"] = match
        if route is not None:
            self._values["route"] = route

    @builtins.property
    def match(self) -> typing.Optional[typing.List["VirtualServiceSpecTcpMatch"]]:
        """
        :schema: VirtualServiceSpecTcp#match
        """
        result = self._values.get("match")
        return result

    @builtins.property
    def route(self) -> typing.Optional[typing.List["VirtualServiceSpecTcpRoute"]]:
        """The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTcp#route
        """
        result = self._values.get("route")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTcpMatch",
    jsii_struct_bases=[],
    name_mapping={
        "destination_subnets": "destinationSubnets",
        "gateways": "gateways",
        "port": "port",
        "source_labels": "sourceLabels",
        "source_namespace": "sourceNamespace",
        "source_subnet": "sourceSubnet",
    },
)
class VirtualServiceSpecTcpMatch:
    def __init__(
        self,
        *,
        destination_subnets: typing.Optional[typing.List[builtins.str]] = None,
        gateways: typing.Optional[typing.List[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        source_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_namespace: typing.Optional[builtins.str] = None,
        source_subnet: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param destination_subnets: IPv4 or IPv6 ip addresses of destination with optional subnet.
        :param gateways: Names of gateways where the rule should be applied.
        :param port: Specifies the port on the host that is being addressed.
        :param source_labels: 
        :param source_namespace: Source namespace constraining the applicability of a rule to workloads in that namespace.
        :param source_subnet: IPv4 or IPv6 ip address of source with optional subnet.

        :schema: VirtualServiceSpecTcpMatch
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_subnets is not None:
            self._values["destination_subnets"] = destination_subnets
        if gateways is not None:
            self._values["gateways"] = gateways
        if port is not None:
            self._values["port"] = port
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if source_namespace is not None:
            self._values["source_namespace"] = source_namespace
        if source_subnet is not None:
            self._values["source_subnet"] = source_subnet

    @builtins.property
    def destination_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        """IPv4 or IPv6 ip addresses of destination with optional subnet.

        :schema: VirtualServiceSpecTcpMatch#destinationSubnets
        """
        result = self._values.get("destination_subnets")
        return result

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        """Names of gateways where the rule should be applied.

        :schema: VirtualServiceSpecTcpMatch#gateways
        """
        result = self._values.get("gateways")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTcpMatch#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def source_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecTcpMatch#sourceLabels
        """
        result = self._values.get("source_labels")
        return result

    @builtins.property
    def source_namespace(self) -> typing.Optional[builtins.str]:
        """Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecTcpMatch#sourceNamespace
        """
        result = self._values.get("source_namespace")
        return result

    @builtins.property
    def source_subnet(self) -> typing.Optional[builtins.str]:
        """IPv4 or IPv6 ip address of source with optional subnet.

        :schema: VirtualServiceSpecTcpMatch#sourceSubnet
        """
        result = self._values.get("source_subnet")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTcpRoute",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination", "weight": "weight"},
)
class VirtualServiceSpecTcpRoute:
    def __init__(
        self,
        *,
        destination: typing.Optional["VirtualServiceSpecTcpRouteDestination"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param destination: 
        :param weight: 

        :schema: VirtualServiceSpecTcpRoute
        """
        if isinstance(destination, dict):
            destination = VirtualServiceSpecTcpRouteDestination(**destination)
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def destination(self) -> typing.Optional["VirtualServiceSpecTcpRouteDestination"]:
        """
        :schema: VirtualServiceSpecTcpRoute#destination
        """
        result = self._values.get("destination")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecTcpRoute#weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTcpRouteDestination",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecTcpRouteDestination:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecTcpRouteDestinationPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecTcpRouteDestination
        """
        if isinstance(port, dict):
            port = VirtualServiceSpecTcpRouteDestinationPort(**port)
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

        :schema: VirtualServiceSpecTcpRouteDestination#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecTcpRouteDestinationPort"]:
        """Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTcpRouteDestination#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        """The name of a subset within the service.

        :schema: VirtualServiceSpecTcpRouteDestination#subset
        """
        result = self._values.get("subset")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpRouteDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTcpRouteDestinationPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecTcpRouteDestinationPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecTcpRouteDestinationPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecTcpRouteDestinationPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpRouteDestinationPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTls",
    jsii_struct_bases=[],
    name_mapping={"match": "match", "route": "route"},
)
class VirtualServiceSpecTls:
    def __init__(
        self,
        *,
        match: typing.Optional[typing.List["VirtualServiceSpecTlsMatch"]] = None,
        route: typing.Optional[typing.List["VirtualServiceSpecTlsRoute"]] = None,
    ) -> None:
        """
        :param match: 
        :param route: The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTls
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if match is not None:
            self._values["match"] = match
        if route is not None:
            self._values["route"] = route

    @builtins.property
    def match(self) -> typing.Optional[typing.List["VirtualServiceSpecTlsMatch"]]:
        """
        :schema: VirtualServiceSpecTls#match
        """
        result = self._values.get("match")
        return result

    @builtins.property
    def route(self) -> typing.Optional[typing.List["VirtualServiceSpecTlsRoute"]]:
        """The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTls#route
        """
        result = self._values.get("route")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTlsMatch",
    jsii_struct_bases=[],
    name_mapping={
        "destination_subnets": "destinationSubnets",
        "gateways": "gateways",
        "port": "port",
        "sni_hosts": "sniHosts",
        "source_labels": "sourceLabels",
        "source_namespace": "sourceNamespace",
    },
)
class VirtualServiceSpecTlsMatch:
    def __init__(
        self,
        *,
        destination_subnets: typing.Optional[typing.List[builtins.str]] = None,
        gateways: typing.Optional[typing.List[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        sni_hosts: typing.Optional[typing.List[builtins.str]] = None,
        source_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param destination_subnets: IPv4 or IPv6 ip addresses of destination with optional subnet.
        :param gateways: Names of gateways where the rule should be applied.
        :param port: Specifies the port on the host that is being addressed.
        :param sni_hosts: SNI (server name indicator) to match on.
        :param source_labels: 
        :param source_namespace: Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecTlsMatch
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_subnets is not None:
            self._values["destination_subnets"] = destination_subnets
        if gateways is not None:
            self._values["gateways"] = gateways
        if port is not None:
            self._values["port"] = port
        if sni_hosts is not None:
            self._values["sni_hosts"] = sni_hosts
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if source_namespace is not None:
            self._values["source_namespace"] = source_namespace

    @builtins.property
    def destination_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        """IPv4 or IPv6 ip addresses of destination with optional subnet.

        :schema: VirtualServiceSpecTlsMatch#destinationSubnets
        """
        result = self._values.get("destination_subnets")
        return result

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        """Names of gateways where the rule should be applied.

        :schema: VirtualServiceSpecTlsMatch#gateways
        """
        result = self._values.get("gateways")
        return result

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        """Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTlsMatch#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def sni_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        """SNI (server name indicator) to match on.

        :schema: VirtualServiceSpecTlsMatch#sniHosts
        """
        result = self._values.get("sni_hosts")
        return result

    @builtins.property
    def source_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """
        :schema: VirtualServiceSpecTlsMatch#sourceLabels
        """
        result = self._values.get("source_labels")
        return result

    @builtins.property
    def source_namespace(self) -> typing.Optional[builtins.str]:
        """Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecTlsMatch#sourceNamespace
        """
        result = self._values.get("source_namespace")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTlsRoute",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination", "weight": "weight"},
)
class VirtualServiceSpecTlsRoute:
    def __init__(
        self,
        *,
        destination: typing.Optional["VirtualServiceSpecTlsRouteDestination"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param destination: 
        :param weight: 

        :schema: VirtualServiceSpecTlsRoute
        """
        if isinstance(destination, dict):
            destination = VirtualServiceSpecTlsRouteDestination(**destination)
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def destination(self) -> typing.Optional["VirtualServiceSpecTlsRouteDestination"]:
        """
        :schema: VirtualServiceSpecTlsRoute#destination
        """
        result = self._values.get("destination")
        return result

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecTlsRoute#weight
        """
        result = self._values.get("weight")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTlsRouteDestination",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecTlsRouteDestination:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecTlsRouteDestinationPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecTlsRouteDestination
        """
        if isinstance(port, dict):
            port = VirtualServiceSpecTlsRouteDestinationPort(**port)
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

        :schema: VirtualServiceSpecTlsRouteDestination#host
        """
        result = self._values.get("host")
        return result

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecTlsRouteDestinationPort"]:
        """Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTlsRouteDestination#port
        """
        result = self._values.get("port")
        return result

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        """The name of a subset within the service.

        :schema: VirtualServiceSpecTlsRouteDestination#subset
        """
        result = self._values.get("subset")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsRouteDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="networkingistioiovirtualservice.VirtualServiceSpecTlsRouteDestinationPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecTlsRouteDestinationPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        """Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecTlsRouteDestinationPort
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        """
        :schema: VirtualServiceSpecTlsRouteDestinationPort#number
        """
        result = self._values.get("number")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsRouteDestinationPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VirtualService",
    "VirtualServiceOptions",
    "VirtualServiceSpec",
    "VirtualServiceSpecHttp",
    "VirtualServiceSpecHttpCorsPolicy",
    "VirtualServiceSpecHttpCorsPolicyAllowOrigins",
    "VirtualServiceSpecHttpDelegate",
    "VirtualServiceSpecHttpFault",
    "VirtualServiceSpecHttpFaultAbort",
    "VirtualServiceSpecHttpFaultAbortPercentage",
    "VirtualServiceSpecHttpFaultDelay",
    "VirtualServiceSpecHttpFaultDelayPercentage",
    "VirtualServiceSpecHttpHeaders",
    "VirtualServiceSpecHttpHeadersRequest",
    "VirtualServiceSpecHttpHeadersResponse",
    "VirtualServiceSpecHttpMatch",
    "VirtualServiceSpecHttpMatchAuthority",
    "VirtualServiceSpecHttpMatchHeaders",
    "VirtualServiceSpecHttpMatchMethod",
    "VirtualServiceSpecHttpMatchQueryParams",
    "VirtualServiceSpecHttpMatchScheme",
    "VirtualServiceSpecHttpMatchUri",
    "VirtualServiceSpecHttpMatchWithoutHeaders",
    "VirtualServiceSpecHttpMirror",
    "VirtualServiceSpecHttpMirrorPercentage",
    "VirtualServiceSpecHttpMirrorPort",
    "VirtualServiceSpecHttpRedirect",
    "VirtualServiceSpecHttpRetries",
    "VirtualServiceSpecHttpRewrite",
    "VirtualServiceSpecHttpRoute",
    "VirtualServiceSpecHttpRouteDestination",
    "VirtualServiceSpecHttpRouteDestinationPort",
    "VirtualServiceSpecHttpRouteHeaders",
    "VirtualServiceSpecHttpRouteHeadersRequest",
    "VirtualServiceSpecHttpRouteHeadersResponse",
    "VirtualServiceSpecTcp",
    "VirtualServiceSpecTcpMatch",
    "VirtualServiceSpecTcpRoute",
    "VirtualServiceSpecTcpRouteDestination",
    "VirtualServiceSpecTcpRouteDestinationPort",
    "VirtualServiceSpecTls",
    "VirtualServiceSpecTlsMatch",
    "VirtualServiceSpecTlsRoute",
    "VirtualServiceSpecTlsRouteDestination",
    "VirtualServiceSpecTlsRouteDestinationPort",
]

publication.publish()
