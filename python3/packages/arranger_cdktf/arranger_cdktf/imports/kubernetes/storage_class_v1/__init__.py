'''
# `kubernetes_storage_class_v1`

Refer to the Terraform Registory for docs: [`kubernetes_storage_class_v1`](https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1).
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


class StorageClassV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.storageClassV1.StorageClassV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1 kubernetes_storage_class_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["StorageClassV1Metadata", typing.Dict[builtins.str, typing.Any]],
        storage_provisioner: builtins.str,
        allowed_topologies: typing.Optional[typing.Union["StorageClassV1AllowedTopologies", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1 kubernetes_storage_class_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#metadata StorageClassV1#metadata}
        :param storage_provisioner: Indicates the type of the provisioner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#storage_provisioner StorageClassV1#storage_provisioner}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#allowed_topologies StorageClassV1#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#allow_volume_expansion StorageClassV1#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#id StorageClassV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#mount_options StorageClassV1#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#parameters StorageClassV1#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#reclaim_policy StorageClassV1#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#volume_binding_mode StorageClassV1#volume_binding_mode}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb77c7b4513fbff56e04121577605f9f86f4540c51c0665afd7a5ac68cd6607)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageClassV1Config(
            metadata=metadata,
            storage_provisioner=storage_provisioner,
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
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageClassV1AllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#match_label_expressions StorageClassV1#match_label_expressions}
        '''
        value = StorageClassV1AllowedTopologies(
            match_label_expressions=match_label_expressions
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedTopologies", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#annotations StorageClassV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#generate_name StorageClassV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#labels StorageClassV1#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#name StorageClassV1#name}
        '''
        value = StorageClassV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
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
    def allowed_topologies(self) -> "StorageClassV1AllowedTopologiesOutputReference":
        return typing.cast("StorageClassV1AllowedTopologiesOutputReference", jsii.get(self, "allowedTopologies"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "StorageClassV1MetadataOutputReference":
        return typing.cast("StorageClassV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="allowedTopologiesInput")
    def allowed_topologies_input(
        self,
    ) -> typing.Optional["StorageClassV1AllowedTopologies"]:
        return typing.cast(typing.Optional["StorageClassV1AllowedTopologies"], jsii.get(self, "allowedTopologiesInput"))

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
    def metadata_input(self) -> typing.Optional["StorageClassV1Metadata"]:
        return typing.cast(typing.Optional["StorageClassV1Metadata"], jsii.get(self, "metadataInput"))

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
    @jsii.member(jsii_name="storageProvisionerInput")
    def storage_provisioner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageProvisionerInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d4839854ffe89a4c8c54f42c834406be65f484fd53e28b635a117c101245a7e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVolumeExpansion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2310de3e058e246b31d6a9eb948fa8c756eeb41016ea7ae9c43d479e192561f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d289b9b57948c9dbda2caa393ba51178989572b381a806ab33e40de13764717c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2884a5365c7464bf31a707650c586eaf100163cd531319d6bd4b0a674a58395b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicy")
    def reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reclaimPolicy"))

    @reclaim_policy.setter
    def reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__838be11402c421472a4f89320aef2cbdd6be784e04401f30440e48c01286a890)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="storageProvisioner")
    def storage_provisioner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageProvisioner"))

    @storage_provisioner.setter
    def storage_provisioner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ffffbd824ae5e21b334417f29777e238b96642c1d99a2aac3f3296533d86dc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageProvisioner", value)

    @builtins.property
    @jsii.member(jsii_name="volumeBindingMode")
    def volume_binding_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeBindingMode"))

    @volume_binding_mode.setter
    def volume_binding_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d7c29d13ea4b5396ac7847d996f9e0a3e04f1565d49b0dc5c88e7fc83d45c38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeBindingMode", value)


@jsii.data_type(
    jsii_type="kubernetes.storageClassV1.StorageClassV1AllowedTopologies",
    jsii_struct_bases=[],
    name_mapping={"match_label_expressions": "matchLabelExpressions"},
)
class StorageClassV1AllowedTopologies:
    def __init__(
        self,
        *,
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageClassV1AllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#match_label_expressions StorageClassV1#match_label_expressions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723b31a35c099923f06d5b7b61ca5b7b944e1f5a4bbe9e01d02fc4d78662ee7a)
            check_type(argname="argument match_label_expressions", value=match_label_expressions, expected_type=type_hints["match_label_expressions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_label_expressions is not None:
            self._values["match_label_expressions"] = match_label_expressions

    @builtins.property
    def match_label_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageClassV1AllowedTopologiesMatchLabelExpressions"]]]:
        '''match_label_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#match_label_expressions StorageClassV1#match_label_expressions}
        '''
        result = self._values.get("match_label_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageClassV1AllowedTopologiesMatchLabelExpressions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassV1AllowedTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.storageClassV1.StorageClassV1AllowedTopologiesMatchLabelExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class StorageClassV1AllowedTopologiesMatchLabelExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#key StorageClassV1#key}
        :param values: An array of string values. One value must match the label to be selected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#values StorageClassV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2e799ff17fdb75c8204ca18f58cc8de737ccfa4105f1c9ea1c11322bca4f8b)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#key StorageClassV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values. One value must match the label to be selected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#values StorageClassV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassV1AllowedTopologiesMatchLabelExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageClassV1AllowedTopologiesMatchLabelExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.storageClassV1.StorageClassV1AllowedTopologiesMatchLabelExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70ab088ae5e2bb845b2bc4e23176263d1b137773f992b15becb70b6fb10ad8a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e898ae5ec84736f2103a1341a140d7ab844ba280be87a631a94d808eb3daa46)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d73421e36f200beeeedb5382adacd16eb4e85f2fe9b2df1d7f4721c2cfeb294d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e6dcca107ce2a3319040aa4510610792437509a4b632c33230b01726b62ee6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb246957aa3aa4dd1f3f06c4e6143aa923abc37f428e7b6c712c5a5c9066b4f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassV1AllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassV1AllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassV1AllowedTopologiesMatchLabelExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d8ec6d6be41cd6bc117f9b6ef0d334d57ba557c9fc9193ac6725afbca4223c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.storageClassV1.StorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eedb09f6590a461b57d38bccaf7f82bddcdb47d7fca59a4e3d2e24540c82bb74)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b9e58dd6c201af5d9b600e5d151c4afa1b530a14a20cbf586db491df3f987cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__644b86b88ebf1532ea6fbd7c3df29fee78660aced31044961d8e90109f1c181c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f953962bdad741792d988ebfb063bc6292ebc5a68f32332d2d8e76fb3a04529a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageClassV1AllowedTopologiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.storageClassV1.StorageClassV1AllowedTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d1e38dcd16d07a1c306b5a62e1ab9c87822b98a1cbb7e13cf62ecb8cce96303)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchLabelExpressions")
    def put_match_label_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65bcafe2381d0108c70319f7c6c2001f5d9287cb46b36891e895ce9a0dcc7b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchLabelExpressions", [value]))

    @jsii.member(jsii_name="resetMatchLabelExpressions")
    def reset_match_label_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabelExpressions", []))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressions")
    def match_label_expressions(
        self,
    ) -> StorageClassV1AllowedTopologiesMatchLabelExpressionsList:
        return typing.cast(StorageClassV1AllowedTopologiesMatchLabelExpressionsList, jsii.get(self, "matchLabelExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressionsInput")
    def match_label_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassV1AllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassV1AllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "matchLabelExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageClassV1AllowedTopologies]:
        return typing.cast(typing.Optional[StorageClassV1AllowedTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageClassV1AllowedTopologies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06a3e4b1121ad30835013b6a471438079c77924e4407f930e6ad5ecc70e6c84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.storageClassV1.StorageClassV1Config",
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
        "storage_provisioner": "storageProvisioner",
        "allowed_topologies": "allowedTopologies",
        "allow_volume_expansion": "allowVolumeExpansion",
        "id": "id",
        "mount_options": "mountOptions",
        "parameters": "parameters",
        "reclaim_policy": "reclaimPolicy",
        "volume_binding_mode": "volumeBindingMode",
    },
)
class StorageClassV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["StorageClassV1Metadata", typing.Dict[builtins.str, typing.Any]],
        storage_provisioner: builtins.str,
        allowed_topologies: typing.Optional[typing.Union[StorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#metadata StorageClassV1#metadata}
        :param storage_provisioner: Indicates the type of the provisioner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#storage_provisioner StorageClassV1#storage_provisioner}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#allowed_topologies StorageClassV1#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#allow_volume_expansion StorageClassV1#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#id StorageClassV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#mount_options StorageClassV1#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#parameters StorageClassV1#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#reclaim_policy StorageClassV1#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#volume_binding_mode StorageClassV1#volume_binding_mode}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = StorageClassV1Metadata(**metadata)
        if isinstance(allowed_topologies, dict):
            allowed_topologies = StorageClassV1AllowedTopologies(**allowed_topologies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c283ea850bdd470b72d08419b3a4a15d28d73b6dd55472b8e2e7546a7bb5b6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument storage_provisioner", value=storage_provisioner, expected_type=type_hints["storage_provisioner"])
            check_type(argname="argument allowed_topologies", value=allowed_topologies, expected_type=type_hints["allowed_topologies"])
            check_type(argname="argument allow_volume_expansion", value=allow_volume_expansion, expected_type=type_hints["allow_volume_expansion"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument volume_binding_mode", value=volume_binding_mode, expected_type=type_hints["volume_binding_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "storage_provisioner": storage_provisioner,
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
    def metadata(self) -> "StorageClassV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#metadata StorageClassV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("StorageClassV1Metadata", result)

    @builtins.property
    def storage_provisioner(self) -> builtins.str:
        '''Indicates the type of the provisioner.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#storage_provisioner StorageClassV1#storage_provisioner}
        '''
        result = self._values.get("storage_provisioner")
        assert result is not None, "Required property 'storage_provisioner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_topologies(self) -> typing.Optional[StorageClassV1AllowedTopologies]:
        '''allowed_topologies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#allowed_topologies StorageClassV1#allowed_topologies}
        '''
        result = self._values.get("allowed_topologies")
        return typing.cast(typing.Optional[StorageClassV1AllowedTopologies], result)

    @builtins.property
    def allow_volume_expansion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the storage class allow volume expand.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#allow_volume_expansion StorageClassV1#allow_volume_expansion}
        '''
        result = self._values.get("allow_volume_expansion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#id StorageClassV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Persistent Volumes that are dynamically created by a storage class will have the mount options specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#mount_options StorageClassV1#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The parameters for the provisioner that should create volumes of this storage class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#parameters StorageClassV1#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''Indicates the type of the reclaim policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#reclaim_policy StorageClassV1#reclaim_policy}
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_binding_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates when volume binding and dynamic provisioning should occur.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#volume_binding_mode StorageClassV1#volume_binding_mode}
        '''
        result = self._values.get("volume_binding_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.storageClassV1.StorageClassV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class StorageClassV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#annotations StorageClassV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#generate_name StorageClassV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#labels StorageClassV1#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#name StorageClassV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e53d840a68b5409439431a30fbc48679737780a6740d4fe8f3390bd2ac54209)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#annotations StorageClassV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#generate_name StorageClassV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the storage class.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#labels StorageClassV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class_v1#name StorageClassV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageClassV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.storageClassV1.StorageClassV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8076339319f1d667b988edea3c27649cf142e1e69d3a8ce5ed1b88d6c7861ed)
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
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__720baf8487c5c0eb6d8064cbd75f3080b50cb012ca44591ca1306b6ac7d70e86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b57b5bbc749600eda3025f5cb6b44bfebdf343b9057ef2d559e12f8433d44b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8168c7d33ced7792294ec6779ad39da2ff7e4cf468aa763e0de0fed546f7b562)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41366acd60ac690f6fcedb11f9644939706f7feef55209b2cd30dbbb75978049)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageClassV1Metadata]:
        return typing.cast(typing.Optional[StorageClassV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageClassV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49df90eb90b97ebc41975371868381d41218167b372c53cb84d9b43dda260b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageClassV1",
    "StorageClassV1AllowedTopologies",
    "StorageClassV1AllowedTopologiesMatchLabelExpressions",
    "StorageClassV1AllowedTopologiesMatchLabelExpressionsList",
    "StorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference",
    "StorageClassV1AllowedTopologiesOutputReference",
    "StorageClassV1Config",
    "StorageClassV1Metadata",
    "StorageClassV1MetadataOutputReference",
]

publication.publish()

def _typecheckingstub__5bb77c7b4513fbff56e04121577605f9f86f4540c51c0665afd7a5ac68cd6607(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[StorageClassV1Metadata, typing.Dict[builtins.str, typing.Any]],
    storage_provisioner: builtins.str,
    allowed_topologies: typing.Optional[typing.Union[StorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__d4839854ffe89a4c8c54f42c834406be65f484fd53e28b635a117c101245a7e3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2310de3e058e246b31d6a9eb948fa8c756eeb41016ea7ae9c43d479e192561f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d289b9b57948c9dbda2caa393ba51178989572b381a806ab33e40de13764717c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2884a5365c7464bf31a707650c586eaf100163cd531319d6bd4b0a674a58395b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__838be11402c421472a4f89320aef2cbdd6be784e04401f30440e48c01286a890(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ffffbd824ae5e21b334417f29777e238b96642c1d99a2aac3f3296533d86dc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d7c29d13ea4b5396ac7847d996f9e0a3e04f1565d49b0dc5c88e7fc83d45c38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723b31a35c099923f06d5b7b61ca5b7b944e1f5a4bbe9e01d02fc4d78662ee7a(
    *,
    match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2e799ff17fdb75c8204ca18f58cc8de737ccfa4105f1c9ea1c11322bca4f8b(
    *,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ab088ae5e2bb845b2bc4e23176263d1b137773f992b15becb70b6fb10ad8a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e898ae5ec84736f2103a1341a140d7ab844ba280be87a631a94d808eb3daa46(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73421e36f200beeeedb5382adacd16eb4e85f2fe9b2df1d7f4721c2cfeb294d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e6dcca107ce2a3319040aa4510610792437509a4b632c33230b01726b62ee6d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb246957aa3aa4dd1f3f06c4e6143aa923abc37f428e7b6c712c5a5c9066b4f5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8ec6d6be41cd6bc117f9b6ef0d334d57ba557c9fc9193ac6725afbca4223c3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassV1AllowedTopologiesMatchLabelExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eedb09f6590a461b57d38bccaf7f82bddcdb47d7fca59a4e3d2e24540c82bb74(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9e58dd6c201af5d9b600e5d151c4afa1b530a14a20cbf586db491df3f987cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644b86b88ebf1532ea6fbd7c3df29fee78660aced31044961d8e90109f1c181c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f953962bdad741792d988ebfb063bc6292ebc5a68f32332d2d8e76fb3a04529a(
    value: typing.Optional[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d1e38dcd16d07a1c306b5a62e1ab9c87822b98a1cbb7e13cf62ecb8cce96303(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65bcafe2381d0108c70319f7c6c2001f5d9287cb46b36891e895ce9a0dcc7b57(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e06a3e4b1121ad30835013b6a471438079c77924e4407f930e6ad5ecc70e6c84(
    value: typing.Optional[StorageClassV1AllowedTopologies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c283ea850bdd470b72d08419b3a4a15d28d73b6dd55472b8e2e7546a7bb5b6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[StorageClassV1Metadata, typing.Dict[builtins.str, typing.Any]],
    storage_provisioner: builtins.str,
    allowed_topologies: typing.Optional[typing.Union[StorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reclaim_policy: typing.Optional[builtins.str] = None,
    volume_binding_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e53d840a68b5409439431a30fbc48679737780a6740d4fe8f3390bd2ac54209(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8076339319f1d667b988edea3c27649cf142e1e69d3a8ce5ed1b88d6c7861ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720baf8487c5c0eb6d8064cbd75f3080b50cb012ca44591ca1306b6ac7d70e86(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b57b5bbc749600eda3025f5cb6b44bfebdf343b9057ef2d559e12f8433d44b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8168c7d33ced7792294ec6779ad39da2ff7e4cf468aa763e0de0fed546f7b562(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41366acd60ac690f6fcedb11f9644939706f7feef55209b2cd30dbbb75978049(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49df90eb90b97ebc41975371868381d41218167b372c53cb84d9b43dda260b58(
    value: typing.Optional[StorageClassV1Metadata],
) -> None:
    """Type checking stubs"""
    pass
