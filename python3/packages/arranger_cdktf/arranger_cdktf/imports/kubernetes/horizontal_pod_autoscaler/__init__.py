'''
# `kubernetes_horizontal_pod_autoscaler`

Refer to the Terraform Registory for docs: [`kubernetes_horizontal_pod_autoscaler`](https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler).
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


class HorizontalPodAutoscaler(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscaler",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler kubernetes_horizontal_pod_autoscaler}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["HorizontalPodAutoscalerMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["HorizontalPodAutoscalerSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler kubernetes_horizontal_pod_autoscaler} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metadata HorizontalPodAutoscaler#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#spec HorizontalPodAutoscaler#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#id HorizontalPodAutoscaler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a253f177f71b2472abdeb0bb492261fc254f926afdf380ba20538fe72cb44c8c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HorizontalPodAutoscalerConfig(
            metadata=metadata,
            spec=spec,
            id=id,
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
        :param annotations: An unstructured key value map stored with the horizontal pod autoscaler that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#annotations HorizontalPodAutoscaler#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#generate_name HorizontalPodAutoscaler#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the horizontal pod autoscaler. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#labels HorizontalPodAutoscaler#labels}
        :param name: Name of the horizontal pod autoscaler, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param namespace: Namespace defines the space within which name of the horizontal pod autoscaler must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#namespace HorizontalPodAutoscaler#namespace}
        '''
        value = HorizontalPodAutoscalerMetadata(
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
        max_replicas: jsii.Number,
        scale_target_ref: typing.Union["HorizontalPodAutoscalerSpecScaleTargetRef", typing.Dict[builtins.str, typing.Any]],
        behavior: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecBehavior", typing.Dict[builtins.str, typing.Any]]] = None,
        metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetric", typing.Dict[builtins.str, typing.Any]]]]] = None,
        min_replicas: typing.Optional[jsii.Number] = None,
        target_cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_replicas: Upper limit for the number of pods that can be set by the autoscaler. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#max_replicas HorizontalPodAutoscaler#max_replicas}
        :param scale_target_ref: scale_target_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_target_ref HorizontalPodAutoscaler#scale_target_ref}
        :param behavior: behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#behavior HorizontalPodAutoscaler#behavior}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param min_replicas: Lower limit for the number of pods that can be set by the autoscaler, defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#min_replicas HorizontalPodAutoscaler#min_replicas}
        :param target_cpu_utilization_percentage: Target average CPU utilization (represented as a percentage of requested CPU) over all the pods. If not specified the default autoscaling policy will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target_cpu_utilization_percentage HorizontalPodAutoscaler#target_cpu_utilization_percentage}
        '''
        value = HorizontalPodAutoscalerSpec(
            max_replicas=max_replicas,
            scale_target_ref=scale_target_ref,
            behavior=behavior,
            metric=metric,
            min_replicas=min_replicas,
            target_cpu_utilization_percentage=target_cpu_utilization_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "HorizontalPodAutoscalerMetadataOutputReference":
        return typing.cast("HorizontalPodAutoscalerMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "HorizontalPodAutoscalerSpecOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["HorizontalPodAutoscalerMetadata"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["HorizontalPodAutoscalerSpec"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405e82a21a284ba206a8cc7cc2c311485ea02265f1bf8b2b251e94b701565861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerConfig",
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
    },
)
class HorizontalPodAutoscalerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["HorizontalPodAutoscalerMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["HorizontalPodAutoscalerSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metadata HorizontalPodAutoscaler#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#spec HorizontalPodAutoscaler#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#id HorizontalPodAutoscaler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = HorizontalPodAutoscalerMetadata(**metadata)
        if isinstance(spec, dict):
            spec = HorizontalPodAutoscalerSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99d0d0362f34f81348159f7fac057293daeed8f10a7efa4c4e8c659d0902f632)
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
    def metadata(self) -> "HorizontalPodAutoscalerMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metadata HorizontalPodAutoscaler#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("HorizontalPodAutoscalerMetadata", result)

    @builtins.property
    def spec(self) -> "HorizontalPodAutoscalerSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#spec HorizontalPodAutoscaler#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("HorizontalPodAutoscalerSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#id HorizontalPodAutoscaler#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class HorizontalPodAutoscalerMetadata:
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
        :param annotations: An unstructured key value map stored with the horizontal pod autoscaler that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#annotations HorizontalPodAutoscaler#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#generate_name HorizontalPodAutoscaler#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the horizontal pod autoscaler. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#labels HorizontalPodAutoscaler#labels}
        :param name: Name of the horizontal pod autoscaler, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param namespace: Namespace defines the space within which name of the horizontal pod autoscaler must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#namespace HorizontalPodAutoscaler#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c4317e07c23a5cdcb50e9970ad9317031bc8254a1e560245747c0799d9588b)
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
        '''An unstructured key value map stored with the horizontal pod autoscaler that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#annotations HorizontalPodAutoscaler#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#generate_name HorizontalPodAutoscaler#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the horizontal pod autoscaler.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#labels HorizontalPodAutoscaler#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the horizontal pod autoscaler, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the horizontal pod autoscaler must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#namespace HorizontalPodAutoscaler#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4310260325fabb3afc7a9f69a9d2eb9798f78dab2487ac6f61c60cc3409d8e3a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6d7a32eba58595c670fc3472a8237b01cb5eeee06788e65bccd1459f5d19902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c39c46654503f79c3e6559f495e84641d03eda7bfe37104cc7f4dcdeced363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30cbbfcce0c0d3c0de16b74cc1784cfeb95a4654431ba6058c5cd685df082d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d48ef1d8d431fbf07180377cfaa4e410625d85895a2c5c0b5e8974b5be65b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b6113a84dcc7d5dc1ec7b2cf386433cadd6c7cd90a2b46cb80048f3634f5137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HorizontalPodAutoscalerMetadata]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerMetadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7651b85c672ecbd1e263a5a89ec550f62690fa30d1aed628f860c864e14ed8de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpec",
    jsii_struct_bases=[],
    name_mapping={
        "max_replicas": "maxReplicas",
        "scale_target_ref": "scaleTargetRef",
        "behavior": "behavior",
        "metric": "metric",
        "min_replicas": "minReplicas",
        "target_cpu_utilization_percentage": "targetCpuUtilizationPercentage",
    },
)
class HorizontalPodAutoscalerSpec:
    def __init__(
        self,
        *,
        max_replicas: jsii.Number,
        scale_target_ref: typing.Union["HorizontalPodAutoscalerSpecScaleTargetRef", typing.Dict[builtins.str, typing.Any]],
        behavior: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecBehavior", typing.Dict[builtins.str, typing.Any]]] = None,
        metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetric", typing.Dict[builtins.str, typing.Any]]]]] = None,
        min_replicas: typing.Optional[jsii.Number] = None,
        target_cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_replicas: Upper limit for the number of pods that can be set by the autoscaler. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#max_replicas HorizontalPodAutoscaler#max_replicas}
        :param scale_target_ref: scale_target_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_target_ref HorizontalPodAutoscaler#scale_target_ref}
        :param behavior: behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#behavior HorizontalPodAutoscaler#behavior}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param min_replicas: Lower limit for the number of pods that can be set by the autoscaler, defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#min_replicas HorizontalPodAutoscaler#min_replicas}
        :param target_cpu_utilization_percentage: Target average CPU utilization (represented as a percentage of requested CPU) over all the pods. If not specified the default autoscaling policy will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target_cpu_utilization_percentage HorizontalPodAutoscaler#target_cpu_utilization_percentage}
        '''
        if isinstance(scale_target_ref, dict):
            scale_target_ref = HorizontalPodAutoscalerSpecScaleTargetRef(**scale_target_ref)
        if isinstance(behavior, dict):
            behavior = HorizontalPodAutoscalerSpecBehavior(**behavior)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992749962498d89f244c2ccbf21cd282b88b4871e2954427a53d140bc363937c)
            check_type(argname="argument max_replicas", value=max_replicas, expected_type=type_hints["max_replicas"])
            check_type(argname="argument scale_target_ref", value=scale_target_ref, expected_type=type_hints["scale_target_ref"])
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument min_replicas", value=min_replicas, expected_type=type_hints["min_replicas"])
            check_type(argname="argument target_cpu_utilization_percentage", value=target_cpu_utilization_percentage, expected_type=type_hints["target_cpu_utilization_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_replicas": max_replicas,
            "scale_target_ref": scale_target_ref,
        }
        if behavior is not None:
            self._values["behavior"] = behavior
        if metric is not None:
            self._values["metric"] = metric
        if min_replicas is not None:
            self._values["min_replicas"] = min_replicas
        if target_cpu_utilization_percentage is not None:
            self._values["target_cpu_utilization_percentage"] = target_cpu_utilization_percentage

    @builtins.property
    def max_replicas(self) -> jsii.Number:
        '''Upper limit for the number of pods that can be set by the autoscaler.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#max_replicas HorizontalPodAutoscaler#max_replicas}
        '''
        result = self._values.get("max_replicas")
        assert result is not None, "Required property 'max_replicas' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scale_target_ref(self) -> "HorizontalPodAutoscalerSpecScaleTargetRef":
        '''scale_target_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_target_ref HorizontalPodAutoscaler#scale_target_ref}
        '''
        result = self._values.get("scale_target_ref")
        assert result is not None, "Required property 'scale_target_ref' is missing"
        return typing.cast("HorizontalPodAutoscalerSpecScaleTargetRef", result)

    @builtins.property
    def behavior(self) -> typing.Optional["HorizontalPodAutoscalerSpecBehavior"]:
        '''behavior block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#behavior HorizontalPodAutoscaler#behavior}
        '''
        result = self._values.get("behavior")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecBehavior"], result)

    @builtins.property
    def metric(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetric"]]]:
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetric"]]], result)

    @builtins.property
    def min_replicas(self) -> typing.Optional[jsii.Number]:
        '''Lower limit for the number of pods that can be set by the autoscaler, defaults to ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#min_replicas HorizontalPodAutoscaler#min_replicas}
        '''
        result = self._values.get("min_replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_cpu_utilization_percentage(self) -> typing.Optional[jsii.Number]:
        '''Target average CPU utilization (represented as a percentage of requested CPU) over all the pods.

        If not specified the default autoscaling policy will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target_cpu_utilization_percentage HorizontalPodAutoscaler#target_cpu_utilization_percentage}
        '''
        result = self._values.get("target_cpu_utilization_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehavior",
    jsii_struct_bases=[],
    name_mapping={"scale_down": "scaleDown", "scale_up": "scaleUp"},
)
class HorizontalPodAutoscalerSpecBehavior:
    def __init__(
        self,
        *,
        scale_down: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleDown", typing.Dict[builtins.str, typing.Any]]]]] = None,
        scale_up: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleUp", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param scale_down: scale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_down HorizontalPodAutoscaler#scale_down}
        :param scale_up: scale_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_up HorizontalPodAutoscaler#scale_up}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12c3da8203cfd5b1d57e52081ae561d94ca2d0de78497fa0cd9ce59091358de5)
            check_type(argname="argument scale_down", value=scale_down, expected_type=type_hints["scale_down"])
            check_type(argname="argument scale_up", value=scale_up, expected_type=type_hints["scale_up"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if scale_down is not None:
            self._values["scale_down"] = scale_down
        if scale_up is not None:
            self._values["scale_up"] = scale_up

    @builtins.property
    def scale_down(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDown"]]]:
        '''scale_down block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_down HorizontalPodAutoscaler#scale_down}
        '''
        result = self._values.get("scale_down")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDown"]]], result)

    @builtins.property
    def scale_up(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUp"]]]:
        '''scale_up block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_up HorizontalPodAutoscaler#scale_up}
        '''
        result = self._values.get("scale_up")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUp"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecBehaviorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__879a9b2c5d56ed1868ceac8a0857d679d4c738541745f745ff993e32c1407dc9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putScaleDown")
    def put_scale_down(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleDown", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c222c47ac711a0d7501efbf852f16d114ea7d372d99b99b9965f7cb7cf762384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScaleDown", [value]))

    @jsii.member(jsii_name="putScaleUp")
    def put_scale_up(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleUp", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc297073a968f46ed7b24b2ffcd1aa6fa06ae9c0fb313fd7befc63d56e153f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScaleUp", [value]))

    @jsii.member(jsii_name="resetScaleDown")
    def reset_scale_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDown", []))

    @jsii.member(jsii_name="resetScaleUp")
    def reset_scale_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleUp", []))

    @builtins.property
    @jsii.member(jsii_name="scaleDown")
    def scale_down(self) -> "HorizontalPodAutoscalerSpecBehaviorScaleDownList":
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleDownList", jsii.get(self, "scaleDown"))

    @builtins.property
    @jsii.member(jsii_name="scaleUp")
    def scale_up(self) -> "HorizontalPodAutoscalerSpecBehaviorScaleUpList":
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleUpList", jsii.get(self, "scaleUp"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownInput")
    def scale_down_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDown"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDown"]]], jsii.get(self, "scaleDownInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleUpInput")
    def scale_up_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUp"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUp"]]], jsii.get(self, "scaleUpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HorizontalPodAutoscalerSpecBehavior]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecBehavior], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecBehavior],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c865ca7514ec716465c6179471f366a75735611b4ec31530c5cc432a88df9a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleDown",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "select_policy": "selectPolicy",
        "stabilization_window_seconds": "stabilizationWindowSeconds",
    },
)
class HorizontalPodAutoscalerSpecBehaviorScaleDown:
    def __init__(
        self,
        *,
        policy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy", typing.Dict[builtins.str, typing.Any]]]],
        select_policy: typing.Optional[builtins.str] = None,
        stabilization_window_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#policy HorizontalPodAutoscaler#policy}
        :param select_policy: Used to specify which policy should be used. If not set, the default value Max is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#select_policy HorizontalPodAutoscaler#select_policy}
        :param stabilization_window_seconds: Number of seconds for which past recommendations should be considered while scaling up or scaling down. This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#stabilization_window_seconds HorizontalPodAutoscaler#stabilization_window_seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a90696c71006e6587039958f8d1e72e5f36941a2cf1950319f847fbf32ec315)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument select_policy", value=select_policy, expected_type=type_hints["select_policy"])
            check_type(argname="argument stabilization_window_seconds", value=stabilization_window_seconds, expected_type=type_hints["stabilization_window_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
        }
        if select_policy is not None:
            self._values["select_policy"] = select_policy
        if stabilization_window_seconds is not None:
            self._values["stabilization_window_seconds"] = stabilization_window_seconds

    @builtins.property
    def policy(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy"]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#policy HorizontalPodAutoscaler#policy}
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy"]], result)

    @builtins.property
    def select_policy(self) -> typing.Optional[builtins.str]:
        '''Used to specify which policy should be used. If not set, the default value Max is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#select_policy HorizontalPodAutoscaler#select_policy}
        '''
        result = self._values.get("select_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stabilization_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds for which past recommendations should be considered while scaling up or scaling down.

        This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#stabilization_window_seconds HorizontalPodAutoscaler#stabilization_window_seconds}
        '''
        result = self._values.get("stabilization_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecBehaviorScaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecBehaviorScaleDownList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleDownList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c066201e04982bc4142c51a3e6bc7f949382ae9a1076dbe03dfe9c16137a5447)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecBehaviorScaleDownOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f96138f1577af02195c1a664c7e66db18303d1f1e28794437e06d43d4bdfbbe)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleDownOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ff2fb2e56bc8bf579ac41d049599a8939a081cf4aaee0835aa82f14ed240fe6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__212ab88d2df666e4aac69c8fcc844179bbc088c2bb3ae0f6f0b5e6272855f69a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__148d32edf6c931538f63d9aee3a347f8c60906db6d074c6ecf4ca3dff8704b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDown]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDown]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDown]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bedba4a1a95a86ed4962919e2d2ace2d8c3ed350164a982104c7f1097ff2da64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecBehaviorScaleDownOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleDownOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed462862491500ebe28d3dd900e8f3668331dd82238387fa01158237a5fc53b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d694db41c3db9f1386f2b772ce8bc828e85ce79981e4332ae97ab18759aae255)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetSelectPolicy")
    def reset_select_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectPolicy", []))

    @jsii.member(jsii_name="resetStabilizationWindowSeconds")
    def reset_stabilization_window_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStabilizationWindowSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyList":
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicyInput")
    def select_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSecondsInput")
    def stabilization_window_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stabilizationWindowSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicy")
    def select_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectPolicy"))

    @select_policy.setter
    def select_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e07469e6c41f269f0a321a9f88c529c25e7df1eb7f7c9d1d09800eb13d57f62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSeconds")
    def stabilization_window_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stabilizationWindowSeconds"))

    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66144bcbf8fe168daa01fc959d88b2f07e57c7ddca4a688b55145a0a30a12ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stabilizationWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c6a63690f1dafee9d53d76b62eb12b613590b2874ca78fbf567810719c655c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy",
    jsii_struct_bases=[],
    name_mapping={"period_seconds": "periodSeconds", "type": "type", "value": "value"},
)
class HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy:
    def __init__(
        self,
        *,
        period_seconds: jsii.Number,
        type: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param period_seconds: Period specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#period_seconds HorizontalPodAutoscaler#period_seconds}
        :param type: Type is used to specify the scaling policy: Percent or Pods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param value: Value contains the amount of change which is permitted by the policy. It must be greater than zero. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd474516c6052f91512884c753d01761cfef643fe7be6d8e354d7259dfc5636)
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "period_seconds": period_seconds,
            "type": type,
            "value": value,
        }

    @builtins.property
    def period_seconds(self) -> jsii.Number:
        '''Period specifies the window of time for which the policy should hold true.

        PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#period_seconds HorizontalPodAutoscaler#period_seconds}
        '''
        result = self._values.get("period_seconds")
        assert result is not None, "Required property 'period_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type is used to specify the scaling policy: Percent or Pods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Value contains the amount of change which is permitted by the policy. It must be greater than zero.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c236355a6662cf97f04625b24edc8f9447c1a4783c8397651db9deb89ccf279)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81fd476e7524a5e8f5a5388e1e78084e0c84cdb214e8e7e89c473c7885835fc5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b078d724448aac52923cb64fd6932145ea3a7e56023243460ccc37586758b305)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6cb97bf25fdc18171986f6391ab980bad8646c747d140be77ae16e472e7d510b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c4124dafe577591ccb40e2260bb19df73bdac25c6ecd2c73c16d97bd01793ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b825b5e6fd4f24e16e60c79738ce54fb7eed86f9e4fed648b6a51d73acaeb05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__79041e186363921e65a1697d0f6f016d3a21738703e02c5fec44bbab34d9b734)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb88844a6671608a23639baf757fcea85c6c0390e27a6f034980a81af17f343c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7630023631d4f1141767c48d6a8c2768a95c6a75f9b9f391c99bb874c34b68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c4ef3ea4e3fe57168255adaf04312bae296f517fd04ae54c7d77b250ce2f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1657b0402a546ec6030bb1b9823c4aa76408ca79344714ad31d640d32df90ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleUp",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "select_policy": "selectPolicy",
        "stabilization_window_seconds": "stabilizationWindowSeconds",
    },
)
class HorizontalPodAutoscalerSpecBehaviorScaleUp:
    def __init__(
        self,
        *,
        policy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy", typing.Dict[builtins.str, typing.Any]]]],
        select_policy: typing.Optional[builtins.str] = None,
        stabilization_window_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#policy HorizontalPodAutoscaler#policy}
        :param select_policy: Used to specify which policy should be used. If not set, the default value Max is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#select_policy HorizontalPodAutoscaler#select_policy}
        :param stabilization_window_seconds: Number of seconds for which past recommendations should be considered while scaling up or scaling down. This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#stabilization_window_seconds HorizontalPodAutoscaler#stabilization_window_seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe31fffaf0741da8129ef39c9813a3b041ded4927fd7e76a9750af5b8725687a)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument select_policy", value=select_policy, expected_type=type_hints["select_policy"])
            check_type(argname="argument stabilization_window_seconds", value=stabilization_window_seconds, expected_type=type_hints["stabilization_window_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
        }
        if select_policy is not None:
            self._values["select_policy"] = select_policy
        if stabilization_window_seconds is not None:
            self._values["stabilization_window_seconds"] = stabilization_window_seconds

    @builtins.property
    def policy(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy"]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#policy HorizontalPodAutoscaler#policy}
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy"]], result)

    @builtins.property
    def select_policy(self) -> typing.Optional[builtins.str]:
        '''Used to specify which policy should be used. If not set, the default value Max is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#select_policy HorizontalPodAutoscaler#select_policy}
        '''
        result = self._values.get("select_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stabilization_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds for which past recommendations should be considered while scaling up or scaling down.

        This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#stabilization_window_seconds HorizontalPodAutoscaler#stabilization_window_seconds}
        '''
        result = self._values.get("stabilization_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecBehaviorScaleUp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecBehaviorScaleUpList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleUpList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a500070053425c056ce0d644f805a2469b734946ba4903876ac0d8b45cfb2782)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecBehaviorScaleUpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa85205f0683ea67fd902847d62630cccf39fef9f803464bfddc411bde1d4a58)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleUpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d108096bbc8d3944fb909148855cd841bf2077df5c1f9f6f5866892b1f2b72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cae50be7736ac8d9c30c9504b0cc0fd55a588e2ebc8fe298598b4ef2c47f812f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbfb4e50281090b6722eab4e59943d8a0ee86120b1187eeb887f0f91a244ff74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUp]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0f4ff7f47f033663d618b3610583c8edb1f00b5cf7003a5fca88be82d190d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecBehaviorScaleUpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleUpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2467afafd934a904b7d7f9d8a6270dfd18d0dddfb8b2aba618c40b0c7d68fbb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28d432ef22dd89c94dca6167a367d27645ce8b0cdb1af6db97b8ffbf8ca393e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetSelectPolicy")
    def reset_select_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectPolicy", []))

    @jsii.member(jsii_name="resetStabilizationWindowSeconds")
    def reset_stabilization_window_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStabilizationWindowSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyList":
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicyInput")
    def select_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSecondsInput")
    def stabilization_window_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stabilizationWindowSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicy")
    def select_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectPolicy"))

    @select_policy.setter
    def select_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ccfa75f49fa0c8e37022aff1e0dfe7005e26b96c533fecc4342f22cdd1d39f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSeconds")
    def stabilization_window_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stabilizationWindowSeconds"))

    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d53c425affa1954c03ea113cbfdea6cdc4bb5ef611d9ed5dfa72e7b8fa47eae7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stabilizationWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2315244fd401ef346e5605173cbd4da11d218b006ea5c5d6f94af629d9f1a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy",
    jsii_struct_bases=[],
    name_mapping={"period_seconds": "periodSeconds", "type": "type", "value": "value"},
)
class HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy:
    def __init__(
        self,
        *,
        period_seconds: jsii.Number,
        type: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param period_seconds: Period specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#period_seconds HorizontalPodAutoscaler#period_seconds}
        :param type: Type is used to specify the scaling policy: Percent or Pods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param value: Value contains the amount of change which is permitted by the policy. It must be greater than zero. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f8003de3aed5535332b2a2bb6592f1ee0625083170dc5caf04f24cb0841241f)
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "period_seconds": period_seconds,
            "type": type,
            "value": value,
        }

    @builtins.property
    def period_seconds(self) -> jsii.Number:
        '''Period specifies the window of time for which the policy should hold true.

        PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#period_seconds HorizontalPodAutoscaler#period_seconds}
        '''
        result = self._values.get("period_seconds")
        assert result is not None, "Required property 'period_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type is used to specify the scaling policy: Percent or Pods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Value contains the amount of change which is permitted by the policy. It must be greater than zero.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8744ac4813532f4a9a35230bbb9dd9003b17ce69d44c61ee85c5283fe52d8f9e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0803da9a5b3dac8bf51e6a4b8492d433898149ac9d113b49d54fb90e498418b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a4d75e2616423ce2577f4bc8872d216a642bd5c05eee5e7944bb5f1e4ebbf89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f311becb7a186f8208f8a2124359b65d5d1fc0e22811edb62ec49d2935f356b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4326e27abfbfff702dc7c7b65512a6927b76da01f39c1be0cb0f94af8f2e5021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb2e9de6979d2500b4c00b2505408d039bcf6bcc32c42e5d67758230a1e3cc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c03dd4d66ec11214ec503f1472359d6eae184cc07383c9c3c7fc917cb83c331)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__167381baec20c06fceaf18b87d8f2aef3fc1ec8992beae695e158a2ece355fbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8617e5c75250104bc9056baf8dd862d94aa826ea14da204663eeff23d4b244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33f51b8c1950ac4e96f1bba0997248488be5f7134891da8b9e535137f392d623)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41cbad3fec02cb6286125c24246438674b9b622f79a816ee6c24807f3f1d04da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetric",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "container_resource": "containerResource",
        "external": "external",
        "object": "object",
        "pods": "pods",
        "resource": "resource",
    },
)
class HorizontalPodAutoscalerSpecMetric:
    def __init__(
        self,
        *,
        type: builtins.str,
        container_resource: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricContainerResource", typing.Dict[builtins.str, typing.Any]]] = None,
        external: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricExternal", typing.Dict[builtins.str, typing.Any]]] = None,
        object: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricObject", typing.Dict[builtins.str, typing.Any]]] = None,
        pods: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricPods", typing.Dict[builtins.str, typing.Any]]] = None,
        resource: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricResource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: type is the type of metric source. It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param container_resource: container_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#container_resource HorizontalPodAutoscaler#container_resource}
        :param external: external block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#external HorizontalPodAutoscaler#external}
        :param object: object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#object HorizontalPodAutoscaler#object}
        :param pods: pods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#pods HorizontalPodAutoscaler#pods}
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#resource HorizontalPodAutoscaler#resource}
        '''
        if isinstance(container_resource, dict):
            container_resource = HorizontalPodAutoscalerSpecMetricContainerResource(**container_resource)
        if isinstance(external, dict):
            external = HorizontalPodAutoscalerSpecMetricExternal(**external)
        if isinstance(object, dict):
            object = HorizontalPodAutoscalerSpecMetricObject(**object)
        if isinstance(pods, dict):
            pods = HorizontalPodAutoscalerSpecMetricPods(**pods)
        if isinstance(resource, dict):
            resource = HorizontalPodAutoscalerSpecMetricResource(**resource)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e16c7637019cea7be16dca52170172975feb90f9be169775304d46f027be72bf)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument container_resource", value=container_resource, expected_type=type_hints["container_resource"])
            check_type(argname="argument external", value=external, expected_type=type_hints["external"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument pods", value=pods, expected_type=type_hints["pods"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if container_resource is not None:
            self._values["container_resource"] = container_resource
        if external is not None:
            self._values["external"] = external
        if object is not None:
            self._values["object"] = object
        if pods is not None:
            self._values["pods"] = pods
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def type(self) -> builtins.str:
        '''type is the type of metric source.

        It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_resource(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricContainerResource"]:
        '''container_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#container_resource HorizontalPodAutoscaler#container_resource}
        '''
        result = self._values.get("container_resource")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricContainerResource"], result)

    @builtins.property
    def external(self) -> typing.Optional["HorizontalPodAutoscalerSpecMetricExternal"]:
        '''external block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#external HorizontalPodAutoscaler#external}
        '''
        result = self._values.get("external")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricExternal"], result)

    @builtins.property
    def object(self) -> typing.Optional["HorizontalPodAutoscalerSpecMetricObject"]:
        '''object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#object HorizontalPodAutoscaler#object}
        '''
        result = self._values.get("object")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricObject"], result)

    @builtins.property
    def pods(self) -> typing.Optional["HorizontalPodAutoscalerSpecMetricPods"]:
        '''pods block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#pods HorizontalPodAutoscaler#pods}
        '''
        result = self._values.get("pods")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricPods"], result)

    @builtins.property
    def resource(self) -> typing.Optional["HorizontalPodAutoscalerSpecMetricResource"]:
        '''resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#resource HorizontalPodAutoscaler#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricResource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricContainerResource",
    jsii_struct_bases=[],
    name_mapping={"container": "container", "name": "name", "target": "target"},
)
class HorizontalPodAutoscalerSpecMetricContainerResource:
    def __init__(
        self,
        *,
        container: builtins.str,
        name: builtins.str,
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricContainerResourceTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param container: name of the container in the pods of the scaling target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#container HorizontalPodAutoscaler#container}
        :param name: name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerSpecMetricContainerResourceTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4947ced4c433b432267a7584bf8156b3da61fdfbe31f7a953dc074b07cc8c413)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container": container,
            "name": name,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def container(self) -> builtins.str:
        '''name of the container in the pods of the scaling target.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#container HorizontalPodAutoscaler#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''name of the resource in question.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricContainerResourceTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricContainerResourceTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricContainerResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricContainerResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricContainerResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5422e87d5094719a4bf2272d3f6278982265d30c0d8d0fa3d891a1baf9b77839)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        value_ = HorizontalPodAutoscalerSpecMetricContainerResourceTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerSpecMetricContainerResourceTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricContainerResourceTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricContainerResourceTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricContainerResourceTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420b10adda8cc40caa705a860acb37b5d6c98333cc7d0893a1ec7d47f4ce2e8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317c99e6cb3d23b5712e22154d313a288fd5b6559192225b359cf07980508077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResource]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b9fb75adc91013ff98d00bc82b6940d5e39078907d032f7393a1d61607be04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricContainerResourceTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerSpecMetricContainerResourceTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__432ec4e2af67b22f2f1100b6f8057c5aca386b3a2ab8b93b55afd6edb8b761b8)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricContainerResourceTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricContainerResourceTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricContainerResourceTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ca07d19af5060b23b79fc57923d92e0e458757ae9c42bdf3da84af6ac543de1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766b5f31128947478731cedc28f790cdd27746524af71711eeb4b26d26805845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a5bd13b568ecc90c9d3d5ea48120c91b99755fa3be320a43f86d762c743903d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e79c21d1c760c9d65613b53a73f1a9a3eaf19b8b122f2df21b1c8e5263339871)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b7fe60498f20db02db4ee68848578bc4e0ab45cce9d6e41c80b0a6b9815c02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResourceTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResourceTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResourceTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7514b0cdd14ba49ffb7280e25ee69688cedc80863def90606eada985ca89dead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternal",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "target": "target"},
)
class HorizontalPodAutoscalerSpecMetricExternal:
    def __init__(
        self,
        *,
        metric: typing.Union["HorizontalPodAutoscalerSpecMetricExternalMetric", typing.Dict[builtins.str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricExternalTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        if isinstance(metric, dict):
            metric = HorizontalPodAutoscalerSpecMetricExternalMetric(**metric)
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerSpecMetricExternalTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de6b00fdcc1a1193670a6ede13fcbfd84929b3679b59dbde3772a03fc43e12ec)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric(self) -> "HorizontalPodAutoscalerSpecMetricExternalMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("HorizontalPodAutoscalerSpecMetricExternalMetric", result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricExternalTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricExternalTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricExternal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetric",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "selector": "selector"},
)
class HorizontalPodAutoscalerSpecMetricExternalMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricExternalMetricSelector", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe0cf092610e2a40dbacc9341ad7eea79db9241937df5290c60c6364803756f3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the given metric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricExternalMetricSelector"]]]:
        '''selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricExternalMetricSelector"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricExternalMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricExternalMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf5f9e9277e980499edc189a1816d5905674b5ea9ea656594cc82fe52d3684f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelector")
    def put_selector(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricExternalMetricSelector", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e4f956d3f7c95d06917a23be3551a5988b98baa415c06f877958d6b824aa8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSelector", [value]))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorList":
        return typing.cast("HorizontalPodAutoscalerSpecMetricExternalMetricSelectorList", jsii.get(self, "selector"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricExternalMetricSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricExternalMetricSelector"]]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad2ed080ea3686e2ce77da5d050b4f6edd9c32b79dcec2e2e4bf0ca111034d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricExternalMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricExternalMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricExternalMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ca433fe2e5ee21852df73433dc0e740fadb4b0fde6ac0001df97c7d2b6986a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class HorizontalPodAutoscalerSpecMetricExternalMetricSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_expressions HorizontalPodAutoscaler#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_labels HorizontalPodAutoscaler#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d40d36e49e2fb452b443a68124669097b40e9203874088aa6cf36d3a1634fcab)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_expressions HorizontalPodAutoscaler#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_labels HorizontalPodAutoscaler#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricExternalMetricSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricExternalMetricSelectorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricSelectorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__306a545f478e12eca7ac161ddaa169b0ec6f340cc4d7772b9e5002da3fcaa723)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b72cd263f2d30b6467be2dda2de9ccd0e6a26e681a962ac2bae3f0bc78fb46cf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricExternalMetricSelectorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7313ada5e52e3e9ef374e0fbb66ebb394308c049af1dc7b16f63b93b53aa02ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d8eff05e7813f4349282abb4be5445568290e5d9b1cd65cf6bcad321c13fd75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__680428e7d4d1a5a099bceefa26bb3f1da35b2133c66d2b361319e31476ada680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelector]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelector]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3123934ddfb56e9db41c044d60b89247010b43ffbc2be516fc015c56d26d2f67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#key HorizontalPodAutoscaler#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#operator HorizontalPodAutoscaler#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#values HorizontalPodAutoscaler#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4d0ea6ce328f2b6153aa113f43da508704b16b6d964e3a8a33e04ba9f7db433)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#key HorizontalPodAutoscaler#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#operator HorizontalPodAutoscaler#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#values HorizontalPodAutoscaler#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddb5ad0fed9b3968ed640cdb0af653be40f13f369f787cb9d3474db8e24668db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baf835b43a1a7d570f71483953d96553a52230f18bda8de4cfef15fe6634992b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aedbc13acfa6776f6e1ccaa9ddcd323ff8fa7951c0b526e60c213456daea2a06)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a654d0886ba8a52ace53e0a8b193b1023eabefa87b877938980f45819bda4662)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86553a53a986509111a57026a00c569fb8f0165adfff80d5f4cdbc9a2a90a2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865512bbf61fc9de2d91c0e373830e4ef95dc5a3f03e5255768eef476cad9e72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5c0087f97453078e5020073c85a0636738e940150db82ac5297e30a9f6a6d10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ec621bc07c032a9835d9015f9ec623fc37d9d91d759502427d1e0bd00daea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7152f779d0010cc757300cbdead859e13f729f9f617ed18d2aa73246d1378907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b3ea9aa241f121a6cd27074b87e838db2a51eabb29acc5686fab1936425ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b861fe853cc61f006754b5910b468748b5c5b5c0ef6d44e66d326bf12ef554ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricExternalMetricSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalMetricSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1b0a0dc9e66f134ce987b928f4bbf6ad0d876e2e16b17db81a1383f32a8ecd0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a14fccbb4ff3e804fd8d768989334acf18a337b756eae09af9f4b60b2131f43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsList:
        return typing.cast(HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc4b8453b33bb822bcc8a7c3384d0b4dd8e98bf8965e96f93b71d503c8e8e88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57cd80724a4150a013b97fd517594ad09f62c4c43a27da88b90f64d2d41af80c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricExternalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__501d2521427a41096667231c1d8784d7d8ef9287091702bbf6a4af492bdb8644)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        value = HorizontalPodAutoscalerSpecMetricExternalMetric(
            name=name, selector=selector
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        value_ = HorizontalPodAutoscalerSpecMetricExternalTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> HorizontalPodAutoscalerSpecMetricExternalMetricOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricExternalMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerSpecMetricExternalTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricExternalTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricExternalMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricExternalMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricExternalTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricExternalTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricExternal]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricExternal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricExternal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b845b32d6a9ce99b5603d8fd36e9613e38314ac33a2adc5b18966bac377bcb91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerSpecMetricExternalTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a1e0794b343d5d9650f97584a69e33e555475c4a4ce411d7f257c630d7b0f7)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricExternalTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricExternalTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricExternalTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7164d9d8c1745a85df21b3a9bb6311782b9a35ad6359ab9c6244c1ea44996c5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0acd014bb28a0146d3c92a72410f0d48c0985f95868f005930c4907d3309742d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0dc76c6d38200358afa3efb68bbd04ca4250a2c1d58439ff6ff91934d2ab730)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b4c342f5c4b1557a34f643038aeba3c4f9b4132fc9e999cb073332e5f5f022)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f274f15f279073807f3893765b79aa075292c61a4ff59549f0e24869e178b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricExternalTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricExternalTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricExternalTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d40e118dfd3a4e31986e26949f546df5b237514e0a5c3cf29d09844095f628a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9220a9bc62febab0c87e2ee7f7d60100d4bd9851c110231c65e3c8dff20f416)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a405ace3a6366ca7a99e4bc19a5476ff7db4669b2d2650898554a4d8fb9040)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__423319d1b677a34c76b754bdf21bacc7f81f5e3dfcc2e75074235ce1a489dca4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88506621d09edea97de51a30a3fea34a7d950260c8363f75ee7fa4b06db1de34)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d60ea8311a1002e8631ad2b37d41027ecc9c2e4b7689277c6930fff9ab7e4ffb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetric]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetric]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetric]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f249ab484c1eaf770677699bdd78f1e8866531f63f7ca6519304552307fe4e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObject",
    jsii_struct_bases=[],
    name_mapping={
        "described_object": "describedObject",
        "metric": "metric",
        "target": "target",
    },
)
class HorizontalPodAutoscalerSpecMetricObject:
    def __init__(
        self,
        *,
        described_object: typing.Union["HorizontalPodAutoscalerSpecMetricObjectDescribedObject", typing.Dict[builtins.str, typing.Any]],
        metric: typing.Union["HorizontalPodAutoscalerSpecMetricObjectMetric", typing.Dict[builtins.str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricObjectTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param described_object: described_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#described_object HorizontalPodAutoscaler#described_object}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        if isinstance(described_object, dict):
            described_object = HorizontalPodAutoscalerSpecMetricObjectDescribedObject(**described_object)
        if isinstance(metric, dict):
            metric = HorizontalPodAutoscalerSpecMetricObjectMetric(**metric)
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerSpecMetricObjectTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a2a625c0d0fe01a16c233aa4b54322aedc1ad0478e99f38b369a73c72a0310)
            check_type(argname="argument described_object", value=described_object, expected_type=type_hints["described_object"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "described_object": described_object,
            "metric": metric,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def described_object(
        self,
    ) -> "HorizontalPodAutoscalerSpecMetricObjectDescribedObject":
        '''described_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#described_object HorizontalPodAutoscaler#described_object}
        '''
        result = self._values.get("described_object")
        assert result is not None, "Required property 'described_object' is missing"
        return typing.cast("HorizontalPodAutoscalerSpecMetricObjectDescribedObject", result)

    @builtins.property
    def metric(self) -> "HorizontalPodAutoscalerSpecMetricObjectMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("HorizontalPodAutoscalerSpecMetricObjectMetric", result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricObjectTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricObjectTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectDescribedObject",
    jsii_struct_bases=[],
    name_mapping={"api_version": "apiVersion", "kind": "kind", "name": "name"},
)
class HorizontalPodAutoscalerSpecMetricObjectDescribedObject:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#api_version HorizontalPodAutoscaler#api_version}
        :param kind: Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#kind HorizontalPodAutoscaler#kind}
        :param name: Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e240b1834490b7e5260cbc1a4db6dbfc1a400328be932cd38aac4b32c01785e)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_version": api_version,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_version(self) -> builtins.str:
        '''API version of the referent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#api_version HorizontalPodAutoscaler#api_version}
        '''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#kind HorizontalPodAutoscaler#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricObjectDescribedObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricObjectDescribedObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectDescribedObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97b20ffba8b030e3011c293e3cce2ff60f35661af1031240a72363a568dc9189)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2aefe8ef9a430faf42d28c165e72871eec6512ac47e7ab310471527a804347)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baba0ba7e3b3fd847f69688a1aff39533508c46ddf41d2031a29a072db2280fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9033dc761be2cbbdf9ddacd96b5fc19acdb3b13641d939f0f9f83afed0d7a0cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObjectDescribedObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObjectDescribedObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricObjectDescribedObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf63ff7dcb139ab2e01862f8fc42d0e639d2e17387c7602685f79f9360b4ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetric",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "selector": "selector"},
)
class HorizontalPodAutoscalerSpecMetricObjectMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricObjectMetricSelector", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0074dbd80d64a5540aae969585f366b759bcabea899515dd1b6baa16827a2ed3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the given metric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricObjectMetricSelector"]]]:
        '''selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricObjectMetricSelector"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricObjectMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricObjectMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__443f3864f0db186298082c311c08e580e98a932a8939312a9cc6e6c610faa933)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelector")
    def put_selector(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricObjectMetricSelector", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb9403ed94087700d8412e0dc829ca78e7c1a4aa1b6e3d3c40869c75a77d8be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSelector", [value]))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorList":
        return typing.cast("HorizontalPodAutoscalerSpecMetricObjectMetricSelectorList", jsii.get(self, "selector"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricObjectMetricSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricObjectMetricSelector"]]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65fa98c7e2053ff16b9d700f9327641120439de88ef52d640a457b222084b7c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObjectMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObjectMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricObjectMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a97040881766607d69b127107db6e0ab2d550d9bad5e93b6286602189c0b600a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class HorizontalPodAutoscalerSpecMetricObjectMetricSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_expressions HorizontalPodAutoscaler#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_labels HorizontalPodAutoscaler#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662d8b0c38b55860a2370ca10a3f4f4b3a9319c4012eedf42c3df98cd207869f)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_expressions HorizontalPodAutoscaler#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_labels HorizontalPodAutoscaler#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricObjectMetricSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricObjectMetricSelectorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricSelectorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70c85076e18422efa9a6a79aec5f39454b1ccec3402cf806ea4c4300ca1a611a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da2e5f40a70ba12a2e189b79fbd88701cfaf20a58ae4fa0b586ea2a5fb6d7b97)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricObjectMetricSelectorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b8486039104d46892e68d2aa190d55e5c7e48c161f486284988cb117e5e814f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c588d8c8d232bfb91cf4d87f836e7b643b1d4831a6ae6aa97af48f9f3e87367e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af79563a9631bb8a756d9c9a29bf2b247876283a7505f4ac84cddb127e84d215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelector]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelector]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51e5d128ee62cccb61dfcc87f580ec9080bd57074822ddf953f12d834ad95651)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#key HorizontalPodAutoscaler#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#operator HorizontalPodAutoscaler#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#values HorizontalPodAutoscaler#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94599473ccbca7c7809a109baa9096f6cfe2f265a1159ca03acffb38f9d42e2)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#key HorizontalPodAutoscaler#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#operator HorizontalPodAutoscaler#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#values HorizontalPodAutoscaler#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00034ea4f52a06d142e8776c29ca351fd3ca0d4becc2e5af96cfe966d5ebeb68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f35c55e27f096d2500705ad63a71712c08395cc77d8d1f01eeca6ed0513327)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd47f4c823c0ead4c487815cdc7f66af912e59aafe2711efea3f0f86cb898a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e82b84b577baf1d8981455907d58636881b4d12985ba6bc19e3d337a592ce771)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c75370b1bdbf851a17a37b6ccd86b8e386ade4ba51f16119fae84d567889d499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ffb77807e8177fa44ff42386fbe585b29fef3f1e8c931df7fc2aced87d3d99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00cb92f39e38e4d23732241c4deca528ba469bf60f069d7343632b08d1ef20ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1550a189b24587c069af96b8bde9fea59001bb566800355f8a676fe5614296)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ee8899f6394592af79b8488005e8fbbd956dbfeb43c3333f1bbc975e4800cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd050e5d5c9f2a429f4d0800b46c716c26a6659a0909409ea3b2803e96243821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c0b498bcc38366478df03848e337073e5077a8a93c7b9b6602d5d7e7574a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricObjectMetricSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectMetricSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cabbc502f93cd25ed31dc39ab4df6dffb2920c5529114e648be537a2e830350)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56285e95d699d1bd699b9a6fd2aeda0faa3d923fe3ca8bd83a21eaa3cf2cc354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsList:
        return typing.cast(HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd87731ce2852eca028524f87f004c57d83e725c360c11c2e6d3c9079c535683)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__914d18eb5af559afa120da45bb2763679095dbe5a47b1b77d2cdf563d9ac536e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c660c2612035b67e3f6d0cfa14388f23c1ca90124d44703450da525e038d1659)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDescribedObject")
    def put_described_object(
        self,
        *,
        api_version: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#api_version HorizontalPodAutoscaler#api_version}
        :param kind: Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#kind HorizontalPodAutoscaler#kind}
        :param name: Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        value = HorizontalPodAutoscalerSpecMetricObjectDescribedObject(
            api_version=api_version, kind=kind, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putDescribedObject", [value]))

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        value = HorizontalPodAutoscalerSpecMetricObjectMetric(
            name=name, selector=selector
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        value_ = HorizontalPodAutoscalerSpecMetricObjectTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="describedObject")
    def described_object(
        self,
    ) -> HorizontalPodAutoscalerSpecMetricObjectDescribedObjectOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricObjectDescribedObjectOutputReference, jsii.get(self, "describedObject"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> HorizontalPodAutoscalerSpecMetricObjectMetricOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricObjectMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "HorizontalPodAutoscalerSpecMetricObjectTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricObjectTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="describedObjectInput")
    def described_object_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObjectDescribedObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObjectDescribedObject], jsii.get(self, "describedObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObjectMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObjectMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricObjectTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricObjectTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2713b00cfec5cf1aa279feb88d7b856fc18fd12e3746a05abcf62e13760753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerSpecMetricObjectTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c9f97b6b09ddabeb82e670b131459a58c1040ab7a20e0f93f94b1e1acffebb)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricObjectTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricObjectTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricObjectTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__383be752630640796a6c4ac81b0b36c06742c30b58adf5f891ef1640c90a418d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b7da196e471d009efa34e7d36e32176118302a25ad752a7c05af350a7ecfba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436f4f9c3e07909db1e1be1fb1223d99462d0ff189a1ac00622d5374717d9286)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e7681fc4ebde3ce943199ebe10015114869dbacea90b33fdae13131fc446f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234352b2c809197f4e5d41669b178bcb1c88966bf1b3984ec2b299e6ba6c0585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObjectTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObjectTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricObjectTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15ed61006efa5402ceceb0d79af6bc14d1f467358663190693cfcf9b1711e576)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__253fecc3dc155c02ed8cc847c82005673968e35e06c8c4e3d63fb166e837351f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putContainerResource")
    def put_container_resource(
        self,
        *,
        container: builtins.str,
        name: builtins.str,
        target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricContainerResourceTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param container: name of the container in the pods of the scaling target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#container HorizontalPodAutoscaler#container}
        :param name: name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        value = HorizontalPodAutoscalerSpecMetricContainerResource(
            container=container, name=name, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putContainerResource", [value]))

    @jsii.member(jsii_name="putExternal")
    def put_external(
        self,
        *,
        metric: typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetric, typing.Dict[builtins.str, typing.Any]],
        target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        value = HorizontalPodAutoscalerSpecMetricExternal(metric=metric, target=target)

        return typing.cast(None, jsii.invoke(self, "putExternal", [value]))

    @jsii.member(jsii_name="putObject")
    def put_object(
        self,
        *,
        described_object: typing.Union[HorizontalPodAutoscalerSpecMetricObjectDescribedObject, typing.Dict[builtins.str, typing.Any]],
        metric: typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetric, typing.Dict[builtins.str, typing.Any]],
        target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param described_object: described_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#described_object HorizontalPodAutoscaler#described_object}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        value = HorizontalPodAutoscalerSpecMetricObject(
            described_object=described_object, metric=metric, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putObject", [value]))

    @jsii.member(jsii_name="putPods")
    def put_pods(
        self,
        *,
        metric: typing.Union["HorizontalPodAutoscalerSpecMetricPodsMetric", typing.Dict[builtins.str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricPodsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        value = HorizontalPodAutoscalerSpecMetricPods(metric=metric, target=target)

        return typing.cast(None, jsii.invoke(self, "putPods", [value]))

    @jsii.member(jsii_name="putResource")
    def put_resource(
        self,
        *,
        name: builtins.str,
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricResourceTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        value = HorizontalPodAutoscalerSpecMetricResource(name=name, target=target)

        return typing.cast(None, jsii.invoke(self, "putResource", [value]))

    @jsii.member(jsii_name="resetContainerResource")
    def reset_container_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerResource", []))

    @jsii.member(jsii_name="resetExternal")
    def reset_external(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternal", []))

    @jsii.member(jsii_name="resetObject")
    def reset_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObject", []))

    @jsii.member(jsii_name="resetPods")
    def reset_pods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPods", []))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="containerResource")
    def container_resource(
        self,
    ) -> HorizontalPodAutoscalerSpecMetricContainerResourceOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricContainerResourceOutputReference, jsii.get(self, "containerResource"))

    @builtins.property
    @jsii.member(jsii_name="external")
    def external(self) -> HorizontalPodAutoscalerSpecMetricExternalOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricExternalOutputReference, jsii.get(self, "external"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> HorizontalPodAutoscalerSpecMetricObjectOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricObjectOutputReference, jsii.get(self, "object"))

    @builtins.property
    @jsii.member(jsii_name="pods")
    def pods(self) -> "HorizontalPodAutoscalerSpecMetricPodsOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricPodsOutputReference", jsii.get(self, "pods"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> "HorizontalPodAutoscalerSpecMetricResourceOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricResourceOutputReference", jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="containerResourceInput")
    def container_resource_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResource]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResource], jsii.get(self, "containerResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="externalInput")
    def external_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricExternal]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricExternal], jsii.get(self, "externalInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[HorizontalPodAutoscalerSpecMetricObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricObject], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="podsInput")
    def pods_input(self) -> typing.Optional["HorizontalPodAutoscalerSpecMetricPods"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricPods"], jsii.get(self, "podsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricResource"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricResource"], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8fb87bcff723c22895ba9b8a20da80b0840c8c4c335d2e27d112639e38566a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetric, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetric, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetric, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80523c5d6bd997b3eb07e037601bcd0dba7063a2c5f2532d77df30d14c8206bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPods",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "target": "target"},
)
class HorizontalPodAutoscalerSpecMetricPods:
    def __init__(
        self,
        *,
        metric: typing.Union["HorizontalPodAutoscalerSpecMetricPodsMetric", typing.Dict[builtins.str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricPodsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        if isinstance(metric, dict):
            metric = HorizontalPodAutoscalerSpecMetricPodsMetric(**metric)
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerSpecMetricPodsTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__219d5f10959824a56bf59745b3766f58c343f0abef47caf6314e61cf569f3856)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric(self) -> "HorizontalPodAutoscalerSpecMetricPodsMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#metric HorizontalPodAutoscaler#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("HorizontalPodAutoscalerSpecMetricPodsMetric", result)

    @builtins.property
    def target(self) -> typing.Optional["HorizontalPodAutoscalerSpecMetricPodsTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricPodsTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricPods(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetric",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "selector": "selector"},
)
class HorizontalPodAutoscalerSpecMetricPodsMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricPodsMetricSelector", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27691f1eafa2df526fbe23ac3fa879592b8cf015e0843d43e01663fbaed4938c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the given metric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricPodsMetricSelector"]]]:
        '''selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricPodsMetricSelector"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricPodsMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricPodsMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__941b73ca1c5b9f549afdc71a67e4a0d61e558af820dcf200792d74ba20a1c318)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelector")
    def put_selector(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricPodsMetricSelector", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466617c5a6d02b94b330968bf55167500f19b20c54b74b8025fde9745d2e18bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSelector", [value]))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorList":
        return typing.cast("HorizontalPodAutoscalerSpecMetricPodsMetricSelectorList", jsii.get(self, "selector"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricPodsMetricSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricPodsMetricSelector"]]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4215fed70dffc43e2bc284a6cb14d88262d4755589d2c69e6ef980fbba81dd47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricPodsMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricPodsMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricPodsMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__339f62d8ac554d1c19a72e5fc3a7a25c319e2b749707d6d62fe89f1c4c174a05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class HorizontalPodAutoscalerSpecMetricPodsMetricSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_expressions HorizontalPodAutoscaler#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_labels HorizontalPodAutoscaler#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee076b9d18da55f8bea8a76a3eb0fdbea46bf040e56c907ee8640cf7f358f2cc)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_expressions HorizontalPodAutoscaler#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#match_labels HorizontalPodAutoscaler#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricPodsMetricSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricPodsMetricSelectorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricSelectorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9baf115670935f86f66c6b9af199cba79f6c107aa78ce29d6433d85d72325c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b995f8078e5a363420b63c3995e6a10cb20128c0b12188474580bacca9d3f8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricPodsMetricSelectorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd5dcbbfbf2da4c353500d95fda43343ed8ef4ea20f4621f8e09068126b006b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b430649c1e1786a27d1228d949ae483b0578963c7666e39bf3eb926e402b945b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d366251ed6455fe3bb73f121747728669885bad1654df2537dac8b9d842c8bc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelector]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelector]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9906601b67f22868a19f7801609b55f114ba51868ba9ca0bad3c1ba22d255a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#key HorizontalPodAutoscaler#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#operator HorizontalPodAutoscaler#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#values HorizontalPodAutoscaler#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a61a7e564ede98ddf1e67007921467f72a732e605a123ec0a8d2392e55b6bd)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#key HorizontalPodAutoscaler#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#operator HorizontalPodAutoscaler#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#values HorizontalPodAutoscaler#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72e631613287428fc7530f7eed488e867fd32df48dbd8806c118c588bcc63eb4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f097a6d24c05edfa58ad56ecbcb0cf11c7a2d1a183ca3d49b576b1aa253af65e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbadcb05b7b5651d4ae0c4236e012e36affcd3dc77cf6cbed7057d188540f13b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ac42b85e7d3bab462bc1a57ab5434e7c79718bfde1ad9f3adc541a47c7cd6c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4608bb55c859fdc2999346803893e595b06a1240f321d132038967d8693276fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753b34365d8d06e1c85c8b325ad8eee737c05f876cdfc6e83242198bfc47990b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4ea94aa155fb7f274c3af9d25fab6a42dbd4ba4bd469f3be9d4c56159009cf3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d663d08be0338ddd37637efc5a62b78afb7ce8d3558f3b9e5100bfcd4a9a77b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0c906ec1cbba11341ebbef8842bdeb3a1eb39b6d1f61cb20185f347ef7be5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55dbcebda5506099d69a933018f8b7d9c795c93175460555b9164d52eb1b5d88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5727c03fe95946d91d025798c9422039b5b2c56fae31a287d3f6a5bfab2d13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricPodsMetricSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsMetricSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78eaf19e28734b6beb6e659d22b27433e748eee344a99fdc0dc34727a3fe89b0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1ca02da8d6cba9906155d759fa1b1cd8de8c8f47215754e0159640a96ddec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsList:
        return typing.cast(HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479af1ff25098bc46a9590ae41afb9a63a812afbc94b8a4926d342b70c5a7bea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0448fee6bc3ba9c56057f36c40b1b124535247c56380399f69bdf3e6369db3bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecMetricPodsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0308e8b12536115a2e6de3c05a424c95186c9079805bc4c7e6ceef539aca9c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#selector HorizontalPodAutoscaler#selector}
        '''
        value = HorizontalPodAutoscalerSpecMetricPodsMetric(
            name=name, selector=selector
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        value_ = HorizontalPodAutoscalerSpecMetricPodsTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> HorizontalPodAutoscalerSpecMetricPodsMetricOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecMetricPodsMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "HorizontalPodAutoscalerSpecMetricPodsTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricPodsTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricPodsMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricPodsMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricPodsTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricPodsTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HorizontalPodAutoscalerSpecMetricPods]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricPods], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricPods],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62736248c9a1c8bf0482cfe5bf8e1477d3c4a6bd2ae118bf72def19d19e629ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerSpecMetricPodsTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bfd9c45cedaa920ec01c8be80f3daf7f38f8bfc02fafd8eb5f907689cd364f5)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricPodsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricPodsTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricPodsTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f261cfab32417bffbc74750d6b4fada9c131c5815d794c8bd4a825281b7c786)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88be9a61cc57a50af586f846b4a71087a09c44bec04e4e927943fd1456330d87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__531ba6d97cc8340881131d418f630f0e9ba92bd224c9b5dd743984faec698960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e17cb4b829c47c4ea75eb6e8499c7e0270f521b7359c4a648dfbc01ff75d3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b04cfcf91d04f817e25a0424ea3908c529a9c10686215e9c498d50c89809cddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricPodsTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricPodsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricPodsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c30d6331d5af8942a1ca9fdc0fb2062122e7058ef24e1439a62309b1bedf47e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricResource",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "target": "target"},
)
class HorizontalPodAutoscalerSpecMetricResource:
    def __init__(
        self,
        *,
        name: builtins.str,
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerSpecMetricResourceTarget", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerSpecMetricResourceTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e2cd09cf40ec1fcceda551c214064d12ba3f06245fd8ae6e8a6db15a0b82e3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the resource in question.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricResourceTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#target HorizontalPodAutoscaler#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricResourceTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c1d7a9b2181c0e04f16ab74fae5166f80e35c640651506b4e6859d1cd3e9526)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        value_ = HorizontalPodAutoscalerSpecMetricResourceTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerSpecMetricResourceTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecMetricResourceTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecMetricResourceTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecMetricResourceTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f46f8b84f9d5eb585932b44c8547ebdde496bbc68ca564b3b9a9e1b1dd4157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricResource]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b170ad140b4bb5d6bc6c1dc630ceb0d0f9764888c34531df6f8461c6d70f40d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricResourceTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerSpecMetricResourceTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__925c6fe67a21a5ba5d4980f747e71b753e959c1eef5e41397346af6b88f91f37)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#type HorizontalPodAutoscaler#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_utilization HorizontalPodAutoscaler#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#average_value HorizontalPodAutoscaler#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#value HorizontalPodAutoscaler#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecMetricResourceTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecMetricResourceTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecMetricResourceTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__818b3e66491884c830b0648bca0e46b860e3da1d7fdabdb8ecc15606f28a22c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee4cb9ac7a73ac4ca31547bc1e3324ff693c22ccf8641cd1f31b370a53eb8e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e315988e44d376e4c3d2c60cbb371d9990b27a0174d8e31a4a6323884d5e825)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df49dd75c042ffe44b46b903973ba48b0f2600e1100cb0172395ad177b84a157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05cad3b74a4d7b96dce7d5c7a0d2bee8606671f1b231550b722941fdc1de985c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecMetricResourceTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecMetricResourceTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecMetricResourceTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069ffd1623907ccb298e8153df2954b339e86610850f6b614fb77dcf4f4656b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4812b41b9f1d8baf8981e099f41a7e48c451e076283e2560ce89c55a2385a6a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBehavior")
    def put_behavior(
        self,
        *,
        scale_down: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, typing.Dict[builtins.str, typing.Any]]]]] = None,
        scale_up: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param scale_down: scale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_down HorizontalPodAutoscaler#scale_down}
        :param scale_up: scale_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#scale_up HorizontalPodAutoscaler#scale_up}
        '''
        value = HorizontalPodAutoscalerSpecBehavior(
            scale_down=scale_down, scale_up=scale_up
        )

        return typing.cast(None, jsii.invoke(self, "putBehavior", [value]))

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetric, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c358435d844a0d498ebdc8a51a436583844d7a790350aea0a6dadbb9c7589d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putScaleTargetRef")
    def put_scale_target_ref(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kind: Kind of the referent. e.g. ``ReplicationController``. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#kind HorizontalPodAutoscaler#kind}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#api_version HorizontalPodAutoscaler#api_version}
        '''
        value = HorizontalPodAutoscalerSpecScaleTargetRef(
            kind=kind, name=name, api_version=api_version
        )

        return typing.cast(None, jsii.invoke(self, "putScaleTargetRef", [value]))

    @jsii.member(jsii_name="resetBehavior")
    def reset_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBehavior", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetMinReplicas")
    def reset_min_replicas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinReplicas", []))

    @jsii.member(jsii_name="resetTargetCpuUtilizationPercentage")
    def reset_target_cpu_utilization_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCpuUtilizationPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> HorizontalPodAutoscalerSpecBehaviorOutputReference:
        return typing.cast(HorizontalPodAutoscalerSpecBehaviorOutputReference, jsii.get(self, "behavior"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> HorizontalPodAutoscalerSpecMetricList:
        return typing.cast(HorizontalPodAutoscalerSpecMetricList, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="scaleTargetRef")
    def scale_target_ref(
        self,
    ) -> "HorizontalPodAutoscalerSpecScaleTargetRefOutputReference":
        return typing.cast("HorizontalPodAutoscalerSpecScaleTargetRefOutputReference", jsii.get(self, "scaleTargetRef"))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(self) -> typing.Optional[HorizontalPodAutoscalerSpecBehavior]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecBehavior], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicasInput")
    def max_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetric]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetric]]], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="minReplicasInput")
    def min_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleTargetRefInput")
    def scale_target_ref_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerSpecScaleTargetRef"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerSpecScaleTargetRef"], jsii.get(self, "scaleTargetRefInput"))

    @builtins.property
    @jsii.member(jsii_name="targetCpuUtilizationPercentageInput")
    def target_cpu_utilization_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetCpuUtilizationPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicas")
    def max_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxReplicas"))

    @max_replicas.setter
    def max_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49218c001706a2aab5a9993a0c17b7fffe74a8a19d3fb73cd0771e64704741bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="minReplicas")
    def min_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minReplicas"))

    @min_replicas.setter
    def min_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dec97000e6b232e76af24a7a7327a548833fc2c808a517d739efc4472d9ce4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="targetCpuUtilizationPercentage")
    def target_cpu_utilization_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetCpuUtilizationPercentage"))

    @target_cpu_utilization_percentage.setter
    def target_cpu_utilization_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fff3090e65f0c47d984c605e351d80f7e3c3e6b4a1ca1c763748d24ffed34312)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCpuUtilizationPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HorizontalPodAutoscalerSpec]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa8719e117bcab5d77847ea74e24e571fd7d4236cf1782209246419a89dc2c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecScaleTargetRef",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "name": "name", "api_version": "apiVersion"},
)
class HorizontalPodAutoscalerSpecScaleTargetRef:
    def __init__(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kind: Kind of the referent. e.g. ``ReplicationController``. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#kind HorizontalPodAutoscaler#kind}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#api_version HorizontalPodAutoscaler#api_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0c037d98a2c338fa3c20646113669bf534ea8920dd70235165898cbdf1247a0)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_version is not None:
            self._values["api_version"] = api_version

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind of the referent. e.g. ``ReplicationController``. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#kind HorizontalPodAutoscaler#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#name HorizontalPodAutoscaler#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version of the referent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler#api_version HorizontalPodAutoscaler#api_version}
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerSpecScaleTargetRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerSpecScaleTargetRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.horizontalPodAutoscaler.HorizontalPodAutoscalerSpecScaleTargetRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bec46804d5729f4bc6782c0ce7e4c11e92ca1cf82bee71d0378bc534d6ce757d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0637a4c377400b84a5c09ce0bebac84affe3dc6f493eddc6c99da9db0c37b4f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599bfeb3582d5ccc5486a3be0dd370f6a11d85263f226e14f5db1b1af97dd700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcfdc4ef0183ba59e7636ad94348f31a3d8cbfed13ab9466753712193f10a2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerSpecScaleTargetRef]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerSpecScaleTargetRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerSpecScaleTargetRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd817ac89217eb729484cac96224e5d4c7bdc9ca9461bd843add22d4f79b1d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HorizontalPodAutoscaler",
    "HorizontalPodAutoscalerConfig",
    "HorizontalPodAutoscalerMetadata",
    "HorizontalPodAutoscalerMetadataOutputReference",
    "HorizontalPodAutoscalerSpec",
    "HorizontalPodAutoscalerSpecBehavior",
    "HorizontalPodAutoscalerSpecBehaviorOutputReference",
    "HorizontalPodAutoscalerSpecBehaviorScaleDown",
    "HorizontalPodAutoscalerSpecBehaviorScaleDownList",
    "HorizontalPodAutoscalerSpecBehaviorScaleDownOutputReference",
    "HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy",
    "HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyList",
    "HorizontalPodAutoscalerSpecBehaviorScaleDownPolicyOutputReference",
    "HorizontalPodAutoscalerSpecBehaviorScaleUp",
    "HorizontalPodAutoscalerSpecBehaviorScaleUpList",
    "HorizontalPodAutoscalerSpecBehaviorScaleUpOutputReference",
    "HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy",
    "HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyList",
    "HorizontalPodAutoscalerSpecBehaviorScaleUpPolicyOutputReference",
    "HorizontalPodAutoscalerSpecMetric",
    "HorizontalPodAutoscalerSpecMetricContainerResource",
    "HorizontalPodAutoscalerSpecMetricContainerResourceOutputReference",
    "HorizontalPodAutoscalerSpecMetricContainerResourceTarget",
    "HorizontalPodAutoscalerSpecMetricContainerResourceTargetOutputReference",
    "HorizontalPodAutoscalerSpecMetricExternal",
    "HorizontalPodAutoscalerSpecMetricExternalMetric",
    "HorizontalPodAutoscalerSpecMetricExternalMetricOutputReference",
    "HorizontalPodAutoscalerSpecMetricExternalMetricSelector",
    "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorList",
    "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions",
    "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsList",
    "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressionsOutputReference",
    "HorizontalPodAutoscalerSpecMetricExternalMetricSelectorOutputReference",
    "HorizontalPodAutoscalerSpecMetricExternalOutputReference",
    "HorizontalPodAutoscalerSpecMetricExternalTarget",
    "HorizontalPodAutoscalerSpecMetricExternalTargetOutputReference",
    "HorizontalPodAutoscalerSpecMetricList",
    "HorizontalPodAutoscalerSpecMetricObject",
    "HorizontalPodAutoscalerSpecMetricObjectDescribedObject",
    "HorizontalPodAutoscalerSpecMetricObjectDescribedObjectOutputReference",
    "HorizontalPodAutoscalerSpecMetricObjectMetric",
    "HorizontalPodAutoscalerSpecMetricObjectMetricOutputReference",
    "HorizontalPodAutoscalerSpecMetricObjectMetricSelector",
    "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorList",
    "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions",
    "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsList",
    "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressionsOutputReference",
    "HorizontalPodAutoscalerSpecMetricObjectMetricSelectorOutputReference",
    "HorizontalPodAutoscalerSpecMetricObjectOutputReference",
    "HorizontalPodAutoscalerSpecMetricObjectTarget",
    "HorizontalPodAutoscalerSpecMetricObjectTargetOutputReference",
    "HorizontalPodAutoscalerSpecMetricOutputReference",
    "HorizontalPodAutoscalerSpecMetricPods",
    "HorizontalPodAutoscalerSpecMetricPodsMetric",
    "HorizontalPodAutoscalerSpecMetricPodsMetricOutputReference",
    "HorizontalPodAutoscalerSpecMetricPodsMetricSelector",
    "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorList",
    "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions",
    "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsList",
    "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressionsOutputReference",
    "HorizontalPodAutoscalerSpecMetricPodsMetricSelectorOutputReference",
    "HorizontalPodAutoscalerSpecMetricPodsOutputReference",
    "HorizontalPodAutoscalerSpecMetricPodsTarget",
    "HorizontalPodAutoscalerSpecMetricPodsTargetOutputReference",
    "HorizontalPodAutoscalerSpecMetricResource",
    "HorizontalPodAutoscalerSpecMetricResourceOutputReference",
    "HorizontalPodAutoscalerSpecMetricResourceTarget",
    "HorizontalPodAutoscalerSpecMetricResourceTargetOutputReference",
    "HorizontalPodAutoscalerSpecOutputReference",
    "HorizontalPodAutoscalerSpecScaleTargetRef",
    "HorizontalPodAutoscalerSpecScaleTargetRefOutputReference",
]

publication.publish()

def _typecheckingstub__a253f177f71b2472abdeb0bb492261fc254f926afdf380ba20538fe72cb44c8c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[HorizontalPodAutoscalerMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[HorizontalPodAutoscalerSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__405e82a21a284ba206a8cc7cc2c311485ea02265f1bf8b2b251e94b701565861(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99d0d0362f34f81348159f7fac057293daeed8f10a7efa4c4e8c659d0902f632(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[HorizontalPodAutoscalerMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[HorizontalPodAutoscalerSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c4317e07c23a5cdcb50e9970ad9317031bc8254a1e560245747c0799d9588b(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4310260325fabb3afc7a9f69a9d2eb9798f78dab2487ac6f61c60cc3409d8e3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6d7a32eba58595c670fc3472a8237b01cb5eeee06788e65bccd1459f5d19902(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c39c46654503f79c3e6559f495e84641d03eda7bfe37104cc7f4dcdeced363(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30cbbfcce0c0d3c0de16b74cc1784cfeb95a4654431ba6058c5cd685df082d63(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d48ef1d8d431fbf07180377cfaa4e410625d85895a2c5c0b5e8974b5be65b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b6113a84dcc7d5dc1ec7b2cf386433cadd6c7cd90a2b46cb80048f3634f5137(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7651b85c672ecbd1e263a5a89ec550f62690fa30d1aed628f860c864e14ed8de(
    value: typing.Optional[HorizontalPodAutoscalerMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992749962498d89f244c2ccbf21cd282b88b4871e2954427a53d140bc363937c(
    *,
    max_replicas: jsii.Number,
    scale_target_ref: typing.Union[HorizontalPodAutoscalerSpecScaleTargetRef, typing.Dict[builtins.str, typing.Any]],
    behavior: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetric, typing.Dict[builtins.str, typing.Any]]]]] = None,
    min_replicas: typing.Optional[jsii.Number] = None,
    target_cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c3da8203cfd5b1d57e52081ae561d94ca2d0de78497fa0cd9ce59091358de5(
    *,
    scale_down: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, typing.Dict[builtins.str, typing.Any]]]]] = None,
    scale_up: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879a9b2c5d56ed1868ceac8a0857d679d4c738541745f745ff993e32c1407dc9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c222c47ac711a0d7501efbf852f16d114ea7d372d99b99b9965f7cb7cf762384(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc297073a968f46ed7b24b2ffcd1aa6fa06ae9c0fb313fd7befc63d56e153f3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c865ca7514ec716465c6179471f366a75735611b4ec31530c5cc432a88df9a6(
    value: typing.Optional[HorizontalPodAutoscalerSpecBehavior],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a90696c71006e6587039958f8d1e72e5f36941a2cf1950319f847fbf32ec315(
    *,
    policy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy, typing.Dict[builtins.str, typing.Any]]]],
    select_policy: typing.Optional[builtins.str] = None,
    stabilization_window_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c066201e04982bc4142c51a3e6bc7f949382ae9a1076dbe03dfe9c16137a5447(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f96138f1577af02195c1a664c7e66db18303d1f1e28794437e06d43d4bdfbbe(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ff2fb2e56bc8bf579ac41d049599a8939a081cf4aaee0835aa82f14ed240fe6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212ab88d2df666e4aac69c8fcc844179bbc088c2bb3ae0f6f0b5e6272855f69a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__148d32edf6c931538f63d9aee3a347f8c60906db6d074c6ecf4ca3dff8704b1a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bedba4a1a95a86ed4962919e2d2ace2d8c3ed350164a982104c7f1097ff2da64(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDown]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed462862491500ebe28d3dd900e8f3668331dd82238387fa01158237a5fc53b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d694db41c3db9f1386f2b772ce8bc828e85ce79981e4332ae97ab18759aae255(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e07469e6c41f269f0a321a9f88c529c25e7df1eb7f7c9d1d09800eb13d57f62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66144bcbf8fe168daa01fc959d88b2f07e57c7ddca4a688b55145a0a30a12ce2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c6a63690f1dafee9d53d76b62eb12b613590b2874ca78fbf567810719c655c(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDown, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd474516c6052f91512884c753d01761cfef643fe7be6d8e354d7259dfc5636(
    *,
    period_seconds: jsii.Number,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c236355a6662cf97f04625b24edc8f9447c1a4783c8397651db9deb89ccf279(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81fd476e7524a5e8f5a5388e1e78084e0c84cdb214e8e7e89c473c7885835fc5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b078d724448aac52923cb64fd6932145ea3a7e56023243460ccc37586758b305(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cb97bf25fdc18171986f6391ab980bad8646c747d140be77ae16e472e7d510b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4124dafe577591ccb40e2260bb19df73bdac25c6ecd2c73c16d97bd01793ce(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b825b5e6fd4f24e16e60c79738ce54fb7eed86f9e4fed648b6a51d73acaeb05(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79041e186363921e65a1697d0f6f016d3a21738703e02c5fec44bbab34d9b734(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb88844a6671608a23639baf757fcea85c6c0390e27a6f034980a81af17f343c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7630023631d4f1141767c48d6a8c2768a95c6a75f9b9f391c99bb874c34b68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c4ef3ea4e3fe57168255adaf04312bae296f517fd04ae54c7d77b250ce2f04(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1657b0402a546ec6030bb1b9823c4aa76408ca79344714ad31d640d32df90ee2(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleDownPolicy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe31fffaf0741da8129ef39c9813a3b041ded4927fd7e76a9750af5b8725687a(
    *,
    policy: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy, typing.Dict[builtins.str, typing.Any]]]],
    select_policy: typing.Optional[builtins.str] = None,
    stabilization_window_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a500070053425c056ce0d644f805a2469b734946ba4903876ac0d8b45cfb2782(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa85205f0683ea67fd902847d62630cccf39fef9f803464bfddc411bde1d4a58(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d108096bbc8d3944fb909148855cd841bf2077df5c1f9f6f5866892b1f2b72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cae50be7736ac8d9c30c9504b0cc0fd55a588e2ebc8fe298598b4ef2c47f812f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbfb4e50281090b6722eab4e59943d8a0ee86120b1187eeb887f0f91a244ff74(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0f4ff7f47f033663d618b3610583c8edb1f00b5cf7003a5fca88be82d190d0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUp]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2467afafd934a904b7d7f9d8a6270dfd18d0dddfb8b2aba618c40b0c7d68fbb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28d432ef22dd89c94dca6167a367d27645ce8b0cdb1af6db97b8ffbf8ca393e3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ccfa75f49fa0c8e37022aff1e0dfe7005e26b96c533fecc4342f22cdd1d39f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53c425affa1954c03ea113cbfdea6cdc4bb5ef611d9ed5dfa72e7b8fa47eae7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2315244fd401ef346e5605173cbd4da11d218b006ea5c5d6f94af629d9f1a2(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUp, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f8003de3aed5535332b2a2bb6592f1ee0625083170dc5caf04f24cb0841241f(
    *,
    period_seconds: jsii.Number,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8744ac4813532f4a9a35230bbb9dd9003b17ce69d44c61ee85c5283fe52d8f9e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0803da9a5b3dac8bf51e6a4b8492d433898149ac9d113b49d54fb90e498418b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4d75e2616423ce2577f4bc8872d216a642bd5c05eee5e7944bb5f1e4ebbf89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f311becb7a186f8208f8a2124359b65d5d1fc0e22811edb62ec49d2935f356b0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4326e27abfbfff702dc7c7b65512a6927b76da01f39c1be0cb0f94af8f2e5021(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb2e9de6979d2500b4c00b2505408d039bcf6bcc32c42e5d67758230a1e3cc4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c03dd4d66ec11214ec503f1472359d6eae184cc07383c9c3c7fc917cb83c331(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167381baec20c06fceaf18b87d8f2aef3fc1ec8992beae695e158a2ece355fbb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8617e5c75250104bc9056baf8dd862d94aa826ea14da204663eeff23d4b244(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33f51b8c1950ac4e96f1bba0997248488be5f7134891da8b9e535137f392d623(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cbad3fec02cb6286125c24246438674b9b622f79a816ee6c24807f3f1d04da(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecBehaviorScaleUpPolicy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e16c7637019cea7be16dca52170172975feb90f9be169775304d46f027be72bf(
    *,
    type: builtins.str,
    container_resource: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricContainerResource, typing.Dict[builtins.str, typing.Any]]] = None,
    external: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternal, typing.Dict[builtins.str, typing.Any]]] = None,
    object: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObject, typing.Dict[builtins.str, typing.Any]]] = None,
    pods: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPods, typing.Dict[builtins.str, typing.Any]]] = None,
    resource: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricResource, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4947ced4c433b432267a7584bf8156b3da61fdfbe31f7a953dc074b07cc8c413(
    *,
    container: builtins.str,
    name: builtins.str,
    target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricContainerResourceTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5422e87d5094719a4bf2272d3f6278982265d30c0d8d0fa3d891a1baf9b77839(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420b10adda8cc40caa705a860acb37b5d6c98333cc7d0893a1ec7d47f4ce2e8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317c99e6cb3d23b5712e22154d313a288fd5b6559192225b359cf07980508077(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b9fb75adc91013ff98d00bc82b6940d5e39078907d032f7393a1d61607be04(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432ec4e2af67b22f2f1100b6f8057c5aca386b3a2ab8b93b55afd6edb8b761b8(
    *,
    type: builtins.str,
    average_utilization: typing.Optional[jsii.Number] = None,
    average_value: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca07d19af5060b23b79fc57923d92e0e458757ae9c42bdf3da84af6ac543de1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766b5f31128947478731cedc28f790cdd27746524af71711eeb4b26d26805845(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a5bd13b568ecc90c9d3d5ea48120c91b99755fa3be320a43f86d762c743903d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79c21d1c760c9d65613b53a73f1a9a3eaf19b8b122f2df21b1c8e5263339871(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b7fe60498f20db02db4ee68848578bc4e0ab45cce9d6e41c80b0a6b9815c02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7514b0cdd14ba49ffb7280e25ee69688cedc80863def90606eada985ca89dead(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricContainerResourceTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6b00fdcc1a1193670a6ede13fcbfd84929b3679b59dbde3772a03fc43e12ec(
    *,
    metric: typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetric, typing.Dict[builtins.str, typing.Any]],
    target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0cf092610e2a40dbacc9341ad7eea79db9241937df5290c60c6364803756f3(
    *,
    name: builtins.str,
    selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5f9e9277e980499edc189a1816d5905674b5ea9ea656594cc82fe52d3684f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e4f956d3f7c95d06917a23be3551a5988b98baa415c06f877958d6b824aa8f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad2ed080ea3686e2ce77da5d050b4f6edd9c32b79dcec2e2e4bf0ca111034d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ca433fe2e5ee21852df73433dc0e740fadb4b0fde6ac0001df97c7d2b6986a(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricExternalMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d40d36e49e2fb452b443a68124669097b40e9203874088aa6cf36d3a1634fcab(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306a545f478e12eca7ac161ddaa169b0ec6f340cc4d7772b9e5002da3fcaa723(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72cd263f2d30b6467be2dda2de9ccd0e6a26e681a962ac2bae3f0bc78fb46cf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7313ada5e52e3e9ef374e0fbb66ebb394308c049af1dc7b16f63b93b53aa02ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8eff05e7813f4349282abb4be5445568290e5d9b1cd65cf6bcad321c13fd75(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__680428e7d4d1a5a099bceefa26bb3f1da35b2133c66d2b361319e31476ada680(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3123934ddfb56e9db41c044d60b89247010b43ffbc2be516fc015c56d26d2f67(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelector]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d0ea6ce328f2b6153aa113f43da508704b16b6d964e3a8a33e04ba9f7db433(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb5ad0fed9b3968ed640cdb0af653be40f13f369f787cb9d3474db8e24668db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf835b43a1a7d570f71483953d96553a52230f18bda8de4cfef15fe6634992b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aedbc13acfa6776f6e1ccaa9ddcd323ff8fa7951c0b526e60c213456daea2a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a654d0886ba8a52ace53e0a8b193b1023eabefa87b877938980f45819bda4662(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86553a53a986509111a57026a00c569fb8f0165adfff80d5f4cdbc9a2a90a2f1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865512bbf61fc9de2d91c0e373830e4ef95dc5a3f03e5255768eef476cad9e72(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c0087f97453078e5020073c85a0636738e940150db82ac5297e30a9f6a6d10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ec621bc07c032a9835d9015f9ec623fc37d9d91d759502427d1e0bd00daea9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7152f779d0010cc757300cbdead859e13f729f9f617ed18d2aa73246d1378907(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b3ea9aa241f121a6cd27074b87e838db2a51eabb29acc5686fab1936425ac5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b861fe853cc61f006754b5910b468748b5c5b5c0ef6d44e66d326bf12ef554ab(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b0a0dc9e66f134ce987b928f4bbf6ad0d876e2e16b17db81a1383f32a8ecd0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a14fccbb4ff3e804fd8d768989334acf18a337b756eae09af9f4b60b2131f43(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc4b8453b33bb822bcc8a7c3384d0b4dd8e98bf8965e96f93b71d503c8e8e88(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57cd80724a4150a013b97fd517594ad09f62c4c43a27da88b90f64d2d41af80c(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricExternalMetricSelector, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501d2521427a41096667231c1d8784d7d8ef9287091702bbf6a4af492bdb8644(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b845b32d6a9ce99b5603d8fd36e9613e38314ac33a2adc5b18966bac377bcb91(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricExternal],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a1e0794b343d5d9650f97584a69e33e555475c4a4ce411d7f257c630d7b0f7(
    *,
    type: builtins.str,
    average_utilization: typing.Optional[jsii.Number] = None,
    average_value: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7164d9d8c1745a85df21b3a9bb6311782b9a35ad6359ab9c6244c1ea44996c5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0acd014bb28a0146d3c92a72410f0d48c0985f95868f005930c4907d3309742d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0dc76c6d38200358afa3efb68bbd04ca4250a2c1d58439ff6ff91934d2ab730(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b4c342f5c4b1557a34f643038aeba3c4f9b4132fc9e999cb073332e5f5f022(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f274f15f279073807f3893765b79aa075292c61a4ff59549f0e24869e178b96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d40e118dfd3a4e31986e26949f546df5b237514e0a5c3cf29d09844095f628a(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricExternalTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9220a9bc62febab0c87e2ee7f7d60100d4bd9851c110231c65e3c8dff20f416(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a405ace3a6366ca7a99e4bc19a5476ff7db4669b2d2650898554a4d8fb9040(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__423319d1b677a34c76b754bdf21bacc7f81f5e3dfcc2e75074235ce1a489dca4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88506621d09edea97de51a30a3fea34a7d950260c8363f75ee7fa4b06db1de34(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60ea8311a1002e8631ad2b37d41027ecc9c2e4b7689277c6930fff9ab7e4ffb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f249ab484c1eaf770677699bdd78f1e8866531f63f7ca6519304552307fe4e0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetric]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a2a625c0d0fe01a16c233aa4b54322aedc1ad0478e99f38b369a73c72a0310(
    *,
    described_object: typing.Union[HorizontalPodAutoscalerSpecMetricObjectDescribedObject, typing.Dict[builtins.str, typing.Any]],
    metric: typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetric, typing.Dict[builtins.str, typing.Any]],
    target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e240b1834490b7e5260cbc1a4db6dbfc1a400328be932cd38aac4b32c01785e(
    *,
    api_version: builtins.str,
    kind: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b20ffba8b030e3011c293e3cce2ff60f35661af1031240a72363a568dc9189(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2aefe8ef9a430faf42d28c165e72871eec6512ac47e7ab310471527a804347(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baba0ba7e3b3fd847f69688a1aff39533508c46ddf41d2031a29a072db2280fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9033dc761be2cbbdf9ddacd96b5fc19acdb3b13641d939f0f9f83afed0d7a0cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf63ff7dcb139ab2e01862f8fc42d0e639d2e17387c7602685f79f9360b4ce2(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricObjectDescribedObject],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0074dbd80d64a5540aae969585f366b759bcabea899515dd1b6baa16827a2ed3(
    *,
    name: builtins.str,
    selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443f3864f0db186298082c311c08e580e98a932a8939312a9cc6e6c610faa933(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb9403ed94087700d8412e0dc829ca78e7c1a4aa1b6e3d3c40869c75a77d8be9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65fa98c7e2053ff16b9d700f9327641120439de88ef52d640a457b222084b7c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a97040881766607d69b127107db6e0ab2d550d9bad5e93b6286602189c0b600a(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricObjectMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662d8b0c38b55860a2370ca10a3f4f4b3a9319c4012eedf42c3df98cd207869f(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70c85076e18422efa9a6a79aec5f39454b1ccec3402cf806ea4c4300ca1a611a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da2e5f40a70ba12a2e189b79fbd88701cfaf20a58ae4fa0b586ea2a5fb6d7b97(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b8486039104d46892e68d2aa190d55e5c7e48c161f486284988cb117e5e814f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c588d8c8d232bfb91cf4d87f836e7b643b1d4831a6ae6aa97af48f9f3e87367e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af79563a9631bb8a756d9c9a29bf2b247876283a7505f4ac84cddb127e84d215(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51e5d128ee62cccb61dfcc87f580ec9080bd57074822ddf953f12d834ad95651(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelector]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94599473ccbca7c7809a109baa9096f6cfe2f265a1159ca03acffb38f9d42e2(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00034ea4f52a06d142e8776c29ca351fd3ca0d4becc2e5af96cfe966d5ebeb68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f35c55e27f096d2500705ad63a71712c08395cc77d8d1f01eeca6ed0513327(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd47f4c823c0ead4c487815cdc7f66af912e59aafe2711efea3f0f86cb898a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e82b84b577baf1d8981455907d58636881b4d12985ba6bc19e3d337a592ce771(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75370b1bdbf851a17a37b6ccd86b8e386ade4ba51f16119fae84d567889d499(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ffb77807e8177fa44ff42386fbe585b29fef3f1e8c931df7fc2aced87d3d99(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00cb92f39e38e4d23732241c4deca528ba469bf60f069d7343632b08d1ef20ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1550a189b24587c069af96b8bde9fea59001bb566800355f8a676fe5614296(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ee8899f6394592af79b8488005e8fbbd956dbfeb43c3333f1bbc975e4800cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd050e5d5c9f2a429f4d0800b46c716c26a6659a0909409ea3b2803e96243821(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c0b498bcc38366478df03848e337073e5077a8a93c7b9b6602d5d7e7574a8e(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cabbc502f93cd25ed31dc39ab4df6dffb2920c5529114e648be537a2e830350(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56285e95d699d1bd699b9a6fd2aeda0faa3d923fe3ca8bd83a21eaa3cf2cc354(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd87731ce2852eca028524f87f004c57d83e725c360c11c2e6d3c9079c535683(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__914d18eb5af559afa120da45bb2763679095dbe5a47b1b77d2cdf563d9ac536e(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricObjectMetricSelector, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c660c2612035b67e3f6d0cfa14388f23c1ca90124d44703450da525e038d1659(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2713b00cfec5cf1aa279feb88d7b856fc18fd12e3746a05abcf62e13760753(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricObject],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c9f97b6b09ddabeb82e670b131459a58c1040ab7a20e0f93f94b1e1acffebb(
    *,
    type: builtins.str,
    average_utilization: typing.Optional[jsii.Number] = None,
    average_value: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__383be752630640796a6c4ac81b0b36c06742c30b58adf5f891ef1640c90a418d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b7da196e471d009efa34e7d36e32176118302a25ad752a7c05af350a7ecfba(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436f4f9c3e07909db1e1be1fb1223d99462d0ff189a1ac00622d5374717d9286(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e7681fc4ebde3ce943199ebe10015114869dbacea90b33fdae13131fc446f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234352b2c809197f4e5d41669b178bcb1c88966bf1b3984ec2b299e6ba6c0585(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15ed61006efa5402ceceb0d79af6bc14d1f467358663190693cfcf9b1711e576(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricObjectTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253fecc3dc155c02ed8cc847c82005673968e35e06c8c4e3d63fb166e837351f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8fb87bcff723c22895ba9b8a20da80b0840c8c4c335d2e27d112639e38566a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80523c5d6bd997b3eb07e037601bcd0dba7063a2c5f2532d77df30d14c8206bd(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetric, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__219d5f10959824a56bf59745b3766f58c343f0abef47caf6314e61cf569f3856(
    *,
    metric: typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetric, typing.Dict[builtins.str, typing.Any]],
    target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27691f1eafa2df526fbe23ac3fa879592b8cf015e0843d43e01663fbaed4938c(
    *,
    name: builtins.str,
    selector: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941b73ca1c5b9f549afdc71a67e4a0d61e558af820dcf200792d74ba20a1c318(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466617c5a6d02b94b330968bf55167500f19b20c54b74b8025fde9745d2e18bf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4215fed70dffc43e2bc284a6cb14d88262d4755589d2c69e6ef980fbba81dd47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__339f62d8ac554d1c19a72e5fc3a7a25c319e2b749707d6d62fe89f1c4c174a05(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricPodsMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee076b9d18da55f8bea8a76a3eb0fdbea46bf040e56c907ee8640cf7f358f2cc(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9baf115670935f86f66c6b9af199cba79f6c107aa78ce29d6433d85d72325c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b995f8078e5a363420b63c3995e6a10cb20128c0b12188474580bacca9d3f8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd5dcbbfbf2da4c353500d95fda43343ed8ef4ea20f4621f8e09068126b006b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b430649c1e1786a27d1228d949ae483b0578963c7666e39bf3eb926e402b945b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d366251ed6455fe3bb73f121747728669885bad1654df2537dac8b9d842c8bc6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c9906601b67f22868a19f7801609b55f114ba51868ba9ca0bad3c1ba22d255a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelector]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a61a7e564ede98ddf1e67007921467f72a732e605a123ec0a8d2392e55b6bd(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e631613287428fc7530f7eed488e867fd32df48dbd8806c118c588bcc63eb4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f097a6d24c05edfa58ad56ecbcb0cf11c7a2d1a183ca3d49b576b1aa253af65e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbadcb05b7b5651d4ae0c4236e012e36affcd3dc77cf6cbed7057d188540f13b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac42b85e7d3bab462bc1a57ab5434e7c79718bfde1ad9f3adc541a47c7cd6c9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4608bb55c859fdc2999346803893e595b06a1240f321d132038967d8693276fe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753b34365d8d06e1c85c8b325ad8eee737c05f876cdfc6e83242198bfc47990b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4ea94aa155fb7f274c3af9d25fab6a42dbd4ba4bd469f3be9d4c56159009cf3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d663d08be0338ddd37637efc5a62b78afb7ce8d3558f3b9e5100bfcd4a9a77b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0c906ec1cbba11341ebbef8842bdeb3a1eb39b6d1f61cb20185f347ef7be5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55dbcebda5506099d69a933018f8b7d9c795c93175460555b9164d52eb1b5d88(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5727c03fe95946d91d025798c9422039b5b2c56fae31a287d3f6a5bfab2d13(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78eaf19e28734b6beb6e659d22b27433e748eee344a99fdc0dc34727a3fe89b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1ca02da8d6cba9906155d759fa1b1cd8de8c8f47215754e0159640a96ddec9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479af1ff25098bc46a9590ae41afb9a63a812afbc94b8a4926d342b70c5a7bea(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0448fee6bc3ba9c56057f36c40b1b124535247c56380399f69bdf3e6369db3bc(
    value: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricPodsMetricSelector, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0308e8b12536115a2e6de3c05a424c95186c9079805bc4c7e6ceef539aca9c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62736248c9a1c8bf0482cfe5bf8e1477d3c4a6bd2ae118bf72def19d19e629ed(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricPods],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bfd9c45cedaa920ec01c8be80f3daf7f38f8bfc02fafd8eb5f907689cd364f5(
    *,
    type: builtins.str,
    average_utilization: typing.Optional[jsii.Number] = None,
    average_value: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f261cfab32417bffbc74750d6b4fada9c131c5815d794c8bd4a825281b7c786(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88be9a61cc57a50af586f846b4a71087a09c44bec04e4e927943fd1456330d87(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531ba6d97cc8340881131d418f630f0e9ba92bd224c9b5dd743984faec698960(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e17cb4b829c47c4ea75eb6e8499c7e0270f521b7359c4a648dfbc01ff75d3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b04cfcf91d04f817e25a0424ea3908c529a9c10686215e9c498d50c89809cddc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c30d6331d5af8942a1ca9fdc0fb2062122e7058ef24e1439a62309b1bedf47e9(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricPodsTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e2cd09cf40ec1fcceda551c214064d12ba3f06245fd8ae6e8a6db15a0b82e3(
    *,
    name: builtins.str,
    target: typing.Optional[typing.Union[HorizontalPodAutoscalerSpecMetricResourceTarget, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c1d7a9b2181c0e04f16ab74fae5166f80e35c640651506b4e6859d1cd3e9526(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f46f8b84f9d5eb585932b44c8547ebdde496bbc68ca564b3b9a9e1b1dd4157(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b170ad140b4bb5d6bc6c1dc630ceb0d0f9764888c34531df6f8461c6d70f40d8(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__925c6fe67a21a5ba5d4980f747e71b753e959c1eef5e41397346af6b88f91f37(
    *,
    type: builtins.str,
    average_utilization: typing.Optional[jsii.Number] = None,
    average_value: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__818b3e66491884c830b0648bca0e46b860e3da1d7fdabdb8ecc15606f28a22c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee4cb9ac7a73ac4ca31547bc1e3324ff693c22ccf8641cd1f31b370a53eb8e9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e315988e44d376e4c3d2c60cbb371d9990b27a0174d8e31a4a6323884d5e825(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df49dd75c042ffe44b46b903973ba48b0f2600e1100cb0172395ad177b84a157(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05cad3b74a4d7b96dce7d5c7a0d2bee8606671f1b231550b722941fdc1de985c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069ffd1623907ccb298e8153df2954b339e86610850f6b614fb77dcf4f4656b9(
    value: typing.Optional[HorizontalPodAutoscalerSpecMetricResourceTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4812b41b9f1d8baf8981e099f41a7e48c451e076283e2560ce89c55a2385a6a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c358435d844a0d498ebdc8a51a436583844d7a790350aea0a6dadbb9c7589d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerSpecMetric, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49218c001706a2aab5a9993a0c17b7fffe74a8a19d3fb73cd0771e64704741bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dec97000e6b232e76af24a7a7327a548833fc2c808a517d739efc4472d9ce4e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fff3090e65f0c47d984c605e351d80f7e3c3e6b4a1ca1c763748d24ffed34312(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa8719e117bcab5d77847ea74e24e571fd7d4236cf1782209246419a89dc2c8(
    value: typing.Optional[HorizontalPodAutoscalerSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c037d98a2c338fa3c20646113669bf534ea8920dd70235165898cbdf1247a0(
    *,
    kind: builtins.str,
    name: builtins.str,
    api_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec46804d5729f4bc6782c0ce7e4c11e92ca1cf82bee71d0378bc534d6ce757d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0637a4c377400b84a5c09ce0bebac84affe3dc6f493eddc6c99da9db0c37b4f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599bfeb3582d5ccc5486a3be0dd370f6a11d85263f226e14f5db1b1af97dd700(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcfdc4ef0183ba59e7636ad94348f31a3d8cbfed13ab9466753712193f10a2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd817ac89217eb729484cac96224e5d4c7bdc9ca9461bd843add22d4f79b1d4(
    value: typing.Optional[HorizontalPodAutoscalerSpecScaleTargetRef],
) -> None:
    """Type checking stubs"""
    pass
