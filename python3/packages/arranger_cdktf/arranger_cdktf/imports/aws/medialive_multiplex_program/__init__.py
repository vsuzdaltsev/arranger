'''
# `aws_medialive_multiplex_program`

Refer to the Terraform Registory for docs: [`aws_medialive_multiplex_program`](https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program).
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


class MedialiveMultiplexProgram(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgram",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program aws_medialive_multiplex_program}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        multiplex_id: builtins.str,
        program_name: builtins.str,
        multiplex_program_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program aws_medialive_multiplex_program} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param multiplex_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_id MedialiveMultiplexProgram#multiplex_id}.
        :param program_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_name MedialiveMultiplexProgram#program_name}.
        :param multiplex_program_settings: multiplex_program_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_program_settings MedialiveMultiplexProgram#multiplex_program_settings}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6acd10e5fd161a619488394a385e06257fcc4489beb29bd93f380bea9a7f9ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = MedialiveMultiplexProgramConfig(
            multiplex_id=multiplex_id,
            program_name=program_name,
            multiplex_program_settings=multiplex_program_settings,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putMultiplexProgramSettings")
    def put_multiplex_program_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9140234b755d95c66ae77606c5f199c06876e079e774a96b891d58bd14823846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMultiplexProgramSettings", [value]))

    @jsii.member(jsii_name="resetMultiplexProgramSettings")
    def reset_multiplex_program_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiplexProgramSettings", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="multiplexProgramSettings")
    def multiplex_program_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsList":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsList", jsii.get(self, "multiplexProgramSettings"))

    @builtins.property
    @jsii.member(jsii_name="multiplexIdInput")
    def multiplex_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "multiplexIdInput"))

    @builtins.property
    @jsii.member(jsii_name="multiplexProgramSettingsInput")
    def multiplex_program_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettings"]]], jsii.get(self, "multiplexProgramSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="programNameInput")
    def program_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "programNameInput"))

    @builtins.property
    @jsii.member(jsii_name="multiplexId")
    def multiplex_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multiplexId"))

    @multiplex_id.setter
    def multiplex_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043736b65f76931a99f796b8774e1db890440404e93224dfd708582327ea378d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiplexId", value)

    @builtins.property
    @jsii.member(jsii_name="programName")
    def program_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "programName"))

    @program_name.setter
    def program_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a620d442845849d7c2be0e4460cdc36d85d11b6adc864ba65dd1ae134ce198fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "programName", value)


@jsii.data_type(
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "multiplex_id": "multiplexId",
        "program_name": "programName",
        "multiplex_program_settings": "multiplexProgramSettings",
    },
)
class MedialiveMultiplexProgramConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        multiplex_id: builtins.str,
        program_name: builtins.str,
        multiplex_program_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param multiplex_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_id MedialiveMultiplexProgram#multiplex_id}.
        :param program_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_name MedialiveMultiplexProgram#program_name}.
        :param multiplex_program_settings: multiplex_program_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_program_settings MedialiveMultiplexProgram#multiplex_program_settings}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58394c7a5ae9e38409847ffe0c2b0402a41b982f71b0cd17bdd4c4dff05cd9f3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument multiplex_id", value=multiplex_id, expected_type=type_hints["multiplex_id"])
            check_type(argname="argument program_name", value=program_name, expected_type=type_hints["program_name"])
            check_type(argname="argument multiplex_program_settings", value=multiplex_program_settings, expected_type=type_hints["multiplex_program_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "multiplex_id": multiplex_id,
            "program_name": program_name,
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
        if multiplex_program_settings is not None:
            self._values["multiplex_program_settings"] = multiplex_program_settings

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
    def multiplex_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_id MedialiveMultiplexProgram#multiplex_id}.'''
        result = self._values.get("multiplex_id")
        assert result is not None, "Required property 'multiplex_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def program_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_name MedialiveMultiplexProgram#program_name}.'''
        result = self._values.get("program_name")
        assert result is not None, "Required property 'program_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multiplex_program_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettings"]]]:
        '''multiplex_program_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_program_settings MedialiveMultiplexProgram#multiplex_program_settings}
        '''
        result = self._values.get("multiplex_program_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettings"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettings",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_channel_pipeline": "preferredChannelPipeline",
        "program_number": "programNumber",
        "service_descriptor": "serviceDescriptor",
        "video_settings": "videoSettings",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettings:
    def __init__(
        self,
        *,
        preferred_channel_pipeline: builtins.str,
        program_number: jsii.Number,
        service_descriptor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor", typing.Dict[builtins.str, typing.Any]]]]] = None,
        video_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param preferred_channel_pipeline: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#preferred_channel_pipeline MedialiveMultiplexProgram#preferred_channel_pipeline}.
        :param program_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_number MedialiveMultiplexProgram#program_number}.
        :param service_descriptor: service_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_descriptor MedialiveMultiplexProgram#service_descriptor}
        :param video_settings: video_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#video_settings MedialiveMultiplexProgram#video_settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d7bf8d8d1995fefca30f7a6c2bba774e36fcea58317b5494aedac556f3c8cc)
            check_type(argname="argument preferred_channel_pipeline", value=preferred_channel_pipeline, expected_type=type_hints["preferred_channel_pipeline"])
            check_type(argname="argument program_number", value=program_number, expected_type=type_hints["program_number"])
            check_type(argname="argument service_descriptor", value=service_descriptor, expected_type=type_hints["service_descriptor"])
            check_type(argname="argument video_settings", value=video_settings, expected_type=type_hints["video_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "preferred_channel_pipeline": preferred_channel_pipeline,
            "program_number": program_number,
        }
        if service_descriptor is not None:
            self._values["service_descriptor"] = service_descriptor
        if video_settings is not None:
            self._values["video_settings"] = video_settings

    @builtins.property
    def preferred_channel_pipeline(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#preferred_channel_pipeline MedialiveMultiplexProgram#preferred_channel_pipeline}.'''
        result = self._values.get("preferred_channel_pipeline")
        assert result is not None, "Required property 'preferred_channel_pipeline' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def program_number(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_number MedialiveMultiplexProgram#program_number}.'''
        result = self._values.get("program_number")
        assert result is not None, "Required property 'program_number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def service_descriptor(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"]]]:
        '''service_descriptor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_descriptor MedialiveMultiplexProgram#service_descriptor}
        '''
        result = self._values.get("service_descriptor")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"]]], result)

    @builtins.property
    def video_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"]]]:
        '''video_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#video_settings MedialiveMultiplexProgram#video_settings}
        '''
        result = self._values.get("video_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7595707fb86ecddca412656caff8ddaf06d55067a1bd4ff3032ed3f1e8858ed5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0c3f8194ac0d1c8bf551151d8705e5b65246e3a6dcbf9e686f1a6f9f88e21e8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0420a3ddd75d4410e75d298d22f884bc9fb8a12db6b2cd539885be44a3b2b2ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81b4b999e79c4b7f617992383b10be890e6db366ab49e6e47f28262d84c18af4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03cc76f0f3d0e5f970b34c6c92f5bc55897e0ee056dbd806501ae8af8a747427)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b84e2561b6be6a8d6f35660e71c76961d7e0fd7e2d053671c9e067040120e03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ce1b62cd9ee7b869af5d9bec7aec558a4d73f7ff91053257d6d97b71c53e567)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putServiceDescriptor")
    def put_service_descriptor(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081d1a0dd42af576c7358d2d8480028010f8e037351ec250f1e15046935bb93c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServiceDescriptor", [value]))

    @jsii.member(jsii_name="putVideoSettings")
    def put_video_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__697b87bff3635af0052dced5af5abce61d50d865c78779d168bc9d08e0fcf40a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVideoSettings", [value]))

    @jsii.member(jsii_name="resetServiceDescriptor")
    def reset_service_descriptor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceDescriptor", []))

    @jsii.member(jsii_name="resetVideoSettings")
    def reset_video_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoSettings", []))

    @builtins.property
    @jsii.member(jsii_name="serviceDescriptor")
    def service_descriptor(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorList":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorList", jsii.get(self, "serviceDescriptor"))

    @builtins.property
    @jsii.member(jsii_name="videoSettings")
    def video_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsList":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsList", jsii.get(self, "videoSettings"))

    @builtins.property
    @jsii.member(jsii_name="preferredChannelPipelineInput")
    def preferred_channel_pipeline_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredChannelPipelineInput"))

    @builtins.property
    @jsii.member(jsii_name="programNumberInput")
    def program_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "programNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDescriptorInput")
    def service_descriptor_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"]]], jsii.get(self, "serviceDescriptorInput"))

    @builtins.property
    @jsii.member(jsii_name="videoSettingsInput")
    def video_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"]]], jsii.get(self, "videoSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredChannelPipeline")
    def preferred_channel_pipeline(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredChannelPipeline"))

    @preferred_channel_pipeline.setter
    def preferred_channel_pipeline(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110b2873e72b5d97a7fa3e9c7723ea848779dbe01248f17311baa98cc46dbc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredChannelPipeline", value)

    @builtins.property
    @jsii.member(jsii_name="programNumber")
    def program_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "programNumber"))

    @program_number.setter
    def program_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49b0a5d96b15c5a2f40b0c3131a19dfa3afd9f52c6a5d6bd02a1a0d88ad30b7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "programNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4140054a20bcc0bb18a41e0bf6c15c6f69521af9a0f5073aabab8a0b4bb2b2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor",
    jsii_struct_bases=[],
    name_mapping={"provider_name": "providerName", "service_name": "serviceName"},
)
class MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor:
    def __init__(
        self,
        *,
        provider_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#provider_name MedialiveMultiplexProgram#provider_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_name MedialiveMultiplexProgram#service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b56a0a97df7cc6739251e8d048564af72287ccc1e60a7db245c7e6a899e17a7b)
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provider_name": provider_name,
            "service_name": service_name,
        }

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#provider_name MedialiveMultiplexProgram#provider_name}.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_name MedialiveMultiplexProgram#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd6922d3ebab05f70ae9955cd359ae917b501f3b35973b2900026bd6ee7b2c09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8877967900d36fcdd4b71f19f9093783bb6bdaf7ccfddc78958ad0fb6c679b3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a6fb3f54692c48874f38eaaf738d903d7df62fb529a2b01fa09cfc86990355)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73727f46998b6e99bda007af7d6973573fce58d83af8bdb0e051d11fa3603791)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48b4ecca85398d5b679a5dac013e0977b9d836ce80a37f17e16757e854159cd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c5bdda9330faa4fb4f27948168b40391df3dc27355603589a70c797ff97f7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95b4386fb17947752fb6c1ac391220ad4523ce9790a27e8c791ffabd094557f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="providerNameInput")
    def provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18580adc8b5c47b35784fe59b71d78b3de1fa3f092a485a02d7f241ca24cdd5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3684dcc2eaaae21b7571ac4917c17d4a9a14ff57f0a62de383ec7edd2a236a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe910eb6101dde504c08fe01449a13716de0ba1c14555d5b224346fc00c1cd47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings",
    jsii_struct_bases=[],
    name_mapping={
        "constant_bitrate": "constantBitrate",
        "statemux_settings": "statemuxSettings",
        "statmux_settings": "statmuxSettings",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings:
    def __init__(
        self,
        *,
        constant_bitrate: typing.Optional[jsii.Number] = None,
        statemux_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        statmux_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param constant_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#constant_bitrate MedialiveMultiplexProgram#constant_bitrate}.
        :param statemux_settings: statemux_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statemux_settings MedialiveMultiplexProgram#statemux_settings}
        :param statmux_settings: statmux_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statmux_settings MedialiveMultiplexProgram#statmux_settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db2d61442258acc24add05308d0ac3c7025beb79006a657fa4cda203f2f9ceb)
            check_type(argname="argument constant_bitrate", value=constant_bitrate, expected_type=type_hints["constant_bitrate"])
            check_type(argname="argument statemux_settings", value=statemux_settings, expected_type=type_hints["statemux_settings"])
            check_type(argname="argument statmux_settings", value=statmux_settings, expected_type=type_hints["statmux_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if constant_bitrate is not None:
            self._values["constant_bitrate"] = constant_bitrate
        if statemux_settings is not None:
            self._values["statemux_settings"] = statemux_settings
        if statmux_settings is not None:
            self._values["statmux_settings"] = statmux_settings

    @builtins.property
    def constant_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#constant_bitrate MedialiveMultiplexProgram#constant_bitrate}.'''
        result = self._values.get("constant_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statemux_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"]]]:
        '''statemux_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statemux_settings MedialiveMultiplexProgram#statemux_settings}
        '''
        result = self._values.get("statemux_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"]]], result)

    @builtins.property
    def statmux_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"]]]:
        '''statmux_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statmux_settings MedialiveMultiplexProgram#statmux_settings}
        '''
        result = self._values.get("statmux_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed01948313748b8442d26c62a0bbbd5a06e7765d162998696ad94e6b4f5351c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__825c30bb691caa2f52ad43e501f08cae3456ea7b0f122a11b75e33875a4306c3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88b19a346b4dcde6d49068527a412e932665145e5f13febb5b04be4119970aa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffa30af7c047ae9f567c4949d55582df3bb5fe8a32f628d3d1b01b8bad9016b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b600346bde3d5b5ee3e8564397f4a837f1ffb897cd6140c0eb4ffde959c9930)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41773e8a9db23c68f38de92b7e65498c07fc2655e424ff591fe422576d3ed56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d53488887772856a77035f02b7b764b5b45d56e774c800a9a74492d8e33bb19)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStatemuxSettings")
    def put_statemux_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e14084ac6dbb365ea78a43215c7d7cc51df98f92e40c794c6bb18ba0d67e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatemuxSettings", [value]))

    @jsii.member(jsii_name="putStatmuxSettings")
    def put_statmux_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__535703e8f88154e935aec1a9f453d6d87254b63cfed05a69ef85c94bba752ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatmuxSettings", [value]))

    @jsii.member(jsii_name="resetConstantBitrate")
    def reset_constant_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConstantBitrate", []))

    @jsii.member(jsii_name="resetStatemuxSettings")
    def reset_statemux_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatemuxSettings", []))

    @jsii.member(jsii_name="resetStatmuxSettings")
    def reset_statmux_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatmuxSettings", []))

    @builtins.property
    @jsii.member(jsii_name="statemuxSettings")
    def statemux_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsList":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsList", jsii.get(self, "statemuxSettings"))

    @builtins.property
    @jsii.member(jsii_name="statmuxSettings")
    def statmux_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsList":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsList", jsii.get(self, "statmuxSettings"))

    @builtins.property
    @jsii.member(jsii_name="constantBitrateInput")
    def constant_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "constantBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="statemuxSettingsInput")
    def statemux_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"]]], jsii.get(self, "statemuxSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="statmuxSettingsInput")
    def statmux_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"]]], jsii.get(self, "statmuxSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="constantBitrate")
    def constant_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "constantBitrate"))

    @constant_bitrate.setter
    def constant_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c437507adbbb8e9eb2aaeeb656c95061dec862e99ab91a508c64d49957261b6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constantBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd5dcd99a7eb7ccc41920662c61abb9fbc8ccd77435ee2b87465910a55bf6ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_bitrate": "maximumBitrate",
        "minimum_bitrate": "minimumBitrate",
        "priority": "priority",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings:
    def __init__(
        self,
        *,
        maximum_bitrate: typing.Optional[jsii.Number] = None,
        minimum_bitrate: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.
        :param minimum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f12a9f2eb5d8991bc6742fa0f26f5ef9dfc5bbf543d0314270ea53e4817ee54)
            check_type(argname="argument maximum_bitrate", value=maximum_bitrate, expected_type=type_hints["maximum_bitrate"])
            check_type(argname="argument minimum_bitrate", value=minimum_bitrate, expected_type=type_hints["minimum_bitrate"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if maximum_bitrate is not None:
            self._values["maximum_bitrate"] = maximum_bitrate
        if minimum_bitrate is not None:
            self._values["minimum_bitrate"] = minimum_bitrate
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def maximum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.'''
        result = self._values.get("maximum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.'''
        result = self._values.get("minimum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c876b637c10223e4dc17912971aecf35dced61bddd08daa8cf4635bd8e06889)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c254cc64c74c5d22c3cc42b77acca30f4b0bd4e2cbc5377d9e3674387967eaf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e586cde9304cd1e5e77b020be25e9333a593a468d7ab4aa30fb4b7ceda1958d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__128acbc9aaa1143e29f31e2e9421b4e08f276b9962695b168ddc5368cc9091b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b3073a986ccf2fb2ec280dec8f00af0908fd4f68e33143a192085e8322a71bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0795263ccd6b7e32f32009576028929f76ef260d4e98e5ed21edf9c802a16d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c0eaaee45f5146329dcea65ff161f03d65f6960187dc9fb34a92008521a5cf5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaximumBitrate")
    def reset_maximum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBitrate", []))

    @jsii.member(jsii_name="resetMinimumBitrate")
    def reset_minimum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumBitrate", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrateInput")
    def maximum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumBitrateInput")
    def minimum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrate")
    def maximum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBitrate"))

    @maximum_bitrate.setter
    def maximum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97452ea44b0f85cb357facaacb0215fb3620509f2d7a2d0e8892d2c1a0329fcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="minimumBitrate")
    def minimum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumBitrate"))

    @minimum_bitrate.setter
    def minimum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a3d22844568b2c4f6e7ac11bf432d10182bf4a95ff6ac54e95bb2a59a04da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73843670c0a138b6ed003d6a173bb310a7b8ed3a60328918a0d7bc2ceef04866)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ff745a1ecb81ccc1884f96cfea4d30295a14f100a38576c03df4f2c33f5905b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_bitrate": "maximumBitrate",
        "minimum_bitrate": "minimumBitrate",
        "priority": "priority",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings:
    def __init__(
        self,
        *,
        maximum_bitrate: typing.Optional[jsii.Number] = None,
        minimum_bitrate: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.
        :param minimum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a0c4673960ad85990e52c5d256daf98714acb20184a1d8727e6e2da07d6c76)
            check_type(argname="argument maximum_bitrate", value=maximum_bitrate, expected_type=type_hints["maximum_bitrate"])
            check_type(argname="argument minimum_bitrate", value=minimum_bitrate, expected_type=type_hints["minimum_bitrate"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if maximum_bitrate is not None:
            self._values["maximum_bitrate"] = maximum_bitrate
        if minimum_bitrate is not None:
            self._values["minimum_bitrate"] = minimum_bitrate
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def maximum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.'''
        result = self._values.get("maximum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.'''
        result = self._values.get("minimum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f3028f7640b5f9d85ac64b2096c8f4adf9bbeb90a558e603af1f1bec80ce715)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5322c6c6ac692b282b70f625ee39a170ceb5133074c813e903d645d3ac8ca91e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429f1e773fcf4b03d51707f5c061d26bae9f1ef2e54bcaf088e9313ca8a9c672)
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
            type_hints = typing.get_type_hints(_typecheckingstub__68c4d2ad1faf95bba76c7701204b788950fd935b32e3c3a367074be5848b3a0e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05987c9101cc2929445deda67d28286b9c79f90aa6ad9e8e9285f2d69c7a6319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3961de497e4375782fe373e44ae490de3cfae41d521e6c2d0c8714010f5ba430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d64d430154d9f4d11feea4ed680c0b017672a142dcaa7c5a83b1a73c7ac7967e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaximumBitrate")
    def reset_maximum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBitrate", []))

    @jsii.member(jsii_name="resetMinimumBitrate")
    def reset_minimum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumBitrate", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrateInput")
    def maximum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumBitrateInput")
    def minimum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrate")
    def maximum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBitrate"))

    @maximum_bitrate.setter
    def maximum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1404bf6d9851d87e846eed6249a97787dfd0f5fb685396463ada18cb16c5c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="minimumBitrate")
    def minimum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumBitrate"))

    @minimum_bitrate.setter
    def minimum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69d25e8b42a3f10686e50cfbd191b70ce7871530469fb63d2f29723fb2932cd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e877f6801abdb24901125cfa46ea4240c3c7da256a22f71cdc5ef40fba11af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85b31f2fac8ddc5a7859559427d73c0666429963161f7224676bd368f98ce8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MedialiveMultiplexProgram",
    "MedialiveMultiplexProgramConfig",
    "MedialiveMultiplexProgramMultiplexProgramSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsList",
    "MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor",
    "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorList",
    "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsList",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsList",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsList",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__a6acd10e5fd161a619488394a385e06257fcc4489beb29bd93f380bea9a7f9ca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    multiplex_id: builtins.str,
    program_name: builtins.str,
    multiplex_program_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__9140234b755d95c66ae77606c5f199c06876e079e774a96b891d58bd14823846(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043736b65f76931a99f796b8774e1db890440404e93224dfd708582327ea378d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a620d442845849d7c2be0e4460cdc36d85d11b6adc864ba65dd1ae134ce198fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58394c7a5ae9e38409847ffe0c2b0402a41b982f71b0cd17bdd4c4dff05cd9f3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    multiplex_id: builtins.str,
    program_name: builtins.str,
    multiplex_program_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d7bf8d8d1995fefca30f7a6c2bba774e36fcea58317b5494aedac556f3c8cc(
    *,
    preferred_channel_pipeline: builtins.str,
    program_number: jsii.Number,
    service_descriptor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, typing.Dict[builtins.str, typing.Any]]]]] = None,
    video_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7595707fb86ecddca412656caff8ddaf06d55067a1bd4ff3032ed3f1e8858ed5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0c3f8194ac0d1c8bf551151d8705e5b65246e3a6dcbf9e686f1a6f9f88e21e8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0420a3ddd75d4410e75d298d22f884bc9fb8a12db6b2cd539885be44a3b2b2ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b4b999e79c4b7f617992383b10be890e6db366ab49e6e47f28262d84c18af4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03cc76f0f3d0e5f970b34c6c92f5bc55897e0ee056dbd806501ae8af8a747427(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b84e2561b6be6a8d6f35660e71c76961d7e0fd7e2d053671c9e067040120e03(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce1b62cd9ee7b869af5d9bec7aec558a4d73f7ff91053257d6d97b71c53e567(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081d1a0dd42af576c7358d2d8480028010f8e037351ec250f1e15046935bb93c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697b87bff3635af0052dced5af5abce61d50d865c78779d168bc9d08e0fcf40a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110b2873e72b5d97a7fa3e9c7723ea848779dbe01248f17311baa98cc46dbc34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b0a5d96b15c5a2f40b0c3131a19dfa3afd9f52c6a5d6bd02a1a0d88ad30b7b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4140054a20bcc0bb18a41e0bf6c15c6f69521af9a0f5073aabab8a0b4bb2b2e(
    value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56a0a97df7cc6739251e8d048564af72287ccc1e60a7db245c7e6a899e17a7b(
    *,
    provider_name: builtins.str,
    service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6922d3ebab05f70ae9955cd359ae917b501f3b35973b2900026bd6ee7b2c09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8877967900d36fcdd4b71f19f9093783bb6bdaf7ccfddc78958ad0fb6c679b3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a6fb3f54692c48874f38eaaf738d903d7df62fb529a2b01fa09cfc86990355(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73727f46998b6e99bda007af7d6973573fce58d83af8bdb0e051d11fa3603791(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b4ecca85398d5b679a5dac013e0977b9d836ce80a37f17e16757e854159cd4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c5bdda9330faa4fb4f27948168b40391df3dc27355603589a70c797ff97f7a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b4386fb17947752fb6c1ac391220ad4523ce9790a27e8c791ffabd094557f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18580adc8b5c47b35784fe59b71d78b3de1fa3f092a485a02d7f241ca24cdd5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3684dcc2eaaae21b7571ac4917c17d4a9a14ff57f0a62de383ec7edd2a236a19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe910eb6101dde504c08fe01449a13716de0ba1c14555d5b224346fc00c1cd47(
    value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db2d61442258acc24add05308d0ac3c7025beb79006a657fa4cda203f2f9ceb(
    *,
    constant_bitrate: typing.Optional[jsii.Number] = None,
    statemux_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    statmux_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed01948313748b8442d26c62a0bbbd5a06e7765d162998696ad94e6b4f5351c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825c30bb691caa2f52ad43e501f08cae3456ea7b0f122a11b75e33875a4306c3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88b19a346b4dcde6d49068527a412e932665145e5f13febb5b04be4119970aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa30af7c047ae9f567c4949d55582df3bb5fe8a32f628d3d1b01b8bad9016b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b600346bde3d5b5ee3e8564397f4a837f1ffb897cd6140c0eb4ffde959c9930(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41773e8a9db23c68f38de92b7e65498c07fc2655e424ff591fe422576d3ed56(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d53488887772856a77035f02b7b764b5b45d56e774c800a9a74492d8e33bb19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e14084ac6dbb365ea78a43215c7d7cc51df98f92e40c794c6bb18ba0d67e85(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__535703e8f88154e935aec1a9f453d6d87254b63cfed05a69ef85c94bba752ae8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c437507adbbb8e9eb2aaeeb656c95061dec862e99ab91a508c64d49957261b6c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd5dcd99a7eb7ccc41920662c61abb9fbc8ccd77435ee2b87465910a55bf6ea(
    value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f12a9f2eb5d8991bc6742fa0f26f5ef9dfc5bbf543d0314270ea53e4817ee54(
    *,
    maximum_bitrate: typing.Optional[jsii.Number] = None,
    minimum_bitrate: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c876b637c10223e4dc17912971aecf35dced61bddd08daa8cf4635bd8e06889(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c254cc64c74c5d22c3cc42b77acca30f4b0bd4e2cbc5377d9e3674387967eaf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e586cde9304cd1e5e77b020be25e9333a593a468d7ab4aa30fb4b7ceda1958d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128acbc9aaa1143e29f31e2e9421b4e08f276b9962695b168ddc5368cc9091b9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3073a986ccf2fb2ec280dec8f00af0908fd4f68e33143a192085e8322a71bb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad0795263ccd6b7e32f32009576028929f76ef260d4e98e5ed21edf9c802a16d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0eaaee45f5146329dcea65ff161f03d65f6960187dc9fb34a92008521a5cf5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97452ea44b0f85cb357facaacb0215fb3620509f2d7a2d0e8892d2c1a0329fcf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a3d22844568b2c4f6e7ac11bf432d10182bf4a95ff6ac54e95bb2a59a04da9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73843670c0a138b6ed003d6a173bb310a7b8ed3a60328918a0d7bc2ceef04866(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ff745a1ecb81ccc1884f96cfea4d30295a14f100a38576c03df4f2c33f5905b(
    value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a0c4673960ad85990e52c5d256daf98714acb20184a1d8727e6e2da07d6c76(
    *,
    maximum_bitrate: typing.Optional[jsii.Number] = None,
    minimum_bitrate: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3028f7640b5f9d85ac64b2096c8f4adf9bbeb90a558e603af1f1bec80ce715(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5322c6c6ac692b282b70f625ee39a170ceb5133074c813e903d645d3ac8ca91e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429f1e773fcf4b03d51707f5c061d26bae9f1ef2e54bcaf088e9313ca8a9c672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c4d2ad1faf95bba76c7701204b788950fd935b32e3c3a367074be5848b3a0e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05987c9101cc2929445deda67d28286b9c79f90aa6ad9e8e9285f2d69c7a6319(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3961de497e4375782fe373e44ae490de3cfae41d521e6c2d0c8714010f5ba430(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64d430154d9f4d11feea4ed680c0b017672a142dcaa7c5a83b1a73c7ac7967e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1404bf6d9851d87e846eed6249a97787dfd0f5fb685396463ada18cb16c5c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d25e8b42a3f10686e50cfbd191b70ce7871530469fb63d2f29723fb2932cd5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e877f6801abdb24901125cfa46ea4240c3c7da256a22f71cdc5ef40fba11af(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85b31f2fac8ddc5a7859559427d73c0666429963161f7224676bd368f98ce8c(
    value: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
