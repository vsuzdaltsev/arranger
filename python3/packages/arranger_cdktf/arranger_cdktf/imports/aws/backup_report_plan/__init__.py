'''
# `aws_backup_report_plan`

Refer to the Terraform Registory for docs: [`aws_backup_report_plan`](https://www.terraform.io/docs/providers/aws/r/backup_report_plan).
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


class BackupReportPlan(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupReportPlan.BackupReportPlan",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan aws_backup_report_plan}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        report_delivery_channel: typing.Union["BackupReportPlanReportDeliveryChannel", typing.Dict[builtins.str, typing.Any]],
        report_setting: typing.Union["BackupReportPlanReportSetting", typing.Dict[builtins.str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan aws_backup_report_plan} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#name BackupReportPlan#name}.
        :param report_delivery_channel: report_delivery_channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_delivery_channel BackupReportPlan#report_delivery_channel}
        :param report_setting: report_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_setting BackupReportPlan#report_setting}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#description BackupReportPlan#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#id BackupReportPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#tags BackupReportPlan#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#tags_all BackupReportPlan#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1651dceba46c4218314cda3f69710076b1e322dec43322f28ecff30241f7d5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BackupReportPlanConfig(
            name=name,
            report_delivery_channel=report_delivery_channel,
            report_setting=report_setting,
            description=description,
            id=id,
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

    @jsii.member(jsii_name="putReportDeliveryChannel")
    def put_report_delivery_channel(
        self,
        *,
        s3_bucket_name: builtins.str,
        formats: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#s3_bucket_name BackupReportPlan#s3_bucket_name}.
        :param formats: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#formats BackupReportPlan#formats}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#s3_key_prefix BackupReportPlan#s3_key_prefix}.
        '''
        value = BackupReportPlanReportDeliveryChannel(
            s3_bucket_name=s3_bucket_name, formats=formats, s3_key_prefix=s3_key_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putReportDeliveryChannel", [value]))

    @jsii.member(jsii_name="putReportSetting")
    def put_report_setting(
        self,
        *,
        report_template: builtins.str,
        framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        number_of_frameworks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param report_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_template BackupReportPlan#report_template}.
        :param framework_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#framework_arns BackupReportPlan#framework_arns}.
        :param number_of_frameworks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#number_of_frameworks BackupReportPlan#number_of_frameworks}.
        '''
        value = BackupReportPlanReportSetting(
            report_template=report_template,
            framework_arns=framework_arns,
            number_of_frameworks=number_of_frameworks,
        )

        return typing.cast(None, jsii.invoke(self, "putReportSetting", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStatus")
    def deployment_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentStatus"))

    @builtins.property
    @jsii.member(jsii_name="reportDeliveryChannel")
    def report_delivery_channel(
        self,
    ) -> "BackupReportPlanReportDeliveryChannelOutputReference":
        return typing.cast("BackupReportPlanReportDeliveryChannelOutputReference", jsii.get(self, "reportDeliveryChannel"))

    @builtins.property
    @jsii.member(jsii_name="reportSetting")
    def report_setting(self) -> "BackupReportPlanReportSettingOutputReference":
        return typing.cast("BackupReportPlanReportSettingOutputReference", jsii.get(self, "reportSetting"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="reportDeliveryChannelInput")
    def report_delivery_channel_input(
        self,
    ) -> typing.Optional["BackupReportPlanReportDeliveryChannel"]:
        return typing.cast(typing.Optional["BackupReportPlanReportDeliveryChannel"], jsii.get(self, "reportDeliveryChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="reportSettingInput")
    def report_setting_input(self) -> typing.Optional["BackupReportPlanReportSetting"]:
        return typing.cast(typing.Optional["BackupReportPlanReportSetting"], jsii.get(self, "reportSettingInput"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f0524580fd97422b8cf5f8cb5103b1ddc12ea6fb097c1af9110998fe2bc7d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18dd3c76f8f096cf1b960a2393bbbb525904ea9f2ab47b5eef5acc6f0d98f5e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7094cdff347c5508a5b81513a27ff8208d8f72c5cd80742d0aefe24ec2fc8b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a748204c14070b215da25a9a8b9253d0d52988aed5f1189c909000c51f44510b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49f28a5c6b488eb0ff2feca7a3ec6dc5bbbdff97c95bcb8cf16d4c709e290abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.backupReportPlan.BackupReportPlanConfig",
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
        "report_delivery_channel": "reportDeliveryChannel",
        "report_setting": "reportSetting",
        "description": "description",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class BackupReportPlanConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        report_delivery_channel: typing.Union["BackupReportPlanReportDeliveryChannel", typing.Dict[builtins.str, typing.Any]],
        report_setting: typing.Union["BackupReportPlanReportSetting", typing.Dict[builtins.str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#name BackupReportPlan#name}.
        :param report_delivery_channel: report_delivery_channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_delivery_channel BackupReportPlan#report_delivery_channel}
        :param report_setting: report_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_setting BackupReportPlan#report_setting}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#description BackupReportPlan#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#id BackupReportPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#tags BackupReportPlan#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#tags_all BackupReportPlan#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(report_delivery_channel, dict):
            report_delivery_channel = BackupReportPlanReportDeliveryChannel(**report_delivery_channel)
        if isinstance(report_setting, dict):
            report_setting = BackupReportPlanReportSetting(**report_setting)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9098e6f4b5fe7bf3759bcbc34792a18f444db41e4bdf91876960e5627c4b7d1d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument report_delivery_channel", value=report_delivery_channel, expected_type=type_hints["report_delivery_channel"])
            check_type(argname="argument report_setting", value=report_setting, expected_type=type_hints["report_setting"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "report_delivery_channel": report_delivery_channel,
            "report_setting": report_setting,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#name BackupReportPlan#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def report_delivery_channel(self) -> "BackupReportPlanReportDeliveryChannel":
        '''report_delivery_channel block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_delivery_channel BackupReportPlan#report_delivery_channel}
        '''
        result = self._values.get("report_delivery_channel")
        assert result is not None, "Required property 'report_delivery_channel' is missing"
        return typing.cast("BackupReportPlanReportDeliveryChannel", result)

    @builtins.property
    def report_setting(self) -> "BackupReportPlanReportSetting":
        '''report_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_setting BackupReportPlan#report_setting}
        '''
        result = self._values.get("report_setting")
        assert result is not None, "Required property 'report_setting' is missing"
        return typing.cast("BackupReportPlanReportSetting", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#description BackupReportPlan#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#id BackupReportPlan#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#tags BackupReportPlan#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#tags_all BackupReportPlan#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupReportPlanConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.backupReportPlan.BackupReportPlanReportDeliveryChannel",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket_name": "s3BucketName",
        "formats": "formats",
        "s3_key_prefix": "s3KeyPrefix",
    },
)
class BackupReportPlanReportDeliveryChannel:
    def __init__(
        self,
        *,
        s3_bucket_name: builtins.str,
        formats: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#s3_bucket_name BackupReportPlan#s3_bucket_name}.
        :param formats: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#formats BackupReportPlan#formats}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#s3_key_prefix BackupReportPlan#s3_key_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f92879aa79766832faabbed20f358a5a4d8a0dba003e235f9a746a4bc016f6d)
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument formats", value=formats, expected_type=type_hints["formats"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_bucket_name": s3_bucket_name,
        }
        if formats is not None:
            self._values["formats"] = formats
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#s3_bucket_name BackupReportPlan#s3_bucket_name}.'''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def formats(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#formats BackupReportPlan#formats}.'''
        result = self._values.get("formats")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#s3_key_prefix BackupReportPlan#s3_key_prefix}.'''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupReportPlanReportDeliveryChannel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupReportPlanReportDeliveryChannelOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupReportPlan.BackupReportPlanReportDeliveryChannelOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a91514126533b2dd439d181cad2e217e96920901b02a997f7fa39aa2f0527e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFormats")
    def reset_formats(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormats", []))

    @jsii.member(jsii_name="resetS3KeyPrefix")
    def reset_s3_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KeyPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="formatsInput")
    def formats_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "formatsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketNameInput")
    def s3_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefixInput")
    def s3_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="formats")
    def formats(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "formats"))

    @formats.setter
    def formats(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__887b6134b0bd135c2e12c32dca609ba97c68318123d36f9e27198a5f6cab3e79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formats", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10f41ebcc4d4d6cd160a3f217d3a8ef39bb3886832753465c7cbbd36a4f15cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e790fadc084b76ecd1bd92c45a8ee196fe48c0280e8fa535a53dd5e0ee840bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupReportPlanReportDeliveryChannel]:
        return typing.cast(typing.Optional[BackupReportPlanReportDeliveryChannel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupReportPlanReportDeliveryChannel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ea7d4aaf92e711c4f178586d58eb28a7529b7f8107e26ad792bf62904d2186d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.backupReportPlan.BackupReportPlanReportSetting",
    jsii_struct_bases=[],
    name_mapping={
        "report_template": "reportTemplate",
        "framework_arns": "frameworkArns",
        "number_of_frameworks": "numberOfFrameworks",
    },
)
class BackupReportPlanReportSetting:
    def __init__(
        self,
        *,
        report_template: builtins.str,
        framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        number_of_frameworks: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param report_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_template BackupReportPlan#report_template}.
        :param framework_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#framework_arns BackupReportPlan#framework_arns}.
        :param number_of_frameworks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#number_of_frameworks BackupReportPlan#number_of_frameworks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4bd03a94d9310a810e3735cd08648fb8373cea14cc2897bbc223792617b845)
            check_type(argname="argument report_template", value=report_template, expected_type=type_hints["report_template"])
            check_type(argname="argument framework_arns", value=framework_arns, expected_type=type_hints["framework_arns"])
            check_type(argname="argument number_of_frameworks", value=number_of_frameworks, expected_type=type_hints["number_of_frameworks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "report_template": report_template,
        }
        if framework_arns is not None:
            self._values["framework_arns"] = framework_arns
        if number_of_frameworks is not None:
            self._values["number_of_frameworks"] = number_of_frameworks

    @builtins.property
    def report_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#report_template BackupReportPlan#report_template}.'''
        result = self._values.get("report_template")
        assert result is not None, "Required property 'report_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def framework_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#framework_arns BackupReportPlan#framework_arns}.'''
        result = self._values.get("framework_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def number_of_frameworks(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_report_plan#number_of_frameworks BackupReportPlan#number_of_frameworks}.'''
        result = self._values.get("number_of_frameworks")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupReportPlanReportSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupReportPlanReportSettingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupReportPlan.BackupReportPlanReportSettingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ba53a08b5a1ce378d138fec3bbd7998b6cb7c034f6c0a8d7679ede26d81a520)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFrameworkArns")
    def reset_framework_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrameworkArns", []))

    @jsii.member(jsii_name="resetNumberOfFrameworks")
    def reset_number_of_frameworks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfFrameworks", []))

    @builtins.property
    @jsii.member(jsii_name="frameworkArnsInput")
    def framework_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "frameworkArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfFrameworksInput")
    def number_of_frameworks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfFrameworksInput"))

    @builtins.property
    @jsii.member(jsii_name="reportTemplateInput")
    def report_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reportTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="frameworkArns")
    def framework_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "frameworkArns"))

    @framework_arns.setter
    def framework_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac948e5d139b8ae66b943e88b26fe9f2103a63ac83ceb4f78121580750569aa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkArns", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfFrameworks")
    def number_of_frameworks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfFrameworks"))

    @number_of_frameworks.setter
    def number_of_frameworks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a1c5bd2ed63b746b9b4600a5c1a2ea1c8eabfc6601ee7ee6f06f2a76f0e509)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfFrameworks", value)

    @builtins.property
    @jsii.member(jsii_name="reportTemplate")
    def report_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reportTemplate"))

    @report_template.setter
    def report_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adab67947b8d58381abfa5e480668baccd2c0e83e140827819523f823c633dec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupReportPlanReportSetting]:
        return typing.cast(typing.Optional[BackupReportPlanReportSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupReportPlanReportSetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d9fba0e5f6c96c08aa6b2973c4774b8de32bf9ddfaa89fb4749a2fb1bf923b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BackupReportPlan",
    "BackupReportPlanConfig",
    "BackupReportPlanReportDeliveryChannel",
    "BackupReportPlanReportDeliveryChannelOutputReference",
    "BackupReportPlanReportSetting",
    "BackupReportPlanReportSettingOutputReference",
]

publication.publish()

def _typecheckingstub__e1651dceba46c4218314cda3f69710076b1e322dec43322f28ecff30241f7d5d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    report_delivery_channel: typing.Union[BackupReportPlanReportDeliveryChannel, typing.Dict[builtins.str, typing.Any]],
    report_setting: typing.Union[BackupReportPlanReportSetting, typing.Dict[builtins.str, typing.Any]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__27f0524580fd97422b8cf5f8cb5103b1ddc12ea6fb097c1af9110998fe2bc7d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18dd3c76f8f096cf1b960a2393bbbb525904ea9f2ab47b5eef5acc6f0d98f5e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7094cdff347c5508a5b81513a27ff8208d8f72c5cd80742d0aefe24ec2fc8b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a748204c14070b215da25a9a8b9253d0d52988aed5f1189c909000c51f44510b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f28a5c6b488eb0ff2feca7a3ec6dc5bbbdff97c95bcb8cf16d4c709e290abd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9098e6f4b5fe7bf3759bcbc34792a18f444db41e4bdf91876960e5627c4b7d1d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    report_delivery_channel: typing.Union[BackupReportPlanReportDeliveryChannel, typing.Dict[builtins.str, typing.Any]],
    report_setting: typing.Union[BackupReportPlanReportSetting, typing.Dict[builtins.str, typing.Any]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f92879aa79766832faabbed20f358a5a4d8a0dba003e235f9a746a4bc016f6d(
    *,
    s3_bucket_name: builtins.str,
    formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a91514126533b2dd439d181cad2e217e96920901b02a997f7fa39aa2f0527e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__887b6134b0bd135c2e12c32dca609ba97c68318123d36f9e27198a5f6cab3e79(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10f41ebcc4d4d6cd160a3f217d3a8ef39bb3886832753465c7cbbd36a4f15cbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e790fadc084b76ecd1bd92c45a8ee196fe48c0280e8fa535a53dd5e0ee840bc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea7d4aaf92e711c4f178586d58eb28a7529b7f8107e26ad792bf62904d2186d(
    value: typing.Optional[BackupReportPlanReportDeliveryChannel],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4bd03a94d9310a810e3735cd08648fb8373cea14cc2897bbc223792617b845(
    *,
    report_template: builtins.str,
    framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    number_of_frameworks: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba53a08b5a1ce378d138fec3bbd7998b6cb7c034f6c0a8d7679ede26d81a520(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac948e5d139b8ae66b943e88b26fe9f2103a63ac83ceb4f78121580750569aa5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a1c5bd2ed63b746b9b4600a5c1a2ea1c8eabfc6601ee7ee6f06f2a76f0e509(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adab67947b8d58381abfa5e480668baccd2c0e83e140827819523f823c633dec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d9fba0e5f6c96c08aa6b2973c4774b8de32bf9ddfaa89fb4749a2fb1bf923b(
    value: typing.Optional[BackupReportPlanReportSetting],
) -> None:
    """Type checking stubs"""
    pass
