'''
# `kubernetes_service_v1`

Refer to the Terraform Registory for docs: [`kubernetes_service_v1`](https://www.terraform.io/docs/providers/kubernetes/r/service_v1).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class ServiceV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1 kubernetes_service_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ServiceV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ServiceV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ServiceV1Timeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1 kubernetes_service_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#metadata ServiceV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#spec ServiceV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#id ServiceV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#timeouts ServiceV1#timeouts}
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#wait_for_load_balancer ServiceV1#wait_for_load_balancer}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5eade294a227f8f4879545dc4710488c43c58a17edefe6263b3d0d3c9b230f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceV1Config(
            metadata=metadata,
            spec=spec,
            id=id,
            timeouts=timeouts,
            wait_for_load_balancer=wait_for_load_balancer,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the service that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#annotations ServiceV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#generate_name ServiceV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the service. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#labels ServiceV1#labels}
        :param name: Name of the service, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#name ServiceV1#name}
        :param namespace: Namespace defines the space within which name of the service must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#namespace ServiceV1#namespace}
        '''
        value = ServiceV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
            namespace=namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        allocate_load_balancer_node_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cluster_ip: typing.Optional[builtins.str] = None,
        cluster_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        external_traffic_policy: typing.Optional[builtins.str] = None,
        health_check_node_port: typing.Optional[jsii.Number] = None,
        internal_traffic_policy: typing.Optional[builtins.str] = None,
        ip_families: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_family_policy: typing.Optional[builtins.str] = None,
        load_balancer_class: typing.Optional[builtins.str] = None,
        load_balancer_ip: typing.Optional[builtins.str] = None,
        load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceV1SpecPort", typing.Dict[builtins.str, typing.Any]]]]] = None,
        publish_not_ready_addresses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        session_affinity_config: typing.Optional[typing.Union["ServiceV1SpecSessionAffinityConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allocate_load_balancer_node_ports: Defines if ``NodePorts`` will be automatically allocated for services with type ``LoadBalancer``. It may be set to ``false`` if the cluster load-balancer does not rely on ``NodePorts``. If the caller requests specific ``NodePorts`` (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type ``LoadBalancer``. Default is ``true``. More info: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#allocate_load_balancer_node_ports ServiceV1#allocate_load_balancer_node_ports}
        :param cluster_ip: The IP address of the service. It is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. ``None`` can be specified for headless services when proxying is not required. Ignored if type is ``ExternalName``. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#cluster_ip ServiceV1#cluster_ip}
        :param cluster_ips: List of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise creation of the service will fail. If this field is not specified, it will be initialized from the ``clusterIP`` field. If this field is specified, clients must ensure that ``clusterIPs[0]`` and ``clusterIP`` have the same value. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#cluster_ips ServiceV1#cluster_ips}
        :param external_ips: A list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_ips ServiceV1#external_ips}
        :param external_name: The external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid DNS name and requires ``type`` to be ``ExternalName``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_name ServiceV1#external_name}
        :param external_traffic_policy: Denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. ``Local`` preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. ``Cluster`` obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading. More info: https://kubernetes.io/docs/tutorials/services/source-ip/ Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_traffic_policy ServiceV1#external_traffic_policy}
        :param health_check_node_port: Specifies the Healthcheck NodePort for the service. Only effects when type is set to ``LoadBalancer`` and external_traffic_policy is set to ``Local``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#health_check_node_port ServiceV1#health_check_node_port}
        :param internal_traffic_policy: Specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only. ``Cluster`` routes internal traffic to a Service to all endpoints. ``Local`` routes traffic to node-local endpoints only, traffic is dropped if no node-local endpoints are ready. The default value is ``Cluster``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#internal_traffic_policy ServiceV1#internal_traffic_policy}
        :param ip_families: IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#ip_families ServiceV1#ip_families}
        :param ip_family_policy: IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#ip_family_policy ServiceV1#ip_family_policy}
        :param load_balancer_class: The class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix. This field can only be set when the Service type is ``LoadBalancer``. If not set, the default load balancer implementation is used. This field can only be set when creating or updating a Service to type ``LoadBalancer``. More info: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_class ServiceV1#load_balancer_class}
        :param load_balancer_ip: Only applies to ``type = LoadBalancer``. LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying this field when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_ip ServiceV1#load_balancer_ip}
        :param load_balancer_source_ranges: If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature. More info: http://kubernetes.io/docs/user-guide/services-firewalls Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_source_ranges ServiceV1#load_balancer_source_ranges}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#port ServiceV1#port}
        :param publish_not_ready_addresses: When set to true, indicates that DNS implementations must publish the ``notReadyAddresses`` of subsets for the Endpoints associated with the Service. The default value is ``false``. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate ``SRV`` records for its Pods without respect to their readiness for purpose of peer discovery. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#publish_not_ready_addresses ServiceV1#publish_not_ready_addresses}
        :param selector: Route service traffic to pods with label keys and values matching this selector. Only applies to types ``ClusterIP``, ``NodePort``, and ``LoadBalancer``. More info: http://kubernetes.io/docs/user-guide/services#overview Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#selector ServiceV1#selector}
        :param session_affinity: Used to maintain session affinity. Supports ``ClientIP`` and ``None``. Defaults to ``None``. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#session_affinity ServiceV1#session_affinity}
        :param session_affinity_config: session_affinity_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#session_affinity_config ServiceV1#session_affinity_config}
        :param type: Determines how the service is exposed. Defaults to ``ClusterIP``. Valid options are ``ExternalName``, ``ClusterIP``, ``NodePort``, and ``LoadBalancer``. ``ExternalName`` maps to the specified ``external_name``. More info: http://kubernetes.io/docs/user-guide/services#overview Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#type ServiceV1#type}
        '''
        value = ServiceV1Spec(
            allocate_load_balancer_node_ports=allocate_load_balancer_node_ports,
            cluster_ip=cluster_ip,
            cluster_ips=cluster_ips,
            external_ips=external_ips,
            external_name=external_name,
            external_traffic_policy=external_traffic_policy,
            health_check_node_port=health_check_node_port,
            internal_traffic_policy=internal_traffic_policy,
            ip_families=ip_families,
            ip_family_policy=ip_family_policy,
            load_balancer_class=load_balancer_class,
            load_balancer_ip=load_balancer_ip,
            load_balancer_source_ranges=load_balancer_source_ranges,
            port=port,
            publish_not_ready_addresses=publish_not_ready_addresses,
            selector=selector,
            session_affinity=session_affinity,
            session_affinity_config=session_affinity_config,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#create ServiceV1#create}.
        '''
        value = ServiceV1Timeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWaitForLoadBalancer")
    def reset_wait_for_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForLoadBalancer", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "ServiceV1MetadataOutputReference":
        return typing.cast("ServiceV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "ServiceV1SpecOutputReference":
        return typing.cast("ServiceV1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "ServiceV1StatusList":
        return typing.cast("ServiceV1StatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ServiceV1TimeoutsOutputReference":
        return typing.cast("ServiceV1TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["ServiceV1Metadata"]:
        return typing.cast(typing.Optional["ServiceV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["ServiceV1Spec"]:
        return typing.cast(typing.Optional["ServiceV1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ServiceV1Timeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ServiceV1Timeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForLoadBalancerInput")
    def wait_for_load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForLoadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8201040bcc0284ccd42cb63f8d5962e841b05bceb6f3c9b705d0ffc48ac2c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="waitForLoadBalancer")
    def wait_for_load_balancer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForLoadBalancer"))

    @wait_for_load_balancer.setter
    def wait_for_load_balancer(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1832b15888659c6e4bc39711136fae86e4389d2f0703f66acaaefd3d3a199f6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForLoadBalancer", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metadata": "metadata",
        "spec": "spec",
        "id": "id",
        "timeouts": "timeouts",
        "wait_for_load_balancer": "waitForLoadBalancer",
    },
)
class ServiceV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Union["ServiceV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ServiceV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ServiceV1Timeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#metadata ServiceV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#spec ServiceV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#id ServiceV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#timeouts ServiceV1#timeouts}
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#wait_for_load_balancer ServiceV1#wait_for_load_balancer}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ServiceV1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = ServiceV1Spec(**spec)
        if isinstance(timeouts, dict):
            timeouts = ServiceV1Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd441e02c1cd57f6078718358bbcc4e69df8dfd53bafd3a0732a885c878ec36d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument wait_for_load_balancer", value=wait_for_load_balancer, expected_type=type_hints["wait_for_load_balancer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if wait_for_load_balancer is not None:
            self._values["wait_for_load_balancer"] = wait_for_load_balancer

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def metadata(self) -> "ServiceV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#metadata ServiceV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ServiceV1Metadata", result)

    @builtins.property
    def spec(self) -> "ServiceV1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#spec ServiceV1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("ServiceV1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#id ServiceV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ServiceV1Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#timeouts ServiceV1#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ServiceV1Timeouts"], result)

    @builtins.property
    def wait_for_load_balancer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#wait_for_load_balancer ServiceV1#wait_for_load_balancer}
        '''
        result = self._values.get("wait_for_load_balancer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class ServiceV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the service that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#annotations ServiceV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#generate_name ServiceV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the service. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#labels ServiceV1#labels}
        :param name: Name of the service, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#name ServiceV1#name}
        :param namespace: Namespace defines the space within which name of the service must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#namespace ServiceV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc54ca5ccc09a88878579bbf1011c20c088197084adf43bb3aaf33ece257a9ad)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the service that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#annotations ServiceV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#generate_name ServiceV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the service.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#labels ServiceV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the service, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#name ServiceV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the service must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#namespace ServiceV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1MetadataOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a3780831abc7938469caeff430578feb90af0cee78cd9854d006a78b1a611b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetGenerateName")
    def reset_generate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerateName", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="generateNameInput")
    def generate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe35e42a823910223b77ddbb2e10804642cef5ef90f176dac9e9087f30b9ecf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1f6e9f9bc9b053cb4aa3f223ace68dfba5fd2ef3f3a9e282201e18f2b5640dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b74451160f802338502e0eecec63fc329b103880b5f7eb74f151a35c8ec444b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48f3e9fc45b5b5c5c6895850ade2b9f18c32c72790b9f0ab8339d3fe8d4ea905)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bada1a86c7cb89048108fd28400e0ebf22cc2802cf4756fa95a8020c2db270f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceV1Metadata]:
        return typing.cast(typing.Optional[ServiceV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca77346322cad9f236b633deea1271ec7472adc7cd72ebd54f2e1000bd962ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "allocate_load_balancer_node_ports": "allocateLoadBalancerNodePorts",
        "cluster_ip": "clusterIp",
        "cluster_ips": "clusterIps",
        "external_ips": "externalIps",
        "external_name": "externalName",
        "external_traffic_policy": "externalTrafficPolicy",
        "health_check_node_port": "healthCheckNodePort",
        "internal_traffic_policy": "internalTrafficPolicy",
        "ip_families": "ipFamilies",
        "ip_family_policy": "ipFamilyPolicy",
        "load_balancer_class": "loadBalancerClass",
        "load_balancer_ip": "loadBalancerIp",
        "load_balancer_source_ranges": "loadBalancerSourceRanges",
        "port": "port",
        "publish_not_ready_addresses": "publishNotReadyAddresses",
        "selector": "selector",
        "session_affinity": "sessionAffinity",
        "session_affinity_config": "sessionAffinityConfig",
        "type": "type",
    },
)
class ServiceV1Spec:
    def __init__(
        self,
        *,
        allocate_load_balancer_node_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cluster_ip: typing.Optional[builtins.str] = None,
        cluster_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        external_traffic_policy: typing.Optional[builtins.str] = None,
        health_check_node_port: typing.Optional[jsii.Number] = None,
        internal_traffic_policy: typing.Optional[builtins.str] = None,
        ip_families: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_family_policy: typing.Optional[builtins.str] = None,
        load_balancer_class: typing.Optional[builtins.str] = None,
        load_balancer_ip: typing.Optional[builtins.str] = None,
        load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceV1SpecPort", typing.Dict[builtins.str, typing.Any]]]]] = None,
        publish_not_ready_addresses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        session_affinity_config: typing.Optional[typing.Union["ServiceV1SpecSessionAffinityConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allocate_load_balancer_node_ports: Defines if ``NodePorts`` will be automatically allocated for services with type ``LoadBalancer``. It may be set to ``false`` if the cluster load-balancer does not rely on ``NodePorts``. If the caller requests specific ``NodePorts`` (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type ``LoadBalancer``. Default is ``true``. More info: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#allocate_load_balancer_node_ports ServiceV1#allocate_load_balancer_node_ports}
        :param cluster_ip: The IP address of the service. It is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. ``None`` can be specified for headless services when proxying is not required. Ignored if type is ``ExternalName``. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#cluster_ip ServiceV1#cluster_ip}
        :param cluster_ips: List of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise creation of the service will fail. If this field is not specified, it will be initialized from the ``clusterIP`` field. If this field is specified, clients must ensure that ``clusterIPs[0]`` and ``clusterIP`` have the same value. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#cluster_ips ServiceV1#cluster_ips}
        :param external_ips: A list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_ips ServiceV1#external_ips}
        :param external_name: The external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid DNS name and requires ``type`` to be ``ExternalName``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_name ServiceV1#external_name}
        :param external_traffic_policy: Denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. ``Local`` preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. ``Cluster`` obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading. More info: https://kubernetes.io/docs/tutorials/services/source-ip/ Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_traffic_policy ServiceV1#external_traffic_policy}
        :param health_check_node_port: Specifies the Healthcheck NodePort for the service. Only effects when type is set to ``LoadBalancer`` and external_traffic_policy is set to ``Local``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#health_check_node_port ServiceV1#health_check_node_port}
        :param internal_traffic_policy: Specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only. ``Cluster`` routes internal traffic to a Service to all endpoints. ``Local`` routes traffic to node-local endpoints only, traffic is dropped if no node-local endpoints are ready. The default value is ``Cluster``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#internal_traffic_policy ServiceV1#internal_traffic_policy}
        :param ip_families: IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#ip_families ServiceV1#ip_families}
        :param ip_family_policy: IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#ip_family_policy ServiceV1#ip_family_policy}
        :param load_balancer_class: The class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix. This field can only be set when the Service type is ``LoadBalancer``. If not set, the default load balancer implementation is used. This field can only be set when creating or updating a Service to type ``LoadBalancer``. More info: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_class ServiceV1#load_balancer_class}
        :param load_balancer_ip: Only applies to ``type = LoadBalancer``. LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying this field when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_ip ServiceV1#load_balancer_ip}
        :param load_balancer_source_ranges: If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature. More info: http://kubernetes.io/docs/user-guide/services-firewalls Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_source_ranges ServiceV1#load_balancer_source_ranges}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#port ServiceV1#port}
        :param publish_not_ready_addresses: When set to true, indicates that DNS implementations must publish the ``notReadyAddresses`` of subsets for the Endpoints associated with the Service. The default value is ``false``. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate ``SRV`` records for its Pods without respect to their readiness for purpose of peer discovery. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#publish_not_ready_addresses ServiceV1#publish_not_ready_addresses}
        :param selector: Route service traffic to pods with label keys and values matching this selector. Only applies to types ``ClusterIP``, ``NodePort``, and ``LoadBalancer``. More info: http://kubernetes.io/docs/user-guide/services#overview Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#selector ServiceV1#selector}
        :param session_affinity: Used to maintain session affinity. Supports ``ClientIP`` and ``None``. Defaults to ``None``. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#session_affinity ServiceV1#session_affinity}
        :param session_affinity_config: session_affinity_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#session_affinity_config ServiceV1#session_affinity_config}
        :param type: Determines how the service is exposed. Defaults to ``ClusterIP``. Valid options are ``ExternalName``, ``ClusterIP``, ``NodePort``, and ``LoadBalancer``. ``ExternalName`` maps to the specified ``external_name``. More info: http://kubernetes.io/docs/user-guide/services#overview Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#type ServiceV1#type}
        '''
        if isinstance(session_affinity_config, dict):
            session_affinity_config = ServiceV1SpecSessionAffinityConfig(**session_affinity_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57931a5d1f75564cecbfe42d2c1c09132deb81497a45ac32de9242c1a9d3418c)
            check_type(argname="argument allocate_load_balancer_node_ports", value=allocate_load_balancer_node_ports, expected_type=type_hints["allocate_load_balancer_node_ports"])
            check_type(argname="argument cluster_ip", value=cluster_ip, expected_type=type_hints["cluster_ip"])
            check_type(argname="argument cluster_ips", value=cluster_ips, expected_type=type_hints["cluster_ips"])
            check_type(argname="argument external_ips", value=external_ips, expected_type=type_hints["external_ips"])
            check_type(argname="argument external_name", value=external_name, expected_type=type_hints["external_name"])
            check_type(argname="argument external_traffic_policy", value=external_traffic_policy, expected_type=type_hints["external_traffic_policy"])
            check_type(argname="argument health_check_node_port", value=health_check_node_port, expected_type=type_hints["health_check_node_port"])
            check_type(argname="argument internal_traffic_policy", value=internal_traffic_policy, expected_type=type_hints["internal_traffic_policy"])
            check_type(argname="argument ip_families", value=ip_families, expected_type=type_hints["ip_families"])
            check_type(argname="argument ip_family_policy", value=ip_family_policy, expected_type=type_hints["ip_family_policy"])
            check_type(argname="argument load_balancer_class", value=load_balancer_class, expected_type=type_hints["load_balancer_class"])
            check_type(argname="argument load_balancer_ip", value=load_balancer_ip, expected_type=type_hints["load_balancer_ip"])
            check_type(argname="argument load_balancer_source_ranges", value=load_balancer_source_ranges, expected_type=type_hints["load_balancer_source_ranges"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument publish_not_ready_addresses", value=publish_not_ready_addresses, expected_type=type_hints["publish_not_ready_addresses"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument session_affinity", value=session_affinity, expected_type=type_hints["session_affinity"])
            check_type(argname="argument session_affinity_config", value=session_affinity_config, expected_type=type_hints["session_affinity_config"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allocate_load_balancer_node_ports is not None:
            self._values["allocate_load_balancer_node_ports"] = allocate_load_balancer_node_ports
        if cluster_ip is not None:
            self._values["cluster_ip"] = cluster_ip
        if cluster_ips is not None:
            self._values["cluster_ips"] = cluster_ips
        if external_ips is not None:
            self._values["external_ips"] = external_ips
        if external_name is not None:
            self._values["external_name"] = external_name
        if external_traffic_policy is not None:
            self._values["external_traffic_policy"] = external_traffic_policy
        if health_check_node_port is not None:
            self._values["health_check_node_port"] = health_check_node_port
        if internal_traffic_policy is not None:
            self._values["internal_traffic_policy"] = internal_traffic_policy
        if ip_families is not None:
            self._values["ip_families"] = ip_families
        if ip_family_policy is not None:
            self._values["ip_family_policy"] = ip_family_policy
        if load_balancer_class is not None:
            self._values["load_balancer_class"] = load_balancer_class
        if load_balancer_ip is not None:
            self._values["load_balancer_ip"] = load_balancer_ip
        if load_balancer_source_ranges is not None:
            self._values["load_balancer_source_ranges"] = load_balancer_source_ranges
        if port is not None:
            self._values["port"] = port
        if publish_not_ready_addresses is not None:
            self._values["publish_not_ready_addresses"] = publish_not_ready_addresses
        if selector is not None:
            self._values["selector"] = selector
        if session_affinity is not None:
            self._values["session_affinity"] = session_affinity
        if session_affinity_config is not None:
            self._values["session_affinity_config"] = session_affinity_config
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def allocate_load_balancer_node_ports(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defines if ``NodePorts`` will be automatically allocated for services with type ``LoadBalancer``.

        It may be set to ``false`` if the cluster load-balancer does not rely on ``NodePorts``.  If the caller requests specific ``NodePorts`` (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type ``LoadBalancer``. Default is ``true``. More info: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#allocate_load_balancer_node_ports ServiceV1#allocate_load_balancer_node_ports}
        '''
        result = self._values.get("allocate_load_balancer_node_ports")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cluster_ip(self) -> typing.Optional[builtins.str]:
        '''The IP address of the service.

        It is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. ``None`` can be specified for headless services when proxying is not required. Ignored if type is ``ExternalName``. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#cluster_ip ServiceV1#cluster_ip}
        '''
        result = self._values.get("cluster_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IP addresses assigned to this service, and are usually assigned randomly.

        If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise creation of the service will fail. If this field is not specified, it will be initialized from the ``clusterIP`` field. If this field is specified, clients must ensure that ``clusterIPs[0]`` and ``clusterIP`` have the same value. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#cluster_ips ServiceV1#cluster_ips}
        '''
        result = self._values.get("cluster_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IP addresses for which nodes in the cluster will also accept traffic for this service.

        These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_ips ServiceV1#external_ips}
        '''
        result = self._values.get("external_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_name(self) -> typing.Optional[builtins.str]:
        '''The external reference that kubedns or equivalent will return as a CNAME record for this service.

        No proxying will be involved. Must be a valid DNS name and requires ``type`` to be ``ExternalName``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_name ServiceV1#external_name}
        '''
        result = self._values.get("external_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_traffic_policy(self) -> typing.Optional[builtins.str]:
        '''Denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints.

        ``Local`` preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. ``Cluster`` obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading. More info: https://kubernetes.io/docs/tutorials/services/source-ip/

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#external_traffic_policy ServiceV1#external_traffic_policy}
        '''
        result = self._values.get("external_traffic_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_node_port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the Healthcheck NodePort for the service.

        Only effects when type is set to ``LoadBalancer`` and external_traffic_policy is set to ``Local``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#health_check_node_port ServiceV1#health_check_node_port}
        '''
        result = self._values.get("health_check_node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def internal_traffic_policy(self) -> typing.Optional[builtins.str]:
        '''Specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only.

        ``Cluster`` routes internal traffic to a Service to all endpoints. ``Local`` routes traffic to node-local endpoints only, traffic is dropped if no node-local endpoints are ready. The default value is ``Cluster``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#internal_traffic_policy ServiceV1#internal_traffic_policy}
        '''
        result = self._values.get("internal_traffic_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_families(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#ip_families ServiceV1#ip_families}
        '''
        result = self._values.get("ip_families")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_family_policy(self) -> typing.Optional[builtins.str]:
        '''IPFamilyPolicy represents the dual-stack-ness requested or required by this Service.

        If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#ip_family_policy ServiceV1#ip_family_policy}
        '''
        result = self._values.get("ip_family_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_class(self) -> typing.Optional[builtins.str]:
        '''The class of the load balancer implementation this Service belongs to.

        If specified, the value of this field must be a label-style identifier, with an optional prefix. This field can only be set when the Service type is ``LoadBalancer``. If not set, the default load balancer implementation is used. This field can only be set when creating or updating a Service to type ``LoadBalancer``. More info: https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_class ServiceV1#load_balancer_class}
        '''
        result = self._values.get("load_balancer_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_ip(self) -> typing.Optional[builtins.str]:
        '''Only applies to ``type = LoadBalancer``.

        LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying this field when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_ip ServiceV1#load_balancer_ip}
        '''
        result = self._values.get("load_balancer_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_source_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs.

        This field will be ignored if the cloud-provider does not support the feature. More info: http://kubernetes.io/docs/user-guide/services-firewalls

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#load_balancer_source_ranges ServiceV1#load_balancer_source_ranges}
        '''
        result = self._values.get("load_balancer_source_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceV1SpecPort"]]]:
        '''port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#port ServiceV1#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceV1SpecPort"]]], result)

    @builtins.property
    def publish_not_ready_addresses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When set to true, indicates that DNS implementations must publish the ``notReadyAddresses`` of subsets for the Endpoints associated with the Service.

        The default value is ``false``. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate ``SRV`` records for its Pods without respect to their readiness for purpose of peer discovery.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#publish_not_ready_addresses ServiceV1#publish_not_ready_addresses}
        '''
        result = self._values.get("publish_not_ready_addresses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def selector(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Route service traffic to pods with label keys and values matching this selector.

        Only applies to types ``ClusterIP``, ``NodePort``, and ``LoadBalancer``. More info: http://kubernetes.io/docs/user-guide/services#overview

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#selector ServiceV1#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def session_affinity(self) -> typing.Optional[builtins.str]:
        '''Used to maintain session affinity. Supports ``ClientIP`` and ``None``. Defaults to ``None``. More info: http://kubernetes.io/docs/user-guide/services#virtual-ips-and-service-proxies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#session_affinity ServiceV1#session_affinity}
        '''
        result = self._values.get("session_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_affinity_config(
        self,
    ) -> typing.Optional["ServiceV1SpecSessionAffinityConfig"]:
        '''session_affinity_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#session_affinity_config ServiceV1#session_affinity_config}
        '''
        result = self._values.get("session_affinity_config")
        return typing.cast(typing.Optional["ServiceV1SpecSessionAffinityConfig"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Determines how the service is exposed.

        Defaults to ``ClusterIP``. Valid options are ``ExternalName``, ``ClusterIP``, ``NodePort``, and ``LoadBalancer``. ``ExternalName`` maps to the specified ``external_name``. More info: http://kubernetes.io/docs/user-guide/services#overview

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#type ServiceV1#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1SpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d13830c4736c61db3a45019fc66085c777afc106771c0c7376052e5d06682b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPort")
    def put_port(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceV1SpecPort", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__338882ec62234099ecb4b2979986c90c07d2e9840ef67e8448347a88d0e9caa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPort", [value]))

    @jsii.member(jsii_name="putSessionAffinityConfig")
    def put_session_affinity_config(
        self,
        *,
        client_ip: typing.Optional[typing.Union["ServiceV1SpecSessionAffinityConfigClientIp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_ip: client_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#client_ip ServiceV1#client_ip}
        '''
        value = ServiceV1SpecSessionAffinityConfig(client_ip=client_ip)

        return typing.cast(None, jsii.invoke(self, "putSessionAffinityConfig", [value]))

    @jsii.member(jsii_name="resetAllocateLoadBalancerNodePorts")
    def reset_allocate_load_balancer_node_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocateLoadBalancerNodePorts", []))

    @jsii.member(jsii_name="resetClusterIp")
    def reset_cluster_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIp", []))

    @jsii.member(jsii_name="resetClusterIps")
    def reset_cluster_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIps", []))

    @jsii.member(jsii_name="resetExternalIps")
    def reset_external_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalIps", []))

    @jsii.member(jsii_name="resetExternalName")
    def reset_external_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalName", []))

    @jsii.member(jsii_name="resetExternalTrafficPolicy")
    def reset_external_traffic_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalTrafficPolicy", []))

    @jsii.member(jsii_name="resetHealthCheckNodePort")
    def reset_health_check_node_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckNodePort", []))

    @jsii.member(jsii_name="resetInternalTrafficPolicy")
    def reset_internal_traffic_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalTrafficPolicy", []))

    @jsii.member(jsii_name="resetIpFamilies")
    def reset_ip_families(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpFamilies", []))

    @jsii.member(jsii_name="resetIpFamilyPolicy")
    def reset_ip_family_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpFamilyPolicy", []))

    @jsii.member(jsii_name="resetLoadBalancerClass")
    def reset_load_balancer_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerClass", []))

    @jsii.member(jsii_name="resetLoadBalancerIp")
    def reset_load_balancer_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerIp", []))

    @jsii.member(jsii_name="resetLoadBalancerSourceRanges")
    def reset_load_balancer_source_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerSourceRanges", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPublishNotReadyAddresses")
    def reset_publish_not_ready_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishNotReadyAddresses", []))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @jsii.member(jsii_name="resetSessionAffinity")
    def reset_session_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinity", []))

    @jsii.member(jsii_name="resetSessionAffinityConfig")
    def reset_session_affinity_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityConfig", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> "ServiceV1SpecPortList":
        return typing.cast("ServiceV1SpecPortList", jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityConfig")
    def session_affinity_config(
        self,
    ) -> "ServiceV1SpecSessionAffinityConfigOutputReference":
        return typing.cast("ServiceV1SpecSessionAffinityConfigOutputReference", jsii.get(self, "sessionAffinityConfig"))

    @builtins.property
    @jsii.member(jsii_name="allocateLoadBalancerNodePortsInput")
    def allocate_load_balancer_node_ports_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allocateLoadBalancerNodePortsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIpInput")
    def cluster_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIpInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIpsInput")
    def cluster_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusterIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIpsInput")
    def external_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="externalNameInput")
    def external_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="externalTrafficPolicyInput")
    def external_traffic_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalTrafficPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckNodePortInput")
    def health_check_node_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckNodePortInput"))

    @builtins.property
    @jsii.member(jsii_name="internalTrafficPolicyInput")
    def internal_traffic_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "internalTrafficPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="ipFamiliesInput")
    def ip_families_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipFamiliesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipFamilyPolicyInput")
    def ip_family_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipFamilyPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerClassInput")
    def load_balancer_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerClassInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerIpInput")
    def load_balancer_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerIpInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSourceRangesInput")
    def load_balancer_source_ranges_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerSourceRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceV1SpecPort"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceV1SpecPort"]]], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="publishNotReadyAddressesInput")
    def publish_not_ready_addresses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publishNotReadyAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityConfigInput")
    def session_affinity_config_input(
        self,
    ) -> typing.Optional["ServiceV1SpecSessionAffinityConfig"]:
        return typing.cast(typing.Optional["ServiceV1SpecSessionAffinityConfig"], jsii.get(self, "sessionAffinityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityInput")
    def session_affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="allocateLoadBalancerNodePorts")
    def allocate_load_balancer_node_ports(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allocateLoadBalancerNodePorts"))

    @allocate_load_balancer_node_ports.setter
    def allocate_load_balancer_node_ports(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba1ce5039c9f047cc83e4783aafc8a8ea15f639a01cbf32aa37c5e47722b451a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocateLoadBalancerNodePorts", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIp")
    def cluster_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIp"))

    @cluster_ip.setter
    def cluster_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8bafe29f8c7f99c029378327f8dffab44c54bedeba6edb00be6d27e64c9a3af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIp", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIps")
    def cluster_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clusterIps"))

    @cluster_ips.setter
    def cluster_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af4851181a5dd66468aba9c399c08add916040b02075e5df1174991d2539dbf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIps", value)

    @builtins.property
    @jsii.member(jsii_name="externalIps")
    def external_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalIps"))

    @external_ips.setter
    def external_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f505695d03b707a62efbabd9be0b57b11489b145249fbbe5766251aa45d15ab1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalIps", value)

    @builtins.property
    @jsii.member(jsii_name="externalName")
    def external_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalName"))

    @external_name.setter
    def external_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e68a856bda02a6d9429bc2e847a8441221bc1f1f9050923047b2ad6ade6037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalName", value)

    @builtins.property
    @jsii.member(jsii_name="externalTrafficPolicy")
    def external_traffic_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalTrafficPolicy"))

    @external_traffic_policy.setter
    def external_traffic_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c3131c8a5c8f0af8fe6f60cf2f6a79358789fe13e55cd6bcbafc7c9da5b77d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalTrafficPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckNodePort")
    def health_check_node_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckNodePort"))

    @health_check_node_port.setter
    def health_check_node_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3f1b487ba4b33565a42dd62b65e557d4dde107ecf8227d6dd39231634c918e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckNodePort", value)

    @builtins.property
    @jsii.member(jsii_name="internalTrafficPolicy")
    def internal_traffic_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalTrafficPolicy"))

    @internal_traffic_policy.setter
    def internal_traffic_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa55b3ab0cd429531fbb52afff42cdf370bc28d397b982d9f559bfb87d6ba56e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalTrafficPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="ipFamilies")
    def ip_families(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipFamilies"))

    @ip_families.setter
    def ip_families(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23bac337517be13400d78def5ddf8b146e55a5512ad9e8db370b88595118280f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipFamilies", value)

    @builtins.property
    @jsii.member(jsii_name="ipFamilyPolicy")
    def ip_family_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipFamilyPolicy"))

    @ip_family_policy.setter
    def ip_family_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f3cb005c9e6d978c5707bc40403c58cc6515638d1c04089ee1a50ca67d6701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipFamilyPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerClass")
    def load_balancer_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerClass"))

    @load_balancer_class.setter
    def load_balancer_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8c587229ff91daab47dfae0cce10c5b19d20d3f1df6e4d6e8ecea9220d12221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerClass", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerIp")
    def load_balancer_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerIp"))

    @load_balancer_ip.setter
    def load_balancer_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d51bd6d2cd2e68daf149941918bc2532cb1543fc4b0a394193919f6180973a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerIp", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSourceRanges")
    def load_balancer_source_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerSourceRanges"))

    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c85f1cf68f4473100d260be49a13f2e4af75b3e1ecc36091c974d46c3fdec51e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerSourceRanges", value)

    @builtins.property
    @jsii.member(jsii_name="publishNotReadyAddresses")
    def publish_not_ready_addresses(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publishNotReadyAddresses"))

    @publish_not_ready_addresses.setter
    def publish_not_ready_addresses(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a199e8163f75e091d78e4e4278914cf30f19d4049d4ca59897b87974aea4ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishNotReadyAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67913347722a3bb57374c04b65c765a57c5341fce2f689e9290c3bb5fdf65c37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinity")
    def session_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionAffinity"))

    @session_affinity.setter
    def session_affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa2b9c1993bea800bfbf396da1751c909cbf66dd220061cd86afd68ea3d5e6eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897c5bca050118cf43abdd14a14bd9ed51ba2298ce3886677644a989bec994b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceV1Spec]:
        return typing.cast(typing.Optional[ServiceV1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceV1Spec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb82c5f982152b474927f44d3609135230e6e090e5f0dfb6bb369b629382571d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1SpecPort",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "app_protocol": "appProtocol",
        "name": "name",
        "node_port": "nodePort",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class ServiceV1SpecPort:
    def __init__(
        self,
        *,
        port: jsii.Number,
        app_protocol: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The port that will be exposed by this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#port ServiceV1#port}
        :param app_protocol: The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#app_protocol ServiceV1#app_protocol}
        :param name: The name of this port within the service. All ports within the service must have unique names. Optional if only one ServicePort is defined on this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#name ServiceV1#name}
        :param node_port: The port on each node on which this service is exposed when ``type`` is ``NodePort`` or ``LoadBalancer``. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ``type`` of this service requires one. More info: http://kubernetes.io/docs/user-guide/services#type--nodeport Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#node_port ServiceV1#node_port}
        :param protocol: The IP protocol for this port. Supports ``TCP`` and ``UDP``. Default is ``TCP``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#protocol ServiceV1#protocol}
        :param target_port: Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. This field is ignored for services with ``cluster_ip = "None"``. More info: http://kubernetes.io/docs/user-guide/services#defining-a-service Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#target_port ServiceV1#target_port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a597adea3c6b2bac8bbe46da236b1dfbaeb7793fa1d8d17b817ee6b922ddc9)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument app_protocol", value=app_protocol, expected_type=type_hints["app_protocol"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_port", value=node_port, expected_type=type_hints["node_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
        }
        if app_protocol is not None:
            self._values["app_protocol"] = app_protocol
        if name is not None:
            self._values["name"] = name
        if node_port is not None:
            self._values["node_port"] = node_port
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port that will be exposed by this service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#port ServiceV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def app_protocol(self) -> typing.Optional[builtins.str]:
        '''The application protocol for this port.

        This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#app_protocol ServiceV1#app_protocol}
        '''
        result = self._values.get("app_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this port within the service.

        All ports within the service must have unique names. Optional if only one ServicePort is defined on this service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#name ServiceV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''The port on each node on which this service is exposed when ``type`` is ``NodePort`` or ``LoadBalancer``.

        Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ``type`` of this service requires one. More info: http://kubernetes.io/docs/user-guide/services#type--nodeport

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#node_port ServiceV1#node_port}
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The IP protocol for this port. Supports ``TCP`` and ``UDP``. Default is ``TCP``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#protocol ServiceV1#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[builtins.str]:
        '''Number or name of the port to access on the pods targeted by the service.

        Number must be in the range 1 to 65535. This field is ignored for services with ``cluster_ip = "None"``. More info: http://kubernetes.io/docs/user-guide/services#defining-a-service

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#target_port ServiceV1#target_port}
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1SpecPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1SpecPortList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1SpecPortList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5381d57dbf1a6b474cae920bb39ffbbd260d26c59d87bf7d4bf5c55840865617)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceV1SpecPortOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4aec442ce22e902d8a54937515adc0cb8514a4dcd0b5718d0bab7203dc4b808)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceV1SpecPortOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9aca8604e6162dcc7d5ba904b18b0f08c95fb948c94e50b86e45e25838981d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef191e3c440f27cb11bb05f65978560b7d74b811e353e437102ed58efe618b2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71c0f3810c56a3fe10e479e39b9595b2caac331f7466d96dad3f207f1a0a7a7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceV1SpecPort]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceV1SpecPort]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceV1SpecPort]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82a51815862317d2eff35ea7980a58f2b74fd00506c71cf5d0c940b7b2187d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceV1SpecPortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1SpecPortOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0669d0a4c79588d993c57eba78861824c5cc658f8672ce38ef44a10f27c5a92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAppProtocol")
    def reset_app_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppProtocol", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNodePort")
    def reset_node_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetTargetPort")
    def reset_target_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPort", []))

    @builtins.property
    @jsii.member(jsii_name="appProtocolInput")
    def app_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePortInput")
    def node_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nodePortInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortInput")
    def target_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPortInput"))

    @builtins.property
    @jsii.member(jsii_name="appProtocol")
    def app_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appProtocol"))

    @app_protocol.setter
    def app_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__469a7b267d43a5aa9bdd6faa5f97bc7d99b76e64f4e4a74544ec0b37b01eed88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63c6fe8e19c61978daf958fcda1aa1228b1215842d8fb0d9f19ba0d88a5fcb69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodePort")
    def node_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nodePort"))

    @node_port.setter
    def node_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad33ef490252cf1d3ecd80f83da556f3112d60f00c813ac9c8cbc5223628537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodePort", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25b5bbcfbfc336b0bbd65c8d6b9809b795dc8ea4ecc2a61caf733eaaee90792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16595b67e53cf95cacc801e7e1160a3aad48e34350be1589ee5a9172caab75be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="targetPort")
    def target_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPort"))

    @target_port.setter
    def target_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945ddb8ff24d3fd647a49cbdd449a764bbb7073331fdffe1cac1cacbd8e9af8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceV1SpecPort, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceV1SpecPort, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceV1SpecPort, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de6e5373320f107a6128a6897ef09831ae4a4574e9882a4d566389847f268c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1SpecSessionAffinityConfig",
    jsii_struct_bases=[],
    name_mapping={"client_ip": "clientIp"},
)
class ServiceV1SpecSessionAffinityConfig:
    def __init__(
        self,
        *,
        client_ip: typing.Optional[typing.Union["ServiceV1SpecSessionAffinityConfigClientIp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_ip: client_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#client_ip ServiceV1#client_ip}
        '''
        if isinstance(client_ip, dict):
            client_ip = ServiceV1SpecSessionAffinityConfigClientIp(**client_ip)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5eb509927d6130d1594c8d5594658befbc2c0de367969e976c885e17ab0e316)
            check_type(argname="argument client_ip", value=client_ip, expected_type=type_hints["client_ip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_ip is not None:
            self._values["client_ip"] = client_ip

    @builtins.property
    def client_ip(
        self,
    ) -> typing.Optional["ServiceV1SpecSessionAffinityConfigClientIp"]:
        '''client_ip block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#client_ip ServiceV1#client_ip}
        '''
        result = self._values.get("client_ip")
        return typing.cast(typing.Optional["ServiceV1SpecSessionAffinityConfigClientIp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1SpecSessionAffinityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1SpecSessionAffinityConfigClientIp",
    jsii_struct_bases=[],
    name_mapping={"timeout_seconds": "timeoutSeconds"},
)
class ServiceV1SpecSessionAffinityConfigClientIp:
    def __init__(self, *, timeout_seconds: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param timeout_seconds: Specifies the seconds of ``ClientIP`` type session sticky time. The value must be > 0 and <= 86400(for 1 day) if ``ServiceAffinity`` == ``ClientIP``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#timeout_seconds ServiceV1#timeout_seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217cf177a9b97fddb7db9b64565c7cc094d32434ac45c6c7e10ddc9b93ed5257)
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Specifies the seconds of ``ClientIP`` type session sticky time.

        The value must be > 0 and <= 86400(for 1 day) if ``ServiceAffinity`` == ``ClientIP``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#timeout_seconds ServiceV1#timeout_seconds}
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1SpecSessionAffinityConfigClientIp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1SpecSessionAffinityConfigClientIpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1SpecSessionAffinityConfigClientIpOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f959704307c16be9f8c16851d3e4d4efb6f8c9ae88a77d9e972ccd2f6a813a31)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86203d136da53cdb81167ba742d9d235d52e37b12ae66bb33b9d1b6bb41f7e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceV1SpecSessionAffinityConfigClientIp]:
        return typing.cast(typing.Optional[ServiceV1SpecSessionAffinityConfigClientIp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceV1SpecSessionAffinityConfigClientIp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb40d0eaea4379ae0f09ef62a79bac03937847c750c173b666d8cf4a6f77e755)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceV1SpecSessionAffinityConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1SpecSessionAffinityConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b043863fcf0dd3b0d2b9d1998a555fe0b441e7c4a4b776185a81e4afcefe5c53)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientIp")
    def put_client_ip(
        self,
        *,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param timeout_seconds: Specifies the seconds of ``ClientIP`` type session sticky time. The value must be > 0 and <= 86400(for 1 day) if ``ServiceAffinity`` == ``ClientIP``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#timeout_seconds ServiceV1#timeout_seconds}
        '''
        value = ServiceV1SpecSessionAffinityConfigClientIp(
            timeout_seconds=timeout_seconds
        )

        return typing.cast(None, jsii.invoke(self, "putClientIp", [value]))

    @jsii.member(jsii_name="resetClientIp")
    def reset_client_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientIp", []))

    @builtins.property
    @jsii.member(jsii_name="clientIp")
    def client_ip(self) -> ServiceV1SpecSessionAffinityConfigClientIpOutputReference:
        return typing.cast(ServiceV1SpecSessionAffinityConfigClientIpOutputReference, jsii.get(self, "clientIp"))

    @builtins.property
    @jsii.member(jsii_name="clientIpInput")
    def client_ip_input(
        self,
    ) -> typing.Optional[ServiceV1SpecSessionAffinityConfigClientIp]:
        return typing.cast(typing.Optional[ServiceV1SpecSessionAffinityConfigClientIp], jsii.get(self, "clientIpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceV1SpecSessionAffinityConfig]:
        return typing.cast(typing.Optional[ServiceV1SpecSessionAffinityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceV1SpecSessionAffinityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079954ca779907ecf6876f20b64d6c14bdeb5bc29e26b0a394c99f8d8a3d28fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1Status",
    jsii_struct_bases=[],
    name_mapping={},
)
class ServiceV1Status:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1Status(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1StatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1StatusList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf20c507497e778ff6b71b421cf55c20a43f6ce62e03270182054c2eaabf715)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceV1StatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a59aeafe272ed5f82b4982b18e0b74e0b8094a16319077271b093df7ff689e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceV1StatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d58a5e823bd208a350150755de17961abfd1e70610ed5fdfe89fc132e58ed30c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c81d569bc8814a8981ec7acc5e850d869bf88d39b777b1e5bb5b41241bd0582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6790b5e556914c1ddc792db32afcb73f62e1595214df59d8794adce05f1ba289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1StatusLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={},
)
class ServiceV1StatusLoadBalancer:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1StatusLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1StatusLoadBalancerIngress",
    jsii_struct_bases=[],
    name_mapping={},
)
class ServiceV1StatusLoadBalancerIngress:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1StatusLoadBalancerIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1StatusLoadBalancerIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1StatusLoadBalancerIngressList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49195be5fd443167e3b14d1a3439134a0c63692fa8a645b9deca93c86aff4dbf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceV1StatusLoadBalancerIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5c956baeb7592e55f24a88cc3f3f9780a8a914e838c4e951df00a4b5fba8b1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceV1StatusLoadBalancerIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21cb82df7f85928a9351f12447a055aecb40f94d7efddb82bb366de007d24c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__580463350e8479281bbe38256d9b662bb5604e588646d2172de6dad7cf29dee9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0cc8d746521dfa5c56a68131d2bf72a787126098f49c3f77fec1b87616b6ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ServiceV1StatusLoadBalancerIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1StatusLoadBalancerIngressOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e057c5adaa69fd54940fdb4b003121b086684333172564d784741fb106604ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceV1StatusLoadBalancerIngress]:
        return typing.cast(typing.Optional[ServiceV1StatusLoadBalancerIngress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceV1StatusLoadBalancerIngress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab9460240931c23d2ba53b0e7c97f9509aa26f8a44d69348765fa4b84e5e6034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceV1StatusLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1StatusLoadBalancerList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d409976b1f2d378ea78c91fb2014155db90f40675040b35e8b4e1a5a6c8648)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceV1StatusLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ff82ab2a62afd94df7dd1c679c67921027413c01ad79b43f87432348227386)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceV1StatusLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d536476c335314c0b53d63bd595e585eeded05baa38c9b20d9a32de0e09bb05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510ba8c475f66bd5a1de7c869b7477a7b4cbbaefad5401c35cecdba5f74a7583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91343081d880b514427a7ca2c47ab2e36c450aa1177608a462be5a4c016a399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ServiceV1StatusLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1StatusLoadBalancerOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd74440194406a8fffe532bb340856ad1cb0e02c12b8199d8b80fc55da0b60b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> ServiceV1StatusLoadBalancerIngressList:
        return typing.cast(ServiceV1StatusLoadBalancerIngressList, jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceV1StatusLoadBalancer]:
        return typing.cast(typing.Optional[ServiceV1StatusLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceV1StatusLoadBalancer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__815b93094439cb17351caf30ad976d1f6cecb1e7ccab8019f0f119c6370f9fc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceV1StatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1StatusOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90f00d610f7487cca4a1f445f7018c9947f012039b4203cea6aec4df7e17f315)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> ServiceV1StatusLoadBalancerList:
        return typing.cast(ServiceV1StatusLoadBalancerList, jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceV1Status]:
        return typing.cast(typing.Optional[ServiceV1Status], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceV1Status]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__263cd6da7586417a484b3e1622224933e026ac55da873ee2c85e684a3cc04c09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.serviceV1.ServiceV1Timeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class ServiceV1Timeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#create ServiceV1#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c8717dd265fb670d4f4a5533d8aa60c54adef1043dd33378d4959ad235eb77)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/service_v1#create ServiceV1#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceV1Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceV1TimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.serviceV1.ServiceV1TimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c1f85fa09df1ef2d8a40f31a8ef36c0b327bab89cb1cea369ef679dbd5a231)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb05c5d01a825abe4886edcf4f3ed203914b43fff2ee960d5e3ce595e407612a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceV1Timeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceV1Timeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceV1Timeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__808c4e1db53f145c38208f6212e06f0a2a0fd19deb21bf136b7810e1525fa8d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceV1",
    "ServiceV1Config",
    "ServiceV1Metadata",
    "ServiceV1MetadataOutputReference",
    "ServiceV1Spec",
    "ServiceV1SpecOutputReference",
    "ServiceV1SpecPort",
    "ServiceV1SpecPortList",
    "ServiceV1SpecPortOutputReference",
    "ServiceV1SpecSessionAffinityConfig",
    "ServiceV1SpecSessionAffinityConfigClientIp",
    "ServiceV1SpecSessionAffinityConfigClientIpOutputReference",
    "ServiceV1SpecSessionAffinityConfigOutputReference",
    "ServiceV1Status",
    "ServiceV1StatusList",
    "ServiceV1StatusLoadBalancer",
    "ServiceV1StatusLoadBalancerIngress",
    "ServiceV1StatusLoadBalancerIngressList",
    "ServiceV1StatusLoadBalancerIngressOutputReference",
    "ServiceV1StatusLoadBalancerList",
    "ServiceV1StatusLoadBalancerOutputReference",
    "ServiceV1StatusOutputReference",
    "ServiceV1Timeouts",
    "ServiceV1TimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__0f5eade294a227f8f4879545dc4710488c43c58a17edefe6263b3d0d3c9b230f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ServiceV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ServiceV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ServiceV1Timeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8201040bcc0284ccd42cb63f8d5962e841b05bceb6f3c9b705d0ffc48ac2c56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1832b15888659c6e4bc39711136fae86e4389d2f0703f66acaaefd3d3a199f6a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd441e02c1cd57f6078718358bbcc4e69df8dfd53bafd3a0732a885c878ec36d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ServiceV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ServiceV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ServiceV1Timeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc54ca5ccc09a88878579bbf1011c20c088197084adf43bb3aaf33ece257a9ad(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a3780831abc7938469caeff430578feb90af0cee78cd9854d006a78b1a611b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe35e42a823910223b77ddbb2e10804642cef5ef90f176dac9e9087f30b9ecf1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f6e9f9bc9b053cb4aa3f223ace68dfba5fd2ef3f3a9e282201e18f2b5640dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b74451160f802338502e0eecec63fc329b103880b5f7eb74f151a35c8ec444b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f3e9fc45b5b5c5c6895850ade2b9f18c32c72790b9f0ab8339d3fe8d4ea905(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bada1a86c7cb89048108fd28400e0ebf22cc2802cf4756fa95a8020c2db270f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca77346322cad9f236b633deea1271ec7472adc7cd72ebd54f2e1000bd962ab(
    value: typing.Optional[ServiceV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57931a5d1f75564cecbfe42d2c1c09132deb81497a45ac32de9242c1a9d3418c(
    *,
    allocate_load_balancer_node_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cluster_ip: typing.Optional[builtins.str] = None,
    cluster_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    external_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    external_name: typing.Optional[builtins.str] = None,
    external_traffic_policy: typing.Optional[builtins.str] = None,
    health_check_node_port: typing.Optional[jsii.Number] = None,
    internal_traffic_policy: typing.Optional[builtins.str] = None,
    ip_families: typing.Optional[typing.Sequence[builtins.str]] = None,
    ip_family_policy: typing.Optional[builtins.str] = None,
    load_balancer_class: typing.Optional[builtins.str] = None,
    load_balancer_ip: typing.Optional[builtins.str] = None,
    load_balancer_source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    port: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceV1SpecPort, typing.Dict[builtins.str, typing.Any]]]]] = None,
    publish_not_ready_addresses: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    session_affinity: typing.Optional[builtins.str] = None,
    session_affinity_config: typing.Optional[typing.Union[ServiceV1SpecSessionAffinityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d13830c4736c61db3a45019fc66085c777afc106771c0c7376052e5d06682b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__338882ec62234099ecb4b2979986c90c07d2e9840ef67e8448347a88d0e9caa3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceV1SpecPort, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba1ce5039c9f047cc83e4783aafc8a8ea15f639a01cbf32aa37c5e47722b451a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8bafe29f8c7f99c029378327f8dffab44c54bedeba6edb00be6d27e64c9a3af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af4851181a5dd66468aba9c399c08add916040b02075e5df1174991d2539dbf0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f505695d03b707a62efbabd9be0b57b11489b145249fbbe5766251aa45d15ab1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e68a856bda02a6d9429bc2e847a8441221bc1f1f9050923047b2ad6ade6037(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3131c8a5c8f0af8fe6f60cf2f6a79358789fe13e55cd6bcbafc7c9da5b77d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3f1b487ba4b33565a42dd62b65e557d4dde107ecf8227d6dd39231634c918e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa55b3ab0cd429531fbb52afff42cdf370bc28d397b982d9f559bfb87d6ba56e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23bac337517be13400d78def5ddf8b146e55a5512ad9e8db370b88595118280f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f3cb005c9e6d978c5707bc40403c58cc6515638d1c04089ee1a50ca67d6701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8c587229ff91daab47dfae0cce10c5b19d20d3f1df6e4d6e8ecea9220d12221(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d51bd6d2cd2e68daf149941918bc2532cb1543fc4b0a394193919f6180973a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85f1cf68f4473100d260be49a13f2e4af75b3e1ecc36091c974d46c3fdec51e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a199e8163f75e091d78e4e4278914cf30f19d4049d4ca59897b87974aea4ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67913347722a3bb57374c04b65c765a57c5341fce2f689e9290c3bb5fdf65c37(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2b9c1993bea800bfbf396da1751c909cbf66dd220061cd86afd68ea3d5e6eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897c5bca050118cf43abdd14a14bd9ed51ba2298ce3886677644a989bec994b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb82c5f982152b474927f44d3609135230e6e090e5f0dfb6bb369b629382571d(
    value: typing.Optional[ServiceV1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a597adea3c6b2bac8bbe46da236b1dfbaeb7793fa1d8d17b817ee6b922ddc9(
    *,
    port: jsii.Number,
    app_protocol: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    node_port: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    target_port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5381d57dbf1a6b474cae920bb39ffbbd260d26c59d87bf7d4bf5c55840865617(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4aec442ce22e902d8a54937515adc0cb8514a4dcd0b5718d0bab7203dc4b808(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9aca8604e6162dcc7d5ba904b18b0f08c95fb948c94e50b86e45e25838981d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef191e3c440f27cb11bb05f65978560b7d74b811e353e437102ed58efe618b2b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c0f3810c56a3fe10e479e39b9595b2caac331f7466d96dad3f207f1a0a7a7e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a51815862317d2eff35ea7980a58f2b74fd00506c71cf5d0c940b7b2187d81(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceV1SpecPort]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0669d0a4c79588d993c57eba78861824c5cc658f8672ce38ef44a10f27c5a92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__469a7b267d43a5aa9bdd6faa5f97bc7d99b76e64f4e4a74544ec0b37b01eed88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c6fe8e19c61978daf958fcda1aa1228b1215842d8fb0d9f19ba0d88a5fcb69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad33ef490252cf1d3ecd80f83da556f3112d60f00c813ac9c8cbc5223628537(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25b5bbcfbfc336b0bbd65c8d6b9809b795dc8ea4ecc2a61caf733eaaee90792(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16595b67e53cf95cacc801e7e1160a3aad48e34350be1589ee5a9172caab75be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945ddb8ff24d3fd647a49cbdd449a764bbb7073331fdffe1cac1cacbd8e9af8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6e5373320f107a6128a6897ef09831ae4a4574e9882a4d566389847f268c5b(
    value: typing.Optional[typing.Union[ServiceV1SpecPort, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5eb509927d6130d1594c8d5594658befbc2c0de367969e976c885e17ab0e316(
    *,
    client_ip: typing.Optional[typing.Union[ServiceV1SpecSessionAffinityConfigClientIp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217cf177a9b97fddb7db9b64565c7cc094d32434ac45c6c7e10ddc9b93ed5257(
    *,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f959704307c16be9f8c16851d3e4d4efb6f8c9ae88a77d9e972ccd2f6a813a31(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86203d136da53cdb81167ba742d9d235d52e37b12ae66bb33b9d1b6bb41f7e67(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb40d0eaea4379ae0f09ef62a79bac03937847c750c173b666d8cf4a6f77e755(
    value: typing.Optional[ServiceV1SpecSessionAffinityConfigClientIp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b043863fcf0dd3b0d2b9d1998a555fe0b441e7c4a4b776185a81e4afcefe5c53(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079954ca779907ecf6876f20b64d6c14bdeb5bc29e26b0a394c99f8d8a3d28fd(
    value: typing.Optional[ServiceV1SpecSessionAffinityConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf20c507497e778ff6b71b421cf55c20a43f6ce62e03270182054c2eaabf715(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a59aeafe272ed5f82b4982b18e0b74e0b8094a16319077271b093df7ff689e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d58a5e823bd208a350150755de17961abfd1e70610ed5fdfe89fc132e58ed30c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c81d569bc8814a8981ec7acc5e850d869bf88d39b777b1e5bb5b41241bd0582(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6790b5e556914c1ddc792db32afcb73f62e1595214df59d8794adce05f1ba289(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49195be5fd443167e3b14d1a3439134a0c63692fa8a645b9deca93c86aff4dbf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5c956baeb7592e55f24a88cc3f3f9780a8a914e838c4e951df00a4b5fba8b1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21cb82df7f85928a9351f12447a055aecb40f94d7efddb82bb366de007d24c45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__580463350e8479281bbe38256d9b662bb5604e588646d2172de6dad7cf29dee9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0cc8d746521dfa5c56a68131d2bf72a787126098f49c3f77fec1b87616b6ded(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e057c5adaa69fd54940fdb4b003121b086684333172564d784741fb106604ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab9460240931c23d2ba53b0e7c97f9509aa26f8a44d69348765fa4b84e5e6034(
    value: typing.Optional[ServiceV1StatusLoadBalancerIngress],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d409976b1f2d378ea78c91fb2014155db90f40675040b35e8b4e1a5a6c8648(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ff82ab2a62afd94df7dd1c679c67921027413c01ad79b43f87432348227386(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d536476c335314c0b53d63bd595e585eeded05baa38c9b20d9a32de0e09bb05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510ba8c475f66bd5a1de7c869b7477a7b4cbbaefad5401c35cecdba5f74a7583(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91343081d880b514427a7ca2c47ab2e36c450aa1177608a462be5a4c016a399(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd74440194406a8fffe532bb340856ad1cb0e02c12b8199d8b80fc55da0b60b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__815b93094439cb17351caf30ad976d1f6cecb1e7ccab8019f0f119c6370f9fc7(
    value: typing.Optional[ServiceV1StatusLoadBalancer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90f00d610f7487cca4a1f445f7018c9947f012039b4203cea6aec4df7e17f315(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263cd6da7586417a484b3e1622224933e026ac55da873ee2c85e684a3cc04c09(
    value: typing.Optional[ServiceV1Status],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c8717dd265fb670d4f4a5533d8aa60c54adef1043dd33378d4959ad235eb77(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c1f85fa09df1ef2d8a40f31a8ef36c0b327bab89cb1cea369ef679dbd5a231(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb05c5d01a825abe4886edcf4f3ed203914b43fff2ee960d5e3ce595e407612a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__808c4e1db53f145c38208f6212e06f0a2a0fd19deb21bf136b7810e1525fa8d8(
    value: typing.Optional[typing.Union[ServiceV1Timeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
