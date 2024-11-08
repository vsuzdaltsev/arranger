'''
# `aws_auditmanager_control`

Refer to the Terraform Registory for docs: [`aws_auditmanager_control`](https://www.terraform.io/docs/providers/aws/r/auditmanager_control).
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


class AuditmanagerControl(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.auditmanagerControl.AuditmanagerControl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control aws_auditmanager_control}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        action_plan_instructions: typing.Optional[builtins.str] = None,
        action_plan_title: typing.Optional[builtins.str] = None,
        control_mapping_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AuditmanagerControlControlMappingSources", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        testing_information: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control aws_auditmanager_control} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#name AuditmanagerControl#name}.
        :param action_plan_instructions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#action_plan_instructions AuditmanagerControl#action_plan_instructions}.
        :param action_plan_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#action_plan_title AuditmanagerControl#action_plan_title}.
        :param control_mapping_sources: control_mapping_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#control_mapping_sources AuditmanagerControl#control_mapping_sources}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#description AuditmanagerControl#description}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#tags AuditmanagerControl#tags}.
        :param testing_information: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#testing_information AuditmanagerControl#testing_information}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f0b3bb9c577d7a4000059f121aa94c51e3c6441f6ae0189ae08bdfc605deba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AuditmanagerControlConfig(
            name=name,
            action_plan_instructions=action_plan_instructions,
            action_plan_title=action_plan_title,
            control_mapping_sources=control_mapping_sources,
            description=description,
            tags=tags,
            testing_information=testing_information,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putControlMappingSources")
    def put_control_mapping_sources(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AuditmanagerControlControlMappingSources", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c95fca78f290b35e086149af35bf2c70e64bf75576074b42637e8b2bc04b4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putControlMappingSources", [value]))

    @jsii.member(jsii_name="resetActionPlanInstructions")
    def reset_action_plan_instructions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionPlanInstructions", []))

    @jsii.member(jsii_name="resetActionPlanTitle")
    def reset_action_plan_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionPlanTitle", []))

    @jsii.member(jsii_name="resetControlMappingSources")
    def reset_control_mapping_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControlMappingSources", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTestingInformation")
    def reset_testing_information(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestingInformation", []))

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
    @jsii.member(jsii_name="controlMappingSources")
    def control_mapping_sources(self) -> "AuditmanagerControlControlMappingSourcesList":
        return typing.cast("AuditmanagerControlControlMappingSourcesList", jsii.get(self, "controlMappingSources"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "tagsAll"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="actionPlanInstructionsInput")
    def action_plan_instructions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionPlanInstructionsInput"))

    @builtins.property
    @jsii.member(jsii_name="actionPlanTitleInput")
    def action_plan_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionPlanTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="controlMappingSourcesInput")
    def control_mapping_sources_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSources"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSources"]]], jsii.get(self, "controlMappingSourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="testingInformationInput")
    def testing_information_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testingInformationInput"))

    @builtins.property
    @jsii.member(jsii_name="actionPlanInstructions")
    def action_plan_instructions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionPlanInstructions"))

    @action_plan_instructions.setter
    def action_plan_instructions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8908c26ed1b5f908f2531ca1410c4b0cb4c6c0c6464357b95faddea23d607b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionPlanInstructions", value)

    @builtins.property
    @jsii.member(jsii_name="actionPlanTitle")
    def action_plan_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionPlanTitle"))

    @action_plan_title.setter
    def action_plan_title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6edc7d6670b5cd80274171fd7a58b34ef6a7f0ddb64e9d42b95dcdc97603b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionPlanTitle", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf1e2128c4d7867ef77934de6640312b946eed4ddda9f37e025dc80238ab7339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd3c2595018eefd5d737bd2289d6249495948f26ce48abdf1c077985ef05d64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31d4c93238b062c3507ef509709c2fc0f5ae40f4924eed36266224f6d56fd586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="testingInformation")
    def testing_information(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testingInformation"))

    @testing_information.setter
    def testing_information(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3208e1799f3dc5add86686a551a449f83496c69671511894dff5b34d1ba70883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testingInformation", value)


@jsii.data_type(
    jsii_type="aws.auditmanagerControl.AuditmanagerControlConfig",
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
        "action_plan_instructions": "actionPlanInstructions",
        "action_plan_title": "actionPlanTitle",
        "control_mapping_sources": "controlMappingSources",
        "description": "description",
        "tags": "tags",
        "testing_information": "testingInformation",
    },
)
class AuditmanagerControlConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action_plan_instructions: typing.Optional[builtins.str] = None,
        action_plan_title: typing.Optional[builtins.str] = None,
        control_mapping_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AuditmanagerControlControlMappingSources", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        testing_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#name AuditmanagerControl#name}.
        :param action_plan_instructions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#action_plan_instructions AuditmanagerControl#action_plan_instructions}.
        :param action_plan_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#action_plan_title AuditmanagerControl#action_plan_title}.
        :param control_mapping_sources: control_mapping_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#control_mapping_sources AuditmanagerControl#control_mapping_sources}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#description AuditmanagerControl#description}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#tags AuditmanagerControl#tags}.
        :param testing_information: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#testing_information AuditmanagerControl#testing_information}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1d171c514f386965f2349394850746462dd8d69cb74f7b4e4faa2149a8dbc58)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument action_plan_instructions", value=action_plan_instructions, expected_type=type_hints["action_plan_instructions"])
            check_type(argname="argument action_plan_title", value=action_plan_title, expected_type=type_hints["action_plan_title"])
            check_type(argname="argument control_mapping_sources", value=control_mapping_sources, expected_type=type_hints["control_mapping_sources"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument testing_information", value=testing_information, expected_type=type_hints["testing_information"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if action_plan_instructions is not None:
            self._values["action_plan_instructions"] = action_plan_instructions
        if action_plan_title is not None:
            self._values["action_plan_title"] = action_plan_title
        if control_mapping_sources is not None:
            self._values["control_mapping_sources"] = control_mapping_sources
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if testing_information is not None:
            self._values["testing_information"] = testing_information

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#name AuditmanagerControl#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_plan_instructions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#action_plan_instructions AuditmanagerControl#action_plan_instructions}.'''
        result = self._values.get("action_plan_instructions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_plan_title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#action_plan_title AuditmanagerControl#action_plan_title}.'''
        result = self._values.get("action_plan_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def control_mapping_sources(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSources"]]]:
        '''control_mapping_sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#control_mapping_sources AuditmanagerControl#control_mapping_sources}
        '''
        result = self._values.get("control_mapping_sources")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSources"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#description AuditmanagerControl#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#tags AuditmanagerControl#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def testing_information(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#testing_information AuditmanagerControl#testing_information}.'''
        result = self._values.get("testing_information")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuditmanagerControlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.auditmanagerControl.AuditmanagerControlControlMappingSources",
    jsii_struct_bases=[],
    name_mapping={
        "source_name": "sourceName",
        "source_set_up_option": "sourceSetUpOption",
        "source_type": "sourceType",
        "source_description": "sourceDescription",
        "source_frequency": "sourceFrequency",
        "source_keyword": "sourceKeyword",
        "troubleshooting_text": "troubleshootingText",
    },
)
class AuditmanagerControlControlMappingSources:
    def __init__(
        self,
        *,
        source_name: builtins.str,
        source_set_up_option: builtins.str,
        source_type: builtins.str,
        source_description: typing.Optional[builtins.str] = None,
        source_frequency: typing.Optional[builtins.str] = None,
        source_keyword: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AuditmanagerControlControlMappingSourcesSourceKeyword", typing.Dict[builtins.str, typing.Any]]]]] = None,
        troubleshooting_text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_name AuditmanagerControl#source_name}.
        :param source_set_up_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_set_up_option AuditmanagerControl#source_set_up_option}.
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_type AuditmanagerControl#source_type}.
        :param source_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_description AuditmanagerControl#source_description}.
        :param source_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_frequency AuditmanagerControl#source_frequency}.
        :param source_keyword: source_keyword block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_keyword AuditmanagerControl#source_keyword}
        :param troubleshooting_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#troubleshooting_text AuditmanagerControl#troubleshooting_text}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3e8c6a622ae9d043fdf3f277ca19a6fdfb0c16da42a873899226462c7089a2e)
            check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
            check_type(argname="argument source_set_up_option", value=source_set_up_option, expected_type=type_hints["source_set_up_option"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument source_description", value=source_description, expected_type=type_hints["source_description"])
            check_type(argname="argument source_frequency", value=source_frequency, expected_type=type_hints["source_frequency"])
            check_type(argname="argument source_keyword", value=source_keyword, expected_type=type_hints["source_keyword"])
            check_type(argname="argument troubleshooting_text", value=troubleshooting_text, expected_type=type_hints["troubleshooting_text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_name": source_name,
            "source_set_up_option": source_set_up_option,
            "source_type": source_type,
        }
        if source_description is not None:
            self._values["source_description"] = source_description
        if source_frequency is not None:
            self._values["source_frequency"] = source_frequency
        if source_keyword is not None:
            self._values["source_keyword"] = source_keyword
        if troubleshooting_text is not None:
            self._values["troubleshooting_text"] = troubleshooting_text

    @builtins.property
    def source_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_name AuditmanagerControl#source_name}.'''
        result = self._values.get("source_name")
        assert result is not None, "Required property 'source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_set_up_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_set_up_option AuditmanagerControl#source_set_up_option}.'''
        result = self._values.get("source_set_up_option")
        assert result is not None, "Required property 'source_set_up_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_type AuditmanagerControl#source_type}.'''
        result = self._values.get("source_type")
        assert result is not None, "Required property 'source_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_description AuditmanagerControl#source_description}.'''
        result = self._values.get("source_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_frequency AuditmanagerControl#source_frequency}.'''
        result = self._values.get("source_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_keyword(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSourcesSourceKeyword"]]]:
        '''source_keyword block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#source_keyword AuditmanagerControl#source_keyword}
        '''
        result = self._values.get("source_keyword")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSourcesSourceKeyword"]]], result)

    @builtins.property
    def troubleshooting_text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#troubleshooting_text AuditmanagerControl#troubleshooting_text}.'''
        result = self._values.get("troubleshooting_text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuditmanagerControlControlMappingSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AuditmanagerControlControlMappingSourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.auditmanagerControl.AuditmanagerControlControlMappingSourcesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35308963b4c264e4a66b74d141ac14ed8ad58b685ffe3b13d5cba31c7aa8144d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AuditmanagerControlControlMappingSourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaece24a1d3b882d2e8310d056c9faab91a8e668205ed5be524ba42f4c4c483a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AuditmanagerControlControlMappingSourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66e268d5759bc0950e78167dfd0bab9b40098de491c7972076f86bdea7dd4d1d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a4148762bd7d5b5f62a753cfe32df5e22415580d31a53a06eb77700a26296b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7bab0d24dbec12df705142dbb0c4dae420917f9885e263e4cd35e1fceb4e21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSources]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06731882825addbddf4f88a99e4ff758fe0eb27f4122122264adb82e9d9c0f6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AuditmanagerControlControlMappingSourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.auditmanagerControl.AuditmanagerControlControlMappingSourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd2aaece32a8e84616ec7915a2fd00599ea9ea3570607e79a602b08ae41994e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSourceKeyword")
    def put_source_keyword(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AuditmanagerControlControlMappingSourcesSourceKeyword", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f2f498e8a0f311039c1082b96d15024cf35ea4145b4d1e6c0ebb98d0bef061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourceKeyword", [value]))

    @jsii.member(jsii_name="resetSourceDescription")
    def reset_source_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDescription", []))

    @jsii.member(jsii_name="resetSourceFrequency")
    def reset_source_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFrequency", []))

    @jsii.member(jsii_name="resetSourceKeyword")
    def reset_source_keyword(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceKeyword", []))

    @jsii.member(jsii_name="resetTroubleshootingText")
    def reset_troubleshooting_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTroubleshootingText", []))

    @builtins.property
    @jsii.member(jsii_name="sourceId")
    def source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceId"))

    @builtins.property
    @jsii.member(jsii_name="sourceKeyword")
    def source_keyword(
        self,
    ) -> "AuditmanagerControlControlMappingSourcesSourceKeywordList":
        return typing.cast("AuditmanagerControlControlMappingSourcesSourceKeywordList", jsii.get(self, "sourceKeyword"))

    @builtins.property
    @jsii.member(jsii_name="sourceDescriptionInput")
    def source_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFrequencyInput")
    def source_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceKeywordInput")
    def source_keyword_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSourcesSourceKeyword"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AuditmanagerControlControlMappingSourcesSourceKeyword"]]], jsii.get(self, "sourceKeywordInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceNameInput")
    def source_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSetUpOptionInput")
    def source_set_up_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceSetUpOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="troubleshootingTextInput")
    def troubleshooting_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "troubleshootingTextInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDescription")
    def source_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDescription"))

    @source_description.setter
    def source_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186d00a4f12e6dbcbfb73b7855fafd0517f0d8246a4dc55f668af2ca45277ece)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDescription", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFrequency")
    def source_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFrequency"))

    @source_frequency.setter
    def source_frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54d3bd7d564df2e8cf01c9039627dba0e83aeb1463860d3b384c170d4e1bb646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="sourceName")
    def source_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceName"))

    @source_name.setter
    def source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__636610e348c59d70c2942a04c053960b6e3456aca8fad14bffb6c1bc64ab3171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceSetUpOption")
    def source_set_up_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceSetUpOption"))

    @source_set_up_option.setter
    def source_set_up_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f0b132540d0f6d0140ed39888883f8aaf878f4bf6eaee792543e6b06c5e967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceSetUpOption", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ae593bf6d3e8c1024f5557a14a36b6558d38bd3593693eb0d00672765b51ab8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="troubleshootingText")
    def troubleshooting_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "troubleshootingText"))

    @troubleshooting_text.setter
    def troubleshooting_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8472a84cfb330190e50adcd78191d0ffb6040a91466e6e23d67189767a35c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "troubleshootingText", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AuditmanagerControlControlMappingSources, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AuditmanagerControlControlMappingSources, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AuditmanagerControlControlMappingSources, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ecebb6a5df30fd8904c2c9863d00bb6572023012c7b7e3d14a32041b594827e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.auditmanagerControl.AuditmanagerControlControlMappingSourcesSourceKeyword",
    jsii_struct_bases=[],
    name_mapping={
        "keyword_input_type": "keywordInputType",
        "keyword_value": "keywordValue",
    },
)
class AuditmanagerControlControlMappingSourcesSourceKeyword:
    def __init__(
        self,
        *,
        keyword_input_type: builtins.str,
        keyword_value: builtins.str,
    ) -> None:
        '''
        :param keyword_input_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#keyword_input_type AuditmanagerControl#keyword_input_type}.
        :param keyword_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#keyword_value AuditmanagerControl#keyword_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fff74f40f907403ca4e6f53f1973ad9a8d483ba6dc3776e29e83fbf2abe7aaa)
            check_type(argname="argument keyword_input_type", value=keyword_input_type, expected_type=type_hints["keyword_input_type"])
            check_type(argname="argument keyword_value", value=keyword_value, expected_type=type_hints["keyword_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keyword_input_type": keyword_input_type,
            "keyword_value": keyword_value,
        }

    @builtins.property
    def keyword_input_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#keyword_input_type AuditmanagerControl#keyword_input_type}.'''
        result = self._values.get("keyword_input_type")
        assert result is not None, "Required property 'keyword_input_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def keyword_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/auditmanager_control#keyword_value AuditmanagerControl#keyword_value}.'''
        result = self._values.get("keyword_value")
        assert result is not None, "Required property 'keyword_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuditmanagerControlControlMappingSourcesSourceKeyword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AuditmanagerControlControlMappingSourcesSourceKeywordList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.auditmanagerControl.AuditmanagerControlControlMappingSourcesSourceKeywordList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a90316dbe5b7d38e5d4d99938e4b8dd0edaa75837bb6b5fb5c5918c3072cbe7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AuditmanagerControlControlMappingSourcesSourceKeywordOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1946deb81b719fc2c32762c921907250a7efa7df26fc6ac4e7ae332a0b0485a0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AuditmanagerControlControlMappingSourcesSourceKeywordOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9564ae70ab8ab235604902af38b4cb9e6e9b17fa87708348b38a91011d9b414)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5fdcd7f881ad1e688c79f9db165908c46cc4aee427eb040bfbd684c66694de9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__365d10649195c2876c869b46d79d89aaf8e7f861b0d61f53e342b346a24cc6ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSourcesSourceKeyword]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSourcesSourceKeyword]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSourcesSourceKeyword]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b18e1b11af00ea617278ea741cfdfeaf3d6532f3661fe5fa2041982a4884873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AuditmanagerControlControlMappingSourcesSourceKeywordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.auditmanagerControl.AuditmanagerControlControlMappingSourcesSourceKeywordOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e26adce145a5a31b403d453fd3ff5fef42e07902593bd33ddea2481f8f9e988)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keywordInputTypeInput")
    def keyword_input_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keywordInputTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keywordValueInput")
    def keyword_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keywordValueInput"))

    @builtins.property
    @jsii.member(jsii_name="keywordInputType")
    def keyword_input_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keywordInputType"))

    @keyword_input_type.setter
    def keyword_input_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8320be0551e1e51e935861fffb00c9bde2ea87f0cfdda430305b3fbffd0a42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keywordInputType", value)

    @builtins.property
    @jsii.member(jsii_name="keywordValue")
    def keyword_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keywordValue"))

    @keyword_value.setter
    def keyword_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac0b961279e67b6179d2636f73d3aad12843a774c3db04a9b6f01b65a2320bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keywordValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AuditmanagerControlControlMappingSourcesSourceKeyword, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AuditmanagerControlControlMappingSourcesSourceKeyword, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AuditmanagerControlControlMappingSourcesSourceKeyword, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f2ae80d40c1fdb8e7a2db8fa6de9f371a5b531b36d2e23d4ded446b0e33c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AuditmanagerControl",
    "AuditmanagerControlConfig",
    "AuditmanagerControlControlMappingSources",
    "AuditmanagerControlControlMappingSourcesList",
    "AuditmanagerControlControlMappingSourcesOutputReference",
    "AuditmanagerControlControlMappingSourcesSourceKeyword",
    "AuditmanagerControlControlMappingSourcesSourceKeywordList",
    "AuditmanagerControlControlMappingSourcesSourceKeywordOutputReference",
]

