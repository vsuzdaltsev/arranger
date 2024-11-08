'''
# `aws_emrserverless_application`

Refer to the Terraform Registory for docs: [`aws_emrserverless_application`](https://www.terraform.io/docs/providers/aws/r/emrserverless_application).
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


class EmrserverlessApplication(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application aws_emrserverless_application}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        release_label: builtins.str,
        type: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        auto_start_configuration: typing.Optional[typing.Union["EmrserverlessApplicationAutoStartConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_stop_configuration: typing.Optional[typing.Union["EmrserverlessApplicationAutoStopConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initial_capacity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrserverlessApplicationInitialCapacity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        maximum_capacity: typing.Optional[typing.Union["EmrserverlessApplicationMaximumCapacity", typing.Dict[builtins.str, typing.Any]]] = None,
        network_configuration: typing.Optional[typing.Union["EmrserverlessApplicationNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application aws_emrserverless_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#name EmrserverlessApplication#name}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#release_label EmrserverlessApplication#release_label}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#type EmrserverlessApplication#type}.
        :param architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#architecture EmrserverlessApplication#architecture}.
        :param auto_start_configuration: auto_start_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#auto_start_configuration EmrserverlessApplication#auto_start_configuration}
        :param auto_stop_configuration: auto_stop_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#auto_stop_configuration EmrserverlessApplication#auto_stop_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#id EmrserverlessApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_capacity: initial_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity EmrserverlessApplication#initial_capacity}
        :param maximum_capacity: maximum_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#maximum_capacity EmrserverlessApplication#maximum_capacity}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#network_configuration EmrserverlessApplication#network_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#tags EmrserverlessApplication#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#tags_all EmrserverlessApplication#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91467d39e834de1657d4547c2c997bbc649e9d06781d23bce02cc15d7454a237)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EmrserverlessApplicationConfig(
            name=name,
            release_label=release_label,
            type=type,
            architecture=architecture,
            auto_start_configuration=auto_start_configuration,
            auto_stop_configuration=auto_stop_configuration,
            id=id,
            initial_capacity=initial_capacity,
            maximum_capacity=maximum_capacity,
            network_configuration=network_configuration,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoStartConfiguration")
    def put_auto_start_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#enabled EmrserverlessApplication#enabled}.
        '''
        value = EmrserverlessApplicationAutoStartConfiguration(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putAutoStartConfiguration", [value]))

    @jsii.member(jsii_name="putAutoStopConfiguration")
    def put_auto_stop_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        idle_timeout_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#enabled EmrserverlessApplication#enabled}.
        :param idle_timeout_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#idle_timeout_minutes EmrserverlessApplication#idle_timeout_minutes}.
        '''
        value = EmrserverlessApplicationAutoStopConfiguration(
            enabled=enabled, idle_timeout_minutes=idle_timeout_minutes
        )

        return typing.cast(None, jsii.invoke(self, "putAutoStopConfiguration", [value]))

    @jsii.member(jsii_name="putInitialCapacity")
    def put_initial_capacity(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrserverlessApplicationInitialCapacity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2e168307ad4c3b288a29d5a46bf47dfbf9635510eafcd225d4d864c0d51e8f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitialCapacity", [value]))

    @jsii.member(jsii_name="putMaximumCapacity")
    def put_maximum_capacity(
        self,
        *,
        cpu: builtins.str,
        memory: builtins.str,
        disk: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#cpu EmrserverlessApplication#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#memory EmrserverlessApplication#memory}.
        :param disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#disk EmrserverlessApplication#disk}.
        '''
        value = EmrserverlessApplicationMaximumCapacity(
            cpu=cpu, memory=memory, disk=disk
        )

        return typing.cast(None, jsii.invoke(self, "putMaximumCapacity", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#security_group_ids EmrserverlessApplication#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#subnet_ids EmrserverlessApplication#subnet_ids}.
        '''
        value = EmrserverlessApplicationNetworkConfiguration(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="resetArchitecture")
    def reset_architecture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchitecture", []))

    @jsii.member(jsii_name="resetAutoStartConfiguration")
    def reset_auto_start_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStartConfiguration", []))

    @jsii.member(jsii_name="resetAutoStopConfiguration")
    def reset_auto_stop_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStopConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialCapacity")
    def reset_initial_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialCapacity", []))

    @jsii.member(jsii_name="resetMaximumCapacity")
    def reset_maximum_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumCapacity", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="autoStartConfiguration")
    def auto_start_configuration(
        self,
    ) -> "EmrserverlessApplicationAutoStartConfigurationOutputReference":
        return typing.cast("EmrserverlessApplicationAutoStartConfigurationOutputReference", jsii.get(self, "autoStartConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="autoStopConfiguration")
    def auto_stop_configuration(
        self,
    ) -> "EmrserverlessApplicationAutoStopConfigurationOutputReference":
        return typing.cast("EmrserverlessApplicationAutoStopConfigurationOutputReference", jsii.get(self, "autoStopConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="initialCapacity")
    def initial_capacity(self) -> "EmrserverlessApplicationInitialCapacityList":
        return typing.cast("EmrserverlessApplicationInitialCapacityList", jsii.get(self, "initialCapacity"))

    @builtins.property
    @jsii.member(jsii_name="maximumCapacity")
    def maximum_capacity(
        self,
    ) -> "EmrserverlessApplicationMaximumCapacityOutputReference":
        return typing.cast("EmrserverlessApplicationMaximumCapacityOutputReference", jsii.get(self, "maximumCapacity"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> "EmrserverlessApplicationNetworkConfigurationOutputReference":
        return typing.cast("EmrserverlessApplicationNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="architectureInput")
    def architecture_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architectureInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStartConfigurationInput")
    def auto_start_configuration_input(
        self,
    ) -> typing.Optional["EmrserverlessApplicationAutoStartConfiguration"]:
        return typing.cast(typing.Optional["EmrserverlessApplicationAutoStartConfiguration"], jsii.get(self, "autoStartConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStopConfigurationInput")
    def auto_stop_configuration_input(
        self,
    ) -> typing.Optional["EmrserverlessApplicationAutoStopConfiguration"]:
        return typing.cast(typing.Optional["EmrserverlessApplicationAutoStopConfiguration"], jsii.get(self, "autoStopConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialCapacityInput")
    def initial_capacity_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrserverlessApplicationInitialCapacity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrserverlessApplicationInitialCapacity"]]], jsii.get(self, "initialCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCapacityInput")
    def maximum_capacity_input(
        self,
    ) -> typing.Optional["EmrserverlessApplicationMaximumCapacity"]:
        return typing.cast(typing.Optional["EmrserverlessApplicationMaximumCapacity"], jsii.get(self, "maximumCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["EmrserverlessApplicationNetworkConfiguration"]:
        return typing.cast(typing.Optional["EmrserverlessApplicationNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseLabelInput")
    def release_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c091d149c2e37b294bf17bcb0360cdeba509f3ca21bf5ea6094ec68fac543378)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f0884b98095cddd2b5c631defbfde814606d75c64d2241885b903031b7f24f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a337219ff3d99816a4f46dbe415b68006fc88d9b857d89fe492e027ca9caae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b8d63644d955d64314d15dbd8b0f3f80c67a5c41eb979c3f89441247a96475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7729aa5954896f7043da90a0d8a2b20d0fb0a4463bf5e83bc9dc7ce63aac1b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b823ce3293e6501faaff4bf840b75a7bb872de66dcc97a9fa856f0df549ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec41a5cf06b218848affc756a91a0ccc075bde102d290cf71b4976fd4b470b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationAutoStartConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class EmrserverlessApplicationAutoStartConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#enabled EmrserverlessApplication#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef4079df202285c5d2de5c7a35ce139373f4d51875c32880244e3de339db69bd)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#enabled EmrserverlessApplication#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationAutoStartConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrserverlessApplicationAutoStartConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationAutoStartConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4c30a346ffe54a5fed4b5b2bce2f2ee2aaed3176cc182077bf4c9255709c69d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b111626a566bca1e8a718d1eca92e4ec66800f742ec10e6b5f27cf06db1d56eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrserverlessApplicationAutoStartConfiguration]:
        return typing.cast(typing.Optional[EmrserverlessApplicationAutoStartConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrserverlessApplicationAutoStartConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e48e15372de178b1ce4990d49e1f752b88eb0f40d5019b78e4fa6e144a4fbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationAutoStopConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "idle_timeout_minutes": "idleTimeoutMinutes"},
)
class EmrserverlessApplicationAutoStopConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        idle_timeout_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#enabled EmrserverlessApplication#enabled}.
        :param idle_timeout_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#idle_timeout_minutes EmrserverlessApplication#idle_timeout_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05cc5aa32f0f929dbf0b2cd2cd19ce38e4dba63cdb54d543cd779e00b5de3beb)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument idle_timeout_minutes", value=idle_timeout_minutes, expected_type=type_hints["idle_timeout_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if idle_timeout_minutes is not None:
            self._values["idle_timeout_minutes"] = idle_timeout_minutes

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#enabled EmrserverlessApplication#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def idle_timeout_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#idle_timeout_minutes EmrserverlessApplication#idle_timeout_minutes}.'''
        result = self._values.get("idle_timeout_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationAutoStopConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrserverlessApplicationAutoStopConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationAutoStopConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4107b47e37e59f64dd3b7c3ab22c62edc7e618555ebb653c8db76f9172a7b3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetIdleTimeoutMinutes")
    def reset_idle_timeout_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutMinutesInput")
    def idle_timeout_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ca1f1080ab7134af485c364843575f6dd08e0113a18aeb68fd9528aeb9c792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutMinutes"))

    @idle_timeout_minutes.setter
    def idle_timeout_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d65d376b9c4390568454293857cd61e2aec9041f0c86ee2725925778586123b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrserverlessApplicationAutoStopConfiguration]:
        return typing.cast(typing.Optional[EmrserverlessApplicationAutoStopConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrserverlessApplicationAutoStopConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb158face632b530dc1ea7a1a62683ad6aa29069863a9f3ec8dd8f8e36c3285c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "release_label": "releaseLabel",
        "type": "type",
        "architecture": "architecture",
        "auto_start_configuration": "autoStartConfiguration",
        "auto_stop_configuration": "autoStopConfiguration",
        "id": "id",
        "initial_capacity": "initialCapacity",
        "maximum_capacity": "maximumCapacity",
        "network_configuration": "networkConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class EmrserverlessApplicationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        release_label: builtins.str,
        type: builtins.str,
        architecture: typing.Optional[builtins.str] = None,
        auto_start_configuration: typing.Optional[typing.Union[EmrserverlessApplicationAutoStartConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_stop_configuration: typing.Optional[typing.Union[EmrserverlessApplicationAutoStopConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initial_capacity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrserverlessApplicationInitialCapacity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        maximum_capacity: typing.Optional[typing.Union["EmrserverlessApplicationMaximumCapacity", typing.Dict[builtins.str, typing.Any]]] = None,
        network_configuration: typing.Optional[typing.Union["EmrserverlessApplicationNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#name EmrserverlessApplication#name}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#release_label EmrserverlessApplication#release_label}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#type EmrserverlessApplication#type}.
        :param architecture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#architecture EmrserverlessApplication#architecture}.
        :param auto_start_configuration: auto_start_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#auto_start_configuration EmrserverlessApplication#auto_start_configuration}
        :param auto_stop_configuration: auto_stop_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#auto_stop_configuration EmrserverlessApplication#auto_stop_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#id EmrserverlessApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_capacity: initial_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity EmrserverlessApplication#initial_capacity}
        :param maximum_capacity: maximum_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#maximum_capacity EmrserverlessApplication#maximum_capacity}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#network_configuration EmrserverlessApplication#network_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#tags EmrserverlessApplication#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#tags_all EmrserverlessApplication#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_start_configuration, dict):
            auto_start_configuration = EmrserverlessApplicationAutoStartConfiguration(**auto_start_configuration)
        if isinstance(auto_stop_configuration, dict):
            auto_stop_configuration = EmrserverlessApplicationAutoStopConfiguration(**auto_stop_configuration)
        if isinstance(maximum_capacity, dict):
            maximum_capacity = EmrserverlessApplicationMaximumCapacity(**maximum_capacity)
        if isinstance(network_configuration, dict):
            network_configuration = EmrserverlessApplicationNetworkConfiguration(**network_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faec98dbf96aa0b11ed9a301274973e54ab65f85d9882bf46e758aa888ed483e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument auto_start_configuration", value=auto_start_configuration, expected_type=type_hints["auto_start_configuration"])
            check_type(argname="argument auto_stop_configuration", value=auto_stop_configuration, expected_type=type_hints["auto_stop_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_capacity", value=initial_capacity, expected_type=type_hints["initial_capacity"])
            check_type(argname="argument maximum_capacity", value=maximum_capacity, expected_type=type_hints["maximum_capacity"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "release_label": release_label,
            "type": type,
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
        if architecture is not None:
            self._values["architecture"] = architecture
        if auto_start_configuration is not None:
            self._values["auto_start_configuration"] = auto_start_configuration
        if auto_stop_configuration is not None:
            self._values["auto_stop_configuration"] = auto_stop_configuration
        if id is not None:
            self._values["id"] = id
        if initial_capacity is not None:
            self._values["initial_capacity"] = initial_capacity
        if maximum_capacity is not None:
            self._values["maximum_capacity"] = maximum_capacity
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#name EmrserverlessApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def release_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#release_label EmrserverlessApplication#release_label}.'''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#type EmrserverlessApplication#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#architecture EmrserverlessApplication#architecture}.'''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_start_configuration(
        self,
    ) -> typing.Optional[EmrserverlessApplicationAutoStartConfiguration]:
        '''auto_start_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#auto_start_configuration EmrserverlessApplication#auto_start_configuration}
        '''
        result = self._values.get("auto_start_configuration")
        return typing.cast(typing.Optional[EmrserverlessApplicationAutoStartConfiguration], result)

    @builtins.property
    def auto_stop_configuration(
        self,
    ) -> typing.Optional[EmrserverlessApplicationAutoStopConfiguration]:
        '''auto_stop_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#auto_stop_configuration EmrserverlessApplication#auto_stop_configuration}
        '''
        result = self._values.get("auto_stop_configuration")
        return typing.cast(typing.Optional[EmrserverlessApplicationAutoStopConfiguration], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#id EmrserverlessApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_capacity(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrserverlessApplicationInitialCapacity"]]]:
        '''initial_capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity EmrserverlessApplication#initial_capacity}
        '''
        result = self._values.get("initial_capacity")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrserverlessApplicationInitialCapacity"]]], result)

    @builtins.property
    def maximum_capacity(
        self,
    ) -> typing.Optional["EmrserverlessApplicationMaximumCapacity"]:
        '''maximum_capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#maximum_capacity EmrserverlessApplication#maximum_capacity}
        '''
        result = self._values.get("maximum_capacity")
        return typing.cast(typing.Optional["EmrserverlessApplicationMaximumCapacity"], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["EmrserverlessApplicationNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#network_configuration EmrserverlessApplication#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["EmrserverlessApplicationNetworkConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#tags EmrserverlessApplication#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#tags_all EmrserverlessApplication#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "initial_capacity_type": "initialCapacityType",
        "initial_capacity_config": "initialCapacityConfig",
    },
)
class EmrserverlessApplicationInitialCapacity:
    def __init__(
        self,
        *,
        initial_capacity_type: builtins.str,
        initial_capacity_config: typing.Optional[typing.Union["EmrserverlessApplicationInitialCapacityInitialCapacityConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param initial_capacity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity_type EmrserverlessApplication#initial_capacity_type}.
        :param initial_capacity_config: initial_capacity_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity_config EmrserverlessApplication#initial_capacity_config}
        '''
        if isinstance(initial_capacity_config, dict):
            initial_capacity_config = EmrserverlessApplicationInitialCapacityInitialCapacityConfig(**initial_capacity_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f8db193e7b51da0e6086531b2782947fa316294d8c7394b6014ac40a520e13)
            check_type(argname="argument initial_capacity_type", value=initial_capacity_type, expected_type=type_hints["initial_capacity_type"])
            check_type(argname="argument initial_capacity_config", value=initial_capacity_config, expected_type=type_hints["initial_capacity_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "initial_capacity_type": initial_capacity_type,
        }
        if initial_capacity_config is not None:
            self._values["initial_capacity_config"] = initial_capacity_config

    @builtins.property
    def initial_capacity_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity_type EmrserverlessApplication#initial_capacity_type}.'''
        result = self._values.get("initial_capacity_type")
        assert result is not None, "Required property 'initial_capacity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_capacity_config(
        self,
    ) -> typing.Optional["EmrserverlessApplicationInitialCapacityInitialCapacityConfig"]:
        '''initial_capacity_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#initial_capacity_config EmrserverlessApplication#initial_capacity_config}
        '''
        result = self._values.get("initial_capacity_config")
        return typing.cast(typing.Optional["EmrserverlessApplicationInitialCapacityInitialCapacityConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationInitialCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacityInitialCapacityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "worker_count": "workerCount",
        "worker_configuration": "workerConfiguration",
    },
)
class EmrserverlessApplicationInitialCapacityInitialCapacityConfig:
    def __init__(
        self,
        *,
        worker_count: jsii.Number,
        worker_configuration: typing.Optional[typing.Union["EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#worker_count EmrserverlessApplication#worker_count}.
        :param worker_configuration: worker_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#worker_configuration EmrserverlessApplication#worker_configuration}
        '''
        if isinstance(worker_configuration, dict):
            worker_configuration = EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration(**worker_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1922b5b905b8de83afe72e11c9cc8fa71c3f12ae6c2440dbe60d93af5dcd2e55)
            check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
            check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "worker_count": worker_count,
        }
        if worker_configuration is not None:
            self._values["worker_configuration"] = worker_configuration

    @builtins.property
    def worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#worker_count EmrserverlessApplication#worker_count}.'''
        result = self._values.get("worker_count")
        assert result is not None, "Required property 'worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def worker_configuration(
        self,
    ) -> typing.Optional["EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration"]:
        '''worker_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#worker_configuration EmrserverlessApplication#worker_configuration}
        '''
        result = self._values.get("worker_configuration")
        return typing.cast(typing.Optional["EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationInitialCapacityInitialCapacityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrserverlessApplicationInitialCapacityInitialCapacityConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacityInitialCapacityConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3e6bf76eb899f872dc11db4887f6cef9be43a80714f89c632bf9e3a3151f019)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWorkerConfiguration")
    def put_worker_configuration(
        self,
        *,
        cpu: builtins.str,
        memory: builtins.str,
        disk: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#cpu EmrserverlessApplication#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#memory EmrserverlessApplication#memory}.
        :param disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#disk EmrserverlessApplication#disk}.
        '''
        value = EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration(
            cpu=cpu, memory=memory, disk=disk
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerConfiguration", [value]))

    @jsii.member(jsii_name="resetWorkerConfiguration")
    def reset_worker_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="workerConfiguration")
    def worker_configuration(
        self,
    ) -> "EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationOutputReference":
        return typing.cast("EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationOutputReference", jsii.get(self, "workerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="workerConfigurationInput")
    def worker_configuration_input(
        self,
    ) -> typing.Optional["EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration"]:
        return typing.cast(typing.Optional["EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration"], jsii.get(self, "workerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="workerCountInput")
    def worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7dea82336dddcf93916e712053501a363ffd81b51159b10dc07748d0d407be2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfig]:
        return typing.cast(typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__858de2d2f795a155d6078aa7d7d37106655701dc27af42241a5e2a51536125a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory": "memory", "disk": "disk"},
)
class EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration:
    def __init__(
        self,
        *,
        cpu: builtins.str,
        memory: builtins.str,
        disk: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#cpu EmrserverlessApplication#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#memory EmrserverlessApplication#memory}.
        :param disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#disk EmrserverlessApplication#disk}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0ab57002e60cf5dcc90e2ea2c8358b34d98805a7d47b0159374f51dae69ba93)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cpu": cpu,
            "memory": memory,
        }
        if disk is not None:
            self._values["disk"] = disk

    @builtins.property
    def cpu(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#cpu EmrserverlessApplication#cpu}.'''
        result = self._values.get("cpu")
        assert result is not None, "Required property 'cpu' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def memory(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#memory EmrserverlessApplication#memory}.'''
        result = self._values.get("memory")
        assert result is not None, "Required property 'memory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#disk EmrserverlessApplication#disk}.'''
        result = self._values.get("disk")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af6058c149168bcdf0d0c94b5cbf4bc256023081f8b8aa7b433cbeae351bef52)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisk")
    def reset_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisk", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b62a0fdb9124553cef6f446ded3e657e0534f88079c433280f11aca84d5c6f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disk"))

    @disk.setter
    def disk(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c315bb9467a7bb146cd141c5851563d9d3cdd45ef66c64570c2d699daa171f16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disk", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2265127192bd047aac8d5559e4c851bb9c06c904b73dbc9cc1575d13b71076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration]:
        return typing.cast(typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b158dd71a9cd2047e1ed2a13177ae393cd81ebf42b446f9f6aaeecf021b3999b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrserverlessApplicationInitialCapacityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9f61b2dbc3b765d447da05dadc72488d070db5ed704c4c5c1f7c41e27ff0dd7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrserverlessApplicationInitialCapacityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c15f6c391ab60a9f4ce9e5b10347074c4c0ae4a7073ed9f58ad953eabf52a300)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrserverlessApplicationInitialCapacityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a620e07d4226495e816c81e9b8f5e351117120be9c6e71b8a0991f023de6f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ea00c662443c0622374a6b7a43ba84deb8662d10f1510197b3407d7effa0131)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22707feadbec696b8ac066cec9e6ebe1af2cee09ae553d0c8bb55fcb2fa77c5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrserverlessApplicationInitialCapacity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrserverlessApplicationInitialCapacity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrserverlessApplicationInitialCapacity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7bb790648d6f77cf7fe5ec03acc37a72e1e95bc773c8a45a994534365cc47f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrserverlessApplicationInitialCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationInitialCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7448be106b96428e71b2ddfa5d21157b98cdeb95edd3df768bbd785baab7e950)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putInitialCapacityConfig")
    def put_initial_capacity_config(
        self,
        *,
        worker_count: jsii.Number,
        worker_configuration: typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#worker_count EmrserverlessApplication#worker_count}.
        :param worker_configuration: worker_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#worker_configuration EmrserverlessApplication#worker_configuration}
        '''
        value = EmrserverlessApplicationInitialCapacityInitialCapacityConfig(
            worker_count=worker_count, worker_configuration=worker_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putInitialCapacityConfig", [value]))

    @jsii.member(jsii_name="resetInitialCapacityConfig")
    def reset_initial_capacity_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialCapacityConfig", []))

    @builtins.property
    @jsii.member(jsii_name="initialCapacityConfig")
    def initial_capacity_config(
        self,
    ) -> EmrserverlessApplicationInitialCapacityInitialCapacityConfigOutputReference:
        return typing.cast(EmrserverlessApplicationInitialCapacityInitialCapacityConfigOutputReference, jsii.get(self, "initialCapacityConfig"))

    @builtins.property
    @jsii.member(jsii_name="initialCapacityConfigInput")
    def initial_capacity_config_input(
        self,
    ) -> typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfig]:
        return typing.cast(typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfig], jsii.get(self, "initialCapacityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="initialCapacityTypeInput")
    def initial_capacity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialCapacityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="initialCapacityType")
    def initial_capacity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialCapacityType"))

    @initial_capacity_type.setter
    def initial_capacity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8384cf6da88aee490d9661f71049b223a31e832ba320c83089ac33090c4b0480)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialCapacityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacity, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacity, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacity, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55230043d3bc2437baa3b6de5e909253c2509fa3eabbd3ade3b612bd80094d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationMaximumCapacity",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory": "memory", "disk": "disk"},
)
class EmrserverlessApplicationMaximumCapacity:
    def __init__(
        self,
        *,
        cpu: builtins.str,
        memory: builtins.str,
        disk: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#cpu EmrserverlessApplication#cpu}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#memory EmrserverlessApplication#memory}.
        :param disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#disk EmrserverlessApplication#disk}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4eb1e73975a21e9990c9d2cc48b3809dff3fac251820e4afdfd7fd5e7214c7e)
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cpu": cpu,
            "memory": memory,
        }
        if disk is not None:
            self._values["disk"] = disk

    @builtins.property
    def cpu(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#cpu EmrserverlessApplication#cpu}.'''
        result = self._values.get("cpu")
        assert result is not None, "Required property 'cpu' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def memory(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#memory EmrserverlessApplication#memory}.'''
        result = self._values.get("memory")
        assert result is not None, "Required property 'memory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#disk EmrserverlessApplication#disk}.'''
        result = self._values.get("disk")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationMaximumCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrserverlessApplicationMaximumCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationMaximumCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97633b1bc014fd30862cde3d9e0ecfa75c7b2b1f9aea4e5b2a391d664cdbca13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisk")
    def reset_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisk", []))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpu"))

    @cpu.setter
    def cpu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e267fd4e0b968b34b3cc3350410cc29aeae5eaa4dab746c06a7fb62ab93025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpu", value)

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disk"))

    @disk.setter
    def disk(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6760950b70f259cc777a0933f9a2da94e584391a596b6d5d00836810067ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disk", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caa76b1fdcefd61d538869270516df960b76d1bbed704dbc59938269d4f0c2f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrserverlessApplicationMaximumCapacity]:
        return typing.cast(typing.Optional[EmrserverlessApplicationMaximumCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrserverlessApplicationMaximumCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25d92d7ff712af3aa88fda07773c27b72af5e0d8efc9b04df7cf0782af5ed5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class EmrserverlessApplicationNetworkConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#security_group_ids EmrserverlessApplication#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#subnet_ids EmrserverlessApplication#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e3a1d1403a62f90c2e1558e5b8f1d93c7e3134d11a3478c6fc0a9860665b0fb)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#security_group_ids EmrserverlessApplication#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emrserverless_application#subnet_ids EmrserverlessApplication#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrserverlessApplicationNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrserverlessApplicationNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrserverlessApplication.EmrserverlessApplicationNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d05ef19aca40b79e33f2776591c11d18e2ab5e5ab19b78a61555ceb5b4dd855)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6012fd08bf1c254221fbfbc655e0cd2d6eee9c95f8fce7e80c2d2f6a6565210e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__756b3dc73403f2efa082a3d7c5d7029345522aefe9d8b9cc404e5f6ebf6005e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrserverlessApplicationNetworkConfiguration]:
        return typing.cast(typing.Optional[EmrserverlessApplicationNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrserverlessApplicationNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5204c67c6b132c064b3ad76dd530af702770b7bb6d586e6ad19739df10cd8e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EmrserverlessApplication",
    "EmrserverlessApplicationAutoStartConfiguration",
    "EmrserverlessApplicationAutoStartConfigurationOutputReference",
    "EmrserverlessApplicationAutoStopConfiguration",
    "EmrserverlessApplicationAutoStopConfigurationOutputReference",
    "EmrserverlessApplicationConfig",
    "EmrserverlessApplicationInitialCapacity",
    "EmrserverlessApplicationInitialCapacityInitialCapacityConfig",
    "EmrserverlessApplicationInitialCapacityInitialCapacityConfigOutputReference",
    "EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration",
    "EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationOutputReference",
    "EmrserverlessApplicationInitialCapacityList",
    "EmrserverlessApplicationInitialCapacityOutputReference",
    "EmrserverlessApplicationMaximumCapacity",
    "EmrserverlessApplicationMaximumCapacityOutputReference",
    "EmrserverlessApplicationNetworkConfiguration",
    "EmrserverlessApplicationNetworkConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__91467d39e834de1657d4547c2c997bbc649e9d06781d23bce02cc15d7454a237(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    release_label: builtins.str,
    type: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
    auto_start_configuration: typing.Optional[typing.Union[EmrserverlessApplicationAutoStartConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_stop_configuration: typing.Optional[typing.Union[EmrserverlessApplicationAutoStopConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    initial_capacity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrserverlessApplicationInitialCapacity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    maximum_capacity: typing.Optional[typing.Union[EmrserverlessApplicationMaximumCapacity, typing.Dict[builtins.str, typing.Any]]] = None,
    network_configuration: typing.Optional[typing.Union[EmrserverlessApplicationNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__c2e168307ad4c3b288a29d5a46bf47dfbf9635510eafcd225d4d864c0d51e8f9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrserverlessApplicationInitialCapacity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c091d149c2e37b294bf17bcb0360cdeba509f3ca21bf5ea6094ec68fac543378(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0884b98095cddd2b5c631defbfde814606d75c64d2241885b903031b7f24f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a337219ff3d99816a4f46dbe415b68006fc88d9b857d89fe492e027ca9caae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b8d63644d955d64314d15dbd8b0f3f80c67a5c41eb979c3f89441247a96475(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7729aa5954896f7043da90a0d8a2b20d0fb0a4463bf5e83bc9dc7ce63aac1b5a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b823ce3293e6501faaff4bf840b75a7bb872de66dcc97a9fa856f0df549ef4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec41a5cf06b218848affc756a91a0ccc075bde102d290cf71b4976fd4b470b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef4079df202285c5d2de5c7a35ce139373f4d51875c32880244e3de339db69bd(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4c30a346ffe54a5fed4b5b2bce2f2ee2aaed3176cc182077bf4c9255709c69d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b111626a566bca1e8a718d1eca92e4ec66800f742ec10e6b5f27cf06db1d56eb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e48e15372de178b1ce4990d49e1f752b88eb0f40d5019b78e4fa6e144a4fbb(
    value: typing.Optional[EmrserverlessApplicationAutoStartConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05cc5aa32f0f929dbf0b2cd2cd19ce38e4dba63cdb54d543cd779e00b5de3beb(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    idle_timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4107b47e37e59f64dd3b7c3ab22c62edc7e618555ebb653c8db76f9172a7b3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ca1f1080ab7134af485c364843575f6dd08e0113a18aeb68fd9528aeb9c792(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d65d376b9c4390568454293857cd61e2aec9041f0c86ee2725925778586123b4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb158face632b530dc1ea7a1a62683ad6aa29069863a9f3ec8dd8f8e36c3285c(
    value: typing.Optional[EmrserverlessApplicationAutoStopConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faec98dbf96aa0b11ed9a301274973e54ab65f85d9882bf46e758aa888ed483e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    release_label: builtins.str,
    type: builtins.str,
    architecture: typing.Optional[builtins.str] = None,
    auto_start_configuration: typing.Optional[typing.Union[EmrserverlessApplicationAutoStartConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_stop_configuration: typing.Optional[typing.Union[EmrserverlessApplicationAutoStopConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    initial_capacity: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrserverlessApplicationInitialCapacity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    maximum_capacity: typing.Optional[typing.Union[EmrserverlessApplicationMaximumCapacity, typing.Dict[builtins.str, typing.Any]]] = None,
    network_configuration: typing.Optional[typing.Union[EmrserverlessApplicationNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f8db193e7b51da0e6086531b2782947fa316294d8c7394b6014ac40a520e13(
    *,
    initial_capacity_type: builtins.str,
    initial_capacity_config: typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacityInitialCapacityConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1922b5b905b8de83afe72e11c9cc8fa71c3f12ae6c2440dbe60d93af5dcd2e55(
    *,
    worker_count: jsii.Number,
    worker_configuration: typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e6bf76eb899f872dc11db4887f6cef9be43a80714f89c632bf9e3a3151f019(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7dea82336dddcf93916e712053501a363ffd81b51159b10dc07748d0d407be2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858de2d2f795a155d6078aa7d7d37106655701dc27af42241a5e2a51536125a3(
    value: typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ab57002e60cf5dcc90e2ea2c8358b34d98805a7d47b0159374f51dae69ba93(
    *,
    cpu: builtins.str,
    memory: builtins.str,
    disk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af6058c149168bcdf0d0c94b5cbf4bc256023081f8b8aa7b433cbeae351bef52(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b62a0fdb9124553cef6f446ded3e657e0534f88079c433280f11aca84d5c6f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c315bb9467a7bb146cd141c5851563d9d3cdd45ef66c64570c2d699daa171f16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2265127192bd047aac8d5559e4c851bb9c06c904b73dbc9cc1575d13b71076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b158dd71a9cd2047e1ed2a13177ae393cd81ebf42b446f9f6aaeecf021b3999b(
    value: typing.Optional[EmrserverlessApplicationInitialCapacityInitialCapacityConfigWorkerConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f61b2dbc3b765d447da05dadc72488d070db5ed704c4c5c1f7c41e27ff0dd7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c15f6c391ab60a9f4ce9e5b10347074c4c0ae4a7073ed9f58ad953eabf52a300(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a620e07d4226495e816c81e9b8f5e351117120be9c6e71b8a0991f023de6f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ea00c662443c0622374a6b7a43ba84deb8662d10f1510197b3407d7effa0131(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22707feadbec696b8ac066cec9e6ebe1af2cee09ae553d0c8bb55fcb2fa77c5a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7bb790648d6f77cf7fe5ec03acc37a72e1e95bc773c8a45a994534365cc47f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrserverlessApplicationInitialCapacity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7448be106b96428e71b2ddfa5d21157b98cdeb95edd3df768bbd785baab7e950(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8384cf6da88aee490d9661f71049b223a31e832ba320c83089ac33090c4b0480(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55230043d3bc2437baa3b6de5e909253c2509fa3eabbd3ade3b612bd80094d3a(
    value: typing.Optional[typing.Union[EmrserverlessApplicationInitialCapacity, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4eb1e73975a21e9990c9d2cc48b3809dff3fac251820e4afdfd7fd5e7214c7e(
    *,
    cpu: builtins.str,
    memory: builtins.str,
    disk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97633b1bc014fd30862cde3d9e0ecfa75c7b2b1f9aea4e5b2a391d664cdbca13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e267fd4e0b968b34b3cc3350410cc29aeae5eaa4dab746c06a7fb62ab93025(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6760950b70f259cc777a0933f9a2da94e584391a596b6d5d00836810067ebd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa76b1fdcefd61d538869270516df960b76d1bbed704dbc59938269d4f0c2f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25d92d7ff712af3aa88fda07773c27b72af5e0d8efc9b04df7cf0782af5ed5d(
    value: typing.Optional[EmrserverlessApplicationMaximumCapacity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e3a1d1403a62f90c2e1558e5b8f1d93c7e3134d11a3478c6fc0a9860665b0fb(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d05ef19aca40b79e33f2776591c11d18e2ab5e5ab19b78a61555ceb5b4dd855(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6012fd08bf1c254221fbfbc655e0cd2d6eee9c95f8fce7e80c2d2f6a6565210e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756b3dc73403f2efa082a3d7c5d7029345522aefe9d8b9cc404e5f6ebf6005e2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5204c67c6b132c064b3ad76dd530af702770b7bb6d586e6ad19739df10cd8e77(
    value: typing.Optional[EmrserverlessApplicationNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass
