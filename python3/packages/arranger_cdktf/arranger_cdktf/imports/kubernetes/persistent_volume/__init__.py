'''
# `kubernetes_persistent_volume`

Refer to the Terraform Registory for docs: [`kubernetes_persistent_volume`](https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume).
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


class PersistentVolume(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolume",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume kubernetes_persistent_volume}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["PersistentVolumeMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpec", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PersistentVolumeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume kubernetes_persistent_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#metadata PersistentVolume#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#spec PersistentVolume#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#id PersistentVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#timeouts PersistentVolume#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a6184870e60f1c7d059664f609d32e79472e6a1b6d1aa0c5564086e0d5a7d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PersistentVolumeConfig(
            metadata=metadata,
            spec=spec,
            id=id,
            timeouts=timeouts,
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
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#annotations PersistentVolume#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#labels PersistentVolume#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        value = PersistentVolumeMetadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpec", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b75ea377b78c94971e190ecc0c738dcaa1bf38588d5d767cfbc031b195dad7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#create PersistentVolume#create}.
        '''
        value = PersistentVolumeTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "PersistentVolumeMetadataOutputReference":
        return typing.cast("PersistentVolumeMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "PersistentVolumeSpecList":
        return typing.cast("PersistentVolumeSpecList", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PersistentVolumeTimeoutsOutputReference":
        return typing.cast("PersistentVolumeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["PersistentVolumeMetadata"]:
        return typing.cast(typing.Optional["PersistentVolumeMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]]], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PersistentVolumeTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PersistentVolumeTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a73a182ba1a01894f12e0603e3319d5067a0c069e2b0f131d5e05b7c8cb018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeConfig",
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
    },
)
class PersistentVolumeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["PersistentVolumeMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpec", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PersistentVolumeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#metadata PersistentVolume#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#spec PersistentVolume#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#id PersistentVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#timeouts PersistentVolume#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = PersistentVolumeMetadata(**metadata)
        if isinstance(timeouts, dict):
            timeouts = PersistentVolumeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75377da2e588936cbb65ddc9e300fee89c6813b814063da7d32d9cd69b20e133)
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
    def metadata(self) -> "PersistentVolumeMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#metadata PersistentVolume#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("PersistentVolumeMetadata", result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]]:
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#spec PersistentVolume#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#id PersistentVolume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PersistentVolumeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#timeouts PersistentVolume#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PersistentVolumeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class PersistentVolumeMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#annotations PersistentVolume#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#labels PersistentVolume#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5eaa320b74832413f72a5055f5612eaaa118b09f65e8f8e0740294ad53f915)
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
        '''An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#annotations PersistentVolume#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#labels PersistentVolume#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__389ce153473be03a8d5b57339504a84546058a2523a01b3d28f653364e562473)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a55d496820743780294d7830b03683a085172339205b8195de97bcf50c812754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59469c66645a9555010e95784d9b5320ca31fe7e037341bed48cba2c16cf0e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48c56f09d8ae43b10f21b574ef5cd4523dcb82d87afa28adf87d25cf45bc222c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeMetadata]:
        return typing.cast(typing.Optional[PersistentVolumeMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PersistentVolumeMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5104a414d37193dab35bb1c8ee8cf74a03cb3604d772d97c305319a61cd26221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpec",
    jsii_struct_bases=[],
    name_mapping={
        "access_modes": "accessModes",
        "capacity": "capacity",
        "persistent_volume_source": "persistentVolumeSource",
        "claim_ref": "claimRef",
        "mount_options": "mountOptions",
        "node_affinity": "nodeAffinity",
        "persistent_volume_reclaim_policy": "persistentVolumeReclaimPolicy",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeSpec:
    def __init__(
        self,
        *,
        access_modes: typing.Sequence[builtins.str],
        capacity: typing.Mapping[builtins.str, builtins.str],
        persistent_volume_source: typing.Union["PersistentVolumeSpecPersistentVolumeSource", typing.Dict[builtins.str, typing.Any]],
        claim_ref: typing.Optional[typing.Union["PersistentVolumeSpecClaimRef", typing.Dict[builtins.str, typing.Any]]] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_affinity: typing.Optional[typing.Union["PersistentVolumeSpecNodeAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_modes: Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#access_modes PersistentVolume#access_modes}
        :param capacity: A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#capacity PersistentVolume#capacity}
        :param persistent_volume_source: persistent_volume_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_source PersistentVolume#persistent_volume_source}
        :param claim_ref: claim_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#claim_ref PersistentVolume#claim_ref}
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#mount_options PersistentVolume#mount_options}
        :param node_affinity: node_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_affinity PersistentVolume#node_affinity}
        :param persistent_volume_reclaim_policy: What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_reclaim_policy PersistentVolume#persistent_volume_reclaim_policy}
        :param storage_class_name: A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#storage_class_name PersistentVolume#storage_class_name}
        :param volume_mode: Defines if a volume is intended to be used with a formatted filesystem. or to remain in raw block state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_mode PersistentVolume#volume_mode}
        '''
        if isinstance(persistent_volume_source, dict):
            persistent_volume_source = PersistentVolumeSpecPersistentVolumeSource(**persistent_volume_source)
        if isinstance(claim_ref, dict):
            claim_ref = PersistentVolumeSpecClaimRef(**claim_ref)
        if isinstance(node_affinity, dict):
            node_affinity = PersistentVolumeSpecNodeAffinity(**node_affinity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccfb5f9fe6a04ad41fc6812cd957b66a63eabc6132ff45ec714639fa6edc63d1)
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument persistent_volume_source", value=persistent_volume_source, expected_type=type_hints["persistent_volume_source"])
            check_type(argname="argument claim_ref", value=claim_ref, expected_type=type_hints["claim_ref"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument node_affinity", value=node_affinity, expected_type=type_hints["node_affinity"])
            check_type(argname="argument persistent_volume_reclaim_policy", value=persistent_volume_reclaim_policy, expected_type=type_hints["persistent_volume_reclaim_policy"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_modes": access_modes,
            "capacity": capacity,
            "persistent_volume_source": persistent_volume_source,
        }
        if claim_ref is not None:
            self._values["claim_ref"] = claim_ref
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if node_affinity is not None:
            self._values["node_affinity"] = node_affinity
        if persistent_volume_reclaim_policy is not None:
            self._values["persistent_volume_reclaim_policy"] = persistent_volume_reclaim_policy
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def access_modes(self) -> typing.List[builtins.str]:
        '''Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#access_modes PersistentVolume#access_modes}
        '''
        result = self._values.get("access_modes")
        assert result is not None, "Required property 'access_modes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#capacity PersistentVolume#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def persistent_volume_source(self) -> "PersistentVolumeSpecPersistentVolumeSource":
        '''persistent_volume_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_source PersistentVolume#persistent_volume_source}
        '''
        result = self._values.get("persistent_volume_source")
        assert result is not None, "Required property 'persistent_volume_source' is missing"
        return typing.cast("PersistentVolumeSpecPersistentVolumeSource", result)

    @builtins.property
    def claim_ref(self) -> typing.Optional["PersistentVolumeSpecClaimRef"]:
        '''claim_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#claim_ref PersistentVolume#claim_ref}
        '''
        result = self._values.get("claim_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecClaimRef"], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#mount_options PersistentVolume#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def node_affinity(self) -> typing.Optional["PersistentVolumeSpecNodeAffinity"]:
        '''node_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_affinity PersistentVolume#node_affinity}
        '''
        result = self._values.get("node_affinity")
        return typing.cast(typing.Optional["PersistentVolumeSpecNodeAffinity"], result)

    @builtins.property
    def persistent_volume_reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''What happens to a persistent volume when released from its claim.

        Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_reclaim_policy PersistentVolume#persistent_volume_reclaim_policy}
        '''
        result = self._values.get("persistent_volume_reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#storage_class_name PersistentVolume#storage_class_name}
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[builtins.str]:
        '''Defines if a volume is intended to be used with a formatted filesystem.

        or to remain in raw block state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_mode PersistentVolume#volume_mode}
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecClaimRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecClaimRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdcd21ea74b7bb88d128b8ecac9aba0c64f0636cb9d845bb4aedf7ecb1e7967b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the PersistentVolumeClaim.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecClaimRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecClaimRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecClaimRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b22e528fad26d22889b20d6e2437597258f1d77a367a2071d37453280f643f5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1dd45f067618dd85cce590b4a4a3c7653a876d2bfb08ccdd8bd364dfb7e71fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18128d0815a3c406db088a3705134b672513a46da0ed359d020beb5e1d3a16d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeSpecClaimRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecClaimRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecClaimRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a4e32cdee0510e6ef5d4caf1ec0062c18a97ab43bb4f372a2415b70beab0d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30a6be768dd10b119e5f032f44ce7adf9a9ee1d7494e010eac3574efdd800496)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PersistentVolumeSpecOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba62478e688dcacfeb44b8969bd3a0a36de1f8fb793e13cd822de32e53c597ef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd980d7ef87e037a19d1d065cd3e530c86b6956ba27ce561c95d0acd09dddd8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9edd86521c850e29576e86b077e94a25c965e3a8b8a36870b693ddccb2ce98fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fce7f57b2c57321a59c4f7095cd76f08112f7a19f660531e0b509190f344f54d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c2254996781ff8c46db509820948e337af8ac7e040dab0a6fae199763995f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinity",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class PersistentVolumeSpecNodeAffinity:
    def __init__(
        self,
        *,
        required: typing.Optional[typing.Union["PersistentVolumeSpecNodeAffinityRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#required PersistentVolume#required}
        '''
        if isinstance(required, dict):
            required = PersistentVolumeSpecNodeAffinityRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1e9f561264f90c7de3f62ed28f3c07fa8340ad1f58cf9c71f790e1816b5837)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional["PersistentVolumeSpecNodeAffinityRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#required PersistentVolume#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["PersistentVolumeSpecNodeAffinityRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80a2c2570814dcb78f5900c1215d58477521d2c1733d7d534231257a2e1596dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_selector_term PersistentVolume#node_selector_term}
        '''
        value = PersistentVolumeSpecNodeAffinityRequired(
            node_selector_term=node_selector_term
        )

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> "PersistentVolumeSpecNodeAffinityRequiredOutputReference":
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecNodeAffinityRequired"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecNodeAffinityRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeSpecNodeAffinity]:
        return typing.cast(typing.Optional[PersistentVolumeSpecNodeAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecNodeAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f4dc900c3c555660f85e3b48d744a8e137cdb3dd34b6e9ed9ea37684451744f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequired",
    jsii_struct_bases=[],
    name_mapping={"node_selector_term": "nodeSelectorTerm"},
)
class PersistentVolumeSpecNodeAffinityRequired:
    def __init__(
        self,
        *,
        node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_selector_term PersistentVolume#node_selector_term}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf12ee91ed4b51a07d33563e6ba7676a18e9948e25602ff2c1ee0b20b95e08f2)
            check_type(argname="argument node_selector_term", value=node_selector_term, expected_type=type_hints["node_selector_term"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "node_selector_term": node_selector_term,
        }

    @builtins.property
    def node_selector_term(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm"]]:
        '''node_selector_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_selector_term PersistentVolume#node_selector_term}
        '''
        result = self._values.get("node_selector_term")
        assert result is not None, "Required property 'node_selector_term' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_fields: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_expressions PersistentVolume#match_expressions}
        :param match_fields: match_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_fields PersistentVolume#match_fields}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f36a4ef4c7b1fdd502a0012418581ae27e75804186f72e71db798cde97437cbf)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_expressions PersistentVolume#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]]:
        '''match_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_fields PersistentVolume#match_fields}
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c73cee0a6fd5df869314e119f83858ddd4011676eef38b95f04be672f2a76cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59bc1e94663ded6cc5d8eaff16e1d36e01d09e65d61cd5bc853e33c8ee596f8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e71636db3714e95e813fb7bd615078b05c2c549ddc7a5bbbf21926ff0c7ddb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d450d62b538ec9b49fd94d7d792622874eba875cd41154e6c6988e6138da8ba6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3483ba2cbd39e0d85fe337b580a1eb1881f24cec34679649d29c8feb6101d861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4732f8a92979488316e030eb87906a54a449314cd8ba914280ec6d53aa9b7431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a1793bd7ada6d4ae3240096ecec52dbc54e9d1aa0e91b9b6f1dc34cce1fb88)
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
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9219d71ebccfba6a16ac18c2599731758524819b6b5ce0b4cdfff88be8a9c378)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14f9ef94402ee182f9d4e697334ea5dee65790f1b1098c83d8110d0b8bb13b22)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffa229168acb48177faef9daf4d154d64b2518dc78a997e34cc6f403a6b34cdd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1effe6d5c0cc063901741b219562588a28060c235a1616c97cf0192bc144072)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd6b0216d6f0b62e33bdfb67ecc3efdad1371d653f61f4fbf888de47f32011bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99eeef23847ac892a4e78daf6564de7c182a692683aa0e577111d0fc89f5a60e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f416b05e2546ce67f461ff88e33d3d7a7a4558a65afbfa2867773e1284385966)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__0fdcf201bd2942d28f91874af2683582aa85bbc11d2d8f88e23d3a3e8591c6c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd1e157f2025f667a1801b152b7616aec56b01a8531a32c4984b4f76e9d4078)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__838609132620f1df8b3d87f900abe10c23ba48f927bca96de4be0e1540271c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbe3dff2cf9b37f760443494883b69ed208dd66df8de414620703d38bea66946)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aeae0363ff3a978372353984fbc93236e72a589d23f0be6db049e9dab741bce)
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
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e58c4c4ba6e1eaa82f78b3c9e1f38d0fdfa6803a29db95d4d4264a804ff00dc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d81a1d8e2b06bcaa8e0a968d1233cc5cae1146e9e13f0c1addc4cbaf053bbd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22bdf6546b1095e243659df16e0981b23859d942096337fd4ef93420f68f7f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5acb03dd33a3ef5d31cd0f99db72a40f5fac71428b3a955e49e667fe794e4695)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c15e5ec75090227b17adf0c311bd7e5e6ced4cdd2e341990682f04d893bf1552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ce2d5f17c67fad621496c4afc70c0ff3c4f933e0f9e630ebee918f52779c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c7e253ef58b7167c2fbe698a01b6bb46038132782a9ec615e2f513666c62e35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__e9ed3d8164622bc050eef7a929eb34f225d3a4b5c6aee101e0a0863485a43c5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d89170d3ee885840924bc642439fc525c30458c68f4359804ff0af597a09583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991f22f91c732692d60929e10180ae8c885afae9fc8b62f168910e65b4e391aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e227f0daf92e9c97ca08e5866cd2386911b4a7d1d08101aaa12efae61f1ddd7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fe5eb967c8bca28714e1f94785678732d55aaf7b39c431dd842e3e50a8843d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4956fa31cfcc734dfa753f717429a7cc863564c9f141811d6958c803f80aec32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="putMatchFields")
    def put_match_fields(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a69d2749c9f0cb7cc9d32b0366c52dc5ab8dc6cd99042919c7ab59928c29f509)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchFields", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchFields")
    def reset_match_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchFields", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList:
        return typing.cast(PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchFields")
    def match_fields(
        self,
    ) -> PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList:
        return typing.cast(PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, jsii.get(self, "matchFields"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchFieldsInput")
    def match_fields_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "matchFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb5e1b57c95c84c2f10b7e5434155f288d82b6636b747cd0cd9057d3a23bdbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30dfb491676eb2043777300917f20670e941c405f6abfe53e2246f936ab1d5aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeSelectorTerm")
    def put_node_selector_term(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9f35e5042f4096e43cec25eed6c93b9266698e4fce1be414b4734859c97dd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeSelectorTerm", [value]))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTerm")
    def node_selector_term(
        self,
    ) -> PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList:
        return typing.cast(PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList, jsii.get(self, "nodeSelectorTerm"))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTermInput")
    def node_selector_term_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "nodeSelectorTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecNodeAffinityRequired]:
        return typing.cast(typing.Optional[PersistentVolumeSpecNodeAffinityRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecNodeAffinityRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51323e0ef5586794e0d3ae10ddfa0c19151b5495e50cccd1ad0e36c288bfcb1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2a1b1be3acaad5b30fe28ff09458e320ec42f09c2b4e45bc5258a81e43ca6d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClaimRef")
    def put_claim_ref(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecClaimRef(name=name, namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putClaimRef", [value]))

    @jsii.member(jsii_name="putNodeAffinity")
    def put_node_affinity(
        self,
        *,
        required: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequired, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#required PersistentVolume#required}
        '''
        value = PersistentVolumeSpecNodeAffinity(required=required)

        return typing.cast(None, jsii.invoke(self, "putNodeAffinity", [value]))

    @jsii.member(jsii_name="putPersistentVolumeSource")
    def put_persistent_volume_source(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureFile", typing.Dict[builtins.str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCephFs", typing.Dict[builtins.str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCinder", typing.Dict[builtins.str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsi", typing.Dict[builtins.str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFc", typing.Dict[builtins.str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlexVolume", typing.Dict[builtins.str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlocker", typing.Dict[builtins.str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGlusterfs", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceHostPath", typing.Dict[builtins.str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceIscsi", typing.Dict[builtins.str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceLocal", typing.Dict[builtins.str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceNfs", typing.Dict[builtins.str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceQuobyte", typing.Dict[builtins.str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbd", typing.Dict[builtins.str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#aws_elastic_block_store PersistentVolume#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_disk PersistentVolume#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_file PersistentVolume#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_fs PersistentVolume#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#cinder PersistentVolume#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#csi PersistentVolume#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fc PersistentVolume#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flex_volume PersistentVolume#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flocker PersistentVolume#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#gce_persistent_disk PersistentVolume#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#glusterfs PersistentVolume#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#host_path PersistentVolume#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi PersistentVolume#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#local PersistentVolume#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#nfs PersistentVolume#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#photon_persistent_disk PersistentVolume#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#quobyte PersistentVolume#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd PersistentVolume#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#vsphere_volume PersistentVolume#vsphere_volume}
        '''
        value = PersistentVolumeSpecPersistentVolumeSource(
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            ceph_fs=ceph_fs,
            cinder=cinder,
            csi=csi,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            local=local,
            nfs=nfs,
            photon_persistent_disk=photon_persistent_disk,
            quobyte=quobyte,
            rbd=rbd,
            vsphere_volume=vsphere_volume,
        )

        return typing.cast(None, jsii.invoke(self, "putPersistentVolumeSource", [value]))

    @jsii.member(jsii_name="resetClaimRef")
    def reset_claim_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimRef", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetNodeAffinity")
    def reset_node_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAffinity", []))

    @jsii.member(jsii_name="resetPersistentVolumeReclaimPolicy")
    def reset_persistent_volume_reclaim_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistentVolumeReclaimPolicy", []))

    @jsii.member(jsii_name="resetStorageClassName")
    def reset_storage_class_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClassName", []))

    @jsii.member(jsii_name="resetVolumeMode")
    def reset_volume_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeMode", []))

    @builtins.property
    @jsii.member(jsii_name="claimRef")
    def claim_ref(self) -> PersistentVolumeSpecClaimRefOutputReference:
        return typing.cast(PersistentVolumeSpecClaimRefOutputReference, jsii.get(self, "claimRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinity")
    def node_affinity(self) -> PersistentVolumeSpecNodeAffinityOutputReference:
        return typing.cast(PersistentVolumeSpecNodeAffinityOutputReference, jsii.get(self, "nodeAffinity"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSource")
    def persistent_volume_source(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceOutputReference", jsii.get(self, "persistentVolumeSource"))

    @builtins.property
    @jsii.member(jsii_name="accessModesInput")
    def access_modes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessModesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="claimRefInput")
    def claim_ref_input(self) -> typing.Optional[PersistentVolumeSpecClaimRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecClaimRef], jsii.get(self, "claimRefInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinityInput")
    def node_affinity_input(self) -> typing.Optional[PersistentVolumeSpecNodeAffinity]:
        return typing.cast(typing.Optional[PersistentVolumeSpecNodeAffinity], jsii.get(self, "nodeAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicyInput")
    def persistent_volume_reclaim_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "persistentVolumeReclaimPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSourceInput")
    def persistent_volume_source_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSource"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSource"], jsii.get(self, "persistentVolumeSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassNameInput")
    def storage_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeModeInput")
    def volume_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessModes"))

    @access_modes.setter
    def access_modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecaf3528e7fec94ac3c34b1682595c3e6eaa2b69f9e9c450d00e78fb645042f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessModes", value)

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a137d5429f4884e3f5dc7e5b528d4f2b763c783ee9459ec91d9f9cac253e13ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d2e76f7c1779c419adbfda314dd2496e8bda962889e39fb531907cbc0b5603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicy")
    def persistent_volume_reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistentVolumeReclaimPolicy"))

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5740f1e023cfcceb64680b26e7b544ee9b8ac1ba2c8c29e69e8a6ba880c1d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistentVolumeReclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClassName"))

    @storage_class_name.setter
    def storage_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9c4c9cd092ea5a05b7a64a283190b7209f45df28a8dc2dc5ff7a0e2e3c7727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClassName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeMode")
    def volume_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeMode"))

    @volume_mode.setter
    def volume_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__607ce9de5e60575122b74c7d795bf2cc0dc87a617292388225a7f8f998363fea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ab95d93bc9f37091fcb6284f2567f39063048a605edef33b621794f6fcbc357)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSource",
    jsii_struct_bases=[],
    name_mapping={
        "aws_elastic_block_store": "awsElasticBlockStore",
        "azure_disk": "azureDisk",
        "azure_file": "azureFile",
        "ceph_fs": "cephFs",
        "cinder": "cinder",
        "csi": "csi",
        "fc": "fc",
        "flex_volume": "flexVolume",
        "flocker": "flocker",
        "gce_persistent_disk": "gcePersistentDisk",
        "glusterfs": "glusterfs",
        "host_path": "hostPath",
        "iscsi": "iscsi",
        "local": "local",
        "nfs": "nfs",
        "photon_persistent_disk": "photonPersistentDisk",
        "quobyte": "quobyte",
        "rbd": "rbd",
        "vsphere_volume": "vsphereVolume",
    },
)
class PersistentVolumeSpecPersistentVolumeSource:
    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureFile", typing.Dict[builtins.str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCephFs", typing.Dict[builtins.str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCinder", typing.Dict[builtins.str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsi", typing.Dict[builtins.str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFc", typing.Dict[builtins.str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlexVolume", typing.Dict[builtins.str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlocker", typing.Dict[builtins.str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGlusterfs", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceHostPath", typing.Dict[builtins.str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceIscsi", typing.Dict[builtins.str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceLocal", typing.Dict[builtins.str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceNfs", typing.Dict[builtins.str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceQuobyte", typing.Dict[builtins.str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbd", typing.Dict[builtins.str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#aws_elastic_block_store PersistentVolume#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_disk PersistentVolume#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_file PersistentVolume#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_fs PersistentVolume#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#cinder PersistentVolume#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#csi PersistentVolume#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fc PersistentVolume#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flex_volume PersistentVolume#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flocker PersistentVolume#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#gce_persistent_disk PersistentVolume#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#glusterfs PersistentVolume#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#host_path PersistentVolume#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi PersistentVolume#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#local PersistentVolume#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#nfs PersistentVolume#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#photon_persistent_disk PersistentVolume#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#quobyte PersistentVolume#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd PersistentVolume#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#vsphere_volume PersistentVolume#vsphere_volume}
        '''
        if isinstance(aws_elastic_block_store, dict):
            aws_elastic_block_store = PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore(**aws_elastic_block_store)
        if isinstance(azure_disk, dict):
            azure_disk = PersistentVolumeSpecPersistentVolumeSourceAzureDisk(**azure_disk)
        if isinstance(azure_file, dict):
            azure_file = PersistentVolumeSpecPersistentVolumeSourceAzureFile(**azure_file)
        if isinstance(ceph_fs, dict):
            ceph_fs = PersistentVolumeSpecPersistentVolumeSourceCephFs(**ceph_fs)
        if isinstance(cinder, dict):
            cinder = PersistentVolumeSpecPersistentVolumeSourceCinder(**cinder)
        if isinstance(csi, dict):
            csi = PersistentVolumeSpecPersistentVolumeSourceCsi(**csi)
        if isinstance(fc, dict):
            fc = PersistentVolumeSpecPersistentVolumeSourceFc(**fc)
        if isinstance(flex_volume, dict):
            flex_volume = PersistentVolumeSpecPersistentVolumeSourceFlexVolume(**flex_volume)
        if isinstance(flocker, dict):
            flocker = PersistentVolumeSpecPersistentVolumeSourceFlocker(**flocker)
        if isinstance(gce_persistent_disk, dict):
            gce_persistent_disk = PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk(**gce_persistent_disk)
        if isinstance(glusterfs, dict):
            glusterfs = PersistentVolumeSpecPersistentVolumeSourceGlusterfs(**glusterfs)
        if isinstance(host_path, dict):
            host_path = PersistentVolumeSpecPersistentVolumeSourceHostPath(**host_path)
        if isinstance(iscsi, dict):
            iscsi = PersistentVolumeSpecPersistentVolumeSourceIscsi(**iscsi)
        if isinstance(local, dict):
            local = PersistentVolumeSpecPersistentVolumeSourceLocal(**local)
        if isinstance(nfs, dict):
            nfs = PersistentVolumeSpecPersistentVolumeSourceNfs(**nfs)
        if isinstance(photon_persistent_disk, dict):
            photon_persistent_disk = PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk(**photon_persistent_disk)
        if isinstance(quobyte, dict):
            quobyte = PersistentVolumeSpecPersistentVolumeSourceQuobyte(**quobyte)
        if isinstance(rbd, dict):
            rbd = PersistentVolumeSpecPersistentVolumeSourceRbd(**rbd)
        if isinstance(vsphere_volume, dict):
            vsphere_volume = PersistentVolumeSpecPersistentVolumeSourceVsphereVolume(**vsphere_volume)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404a5fa4a35be6cac04da0661fa5a9f3bf6b294b85ac4861a0c35101c32b6ddc)
            check_type(argname="argument aws_elastic_block_store", value=aws_elastic_block_store, expected_type=type_hints["aws_elastic_block_store"])
            check_type(argname="argument azure_disk", value=azure_disk, expected_type=type_hints["azure_disk"])
            check_type(argname="argument azure_file", value=azure_file, expected_type=type_hints["azure_file"])
            check_type(argname="argument ceph_fs", value=ceph_fs, expected_type=type_hints["ceph_fs"])
            check_type(argname="argument cinder", value=cinder, expected_type=type_hints["cinder"])
            check_type(argname="argument csi", value=csi, expected_type=type_hints["csi"])
            check_type(argname="argument fc", value=fc, expected_type=type_hints["fc"])
            check_type(argname="argument flex_volume", value=flex_volume, expected_type=type_hints["flex_volume"])
            check_type(argname="argument flocker", value=flocker, expected_type=type_hints["flocker"])
            check_type(argname="argument gce_persistent_disk", value=gce_persistent_disk, expected_type=type_hints["gce_persistent_disk"])
            check_type(argname="argument glusterfs", value=glusterfs, expected_type=type_hints["glusterfs"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument iscsi", value=iscsi, expected_type=type_hints["iscsi"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
            check_type(argname="argument photon_persistent_disk", value=photon_persistent_disk, expected_type=type_hints["photon_persistent_disk"])
            check_type(argname="argument quobyte", value=quobyte, expected_type=type_hints["quobyte"])
            check_type(argname="argument rbd", value=rbd, expected_type=type_hints["rbd"])
            check_type(argname="argument vsphere_volume", value=vsphere_volume, expected_type=type_hints["vsphere_volume"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_elastic_block_store is not None:
            self._values["aws_elastic_block_store"] = aws_elastic_block_store
        if azure_disk is not None:
            self._values["azure_disk"] = azure_disk
        if azure_file is not None:
            self._values["azure_file"] = azure_file
        if ceph_fs is not None:
            self._values["ceph_fs"] = ceph_fs
        if cinder is not None:
            self._values["cinder"] = cinder
        if csi is not None:
            self._values["csi"] = csi
        if fc is not None:
            self._values["fc"] = fc
        if flex_volume is not None:
            self._values["flex_volume"] = flex_volume
        if flocker is not None:
            self._values["flocker"] = flocker
        if gce_persistent_disk is not None:
            self._values["gce_persistent_disk"] = gce_persistent_disk
        if glusterfs is not None:
            self._values["glusterfs"] = glusterfs
        if host_path is not None:
            self._values["host_path"] = host_path
        if iscsi is not None:
            self._values["iscsi"] = iscsi
        if local is not None:
            self._values["local"] = local
        if nfs is not None:
            self._values["nfs"] = nfs
        if photon_persistent_disk is not None:
            self._values["photon_persistent_disk"] = photon_persistent_disk
        if quobyte is not None:
            self._values["quobyte"] = quobyte
        if rbd is not None:
            self._values["rbd"] = rbd
        if vsphere_volume is not None:
            self._values["vsphere_volume"] = vsphere_volume

    @builtins.property
    def aws_elastic_block_store(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore"]:
        '''aws_elastic_block_store block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#aws_elastic_block_store PersistentVolume#aws_elastic_block_store}
        '''
        result = self._values.get("aws_elastic_block_store")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore"], result)

    @builtins.property
    def azure_disk(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureDisk"]:
        '''azure_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_disk PersistentVolume#azure_disk}
        '''
        result = self._values.get("azure_disk")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureDisk"], result)

    @builtins.property
    def azure_file(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureFile"]:
        '''azure_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_file PersistentVolume#azure_file}
        '''
        result = self._values.get("azure_file")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureFile"], result)

    @builtins.property
    def ceph_fs(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFs"]:
        '''ceph_fs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_fs PersistentVolume#ceph_fs}
        '''
        result = self._values.get("ceph_fs")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFs"], result)

    @builtins.property
    def cinder(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCinder"]:
        '''cinder block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#cinder PersistentVolume#cinder}
        '''
        result = self._values.get("cinder")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCinder"], result)

    @builtins.property
    def csi(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsi"]:
        '''csi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#csi PersistentVolume#csi}
        '''
        result = self._values.get("csi")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsi"], result)

    @builtins.property
    def fc(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFc"]:
        '''fc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fc PersistentVolume#fc}
        '''
        result = self._values.get("fc")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFc"], result)

    @builtins.property
    def flex_volume(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolume"]:
        '''flex_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flex_volume PersistentVolume#flex_volume}
        '''
        result = self._values.get("flex_volume")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolume"], result)

    @builtins.property
    def flocker(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlocker"]:
        '''flocker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flocker PersistentVolume#flocker}
        '''
        result = self._values.get("flocker")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlocker"], result)

    @builtins.property
    def gce_persistent_disk(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk"]:
        '''gce_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#gce_persistent_disk PersistentVolume#gce_persistent_disk}
        '''
        result = self._values.get("gce_persistent_disk")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk"], result)

    @builtins.property
    def glusterfs(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGlusterfs"]:
        '''glusterfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#glusterfs PersistentVolume#glusterfs}
        '''
        result = self._values.get("glusterfs")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGlusterfs"], result)

    @builtins.property
    def host_path(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceHostPath"]:
        '''host_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#host_path PersistentVolume#host_path}
        '''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceHostPath"], result)

    @builtins.property
    def iscsi(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceIscsi"]:
        '''iscsi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi PersistentVolume#iscsi}
        '''
        result = self._values.get("iscsi")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceIscsi"], result)

    @builtins.property
    def local(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceLocal"]:
        '''local block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#local PersistentVolume#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceLocal"], result)

    @builtins.property
    def nfs(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceNfs"]:
        '''nfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#nfs PersistentVolume#nfs}
        '''
        result = self._values.get("nfs")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceNfs"], result)

    @builtins.property
    def photon_persistent_disk(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"]:
        '''photon_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#photon_persistent_disk PersistentVolume#photon_persistent_disk}
        '''
        result = self._values.get("photon_persistent_disk")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"], result)

    @builtins.property
    def quobyte(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"]:
        '''quobyte block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#quobyte PersistentVolume#quobyte}
        '''
        result = self._values.get("quobyte")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"], result)

    @builtins.property
    def rbd(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"]:
        '''rbd block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd PersistentVolume#rbd}
        '''
        result = self._values.get("rbd")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"], result)

    @builtins.property
    def vsphere_volume(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"]:
        '''vsphere_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#vsphere_volume PersistentVolume#vsphere_volume}
        '''
        result = self._values.get("vsphere_volume")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d98ff10ad3e80c81865f34e601b53bf1d539b0f9d6a749d9e72aef95c3d9d0b4)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86426a9cd546f1212fddd0f42da1e491e4d9e06bc0b5e20f03d906ebed2ef69d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd60fbfadcdd78071080559c413ce17394addaba146b315bd0e63272404ef711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f1bfc36526a6737a7484ce81c8ee8d0075d2c75ae737ee7219ae376000e1a58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd03ecec68e9766151236148349829a47650b99b6767bdc33ed02373785d63ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c31852032234320260ad6e4eb1e1897b98692bd1e65308c2ba4e59c2584efa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec80b050892252682586fe47751a35038574724b1d53e876caf91f469d35b68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching_mode": "cachingMode",
        "data_disk_uri": "dataDiskUri",
        "disk_name": "diskName",
        "fs_type": "fsType",
        "kind": "kind",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceAzureDisk:
    def __init__(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#caching_mode PersistentVolume#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#data_disk_uri PersistentVolume#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#disk_name PersistentVolume#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#kind PersistentVolume#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdb1db2c22488cc2ea088476561d726dd998b44e1f11186ebbb7966c51b4f6d8)
            check_type(argname="argument caching_mode", value=caching_mode, expected_type=type_hints["caching_mode"])
            check_type(argname="argument data_disk_uri", value=data_disk_uri, expected_type=type_hints["data_disk_uri"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "caching_mode": caching_mode,
            "data_disk_uri": data_disk_uri,
            "disk_name": disk_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def caching_mode(self) -> builtins.str:
        '''Host Caching mode: None, Read Only, Read Write.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#caching_mode PersistentVolume#caching_mode}
        '''
        result = self._values.get("caching_mode")
        assert result is not None, "Required property 'caching_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_disk_uri(self) -> builtins.str:
        '''The URI the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#data_disk_uri PersistentVolume#data_disk_uri}
        '''
        result = self._values.get("data_disk_uri")
        assert result is not None, "Required property 'data_disk_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The Name of the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#disk_name PersistentVolume#disk_name}
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#kind PersistentVolume#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceAzureDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ceb0a337abd4fccb2faf2f242903b762c8180b7d93ddc21cb9baae1ab2af3ce9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="cachingModeInput")
    def caching_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskUriInput")
    def data_disk_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataDiskUriInput"))

    @builtins.property
    @jsii.member(jsii_name="diskNameInput")
    def disk_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingMode")
    def caching_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cachingMode"))

    @caching_mode.setter
    def caching_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a46218030eb3c83935b0a22b5d06c1507df19b06f9b0081c952792fc12c0f98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingMode", value)

    @builtins.property
    @jsii.member(jsii_name="dataDiskUri")
    def data_disk_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataDiskUri"))

    @data_disk_uri.setter
    def data_disk_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ebe55efa73706c6ca6098c8c7063a104da88dbd63ee209871fc961c690f8d97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDiskUri", value)

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0768813cbd29acd03403757f37c896a5eab7625b3f5a46af50944849118fd86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97aa4c79777c1f24e369cbf0e513d5cf5dd76a588f78d5d23c42d1d5a43f49e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473beca9588a0fbb9ab39936483c8eeae23fed93f3f6c2f471daf2fea26b6e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8bb5cefe743d0707d4651b6ca944e9dd982dbcb79e6a407eab0d91fc55af225)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5c4c911bf1d90232603623fd915dc52bbcb4b2fc253816790758399d83925b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureFile",
    jsii_struct_bases=[],
    name_mapping={
        "secret_name": "secretName",
        "share_name": "shareName",
        "read_only": "readOnly",
        "secret_namespace": "secretNamespace",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceAzureFile:
    def __init__(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_name PersistentVolume#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#share_name PersistentVolume#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_namespace PersistentVolume#secret_namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce81e23af0b97561fdba435bd30c6d3c1772d82700823a826e76e474e208b610)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_namespace", value=secret_namespace, expected_type=type_hints["secret_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
            "share_name": share_name,
        }
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_namespace is not None:
            self._values["secret_namespace"] = secret_namespace

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''The name of secret that contains Azure Storage Account Name and Key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_name PersistentVolume#secret_name}
        '''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Share Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#share_name PersistentVolume#share_name}
        '''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the secret that contains Azure Storage Account Name and Key.

        For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_namespace PersistentVolume#secret_namespace}
        '''
        result = self._values.get("secret_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceAzureFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__296bef3b8dc4f884d6c029674dfb7ae630bb7f740d2236c2626cde1767c027d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretNamespace")
    def reset_secret_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNamespaceInput")
    def secret_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaac26b73ecaf967c42de2dd8e01bbc14d172541adf243cc6cff4ca91773bf90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fad77291da6b5eaf4e16dcfb68adb9895a05d4d49db9496f02f7bb19b9204be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="secretNamespace")
    def secret_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretNamespace"))

    @secret_namespace.setter
    def secret_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c707921aefe9b45ad673441dd034c53c0b19ee827333a09abd142524820138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__500d2d89f639e0ebfd00134615ea3e085c09369acc11033417e87cd226561a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd798c416c0edf7d5d411b22005df4c351507d53e198b5901aac939067c8188)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFs",
    jsii_struct_bases=[],
    name_mapping={
        "monitors": "monitors",
        "path": "path",
        "read_only": "readOnly",
        "secret_file": "secretFile",
        "secret_ref": "secretRef",
        "user": "user",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceCephFs:
    def __init__(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#monitors PersistentVolume#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_file PersistentVolume#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__920c52c5f73a545aa46628d8e94bc2ca94dc4746865768e089a53337f2b14801)
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_file", value=secret_file, expected_type=type_hints["secret_file"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitors": monitors,
        }
        if path is not None:
            self._values["path"] = path
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_file is not None:
            self._values["secret_file"] = secret_file
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def monitors(self) -> typing.List[builtins.str]:
        '''Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#monitors PersistentVolume#monitors}
        '''
        result = self._values.get("monitors")
        assert result is not None, "Required property 'monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Used as the mounted root, rather than the full Ceph tree, default is /.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_file(self) -> typing.Optional[builtins.str]:
        '''The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_file PersistentVolume#secret_file}
        '''
        result = self._values.get("secret_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCephFs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9c1a759f399ec2ca63113d4fbad12d521031fb559ac61bccccdcdbb843d1d7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretFile")
    def reset_secret_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretFile", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="monitorsInput")
    def monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "monitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretFileInput")
    def secret_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretFileInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1baf44f1585ca3980fd3900252bfd402eb5a881491a1870cf7ae7660f6d7a9aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitors", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f984a11f9820612fa25a9e14680d00732b912f4f764e12166c4dcc076d6b7625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb605878d0d564469b7a47d2884832f067ad07c4866a76d409a5e05adf572901)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretFile")
    def secret_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretFile"))

    @secret_file.setter
    def secret_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe98dbea219980d76223f1f5812ebb366d6d3fac032fe93816374d58651c719b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretFile", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea039ce698ac8df6d77ee9fa1afe8f1f490e532a450fcc20ff4096180a87c08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82923af7bde83bb72cb20d98b6446365023c58b0ab237cff7dfff3e02e9e1bf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caed1715a1a3dda7402e32d7aa81aa607da530bc64e742770e77b14c5f077430)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c18312270d1de3162942f57a0da0606484d114731870cad76f9181b27676bd9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7bf1ede2baa975dccbb6950c66954a33cc78d253407e8a655910b446d5a7fa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc3f570e20af7e141099e988703fb4473c992975865ff4295b234948c86a2f10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9a5394d1e7f55f68314a18033cba1d20837c7cf98882df5a5b2f7bfeacc0d93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCinder",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceCinder:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ee8458fcab0c4c480dd9140968a0b91164ff2e83f18188d7f054a6d24702356)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCinder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94352aa981418a887eb2a8ba7f3d4af2d67dc79b222f166b78c4ebfe2a05acdf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663d7d4f12271de3d9c3d5778c063c9e7dc9099571765467871f51e307511016)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c5872be90afb61f89069a599fa089da09053a7372fdcde357eaa0d718783ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71d72a2c7dca79ab8b0fe3437395e891f024d373259439f1932d45b8d8ef6d76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2251207125bc07175b408fc6d2dd81bae714135f6ebb34ba25b83e57057f108b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsi",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "volume_handle": "volumeHandle",
        "controller_expand_secret_ref": "controllerExpandSecretRef",
        "controller_publish_secret_ref": "controllerPublishSecretRef",
        "fs_type": "fsType",
        "node_publish_secret_ref": "nodePublishSecretRef",
        "node_stage_secret_ref": "nodeStageSecretRef",
        "read_only": "readOnly",
        "volume_attributes": "volumeAttributes",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceCsi:
    def __init__(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_handle PersistentVolume#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_expand_secret_ref PersistentVolume#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_publish_secret_ref PersistentVolume#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_publish_secret_ref PersistentVolume#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_stage_secret_ref PersistentVolume#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_attributes PersistentVolume#volume_attributes}
        '''
        if isinstance(controller_expand_secret_ref, dict):
            controller_expand_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef(**controller_expand_secret_ref)
        if isinstance(controller_publish_secret_ref, dict):
            controller_publish_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef(**controller_publish_secret_ref)
        if isinstance(node_publish_secret_ref, dict):
            node_publish_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef(**node_publish_secret_ref)
        if isinstance(node_stage_secret_ref, dict):
            node_stage_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef(**node_stage_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed2643de98eae22ea1cacf28b825cf36828ce32892acd2fdb558f350e183531)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument volume_handle", value=volume_handle, expected_type=type_hints["volume_handle"])
            check_type(argname="argument controller_expand_secret_ref", value=controller_expand_secret_ref, expected_type=type_hints["controller_expand_secret_ref"])
            check_type(argname="argument controller_publish_secret_ref", value=controller_publish_secret_ref, expected_type=type_hints["controller_publish_secret_ref"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument node_publish_secret_ref", value=node_publish_secret_ref, expected_type=type_hints["node_publish_secret_ref"])
            check_type(argname="argument node_stage_secret_ref", value=node_stage_secret_ref, expected_type=type_hints["node_stage_secret_ref"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument volume_attributes", value=volume_attributes, expected_type=type_hints["volume_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
            "volume_handle": volume_handle,
        }
        if controller_expand_secret_ref is not None:
            self._values["controller_expand_secret_ref"] = controller_expand_secret_ref
        if controller_publish_secret_ref is not None:
            self._values["controller_publish_secret_ref"] = controller_publish_secret_ref
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if node_publish_secret_ref is not None:
            self._values["node_publish_secret_ref"] = node_publish_secret_ref
        if node_stage_secret_ref is not None:
            self._values["node_stage_secret_ref"] = node_stage_secret_ref
        if read_only is not None:
            self._values["read_only"] = read_only
        if volume_attributes is not None:
            self._values["volume_attributes"] = volume_attributes

    @builtins.property
    def driver(self) -> builtins.str:
        '''the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_handle(self) -> builtins.str:
        '''A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_handle PersistentVolume#volume_handle}
        '''
        result = self._values.get("volume_handle")
        assert result is not None, "Required property 'volume_handle' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def controller_expand_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef"]:
        '''controller_expand_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_expand_secret_ref PersistentVolume#controller_expand_secret_ref}
        '''
        result = self._values.get("controller_expand_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef"], result)

    @builtins.property
    def controller_publish_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef"]:
        '''controller_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_publish_secret_ref PersistentVolume#controller_publish_secret_ref}
        '''
        result = self._values.get("controller_publish_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef"], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_publish_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef"]:
        '''node_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_publish_secret_ref PersistentVolume#node_publish_secret_ref}
        '''
        result = self._values.get("node_publish_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef"], result)

    @builtins.property
    def node_stage_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef"]:
        '''node_stage_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_stage_secret_ref PersistentVolume#node_stage_secret_ref}
        '''
        result = self._values.get("node_stage_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def volume_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Attributes of the volume to publish.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_attributes PersistentVolume#volume_attributes}
        '''
        result = self._values.get("volume_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1386d202ab876fee043f35197db8bfe61c5722b8b27f22b8894973e9c7c7e089)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__666f9568d2157e34c603b2ea6b1be0db7865cb7ed61c1133b43968862d925970)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e02f7d972c46a353aee54a580e77bcb2c6a69ba2d0cf6092af2ed4b5630b7b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3584a7b3d7498df605a93ba8333309218c6c7ea890180dac3bbe7b7593e2807e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a049acd60fd07f75a94fc60b64481d7291be89df4b77a61aa3b2abc072098ddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb0be1c97d6eab0d0c8e3c83f8b0e944d4b2e73e6580a3f002805fa066b965e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7664e8238a072697285ce2af3a7874ba112b4575b4c04fbfc0b4123c06fbc545)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f74bf620f6206f1e30f3941f690d78f3b46c5a1e7babdaacffe3b6bb55fc154)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbc51109d7533680a74e44f4b6607b2e59a024aeb0b5b7c13b051cf31cdb516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6153820c073333eb95c4f3be3b577b76d832b8307658c516f967a4badae99da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e24606d137a4b669a834675e480b5c4ae04f26d23f5e18b368aa66805a3ddc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__20fd288e35dfb51e84103b6b59882c7c3b837d8ac166f649017a67a338d8d153)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f846462ab16d036490797725cf2462bd7d72b6d8961befc9c8e15e1c3db3a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c440d7b23cc253cbd6f0ae98820552b079f3a1c2961ce87c1ce973ced13930f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a00676f92cc926312a272cca694d466c0d5924ab46f49d067ba567d342b7e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d252582fe21c5bd374ff021304d58b9a54e92c0ae9a6ad41d1524457bdaf55f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4195bce43941b5c504dc21d8e6c44ae19dad8e69cfbb5607fe90eda0c7dd0f05)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71dfb8d997d9a785826c653c4680792d490361b0c149a21e51e31f4b8d724279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c02805ec7f365307b8afcd1776bf4ce3841150a28586393f4909a3fc7073b233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9d39a5cc8fb240136525665239de3be125568aef17178bdda8cca8da46c2f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__623ab9a06adbccb865f150938b13d25a2504cd9a07e7b437520d501e1533accf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putControllerExpandSecretRef")
    def put_controller_expand_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerExpandSecretRef", [value]))

    @jsii.member(jsii_name="putControllerPublishSecretRef")
    def put_controller_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerPublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodePublishSecretRef")
    def put_node_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodePublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodeStageSecretRef")
    def put_node_stage_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodeStageSecretRef", [value]))

    @jsii.member(jsii_name="resetControllerExpandSecretRef")
    def reset_controller_expand_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerExpandSecretRef", []))

    @jsii.member(jsii_name="resetControllerPublishSecretRef")
    def reset_controller_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerPublishSecretRef", []))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetNodePublishSecretRef")
    def reset_node_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePublishSecretRef", []))

    @jsii.member(jsii_name="resetNodeStageSecretRef")
    def reset_node_stage_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeStageSecretRef", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetVolumeAttributes")
    def reset_volume_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRef")
    def controller_expand_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, jsii.get(self, "controllerExpandSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRef")
    def controller_publish_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, jsii.get(self, "controllerPublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRef")
    def node_publish_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, jsii.get(self, "nodePublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRef")
    def node_stage_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, jsii.get(self, "nodeStageSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRefInput")
    def controller_expand_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "controllerExpandSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRefInput")
    def controller_publish_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "controllerPublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRefInput")
    def node_publish_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "nodePublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRefInput")
    def node_stage_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "nodeStageSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeAttributesInput")
    def volume_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "volumeAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeHandleInput")
    def volume_handle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeHandleInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__197d7fde8c7f7d923e0d608adbc304e363afdfa99777d09b2c13abf6ab113e16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c01ace4f2be4c01ed736aaea80d9ee2f466c285b02e78f8f510f2d1cbd34ebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb315f84f0be250e8051b96c43f8dbafbe124d75a4c203447f7158b96bd7d31a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeAttributes")
    def volume_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "volumeAttributes"))

    @volume_attributes.setter
    def volume_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e542a9bceb15500b4a90e4383f180b6a821fff641b83216b093ec072d38073c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="volumeHandle")
    def volume_handle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeHandle"))

    @volume_handle.setter
    def volume_handle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51697cfe5cef4b716aa9332def59f6b097e12994c66bb5e7940ed6e282288824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeHandle", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d7f5c3f3301ae11899780bbbe17f228bca5b082005cb28015003b9fb4982b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFc",
    jsii_struct_bases=[],
    name_mapping={
        "lun": "lun",
        "target_ww_ns": "targetWwNs",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceFc:
    def __init__(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_ww_ns PersistentVolume#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fb0cf6b2b9b1959023b4625786e686d82bcf5d0b2f20394dc18f1d127e0c42f)
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument target_ww_ns", value=target_ww_ns, expected_type=type_hints["target_ww_ns"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lun": lun,
            "target_ww_ns": target_ww_ns,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def lun(self) -> jsii.Number:
        '''FC target lun number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        '''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target_ww_ns(self) -> typing.List[builtins.str]:
        '''FC target worldwide names (WWNs).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_ww_ns PersistentVolume#target_ww_ns}
        '''
        result = self._values.get("target_ww_ns")
        assert result is not None, "Required property 'target_ww_ns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2ae5eb4e1b395a37af9b24f4e0ce67ae24f8557c0027955cd5fdaafb3e40ca2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetWwNsInput")
    def target_ww_ns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetWwNsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d55b5ab22c860e2c334b68aafd3de8450c9ea96261b17ac3539c16c10ecc16a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56fe4660e69c63a07fbb505bbd3b0c3baec21f556996da1c4bbfc85e9f81d2fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09d09a64e94d7c05bc669d1b8f5666310e9fcb1673291050a61a2f0c610b7063)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetWwNs")
    def target_ww_ns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetWwNs"))

    @target_ww_ns.setter
    def target_ww_ns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0231011d258c8bbfa259b49c92eb48dc537803ac9f51ddff719ebb4da8abc697)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetWwNs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b1839a773a5aa2c47f824cd6da6527f818903dff2dfe1fd209c84d6770843d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolume",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "fs_type": "fsType",
        "options": "options",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceFlexVolume:
    def __init__(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#options PersistentVolume#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8c085c0d4cc3e89bec38f451a0e2fd8fa517fe0a0b20dafe15d5d85a85737f8)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if options is not None:
            self._values["options"] = options
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def driver(self) -> builtins.str:
        '''Driver is the name of the driver to use for this volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Extra command options if any.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#options PersistentVolume#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFlexVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f42a909bcc30d166ca4876216c044d649b22ef6bd906afadf92b03037215898b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2bd538bc9bac62d14346e441a90f86b958320f24c630ad7b3d0034d1b23fa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf4116f28fd77d0dee6a21cb9b7b7a59d7abc2ee342436a35d9509d2e392f13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b026830040e0c2d726ca904e94888bdacc4d861bd9fc4048b7d149ffdc44bfcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05954e814d26040fbdbf1ff97d0dd8f775bf706e751e9560303ed3d1f30e1493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b845b1a59df9a1c2f25be44766345fedca8c2dc8902c4eda0f78cc381671418c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__337998b9de5aaec16eb93f4c1daf8a991f2a4ba6341be5ad844add1521b81284)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6387ef14c771cc23c8d50a328974cc9da8e8285c40292ef23a38d9fbc407f39)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd2d0a83af5f6e91b7dc8d0d63eac41eb327cd98f152bbef611086fa02d7c36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e373a898de7d0147e3c2a2052036dec1cfc8b09bb69aedce529fca444a69a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1459a8e1ca826494d05f3b214c5af9da62b4f7d5a4a8de108c7cdfe3ed2968b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlocker",
    jsii_struct_bases=[],
    name_mapping={"dataset_name": "datasetName", "dataset_uuid": "datasetUuid"},
)
class PersistentVolumeSpecPersistentVolumeSourceFlocker:
    def __init__(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_name PersistentVolume#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_uuid PersistentVolume#dataset_uuid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a38054b27312f1db834f38d2bd83732e4f706d9b0e797ed01d80dd94587b36)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument dataset_uuid", value=dataset_uuid, expected_type=type_hints["dataset_uuid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if dataset_uuid is not None:
            self._values["dataset_uuid"] = dataset_uuid

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_name PersistentVolume#dataset_name}
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dataset_uuid(self) -> typing.Optional[builtins.str]:
        '''UUID of the dataset. This is unique identifier of a Flocker dataset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_uuid PersistentVolume#dataset_uuid}
        '''
        result = self._values.get("dataset_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFlocker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0e8597f58e6c6c06c9b0c1d2a1711a356b10501b6027355f779edf34dc8605e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetName")
    def reset_dataset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetName", []))

    @jsii.member(jsii_name="resetDatasetUuid")
    def reset_dataset_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetUuid", []))

    @builtins.property
    @jsii.member(jsii_name="datasetNameInput")
    def dataset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetUuidInput")
    def dataset_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec97419ff899bffece53110f342c8d4322d67d52805686637488b02dbae8b9a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value)

    @builtins.property
    @jsii.member(jsii_name="datasetUuid")
    def dataset_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetUuid"))

    @dataset_uuid.setter
    def dataset_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d01875562b81cb123156916202f0e4b6a2f8a65d1f11f13a895226f16e60621b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetUuid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1386f088572ce12c637f43b206e008140ab4968a0647df39f7a654fa448cfd52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk",
    jsii_struct_bases=[],
    name_mapping={
        "pd_name": "pdName",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk:
    def __init__(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_name PersistentVolume#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c3794ebbbb4f02002aad0534a6465537dbc803a75bb44e41fc111333e9ba67)
            check_type(argname="argument pd_name", value=pd_name, expected_type=type_hints["pd_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pd_name": pd_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def pd_name(self) -> builtins.str:
        '''Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_name PersistentVolume#pd_name}
        '''
        result = self._values.get("pd_name")
        assert result is not None, "Required property 'pd_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c83e297ff9f1fa030fcf491b29e5c81b8fc7392274e9b9f14f186ec78937e011)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="pdNameInput")
    def pd_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c134191e52b87adf25e26d1cdd1eb038fef5eccc73a9ccc446ca5c3d2431c35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7b553df3489fee3ddcef1e01950e9ae3278ec4e3107c4c4d86924bb22f657c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="pdName")
    def pd_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdName"))

    @pd_name.setter
    def pd_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c77bf0746916728fe1961eb964b23df9103fbb336290cca4a9d4b6bb99edfa38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdName", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83c63d6f37d9d5f8aaa540bddc16cb10086db21f33af6219551affe19b75053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3d6e2969d214a27fdf39f2833d7a25613a8f80ad7bcd7d7145069e320c0056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGlusterfs",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints_name": "endpointsName",
        "path": "path",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceGlusterfs:
    def __init__(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#endpoints_name PersistentVolume#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d1a3c5436e922d6c7a595352b240f36537cf7f55d15f5e0dc608a02e4c1c18)
            check_type(argname="argument endpoints_name", value=endpoints_name, expected_type=type_hints["endpoints_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoints_name": endpoints_name,
            "path": path,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def endpoints_name(self) -> builtins.str:
        '''The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#endpoints_name PersistentVolume#endpoints_name}
        '''
        result = self._values.get("endpoints_name")
        assert result is not None, "Required property 'endpoints_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceGlusterfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb3b377c0beaa4c91aa39f96385fb00971ca4e990bc3b566fca75d67306ff2d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="endpointsNameInput")
    def endpoints_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsName")
    def endpoints_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointsName"))

    @endpoints_name.setter
    def endpoints_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a80dab7665f3e3e17bf060c98fd4f2141185669b84c3f6722be2f05cbdf922f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointsName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ecf0496e240b8dea98facb869bbb17676e72a17ba527b6ed9a449016b87ac8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a615454c6dc2da9972260eb50bad9bce48402611e9660ca8a8a5c81c7fbc2c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3787bcf83aa184e3f1ada9f71fd43d36b071358111f2c6085fefb8312d0ee8e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceHostPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "type": "type"},
)
class PersistentVolumeSpecPersistentVolumeSourceHostPath:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#type PersistentVolume#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a82063d8220e51423177c008955902ab5d503ace839caac1d3f1ad6929864107)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#type PersistentVolume#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceHostPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d952e9e216cc520bdbed0ebee6ddacd0323affcf16afcfb305c231e175f6281d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6b2e8bf730f475d0bfa73f908adcf745c5cf243e3a903deed1e8f14877cec7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d3494d287a11c2f57722daf38b31295a30ad9507b6af223311cdd85a5012808)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a339ebae97fe23cf15699f647cdc1bb671a2297a9fe085263c7fbe7c4a24435)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceIscsi",
    jsii_struct_bases=[],
    name_mapping={
        "iqn": "iqn",
        "target_portal": "targetPortal",
        "fs_type": "fsType",
        "iscsi_interface": "iscsiInterface",
        "lun": "lun",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceIscsi:
    def __init__(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iqn PersistentVolume#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_portal PersistentVolume#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi_interface PersistentVolume#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb2179de46eefab40b9f2babbbad5d0f9e99fe6f6b0fd736ae031555fc3906a)
            check_type(argname="argument iqn", value=iqn, expected_type=type_hints["iqn"])
            check_type(argname="argument target_portal", value=target_portal, expected_type=type_hints["target_portal"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument iscsi_interface", value=iscsi_interface, expected_type=type_hints["iscsi_interface"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iqn": iqn,
            "target_portal": target_portal,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if iscsi_interface is not None:
            self._values["iscsi_interface"] = iscsi_interface
        if lun is not None:
            self._values["lun"] = lun
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def iqn(self) -> builtins.str:
        '''Target iSCSI Qualified Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iqn PersistentVolume#iqn}
        '''
        result = self._values.get("iqn")
        assert result is not None, "Required property 'iqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_portal(self) -> builtins.str:
        '''iSCSI target portal.

        The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_portal PersistentVolume#target_portal}
        '''
        result = self._values.get("target_portal")
        assert result is not None, "Required property 'target_portal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iscsi_interface(self) -> typing.Optional[builtins.str]:
        '''iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi_interface PersistentVolume#iscsi_interface}
        '''
        result = self._values.get("iscsi_interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lun(self) -> typing.Optional[jsii.Number]:
        '''iSCSI target lun number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        '''
        result = self._values.get("lun")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceIscsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__831fba4961634ade654cf4c3923c74018a831786db0ed8ede6fe1101858db35f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetIscsiInterface")
    def reset_iscsi_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiInterface", []))

    @jsii.member(jsii_name="resetLun")
    def reset_lun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLun", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iqnInput")
    def iqn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iqnInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInterfaceInput")
    def iscsi_interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscsiInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortalInput")
    def target_portal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e5eaa9b49c9fcef74f4b1df4cbb53e06dd725006ec9383f5d15c4da305d1ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="iqn")
    def iqn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iqn"))

    @iqn.setter
    def iqn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2dd0008dc9f5294c0fc7c06a47ad94a76603f1a7341fa8ce4461d022f6cf7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iqn", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiInterface")
    def iscsi_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscsiInterface"))

    @iscsi_interface.setter
    def iscsi_interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c94ab6e602cb29a6279eee13940f8607c432954d6610930b73249285a3692b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiInterface", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec65f23acb9d0f0113fd2aae77f9c7108a60512c8937225991c93104d10c9e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca845b48837f519a4d70e22b052e812f62d6c28a5d207adffe94bb76c05d1793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetPortal")
    def target_portal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPortal"))

    @target_portal.setter
    def target_portal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c316bcb99f0dbc4adfa057f122aa6506f872cceb1a9302b4790ecef7b41a43a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPortal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c4f5c00988fb841fcba62c743bc16ea208634549b3b9e982cfa94a3190dd84c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceLocal",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PersistentVolumeSpecPersistentVolumeSourceLocal:
    def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3e5a6e38558941d8c37cbeda1e19ce7b1a6bfa00f69acd4c4ec4e9d59942cf)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceLocal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c671c6b7c665643eae3c07c4af13acf7c5ed88d9129ad01366e09473e072e3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__bc2e0c1ce795b6d6bde7660c0f3170488cb3bfb34533d7ba44ffa222fe23e22c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48129b1fd7922f95abfc69486481263216e691c0661c8d2f8193fb104fb42c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceNfs",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "server": "server", "read_only": "readOnly"},
)
class PersistentVolumeSpecPersistentVolumeSourceNfs:
    def __init__(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#server PersistentVolume#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6140c97a7053eb3a9e5ae7cb09e847f84e9d443d071b6468c7712be4e0985fb)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
            "server": server,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path(self) -> builtins.str:
        '''Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#server PersistentVolume#server}
        '''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceNfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd7dcd195df00e304b2447cb63eecae78859429607ed17ca78645e8c3665fdea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7508729c237561ffb51a64bd3eba1b014f90a23cd3111bd4f003180f54ce3c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3628ec115048bc58318c89765283bc6516e2a10f3bbc778c6d66265b16772137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47c4df5c9b44c454ef1b396942af7ba730bc695733f698c2d1684e8fbb820e92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6cd9b8cb6e4e2d56f28861d7c1199afb07ede9a5f8c729bcb62c64b4eb01e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecPersistentVolumeSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad107e90288f52998544cf55e30ed34345c449246ea597f9fb6e2f3480a4cc54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsElasticBlockStore")
    def put_aws_elastic_block_store(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore(
            volume_id=volume_id,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsElasticBlockStore", [value]))

    @jsii.member(jsii_name="putAzureDisk")
    def put_azure_disk(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#caching_mode PersistentVolume#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#data_disk_uri PersistentVolume#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#disk_name PersistentVolume#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#kind PersistentVolume#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceAzureDisk(
            caching_mode=caching_mode,
            data_disk_uri=data_disk_uri,
            disk_name=disk_name,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureDisk", [value]))

    @jsii.member(jsii_name="putAzureFile")
    def put_azure_file(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_name PersistentVolume#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#share_name PersistentVolume#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_namespace PersistentVolume#secret_namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceAzureFile(
            secret_name=secret_name,
            share_name=share_name,
            read_only=read_only,
            secret_namespace=secret_namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureFile", [value]))

    @jsii.member(jsii_name="putCephFs")
    def put_ceph_fs(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#monitors PersistentVolume#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_file PersistentVolume#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCephFs(
            monitors=monitors,
            path=path,
            read_only=read_only,
            secret_file=secret_file,
            secret_ref=secret_ref,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putCephFs", [value]))

    @jsii.member(jsii_name="putCinder")
    def put_cinder(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCinder(
            volume_id=volume_id, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putCinder", [value]))

    @jsii.member(jsii_name="putCsi")
    def put_csi(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_handle PersistentVolume#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_expand_secret_ref PersistentVolume#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_publish_secret_ref PersistentVolume#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_publish_secret_ref PersistentVolume#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_stage_secret_ref PersistentVolume#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_attributes PersistentVolume#volume_attributes}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsi(
            driver=driver,
            volume_handle=volume_handle,
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            fs_type=fs_type,
            node_publish_secret_ref=node_publish_secret_ref,
            node_stage_secret_ref=node_stage_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
        )

        return typing.cast(None, jsii.invoke(self, "putCsi", [value]))

    @jsii.member(jsii_name="putFc")
    def put_fc(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_ww_ns PersistentVolume#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFc(
            lun=lun, target_ww_ns=target_ww_ns, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putFc", [value]))

    @jsii.member(jsii_name="putFlexVolume")
    def put_flex_volume(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#options PersistentVolume#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFlexVolume(
            driver=driver,
            fs_type=fs_type,
            options=options,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putFlexVolume", [value]))

    @jsii.member(jsii_name="putFlocker")
    def put_flocker(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_name PersistentVolume#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_uuid PersistentVolume#dataset_uuid}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFlocker(
            dataset_name=dataset_name, dataset_uuid=dataset_uuid
        )

        return typing.cast(None, jsii.invoke(self, "putFlocker", [value]))

    @jsii.member(jsii_name="putGcePersistentDisk")
    def put_gce_persistent_disk(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_name PersistentVolume#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk(
            pd_name=pd_name, fs_type=fs_type, partition=partition, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGcePersistentDisk", [value]))

    @jsii.member(jsii_name="putGlusterfs")
    def put_glusterfs(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#endpoints_name PersistentVolume#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceGlusterfs(
            endpoints_name=endpoints_name, path=path, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGlusterfs", [value]))

    @jsii.member(jsii_name="putHostPath")
    def put_host_path(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#type PersistentVolume#type}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceHostPath(
            path=path, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putHostPath", [value]))

    @jsii.member(jsii_name="putIscsi")
    def put_iscsi(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iqn PersistentVolume#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_portal PersistentVolume#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi_interface PersistentVolume#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceIscsi(
            iqn=iqn,
            target_portal=target_portal,
            fs_type=fs_type,
            iscsi_interface=iscsi_interface,
            lun=lun,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putIscsi", [value]))

    @jsii.member(jsii_name="putLocal")
    def put_local(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceLocal(path=path)

        return typing.cast(None, jsii.invoke(self, "putLocal", [value]))

    @jsii.member(jsii_name="putNfs")
    def put_nfs(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#server PersistentVolume#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceNfs(
            path=path, server=server, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putNfs", [value]))

    @jsii.member(jsii_name="putPhotonPersistentDisk")
    def put_photon_persistent_disk(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_id PersistentVolume#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk(
            pd_id=pd_id, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putPhotonPersistentDisk", [value]))

    @jsii.member(jsii_name="putQuobyte")
    def put_quobyte(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#registry PersistentVolume#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume PersistentVolume#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#group PersistentVolume#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceQuobyte(
            registry=registry,
            volume=volume,
            group=group,
            read_only=read_only,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putQuobyte", [value]))

    @jsii.member(jsii_name="putRbd")
    def put_rbd(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_monitors PersistentVolume#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_image PersistentVolume#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#keyring PersistentVolume#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rados_user PersistentVolume#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_pool PersistentVolume#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceRbd(
            ceph_monitors=ceph_monitors,
            rbd_image=rbd_image,
            fs_type=fs_type,
            keyring=keyring,
            rados_user=rados_user,
            rbd_pool=rbd_pool,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putRbd", [value]))

    @jsii.member(jsii_name="putVsphereVolume")
    def put_vsphere_volume(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_path PersistentVolume#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceVsphereVolume(
            volume_path=volume_path, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putVsphereVolume", [value]))

    @jsii.member(jsii_name="resetAwsElasticBlockStore")
    def reset_aws_elastic_block_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsElasticBlockStore", []))

    @jsii.member(jsii_name="resetAzureDisk")
    def reset_azure_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDisk", []))

    @jsii.member(jsii_name="resetAzureFile")
    def reset_azure_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFile", []))

    @jsii.member(jsii_name="resetCephFs")
    def reset_ceph_fs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCephFs", []))

    @jsii.member(jsii_name="resetCinder")
    def reset_cinder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCinder", []))

    @jsii.member(jsii_name="resetCsi")
    def reset_csi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsi", []))

    @jsii.member(jsii_name="resetFc")
    def reset_fc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFc", []))

    @jsii.member(jsii_name="resetFlexVolume")
    def reset_flex_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlexVolume", []))

    @jsii.member(jsii_name="resetFlocker")
    def reset_flocker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlocker", []))

    @jsii.member(jsii_name="resetGcePersistentDisk")
    def reset_gce_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcePersistentDisk", []))

    @jsii.member(jsii_name="resetGlusterfs")
    def reset_glusterfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlusterfs", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @jsii.member(jsii_name="resetIscsi")
    def reset_iscsi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsi", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetNfs")
    def reset_nfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfs", []))

    @jsii.member(jsii_name="resetPhotonPersistentDisk")
    def reset_photon_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonPersistentDisk", []))

    @jsii.member(jsii_name="resetQuobyte")
    def reset_quobyte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuobyte", []))

    @jsii.member(jsii_name="resetRbd")
    def reset_rbd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbd", []))

    @jsii.member(jsii_name="resetVsphereVolume")
    def reset_vsphere_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsphereVolume", []))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStore")
    def aws_elastic_block_store(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, jsii.get(self, "awsElasticBlockStore"))

    @builtins.property
    @jsii.member(jsii_name="azureDisk")
    def azure_disk(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference, jsii.get(self, "azureDisk"))

    @builtins.property
    @jsii.member(jsii_name="azureFile")
    def azure_file(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference, jsii.get(self, "azureFile"))

    @builtins.property
    @jsii.member(jsii_name="cephFs")
    def ceph_fs(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference, jsii.get(self, "cephFs"))

    @builtins.property
    @jsii.member(jsii_name="cinder")
    def cinder(self) -> PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference, jsii.get(self, "cinder"))

    @builtins.property
    @jsii.member(jsii_name="csi")
    def csi(self) -> PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference, jsii.get(self, "csi"))

    @builtins.property
    @jsii.member(jsii_name="fc")
    def fc(self) -> PersistentVolumeSpecPersistentVolumeSourceFcOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceFcOutputReference, jsii.get(self, "fc"))

    @builtins.property
    @jsii.member(jsii_name="flexVolume")
    def flex_volume(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference, jsii.get(self, "flexVolume"))

    @builtins.property
    @jsii.member(jsii_name="flocker")
    def flocker(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference, jsii.get(self, "flocker"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDisk")
    def gce_persistent_disk(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference, jsii.get(self, "gcePersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="glusterfs")
    def glusterfs(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference, jsii.get(self, "glusterfs"))

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference, jsii.get(self, "hostPath"))

    @builtins.property
    @jsii.member(jsii_name="iscsi")
    def iscsi(self) -> PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference, jsii.get(self, "iscsi"))

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference, jsii.get(self, "local"))

    @builtins.property
    @jsii.member(jsii_name="nfs")
    def nfs(self) -> PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference, jsii.get(self, "nfs"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDisk")
    def photon_persistent_disk(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference", jsii.get(self, "photonPersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="quobyte")
    def quobyte(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference", jsii.get(self, "quobyte"))

    @builtins.property
    @jsii.member(jsii_name="rbd")
    def rbd(self) -> "PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference", jsii.get(self, "rbd"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolume")
    def vsphere_volume(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference", jsii.get(self, "vsphereVolume"))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStoreInput")
    def aws_elastic_block_store_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "awsElasticBlockStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDiskInput")
    def azure_disk_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk], jsii.get(self, "azureDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFileInput")
    def azure_file_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile], jsii.get(self, "azureFileInput"))

    @builtins.property
    @jsii.member(jsii_name="cephFsInput")
    def ceph_fs_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs], jsii.get(self, "cephFsInput"))

    @builtins.property
    @jsii.member(jsii_name="cinderInput")
    def cinder_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder], jsii.get(self, "cinderInput"))

    @builtins.property
    @jsii.member(jsii_name="csiInput")
    def csi_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi], jsii.get(self, "csiInput"))

    @builtins.property
    @jsii.member(jsii_name="fcInput")
    def fc_input(self) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc], jsii.get(self, "fcInput"))

    @builtins.property
    @jsii.member(jsii_name="flexVolumeInput")
    def flex_volume_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume], jsii.get(self, "flexVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="flockerInput")
    def flocker_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker], jsii.get(self, "flockerInput"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDiskInput")
    def gce_persistent_disk_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "gcePersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="glusterfsInput")
    def glusterfs_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs], jsii.get(self, "glusterfsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInput")
    def iscsi_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi], jsii.get(self, "iscsiInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsInput")
    def nfs_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs], jsii.get(self, "nfsInput"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDiskInput")
    def photon_persistent_disk_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"], jsii.get(self, "photonPersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="quobyteInput")
    def quobyte_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"], jsii.get(self, "quobyteInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdInput")
    def rbd_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"], jsii.get(self, "rbdInput"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolumeInput")
    def vsphere_volume_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"], jsii.get(self, "vsphereVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSource]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2be69d84a78b4d0291802779322f72ad52ad3e192367908583246751fb2c47b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk",
    jsii_struct_bases=[],
    name_mapping={"pd_id": "pdId", "fs_type": "fsType"},
)
class PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk:
    def __init__(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_id PersistentVolume#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__263ffaa980738f2b00d03012b9b82f21071c277b019817a9d8d9bfc7b1ad01f5)
            check_type(argname="argument pd_id", value=pd_id, expected_type=type_hints["pd_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pd_id": pd_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def pd_id(self) -> builtins.str:
        '''ID that identifies Photon Controller persistent disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_id PersistentVolume#pd_id}
        '''
        result = self._values.get("pd_id")
        assert result is not None, "Required property 'pd_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8630df24d65170767965e838b58e30f58f5f2a7fc2b3662ce07aadd99a1f0b85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="pdIdInput")
    def pd_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e14981a53c48b1e9eec94c50b0ea27c2b608b6d491a28332aaf417ebfe46daaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="pdId")
    def pd_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdId"))

    @pd_id.setter
    def pd_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf3bf900608c66a7bfa974ff0293780a49be22e9523a99accb16e6866b2d0ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__631d666d8bf87dca2ec98abd13c13e9f309530152673ffe7d45483495ef790df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceQuobyte",
    jsii_struct_bases=[],
    name_mapping={
        "registry": "registry",
        "volume": "volume",
        "group": "group",
        "read_only": "readOnly",
        "user": "user",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceQuobyte:
    def __init__(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#registry PersistentVolume#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume PersistentVolume#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#group PersistentVolume#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31466a3f8c03f378b93999fbf1742240b775a3490aa4af7298f60b69b6b58aae)
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry": registry,
            "volume": volume,
        }
        if group is not None:
            self._values["group"] = group
        if read_only is not None:
            self._values["read_only"] = read_only
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def registry(self) -> builtins.str:
        '''Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#registry PersistentVolume#registry}
        '''
        result = self._values.get("registry")
        assert result is not None, "Required property 'registry' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume(self) -> builtins.str:
        '''Volume is a string that references an already created Quobyte volume by name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume PersistentVolume#volume}
        '''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group to map volume access to Default is no group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#group PersistentVolume#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User to map volume access to Defaults to serivceaccount user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceQuobyte(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__738097a4feeec81e19419f00c2840a457ec1eac3e9096a729939c3c92bdd4b8f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39fee6694dbe615c357aae58f8bdf4897717421814ca160c75dbe5ce1eae2bfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfddd8f5c67bef4c0732f78d1a6b84d3bd21c6d9dc83e850445682b152e338e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff0ce3820d7ce75400966024e2be016b883038742e0254e31d6bee32b8bb116)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1919c3902a3b20c044530ce3f0964857f28e28c68c3eacd80f2033f229ef7bfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @volume.setter
    def volume(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b89421f7edf530c52e87843e5e9fab3c6dd6288b54f48e478a82ec7c991301f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volume", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c438737b6f47232a4643fa1e2ba9cf310bc2794105952aec8a320d6fb2f5bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbd",
    jsii_struct_bases=[],
    name_mapping={
        "ceph_monitors": "cephMonitors",
        "rbd_image": "rbdImage",
        "fs_type": "fsType",
        "keyring": "keyring",
        "rados_user": "radosUser",
        "rbd_pool": "rbdPool",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceRbd:
    def __init__(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_monitors PersistentVolume#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_image PersistentVolume#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#keyring PersistentVolume#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rados_user PersistentVolume#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_pool PersistentVolume#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63bb1e7b0f3d4a05a4da9857e255070d91b17724b2b447e8a3511e8af3fc44ed)
            check_type(argname="argument ceph_monitors", value=ceph_monitors, expected_type=type_hints["ceph_monitors"])
            check_type(argname="argument rbd_image", value=rbd_image, expected_type=type_hints["rbd_image"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument keyring", value=keyring, expected_type=type_hints["keyring"])
            check_type(argname="argument rados_user", value=rados_user, expected_type=type_hints["rados_user"])
            check_type(argname="argument rbd_pool", value=rbd_pool, expected_type=type_hints["rbd_pool"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ceph_monitors": ceph_monitors,
            "rbd_image": rbd_image,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if keyring is not None:
            self._values["keyring"] = keyring
        if rados_user is not None:
            self._values["rados_user"] = rados_user
        if rbd_pool is not None:
            self._values["rbd_pool"] = rbd_pool
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def ceph_monitors(self) -> typing.List[builtins.str]:
        '''A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_monitors PersistentVolume#ceph_monitors}
        '''
        result = self._values.get("ceph_monitors")
        assert result is not None, "Required property 'ceph_monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rbd_image(self) -> builtins.str:
        '''The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_image PersistentVolume#rbd_image}
        '''
        result = self._values.get("rbd_image")
        assert result is not None, "Required property 'rbd_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyring(self) -> typing.Optional[builtins.str]:
        '''Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#keyring PersistentVolume#keyring}
        '''
        result = self._values.get("keyring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rados_user(self) -> typing.Optional[builtins.str]:
        '''The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rados_user PersistentVolume#rados_user}
        '''
        result = self._values.get("rados_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbd_pool(self) -> typing.Optional[builtins.str]:
        '''The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_pool PersistentVolume#rbd_pool}
        '''
        result = self._values.get("rbd_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceRbd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00183ebef62f60fbc231d6fa544c50576effba2aa2f7021b549e23e383cc175f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKeyring")
    def reset_keyring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyring", []))

    @jsii.member(jsii_name="resetRadosUser")
    def reset_rados_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadosUser", []))

    @jsii.member(jsii_name="resetRbdPool")
    def reset_rbd_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbdPool", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitorsInput")
    def ceph_monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cephMonitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyringInput")
    def keyring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyringInput"))

    @builtins.property
    @jsii.member(jsii_name="radosUserInput")
    def rados_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radosUserInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdImageInput")
    def rbd_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdImageInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdPoolInput")
    def rbd_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitors")
    def ceph_monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cephMonitors"))

    @ceph_monitors.setter
    def ceph_monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b0f30e2c0f85428db21197642b5b5a9b3a4a7f255d1299f92b963b8cc59061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cephMonitors", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4cfd5457a06528803d3a2028da4d18ad27a6df0f95c44d574c3cae4521ed595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="keyring")
    def keyring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyring"))

    @keyring.setter
    def keyring(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccda696f2d3d94f6d31b4bcda4e706245f0569df703894c12204df7d1c1d8dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyring", value)

    @builtins.property
    @jsii.member(jsii_name="radosUser")
    def rados_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radosUser"))

    @rados_user.setter
    def rados_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb14018f91510bd87c9616332e91c06bac40a3622d2f91123f1c42f212629f63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radosUser", value)

    @builtins.property
    @jsii.member(jsii_name="rbdImage")
    def rbd_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdImage"))

    @rbd_image.setter
    def rbd_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8266ea8c16f015dc636ddc5fbaa03fc4951ae9744ea211100e8d1897dda92d75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdImage", value)

    @builtins.property
    @jsii.member(jsii_name="rbdPool")
    def rbd_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdPool"))

    @rbd_pool.setter
    def rbd_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f78e178d900ffec601bd30b9fda4bf86f26aab1d4f9d36baeabb622c12cedf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdPool", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b638688cef8f01a032d5582823b1361534e03aeb020bdbbc2e0196e7fe5ab6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38d47d2178fb8f0c5066533edf072f2bdb5ae816d1b758fd48285b39fd342fa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e73889c55c58d9f543a2ada238f429dc25dedc3fe427c62190e6f35b7dde160)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e874451765d67410376cb0fb24d79f294f44f667dd4d594bca09bfcb5e973cd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b79b44c4cdadb941cad704ad26da55139e8a53d7fa9f456efc9c4d2fa4501ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be54173c0f4ddd54a732586a2cbcd744718150c4ea7deca6b4c456655a8337fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f76cd17483f48b396813c437d3e5b0929841c5577c09177512cfff787086ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceVsphereVolume",
    jsii_struct_bases=[],
    name_mapping={"volume_path": "volumePath", "fs_type": "fsType"},
)
class PersistentVolumeSpecPersistentVolumeSourceVsphereVolume:
    def __init__(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_path PersistentVolume#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e007e75ffb92e8f69fe9e0474b3ab5c8addc9f02876452d7ab69a590ac7a1c71)
            check_type(argname="argument volume_path", value=volume_path, expected_type=type_hints["volume_path"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_path": volume_path,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def volume_path(self) -> builtins.str:
        '''Path that identifies vSphere volume vmdk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_path PersistentVolume#volume_path}
        '''
        result = self._values.get("volume_path")
        assert result is not None, "Required property 'volume_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceVsphereVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab70ca701e1bbeea9e127a9729305af83532fb36821ac708b4e8a489680d1638)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumePathInput")
    def volume_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumePathInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be6f3ab722c7c2ad39de284898295eb8960fb9861e24cfa7c8be095af80f7b56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="volumePath")
    def volume_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumePath"))

    @volume_path.setter
    def volume_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc0d76c3abd931a400540d84ef183e91c11a2db7c9cd2f7348636c89eca0c4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumePath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456f4a532175ba45004f1a3652bb6da144ab24123151cc60e1e13e52dcfe9282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.persistentVolume.PersistentVolumeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class PersistentVolumeTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#create PersistentVolume#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce3f2456cedac4464ce08def2fee9abb5d9028408bd809f55578146b97816a48)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#create PersistentVolume#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.persistentVolume.PersistentVolumeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22b64dcee6b18a80fe54de3e9993e8ea8d8ce3f773563d7204df7ba3318b364b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87113a3c6676c4edc9530bfad814931689ff1901813f2143cca83c88e8ae449d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb5d5b82c6c4fb5b00246f4a26b9b72509385d6f50307ec3a8cf6233494bf57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PersistentVolume",
    "PersistentVolumeConfig",
    "PersistentVolumeMetadata",
    "PersistentVolumeMetadataOutputReference",
    "PersistentVolumeSpec",
    "PersistentVolumeSpecClaimRef",
    "PersistentVolumeSpecClaimRefOutputReference",
    "PersistentVolumeSpecList",
    "PersistentVolumeSpecNodeAffinity",
    "PersistentVolumeSpecNodeAffinityOutputReference",
    "PersistentVolumeSpecNodeAffinityRequired",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference",
    "PersistentVolumeSpecNodeAffinityRequiredOutputReference",
    "PersistentVolumeSpecOutputReference",
    "PersistentVolumeSpecPersistentVolumeSource",
    "PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore",
    "PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceAzureDisk",
    "PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceAzureFile",
    "PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCephFs",
    "PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCinder",
    "PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsi",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFc",
    "PersistentVolumeSpecPersistentVolumeSourceFcOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolume",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFlocker",
    "PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk",
    "PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceGlusterfs",
    "PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceHostPath",
    "PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceIscsi",
    "PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceLocal",
    "PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceNfs",
    "PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk",
    "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceQuobyte",
    "PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceRbd",
    "PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceVsphereVolume",
    "PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference",
    "PersistentVolumeTimeouts",
    "PersistentVolumeTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__22a6184870e60f1c7d059664f609d32e79472e6a1b6d1aa0c5564086e0d5a7d2(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[PersistentVolumeMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpec, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PersistentVolumeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__b75ea377b78c94971e190ecc0c738dcaa1bf38588d5d767cfbc031b195dad7fe(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpec, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a73a182ba1a01894f12e0603e3319d5067a0c069e2b0f131d5e05b7c8cb018(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75377da2e588936cbb65ddc9e300fee89c6813b814063da7d32d9cd69b20e133(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[PersistentVolumeMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpec, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PersistentVolumeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5eaa320b74832413f72a5055f5612eaaa118b09f65e8f8e0740294ad53f915(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389ce153473be03a8d5b57339504a84546058a2523a01b3d28f653364e562473(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55d496820743780294d7830b03683a085172339205b8195de97bcf50c812754(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59469c66645a9555010e95784d9b5320ca31fe7e037341bed48cba2c16cf0e4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48c56f09d8ae43b10f21b574ef5cd4523dcb82d87afa28adf87d25cf45bc222c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5104a414d37193dab35bb1c8ee8cf74a03cb3604d772d97c305319a61cd26221(
    value: typing.Optional[PersistentVolumeMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccfb5f9fe6a04ad41fc6812cd957b66a63eabc6132ff45ec714639fa6edc63d1(
    *,
    access_modes: typing.Sequence[builtins.str],
    capacity: typing.Mapping[builtins.str, builtins.str],
    persistent_volume_source: typing.Union[PersistentVolumeSpecPersistentVolumeSource, typing.Dict[builtins.str, typing.Any]],
    claim_ref: typing.Optional[typing.Union[PersistentVolumeSpecClaimRef, typing.Dict[builtins.str, typing.Any]]] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    node_affinity: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
    storage_class_name: typing.Optional[builtins.str] = None,
    volume_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcd21ea74b7bb88d128b8ecac9aba0c64f0636cb9d845bb4aedf7ecb1e7967b(
    *,
    name: builtins.str,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b22e528fad26d22889b20d6e2437597258f1d77a367a2071d37453280f643f5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1dd45f067618dd85cce590b4a4a3c7653a876d2bfb08ccdd8bd364dfb7e71fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18128d0815a3c406db088a3705134b672513a46da0ed359d020beb5e1d3a16d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a4e32cdee0510e6ef5d4caf1ec0062c18a97ab43bb4f372a2415b70beab0d0(
    value: typing.Optional[PersistentVolumeSpecClaimRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a6be768dd10b119e5f032f44ce7adf9a9ee1d7494e010eac3574efdd800496(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba62478e688dcacfeb44b8969bd3a0a36de1f8fb793e13cd822de32e53c597ef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd980d7ef87e037a19d1d065cd3e530c86b6956ba27ce561c95d0acd09dddd8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9edd86521c850e29576e86b077e94a25c965e3a8b8a36870b693ddccb2ce98fe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fce7f57b2c57321a59c4f7095cd76f08112f7a19f660531e0b509190f344f54d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c2254996781ff8c46db509820948e337af8ac7e040dab0a6fae199763995f5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1e9f561264f90c7de3f62ed28f3c07fa8340ad1f58cf9c71f790e1816b5837(
    *,
    required: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequired, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a2c2570814dcb78f5900c1215d58477521d2c1733d7d534231257a2e1596dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f4dc900c3c555660f85e3b48d744a8e137cdb3dd34b6e9ed9ea37684451744f(
    value: typing.Optional[PersistentVolumeSpecNodeAffinity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf12ee91ed4b51a07d33563e6ba7676a18e9948e25602ff2c1ee0b20b95e08f2(
    *,
    node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36a4ef4c7b1fdd502a0012418581ae27e75804186f72e71db798cde97437cbf(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_fields: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c73cee0a6fd5df869314e119f83858ddd4011676eef38b95f04be672f2a76cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59bc1e94663ded6cc5d8eaff16e1d36e01d09e65d61cd5bc853e33c8ee596f8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e71636db3714e95e813fb7bd615078b05c2c549ddc7a5bbbf21926ff0c7ddb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d450d62b538ec9b49fd94d7d792622874eba875cd41154e6c6988e6138da8ba6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3483ba2cbd39e0d85fe337b580a1eb1881f24cec34679649d29c8feb6101d861(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4732f8a92979488316e030eb87906a54a449314cd8ba914280ec6d53aa9b7431(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a1793bd7ada6d4ae3240096ecec52dbc54e9d1aa0e91b9b6f1dc34cce1fb88(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9219d71ebccfba6a16ac18c2599731758524819b6b5ce0b4cdfff88be8a9c378(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f9ef94402ee182f9d4e697334ea5dee65790f1b1098c83d8110d0b8bb13b22(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa229168acb48177faef9daf4d154d64b2518dc78a997e34cc6f403a6b34cdd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1effe6d5c0cc063901741b219562588a28060c235a1616c97cf0192bc144072(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6b0216d6f0b62e33bdfb67ecc3efdad1371d653f61f4fbf888de47f32011bc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99eeef23847ac892a4e78daf6564de7c182a692683aa0e577111d0fc89f5a60e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f416b05e2546ce67f461ff88e33d3d7a7a4558a65afbfa2867773e1284385966(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fdcf201bd2942d28f91874af2683582aa85bbc11d2d8f88e23d3a3e8591c6c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd1e157f2025f667a1801b152b7616aec56b01a8531a32c4984b4f76e9d4078(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__838609132620f1df8b3d87f900abe10c23ba48f927bca96de4be0e1540271c4c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbe3dff2cf9b37f760443494883b69ed208dd66df8de414620703d38bea66946(
    value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aeae0363ff3a978372353984fbc93236e72a589d23f0be6db049e9dab741bce(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58c4c4ba6e1eaa82f78b3c9e1f38d0fdfa6803a29db95d4d4264a804ff00dc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d81a1d8e2b06bcaa8e0a968d1233cc5cae1146e9e13f0c1addc4cbaf053bbd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22bdf6546b1095e243659df16e0981b23859d942096337fd4ef93420f68f7f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5acb03dd33a3ef5d31cd0f99db72a40f5fac71428b3a955e49e667fe794e4695(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c15e5ec75090227b17adf0c311bd7e5e6ced4cdd2e341990682f04d893bf1552(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ce2d5f17c67fad621496c4afc70c0ff3c4f933e0f9e630ebee918f52779c57(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7e253ef58b7167c2fbe698a01b6bb46038132782a9ec615e2f513666c62e35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ed3d8164622bc050eef7a929eb34f225d3a4b5c6aee101e0a0863485a43c5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d89170d3ee885840924bc642439fc525c30458c68f4359804ff0af597a09583(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991f22f91c732692d60929e10180ae8c885afae9fc8b62f168910e65b4e391aa(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e227f0daf92e9c97ca08e5866cd2386911b4a7d1d08101aaa12efae61f1ddd7a(
    value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe5eb967c8bca28714e1f94785678732d55aaf7b39c431dd842e3e50a8843d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4956fa31cfcc734dfa753f717429a7cc863564c9f141811d6958c803f80aec32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a69d2749c9f0cb7cc9d32b0366c52dc5ab8dc6cd99042919c7ab59928c29f509(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb5e1b57c95c84c2f10b7e5434155f288d82b6636b747cd0cd9057d3a23bdbe(
    value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30dfb491676eb2043777300917f20670e941c405f6abfe53e2246f936ab1d5aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9f35e5042f4096e43cec25eed6c93b9266698e4fce1be414b4734859c97dd6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51323e0ef5586794e0d3ae10ddfa0c19151b5495e50cccd1ad0e36c288bfcb1e(
    value: typing.Optional[PersistentVolumeSpecNodeAffinityRequired],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a1b1be3acaad5b30fe28ff09458e320ec42f09c2b4e45bc5258a81e43ca6d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecaf3528e7fec94ac3c34b1682595c3e6eaa2b69f9e9c450d00e78fb645042f5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a137d5429f4884e3f5dc7e5b528d4f2b763c783ee9459ec91d9f9cac253e13ae(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d2e76f7c1779c419adbfda314dd2496e8bda962889e39fb531907cbc0b5603(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5740f1e023cfcceb64680b26e7b544ee9b8ac1ba2c8c29e69e8a6ba880c1d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9c4c9cd092ea5a05b7a64a283190b7209f45df28a8dc2dc5ff7a0e2e3c7727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607ce9de5e60575122b74c7d795bf2cc0dc87a617292388225a7f8f998363fea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ab95d93bc9f37091fcb6284f2567f39063048a605edef33b621794f6fcbc357(
    value: typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404a5fa4a35be6cac04da0661fa5a9f3bf6b294b85ac4861a0c35101c32b6ddc(
    *,
    aws_elastic_block_store: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_disk: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceAzureDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_file: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceAzureFile, typing.Dict[builtins.str, typing.Any]]] = None,
    ceph_fs: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCephFs, typing.Dict[builtins.str, typing.Any]]] = None,
    cinder: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCinder, typing.Dict[builtins.str, typing.Any]]] = None,
    csi: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsi, typing.Dict[builtins.str, typing.Any]]] = None,
    fc: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFc, typing.Dict[builtins.str, typing.Any]]] = None,
    flex_volume: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlexVolume, typing.Dict[builtins.str, typing.Any]]] = None,
    flocker: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlocker, typing.Dict[builtins.str, typing.Any]]] = None,
    gce_persistent_disk: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    glusterfs: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceGlusterfs, typing.Dict[builtins.str, typing.Any]]] = None,
    host_path: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceHostPath, typing.Dict[builtins.str, typing.Any]]] = None,
    iscsi: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceIscsi, typing.Dict[builtins.str, typing.Any]]] = None,
    local: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceLocal, typing.Dict[builtins.str, typing.Any]]] = None,
    nfs: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceNfs, typing.Dict[builtins.str, typing.Any]]] = None,
    photon_persistent_disk: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    quobyte: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceQuobyte, typing.Dict[builtins.str, typing.Any]]] = None,
    rbd: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceRbd, typing.Dict[builtins.str, typing.Any]]] = None,
    vsphere_volume: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98ff10ad3e80c81865f34e601b53bf1d539b0f9d6a749d9e72aef95c3d9d0b4(
    *,
    volume_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    partition: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86426a9cd546f1212fddd0f42da1e491e4d9e06bc0b5e20f03d906ebed2ef69d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd60fbfadcdd78071080559c413ce17394addaba146b315bd0e63272404ef711(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1bfc36526a6737a7484ce81c8ee8d0075d2c75ae737ee7219ae376000e1a58(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd03ecec68e9766151236148349829a47650b99b6767bdc33ed02373785d63ab(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c31852032234320260ad6e4eb1e1897b98692bd1e65308c2ba4e59c2584efa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec80b050892252682586fe47751a35038574724b1d53e876caf91f469d35b68(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdb1db2c22488cc2ea088476561d726dd998b44e1f11186ebbb7966c51b4f6d8(
    *,
    caching_mode: builtins.str,
    data_disk_uri: builtins.str,
    disk_name: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceb0a337abd4fccb2faf2f242903b762c8180b7d93ddc21cb9baae1ab2af3ce9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a46218030eb3c83935b0a22b5d06c1507df19b06f9b0081c952792fc12c0f98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ebe55efa73706c6ca6098c8c7063a104da88dbd63ee209871fc961c690f8d97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0768813cbd29acd03403757f37c896a5eab7625b3f5a46af50944849118fd86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97aa4c79777c1f24e369cbf0e513d5cf5dd76a588f78d5d23c42d1d5a43f49e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473beca9588a0fbb9ab39936483c8eeae23fed93f3f6c2f471daf2fea26b6e34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8bb5cefe743d0707d4651b6ca944e9dd982dbcb79e6a407eab0d91fc55af225(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5c4c911bf1d90232603623fd915dc52bbcb4b2fc253816790758399d83925b(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce81e23af0b97561fdba435bd30c6d3c1772d82700823a826e76e474e208b610(
    *,
    secret_name: builtins.str,
    share_name: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296bef3b8dc4f884d6c029674dfb7ae630bb7f740d2236c2626cde1767c027d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaac26b73ecaf967c42de2dd8e01bbc14d172541adf243cc6cff4ca91773bf90(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fad77291da6b5eaf4e16dcfb68adb9895a05d4d49db9496f02f7bb19b9204be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c707921aefe9b45ad673441dd034c53c0b19ee827333a09abd142524820138(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500d2d89f639e0ebfd00134615ea3e085c09369acc11033417e87cd226561a39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd798c416c0edf7d5d411b22005df4c351507d53e198b5901aac939067c8188(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__920c52c5f73a545aa46628d8e94bc2ca94dc4746865768e089a53337f2b14801(
    *,
    monitors: typing.Sequence[builtins.str],
    path: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_file: typing.Optional[builtins.str] = None,
    secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c1a759f399ec2ca63113d4fbad12d521031fb559ac61bccccdcdbb843d1d7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1baf44f1585ca3980fd3900252bfd402eb5a881491a1870cf7ae7660f6d7a9aa(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f984a11f9820612fa25a9e14680d00732b912f4f764e12166c4dcc076d6b7625(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb605878d0d564469b7a47d2884832f067ad07c4866a76d409a5e05adf572901(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe98dbea219980d76223f1f5812ebb366d6d3fac032fe93816374d58651c719b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea039ce698ac8df6d77ee9fa1afe8f1f490e532a450fcc20ff4096180a87c08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82923af7bde83bb72cb20d98b6446365023c58b0ab237cff7dfff3e02e9e1bf4(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caed1715a1a3dda7402e32d7aa81aa607da530bc64e742770e77b14c5f077430(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c18312270d1de3162942f57a0da0606484d114731870cad76f9181b27676bd9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7bf1ede2baa975dccbb6950c66954a33cc78d253407e8a655910b446d5a7fa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3f570e20af7e141099e988703fb4473c992975865ff4295b234948c86a2f10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a5394d1e7f55f68314a18033cba1d20837c7cf98882df5a5b2f7bfeacc0d93(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee8458fcab0c4c480dd9140968a0b91164ff2e83f18188d7f054a6d24702356(
    *,
    volume_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94352aa981418a887eb2a8ba7f3d4af2d67dc79b222f166b78c4ebfe2a05acdf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663d7d4f12271de3d9c3d5778c063c9e7dc9099571765467871f51e307511016(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5872be90afb61f89069a599fa089da09053a7372fdcde357eaa0d718783ef4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d72a2c7dca79ab8b0fe3437395e891f024d373259439f1932d45b8d8ef6d76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2251207125bc07175b408fc6d2dd81bae714135f6ebb34ba25b83e57057f108b(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed2643de98eae22ea1cacf28b825cf36828ce32892acd2fdb558f350e183531(
    *,
    driver: builtins.str,
    volume_handle: builtins.str,
    controller_expand_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    controller_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    fs_type: typing.Optional[builtins.str] = None,
    node_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    node_stage_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1386d202ab876fee043f35197db8bfe61c5722b8b27f22b8894973e9c7c7e089(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__666f9568d2157e34c603b2ea6b1be0db7865cb7ed61c1133b43968862d925970(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e02f7d972c46a353aee54a580e77bcb2c6a69ba2d0cf6092af2ed4b5630b7b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3584a7b3d7498df605a93ba8333309218c6c7ea890180dac3bbe7b7593e2807e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a049acd60fd07f75a94fc60b64481d7291be89df4b77a61aa3b2abc072098ddd(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb0be1c97d6eab0d0c8e3c83f8b0e944d4b2e73e6580a3f002805fa066b965e(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7664e8238a072697285ce2af3a7874ba112b4575b4c04fbfc0b4123c06fbc545(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f74bf620f6206f1e30f3941f690d78f3b46c5a1e7babdaacffe3b6bb55fc154(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbc51109d7533680a74e44f4b6607b2e59a024aeb0b5b7c13b051cf31cdb516(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6153820c073333eb95c4f3be3b577b76d832b8307658c516f967a4badae99da(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e24606d137a4b669a834675e480b5c4ae04f26d23f5e18b368aa66805a3ddc(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fd288e35dfb51e84103b6b59882c7c3b837d8ac166f649017a67a338d8d153(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f846462ab16d036490797725cf2462bd7d72b6d8961befc9c8e15e1c3db3a16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c440d7b23cc253cbd6f0ae98820552b079f3a1c2961ce87c1ce973ced13930f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a00676f92cc926312a272cca694d466c0d5924ab46f49d067ba567d342b7e71(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d252582fe21c5bd374ff021304d58b9a54e92c0ae9a6ad41d1524457bdaf55f(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4195bce43941b5c504dc21d8e6c44ae19dad8e69cfbb5607fe90eda0c7dd0f05(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dfb8d997d9a785826c653c4680792d490361b0c149a21e51e31f4b8d724279(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c02805ec7f365307b8afcd1776bf4ce3841150a28586393f4909a3fc7073b233(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9d39a5cc8fb240136525665239de3be125568aef17178bdda8cca8da46c2f9(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__623ab9a06adbccb865f150938b13d25a2504cd9a07e7b437520d501e1533accf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197d7fde8c7f7d923e0d608adbc304e363afdfa99777d09b2c13abf6ab113e16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c01ace4f2be4c01ed736aaea80d9ee2f466c285b02e78f8f510f2d1cbd34ebc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb315f84f0be250e8051b96c43f8dbafbe124d75a4c203447f7158b96bd7d31a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e542a9bceb15500b4a90e4383f180b6a821fff641b83216b093ec072d38073c6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51697cfe5cef4b716aa9332def59f6b097e12994c66bb5e7940ed6e282288824(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7f5c3f3301ae11899780bbbe17f228bca5b082005cb28015003b9fb4982b7a(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb0cf6b2b9b1959023b4625786e686d82bcf5d0b2f20394dc18f1d127e0c42f(
    *,
    lun: jsii.Number,
    target_ww_ns: typing.Sequence[builtins.str],
    fs_type: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2ae5eb4e1b395a37af9b24f4e0ce67ae24f8557c0027955cd5fdaafb3e40ca2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55b5ab22c860e2c334b68aafd3de8450c9ea96261b17ac3539c16c10ecc16a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56fe4660e69c63a07fbb505bbd3b0c3baec21f556996da1c4bbfc85e9f81d2fe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d09a64e94d7c05bc669d1b8f5666310e9fcb1673291050a61a2f0c610b7063(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0231011d258c8bbfa259b49c92eb48dc537803ac9f51ddff719ebb4da8abc697(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b1839a773a5aa2c47f824cd6da6527f818903dff2dfe1fd209c84d6770843d(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8c085c0d4cc3e89bec38f451a0e2fd8fa517fe0a0b20dafe15d5d85a85737f8(
    *,
    driver: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42a909bcc30d166ca4876216c044d649b22ef6bd906afadf92b03037215898b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2bd538bc9bac62d14346e441a90f86b958320f24c630ad7b3d0034d1b23fa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf4116f28fd77d0dee6a21cb9b7b7a59d7abc2ee342436a35d9509d2e392f13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b026830040e0c2d726ca904e94888bdacc4d861bd9fc4048b7d149ffdc44bfcd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05954e814d26040fbdbf1ff97d0dd8f775bf706e751e9560303ed3d1f30e1493(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b845b1a59df9a1c2f25be44766345fedca8c2dc8902c4eda0f78cc381671418c(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__337998b9de5aaec16eb93f4c1daf8a991f2a4ba6341be5ad844add1521b81284(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6387ef14c771cc23c8d50a328974cc9da8e8285c40292ef23a38d9fbc407f39(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd2d0a83af5f6e91b7dc8d0d63eac41eb327cd98f152bbef611086fa02d7c36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e373a898de7d0147e3c2a2052036dec1cfc8b09bb69aedce529fca444a69a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1459a8e1ca826494d05f3b214c5af9da62b4f7d5a4a8de108c7cdfe3ed2968b(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a38054b27312f1db834f38d2bd83732e4f706d9b0e797ed01d80dd94587b36(
    *,
    dataset_name: typing.Optional[builtins.str] = None,
    dataset_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e8597f58e6c6c06c9b0c1d2a1711a356b10501b6027355f779edf34dc8605e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec97419ff899bffece53110f342c8d4322d67d52805686637488b02dbae8b9a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d01875562b81cb123156916202f0e4b6a2f8a65d1f11f13a895226f16e60621b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1386f088572ce12c637f43b206e008140ab4968a0647df39f7a654fa448cfd52(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c3794ebbbb4f02002aad0534a6465537dbc803a75bb44e41fc111333e9ba67(
    *,
    pd_name: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    partition: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83e297ff9f1fa030fcf491b29e5c81b8fc7392274e9b9f14f186ec78937e011(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c134191e52b87adf25e26d1cdd1eb038fef5eccc73a9ccc446ca5c3d2431c35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7b553df3489fee3ddcef1e01950e9ae3278ec4e3107c4c4d86924bb22f657c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c77bf0746916728fe1961eb964b23df9103fbb336290cca4a9d4b6bb99edfa38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83c63d6f37d9d5f8aaa540bddc16cb10086db21f33af6219551affe19b75053(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3d6e2969d214a27fdf39f2833d7a25613a8f80ad7bcd7d7145069e320c0056(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d1a3c5436e922d6c7a595352b240f36537cf7f55d15f5e0dc608a02e4c1c18(
    *,
    endpoints_name: builtins.str,
    path: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3b377c0beaa4c91aa39f96385fb00971ca4e990bc3b566fca75d67306ff2d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a80dab7665f3e3e17bf060c98fd4f2141185669b84c3f6722be2f05cbdf922f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecf0496e240b8dea98facb869bbb17676e72a17ba527b6ed9a449016b87ac8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a615454c6dc2da9972260eb50bad9bce48402611e9660ca8a8a5c81c7fbc2c3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3787bcf83aa184e3f1ada9f71fd43d36b071358111f2c6085fefb8312d0ee8e3(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82063d8220e51423177c008955902ab5d503ace839caac1d3f1ad6929864107(
    *,
    path: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d952e9e216cc520bdbed0ebee6ddacd0323affcf16afcfb305c231e175f6281d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6b2e8bf730f475d0bfa73f908adcf745c5cf243e3a903deed1e8f14877cec7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d3494d287a11c2f57722daf38b31295a30ad9507b6af223311cdd85a5012808(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a339ebae97fe23cf15699f647cdc1bb671a2297a9fe085263c7fbe7c4a24435(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb2179de46eefab40b9f2babbbad5d0f9e99fe6f6b0fd736ae031555fc3906a(
    *,
    iqn: builtins.str,
    target_portal: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    iscsi_interface: typing.Optional[builtins.str] = None,
    lun: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__831fba4961634ade654cf4c3923c74018a831786db0ed8ede6fe1101858db35f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e5eaa9b49c9fcef74f4b1df4cbb53e06dd725006ec9383f5d15c4da305d1ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2dd0008dc9f5294c0fc7c06a47ad94a76603f1a7341fa8ce4461d022f6cf7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c94ab6e602cb29a6279eee13940f8607c432954d6610930b73249285a3692b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec65f23acb9d0f0113fd2aae77f9c7108a60512c8937225991c93104d10c9e4c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca845b48837f519a4d70e22b052e812f62d6c28a5d207adffe94bb76c05d1793(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c316bcb99f0dbc4adfa057f122aa6506f872cceb1a9302b4790ecef7b41a43a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4f5c00988fb841fcba62c743bc16ea208634549b3b9e982cfa94a3190dd84c(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3e5a6e38558941d8c37cbeda1e19ce7b1a6bfa00f69acd4c4ec4e9d59942cf(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c671c6b7c665643eae3c07c4af13acf7c5ed88d9129ad01366e09473e072e3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2e0c1ce795b6d6bde7660c0f3170488cb3bfb34533d7ba44ffa222fe23e22c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48129b1fd7922f95abfc69486481263216e691c0661c8d2f8193fb104fb42c6(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6140c97a7053eb3a9e5ae7cb09e847f84e9d443d071b6468c7712be4e0985fb(
    *,
    path: builtins.str,
    server: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd7dcd195df00e304b2447cb63eecae78859429607ed17ca78645e8c3665fdea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7508729c237561ffb51a64bd3eba1b014f90a23cd3111bd4f003180f54ce3c56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3628ec115048bc58318c89765283bc6516e2a10f3bbc778c6d66265b16772137(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47c4df5c9b44c454ef1b396942af7ba730bc695733f698c2d1684e8fbb820e92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6cd9b8cb6e4e2d56f28861d7c1199afb07ede9a5f8c729bcb62c64b4eb01e9(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad107e90288f52998544cf55e30ed34345c449246ea597f9fb6e2f3480a4cc54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be69d84a78b4d0291802779322f72ad52ad3e192367908583246751fb2c47b6(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263ffaa980738f2b00d03012b9b82f21071c277b019817a9d8d9bfc7b1ad01f5(
    *,
    pd_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8630df24d65170767965e838b58e30f58f5f2a7fc2b3662ce07aadd99a1f0b85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e14981a53c48b1e9eec94c50b0ea27c2b608b6d491a28332aaf417ebfe46daaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3bf900608c66a7bfa974ff0293780a49be22e9523a99accb16e6866b2d0ffe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631d666d8bf87dca2ec98abd13c13e9f309530152673ffe7d45483495ef790df(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31466a3f8c03f378b93999fbf1742240b775a3490aa4af7298f60b69b6b58aae(
    *,
    registry: builtins.str,
    volume: builtins.str,
    group: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738097a4feeec81e19419f00c2840a457ec1eac3e9096a729939c3c92bdd4b8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39fee6694dbe615c357aae58f8bdf4897717421814ca160c75dbe5ce1eae2bfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfddd8f5c67bef4c0732f78d1a6b84d3bd21c6d9dc83e850445682b152e338e7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff0ce3820d7ce75400966024e2be016b883038742e0254e31d6bee32b8bb116(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1919c3902a3b20c044530ce3f0964857f28e28c68c3eacd80f2033f229ef7bfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b89421f7edf530c52e87843e5e9fab3c6dd6288b54f48e478a82ec7c991301f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c438737b6f47232a4643fa1e2ba9cf310bc2794105952aec8a320d6fb2f5bd(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bb1e7b0f3d4a05a4da9857e255070d91b17724b2b447e8a3511e8af3fc44ed(
    *,
    ceph_monitors: typing.Sequence[builtins.str],
    rbd_image: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    keyring: typing.Optional[builtins.str] = None,
    rados_user: typing.Optional[builtins.str] = None,
    rbd_pool: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00183ebef62f60fbc231d6fa544c50576effba2aa2f7021b549e23e383cc175f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b0f30e2c0f85428db21197642b5b5a9b3a4a7f255d1299f92b963b8cc59061(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4cfd5457a06528803d3a2028da4d18ad27a6df0f95c44d574c3cae4521ed595(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccda696f2d3d94f6d31b4bcda4e706245f0569df703894c12204df7d1c1d8dc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb14018f91510bd87c9616332e91c06bac40a3622d2f91123f1c42f212629f63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8266ea8c16f015dc636ddc5fbaa03fc4951ae9744ea211100e8d1897dda92d75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f78e178d900ffec601bd30b9fda4bf86f26aab1d4f9d36baeabb622c12cedf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b638688cef8f01a032d5582823b1361534e03aeb020bdbbc2e0196e7fe5ab6b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38d47d2178fb8f0c5066533edf072f2bdb5ae816d1b758fd48285b39fd342fa1(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e73889c55c58d9f543a2ada238f429dc25dedc3fe427c62190e6f35b7dde160(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e874451765d67410376cb0fb24d79f294f44f667dd4d594bca09bfcb5e973cd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b79b44c4cdadb941cad704ad26da55139e8a53d7fa9f456efc9c4d2fa4501ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be54173c0f4ddd54a732586a2cbcd744718150c4ea7deca6b4c456655a8337fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f76cd17483f48b396813c437d3e5b0929841c5577c09177512cfff787086ff2(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e007e75ffb92e8f69fe9e0474b3ab5c8addc9f02876452d7ab69a590ac7a1c71(
    *,
    volume_path: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab70ca701e1bbeea9e127a9729305af83532fb36821ac708b4e8a489680d1638(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6f3ab722c7c2ad39de284898295eb8960fb9861e24cfa7c8be095af80f7b56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc0d76c3abd931a400540d84ef183e91c11a2db7c9cd2f7348636c89eca0c4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456f4a532175ba45004f1a3652bb6da144ab24123151cc60e1e13e52dcfe9282(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3f2456cedac4464ce08def2fee9abb5d9028408bd809f55578146b97816a48(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b64dcee6b18a80fe54de3e9993e8ea8d8ce3f773563d7204df7ba3318b364b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87113a3c6676c4edc9530bfad814931689ff1901813f2143cca83c88e8ae449d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb5d5b82c6c4fb5b00246f4a26b9b72509385d6f50307ec3a8cf6233494bf57(
    value: typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