publication.publish()

def _typecheckingstub__a9f0b3bb9c577d7a4000059f121aa94c51e3c6441f6ae0189ae08bdfc605deba(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    action_plan_instructions: typing.Optional[builtins.str] = None,
    action_plan_title: typing.Optional[builtins.str] = None,
    control_mapping_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AuditmanagerControlControlMappingSources, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    testing_information: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__74c95fca78f290b35e086149af35bf2c70e64bf75576074b42637e8b2bc04b4b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AuditmanagerControlControlMappingSources, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8908c26ed1b5f908f2531ca1410c4b0cb4c6c0c6464357b95faddea23d607b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6edc7d6670b5cd80274171fd7a58b34ef6a7f0ddb64e9d42b95dcdc97603b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf1e2128c4d7867ef77934de6640312b946eed4ddda9f37e025dc80238ab7339(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd3c2595018eefd5d737bd2289d6249495948f26ce48abdf1c077985ef05d64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d4c93238b062c3507ef509709c2fc0f5ae40f4924eed36266224f6d56fd586(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3208e1799f3dc5add86686a551a449f83496c69671511894dff5b34d1ba70883(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1d171c514f386965f2349394850746462dd8d69cb74f7b4e4faa2149a8dbc58(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    action_plan_instructions: typing.Optional[builtins.str] = None,
    action_plan_title: typing.Optional[builtins.str] = None,
    control_mapping_sources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AuditmanagerControlControlMappingSources, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    testing_information: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e8c6a622ae9d043fdf3f277ca19a6fdfb0c16da42a873899226462c7089a2e(
    *,
    source_name: builtins.str,
    source_set_up_option: builtins.str,
    source_type: builtins.str,
    source_description: typing.Optional[builtins.str] = None,
    source_frequency: typing.Optional[builtins.str] = None,
    source_keyword: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AuditmanagerControlControlMappingSourcesSourceKeyword, typing.Dict[builtins.str, typing.Any]]]]] = None,
    troubleshooting_text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35308963b4c264e4a66b74d141ac14ed8ad58b685ffe3b13d5cba31c7aa8144d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaece24a1d3b882d2e8310d056c9faab91a8e668205ed5be524ba42f4c4c483a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e268d5759bc0950e78167dfd0bab9b40098de491c7972076f86bdea7dd4d1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4148762bd7d5b5f62a753cfe32df5e22415580d31a53a06eb77700a26296b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7bab0d24dbec12df705142dbb0c4dae420917f9885e263e4cd35e1fceb4e21d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06731882825addbddf4f88a99e4ff758fe0eb27f4122122264adb82e9d9c0f6b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSources]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2aaece32a8e84616ec7915a2fd00599ea9ea3570607e79a602b08ae41994e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f2f498e8a0f311039c1082b96d15024cf35ea4145b4d1e6c0ebb98d0bef061(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AuditmanagerControlControlMappingSourcesSourceKeyword, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186d00a4f12e6dbcbfb73b7855fafd0517f0d8246a4dc55f668af2ca45277ece(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54d3bd7d564df2e8cf01c9039627dba0e83aeb1463860d3b384c170d4e1bb646(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__636610e348c59d70c2942a04c053960b6e3456aca8fad14bffb6c1bc64ab3171(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f0b132540d0f6d0140ed39888883f8aaf878f4bf6eaee792543e6b06c5e967(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae593bf6d3e8c1024f5557a14a36b6558d38bd3593693eb0d00672765b51ab8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8472a84cfb330190e50adcd78191d0ffb6040a91466e6e23d67189767a35c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecebb6a5df30fd8904c2c9863d00bb6572023012c7b7e3d14a32041b594827e(
    value: typing.Optional[typing.Union[AuditmanagerControlControlMappingSources, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fff74f40f907403ca4e6f53f1973ad9a8d483ba6dc3776e29e83fbf2abe7aaa(
    *,
    keyword_input_type: builtins.str,
    keyword_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90316dbe5b7d38e5d4d99938e4b8dd0edaa75837bb6b5fb5c5918c3072cbe7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1946deb81b719fc2c32762c921907250a7efa7df26fc6ac4e7ae332a0b0485a0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9564ae70ab8ab235604902af38b4cb9e6e9b17fa87708348b38a91011d9b414(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fdcd7f881ad1e688c79f9db165908c46cc4aee427eb040bfbd684c66694de9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365d10649195c2876c869b46d79d89aaf8e7f861b0d61f53e342b346a24cc6ef(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b18e1b11af00ea617278ea741cfdfeaf3d6532f3661fe5fa2041982a4884873(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AuditmanagerControlControlMappingSourcesSourceKeyword]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e26adce145a5a31b403d453fd3ff5fef42e07902593bd33ddea2481f8f9e988(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8320be0551e1e51e935861fffb00c9bde2ea87f0cfdda430305b3fbffd0a42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac0b961279e67b6179d2636f73d3aad12843a774c3db04a9b6f01b65a2320bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f2ae80d40c1fdb8e7a2db8fa6de9f371a5b531b36d2e23d4ded446b0e33c1b(
    value: typing.Optional[typing.Union[AuditmanagerControlControlMappingSourcesSourceKeyword, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
