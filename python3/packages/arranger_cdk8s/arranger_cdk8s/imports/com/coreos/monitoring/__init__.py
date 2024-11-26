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


class ServiceMonitor(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="comcoreosmonitoring.ServiceMonitor",
):
    '''ServiceMonitor defines monitoring for a set of services.

    :schema: ServiceMonitor
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        spec: typing.Union["ServiceMonitorSpec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a "ServiceMonitor" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param spec: Specification of desired Service selection for target discovery by Prometheus.
        :param metadata: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae743b5825b3e6075ede1500d52f893c3c6a63be14f647f9a44d0e722d356470)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServiceMonitorProps(spec=spec, metadata=metadata)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        spec: typing.Union["ServiceMonitorSpec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "ServiceMonitor".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param spec: Specification of desired Service selection for target discovery by Prometheus.
        :param metadata: 
        '''
        props = ServiceMonitorProps(spec=spec, metadata=metadata)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "ServiceMonitor".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorProps",
    jsii_struct_bases=[],
    name_mapping={"spec": "spec", "metadata": "metadata"},
)
class ServiceMonitorProps:
    def __init__(
        self,
        *,
        spec: typing.Union["ServiceMonitorSpec", typing.Dict[builtins.str, typing.Any]],
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''ServiceMonitor defines monitoring for a set of services.

        :param spec: Specification of desired Service selection for target discovery by Prometheus.
        :param metadata: 

        :schema: ServiceMonitor
        '''
        if isinstance(spec, dict):
            spec = ServiceMonitorSpec(**spec)
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56bca6778cf6036cd0140b25f1a1429742323914ee819ae9276e47c0e290aaf5)
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "spec": spec,
        }
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def spec(self) -> "ServiceMonitorSpec":
        '''Specification of desired Service selection for target discovery by Prometheus.

        :schema: ServiceMonitor#spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("ServiceMonitorSpec", result)

    @builtins.property
    def metadata(self) -> typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata]:
        '''
        :schema: ServiceMonitor#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpec",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints": "endpoints",
        "selector": "selector",
        "attach_metadata": "attachMetadata",
        "job_label": "jobLabel",
        "label_limit": "labelLimit",
        "label_name_length_limit": "labelNameLengthLimit",
        "label_value_length_limit": "labelValueLengthLimit",
        "namespace_selector": "namespaceSelector",
        "pod_target_labels": "podTargetLabels",
        "sample_limit": "sampleLimit",
        "target_labels": "targetLabels",
        "target_limit": "targetLimit",
    },
)
class ServiceMonitorSpec:
    def __init__(
        self,
        *,
        endpoints: typing.Sequence[typing.Union["ServiceMonitorSpecEndpoints", typing.Dict[builtins.str, typing.Any]]],
        selector: typing.Union["ServiceMonitorSpecSelector", typing.Dict[builtins.str, typing.Any]],
        attach_metadata: typing.Optional[typing.Union["ServiceMonitorSpecAttachMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        job_label: typing.Optional[builtins.str] = None,
        label_limit: typing.Optional[jsii.Number] = None,
        label_name_length_limit: typing.Optional[jsii.Number] = None,
        label_value_length_limit: typing.Optional[jsii.Number] = None,
        namespace_selector: typing.Optional[typing.Union["ServiceMonitorSpecNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_target_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_limit: typing.Optional[jsii.Number] = None,
        target_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Specification of desired Service selection for target discovery by Prometheus.

        :param endpoints: A list of endpoints allowed as part of this ServiceMonitor.
        :param selector: Selector to select Endpoints objects.
        :param attach_metadata: Attaches node metadata to discovered targets. Requires Prometheus v2.37.0 and above.
        :param job_label: JobLabel selects the label from the associated Kubernetes service which will be used as the ``job`` label for all metrics. For example: If in ``ServiceMonitor.spec.jobLabel: foo`` and in ``Service.metadata.labels.foo: bar``, then the ``job="bar"`` label is added to all metrics. If the value of this field is empty or if the label doesn't exist for the given Service, the ``job`` label of the metrics defaults to the name of the Kubernetes Service.
        :param label_limit: Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.
        :param label_name_length_limit: Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.
        :param label_value_length_limit: Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.
        :param namespace_selector: Selector to select which namespaces the Kubernetes Endpoints objects are discovered from.
        :param pod_target_labels: PodTargetLabels transfers labels on the Kubernetes ``Pod`` onto the created metrics.
        :param sample_limit: SampleLimit defines per-scrape limit on number of scraped samples that will be accepted.
        :param target_labels: TargetLabels transfers labels from the Kubernetes ``Service`` onto the created metrics.
        :param target_limit: TargetLimit defines a limit on the number of scraped targets that will be accepted.

        :schema: ServiceMonitorSpec
        '''
        if isinstance(selector, dict):
            selector = ServiceMonitorSpecSelector(**selector)
        if isinstance(attach_metadata, dict):
            attach_metadata = ServiceMonitorSpecAttachMetadata(**attach_metadata)
        if isinstance(namespace_selector, dict):
            namespace_selector = ServiceMonitorSpecNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77dad9e9e97980d2d9001de098d81faeb424d5144d09285dc28512f29a3815ba)
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument attach_metadata", value=attach_metadata, expected_type=type_hints["attach_metadata"])
            check_type(argname="argument job_label", value=job_label, expected_type=type_hints["job_label"])
            check_type(argname="argument label_limit", value=label_limit, expected_type=type_hints["label_limit"])
            check_type(argname="argument label_name_length_limit", value=label_name_length_limit, expected_type=type_hints["label_name_length_limit"])
            check_type(argname="argument label_value_length_limit", value=label_value_length_limit, expected_type=type_hints["label_value_length_limit"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument pod_target_labels", value=pod_target_labels, expected_type=type_hints["pod_target_labels"])
            check_type(argname="argument sample_limit", value=sample_limit, expected_type=type_hints["sample_limit"])
            check_type(argname="argument target_labels", value=target_labels, expected_type=type_hints["target_labels"])
            check_type(argname="argument target_limit", value=target_limit, expected_type=type_hints["target_limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoints": endpoints,
            "selector": selector,
        }
        if attach_metadata is not None:
            self._values["attach_metadata"] = attach_metadata
        if job_label is not None:
            self._values["job_label"] = job_label
        if label_limit is not None:
            self._values["label_limit"] = label_limit
        if label_name_length_limit is not None:
            self._values["label_name_length_limit"] = label_name_length_limit
        if label_value_length_limit is not None:
            self._values["label_value_length_limit"] = label_value_length_limit
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if pod_target_labels is not None:
            self._values["pod_target_labels"] = pod_target_labels
        if sample_limit is not None:
            self._values["sample_limit"] = sample_limit
        if target_labels is not None:
            self._values["target_labels"] = target_labels
        if target_limit is not None:
            self._values["target_limit"] = target_limit

    @builtins.property
    def endpoints(self) -> typing.List["ServiceMonitorSpecEndpoints"]:
        '''A list of endpoints allowed as part of this ServiceMonitor.

        :schema: ServiceMonitorSpec#endpoints
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(typing.List["ServiceMonitorSpecEndpoints"], result)

    @builtins.property
    def selector(self) -> "ServiceMonitorSpecSelector":
        '''Selector to select Endpoints objects.

        :schema: ServiceMonitorSpec#selector
        '''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast("ServiceMonitorSpecSelector", result)

    @builtins.property
    def attach_metadata(self) -> typing.Optional["ServiceMonitorSpecAttachMetadata"]:
        '''Attaches node metadata to discovered targets.

        Requires Prometheus v2.37.0 and above.

        :schema: ServiceMonitorSpec#attachMetadata
        '''
        result = self._values.get("attach_metadata")
        return typing.cast(typing.Optional["ServiceMonitorSpecAttachMetadata"], result)

    @builtins.property
    def job_label(self) -> typing.Optional[builtins.str]:
        '''JobLabel selects the label from the associated Kubernetes service which will be used as the ``job`` label for all metrics.

        For example: If in ``ServiceMonitor.spec.jobLabel: foo`` and in ``Service.metadata.labels.foo: bar``, then the ``job="bar"`` label is added to all metrics.
        If the value of this field is empty or if the label doesn't exist for the given Service, the ``job`` label of the metrics defaults to the name of the Kubernetes Service.

        :schema: ServiceMonitorSpec#jobLabel
        '''
        result = self._values.get("job_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_limit(self) -> typing.Optional[jsii.Number]:
        '''Per-scrape limit on number of labels that will be accepted for a sample.

        Only valid in Prometheus versions 2.27.0 and newer.

        :schema: ServiceMonitorSpec#labelLimit
        '''
        result = self._values.get("label_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def label_name_length_limit(self) -> typing.Optional[jsii.Number]:
        '''Per-scrape limit on length of labels name that will be accepted for a sample.

        Only valid in Prometheus versions 2.27.0 and newer.

        :schema: ServiceMonitorSpec#labelNameLengthLimit
        '''
        result = self._values.get("label_name_length_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def label_value_length_limit(self) -> typing.Optional[jsii.Number]:
        '''Per-scrape limit on length of labels value that will be accepted for a sample.

        Only valid in Prometheus versions 2.27.0 and newer.

        :schema: ServiceMonitorSpec#labelValueLengthLimit
        '''
        result = self._values.get("label_value_length_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ServiceMonitorSpecNamespaceSelector"]:
        '''Selector to select which namespaces the Kubernetes Endpoints objects are discovered from.

        :schema: ServiceMonitorSpec#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ServiceMonitorSpecNamespaceSelector"], result)

    @builtins.property
    def pod_target_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''PodTargetLabels transfers labels on the Kubernetes ``Pod`` onto the created metrics.

        :schema: ServiceMonitorSpec#podTargetLabels
        '''
        result = self._values.get("pod_target_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sample_limit(self) -> typing.Optional[jsii.Number]:
        '''SampleLimit defines per-scrape limit on number of scraped samples that will be accepted.

        :schema: ServiceMonitorSpec#sampleLimit
        '''
        result = self._values.get("sample_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''TargetLabels transfers labels from the Kubernetes ``Service`` onto the created metrics.

        :schema: ServiceMonitorSpec#targetLabels
        '''
        result = self._values.get("target_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_limit(self) -> typing.Optional[jsii.Number]:
        '''TargetLimit defines a limit on the number of scraped targets that will be accepted.

        :schema: ServiceMonitorSpec#targetLimit
        '''
        result = self._values.get("target_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecAttachMetadata",
    jsii_struct_bases=[],
    name_mapping={"node": "node"},
)
class ServiceMonitorSpecAttachMetadata:
    def __init__(self, *, node: typing.Optional[builtins.bool] = None) -> None:
        '''Attaches node metadata to discovered targets.

        Requires Prometheus v2.37.0 and above.

        :param node: When set to true, Prometheus must have permissions to get Nodes.

        :schema: ServiceMonitorSpecAttachMetadata
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bbe935572488af708dc3190e619dcc20410fc1feb14d189191dcc70c240bc2a)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if node is not None:
            self._values["node"] = node

    @builtins.property
    def node(self) -> typing.Optional[builtins.bool]:
        '''When set to true, Prometheus must have permissions to get Nodes.

        :schema: ServiceMonitorSpecAttachMetadata#node
        '''
        result = self._values.get("node")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecAttachMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpoints",
    jsii_struct_bases=[],
    name_mapping={
        "authorization": "authorization",
        "basic_auth": "basicAuth",
        "bearer_token_file": "bearerTokenFile",
        "bearer_token_secret": "bearerTokenSecret",
        "enable_http2": "enableHttp2",
        "filter_running": "filterRunning",
        "follow_redirects": "followRedirects",
        "honor_labels": "honorLabels",
        "honor_timestamps": "honorTimestamps",
        "interval": "interval",
        "metric_relabelings": "metricRelabelings",
        "oauth2": "oauth2",
        "params": "params",
        "path": "path",
        "port": "port",
        "proxy_url": "proxyUrl",
        "relabelings": "relabelings",
        "scheme": "scheme",
        "scrape_timeout": "scrapeTimeout",
        "target_port": "targetPort",
        "tls_config": "tlsConfig",
    },
)
class ServiceMonitorSpecEndpoints:
    def __init__(
        self,
        *,
        authorization: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsAuthorization", typing.Dict[builtins.str, typing.Any]]] = None,
        basic_auth: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
        bearer_token_file: typing.Optional[builtins.str] = None,
        bearer_token_secret: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsBearerTokenSecret", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_http2: typing.Optional[builtins.bool] = None,
        filter_running: typing.Optional[builtins.bool] = None,
        follow_redirects: typing.Optional[builtins.bool] = None,
        honor_labels: typing.Optional[builtins.bool] = None,
        honor_timestamps: typing.Optional[builtins.bool] = None,
        interval: typing.Optional[builtins.str] = None,
        metric_relabelings: typing.Optional[typing.Sequence[typing.Union["ServiceMonitorSpecEndpointsMetricRelabelings", typing.Dict[builtins.str, typing.Any]]]] = None,
        oauth2: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsOauth2", typing.Dict[builtins.str, typing.Any]]] = None,
        params: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        relabelings: typing.Optional[typing.Sequence[typing.Union["ServiceMonitorSpecEndpointsRelabelings", typing.Dict[builtins.str, typing.Any]]]] = None,
        scheme: typing.Optional[builtins.str] = None,
        scrape_timeout: typing.Optional[builtins.str] = None,
        target_port: typing.Optional["ServiceMonitorSpecEndpointsTargetPort"] = None,
        tls_config: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Endpoint defines a scrapeable endpoint serving Prometheus metrics.

        :param authorization: Authorization section for this endpoint.
        :param basic_auth: BasicAuth allow an endpoint to authenticate over basic authentication More info: https://prometheus.io/docs/operating/configuration/#endpoints.
        :param bearer_token_file: File to read bearer token for scraping targets.
        :param bearer_token_secret: Secret to mount to read bearer token for scraping targets. The secret needs to be in the same namespace as the service monitor and accessible by the Prometheus Operator.
        :param enable_http2: Whether to enable HTTP2.
        :param filter_running: Drop pods that are not running. (Failed, Succeeded). Enabled by default. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase
        :param follow_redirects: FollowRedirects configures whether scrape requests follow HTTP 3xx redirects.
        :param honor_labels: HonorLabels chooses the metric's labels on collisions with target labels.
        :param honor_timestamps: HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data.
        :param interval: Interval at which metrics should be scraped If not specified Prometheus' global scrape interval is used.
        :param metric_relabelings: MetricRelabelConfigs to apply to samples before ingestion.
        :param oauth2: OAuth2 for the URL. Only valid in Prometheus versions 2.27.0 and newer.
        :param params: Optional HTTP URL parameters.
        :param path: HTTP path to scrape for metrics. If empty, Prometheus uses the default value (e.g. ``/metrics``).
        :param port: Name of the service port this endpoint refers to. Mutually exclusive with targetPort.
        :param proxy_url: ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint.
        :param relabelings: RelabelConfigs to apply to samples before scraping. Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields. The original scrape job's name is available via the ``__tmp_prometheus_job_name`` label. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config
        :param scheme: HTTP scheme to use for scraping.
        :param scrape_timeout: Timeout after which the scrape is ended If not specified, the Prometheus global scrape timeout is used unless it is less than ``Interval`` in which the latter is used.
        :param target_port: Name or number of the target port of the Pod behind the Service, the port must be specified with container port property. Mutually exclusive with port.
        :param tls_config: TLS configuration to use when scraping the endpoint.

        :schema: ServiceMonitorSpecEndpoints
        '''
        if isinstance(authorization, dict):
            authorization = ServiceMonitorSpecEndpointsAuthorization(**authorization)
        if isinstance(basic_auth, dict):
            basic_auth = ServiceMonitorSpecEndpointsBasicAuth(**basic_auth)
        if isinstance(bearer_token_secret, dict):
            bearer_token_secret = ServiceMonitorSpecEndpointsBearerTokenSecret(**bearer_token_secret)
        if isinstance(oauth2, dict):
            oauth2 = ServiceMonitorSpecEndpointsOauth2(**oauth2)
        if isinstance(tls_config, dict):
            tls_config = ServiceMonitorSpecEndpointsTlsConfig(**tls_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0387a341502661c257fa633a8de56a63d951087fafafcbad7e1c75709428ef9f)
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
            check_type(argname="argument bearer_token_file", value=bearer_token_file, expected_type=type_hints["bearer_token_file"])
            check_type(argname="argument bearer_token_secret", value=bearer_token_secret, expected_type=type_hints["bearer_token_secret"])
            check_type(argname="argument enable_http2", value=enable_http2, expected_type=type_hints["enable_http2"])
            check_type(argname="argument filter_running", value=filter_running, expected_type=type_hints["filter_running"])
            check_type(argname="argument follow_redirects", value=follow_redirects, expected_type=type_hints["follow_redirects"])
            check_type(argname="argument honor_labels", value=honor_labels, expected_type=type_hints["honor_labels"])
            check_type(argname="argument honor_timestamps", value=honor_timestamps, expected_type=type_hints["honor_timestamps"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument metric_relabelings", value=metric_relabelings, expected_type=type_hints["metric_relabelings"])
            check_type(argname="argument oauth2", value=oauth2, expected_type=type_hints["oauth2"])
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument proxy_url", value=proxy_url, expected_type=type_hints["proxy_url"])
            check_type(argname="argument relabelings", value=relabelings, expected_type=type_hints["relabelings"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument scrape_timeout", value=scrape_timeout, expected_type=type_hints["scrape_timeout"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorization is not None:
            self._values["authorization"] = authorization
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth
        if bearer_token_file is not None:
            self._values["bearer_token_file"] = bearer_token_file
        if bearer_token_secret is not None:
            self._values["bearer_token_secret"] = bearer_token_secret
        if enable_http2 is not None:
            self._values["enable_http2"] = enable_http2
        if filter_running is not None:
            self._values["filter_running"] = filter_running
        if follow_redirects is not None:
            self._values["follow_redirects"] = follow_redirects
        if honor_labels is not None:
            self._values["honor_labels"] = honor_labels
        if honor_timestamps is not None:
            self._values["honor_timestamps"] = honor_timestamps
        if interval is not None:
            self._values["interval"] = interval
        if metric_relabelings is not None:
            self._values["metric_relabelings"] = metric_relabelings
        if oauth2 is not None:
            self._values["oauth2"] = oauth2
        if params is not None:
            self._values["params"] = params
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if proxy_url is not None:
            self._values["proxy_url"] = proxy_url
        if relabelings is not None:
            self._values["relabelings"] = relabelings
        if scheme is not None:
            self._values["scheme"] = scheme
        if scrape_timeout is not None:
            self._values["scrape_timeout"] = scrape_timeout
        if target_port is not None:
            self._values["target_port"] = target_port
        if tls_config is not None:
            self._values["tls_config"] = tls_config

    @builtins.property
    def authorization(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsAuthorization"]:
        '''Authorization section for this endpoint.

        :schema: ServiceMonitorSpecEndpoints#authorization
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsAuthorization"], result)

    @builtins.property
    def basic_auth(self) -> typing.Optional["ServiceMonitorSpecEndpointsBasicAuth"]:
        '''BasicAuth allow an endpoint to authenticate over basic authentication More info: https://prometheus.io/docs/operating/configuration/#endpoints.

        :schema: ServiceMonitorSpecEndpoints#basicAuth
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsBasicAuth"], result)

    @builtins.property
    def bearer_token_file(self) -> typing.Optional[builtins.str]:
        '''File to read bearer token for scraping targets.

        :schema: ServiceMonitorSpecEndpoints#bearerTokenFile
        '''
        result = self._values.get("bearer_token_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bearer_token_secret(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsBearerTokenSecret"]:
        '''Secret to mount to read bearer token for scraping targets.

        The secret needs to be in the same namespace as the service monitor and accessible by the Prometheus Operator.

        :schema: ServiceMonitorSpecEndpoints#bearerTokenSecret
        '''
        result = self._values.get("bearer_token_secret")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsBearerTokenSecret"], result)

    @builtins.property
    def enable_http2(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable HTTP2.

        :schema: ServiceMonitorSpecEndpoints#enableHttp2
        '''
        result = self._values.get("enable_http2")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def filter_running(self) -> typing.Optional[builtins.bool]:
        '''Drop pods that are not running.

        (Failed, Succeeded). Enabled by default. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase

        :schema: ServiceMonitorSpecEndpoints#filterRunning
        '''
        result = self._values.get("filter_running")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def follow_redirects(self) -> typing.Optional[builtins.bool]:
        '''FollowRedirects configures whether scrape requests follow HTTP 3xx redirects.

        :schema: ServiceMonitorSpecEndpoints#followRedirects
        '''
        result = self._values.get("follow_redirects")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def honor_labels(self) -> typing.Optional[builtins.bool]:
        '''HonorLabels chooses the metric's labels on collisions with target labels.

        :schema: ServiceMonitorSpecEndpoints#honorLabels
        '''
        result = self._values.get("honor_labels")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def honor_timestamps(self) -> typing.Optional[builtins.bool]:
        '''HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data.

        :schema: ServiceMonitorSpecEndpoints#honorTimestamps
        '''
        result = self._values.get("honor_timestamps")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Interval at which metrics should be scraped If not specified Prometheus' global scrape interval is used.

        :schema: ServiceMonitorSpecEndpoints#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_relabelings(
        self,
    ) -> typing.Optional[typing.List["ServiceMonitorSpecEndpointsMetricRelabelings"]]:
        '''MetricRelabelConfigs to apply to samples before ingestion.

        :schema: ServiceMonitorSpecEndpoints#metricRelabelings
        '''
        result = self._values.get("metric_relabelings")
        return typing.cast(typing.Optional[typing.List["ServiceMonitorSpecEndpointsMetricRelabelings"]], result)

    @builtins.property
    def oauth2(self) -> typing.Optional["ServiceMonitorSpecEndpointsOauth2"]:
        '''OAuth2 for the URL.

        Only valid in Prometheus versions 2.27.0 and newer.

        :schema: ServiceMonitorSpecEndpoints#oauth2
        '''
        result = self._values.get("oauth2")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsOauth2"], result)

    @builtins.property
    def params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''Optional HTTP URL parameters.

        :schema: ServiceMonitorSpecEndpoints#params
        '''
        result = self._values.get("params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''HTTP path to scrape for metrics.

        If empty, Prometheus uses the default value (e.g. ``/metrics``).

        :schema: ServiceMonitorSpecEndpoints#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''Name of the service port this endpoint refers to.

        Mutually exclusive with targetPort.

        :schema: ServiceMonitorSpecEndpoints#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_url(self) -> typing.Optional[builtins.str]:
        '''ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint.

        :schema: ServiceMonitorSpecEndpoints#proxyUrl
        '''
        result = self._values.get("proxy_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relabelings(
        self,
    ) -> typing.Optional[typing.List["ServiceMonitorSpecEndpointsRelabelings"]]:
        '''RelabelConfigs to apply to samples before scraping.

        Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields. The original scrape job's name is available via the ``__tmp_prometheus_job_name`` label. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config

        :schema: ServiceMonitorSpecEndpoints#relabelings
        '''
        result = self._values.get("relabelings")
        return typing.cast(typing.Optional[typing.List["ServiceMonitorSpecEndpointsRelabelings"]], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''HTTP scheme to use for scraping.

        :schema: ServiceMonitorSpecEndpoints#scheme
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scrape_timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout after which the scrape is ended If not specified, the Prometheus global scrape timeout is used unless it is less than ``Interval`` in which the latter is used.

        :schema: ServiceMonitorSpecEndpoints#scrapeTimeout
        '''
        result = self._values.get("scrape_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional["ServiceMonitorSpecEndpointsTargetPort"]:
        '''Name or number of the target port of the Pod behind the Service, the port must be specified with container port property.

        Mutually exclusive with port.

        :schema: ServiceMonitorSpecEndpoints#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTargetPort"], result)

    @builtins.property
    def tls_config(self) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfig"]:
        '''TLS configuration to use when scraping the endpoint.

        :schema: ServiceMonitorSpecEndpoints#tlsConfig
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsAuthorization",
    jsii_struct_bases=[],
    name_mapping={"credentials": "credentials", "type": "type"},
)
class ServiceMonitorSpecEndpointsAuthorization:
    def __init__(
        self,
        *,
        credentials: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsAuthorizationCredentials", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Authorization section for this endpoint.

        :param credentials: The secret's key that contains the credentials of the request.
        :param type: Set the authentication type. Defaults to Bearer, Basic will cause an error Default: Bearer, Basic will cause an error

        :schema: ServiceMonitorSpecEndpointsAuthorization
        '''
        if isinstance(credentials, dict):
            credentials = ServiceMonitorSpecEndpointsAuthorizationCredentials(**credentials)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05be2dbf3d1f785c44186c59ea265d852bfc4c161dd2a667dfb7fb72d3fafab)
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if credentials is not None:
            self._values["credentials"] = credentials
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsAuthorizationCredentials"]:
        '''The secret's key that contains the credentials of the request.

        :schema: ServiceMonitorSpecEndpointsAuthorization#credentials
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsAuthorizationCredentials"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Set the authentication type.

        Defaults to Bearer, Basic will cause an error

        :default: Bearer, Basic will cause an error

        :schema: ServiceMonitorSpecEndpointsAuthorization#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsAuthorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsAuthorizationCredentials",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsAuthorizationCredentials:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The secret's key that contains the credentials of the request.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsAuthorizationCredentials
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c83826f5d1af77f6b472277f612d8fe893abd225721d0ad52a0b6e894c6ca91)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsAuthorizationCredentials#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsAuthorizationCredentials#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsAuthorizationCredentials#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsAuthorizationCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class ServiceMonitorSpecEndpointsBasicAuth:
    def __init__(
        self,
        *,
        password: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsBasicAuthPassword", typing.Dict[builtins.str, typing.Any]]] = None,
        username: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsBasicAuthUsername", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''BasicAuth allow an endpoint to authenticate over basic authentication More info: https://prometheus.io/docs/operating/configuration/#endpoints.

        :param password: The secret in the service monitor namespace that contains the password for authentication.
        :param username: The secret in the service monitor namespace that contains the username for authentication.

        :schema: ServiceMonitorSpecEndpointsBasicAuth
        '''
        if isinstance(password, dict):
            password = ServiceMonitorSpecEndpointsBasicAuthPassword(**password)
        if isinstance(username, dict):
            username = ServiceMonitorSpecEndpointsBasicAuthUsername(**username)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bb86167c1eb1b7c3cfb101e3ccc00e531d6a4cf5db0187880449cdd1206f66d)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def password(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsBasicAuthPassword"]:
        '''The secret in the service monitor namespace that contains the password for authentication.

        :schema: ServiceMonitorSpecEndpointsBasicAuth#password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsBasicAuthPassword"], result)

    @builtins.property
    def username(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsBasicAuthUsername"]:
        '''The secret in the service monitor namespace that contains the username for authentication.

        :schema: ServiceMonitorSpecEndpointsBasicAuth#username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsBasicAuthUsername"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsBasicAuthPassword",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsBasicAuthPassword:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The secret in the service monitor namespace that contains the password for authentication.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsBasicAuthPassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0aade533948af8db0e7c96e2e543426177c8f6b9848b8d7d378a3a936439ce)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsBasicAuthPassword#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsBasicAuthPassword#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsBasicAuthPassword#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsBasicAuthPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsBasicAuthUsername",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsBasicAuthUsername:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The secret in the service monitor namespace that contains the username for authentication.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsBasicAuthUsername
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__650161eb2ae5d4744ac93cdb731365c5ebf1f8ffe3eb9fa80895090d59430fc4)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsBasicAuthUsername#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsBasicAuthUsername#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsBasicAuthUsername#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsBasicAuthUsername(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsBearerTokenSecret",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsBearerTokenSecret:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Secret to mount to read bearer token for scraping targets.

        The secret needs to be in the same namespace as the service monitor and accessible by the Prometheus Operator.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsBearerTokenSecret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f101e1b8c5f41fb997e62c8c7f7fc1316f2176377c3a84a57a4345a28bafc76d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsBearerTokenSecret#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsBearerTokenSecret#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsBearerTokenSecret#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsBearerTokenSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsMetricRelabelings",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "modulus": "modulus",
        "regex": "regex",
        "replacement": "replacement",
        "separator": "separator",
        "source_labels": "sourceLabels",
        "target_label": "targetLabel",
    },
)
class ServiceMonitorSpecEndpointsMetricRelabelings:
    def __init__(
        self,
        *,
        action: typing.Optional["ServiceMonitorSpecEndpointsMetricRelabelingsAction"] = None,
        modulus: typing.Optional[jsii.Number] = None,
        regex: typing.Optional[builtins.str] = None,
        replacement: typing.Optional[builtins.str] = None,
        separator: typing.Optional[builtins.str] = None,
        source_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion.

        It defines ``<metric_relabel_configs>``-section of Prometheus configuration. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs

        :param action: Action to perform based on regex matching. Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36. Default: replace'. uppercase and lowercase actions require Prometheus >= 2.36.
        :param modulus: Modulus to take of the hash of the source label values.
        :param regex: Regular expression against which the extracted value is matched. Default is '(.*)' Default: '
        :param replacement: Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1' Default: 1'
        :param separator: Separator placed between concatenated source label values. default is ';'.
        :param source_labels: The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.
        :param target_label: Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecdf834c71cee7105eb773035064fc34b431e349772b048e9be974173861c391)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument modulus", value=modulus, expected_type=type_hints["modulus"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument replacement", value=replacement, expected_type=type_hints["replacement"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            check_type(argname="argument source_labels", value=source_labels, expected_type=type_hints["source_labels"])
            check_type(argname="argument target_label", value=target_label, expected_type=type_hints["target_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if modulus is not None:
            self._values["modulus"] = modulus
        if regex is not None:
            self._values["regex"] = regex
        if replacement is not None:
            self._values["replacement"] = replacement
        if separator is not None:
            self._values["separator"] = separator
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if target_label is not None:
            self._values["target_label"] = target_label

    @builtins.property
    def action(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsMetricRelabelingsAction"]:
        '''Action to perform based on regex matching.

        Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36.

        :default: replace'. uppercase and lowercase actions require Prometheus >= 2.36.

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsMetricRelabelingsAction"], result)

    @builtins.property
    def modulus(self) -> typing.Optional[jsii.Number]:
        '''Modulus to take of the hash of the source label values.

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#modulus
        '''
        result = self._values.get("modulus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Regular expression against which the extracted value is matched.

        Default is '(.*)'

        :default: '

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replacement(self) -> typing.Optional[builtins.str]:
        '''Replacement value against which a regex replace is performed if the regular expression matches.

        Regex capture groups are available. Default is '$1'

        :default: 1'

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#replacement
        '''
        result = self._values.get("replacement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def separator(self) -> typing.Optional[builtins.str]:
        '''Separator placed between concatenated source label values.

        default is ';'.

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#separator
        '''
        result = self._values.get("separator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The source labels select values from existing labels.

        Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#sourceLabels
        '''
        result = self._values.get("source_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_label(self) -> typing.Optional[builtins.str]:
        '''Label to which the resulting value is written in a replace action.

        It is mandatory for replace actions. Regex capture groups are available.

        :schema: ServiceMonitorSpecEndpointsMetricRelabelings#targetLabel
        '''
        result = self._values.get("target_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsMetricRelabelings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsMetricRelabelingsAction"
)
class ServiceMonitorSpecEndpointsMetricRelabelingsAction(enum.Enum):
    '''Action to perform based on regex matching.

    Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36.

    :default: replace'. uppercase and lowercase actions require Prometheus >= 2.36.

    :schema: ServiceMonitorSpecEndpointsMetricRelabelingsAction
    '''

    REPLACE = "REPLACE"
    '''replace.'''
    KEEP = "KEEP"
    '''keep.'''
    DROP = "DROP"
    '''drop.'''
    HASHMOD = "HASHMOD"
    '''hashmod.'''
    LABELMAP = "LABELMAP"
    '''labelmap.'''
    LABELDROP = "LABELDROP"
    '''labeldrop.'''
    LABELKEEP = "LABELKEEP"
    '''labelkeep.'''
    LOWERCASE = "LOWERCASE"
    '''lowercase.'''
    UPPERCASE = "UPPERCASE"
    '''uppercase.'''


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsOauth2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "token_url": "tokenUrl",
        "endpoint_params": "endpointParams",
        "scopes": "scopes",
    },
)
class ServiceMonitorSpecEndpointsOauth2:
    def __init__(
        self,
        *,
        client_id: typing.Union["ServiceMonitorSpecEndpointsOauth2ClientId", typing.Dict[builtins.str, typing.Any]],
        client_secret: typing.Union["ServiceMonitorSpecEndpointsOauth2ClientSecret", typing.Dict[builtins.str, typing.Any]],
        token_url: builtins.str,
        endpoint_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''OAuth2 for the URL.

        Only valid in Prometheus versions 2.27.0 and newer.

        :param client_id: The secret or configmap containing the OAuth2 client id.
        :param client_secret: The secret containing the OAuth2 client secret.
        :param token_url: The URL to fetch the token from.
        :param endpoint_params: Parameters to append to the token URL.
        :param scopes: OAuth2 scopes used for the token request.

        :schema: ServiceMonitorSpecEndpointsOauth2
        '''
        if isinstance(client_id, dict):
            client_id = ServiceMonitorSpecEndpointsOauth2ClientId(**client_id)
        if isinstance(client_secret, dict):
            client_secret = ServiceMonitorSpecEndpointsOauth2ClientSecret(**client_secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fbf1a17774c9325051b1afae8b5079d104a808c07e2045229b6a3d401d1fcb4)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
            check_type(argname="argument endpoint_params", value=endpoint_params, expected_type=type_hints["endpoint_params"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
        }
        if endpoint_params is not None:
            self._values["endpoint_params"] = endpoint_params
        if scopes is not None:
            self._values["scopes"] = scopes

    @builtins.property
    def client_id(self) -> "ServiceMonitorSpecEndpointsOauth2ClientId":
        '''The secret or configmap containing the OAuth2 client id.

        :schema: ServiceMonitorSpecEndpointsOauth2#clientId
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast("ServiceMonitorSpecEndpointsOauth2ClientId", result)

    @builtins.property
    def client_secret(self) -> "ServiceMonitorSpecEndpointsOauth2ClientSecret":
        '''The secret containing the OAuth2 client secret.

        :schema: ServiceMonitorSpecEndpointsOauth2#clientSecret
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast("ServiceMonitorSpecEndpointsOauth2ClientSecret", result)

    @builtins.property
    def token_url(self) -> builtins.str:
        '''The URL to fetch the token from.

        :schema: ServiceMonitorSpecEndpointsOauth2#tokenUrl
        '''
        result = self._values.get("token_url")
        assert result is not None, "Required property 'token_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Parameters to append to the token URL.

        :schema: ServiceMonitorSpecEndpointsOauth2#endpointParams
        '''
        result = self._values.get("endpoint_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''OAuth2 scopes used for the token request.

        :schema: ServiceMonitorSpecEndpointsOauth2#scopes
        '''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsOauth2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsOauth2ClientId",
    jsii_struct_bases=[],
    name_mapping={"config_map": "configMap", "secret": "secret"},
)
class ServiceMonitorSpecEndpointsOauth2ClientId:
    def __init__(
        self,
        *,
        config_map: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap", typing.Dict[builtins.str, typing.Any]]] = None,
        secret: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsOauth2ClientIdSecret", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''The secret or configmap containing the OAuth2 client id.

        :param config_map: ConfigMap containing data to use for the targets.
        :param secret: Secret containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientId
        '''
        if isinstance(config_map, dict):
            config_map = ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap(**config_map)
        if isinstance(secret, dict):
            secret = ServiceMonitorSpecEndpointsOauth2ClientIdSecret(**secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b23a4d24eb9eb69c5d201cdffad8413acfa1f419c8a41a1d59e60b419084b5e)
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_map is not None:
            self._values["config_map"] = config_map
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def config_map(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap"]:
        '''ConfigMap containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientId#configMap
        '''
        result = self._values.get("config_map")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap"], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsOauth2ClientIdSecret"]:
        '''Secret containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientId#secret
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsOauth2ClientIdSecret"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsOauth2ClientId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''ConfigMap containing data to use for the targets.

        :param key: The key to select.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the ConfigMap or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec94d0b7ad6b1d19e33b596d14da05ba8a4e7ca4ca951dc592d31e9d25189676)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key to select.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsOauth2ClientIdSecret",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsOauth2ClientIdSecret:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Secret containing data to use for the targets.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdSecret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87adb09a12da5a2e30ed878fc51cb100bb3d1390ff6aaef2644476c51f4cff23)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdSecret#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdSecret#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientIdSecret#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsOauth2ClientIdSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsOauth2ClientSecret",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsOauth2ClientSecret:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The secret containing the OAuth2 client secret.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientSecret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a5f493304f38e2b06749204c2233f60863fb580f98104b324a73426c3f8810)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientSecret#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsOauth2ClientSecret#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsOauth2ClientSecret#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsOauth2ClientSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsRelabelings",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "modulus": "modulus",
        "regex": "regex",
        "replacement": "replacement",
        "separator": "separator",
        "source_labels": "sourceLabels",
        "target_label": "targetLabel",
    },
)
class ServiceMonitorSpecEndpointsRelabelings:
    def __init__(
        self,
        *,
        action: typing.Optional["ServiceMonitorSpecEndpointsRelabelingsAction"] = None,
        modulus: typing.Optional[jsii.Number] = None,
        regex: typing.Optional[builtins.str] = None,
        replacement: typing.Optional[builtins.str] = None,
        separator: typing.Optional[builtins.str] = None,
        source_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion.

        It defines ``<metric_relabel_configs>``-section of Prometheus configuration. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs

        :param action: Action to perform based on regex matching. Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36. Default: replace'. uppercase and lowercase actions require Prometheus >= 2.36.
        :param modulus: Modulus to take of the hash of the source label values.
        :param regex: Regular expression against which the extracted value is matched. Default is '(.*)' Default: '
        :param replacement: Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is '$1' Default: 1'
        :param separator: Separator placed between concatenated source label values. default is ';'.
        :param source_labels: The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.
        :param target_label: Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available.

        :schema: ServiceMonitorSpecEndpointsRelabelings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2635c776631324d4d88ad60676fe0b6bf4e435f64f67f6bd98c0af6e1a54b3d7)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument modulus", value=modulus, expected_type=type_hints["modulus"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument replacement", value=replacement, expected_type=type_hints["replacement"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            check_type(argname="argument source_labels", value=source_labels, expected_type=type_hints["source_labels"])
            check_type(argname="argument target_label", value=target_label, expected_type=type_hints["target_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if modulus is not None:
            self._values["modulus"] = modulus
        if regex is not None:
            self._values["regex"] = regex
        if replacement is not None:
            self._values["replacement"] = replacement
        if separator is not None:
            self._values["separator"] = separator
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if target_label is not None:
            self._values["target_label"] = target_label

    @builtins.property
    def action(self) -> typing.Optional["ServiceMonitorSpecEndpointsRelabelingsAction"]:
        '''Action to perform based on regex matching.

        Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36.

        :default: replace'. uppercase and lowercase actions require Prometheus >= 2.36.

        :schema: ServiceMonitorSpecEndpointsRelabelings#action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsRelabelingsAction"], result)

    @builtins.property
    def modulus(self) -> typing.Optional[jsii.Number]:
        '''Modulus to take of the hash of the source label values.

        :schema: ServiceMonitorSpecEndpointsRelabelings#modulus
        '''
        result = self._values.get("modulus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Regular expression against which the extracted value is matched.

        Default is '(.*)'

        :default: '

        :schema: ServiceMonitorSpecEndpointsRelabelings#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replacement(self) -> typing.Optional[builtins.str]:
        '''Replacement value against which a regex replace is performed if the regular expression matches.

        Regex capture groups are available. Default is '$1'

        :default: 1'

        :schema: ServiceMonitorSpecEndpointsRelabelings#replacement
        '''
        result = self._values.get("replacement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def separator(self) -> typing.Optional[builtins.str]:
        '''Separator placed between concatenated source label values.

        default is ';'.

        :schema: ServiceMonitorSpecEndpointsRelabelings#separator
        '''
        result = self._values.get("separator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The source labels select values from existing labels.

        Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions.

        :schema: ServiceMonitorSpecEndpointsRelabelings#sourceLabels
        '''
        result = self._values.get("source_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_label(self) -> typing.Optional[builtins.str]:
        '''Label to which the resulting value is written in a replace action.

        It is mandatory for replace actions. Regex capture groups are available.

        :schema: ServiceMonitorSpecEndpointsRelabelings#targetLabel
        '''
        result = self._values.get("target_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsRelabelings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsRelabelingsAction"
)
class ServiceMonitorSpecEndpointsRelabelingsAction(enum.Enum):
    '''Action to perform based on regex matching.

    Default is 'replace'. uppercase and lowercase actions require Prometheus >= 2.36.

    :default: replace'. uppercase and lowercase actions require Prometheus >= 2.36.

    :schema: ServiceMonitorSpecEndpointsRelabelingsAction
    '''

    REPLACE = "REPLACE"
    '''replace.'''
    KEEP = "KEEP"
    '''keep.'''
    DROP = "DROP"
    '''drop.'''
    HASHMOD = "HASHMOD"
    '''hashmod.'''
    LABELMAP = "LABELMAP"
    '''labelmap.'''
    LABELDROP = "LABELDROP"
    '''labeldrop.'''
    LABELKEEP = "LABELKEEP"
    '''labelkeep.'''
    LOWERCASE = "LOWERCASE"
    '''lowercase.'''
    UPPERCASE = "UPPERCASE"
    '''uppercase.'''


class ServiceMonitorSpecEndpointsTargetPort(
    metaclass=jsii.JSIIMeta,
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTargetPort",
):
    '''Name or number of the target port of the Pod behind the Service, the port must be specified with container port property.

    Mutually exclusive with port.

    :schema: ServiceMonitorSpecEndpointsTargetPort
    '''

    @jsii.member(jsii_name="fromNumber")
    @builtins.classmethod
    def from_number(cls, value: jsii.Number) -> "ServiceMonitorSpecEndpointsTargetPort":
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921466a7217a2e8c0331771b9a8e0d0eae5bcaaf21ce66143ab70c1574377ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("ServiceMonitorSpecEndpointsTargetPort", jsii.sinvoke(cls, "fromNumber", [value]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(
        cls,
        value: builtins.str,
    ) -> "ServiceMonitorSpecEndpointsTargetPort":
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__637b86ffabdc810a999e12c8ef0d4865b9dcb222e2b33b3127f2d5d298cb04fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("ServiceMonitorSpecEndpointsTargetPort", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Union[builtins.str, jsii.Number]:
        return typing.cast(typing.Union[builtins.str, jsii.Number], jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "ca": "ca",
        "ca_file": "caFile",
        "cert": "cert",
        "cert_file": "certFile",
        "insecure_skip_verify": "insecureSkipVerify",
        "key_file": "keyFile",
        "key_secret": "keySecret",
        "server_name": "serverName",
    },
)
class ServiceMonitorSpecEndpointsTlsConfig:
    def __init__(
        self,
        *,
        ca: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigCa", typing.Dict[builtins.str, typing.Any]]] = None,
        ca_file: typing.Optional[builtins.str] = None,
        cert: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigCert", typing.Dict[builtins.str, typing.Any]]] = None,
        cert_file: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[builtins.bool] = None,
        key_file: typing.Optional[builtins.str] = None,
        key_secret: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigKeySecret", typing.Dict[builtins.str, typing.Any]]] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''TLS configuration to use when scraping the endpoint.

        :param ca: Certificate authority used when verifying server certificates.
        :param ca_file: Path to the CA cert in the Prometheus container to use for the targets.
        :param cert: Client certificate to present when doing client-authentication.
        :param cert_file: Path to the client cert file in the Prometheus container for the targets.
        :param insecure_skip_verify: Disable target certificate validation.
        :param key_file: Path to the client key file in the Prometheus container for the targets.
        :param key_secret: Secret containing the client key file for the targets.
        :param server_name: Used to verify the hostname for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfig
        '''
        if isinstance(ca, dict):
            ca = ServiceMonitorSpecEndpointsTlsConfigCa(**ca)
        if isinstance(cert, dict):
            cert = ServiceMonitorSpecEndpointsTlsConfigCert(**cert)
        if isinstance(key_secret, dict):
            key_secret = ServiceMonitorSpecEndpointsTlsConfigKeySecret(**key_secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f61ccd8cbac6223a039c16101703c8606ce1f842334d316300d980bb74ee2d)
            check_type(argname="argument ca", value=ca, expected_type=type_hints["ca"])
            check_type(argname="argument ca_file", value=ca_file, expected_type=type_hints["ca_file"])
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument cert_file", value=cert_file, expected_type=type_hints["cert_file"])
            check_type(argname="argument insecure_skip_verify", value=insecure_skip_verify, expected_type=type_hints["insecure_skip_verify"])
            check_type(argname="argument key_file", value=key_file, expected_type=type_hints["key_file"])
            check_type(argname="argument key_secret", value=key_secret, expected_type=type_hints["key_secret"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca is not None:
            self._values["ca"] = ca
        if ca_file is not None:
            self._values["ca_file"] = ca_file
        if cert is not None:
            self._values["cert"] = cert
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if key_file is not None:
            self._values["key_file"] = key_file
        if key_secret is not None:
            self._values["key_secret"] = key_secret
        if server_name is not None:
            self._values["server_name"] = server_name

    @builtins.property
    def ca(self) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCa"]:
        '''Certificate authority used when verifying server certificates.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#ca
        '''
        result = self._values.get("ca")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCa"], result)

    @builtins.property
    def ca_file(self) -> typing.Optional[builtins.str]:
        '''Path to the CA cert in the Prometheus container to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#caFile
        '''
        result = self._values.get("ca_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert(self) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCert"]:
        '''Client certificate to present when doing client-authentication.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#cert
        '''
        result = self._values.get("cert")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCert"], result)

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''Path to the client cert file in the Prometheus container for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#certFile
        '''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(self) -> typing.Optional[builtins.bool]:
        '''Disable target certificate validation.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#insecureSkipVerify
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key_file(self) -> typing.Optional[builtins.str]:
        '''Path to the client key file in the Prometheus container for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#keyFile
        '''
        result = self._values.get("key_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_secret(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigKeySecret"]:
        '''Secret containing the client key file for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#keySecret
        '''
        result = self._values.get("key_secret")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigKeySecret"], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''Used to verify the hostname for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfig#serverName
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigCa",
    jsii_struct_bases=[],
    name_mapping={"config_map": "configMap", "secret": "secret"},
)
class ServiceMonitorSpecEndpointsTlsConfigCa:
    def __init__(
        self,
        *,
        config_map: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigCaConfigMap", typing.Dict[builtins.str, typing.Any]]] = None,
        secret: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigCaSecret", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Certificate authority used when verifying server certificates.

        :param config_map: ConfigMap containing data to use for the targets.
        :param secret: Secret containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCa
        '''
        if isinstance(config_map, dict):
            config_map = ServiceMonitorSpecEndpointsTlsConfigCaConfigMap(**config_map)
        if isinstance(secret, dict):
            secret = ServiceMonitorSpecEndpointsTlsConfigCaSecret(**secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0e3bda2c9cf9f5c7ebe493483bb7890dd7b12e129f323712b0d1b5bcf35c6b)
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_map is not None:
            self._values["config_map"] = config_map
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def config_map(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCaConfigMap"]:
        '''ConfigMap containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCa#configMap
        '''
        result = self._values.get("config_map")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCaConfigMap"], result)

    @builtins.property
    def secret(self) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCaSecret"]:
        '''Secret containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCa#secret
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCaSecret"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigCa(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigCaConfigMap",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsTlsConfigCaConfigMap:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''ConfigMap containing data to use for the targets.

        :param key: The key to select.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the ConfigMap or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaConfigMap
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f281050edbf368ccdc8635525823ea5e2a98d556fc88178a1b5496e01c1d173)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key to select.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaConfigMap#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaConfigMap#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaConfigMap#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigCaConfigMap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigCaSecret",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsTlsConfigCaSecret:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Secret containing data to use for the targets.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaSecret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f85e562e9ea5ccc14e6f2ebb0dfa3bec9acedd855dd37e3454e187f0f3eda4ee)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaSecret#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaSecret#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCaSecret#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigCaSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigCert",
    jsii_struct_bases=[],
    name_mapping={"config_map": "configMap", "secret": "secret"},
)
class ServiceMonitorSpecEndpointsTlsConfigCert:
    def __init__(
        self,
        *,
        config_map: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigCertConfigMap", typing.Dict[builtins.str, typing.Any]]] = None,
        secret: typing.Optional[typing.Union["ServiceMonitorSpecEndpointsTlsConfigCertSecret", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Client certificate to present when doing client-authentication.

        :param config_map: ConfigMap containing data to use for the targets.
        :param secret: Secret containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCert
        '''
        if isinstance(config_map, dict):
            config_map = ServiceMonitorSpecEndpointsTlsConfigCertConfigMap(**config_map)
        if isinstance(secret, dict):
            secret = ServiceMonitorSpecEndpointsTlsConfigCertSecret(**secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6582fab979e22866d67d8ec9ed1ca599a28e957aa40db8821f3884224dd8c9)
            check_type(argname="argument config_map", value=config_map, expected_type=type_hints["config_map"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_map is not None:
            self._values["config_map"] = config_map
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def config_map(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCertConfigMap"]:
        '''ConfigMap containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCert#configMap
        '''
        result = self._values.get("config_map")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCertConfigMap"], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCertSecret"]:
        '''Secret containing data to use for the targets.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCert#secret
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional["ServiceMonitorSpecEndpointsTlsConfigCertSecret"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigCert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigCertConfigMap",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsTlsConfigCertConfigMap:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''ConfigMap containing data to use for the targets.

        :param key: The key to select.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the ConfigMap or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertConfigMap
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7438f334d5518e8db9c8f8f9d7b7eae5d251d0d23c70c6c81de817a9aaca462)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key to select.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertConfigMap#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertConfigMap#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the ConfigMap or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertConfigMap#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigCertConfigMap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigCertSecret",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsTlsConfigCertSecret:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Secret containing data to use for the targets.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertSecret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3376a030f3eeef358b5a57d83bb8f17fec010fde7f20bcf209b46ab4c63161c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertSecret#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertSecret#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigCertSecret#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigCertSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecEndpointsTlsConfigKeySecret",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class ServiceMonitorSpecEndpointsTlsConfigKeySecret:
    def __init__(
        self,
        *,
        key: builtins.str,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Secret containing the client key file for the targets.

        :param key: The key of the secret to select from. Must be a valid secret key.
        :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
        :param optional: Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigKeySecret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a121bd59efac998876b4760c4d96a77dbcfcab89ff8734d421528126d32553a9)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret to select from.

        Must be a valid secret key.

        :schema: ServiceMonitorSpecEndpointsTlsConfigKeySecret#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?

        :schema: ServiceMonitorSpecEndpointsTlsConfigKeySecret#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(self) -> typing.Optional[builtins.bool]:
        '''Specify whether the Secret or its key must be defined.

        :schema: ServiceMonitorSpecEndpointsTlsConfigKeySecret#optional
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecEndpointsTlsConfigKeySecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={"any": "any", "match_names": "matchNames"},
)
class ServiceMonitorSpecNamespaceSelector:
    def __init__(
        self,
        *,
        any: typing.Optional[builtins.bool] = None,
        match_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Selector to select which namespaces the Kubernetes Endpoints objects are discovered from.

        :param any: Boolean describing whether all namespaces are selected in contrast to a list restricting them.
        :param match_names: List of namespace names to select from.

        :schema: ServiceMonitorSpecNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3777ad0e448bbe33a35bb765a202fa80d5ee3d0645daad234080935f7a1382a)
            check_type(argname="argument any", value=any, expected_type=type_hints["any"])
            check_type(argname="argument match_names", value=match_names, expected_type=type_hints["match_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if any is not None:
            self._values["any"] = any
        if match_names is not None:
            self._values["match_names"] = match_names

    @builtins.property
    def any(self) -> typing.Optional[builtins.bool]:
        '''Boolean describing whether all namespaces are selected in contrast to a list restricting them.

        :schema: ServiceMonitorSpecNamespaceSelector#any
        '''
        result = self._values.get("any")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def match_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of namespace names to select from.

        :schema: ServiceMonitorSpecNamespaceSelector#matchNames
        '''
        result = self._values.get("match_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ServiceMonitorSpecSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ServiceMonitorSpecSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Selector to select Endpoints objects.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ServiceMonitorSpecSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75475617ce7ac77ec0e4c501cb7ce5e19effcb4debd314d1f947679b9fcba6e1)
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
    ) -> typing.Optional[typing.List["ServiceMonitorSpecSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ServiceMonitorSpecSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ServiceMonitorSpecSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ServiceMonitorSpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comcoreosmonitoring.ServiceMonitorSpecSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ServiceMonitorSpecSelectorMatchExpressions:
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

        :schema: ServiceMonitorSpecSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b17baff1becd42b6823f8a48b1b57fa905d0467e143302eafd1d9d0c098db45)
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

        :schema: ServiceMonitorSpecSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ServiceMonitorSpecSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ServiceMonitorSpecSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMonitorSpecSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ServiceMonitor",
    "ServiceMonitorProps",
    "ServiceMonitorSpec",
    "ServiceMonitorSpecAttachMetadata",
    "ServiceMonitorSpecEndpoints",
    "ServiceMonitorSpecEndpointsAuthorization",
    "ServiceMonitorSpecEndpointsAuthorizationCredentials",
    "ServiceMonitorSpecEndpointsBasicAuth",
    "ServiceMonitorSpecEndpointsBasicAuthPassword",
    "ServiceMonitorSpecEndpointsBasicAuthUsername",
    "ServiceMonitorSpecEndpointsBearerTokenSecret",
    "ServiceMonitorSpecEndpointsMetricRelabelings",
    "ServiceMonitorSpecEndpointsMetricRelabelingsAction",
    "ServiceMonitorSpecEndpointsOauth2",
    "ServiceMonitorSpecEndpointsOauth2ClientId",
    "ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap",
    "ServiceMonitorSpecEndpointsOauth2ClientIdSecret",
    "ServiceMonitorSpecEndpointsOauth2ClientSecret",
    "ServiceMonitorSpecEndpointsRelabelings",
    "ServiceMonitorSpecEndpointsRelabelingsAction",
    "ServiceMonitorSpecEndpointsTargetPort",
    "ServiceMonitorSpecEndpointsTlsConfig",
    "ServiceMonitorSpecEndpointsTlsConfigCa",
    "ServiceMonitorSpecEndpointsTlsConfigCaConfigMap",
    "ServiceMonitorSpecEndpointsTlsConfigCaSecret",
    "ServiceMonitorSpecEndpointsTlsConfigCert",
    "ServiceMonitorSpecEndpointsTlsConfigCertConfigMap",
    "ServiceMonitorSpecEndpointsTlsConfigCertSecret",
    "ServiceMonitorSpecEndpointsTlsConfigKeySecret",
    "ServiceMonitorSpecNamespaceSelector",
    "ServiceMonitorSpecSelector",
    "ServiceMonitorSpecSelectorMatchExpressions",
]

publication.publish()

def _typecheckingstub__ae743b5825b3e6075ede1500d52f893c3c6a63be14f647f9a44d0e722d356470(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    spec: typing.Union[ServiceMonitorSpec, typing.Dict[builtins.str, typing.Any]],
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56bca6778cf6036cd0140b25f1a1429742323914ee819ae9276e47c0e290aaf5(
    *,
    spec: typing.Union[ServiceMonitorSpec, typing.Dict[builtins.str, typing.Any]],
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77dad9e9e97980d2d9001de098d81faeb424d5144d09285dc28512f29a3815ba(
    *,
    endpoints: typing.Sequence[typing.Union[ServiceMonitorSpecEndpoints, typing.Dict[builtins.str, typing.Any]]],
    selector: typing.Union[ServiceMonitorSpecSelector, typing.Dict[builtins.str, typing.Any]],
    attach_metadata: typing.Optional[typing.Union[ServiceMonitorSpecAttachMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    job_label: typing.Optional[builtins.str] = None,
    label_limit: typing.Optional[jsii.Number] = None,
    label_name_length_limit: typing.Optional[jsii.Number] = None,
    label_value_length_limit: typing.Optional[jsii.Number] = None,
    namespace_selector: typing.Optional[typing.Union[ServiceMonitorSpecNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_target_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    sample_limit: typing.Optional[jsii.Number] = None,
    target_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbe935572488af708dc3190e619dcc20410fc1feb14d189191dcc70c240bc2a(
    *,
    node: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0387a341502661c257fa633a8de56a63d951087fafafcbad7e1c75709428ef9f(
    *,
    authorization: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsAuthorization, typing.Dict[builtins.str, typing.Any]]] = None,
    basic_auth: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    bearer_token_file: typing.Optional[builtins.str] = None,
    bearer_token_secret: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsBearerTokenSecret, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_http2: typing.Optional[builtins.bool] = None,
    filter_running: typing.Optional[builtins.bool] = None,
    follow_redirects: typing.Optional[builtins.bool] = None,
    honor_labels: typing.Optional[builtins.bool] = None,
    honor_timestamps: typing.Optional[builtins.bool] = None,
    interval: typing.Optional[builtins.str] = None,
    metric_relabelings: typing.Optional[typing.Sequence[typing.Union[ServiceMonitorSpecEndpointsMetricRelabelings, typing.Dict[builtins.str, typing.Any]]]] = None,
    oauth2: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsOauth2, typing.Dict[builtins.str, typing.Any]]] = None,
    params: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    relabelings: typing.Optional[typing.Sequence[typing.Union[ServiceMonitorSpecEndpointsRelabelings, typing.Dict[builtins.str, typing.Any]]]] = None,
    scheme: typing.Optional[builtins.str] = None,
    scrape_timeout: typing.Optional[builtins.str] = None,
    target_port: typing.Optional[ServiceMonitorSpecEndpointsTargetPort] = None,
    tls_config: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05be2dbf3d1f785c44186c59ea265d852bfc4c161dd2a667dfb7fb72d3fafab(
    *,
    credentials: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsAuthorizationCredentials, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c83826f5d1af77f6b472277f612d8fe893abd225721d0ad52a0b6e894c6ca91(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bb86167c1eb1b7c3cfb101e3ccc00e531d6a4cf5db0187880449cdd1206f66d(
    *,
    password: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsBasicAuthPassword, typing.Dict[builtins.str, typing.Any]]] = None,
    username: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsBasicAuthUsername, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0aade533948af8db0e7c96e2e543426177c8f6b9848b8d7d378a3a936439ce(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__650161eb2ae5d4744ac93cdb731365c5ebf1f8ffe3eb9fa80895090d59430fc4(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f101e1b8c5f41fb997e62c8c7f7fc1316f2176377c3a84a57a4345a28bafc76d(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecdf834c71cee7105eb773035064fc34b431e349772b048e9be974173861c391(
    *,
    action: typing.Optional[ServiceMonitorSpecEndpointsMetricRelabelingsAction] = None,
    modulus: typing.Optional[jsii.Number] = None,
    regex: typing.Optional[builtins.str] = None,
    replacement: typing.Optional[builtins.str] = None,
    separator: typing.Optional[builtins.str] = None,
    source_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbf1a17774c9325051b1afae8b5079d104a808c07e2045229b6a3d401d1fcb4(
    *,
    client_id: typing.Union[ServiceMonitorSpecEndpointsOauth2ClientId, typing.Dict[builtins.str, typing.Any]],
    client_secret: typing.Union[ServiceMonitorSpecEndpointsOauth2ClientSecret, typing.Dict[builtins.str, typing.Any]],
    token_url: builtins.str,
    endpoint_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b23a4d24eb9eb69c5d201cdffad8413acfa1f419c8a41a1d59e60b419084b5e(
    *,
    config_map: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsOauth2ClientIdConfigMap, typing.Dict[builtins.str, typing.Any]]] = None,
    secret: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsOauth2ClientIdSecret, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec94d0b7ad6b1d19e33b596d14da05ba8a4e7ca4ca951dc592d31e9d25189676(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87adb09a12da5a2e30ed878fc51cb100bb3d1390ff6aaef2644476c51f4cff23(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a5f493304f38e2b06749204c2233f60863fb580f98104b324a73426c3f8810(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2635c776631324d4d88ad60676fe0b6bf4e435f64f67f6bd98c0af6e1a54b3d7(
    *,
    action: typing.Optional[ServiceMonitorSpecEndpointsRelabelingsAction] = None,
    modulus: typing.Optional[jsii.Number] = None,
    regex: typing.Optional[builtins.str] = None,
    replacement: typing.Optional[builtins.str] = None,
    separator: typing.Optional[builtins.str] = None,
    source_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921466a7217a2e8c0331771b9a8e0d0eae5bcaaf21ce66143ab70c1574377ef4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__637b86ffabdc810a999e12c8ef0d4865b9dcb222e2b33b3127f2d5d298cb04fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f61ccd8cbac6223a039c16101703c8606ce1f842334d316300d980bb74ee2d(
    *,
    ca: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigCa, typing.Dict[builtins.str, typing.Any]]] = None,
    ca_file: typing.Optional[builtins.str] = None,
    cert: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigCert, typing.Dict[builtins.str, typing.Any]]] = None,
    cert_file: typing.Optional[builtins.str] = None,
    insecure_skip_verify: typing.Optional[builtins.bool] = None,
    key_file: typing.Optional[builtins.str] = None,
    key_secret: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigKeySecret, typing.Dict[builtins.str, typing.Any]]] = None,
    server_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0e3bda2c9cf9f5c7ebe493483bb7890dd7b12e129f323712b0d1b5bcf35c6b(
    *,
    config_map: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigCaConfigMap, typing.Dict[builtins.str, typing.Any]]] = None,
    secret: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigCaSecret, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f281050edbf368ccdc8635525823ea5e2a98d556fc88178a1b5496e01c1d173(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85e562e9ea5ccc14e6f2ebb0dfa3bec9acedd855dd37e3454e187f0f3eda4ee(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6582fab979e22866d67d8ec9ed1ca599a28e957aa40db8821f3884224dd8c9(
    *,
    config_map: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigCertConfigMap, typing.Dict[builtins.str, typing.Any]]] = None,
    secret: typing.Optional[typing.Union[ServiceMonitorSpecEndpointsTlsConfigCertSecret, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7438f334d5518e8db9c8f8f9d7b7eae5d251d0d23c70c6c81de817a9aaca462(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3376a030f3eeef358b5a57d83bb8f17fec010fde7f20bcf209b46ab4c63161c(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a121bd59efac998876b4760c4d96a77dbcfcab89ff8734d421528126d32553a9(
    *,
    key: builtins.str,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3777ad0e448bbe33a35bb765a202fa80d5ee3d0645daad234080935f7a1382a(
    *,
    any: typing.Optional[builtins.bool] = None,
    match_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75475617ce7ac77ec0e4c501cb7ce5e19effcb4debd314d1f947679b9fcba6e1(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ServiceMonitorSpecSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b17baff1becd42b6823f8a48b1b57fa905d0467e143302eafd1d9d0c098db45(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
