'''
# `aws_sagemaker_workteam`

Refer to the Terraform Registory for docs: [`aws_sagemaker_workteam`](https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam).
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


class SagemakerWorkteam(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteam",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam aws_sagemaker_workteam}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        description: builtins.str,
        member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerWorkteamMemberDefinition", typing.Dict[builtins.str, typing.Any]]]],
        workforce_name: builtins.str,
        workteam_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        notification_configuration: typing.Optional[typing.Union["SagemakerWorkteamNotificationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam aws_sagemaker_workteam} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#description SagemakerWorkteam#description}.
        :param member_definition: member_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#member_definition SagemakerWorkteam#member_definition}
        :param workforce_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#workforce_name SagemakerWorkteam#workforce_name}.
        :param workteam_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#workteam_name SagemakerWorkteam#workteam_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#id SagemakerWorkteam#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_configuration: notification_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#notification_configuration SagemakerWorkteam#notification_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#tags SagemakerWorkteam#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#tags_all SagemakerWorkteam#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b3b501dbc4203164202ba4e56883faef928290fad8084a65611a0b6e55b8eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerWorkteamConfig(
            description=description,
            member_definition=member_definition,
            workforce_name=workforce_name,
            workteam_name=workteam_name,
            id=id,
            notification_configuration=notification_configuration,
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

    @jsii.member(jsii_name="putMemberDefinition")
    def put_member_definition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerWorkteamMemberDefinition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a31037a66fb1f1b94f99567f9ef8ed259d7a9fae3fb61fb15f41a18e6639f938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMemberDefinition", [value]))

    @jsii.member(jsii_name="putNotificationConfiguration")
    def put_notification_configuration(
        self,
        *,
        notification_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#notification_topic_arn SagemakerWorkteam#notification_topic_arn}.
        '''
        value = SagemakerWorkteamNotificationConfiguration(
            notification_topic_arn=notification_topic_arn
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationConfiguration")
    def reset_notification_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfiguration", []))

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
    @jsii.member(jsii_name="memberDefinition")
    def member_definition(self) -> "SagemakerWorkteamMemberDefinitionList":
        return typing.cast("SagemakerWorkteamMemberDefinitionList", jsii.get(self, "memberDefinition"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> "SagemakerWorkteamNotificationConfigurationOutputReference":
        return typing.cast("SagemakerWorkteamNotificationConfigurationOutputReference", jsii.get(self, "notificationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="subdomain")
    def subdomain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdomain"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="memberDefinitionInput")
    def member_definition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]]], jsii.get(self, "memberDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigurationInput")
    def notification_configuration_input(
        self,
    ) -> typing.Optional["SagemakerWorkteamNotificationConfiguration"]:
        return typing.cast(typing.Optional["SagemakerWorkteamNotificationConfiguration"], jsii.get(self, "notificationConfigurationInput"))

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
    @jsii.member(jsii_name="workforceNameInput")
    def workforce_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workforceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="workteamNameInput")
    def workteam_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workteamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c06233f1de07266f028b2dd2b0da500f93b34e7393c621a858799057ac2fca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab4e891f686a814cfa2d4eb7c0e4adfb352867349b79fc3dcb441c4cf58676cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d41f16ef30e5e9e30878e125e10a1dfd6251bfb9de425c1b8534c5f61acb708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd828e74dbe326ccbf0430e0d0285836d0f32c2e34984652d67ae98e39864eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="workforceName")
    def workforce_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workforceName"))

    @workforce_name.setter
    def workforce_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414a371c7bdcc8d16243b44ebceecaa9d30cca09905acdc603b6026c1ce892e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workforceName", value)

    @builtins.property
    @jsii.member(jsii_name="workteamName")
    def workteam_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workteamName"))

    @workteam_name.setter
    def workteam_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7d228db3a12f5b8f3cc8cdf0574a9ad83291a9867df56dfcfcaf278f9964ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workteamName", value)


