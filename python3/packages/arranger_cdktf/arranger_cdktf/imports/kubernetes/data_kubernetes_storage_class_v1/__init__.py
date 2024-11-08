'''
# `data_kubernetes_storage_class_v1`

Refer to the Terraform Registory for docs: [`data_kubernetes_storage_class_v1`](https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1).
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


class DataKubernetesStorageClassV1(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1 kubernetes_storage_class_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["DataKubernetesStorageClassV1Metadata", typing.Dict[builtins.str, typing.Any]],
        allowed_topologies: typing.Optional[typing.Union["DataKubernetesStorageClassV1AllowedTopologies", typing.Dict[builtins.str, typing.Any]]] = None,
        allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reclaim_policy: typing.Optional[builtins.str] = None,
        volume_binding_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1 kubernetes_storage_class_v1} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#metadata DataKubernetesStorageClassV1#metadata}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allowed_topologies DataKubernetesStorageClassV1#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allow_volume_expansion DataKubernetesStorageClassV1#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#id DataKubernetesStorageClassV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#mount_options DataKubernetesStorageClassV1#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#parameters DataKubernetesStorageClassV1#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#reclaim_policy DataKubernetesStorageClassV1#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#volume_binding_mode DataKubernetesStorageClassV1#volume_binding_mode}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b37881981e49c80453625ab15f3d9cdff4ea5ff028a5ec3f970f711845a9666f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataKubernetesStorageClassV1Config(
            metadata=metadata,
            allowed_topologies=allowed_topologies,
            allow_volume_expansion=allow_volume_expansion,
            id=id,
            mount_options=mount_options,
            parameters=parameters,
            reclaim_policy=reclaim_policy,
            volume_binding_mode=volume_binding_mode,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllowedTopologies")
    def put_allowed_topologies(
        self,
        *,
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#match_label_expressions DataKubernetesStorageClassV1#match_label_expressions}
        '''
        value = DataKubernetesStorageClassV1AllowedTopologies(
            match_label_expressions=match_label_expressions
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedTopologies", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#annotations DataKubernetesStorageClassV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#labels DataKubernetesStorageClassV1#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#name DataKubernetesStorageClassV1#name}
        '''
        value = DataKubernetesStorageClassV1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="resetAllowedTopologies")
    def reset_allowed_topologies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedTopologies", []))

    @jsii.member(jsii_name="resetAllowVolumeExpansion")
    def reset_allow_volume_expansion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowVolumeExpansion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetReclaimPolicy")
    def reset_reclaim_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReclaimPolicy", []))

    @jsii.member(jsii_name="resetVolumeBindingMode")
    def reset_volume_binding_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeBindingMode", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedTopologies")
    def allowed_topologies(
        self,
    ) -> "DataKubernetesStorageClassV1AllowedTopologiesOutputReference":
        return typing.cast("DataKubernetesStorageClassV1AllowedTopologiesOutputReference", jsii.get(self, "allowedTopologies"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "DataKubernetesStorageClassV1MetadataOutputReference":
        return typing.cast("DataKubernetesStorageClassV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="storageProvisioner")
    def storage_provisioner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageProvisioner"))

    @builtins.property
    @jsii.member(jsii_name="allowedTopologiesInput")
    def allowed_topologies_input(
        self,
    ) -> typing.Optional["DataKubernetesStorageClassV1AllowedTopologies"]:
        return typing.cast(typing.Optional["DataKubernetesStorageClassV1AllowedTopologies"], jsii.get(self, "allowedTopologiesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVolumeExpansionInput")
    def allow_volume_expansion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowVolumeExpansionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["DataKubernetesStorageClassV1Metadata"]:
        return typing.cast(typing.Optional["DataKubernetesStorageClassV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicyInput")
    def reclaim_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reclaimPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeBindingModeInput")
    def volume_binding_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeBindingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVolumeExpansion")
    def allow_volume_expansion(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowVolumeExpansion"))

    @allow_volume_expansion.setter
    def allow_volume_expansion(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b221032cdcdd5be02d1d6557957ac1a35c8d739bfff0d6129114e3a8a87ef88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVolumeExpansion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ecc43cab9b65eb376388c7f3564186eba2fa3feca036c2744b4253f1d753eec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbb997d6ca94c2882332e4e8535df34284430199c11d6c0e5964fe0674de3831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a81f1f203b950403521e7612b2a8d74444906b9a43fcd19e44b8ed87bb7f76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicy")
    def reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reclaimPolicy"))

    @reclaim_policy.setter
    def reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63bbee101e6fefc1eafbf5f3285fd9586b431a101cc58b95cf982b1614ca3d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="volumeBindingMode")
    def volume_binding_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeBindingMode"))

    @volume_binding_mode.setter
    def volume_binding_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940e58a81ce4590d57e0df400a3e2cb2e4165a01b433c0791ab14a83bbc3268c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeBindingMode", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologies",
    jsii_struct_bases=[],
    name_mapping={"match_label_expressions": "matchLabelExpressions"},
)
class DataKubernetesStorageClassV1AllowedTopologies:
    def __init__(
        self,
        *,
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#match_label_expressions DataKubernetesStorageClassV1#match_label_expressions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e6bef322aa87e05dfe6654c6b4035ef8ab2a85253b5f97545b980adf19f915)
            check_type(argname="argument match_label_expressions", value=match_label_expressions, expected_type=type_hints["match_label_expressions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_label_expressions is not None:
            self._values["match_label_expressions"] = match_label_expressions

    @builtins.property
    def match_label_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions"]]]:
        '''match_label_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#match_label_expressions DataKubernetesStorageClassV1#match_label_expressions}
        '''
        result = self._values.get("match_label_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1AllowedTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#key DataKubernetesStorageClassV1#key}
        :param values: An array of string values. One value must match the label to be selected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#values DataKubernetesStorageClassV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a9050a0545e63847610a12ea91a06835ef7202df92860c9ad925950e7dc9e1)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#key DataKubernetesStorageClassV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values. One value must match the label to be selected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#values DataKubernetesStorageClassV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb603e823f8660a60df9998580448c6d2ca08e98a2d21a223ebb566ae3071495)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed0cef5adab1b15a23cc11d53135e7c56e7e101ad7f14dbff8c236a8ec1be2d3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aea068eae5a0e156a7213645345fa26652e227f7995e8c4b2d97c878b6ceca8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df4feb8f47a06df3a570ec6def64497ef59a91273865b9a90016bf02a9a23f53)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adf730cc74f2e4fad89092cb1ea6b7cf7a64bcfffb7b6f309fc9331166ffaef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0e6bec181ed82c2674411805625faa93fe50c4be598ebeecf70d5b41528c64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fb340d79120d860692b667398c5efeaeedc5d1e4a9d93604d4cbdb3b832cdd1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__fea5387049422f4a73caea02c578b102db5c6e7dc06eb158e53b04f1bd1249c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3512027dc9b757ca83b88fa16e4845da4abafd6a8ac462c90f1fc4634b100402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a99ce437e7de463a18edc712e4b20bba93019981ecbb86d20d7afc7feae9c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesStorageClassV1AllowedTopologiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03b5827c3957f0be377ab5b00858335d37635a94fbd17204ecdc19ef8196428a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchLabelExpressions")
    def put_match_label_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3c0952e520b58a0de9ffd118452c38df338eae9b3fd55d79ea1f3185b849c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchLabelExpressions", [value]))

    @jsii.member(jsii_name="resetMatchLabelExpressions")
    def reset_match_label_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabelExpressions", []))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressions")
    def match_label_expressions(
        self,
    ) -> DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList:
        return typing.cast(DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList, jsii.get(self, "matchLabelExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressionsInput")
    def match_label_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "matchLabelExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesStorageClassV1AllowedTopologies]:
        return typing.cast(typing.Optional[DataKubernetesStorageClassV1AllowedTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesStorageClassV1AllowedTopologies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6cd1f1845a43f63a4a97212dcc3ba535424a3b335fa872fb259b337cb3c8a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1Config",
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
        "allowed_topologies": "allowedTopologies",
        "allow_volume_expansion": "allowVolumeExpansion",
        "id": "id",
        "mount_options": "mountOptions",
        "parameters": "parameters",
        "reclaim_policy": "reclaimPolicy",
        "volume_binding_mode": "volumeBindingMode",
    },
)
class DataKubernetesStorageClassV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["DataKubernetesStorageClassV1Metadata", typing.Dict[builtins.str, typing.Any]],
        allowed_topologies: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reclaim_policy: typing.Optional[builtins.str] = None,
        volume_binding_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#metadata DataKubernetesStorageClassV1#metadata}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allowed_topologies DataKubernetesStorageClassV1#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allow_volume_expansion DataKubernetesStorageClassV1#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#id DataKubernetesStorageClassV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#mount_options DataKubernetesStorageClassV1#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#parameters DataKubernetesStorageClassV1#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#reclaim_policy DataKubernetesStorageClassV1#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#volume_binding_mode DataKubernetesStorageClassV1#volume_binding_mode}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = DataKubernetesStorageClassV1Metadata(**metadata)
        if isinstance(allowed_topologies, dict):
            allowed_topologies = DataKubernetesStorageClassV1AllowedTopologies(**allowed_topologies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16cb347f716f501b6004f7c6c07f7c84290fc33b176275599d6460f11e2a4bd9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument allowed_topologies", value=allowed_topologies, expected_type=type_hints["allowed_topologies"])
            check_type(argname="argument allow_volume_expansion", value=allow_volume_expansion, expected_type=type_hints["allow_volume_expansion"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument volume_binding_mode", value=volume_binding_mode, expected_type=type_hints["volume_binding_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
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
        if allowed_topologies is not None:
            self._values["allowed_topologies"] = allowed_topologies
        if allow_volume_expansion is not None:
            self._values["allow_volume_expansion"] = allow_volume_expansion
        if id is not None:
            self._values["id"] = id
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if parameters is not None:
            self._values["parameters"] = parameters
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if volume_binding_mode is not None:
            self._values["volume_binding_mode"] = volume_binding_mode

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
    def metadata(self) -> "DataKubernetesStorageClassV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#metadata DataKubernetesStorageClassV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("DataKubernetesStorageClassV1Metadata", result)

    @builtins.property
    def allowed_topologies(
        self,
    ) -> typing.Optional[DataKubernetesStorageClassV1AllowedTopologies]:
        '''allowed_topologies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allowed_topologies DataKubernetesStorageClassV1#allowed_topologies}
        '''
        result = self._values.get("allowed_topologies")
        return typing.cast(typing.Optional[DataKubernetesStorageClassV1AllowedTopologies], result)

    @builtins.property
    def allow_volume_expansion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the storage class allow volume expand.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allow_volume_expansion DataKubernetesStorageClassV1#allow_volume_expansion}
        '''
        result = self._values.get("allow_volume_expansion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#id DataKubernetesStorageClassV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Persistent Volumes that are dynamically created by a storage class will have the mount options specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#mount_options DataKubernetesStorageClassV1#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The parameters for the provisioner that should create volumes of this storage class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#parameters DataKubernetesStorageClassV1#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''Indicates the type of the reclaim policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#reclaim_policy DataKubernetesStorageClassV1#reclaim_policy}
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_binding_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates when volume binding and dynamic provisioning should occur.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#volume_binding_mode DataKubernetesStorageClassV1#volume_binding_mode}
        '''
        result = self._values.get("volume_binding_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class DataKubernetesStorageClassV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#annotations DataKubernetesStorageClassV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#labels DataKubernetesStorageClassV1#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#name DataKubernetesStorageClassV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84604e53b327fc1f82e92acd6212ff4811d782c6cbf4b8348d57f97f2c3c90d6)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the storage class that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#annotations DataKubernetesStorageClassV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the storage class.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#labels DataKubernetesStorageClassV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#name DataKubernetesStorageClassV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesStorageClassV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f7afd828a8753fd031dced5bf0056b4f522646fd57a6d2655eaeab9f3397e50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39f9291596f2b0e9f8ea231c674c73165fc3c1e83473b4103f366604ea9ba992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c572c5833baec4298e263e05b5d906ab440c0c46b2e7fba03a7842a2d1cb42d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63a1cf194279370384b1eb6653d2bb97bcd9fd8be6c5a0518676e011ae18dfb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataKubernetesStorageClassV1Metadata]:
        return typing.cast(typing.Optional[DataKubernetesStorageClassV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesStorageClassV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8313046935a0c20725f9ed0faacf75dc0d6c0311e5d2a4c810db7e25206cfb4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataKubernetesStorageClassV1",
    "DataKubernetesStorageClassV1AllowedTopologies",
    "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions",
    "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList",
    "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference",
    "DataKubernetesStorageClassV1AllowedTopologiesOutputReference",
    "DataKubernetesStorageClassV1Config",
    "DataKubernetesStorageClassV1Metadata",
    "DataKubernetesStorageClassV1MetadataOutputReference",
]

publication.publish()

def _typecheckingstub__b37881981e49c80453625ab15f3d9cdff4ea5ff028a5ec3f970f711845a9666f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[DataKubernetesStorageClassV1Metadata, typing.Dict[builtins.str, typing.Any]],
    allowed_topologies: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reclaim_policy: typing.Optional[builtins.str] = None,
    volume_binding_mode: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4b221032cdcdd5be02d1d6557957ac1a35c8d739bfff0d6129114e3a8a87ef88(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ecc43cab9b65eb376388c7f3564186eba2fa3feca036c2744b4253f1d753eec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb997d6ca94c2882332e4e8535df34284430199c11d6c0e5964fe0674de3831(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a81f1f203b950403521e7612b2a8d74444906b9a43fcd19e44b8ed87bb7f76(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63bbee101e6fefc1eafbf5f3285fd9586b431a101cc58b95cf982b1614ca3d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940e58a81ce4590d57e0df400a3e2cb2e4165a01b433c0791ab14a83bbc3268c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e6bef322aa87e05dfe6654c6b4035ef8ab2a85253b5f97545b980adf19f915(
    *,
    match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a9050a0545e63847610a12ea91a06835ef7202df92860c9ad925950e7dc9e1(
    *,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb603e823f8660a60df9998580448c6d2ca08e98a2d21a223ebb566ae3071495(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed0cef5adab1b15a23cc11d53135e7c56e7e101ad7f14dbff8c236a8ec1be2d3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aea068eae5a0e156a7213645345fa26652e227f7995e8c4b2d97c878b6ceca8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df4feb8f47a06df3a570ec6def64497ef59a91273865b9a90016bf02a9a23f53(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf730cc74f2e4fad89092cb1ea6b7cf7a64bcfffb7b6f309fc9331166ffaef6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0e6bec181ed82c2674411805625faa93fe50c4be598ebeecf70d5b41528c64(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb340d79120d860692b667398c5efeaeedc5d1e4a9d93604d4cbdb3b832cdd1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea5387049422f4a73caea02c578b102db5c6e7dc06eb158e53b04f1bd1249c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3512027dc9b757ca83b88fa16e4845da4abafd6a8ac462c90f1fc4634b100402(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a99ce437e7de463a18edc712e4b20bba93019981ecbb86d20d7afc7feae9c0(
    value: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b5827c3957f0be377ab5b00858335d37635a94fbd17204ecdc19ef8196428a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3c0952e520b58a0de9ffd118452c38df338eae9b3fd55d79ea1f3185b849c4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6cd1f1845a43f63a4a97212dcc3ba535424a3b335fa872fb259b337cb3c8a4e(
    value: typing.Optional[DataKubernetesStorageClassV1AllowedTopologies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16cb347f716f501b6004f7c6c07f7c84290fc33b176275599d6460f11e2a4bd9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[DataKubernetesStorageClassV1Metadata, typing.Dict[builtins.str, typing.Any]],
    allowed_topologies: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reclaim_policy: typing.Optional[builtins.str] = None,
    volume_binding_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84604e53b327fc1f82e92acd6212ff4811d782c6cbf4b8348d57f97f2c3c90d6(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f7afd828a8753fd031dced5bf0056b4f522646fd57a6d2655eaeab9f3397e50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39f9291596f2b0e9f8ea231c674c73165fc3c1e83473b4103f366604ea9ba992(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c572c5833baec4298e263e05b5d906ab440c0c46b2e7fba03a7842a2d1cb42d3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a1cf194279370384b1eb6653d2bb97bcd9fd8be6c5a0518676e011ae18dfb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8313046935a0c20725f9ed0faacf75dc0d6c0311e5d2a4c810db7e25206cfb4e(
    value: typing.Optional[DataKubernetesStorageClassV1Metadata],
) -> None:
    """Type checking stubs"""
    pass
