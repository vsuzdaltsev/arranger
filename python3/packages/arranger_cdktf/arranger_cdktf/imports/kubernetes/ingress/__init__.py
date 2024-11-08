'''
# `kubernetes_ingress`

Refer to the Terraform Registory for docs: [`kubernetes_ingress`](https://www.terraform.io/docs/providers/kubernetes/r/ingress).
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


class Ingress(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.Ingress",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress kubernetes_ingress}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["IngressMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress kubernetes_ingress} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#metadata Ingress#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#spec Ingress#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#id Ingress#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#wait_for_load_balancer Ingress#wait_for_load_balancer}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a518448844d79ae5a0ff81dcba8f6670126d9286705ed8042d404f1c05fd42e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IngressConfig(
            metadata=metadata,
            spec=spec,
            id=id,
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#annotations Ingress#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#generate_name Ingress#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#labels Ingress#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#name Ingress#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#namespace Ingress#namespace}
        '''
        value = IngressMetadata(
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
        backend: typing.Optional[typing.Union["IngressSpecBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        :param ingress_class_name: IngressClassName is the name of the IngressClass cluster resource. The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#ingress_class_name Ingress#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#rule Ingress#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#tls Ingress#tls}
        '''
        value = IngressSpec(
            backend=backend, ingress_class_name=ingress_class_name, rule=rule, tls=tls
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    def metadata(self) -> "IngressMetadataOutputReference":
        return typing.cast("IngressMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "IngressSpecOutputReference":
        return typing.cast("IngressSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "IngressStatusList":
        return typing.cast("IngressStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["IngressMetadata"]:
        return typing.cast(typing.Optional["IngressMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["IngressSpec"]:
        return typing.cast(typing.Optional["IngressSpec"], jsii.get(self, "specInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b3b823ce6bf281302340f4b96bbd8aaf3804bf251fda683021a418d8e7271895)
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
            type_hints = typing.get_type_hints(_typecheckingstub__830672566fc89c847f9574efdd33ebc9385b017aed4792426ef25859e988c2a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForLoadBalancer", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressConfig",
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
        "wait_for_load_balancer": "waitForLoadBalancer",
    },
)
class IngressConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["IngressMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#metadata Ingress#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#spec Ingress#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#id Ingress#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#wait_for_load_balancer Ingress#wait_for_load_balancer}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = IngressMetadata(**metadata)
        if isinstance(spec, dict):
            spec = IngressSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7aeedb2248dfe2f88cba71671ce486eee6a1a4b691f80def40881b751cbf73c)
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
    def metadata(self) -> "IngressMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#metadata Ingress#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("IngressMetadata", result)

    @builtins.property
    def spec(self) -> "IngressSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#spec Ingress#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("IngressSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#id Ingress#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_load_balancer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#wait_for_load_balancer Ingress#wait_for_load_balancer}
        '''
        result = self._values.get("wait_for_load_balancer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class IngressMetadata:
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#annotations Ingress#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#generate_name Ingress#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#labels Ingress#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#name Ingress#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#namespace Ingress#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0df1bebb217730a9a96550c0145b400bbd8eb4ac605bbbd49ba261faae84beaf)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#annotations Ingress#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#generate_name Ingress#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the ingress.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#labels Ingress#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#name Ingress#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the ingress must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#namespace Ingress#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac60b8048ef3b8a647855efac89ea8c4130df4d4553b113f84ff00ed813a18fc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe0fae4546fc868baaf01cba6d92cd77c312e84d24cd02827d2ef52cb2835761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebdc821206d1ff1dc60eb7bab4a86bc92d239e021db614e9eb4ca5a77cdffce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__428eca43080f3279cb9edab7a7e9ce5f737fc27bb3206a08814d668bb95c5f15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43747fa8235d113c7d915825f27fdebaa0ee0164671d80c3d107191ddf78ca2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cbab1d106ff22631f611c902f10e129b6179b09c43397e40e94020eb5fd27ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressMetadata]:
        return typing.cast(typing.Optional[IngressMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bc027e5cfb4ddd396cf735d5029e059d631564938a207b7011729a49b82cc57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpec",
    jsii_struct_bases=[],
    name_mapping={
        "backend": "backend",
        "ingress_class_name": "ingressClassName",
        "rule": "rule",
        "tls": "tls",
    },
)
class IngressSpec:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union["IngressSpecBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        :param ingress_class_name: IngressClassName is the name of the IngressClass cluster resource. The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#ingress_class_name Ingress#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#rule Ingress#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#tls Ingress#tls}
        '''
        if isinstance(backend, dict):
            backend = IngressSpecBackend(**backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8198d7e3eb46ac8980db02c00ec4cf474339e74da2e997d8a0406384b28b2022)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument ingress_class_name", value=ingress_class_name, expected_type=type_hints["ingress_class_name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if ingress_class_name is not None:
            self._values["ingress_class_name"] = ingress_class_name
        if rule is not None:
            self._values["rule"] = rule
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def backend(self) -> typing.Optional["IngressSpecBackend"]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional["IngressSpecBackend"], result)

    @builtins.property
    def ingress_class_name(self) -> typing.Optional[builtins.str]:
        '''IngressClassName is the name of the IngressClass cluster resource.

        The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#ingress_class_name Ingress#ingress_class_name}
        '''
        result = self._values.get("ingress_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#rule Ingress#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#tls Ingress#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpecBackend",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName", "service_port": "servicePort"},
)
class IngressSpecBackend:
    def __init__(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__382be0aa2a7daf6ec2be05e1faee74c392674f2fc88f2ebc785581f651548908)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument service_port", value=service_port, expected_type=type_hints["service_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if service_name is not None:
            self._values["service_name"] = service_name
        if service_port is not None:
            self._values["service_port"] = service_port

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_port(self) -> typing.Optional[builtins.str]:
        '''Specifies the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        result = self._values.get("service_port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5275ad769d06db464ad61824b52a9780e7a1f577d2eb67145b3e230fedcd16a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @jsii.member(jsii_name="resetServicePort")
    def reset_service_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePort", []))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePortInput")
    def service_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePortInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64b0feb32007d63dbbbb04da85ef4f77c517771398fa3af24faae9eb28043c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePort")
    def service_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePort"))

    @service_port.setter
    def service_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9212248980c13743401c90f2d4ddab75ea62b618981f7b93ef9a89b528fac74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpecBackend]:
        return typing.cast(typing.Optional[IngressSpecBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressSpecBackend]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0899fc8d382d97067cde35c3650eaebde60fcbea7900e8cff20365ac221902b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52ab01a92adab0c5ba3291dda7ba9446829925a3739006b6348b8014531a5578)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        value = IngressSpecBackend(
            service_name=service_name, service_port=service_port
        )

        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4db4dac9a9b6f4bc7970cd994e14f9cfb439f08aa227de2bce1f917be7fff58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecTls", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36ab3ca4162571e219a201f410ff736e2d3809ea9563c4432b8009cc67caa92f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

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
    @jsii.member(jsii_name="backend")
    def backend(self) -> IngressSpecBackendOutputReference:
        return typing.cast(IngressSpecBackendOutputReference, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "IngressSpecRuleList":
        return typing.cast("IngressSpecRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "IngressSpecTlsList":
        return typing.cast("IngressSpecTlsList", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[IngressSpecBackend]:
        return typing.cast(typing.Optional[IngressSpecBackend], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassNameInput")
    def ingress_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingressClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassName")
    def ingress_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ingressClassName"))

    @ingress_class_name.setter
    def ingress_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__601d8c6df170b6a36c508ddc7225846735b3fd8485dbd908bb14852618be10d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressClassName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpec]:
        return typing.cast(typing.Optional[IngressSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae8e93276642b6e8c83c14dcc8b6ae86400b4c82c8f778e3c0b4f30da2b31a5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpecRule",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "host": "host"},
)
class IngressSpecRule:
    def __init__(
        self,
        *,
        http: typing.Union["IngressSpecRuleHttp", typing.Dict[builtins.str, typing.Any]],
        host: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#http Ingress#http}
        :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the IP in the Spec of the parent Ingress. 2. The ``:`` delimiter is not respected because ports are not allowed. Currently the port of an Ingress is implicitly :80 for http and :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue. Host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#host Ingress#host}
        '''
        if isinstance(http, dict):
            http = IngressSpecRuleHttp(**http)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bed920fd8aae1aa0612cf7d207af0a3734a46a2c9de416aa26661fd9a9ce37f)
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http": http,
        }
        if host is not None:
            self._values["host"] = host

    @builtins.property
    def http(self) -> "IngressSpecRuleHttp":
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#http Ingress#http}
        '''
        result = self._values.get("http")
        assert result is not None, "Required property 'http' is missing"
        return typing.cast("IngressSpecRuleHttp", result)

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#host Ingress#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpecRuleHttp",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class IngressSpecRuleHttp:
    def __init__(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55d041e23908b96c9d78901ddf83658da77238b5b6ac5de8cc5fdfd1dbc0850)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]]:
        '''path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRuleHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecRuleHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecRuleHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99f5fed1dc617533dc9ff57249e459bdc2c5b0e3475aa521bc6bb06b37aacc1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34a320515f67e44c454825f0441441a86981a40586e30913a7e3f38f215fcea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPath", [value]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "IngressSpecRuleHttpPathList":
        return typing.cast("IngressSpecRuleHttpPathList", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]]], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpecRuleHttp]:
        return typing.cast(typing.Optional[IngressSpecRuleHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressSpecRuleHttp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c03171e58e4814034ef892139dca0b0c5b8e4c570e24f6c953a74d898f56cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpecRuleHttpPath",
    jsii_struct_bases=[],
    name_mapping={"backend": "backend", "path": "path"},
)
class IngressSpecRuleHttpPath:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union["IngressSpecRuleHttpPathBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        :param path: Path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        if isinstance(backend, dict):
            backend = IngressSpecRuleHttpPathBackend(**backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1697160d92a457a536452ec8e32098b1bd41246e8147a3edb789a3645d8b7d3d)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def backend(self) -> typing.Optional["IngressSpecRuleHttpPathBackend"]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional["IngressSpecRuleHttpPathBackend"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path is matched against the path of an incoming request.

        Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRuleHttpPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpecRuleHttpPathBackend",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName", "service_port": "servicePort"},
)
class IngressSpecRuleHttpPathBackend:
    def __init__(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9db8c83266c917a02afe305de4b31d4a4bb2878096d3388f95057cac90afb52)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument service_port", value=service_port, expected_type=type_hints["service_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if service_name is not None:
            self._values["service_name"] = service_name
        if service_port is not None:
            self._values["service_port"] = service_port

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_port(self) -> typing.Optional[builtins.str]:
        '''Specifies the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        result = self._values.get("service_port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRuleHttpPathBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecRuleHttpPathBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecRuleHttpPathBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b1e5e776a4f1f3ab9019ef7dd3259bbc6dd2a902b8fa8cc6052863114d43b86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @jsii.member(jsii_name="resetServicePort")
    def reset_service_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePort", []))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePortInput")
    def service_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePortInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2d827f55fb4b90aa68d9cc6387a3e8ed80faea20554999970684a2587a334b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePort")
    def service_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePort"))

    @service_port.setter
    def service_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045a11f2630f1cbbe51b455c4306694973a37c88401900d730d66e09170e19f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressSpecRuleHttpPathBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressSpecRuleHttpPathBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c3fd723db7515b9ec14e0f2da97a309af98c35b86a1911ec441dba216072e48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleHttpPathList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecRuleHttpPathList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cb7b4c8fdd47ea7320026ce9d781d3400076d155d3420ccddac6cf2ef21ba71)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressSpecRuleHttpPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5635ed578c3a82b3b1673e7486e06db14eb198b1f4e7f92cb6938993d9bf07b2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressSpecRuleHttpPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7941cd5e54fde9794851be0683291ea62292be72cfe888e0c20256fe0241a757)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e3ad7a9f0476b1531aa299ddfaf07854faa52f2de6ed30ce2295b1c6fd8ee63)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e9b6922ca093905de5443de5f6113ab87327ec360e9ab86a9ba4b7e5d8e4970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2dd27060217838eea336b60c238f0a57f0a744dafdd0eab172a7c78424a0aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleHttpPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecRuleHttpPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__17cc08dba0e9fa0af6b84ef17fe7203e4e44ff608fa02d0f0e1974031e603537)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        value = IngressSpecRuleHttpPathBackend(
            service_name=service_name, service_port=service_port
        )

        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> IngressSpecRuleHttpPathBackendOutputReference:
        return typing.cast(IngressSpecRuleHttpPathBackendOutputReference, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[IngressSpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressSpecRuleHttpPathBackend], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2bf95ff72ea55dbcb26182f28693ddd96f8f4a30c9f5dfd741f15efbd4ad2c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51eaad6bceb230e4ad0baa409cc7b0f3ced0c892a60a35bd563779f97b04617)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0bba251e59a394a310800e24e907bae9c6a610f1cd6bc8a6734fa0751f1d157)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressSpecRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e84935caad7a4e581bc0b661d7fc8bdfa718e55afed505bc8411f65faa32a3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressSpecRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__280b8df3dcf56917a765240cad19332ddb1214acdf89e1bb2cfddd70e25b3f8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__00e11b15f42d0a7e3301e4694f82362b160e2f70a0cdeb7a9bd6ff378a51d3e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45ae0c84ba0bfcfbae74d73b19862a306fb8781ff1e78d90290c3fa82b02c68b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f7c7fc5d5c94b74d0e26e2cb1e22d671716f8bbdc3392a167ae71e1a65e1dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7625295798aef01d27e32700a5359c9d03651aa3af51e562eeb61808a6d1ad49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        value = IngressSpecRuleHttp(path=path)

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> IngressSpecRuleHttpOutputReference:
        return typing.cast(IngressSpecRuleHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[IngressSpecRuleHttp]:
        return typing.cast(typing.Optional[IngressSpecRuleHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e8e0cd2b6aad167b56180a75314c9d04e037ee5b0f7c9967d3354a63efdb53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ec08d1279fa18e647f943f198090ede674578ad8ebdea50c5276884d7b1e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressSpecTls",
    jsii_struct_bases=[],
    name_mapping={"hosts": "hosts", "secret_name": "secretName"},
)
class IngressSpecTls:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#hosts Ingress#hosts}
        :param secret_name: SecretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#secret_name Ingress#secret_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9779ddc78da8215208768b1aa024084c2bccf95c66c6d1ca557cf56f36c2b3b3)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#hosts Ingress#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''SecretName is the name of the secret used to terminate TLS traffic on port 443.

        Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#secret_name Ingress#secret_name}
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecTlsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecTlsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b39dad7f7b709e8d7ddf948f15873165d578880590438222f3f9bf93aab740b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressSpecTlsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd817549910078ca95501a6fcc264327e06e49aa959e828d06a75282965d21a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressSpecTlsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1082b5de05d891a3174b7ea8969f5806c0107623c3fa32964810b6718b7cd0e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88b6cc28920c211477e06809373382eecf9f47afea92bca94395c0cbe3fc2e3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6e12475dd0a84c3e7e2b95ef816c65588df7a9a1e260fb8cc70d2922911391f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9a6d4f151027a905384382f78f99145dcfa49f2f5dd864ba05cd6cd7797191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressSpecTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1fbe33fc34ba7eaa608b378cc99adf811df73f75443f868c912d4d4d982695a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__01b3409367ae54d346f6dc216c4b4926f3d07725f35bded967ccb465f0c0a78d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61f1732edbfcf84a99de844d690725b10aea96ae315e5f0ecd2d22ff2e001ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cccad84e0891745859a38c3fdd6214d473ce9db8281645c64f1b7a4aa1ec4c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressStatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressStatusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e23d3df5aca435ac6028e4a15aa9aba91d59adbaca83eb902b93692fb2e25160)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c969894b8897bfaf25e8b6504aee5f9e238d4072fcea811818d8711cf0c68dc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d33819d9e6c226892b477fa67cda969a2627261c897b60bbd07ac35465191a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f0e9a8b1e760e5f3db10603a1c90bbcd40da7088ce955ba7517f413f1d0cc66)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13d0c4a49cab594900e1f45651646ebf27d4e429ae027ccc73f672abd4278242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressStatusLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressStatusLoadBalancer:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressStatusLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.ingress.IngressStatusLoadBalancerIngress",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressStatusLoadBalancerIngress:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressStatusLoadBalancerIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressStatusLoadBalancerIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressStatusLoadBalancerIngressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d3b724546235701cd57f51f5101df624ac045512a2a60f58aa652489ec03d83)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IngressStatusLoadBalancerIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebecbe9154d0d09240dd288539bd08b7bdc69152df34497c5d22d7ae8fac1514)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressStatusLoadBalancerIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0eaa56b7e0b99f87a01bfd0e45612cd0dbfa8c31b15a4057f9ffbdfae78edd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__733be5772da35f82f4edcc76f933f6029ad4031a3beb0a078206054ec1294d06)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fc0e308eccd481d792817a1625b6f03ed901487527585d29bc847621bee7dd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressStatusLoadBalancerIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressStatusLoadBalancerIngressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae7840979a4e2bd1137e3d0d584285c813da720bf963fb62f04955af7f012cea)
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
    def internal_value(self) -> typing.Optional[IngressStatusLoadBalancerIngress]:
        return typing.cast(typing.Optional[IngressStatusLoadBalancerIngress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressStatusLoadBalancerIngress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b40e5b2b7a9e9af86f2642db96c65827453ec05b43f99aff24f425e04c723d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressStatusLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressStatusLoadBalancerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aefb28d1df19e4febb2cf2558efd39773856fb73d7f4431296bfccbac1914a0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressStatusLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e695a2625bbf27af2c8e4b10e16890a7eb93eb0b48f74f4ba7ba88036238ff0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressStatusLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e52a0881d18a875b63bd8d3cf818a33deabbe3bff614e2ee55db328ed67a11)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bf28efcc792764812bd82e58434ff5d8ed51987da4cc4118ef69d6bce3eae69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9ca9872ee7b2f8afd3bdd92db949f29e30a129543ca5ae99210f258891c1673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressStatusLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressStatusLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92802967b20f309521102c6a5850579dc0c31c14001624136057695fbda8684e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> IngressStatusLoadBalancerIngressList:
        return typing.cast(IngressStatusLoadBalancerIngressList, jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressStatusLoadBalancer]:
        return typing.cast(typing.Optional[IngressStatusLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressStatusLoadBalancer]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a31b81ddaad2ba77177562f3c23c8fc72f295d3d69b6ce8bb3f393102001980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.ingress.IngressStatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec3f6730bcfa5a2f076ae3351d54ea42e1708a32fbd20b298d3cf0902e9abf42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> IngressStatusLoadBalancerList:
        return typing.cast(IngressStatusLoadBalancerList, jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressStatus]:
        return typing.cast(typing.Optional[IngressStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressStatus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f659835e8a276a4a96aa7bf4988344a9e268a9f1e54b7e4ed46bd4d163de4b98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Ingress",
    "IngressConfig",
    "IngressMetadata",
    "IngressMetadataOutputReference",
    "IngressSpec",
    "IngressSpecBackend",
    "IngressSpecBackendOutputReference",
    "IngressSpecOutputReference",
    "IngressSpecRule",
    "IngressSpecRuleHttp",
    "IngressSpecRuleHttpOutputReference",
    "IngressSpecRuleHttpPath",
    "IngressSpecRuleHttpPathBackend",
    "IngressSpecRuleHttpPathBackendOutputReference",
    "IngressSpecRuleHttpPathList",
    "IngressSpecRuleHttpPathOutputReference",
    "IngressSpecRuleList",
    "IngressSpecRuleOutputReference",
    "IngressSpecTls",
    "IngressSpecTlsList",
    "IngressSpecTlsOutputReference",
    "IngressStatus",
    "IngressStatusList",
    "IngressStatusLoadBalancer",
    "IngressStatusLoadBalancerIngress",
    "IngressStatusLoadBalancerIngressList",
    "IngressStatusLoadBalancerIngressOutputReference",
    "IngressStatusLoadBalancerList",
    "IngressStatusLoadBalancerOutputReference",
    "IngressStatusOutputReference",
]

publication.publish()

def _typecheckingstub__a518448844d79ae5a0ff81dcba8f6670126d9286705ed8042d404f1c05fd42e2(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[IngressMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b3b823ce6bf281302340f4b96bbd8aaf3804bf251fda683021a418d8e7271895(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__830672566fc89c847f9574efdd33ebc9385b017aed4792426ef25859e988c2a7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7aeedb2248dfe2f88cba71671ce486eee6a1a4b691f80def40881b751cbf73c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[IngressMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df1bebb217730a9a96550c0145b400bbd8eb4ac605bbbd49ba261faae84beaf(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac60b8048ef3b8a647855efac89ea8c4130df4d4553b113f84ff00ed813a18fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0fae4546fc868baaf01cba6d92cd77c312e84d24cd02827d2ef52cb2835761(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebdc821206d1ff1dc60eb7bab4a86bc92d239e021db614e9eb4ca5a77cdffce3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428eca43080f3279cb9edab7a7e9ce5f737fc27bb3206a08814d668bb95c5f15(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43747fa8235d113c7d915825f27fdebaa0ee0164671d80c3d107191ddf78ca2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cbab1d106ff22631f611c902f10e129b6179b09c43397e40e94020eb5fd27ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc027e5cfb4ddd396cf735d5029e059d631564938a207b7011729a49b82cc57(
    value: typing.Optional[IngressMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8198d7e3eb46ac8980db02c00ec4cf474339e74da2e997d8a0406384b28b2022(
    *,
    backend: typing.Optional[typing.Union[IngressSpecBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    ingress_class_name: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecTls, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382be0aa2a7daf6ec2be05e1faee74c392674f2fc88f2ebc785581f651548908(
    *,
    service_name: typing.Optional[builtins.str] = None,
    service_port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5275ad769d06db464ad61824b52a9780e7a1f577d2eb67145b3e230fedcd16a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64b0feb32007d63dbbbb04da85ef4f77c517771398fa3af24faae9eb28043c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9212248980c13743401c90f2d4ddab75ea62b618981f7b93ef9a89b528fac74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0899fc8d382d97067cde35c3650eaebde60fcbea7900e8cff20365ac221902b4(
    value: typing.Optional[IngressSpecBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ab01a92adab0c5ba3291dda7ba9446829925a3739006b6348b8014531a5578(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4db4dac9a9b6f4bc7970cd994e14f9cfb439f08aa227de2bce1f917be7fff58(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ab3ca4162571e219a201f410ff736e2d3809ea9563c4432b8009cc67caa92f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecTls, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601d8c6df170b6a36c508ddc7225846735b3fd8485dbd908bb14852618be10d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8e93276642b6e8c83c14dcc8b6ae86400b4c82c8f778e3c0b4f30da2b31a5a(
    value: typing.Optional[IngressSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bed920fd8aae1aa0612cf7d207af0a3734a46a2c9de416aa26661fd9a9ce37f(
    *,
    http: typing.Union[IngressSpecRuleHttp, typing.Dict[builtins.str, typing.Any]],
    host: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55d041e23908b96c9d78901ddf83658da77238b5b6ac5de8cc5fdfd1dbc0850(
    *,
    path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f5fed1dc617533dc9ff57249e459bdc2c5b0e3475aa521bc6bb06b37aacc1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a320515f67e44c454825f0441441a86981a40586e30913a7e3f38f215fcea3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c03171e58e4814034ef892139dca0b0c5b8e4c570e24f6c953a74d898f56cd(
    value: typing.Optional[IngressSpecRuleHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1697160d92a457a536452ec8e32098b1bd41246e8147a3edb789a3645d8b7d3d(
    *,
    backend: typing.Optional[typing.Union[IngressSpecRuleHttpPathBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9db8c83266c917a02afe305de4b31d4a4bb2878096d3388f95057cac90afb52(
    *,
    service_name: typing.Optional[builtins.str] = None,
    service_port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b1e5e776a4f1f3ab9019ef7dd3259bbc6dd2a902b8fa8cc6052863114d43b86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2d827f55fb4b90aa68d9cc6387a3e8ed80faea20554999970684a2587a334b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045a11f2630f1cbbe51b455c4306694973a37c88401900d730d66e09170e19f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3fd723db7515b9ec14e0f2da97a309af98c35b86a1911ec441dba216072e48(
    value: typing.Optional[IngressSpecRuleHttpPathBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb7b4c8fdd47ea7320026ce9d781d3400076d155d3420ccddac6cf2ef21ba71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5635ed578c3a82b3b1673e7486e06db14eb198b1f4e7f92cb6938993d9bf07b2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7941cd5e54fde9794851be0683291ea62292be72cfe888e0c20256fe0241a757(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3ad7a9f0476b1531aa299ddfaf07854faa52f2de6ed30ce2295b1c6fd8ee63(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9b6922ca093905de5443de5f6113ab87327ec360e9ab86a9ba4b7e5d8e4970(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2dd27060217838eea336b60c238f0a57f0a744dafdd0eab172a7c78424a0aa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cc08dba0e9fa0af6b84ef17fe7203e4e44ff608fa02d0f0e1974031e603537(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2bf95ff72ea55dbcb26182f28693ddd96f8f4a30c9f5dfd741f15efbd4ad2c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51eaad6bceb230e4ad0baa409cc7b0f3ced0c892a60a35bd563779f97b04617(
    value: typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0bba251e59a394a310800e24e907bae9c6a610f1cd6bc8a6734fa0751f1d157(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e84935caad7a4e581bc0b661d7fc8bdfa718e55afed505bc8411f65faa32a3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__280b8df3dcf56917a765240cad19332ddb1214acdf89e1bb2cfddd70e25b3f8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e11b15f42d0a7e3301e4694f82362b160e2f70a0cdeb7a9bd6ff378a51d3e1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ae0c84ba0bfcfbae74d73b19862a306fb8781ff1e78d90290c3fa82b02c68b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f7c7fc5d5c94b74d0e26e2cb1e22d671716f8bbdc3392a167ae71e1a65e1dd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7625295798aef01d27e32700a5359c9d03651aa3af51e562eeb61808a6d1ad49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e8e0cd2b6aad167b56180a75314c9d04e037ee5b0f7c9967d3354a63efdb53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ec08d1279fa18e647f943f198090ede674578ad8ebdea50c5276884d7b1e2d(
    value: typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9779ddc78da8215208768b1aa024084c2bccf95c66c6d1ca557cf56f36c2b3b3(
    *,
    hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b39dad7f7b709e8d7ddf948f15873165d578880590438222f3f9bf93aab740b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd817549910078ca95501a6fcc264327e06e49aa959e828d06a75282965d21a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1082b5de05d891a3174b7ea8969f5806c0107623c3fa32964810b6718b7cd0e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b6cc28920c211477e06809373382eecf9f47afea92bca94395c0cbe3fc2e3b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e12475dd0a84c3e7e2b95ef816c65588df7a9a1e260fb8cc70d2922911391f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9a6d4f151027a905384382f78f99145dcfa49f2f5dd864ba05cd6cd7797191(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbe33fc34ba7eaa608b378cc99adf811df73f75443f868c912d4d4d982695a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b3409367ae54d346f6dc216c4b4926f3d07725f35bded967ccb465f0c0a78d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61f1732edbfcf84a99de844d690725b10aea96ae315e5f0ecd2d22ff2e001ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cccad84e0891745859a38c3fdd6214d473ce9db8281645c64f1b7a4aa1ec4c5(
    value: typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e23d3df5aca435ac6028e4a15aa9aba91d59adbaca83eb902b93692fb2e25160(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c969894b8897bfaf25e8b6504aee5f9e238d4072fcea811818d8711cf0c68dc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d33819d9e6c226892b477fa67cda969a2627261c897b60bbd07ac35465191a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0e9a8b1e760e5f3db10603a1c90bbcd40da7088ce955ba7517f413f1d0cc66(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d0c4a49cab594900e1f45651646ebf27d4e429ae027ccc73f672abd4278242(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3b724546235701cd57f51f5101df624ac045512a2a60f58aa652489ec03d83(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebecbe9154d0d09240dd288539bd08b7bdc69152df34497c5d22d7ae8fac1514(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad0eaa56b7e0b99f87a01bfd0e45612cd0dbfa8c31b15a4057f9ffbdfae78edd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__733be5772da35f82f4edcc76f933f6029ad4031a3beb0a078206054ec1294d06(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fc0e308eccd481d792817a1625b6f03ed901487527585d29bc847621bee7dd6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7840979a4e2bd1137e3d0d584285c813da720bf963fb62f04955af7f012cea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b40e5b2b7a9e9af86f2642db96c65827453ec05b43f99aff24f425e04c723d7(
    value: typing.Optional[IngressStatusLoadBalancerIngress],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aefb28d1df19e4febb2cf2558efd39773856fb73d7f4431296bfccbac1914a0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e695a2625bbf27af2c8e4b10e16890a7eb93eb0b48f74f4ba7ba88036238ff0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e52a0881d18a875b63bd8d3cf818a33deabbe3bff614e2ee55db328ed67a11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bf28efcc792764812bd82e58434ff5d8ed51987da4cc4118ef69d6bce3eae69(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ca9872ee7b2f8afd3bdd92db949f29e30a129543ca5ae99210f258891c1673(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92802967b20f309521102c6a5850579dc0c31c14001624136057695fbda8684e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a31b81ddaad2ba77177562f3c23c8fc72f295d3d69b6ce8bb3f393102001980(
    value: typing.Optional[IngressStatusLoadBalancer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3f6730bcfa5a2f076ae3351d54ea42e1708a32fbd20b298d3cf0902e9abf42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f659835e8a276a4a96aa7bf4988344a9e268a9f1e54b7e4ed46bd4d163de4b98(
    value: typing.Optional[IngressStatus],
) -> None:
    """Type checking stubs"""
    pass
