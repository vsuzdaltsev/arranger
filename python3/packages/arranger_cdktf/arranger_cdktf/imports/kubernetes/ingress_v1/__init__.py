'''
# `kubernetes_ingress_v1`

Refer to the Terraform Registory for docs: [`kubernetes_ingress_v1`](https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1).
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


class IngressV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1 kubernetes_ingress_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["IngressV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["IngressV1Timeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1 kubernetes_ingress_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#metadata IngressV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#spec IngressV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#id IngressV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#timeouts IngressV1#timeouts}
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#wait_for_load_balancer IngressV1#wait_for_load_balancer}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8158158d9052d8eed6b906e74f1787b3388d3d06eeba44f1e8d6bc802537f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IngressV1Config(
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#annotations IngressV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#generate_name IngressV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#labels IngressV1#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#namespace IngressV1#namespace}
        '''
        value = IngressV1Metadata(
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
        default_backend: typing.Optional[typing.Union["IngressV1SpecDefaultBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default_backend: default_backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#default_backend IngressV1#default_backend}
        :param ingress_class_name: IngressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the ``kubernetes.io/ingress.class`` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#ingress_class_name IngressV1#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#rule IngressV1#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#tls IngressV1#tls}
        '''
        value = IngressV1Spec(
            default_backend=default_backend,
            ingress_class_name=ingress_class_name,
            rule=rule,
            tls=tls,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#create IngressV1#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#delete IngressV1#delete}.
        '''
        value = IngressV1Timeouts(create=create, delete=delete)

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
    def metadata(self) -> "IngressV1MetadataOutputReference":
        return typing.cast("IngressV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "IngressV1SpecOutputReference":
        return typing.cast("IngressV1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "IngressV1StatusList":
        return typing.cast("IngressV1StatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "IngressV1TimeoutsOutputReference":
        return typing.cast("IngressV1TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["IngressV1Metadata"]:
        return typing.cast(typing.Optional["IngressV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["IngressV1Spec"]:
        return typing.cast(typing.Optional["IngressV1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["IngressV1Timeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["IngressV1Timeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__59a6c0cda575b81c824d85c30909fc74541fb1eaa78cd76f311828c23cb08181)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e13fff77d4100235564d056e4c8eaaf56d7db6d3579dc67f5eae6cd3717ba9ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForLoadBalancer", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1Config",
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
class IngressV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["IngressV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["IngressV1Timeouts", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#metadata IngressV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#spec IngressV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#id IngressV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#timeouts IngressV1#timeouts}
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#wait_for_load_balancer IngressV1#wait_for_load_balancer}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = IngressV1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = IngressV1Spec(**spec)
        if isinstance(timeouts, dict):
            timeouts = IngressV1Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56f471bac4bf92659dd5cd78c0140657b8bd36558f105e95ddefd4f2d4b0c891)
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
    def metadata(self) -> "IngressV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#metadata IngressV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("IngressV1Metadata", result)

    @builtins.property
    def spec(self) -> "IngressV1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#spec IngressV1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("IngressV1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#id IngressV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["IngressV1Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#timeouts IngressV1#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["IngressV1Timeouts"], result)

    @builtins.property
    def wait_for_load_balancer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#wait_for_load_balancer IngressV1#wait_for_load_balancer}
        '''
        result = self._values.get("wait_for_load_balancer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class IngressV1Metadata:
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#annotations IngressV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#generate_name IngressV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#labels IngressV1#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#namespace IngressV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a2184811dc6f73ff3c7fc1e56e184f800fb084f4e6c5166328ca31c0822850d)
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
        '''An unstructured key value map stored with the ingress that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#annotations IngressV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#generate_name IngressV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the ingress.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#labels IngressV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the ingress must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#namespace IngressV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f30acbc5e401b401c6c4de4c4c69c80a56f8c2642b66c353de7c6379a5faaa2e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__130b4fa11fe3313590c4946f3dd01d0a860937d8f199f9600c6acad56f16db99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acdfe5591a5826beb100c0fb802f5c33fc93d770fd7410a05c017fc847e00980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db148978e3b8cd16dd83ef854b39b137ebf51af340a650d0baeeb4cb0b3129fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3220f9eee0daa18364e69098dd29e2a59f5554c639f93e607fc51080d277cc4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a33423795c77b079d97272ed6c9cd3e2dc71fd7d0a4d9c5c954a4ef9217ab689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1Metadata]:
        return typing.cast(typing.Optional[IngressV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12be67ef98c195348d8b03c79c75392f0f679241e35d6655c99f1cde0632cc67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "default_backend": "defaultBackend",
        "ingress_class_name": "ingressClassName",
        "rule": "rule",
        "tls": "tls",
    },
)
class IngressV1Spec:
    def __init__(
        self,
        *,
        default_backend: typing.Optional[typing.Union["IngressV1SpecDefaultBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default_backend: default_backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#default_backend IngressV1#default_backend}
        :param ingress_class_name: IngressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the ``kubernetes.io/ingress.class`` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#ingress_class_name IngressV1#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#rule IngressV1#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#tls IngressV1#tls}
        '''
        if isinstance(default_backend, dict):
            default_backend = IngressV1SpecDefaultBackend(**default_backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e9e2c913015402635ce7e5883adc256307e0e55944e6982922eaba79157ec8)
            check_type(argname="argument default_backend", value=default_backend, expected_type=type_hints["default_backend"])
            check_type(argname="argument ingress_class_name", value=ingress_class_name, expected_type=type_hints["ingress_class_name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_backend is not None:
            self._values["default_backend"] = default_backend
        if ingress_class_name is not None:
            self._values["ingress_class_name"] = ingress_class_name
        if rule is not None:
            self._values["rule"] = rule
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def default_backend(self) -> typing.Optional["IngressV1SpecDefaultBackend"]:
        '''default_backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#default_backend IngressV1#default_backend}
        '''
        result = self._values.get("default_backend")
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackend"], result)

    @builtins.property
    def ingress_class_name(self) -> typing.Optional[builtins.str]:
        '''IngressClassName is the name of an IngressClass cluster resource.

        Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the ``kubernetes.io/ingress.class`` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#ingress_class_name IngressV1#ingress_class_name}
        '''
        result = self._values.get("ingress_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#rule IngressV1#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#tls IngressV1#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackend",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource", "service": "service"},
)
class IngressV1SpecDefaultBackend:
    def __init__(
        self,
        *,
        resource: typing.Optional[typing.Union["IngressV1SpecDefaultBackendResource", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["IngressV1SpecDefaultBackendService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        if isinstance(resource, dict):
            resource = IngressV1SpecDefaultBackendResource(**resource)
        if isinstance(service, dict):
            service = IngressV1SpecDefaultBackendService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50eb82eddbfbefc9fe5eaa79ce77ae977a9aff07ae404af25c19cafb26ca8118)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource is not None:
            self._values["resource"] = resource
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def resource(self) -> typing.Optional["IngressV1SpecDefaultBackendResource"]:
        '''resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendResource"], result)

    @builtins.property
    def service(self) -> typing.Optional["IngressV1SpecDefaultBackendService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38f2b93d69e8f94f7187e347caa5b0f163600365710dc62ab07c21be83f070e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putResource")
    def put_resource(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        value = IngressV1SpecDefaultBackendResource(
            api_group=api_group, kind=kind, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putResource", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecDefaultBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        value = IngressV1SpecDefaultBackendService(name=name, port=port)

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> "IngressV1SpecDefaultBackendResourceOutputReference":
        return typing.cast("IngressV1SpecDefaultBackendResourceOutputReference", jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "IngressV1SpecDefaultBackendServiceOutputReference":
        return typing.cast("IngressV1SpecDefaultBackendServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional["IngressV1SpecDefaultBackendResource"]:
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendResource"], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional["IngressV1SpecDefaultBackendService"]:
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackend]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c205045b80ac14a56d1242c0641463b5dfe8a9b4c86401bbe5221e1d3660538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendResource",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "kind": "kind", "name": "name"},
)
class IngressV1SpecDefaultBackendResource:
    def __init__(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d32c29e43a10a3bb07e63f042854aeca592615bd1aff315a545b8e11b497985d)
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_group": api_group,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_group(self) -> builtins.str:
        '''APIGroup is the group for the resource being referenced.

        If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        '''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the User to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackendResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c80e41eccfe9e7acd13254aca1a75145036e32b071480f91651140c0a1624b1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiGroupInput")
    def api_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40be8e44a0d2fe13f04f67289c9b94dba9caf5dd2f296f7a70ddc45a69ee5f0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f363a47990e4f6d9c939e663a731fc91893429b65664d8c347f50764c58f7d5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390d8d566d02fd4eb3e802b1d96ef08c8dce352412ec7f3f21bf53e116144c10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackendResource]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackendResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackendResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfc77f985d435d2ba933dde020c4ce5d3e461f2eb2fd97c793fb70b42ee7228d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "port": "port"},
)
class IngressV1SpecDefaultBackendService:
    def __init__(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecDefaultBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        if isinstance(port, dict):
            port = IngressV1SpecDefaultBackendServicePort(**port)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80db76e9cee9c46448f0b2b1cf315e5cb5d8adb98932b92bbb46548fca6e710a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "port": port,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> "IngressV1SpecDefaultBackendServicePort":
        '''port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast("IngressV1SpecDefaultBackendServicePort", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackendService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84578decf9a61e593aab90ad345cd0f99fab537466184d918d0085606d4cb617)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPort")
    def put_port(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        value = IngressV1SpecDefaultBackendServicePort(name=name, number=number)

        return typing.cast(None, jsii.invoke(self, "putPort", [value]))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> "IngressV1SpecDefaultBackendServicePortOutputReference":
        return typing.cast("IngressV1SpecDefaultBackendServicePortOutputReference", jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional["IngressV1SpecDefaultBackendServicePort"]:
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendServicePort"], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2213f92c0605f2d3b3d09adc0ee2b2313a3b7f25201f042d804110af56224c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackendService]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackendService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackendService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a481eb1281aaaac509c41043834dd76c81826c2fcb43247cd68e83d913beaf2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendServicePort",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "number": "number"},
)
class IngressV1SpecDefaultBackendServicePort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4865143546e4283e869a52ffcd1441cfaae7d3c866e482e0215b8a84986b346)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''Specifies the numerical port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackendServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendServicePortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecDefaultBackendServicePortOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7b14d51a52811651ecd3e01be23ccae67dfac8af7b4cd817356070fd629aafe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c81cb6e456ea6dd5d349dc813b736d67dec8ae16a99ecb7d538dfbf1eb210c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "number"))

    @number.setter
    def number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ece070935450eb85d0cd3eed1ad5c66a21525218fa23736ad5f44b3a7b68b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "number", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackendServicePort]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackendServicePort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackendServicePort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49efb659fb7538b99e06deffa43ae2e33517999fd1c8905146cce0b7ba266868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05d1840c749148af7dcd89211a88bab03cc49f5e41197b649f4f9a1ee8e0ba2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultBackend")
    def put_default_backend(
        self,
        *,
        resource: typing.Optional[typing.Union[IngressV1SpecDefaultBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union[IngressV1SpecDefaultBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        value = IngressV1SpecDefaultBackend(resource=resource, service=service)

        return typing.cast(None, jsii.invoke(self, "putDefaultBackend", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5a97bc40e48ff145e930747fcaced8e80f24fb5c4bf1dcd54053e3dbf0614d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecTls", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3e4dd82af60b8baa551c09e43f7a36eb342200276aede3fb03535ac3be5c46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetDefaultBackend")
    def reset_default_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBackend", []))

    @jsii.member(jsii_name="resetIngressClassName")
    def reset_ingress_class_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressClassName", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="defaultBackend")
    def default_backend(self) -> IngressV1SpecDefaultBackendOutputReference:
        return typing.cast(IngressV1SpecDefaultBackendOutputReference, jsii.get(self, "defaultBackend"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "IngressV1SpecRuleList":
        return typing.cast("IngressV1SpecRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "IngressV1SpecTlsList":
        return typing.cast("IngressV1SpecTlsList", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendInput")
    def default_backend_input(self) -> typing.Optional[IngressV1SpecDefaultBackend]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackend], jsii.get(self, "defaultBackendInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassNameInput")
    def ingress_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingressClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassName")
    def ingress_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ingressClassName"))

    @ingress_class_name.setter
    def ingress_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8887af680945102a716c2bce078cd2b18184557233a0587627ebca779f8ffb63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressClassName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1Spec]:
        return typing.cast(typing.Optional[IngressV1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1Spec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08ec586079b7eb30fc153cc6fb60caa33bc67577c5a99fc5c68d2c3343a43e44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRule",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "http": "http"},
)
class IngressV1SpecRule:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        http: typing.Optional[typing.Union["IngressV1SpecRuleHttp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the IP in the Spec of the parent Ingress. 2. The ``:`` delimiter is not respected because ports are not allowed. Currently the port of an Ingress is implicitly :80 for http and :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue. Host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#host IngressV1#host}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#http IngressV1#http}
        '''
        if isinstance(http, dict):
            http = IngressV1SpecRuleHttp(**http)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de8a3d244667107ecb6c23fab60549c3f35cc85abe094086d4c6b6f9456ea196)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if http is not None:
            self._values["http"] = http

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host is the fully qualified domain name of a network host, as defined by RFC 3986.

        Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to
        the IP in the Spec of the parent Ingress.
        2. The ``:`` delimiter is not respected because ports are not allowed.
        Currently the port of an Ingress is implicitly :80 for http and
        :443 for https.
        Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.

        Host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#host IngressV1#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http(self) -> typing.Optional["IngressV1SpecRuleHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#http IngressV1#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttp",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class IngressV1SpecRuleHttp:
    def __init__(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b19742b9021a645e80c69f360722388ef5ec00c50b300ac2eefb62df0946af)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]]:
        '''path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__414407edb6a259e5379fe82c4c082bf9c5c7b197257803b409c96c11d335a07e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2273fcd42f9b0edcfc422549c8765a81bf3bc7d2fcafef9d0b99df04638cf97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPath", [value]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "IngressV1SpecRuleHttpPathList":
        return typing.cast("IngressV1SpecRuleHttpPathList", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]]], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecRuleHttp]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1SpecRuleHttp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590580c40667ba20a7116369c575acc6b7e01825995f44d05ba7030a8e4dc87f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPath",
    jsii_struct_bases=[],
    name_mapping={"backend": "backend", "path": "path", "path_type": "pathType"},
)
class IngressV1SpecRuleHttpPath:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union["IngressV1SpecRuleHttpPathBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        path_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#backend IngressV1#backend}
        :param path: Path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        :param path_type: PathType determines the interpretation of the Path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is done on a path element by element basis. A path element refers is the list of labels in the path split by the '/' separator. A request is a match for path p if every p is an element-wise prefix of p of the request path. Note that if the last element of the path is a substring of the last element in request path, it is not a match (e.g. /foo/bar matches /foo/bar/baz, but does not match /foo/barbaz). ImplementationSpecific: Interpretation of the Path matching is up to the IngressClass. Implementations can treat this as a separate PathType or treat it identically to Prefix or Exact path types. Implementations are required to support all path types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path_type IngressV1#path_type}
        '''
        if isinstance(backend, dict):
            backend = IngressV1SpecRuleHttpPathBackend(**backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bccd0dd5eb2acf2caafc4278824093d4ef9b3ab490fa9a521dd214affff89567)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if path is not None:
            self._values["path"] = path
        if path_type is not None:
            self._values["path_type"] = path_type

    @builtins.property
    def backend(self) -> typing.Optional["IngressV1SpecRuleHttpPathBackend"]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#backend IngressV1#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackend"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path is matched against the path of an incoming request.

        Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_type(self) -> typing.Optional[builtins.str]:
        '''PathType determines the interpretation of the Path matching.

        PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is
        done on a path element by element basis. A path element refers is the
        list of labels in the path split by the '/' separator. A request is a
        match for path p if every p is an element-wise prefix of p of the
        request path. Note that if the last element of the path is a substring
        of the last element in request path, it is not a match (e.g. /foo/bar
        matches /foo/bar/baz, but does not match /foo/barbaz).
        ImplementationSpecific: Interpretation of the Path matching is up to
        the IngressClass. Implementations can treat this as a separate PathType
        or treat it identically to Prefix or Exact path types.
        Implementations are required to support all path types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path_type IngressV1#path_type}
        '''
        result = self._values.get("path_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackend",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource", "service": "service"},
)
class IngressV1SpecRuleHttpPathBackend:
    def __init__(
        self,
        *,
        resource: typing.Optional[typing.Union["IngressV1SpecRuleHttpPathBackendResource", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["IngressV1SpecRuleHttpPathBackendService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        if isinstance(resource, dict):
            resource = IngressV1SpecRuleHttpPathBackendResource(**resource)
        if isinstance(service, dict):
            service = IngressV1SpecRuleHttpPathBackendService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35efd4f09fbcfcdaf79b2824153f5c1ebe625ba6f5ec1f26b75f10c34866bdbd)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource is not None:
            self._values["resource"] = resource
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def resource(self) -> typing.Optional["IngressV1SpecRuleHttpPathBackendResource"]:
        '''resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendResource"], result)

    @builtins.property
    def service(self) -> typing.Optional["IngressV1SpecRuleHttpPathBackendService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6540593348109daab889f2a4040d9c04d8c3b13b0a6a27fa89bca16761e22ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putResource")
    def put_resource(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        value = IngressV1SpecRuleHttpPathBackendResource(
            api_group=api_group, kind=kind, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putResource", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecRuleHttpPathBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        value = IngressV1SpecRuleHttpPathBackendService(name=name, port=port)

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> "IngressV1SpecRuleHttpPathBackendResourceOutputReference":
        return typing.cast("IngressV1SpecRuleHttpPathBackendResourceOutputReference", jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "IngressV1SpecRuleHttpPathBackendServiceOutputReference":
        return typing.cast("IngressV1SpecRuleHttpPathBackendServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(
        self,
    ) -> typing.Optional["IngressV1SpecRuleHttpPathBackendResource"]:
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendResource"], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional["IngressV1SpecRuleHttpPathBackendService"]:
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a00280c96daa68d61bc54778678f2debf83d0f5edb04cacd29d5ffa866cb474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendResource",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "kind": "kind", "name": "name"},
)
class IngressV1SpecRuleHttpPathBackendResource:
    def __init__(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a6ed77e094f187f4107986d60be51b99f3062ebfe321fd2bc96c3f72a8fb60)
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_group": api_group,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_group(self) -> builtins.str:
        '''APIGroup is the group for the resource being referenced.

        If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        '''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the User to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackendResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f7f3dba4be3a33f1f807f1c17b3b7d17cec4e32ee00e35eb235aa858e3b54d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiGroupInput")
    def api_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96e7a4c63b773d456c251f8d2b5983a17c2224dcc2cee00219ac43ce45b87ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5b2e0dc08c736754abe209a0eae1b6d411b3e60a7ff131eb071d33514dcc3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d2c1f38643edd4d4db3c912882ab8c0aff6c0f88b05583ee9e95ddbc0425a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IngressV1SpecRuleHttpPathBackendResource]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackendResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackendResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d184504e91988d4074dc0fdf818fd17a90de7565b0625e5d377e1d1269f676e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "port": "port"},
)
class IngressV1SpecRuleHttpPathBackendService:
    def __init__(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecRuleHttpPathBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        if isinstance(port, dict):
            port = IngressV1SpecRuleHttpPathBackendServicePort(**port)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2631384f0d147adbbd447235486337a095ee74112d039b045ebba60ff37f9ff)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "port": port,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> "IngressV1SpecRuleHttpPathBackendServicePort":
        '''port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast("IngressV1SpecRuleHttpPathBackendServicePort", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackendService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dbd24afc6a6e63a94a984dff035745e16777d9431f45db5dfe090be8b44862b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPort")
    def put_port(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        value = IngressV1SpecRuleHttpPathBackendServicePort(name=name, number=number)

        return typing.cast(None, jsii.invoke(self, "putPort", [value]))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> "IngressV1SpecRuleHttpPathBackendServicePortOutputReference":
        return typing.cast("IngressV1SpecRuleHttpPathBackendServicePortOutputReference", jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(
        self,
    ) -> typing.Optional["IngressV1SpecRuleHttpPathBackendServicePort"]:
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendServicePort"], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a16d35134f96e00c66016750d7929e64b8e2d51fbf684e8cfa8f1302cd06d8e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IngressV1SpecRuleHttpPathBackendService]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackendService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackendService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe596630fbe3f700c261490ea3f2b182597654954b6dac96afc7d99b3c01813)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendServicePort",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "number": "number"},
)
class IngressV1SpecRuleHttpPathBackendServicePort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93cac2f6a57e74851f1e0a0311b216032e63d0f55016f1a56ca690c0b2844427)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''Specifies the numerical port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackendServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendServicePortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendServicePortOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2429bd3a0fa90e097b11f5529922a29c752b8d0d07de3ae4466ea7b6066d6af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21241e424624952608cd51369c070bf1fa85bf80812852b463d051f13e570b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "number"))

    @number.setter
    def number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66ef5c0274d39236060047472949666c3f788b473129230e3538d650c82c5d0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "number", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a74f00ed3b06d3c2434117cde50453d2a3b1927eb2bed629993042f0246b093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleHttpPathList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f64348e0ddf066bec3024eee82bf1b0df3960f9876dac791f6ea11d3b1f153d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1SpecRuleHttpPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c63582d66caa1ef7d4f201d47056b6fafd71fa65473631b24e3f0ba6f5e989)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1SpecRuleHttpPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91503e2013ddf89fc4ddd65a9c22c05d74fabbaf2bb28cbb07c41031d1bc0cb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d841bc1b7f3d20de0f994791c821c768d28a115239e29e093c296aa97e7bef4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a8db6b26649ed64f2708fecf1c70b9d1b78f561a3da122b0188cfa52be1a7e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad11a7e374c42520bf8f20e84317c19a3cd97484c4a5a07ae12d7b4bdf237363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleHttpPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleHttpPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cee93b6ec69067f2d9108a7f976716b3fd5b170572d74e40fc5785515abe847)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        *,
        resource: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        value = IngressV1SpecRuleHttpPathBackend(resource=resource, service=service)

        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPathType")
    def reset_path_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathType", []))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> IngressV1SpecRuleHttpPathBackendOutputReference:
        return typing.cast(IngressV1SpecRuleHttpPathBackendOutputReference, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[IngressV1SpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackend], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="pathTypeInput")
    def path_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a61402ab32775213ce66d39f22f1dd20c93e9047433a5836d58bae08c9b5b78c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="pathType")
    def path_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathType"))

    @path_type.setter
    def path_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd3930be2f07c2fa1ea39dd94a3751beb292d1808ac623ac39c3b62e0f124784)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5651813c298b4718bdd674f244819825ee24ef0842578a5830694becd1fdadd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26b13052487a688c14a301a9f502894e82348744dba2b29b69f3ec17148b8b3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1SpecRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__becb5d593d32a9fc231ec5e60634bf194dad09571629d43f7c4edfff43c6cfd5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1SpecRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd344e6b5be5662ea7402d3ff7a4f76e7506706eefc630884cc51ddfe03868b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7cdbe5be52214c52c0437f2ab4e73b8ae3369c0c819cc141255770e962b436a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aac7fc71ca7dd689b606e9db5e5026726137736267837c0ce366361e31add43e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa9dfe0838579946170c4ae2a8fa303ec08ee3e653bbfb15e8b3fefd8bbc1eeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__963682ea5713a286710e471cdfd9a5f9d895155b050612aa2b7560add11fffbf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        value = IngressV1SpecRuleHttp(path=path)

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> IngressV1SpecRuleHttpOutputReference:
        return typing.cast(IngressV1SpecRuleHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[IngressV1SpecRuleHttp]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d87c7269d1aca705d09d7c278997ff5975207827ebea50c812a6882a7f19a87d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f521ffd442ef93ad601bdd516170ce2a9ecb3e07375b65e583aae5316ab6e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1SpecTls",
    jsii_struct_bases=[],
    name_mapping={"hosts": "hosts", "secret_name": "secretName"},
)
class IngressV1SpecTls:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#hosts IngressV1#hosts}
        :param secret_name: SecretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#secret_name IngressV1#secret_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10710e25eb63bb1b2ab1848a899aa29ad680db20fee3657979b66206022ebc89)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Hosts are a list of hosts included in the TLS certificate.

        The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#hosts IngressV1#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''SecretName is the name of the secret used to terminate TLS traffic on port 443.

        Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#secret_name IngressV1#secret_name}
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecTlsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecTlsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80a3e52775f55f18ddd38903afe4bca47168e4eb7ea8554210fc6f40628112d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1SpecTlsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__728736f2ddaf1f742a56c426dd7724830c142b558a181d2494f7a2e39ca88759)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1SpecTlsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de7ed889deb64028fc43890913130e161578ddcc87756792cccf8c56d0d5db3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__498acbd662b47a5ca7049cdb511f3fa1b6cec6c2c5bda47062e0c6b363829c9a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0453d49c956c7fd7df5ff30c9c4da5c973d6ac5e2ad09442c700ed9f1ec2a50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96bd7a218bfda7b1dab4fb686071ca0288b1f7c6b2e946f0168f07d79ba5f12f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1SpecTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6924791eb2bf9ad345630391cbd16972686c24e3d1844a6c96808e043d46116)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetSecretName")
    def reset_secret_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretName", []))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f796534cbcd108e7d6aebaa3d742952b40543a95a2861e1ffc2476dd859072f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efc798e99211cc7d0228a5ab587d27a6680774f6bc4cc533bdfd45d46c01acb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9507b8d4e261a7f14a4b5deb1820ff9e8532eaa9a2f51f664305a977b23e4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1Status",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressV1Status:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Status(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1StatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1StatusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5031d67c24067d044ad6d7934b5a7352e4ae644703f98a728fa72344355eccab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1StatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bb2dcdb518782bfac87772626fcfff636009606ab28c78311a9d58b782c296)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1StatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3acc077b00237e23e9cd2761373b0322f78ee52c5114f7e53341b527516b22f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7875147fa23ffcd2933ff061357de7be87648482552984d80f24462a1b98d8e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6553d3270b4f4adc485e0ad796a9b5701908a28abec42ae414da02ba6cc69232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1StatusLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressV1StatusLoadBalancer:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1StatusLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1StatusLoadBalancerIngress",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressV1StatusLoadBalancerIngress:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1StatusLoadBalancerIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1StatusLoadBalancerIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1StatusLoadBalancerIngressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b011b789064952b2b517f7cb521a592a5488798d37b3da2025e3306dd9f3ef0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IngressV1StatusLoadBalancerIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d254bc9e8e07566391a74aafb9bdb4e94f56d210ba0cd46f3e3aeb507dc37793)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1StatusLoadBalancerIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c392c65c9da4fdaad7420a4d54bea5eea6e4214bfde816050689dd56614677)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c97dcb0ae51c3e4ace970de3c40e6d097fc559c0a5c74db6a3672f7b36e58712)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72679a557dbe2472555aea1d49a0b698fd0367dedd95ccd8a1b2d33a1f175b1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressV1StatusLoadBalancerIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1StatusLoadBalancerIngressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b46221bb945b5dffb15bf077e7b97593f67c1efbae67cfeabe0139323df08381)
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
    def internal_value(self) -> typing.Optional[IngressV1StatusLoadBalancerIngress]:
        return typing.cast(typing.Optional[IngressV1StatusLoadBalancerIngress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1StatusLoadBalancerIngress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d53ab89b5ccd7b0dd8f4b03fe7480af5a0bc789badb983b0b3f97fd442cead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1StatusLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1StatusLoadBalancerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b5787bedff927d65277b203a57696b44b56ebe94ffb59f24be9c67f0d698615)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1StatusLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e83fd41e2446295e66ffaf747e68b407bcfd9b26f544ede81e98d7e518752bd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1StatusLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69bcf540392173a4ce9da708cbfdb92c8260ce25b2eebd51cade3b1f8e48c12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29c031e628cf714f38a213f8984c8423b6748babaf408d80aa171628ed4b49d7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__892a6e3ae4abd5a8a42a3069dd8fd653cfa7974b4ecd9636bd8afc7370c87f39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressV1StatusLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1StatusLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9be925752ff13d6ae039eb399e99839a197449a0fc8e032d20bcb14fa4363297)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> IngressV1StatusLoadBalancerIngressList:
        return typing.cast(IngressV1StatusLoadBalancerIngressList, jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1StatusLoadBalancer]:
        return typing.cast(typing.Optional[IngressV1StatusLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1StatusLoadBalancer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7827e5430df38d1ca7fa29d35740410ef5fc89512b8a417aa336a0bc5c86361d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1StatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1StatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82a27ae3c65922e10c6953f479e77f0c411d3d2b8f4dc38c995be6b0033cb621)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> IngressV1StatusLoadBalancerList:
        return typing.cast(IngressV1StatusLoadBalancerList, jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1Status]:
        return typing.cast(typing.Optional[IngressV1Status], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1Status]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__080da60013986d48a0f6ac629d8d1df297d9160a1456c5776615e4433553ef89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingressV1.IngressV1Timeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class IngressV1Timeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#create IngressV1#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#delete IngressV1#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73be57f295ede3ac6a97c07df02735dba0b18e722a3d69be6fbcf00fdbec8750)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#create IngressV1#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#delete IngressV1#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1TimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingressV1.IngressV1TimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21572ef2bd1ab6ed5d619a8b8286e3808c53be0c82098f42da0e37d16b2bd63c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6429361ef137795ba8162754f0c7198563f946cc0684d95ebde7d55e002563a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59cdebd6c60a8ab9291e6aee67ccb6420caea2a9cd2dfc4da1393aa4afe4875d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1Timeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1Timeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1Timeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd8a6c5e94184bba7b5a220a98b7d0abd822c0e3cbd842cd69eae3d4888c1f16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IngressV1",
    "IngressV1Config",
    "IngressV1Metadata",
    "IngressV1MetadataOutputReference",
    "IngressV1Spec",
    "IngressV1SpecDefaultBackend",
    "IngressV1SpecDefaultBackendOutputReference",
    "IngressV1SpecDefaultBackendResource",
    "IngressV1SpecDefaultBackendResourceOutputReference",
    "IngressV1SpecDefaultBackendService",
    "IngressV1SpecDefaultBackendServiceOutputReference",
    "IngressV1SpecDefaultBackendServicePort",
    "IngressV1SpecDefaultBackendServicePortOutputReference",
    "IngressV1SpecOutputReference",
    "IngressV1SpecRule",
    "IngressV1SpecRuleHttp",
    "IngressV1SpecRuleHttpOutputReference",
    "IngressV1SpecRuleHttpPath",
    "IngressV1SpecRuleHttpPathBackend",
    "IngressV1SpecRuleHttpPathBackendOutputReference",
    "IngressV1SpecRuleHttpPathBackendResource",
    "IngressV1SpecRuleHttpPathBackendResourceOutputReference",
    "IngressV1SpecRuleHttpPathBackendService",
    "IngressV1SpecRuleHttpPathBackendServiceOutputReference",
    "IngressV1SpecRuleHttpPathBackendServicePort",
    "IngressV1SpecRuleHttpPathBackendServicePortOutputReference",
    "IngressV1SpecRuleHttpPathList",
    "IngressV1SpecRuleHttpPathOutputReference",
    "IngressV1SpecRuleList",
    "IngressV1SpecRuleOutputReference",
    "IngressV1SpecTls",
    "IngressV1SpecTlsList",
    "IngressV1SpecTlsOutputReference",
    "IngressV1Status",
    "IngressV1StatusList",
    "IngressV1StatusLoadBalancer",
    "IngressV1StatusLoadBalancerIngress",
    "IngressV1StatusLoadBalancerIngressList",
    "IngressV1StatusLoadBalancerIngressOutputReference",
    "IngressV1StatusLoadBalancerList",
    "IngressV1StatusLoadBalancerOutputReference",
    "IngressV1StatusOutputReference",
    "IngressV1Timeouts",
    "IngressV1TimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6c8158158d9052d8eed6b906e74f1787b3388d3d06eeba44f1e8d6bc802537f9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[IngressV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[IngressV1Timeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__59a6c0cda575b81c824d85c30909fc74541fb1eaa78cd76f311828c23cb08181(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e13fff77d4100235564d056e4c8eaaf56d7db6d3579dc67f5eae6cd3717ba9ab(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f471bac4bf92659dd5cd78c0140657b8bd36558f105e95ddefd4f2d4b0c891(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[IngressV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[IngressV1Timeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2184811dc6f73ff3c7fc1e56e184f800fb084f4e6c5166328ca31c0822850d(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30acbc5e401b401c6c4de4c4c69c80a56f8c2642b66c353de7c6379a5faaa2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__130b4fa11fe3313590c4946f3dd01d0a860937d8f199f9600c6acad56f16db99(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdfe5591a5826beb100c0fb802f5c33fc93d770fd7410a05c017fc847e00980(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db148978e3b8cd16dd83ef854b39b137ebf51af340a650d0baeeb4cb0b3129fa(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3220f9eee0daa18364e69098dd29e2a59f5554c639f93e607fc51080d277cc4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33423795c77b079d97272ed6c9cd3e2dc71fd7d0a4d9c5c954a4ef9217ab689(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12be67ef98c195348d8b03c79c75392f0f679241e35d6655c99f1cde0632cc67(
    value: typing.Optional[IngressV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e9e2c913015402635ce7e5883adc256307e0e55944e6982922eaba79157ec8(
    *,
    default_backend: typing.Optional[typing.Union[IngressV1SpecDefaultBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    ingress_class_name: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecTls, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50eb82eddbfbefc9fe5eaa79ce77ae977a9aff07ae404af25c19cafb26ca8118(
    *,
    resource: typing.Optional[typing.Union[IngressV1SpecDefaultBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[IngressV1SpecDefaultBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f2b93d69e8f94f7187e347caa5b0f163600365710dc62ab07c21be83f070e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c205045b80ac14a56d1242c0641463b5dfe8a9b4c86401bbe5221e1d3660538(
    value: typing.Optional[IngressV1SpecDefaultBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32c29e43a10a3bb07e63f042854aeca592615bd1aff315a545b8e11b497985d(
    *,
    api_group: builtins.str,
    kind: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c80e41eccfe9e7acd13254aca1a75145036e32b071480f91651140c0a1624b1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40be8e44a0d2fe13f04f67289c9b94dba9caf5dd2f296f7a70ddc45a69ee5f0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f363a47990e4f6d9c939e663a731fc91893429b65664d8c347f50764c58f7d5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390d8d566d02fd4eb3e802b1d96ef08c8dce352412ec7f3f21bf53e116144c10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfc77f985d435d2ba933dde020c4ce5d3e461f2eb2fd97c793fb70b42ee7228d(
    value: typing.Optional[IngressV1SpecDefaultBackendResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80db76e9cee9c46448f0b2b1cf315e5cb5d8adb98932b92bbb46548fca6e710a(
    *,
    name: builtins.str,
    port: typing.Union[IngressV1SpecDefaultBackendServicePort, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84578decf9a61e593aab90ad345cd0f99fab537466184d918d0085606d4cb617(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2213f92c0605f2d3b3d09adc0ee2b2313a3b7f25201f042d804110af56224c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a481eb1281aaaac509c41043834dd76c81826c2fcb43247cd68e83d913beaf2d(
    value: typing.Optional[IngressV1SpecDefaultBackendService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4865143546e4283e869a52ffcd1441cfaae7d3c866e482e0215b8a84986b346(
    *,
    name: typing.Optional[builtins.str] = None,
    number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b14d51a52811651ecd3e01be23ccae67dfac8af7b4cd817356070fd629aafe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c81cb6e456ea6dd5d349dc813b736d67dec8ae16a99ecb7d538dfbf1eb210c1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ece070935450eb85d0cd3eed1ad5c66a21525218fa23736ad5f44b3a7b68b44(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49efb659fb7538b99e06deffa43ae2e33517999fd1c8905146cce0b7ba266868(
    value: typing.Optional[IngressV1SpecDefaultBackendServicePort],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d1840c749148af7dcd89211a88bab03cc49f5e41197b649f4f9a1ee8e0ba2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a97bc40e48ff145e930747fcaced8e80f24fb5c4bf1dcd54053e3dbf0614d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3e4dd82af60b8baa551c09e43f7a36eb342200276aede3fb03535ac3be5c46(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecTls, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8887af680945102a716c2bce078cd2b18184557233a0587627ebca779f8ffb63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ec586079b7eb30fc153cc6fb60caa33bc67577c5a99fc5c68d2c3343a43e44(
    value: typing.Optional[IngressV1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de8a3d244667107ecb6c23fab60549c3f35cc85abe094086d4c6b6f9456ea196(
    *,
    host: typing.Optional[builtins.str] = None,
    http: typing.Optional[typing.Union[IngressV1SpecRuleHttp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b19742b9021a645e80c69f360722388ef5ec00c50b300ac2eefb62df0946af(
    *,
    path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414407edb6a259e5379fe82c4c082bf9c5c7b197257803b409c96c11d335a07e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2273fcd42f9b0edcfc422549c8765a81bf3bc7d2fcafef9d0b99df04638cf97(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590580c40667ba20a7116369c575acc6b7e01825995f44d05ba7030a8e4dc87f(
    value: typing.Optional[IngressV1SpecRuleHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bccd0dd5eb2acf2caafc4278824093d4ef9b3ab490fa9a521dd214affff89567(
    *,
    backend: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    path_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35efd4f09fbcfcdaf79b2824153f5c1ebe625ba6f5ec1f26b75f10c34866bdbd(
    *,
    resource: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6540593348109daab889f2a4040d9c04d8c3b13b0a6a27fa89bca16761e22ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a00280c96daa68d61bc54778678f2debf83d0f5edb04cacd29d5ffa866cb474(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a6ed77e094f187f4107986d60be51b99f3062ebfe321fd2bc96c3f72a8fb60(
    *,
    api_group: builtins.str,
    kind: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7f3dba4be3a33f1f807f1c17b3b7d17cec4e32ee00e35eb235aa858e3b54d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96e7a4c63b773d456c251f8d2b5983a17c2224dcc2cee00219ac43ce45b87ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5b2e0dc08c736754abe209a0eae1b6d411b3e60a7ff131eb071d33514dcc3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d2c1f38643edd4d4db3c912882ab8c0aff6c0f88b05583ee9e95ddbc0425a99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d184504e91988d4074dc0fdf818fd17a90de7565b0625e5d377e1d1269f676e(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackendResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2631384f0d147adbbd447235486337a095ee74112d039b045ebba60ff37f9ff(
    *,
    name: builtins.str,
    port: typing.Union[IngressV1SpecRuleHttpPathBackendServicePort, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dbd24afc6a6e63a94a984dff035745e16777d9431f45db5dfe090be8b44862b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16d35134f96e00c66016750d7929e64b8e2d51fbf684e8cfa8f1302cd06d8e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe596630fbe3f700c261490ea3f2b182597654954b6dac96afc7d99b3c01813(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackendService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93cac2f6a57e74851f1e0a0311b216032e63d0f55016f1a56ca690c0b2844427(
    *,
    name: typing.Optional[builtins.str] = None,
    number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2429bd3a0fa90e097b11f5529922a29c752b8d0d07de3ae4466ea7b6066d6af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21241e424624952608cd51369c070bf1fa85bf80812852b463d051f13e570b54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ef5c0274d39236060047472949666c3f788b473129230e3538d650c82c5d0b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a74f00ed3b06d3c2434117cde50453d2a3b1927eb2bed629993042f0246b093(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64348e0ddf066bec3024eee82bf1b0df3960f9876dac791f6ea11d3b1f153d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c63582d66caa1ef7d4f201d47056b6fafd71fa65473631b24e3f0ba6f5e989(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91503e2013ddf89fc4ddd65a9c22c05d74fabbaf2bb28cbb07c41031d1bc0cb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d841bc1b7f3d20de0f994791c821c768d28a115239e29e093c296aa97e7bef4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8db6b26649ed64f2708fecf1c70b9d1b78f561a3da122b0188cfa52be1a7e6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad11a7e374c42520bf8f20e84317c19a3cd97484c4a5a07ae12d7b4bdf237363(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cee93b6ec69067f2d9108a7f976716b3fd5b170572d74e40fc5785515abe847(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a61402ab32775213ce66d39f22f1dd20c93e9047433a5836d58bae08c9b5b78c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd3930be2f07c2fa1ea39dd94a3751beb292d1808ac623ac39c3b62e0f124784(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5651813c298b4718bdd674f244819825ee24ef0842578a5830694becd1fdadd7(
    value: typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b13052487a688c14a301a9f502894e82348744dba2b29b69f3ec17148b8b3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__becb5d593d32a9fc231ec5e60634bf194dad09571629d43f7c4edfff43c6cfd5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd344e6b5be5662ea7402d3ff7a4f76e7506706eefc630884cc51ddfe03868b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cdbe5be52214c52c0437f2ab4e73b8ae3369c0c819cc141255770e962b436a9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac7fc71ca7dd689b606e9db5e5026726137736267837c0ce366361e31add43e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa9dfe0838579946170c4ae2a8fa303ec08ee3e653bbfb15e8b3fefd8bbc1eeb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__963682ea5713a286710e471cdfd9a5f9d895155b050612aa2b7560add11fffbf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d87c7269d1aca705d09d7c278997ff5975207827ebea50c812a6882a7f19a87d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f521ffd442ef93ad601bdd516170ce2a9ecb3e07375b65e583aae5316ab6e3e(
    value: typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10710e25eb63bb1b2ab1848a899aa29ad680db20fee3657979b66206022ebc89(
    *,
    hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a3e52775f55f18ddd38903afe4bca47168e4eb7ea8554210fc6f40628112d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__728736f2ddaf1f742a56c426dd7724830c142b558a181d2494f7a2e39ca88759(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de7ed889deb64028fc43890913130e161578ddcc87756792cccf8c56d0d5db3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__498acbd662b47a5ca7049cdb511f3fa1b6cec6c2c5bda47062e0c6b363829c9a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0453d49c956c7fd7df5ff30c9c4da5c973d6ac5e2ad09442c700ed9f1ec2a50(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96bd7a218bfda7b1dab4fb686071ca0288b1f7c6b2e946f0168f07d79ba5f12f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6924791eb2bf9ad345630391cbd16972686c24e3d1844a6c96808e043d46116(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f796534cbcd108e7d6aebaa3d742952b40543a95a2861e1ffc2476dd859072f0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc798e99211cc7d0228a5ab587d27a6680774f6bc4cc533bdfd45d46c01acb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9507b8d4e261a7f14a4b5deb1820ff9e8532eaa9a2f51f664305a977b23e4d(
    value: typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5031d67c24067d044ad6d7934b5a7352e4ae644703f98a728fa72344355eccab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bb2dcdb518782bfac87772626fcfff636009606ab28c78311a9d58b782c296(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3acc077b00237e23e9cd2761373b0322f78ee52c5114f7e53341b527516b22f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7875147fa23ffcd2933ff061357de7be87648482552984d80f24462a1b98d8e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6553d3270b4f4adc485e0ad796a9b5701908a28abec42ae414da02ba6cc69232(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b011b789064952b2b517f7cb521a592a5488798d37b3da2025e3306dd9f3ef0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d254bc9e8e07566391a74aafb9bdb4e94f56d210ba0cd46f3e3aeb507dc37793(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c392c65c9da4fdaad7420a4d54bea5eea6e4214bfde816050689dd56614677(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97dcb0ae51c3e4ace970de3c40e6d097fc559c0a5c74db6a3672f7b36e58712(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72679a557dbe2472555aea1d49a0b698fd0367dedd95ccd8a1b2d33a1f175b1f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46221bb945b5dffb15bf077e7b97593f67c1efbae67cfeabe0139323df08381(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d53ab89b5ccd7b0dd8f4b03fe7480af5a0bc789badb983b0b3f97fd442cead(
    value: typing.Optional[IngressV1StatusLoadBalancerIngress],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b5787bedff927d65277b203a57696b44b56ebe94ffb59f24be9c67f0d698615(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e83fd41e2446295e66ffaf747e68b407bcfd9b26f544ede81e98d7e518752bd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69bcf540392173a4ce9da708cbfdb92c8260ce25b2eebd51cade3b1f8e48c12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c031e628cf714f38a213f8984c8423b6748babaf408d80aa171628ed4b49d7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__892a6e3ae4abd5a8a42a3069dd8fd653cfa7974b4ecd9636bd8afc7370c87f39(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be925752ff13d6ae039eb399e99839a197449a0fc8e032d20bcb14fa4363297(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7827e5430df38d1ca7fa29d35740410ef5fc89512b8a417aa336a0bc5c86361d(
    value: typing.Optional[IngressV1StatusLoadBalancer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a27ae3c65922e10c6953f479e77f0c411d3d2b8f4dc38c995be6b0033cb621(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__080da60013986d48a0f6ac629d8d1df297d9160a1456c5776615e4433553ef89(
    value: typing.Optional[IngressV1Status],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73be57f295ede3ac6a97c07df02735dba0b18e722a3d69be6fbcf00fdbec8750(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21572ef2bd1ab6ed5d619a8b8286e3808c53be0c82098f42da0e37d16b2bd63c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6429361ef137795ba8162754f0c7198563f946cc0684d95ebde7d55e002563a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59cdebd6c60a8ab9291e6aee67ccb6420caea2a9cd2dfc4da1393aa4afe4875d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8a6c5e94184bba7b5a220a98b7d0abd822c0e3cbd842cd69eae3d4888c1f16(
    value: typing.Optional[typing.Union[IngressV1Timeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