@jsii.data_type(
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "description": "description",
        "member_definition": "memberDefinition",
        "workforce_name": "workforceName",
        "workteam_name": "workteamName",
        "id": "id",
        "notification_configuration": "notificationConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerWorkteamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        description: builtins.str,
        member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerWorkteamMemberDefinition", typing.Dict[builtins.str, typing.Any]]]],
        workforce_name: builtins.str,
        workteam_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        notification_configuration: typing.Optional[typing.Union["SagemakerWorkteamNotificationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#description SagemakerWorkteam#description}.
        :param member_definition: member_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#member_definition SagemakerWorkteam#member_definition}
        :param workforce_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#workforce_name SagemakerWorkteam#workforce_name}.
        :param workteam_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#workteam_name SagemakerWorkteam#workteam_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#id SagemakerWorkteam#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_configuration: notification_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#notification_configuration SagemakerWorkteam#notification_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#tags SagemakerWorkteam#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#tags_all SagemakerWorkteam#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(notification_configuration, dict):
            notification_configuration = SagemakerWorkteamNotificationConfiguration(**notification_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbbd1eeefe9731c19fcf42dcb9c0e747432fb88e61b13cd0c84fef82855b9407)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument member_definition", value=member_definition, expected_type=type_hints["member_definition"])
            check_type(argname="argument workforce_name", value=workforce_name, expected_type=type_hints["workforce_name"])
            check_type(argname="argument workteam_name", value=workteam_name, expected_type=type_hints["workteam_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_configuration", value=notification_configuration, expected_type=type_hints["notification_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "member_definition": member_definition,
            "workforce_name": workforce_name,
            "workteam_name": workteam_name,
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
        if notification_configuration is not None:
            self._values["notification_configuration"] = notification_configuration
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
    def description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#description SagemakerWorkteam#description}.'''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_definition(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]]:
        '''member_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#member_definition SagemakerWorkteam#member_definition}
        '''
        result = self._values.get("member_definition")
        assert result is not None, "Required property 'member_definition' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerWorkteamMemberDefinition"]], result)

    @builtins.property
    def workforce_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#workforce_name SagemakerWorkteam#workforce_name}.'''
        result = self._values.get("workforce_name")
        assert result is not None, "Required property 'workforce_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workteam_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#workteam_name SagemakerWorkteam#workteam_name}.'''
        result = self._values.get("workteam_name")
        assert result is not None, "Required property 'workteam_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#id SagemakerWorkteam#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_configuration(
        self,
    ) -> typing.Optional["SagemakerWorkteamNotificationConfiguration"]:
        '''notification_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#notification_configuration SagemakerWorkteam#notification_configuration}
        '''
        result = self._values.get("notification_configuration")
        return typing.cast(typing.Optional["SagemakerWorkteamNotificationConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#tags SagemakerWorkteam#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#tags_all SagemakerWorkteam#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "cognito_member_definition": "cognitoMemberDefinition",
        "oidc_member_definition": "oidcMemberDefinition",
    },
)
class SagemakerWorkteamMemberDefinition:
    def __init__(
        self,
        *,
        cognito_member_definition: typing.Optional[typing.Union["SagemakerWorkteamMemberDefinitionCognitoMemberDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
        oidc_member_definition: typing.Optional[typing.Union["SagemakerWorkteamMemberDefinitionOidcMemberDefinition", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cognito_member_definition: cognito_member_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#cognito_member_definition SagemakerWorkteam#cognito_member_definition}
        :param oidc_member_definition: oidc_member_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#oidc_member_definition SagemakerWorkteam#oidc_member_definition}
        '''
        if isinstance(cognito_member_definition, dict):
            cognito_member_definition = SagemakerWorkteamMemberDefinitionCognitoMemberDefinition(**cognito_member_definition)
        if isinstance(oidc_member_definition, dict):
            oidc_member_definition = SagemakerWorkteamMemberDefinitionOidcMemberDefinition(**oidc_member_definition)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2366ac26f77f9e81e5b607a18eca72752cacc61f9c5f8db6fed88f3a62ce6af4)
            check_type(argname="argument cognito_member_definition", value=cognito_member_definition, expected_type=type_hints["cognito_member_definition"])
            check_type(argname="argument oidc_member_definition", value=oidc_member_definition, expected_type=type_hints["oidc_member_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cognito_member_definition is not None:
            self._values["cognito_member_definition"] = cognito_member_definition
        if oidc_member_definition is not None:
            self._values["oidc_member_definition"] = oidc_member_definition

    @builtins.property
    def cognito_member_definition(
        self,
    ) -> typing.Optional["SagemakerWorkteamMemberDefinitionCognitoMemberDefinition"]:
        '''cognito_member_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#cognito_member_definition SagemakerWorkteam#cognito_member_definition}
        '''
        result = self._values.get("cognito_member_definition")
        return typing.cast(typing.Optional["SagemakerWorkteamMemberDefinitionCognitoMemberDefinition"], result)

    @builtins.property
    def oidc_member_definition(
        self,
    ) -> typing.Optional["SagemakerWorkteamMemberDefinitionOidcMemberDefinition"]:
        '''oidc_member_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#oidc_member_definition SagemakerWorkteam#oidc_member_definition}
        '''
        result = self._values.get("oidc_member_definition")
        return typing.cast(typing.Optional["SagemakerWorkteamMemberDefinitionOidcMemberDefinition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamMemberDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionCognitoMemberDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "user_group": "userGroup",
        "user_pool": "userPool",
    },
)
class SagemakerWorkteamMemberDefinitionCognitoMemberDefinition:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        user_group: builtins.str,
        user_pool: builtins.str,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#client_id SagemakerWorkteam#client_id}.
        :param user_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#user_group SagemakerWorkteam#user_group}.
        :param user_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#user_pool SagemakerWorkteam#user_pool}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33873c48a8a76449a2690f45f8432c462b57afda505bba983cccc0911e8c7e6)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument user_group", value=user_group, expected_type=type_hints["user_group"])
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "user_group": user_group,
            "user_pool": user_pool,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#client_id SagemakerWorkteam#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#user_group SagemakerWorkteam#user_group}.'''
        result = self._values.get("user_group")
        assert result is not None, "Required property 'user_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#user_pool SagemakerWorkteam#user_pool}.'''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamMemberDefinitionCognitoMemberDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6f6774403b1e1d0485e1474fa530253b1d15c2772b56afe5b678f9b8f217f11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupInput")
    def user_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolInput")
    def user_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a09bb4725b679866b3ab089785fccf2e6d21e5c64cd98529368fbdf4353ed7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="userGroup")
    def user_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userGroup"))

    @user_group.setter
    def user_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6230b74999d4150a95cbe8648e103d58a64392a179f902fd338d4b222920118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroup", value)

    @builtins.property
    @jsii.member(jsii_name="userPool")
    def user_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPool"))

    @user_pool.setter
    def user_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341539d26aa9099e305143adcd2808fcd0b5087c7dd910a086b40aebc479540d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPool", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3f187c658d5099c04c75e6345d5cfbc470730c44dfd3f57abed1c93f582692c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerWorkteamMemberDefinitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3345fa4e28ca53fc6f827af094fa992e8d76be8f5b3020ef70dd71b647e95606)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerWorkteamMemberDefinitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe4bc044fa3caeb860b8fae497770cb50c7b771a5e6ed7e0fc186a0e1cde31ed)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerWorkteamMemberDefinitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de00698bf8f0bdaf309cff4c0d4c051dac315a351845bc5c071ff2d7ecdd9d88)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ec8523a6a375ab68eaf38e485f6de7fdafef4d4a3a7955e00509ddd2ca3db82)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac5939fa166e681ba3eb76d81acb01c663e7dcd2304c20c35872a4282258f1aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e60e9814fd04c84096c52b8ef72c1db0e83bbb47a8096c5bfaec0aed9a2e79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionOidcMemberDefinition",
    jsii_struct_bases=[],
    name_mapping={"groups": "groups"},
)
class SagemakerWorkteamMemberDefinitionOidcMemberDefinition:
    def __init__(self, *, groups: typing.Sequence[builtins.str]) -> None:
        '''
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#groups SagemakerWorkteam#groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934409979e1770e70e5f3260abe8efed920a8cd3d79b292be96f6d38ebb176eb)
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "groups": groups,
        }

    @builtins.property
    def groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#groups SagemakerWorkteam#groups}.'''
        result = self._values.get("groups")
        assert result is not None, "Required property 'groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamMemberDefinitionOidcMemberDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9ecd3bea28855bc5e40e5f7dc3baa41a762cdddb11a248f2e0e02e853f8bd1a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea114467442b4a608b88d58cb3f5f614acf24b8e199866a9e41102df2416f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa03949089d66c86f6715aac8b42a2b7b4aa01a459b283ad2fcd12fe3ba5bcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerWorkteamMemberDefinitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamMemberDefinitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1d91bfc706bcb03b0c95a9447537283793770f4080573f81d7a1920e3b288db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCognitoMemberDefinition")
    def put_cognito_member_definition(
        self,
        *,
        client_id: builtins.str,
        user_group: builtins.str,
        user_pool: builtins.str,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#client_id SagemakerWorkteam#client_id}.
        :param user_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#user_group SagemakerWorkteam#user_group}.
        :param user_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#user_pool SagemakerWorkteam#user_pool}.
        '''
        value = SagemakerWorkteamMemberDefinitionCognitoMemberDefinition(
            client_id=client_id, user_group=user_group, user_pool=user_pool
        )

        return typing.cast(None, jsii.invoke(self, "putCognitoMemberDefinition", [value]))

    @jsii.member(jsii_name="putOidcMemberDefinition")
    def put_oidc_member_definition(
        self,
        *,
        groups: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#groups SagemakerWorkteam#groups}.
        '''
        value = SagemakerWorkteamMemberDefinitionOidcMemberDefinition(groups=groups)

        return typing.cast(None, jsii.invoke(self, "putOidcMemberDefinition", [value]))

    @jsii.member(jsii_name="resetCognitoMemberDefinition")
    def reset_cognito_member_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCognitoMemberDefinition", []))

    @jsii.member(jsii_name="resetOidcMemberDefinition")
    def reset_oidc_member_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcMemberDefinition", []))

    @builtins.property
    @jsii.member(jsii_name="cognitoMemberDefinition")
    def cognito_member_definition(
        self,
    ) -> SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference:
        return typing.cast(SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference, jsii.get(self, "cognitoMemberDefinition"))

    @builtins.property
    @jsii.member(jsii_name="oidcMemberDefinition")
    def oidc_member_definition(
        self,
    ) -> SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference:
        return typing.cast(SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference, jsii.get(self, "oidcMemberDefinition"))

    @builtins.property
    @jsii.member(jsii_name="cognitoMemberDefinitionInput")
    def cognito_member_definition_input(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition], jsii.get(self, "cognitoMemberDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcMemberDefinitionInput")
    def oidc_member_definition_input(
        self,
    ) -> typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition]:
        return typing.cast(typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition], jsii.get(self, "oidcMemberDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b5a96ee1107670fba71aca7b35bd066eeed3749e3fa9bd16fbd9715dcfb0d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamNotificationConfiguration",
    jsii_struct_bases=[],
    name_mapping={"notification_topic_arn": "notificationTopicArn"},
)
class SagemakerWorkteamNotificationConfiguration:
    def __init__(
        self,
        *,
        notification_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#notification_topic_arn SagemakerWorkteam#notification_topic_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a71b9993b2d707d766b6b12d9759867340a2b6eb1277eb7ce4c4a1b32d577e)
            check_type(argname="argument notification_topic_arn", value=notification_topic_arn, expected_type=type_hints["notification_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_workteam#notification_topic_arn SagemakerWorkteam#notification_topic_arn}.'''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerWorkteamNotificationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerWorkteamNotificationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerWorkteam.SagemakerWorkteamNotificationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6c8be2d1af1582518a8fb8e9a077ac4b1cbb8c5c3f6b10088a8ac3beecef047)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotificationTopicArn")
    def reset_notification_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationTopicArn", []))

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArnInput")
    def notification_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f56142bf8c602c8a68ff5934897890397296e245ee485ffd33faa32e409e3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerWorkteamNotificationConfiguration]:
        return typing.cast(typing.Optional[SagemakerWorkteamNotificationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerWorkteamNotificationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d52cb98a0b1952db0a2fd0508d71cfb42eb8db61051bb58df10d9f7df8ce032)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerWorkteam",
    "SagemakerWorkteamConfig",
    "SagemakerWorkteamMemberDefinition",
    "SagemakerWorkteamMemberDefinitionCognitoMemberDefinition",
    "SagemakerWorkteamMemberDefinitionCognitoMemberDefinitionOutputReference",
    "SagemakerWorkteamMemberDefinitionList",
    "SagemakerWorkteamMemberDefinitionOidcMemberDefinition",
    "SagemakerWorkteamMemberDefinitionOidcMemberDefinitionOutputReference",
    "SagemakerWorkteamMemberDefinitionOutputReference",
    "SagemakerWorkteamNotificationConfiguration",
    "SagemakerWorkteamNotificationConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__b1b3b501dbc4203164202ba4e56883faef928290fad8084a65611a0b6e55b8eb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    description: builtins.str,
    member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerWorkteamMemberDefinition, typing.Dict[builtins.str, typing.Any]]]],
    workforce_name: builtins.str,
    workteam_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    notification_configuration: typing.Optional[typing.Union[SagemakerWorkteamNotificationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a31037a66fb1f1b94f99567f9ef8ed259d7a9fae3fb61fb15f41a18e6639f938(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerWorkteamMemberDefinition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c06233f1de07266f028b2dd2b0da500f93b34e7393c621a858799057ac2fca6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4e891f686a814cfa2d4eb7c0e4adfb352867349b79fc3dcb441c4cf58676cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d41f16ef30e5e9e30878e125e10a1dfd6251bfb9de425c1b8534c5f61acb708(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd828e74dbe326ccbf0430e0d0285836d0f32c2e34984652d67ae98e39864eb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414a371c7bdcc8d16243b44ebceecaa9d30cca09905acdc603b6026c1ce892e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7d228db3a12f5b8f3cc8cdf0574a9ad83291a9867df56dfcfcaf278f9964ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbbd1eeefe9731c19fcf42dcb9c0e747432fb88e61b13cd0c84fef82855b9407(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: builtins.str,
    member_definition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerWorkteamMemberDefinition, typing.Dict[builtins.str, typing.Any]]]],
    workforce_name: builtins.str,
    workteam_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    notification_configuration: typing.Optional[typing.Union[SagemakerWorkteamNotificationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2366ac26f77f9e81e5b607a18eca72752cacc61f9c5f8db6fed88f3a62ce6af4(
    *,
    cognito_member_definition: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    oidc_member_definition: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinitionOidcMemberDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c33873c48a8a76449a2690f45f8432c462b57afda505bba983cccc0911e8c7e6(
    *,
    client_id: builtins.str,
    user_group: builtins.str,
    user_pool: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f6774403b1e1d0485e1474fa530253b1d15c2772b56afe5b678f9b8f217f11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a09bb4725b679866b3ab089785fccf2e6d21e5c64cd98529368fbdf4353ed7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6230b74999d4150a95cbe8648e103d58a64392a179f902fd338d4b222920118(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341539d26aa9099e305143adcd2808fcd0b5087c7dd910a086b40aebc479540d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f187c658d5099c04c75e6345d5cfbc470730c44dfd3f57abed1c93f582692c(
    value: typing.Optional[SagemakerWorkteamMemberDefinitionCognitoMemberDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3345fa4e28ca53fc6f827af094fa992e8d76be8f5b3020ef70dd71b647e95606(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4bc044fa3caeb860b8fae497770cb50c7b771a5e6ed7e0fc186a0e1cde31ed(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de00698bf8f0bdaf309cff4c0d4c051dac315a351845bc5c071ff2d7ecdd9d88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ec8523a6a375ab68eaf38e485f6de7fdafef4d4a3a7955e00509ddd2ca3db82(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5939fa166e681ba3eb76d81acb01c663e7dcd2304c20c35872a4282258f1aa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e60e9814fd04c84096c52b8ef72c1db0e83bbb47a8096c5bfaec0aed9a2e79(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerWorkteamMemberDefinition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934409979e1770e70e5f3260abe8efed920a8cd3d79b292be96f6d38ebb176eb(
    *,
    groups: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ecd3bea28855bc5e40e5f7dc3baa41a762cdddb11a248f2e0e02e853f8bd1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea114467442b4a608b88d58cb3f5f614acf24b8e199866a9e41102df2416f8d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa03949089d66c86f6715aac8b42a2b7b4aa01a459b283ad2fcd12fe3ba5bcb(
    value: typing.Optional[SagemakerWorkteamMemberDefinitionOidcMemberDefinition],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d91bfc706bcb03b0c95a9447537283793770f4080573f81d7a1920e3b288db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b5a96ee1107670fba71aca7b35bd066eeed3749e3fa9bd16fbd9715dcfb0d5(
    value: typing.Optional[typing.Union[SagemakerWorkteamMemberDefinition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a71b9993b2d707d766b6b12d9759867340a2b6eb1277eb7ce4c4a1b32d577e(
    *,
    notification_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c8be2d1af1582518a8fb8e9a077ac4b1cbb8c5c3f6b10088a8ac3beecef047(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f56142bf8c602c8a68ff5934897890397296e245ee485ffd33faa32e409e3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d52cb98a0b1952db0a2fd0508d71cfb42eb8db61051bb58df10d9f7df8ce032(
    value: typing.Optional[SagemakerWorkteamNotificationConfiguration],
) -> None:
    """Type checking stubs"""
    pass
