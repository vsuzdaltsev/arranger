'''
# `aws_backup_plan`

Refer to the Terraform Registory for docs: [`aws_backup_plan`](https://www.terraform.io/docs/providers/aws/r/backup_plan).
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


class BackupPlan(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlan",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/backup_plan aws_backup_plan}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BackupPlanRule", typing.Dict[builtins.str, typing.Any]]]],
        advanced_backup_setting: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BackupPlanAdvancedBackupSetting", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/backup_plan aws_backup_plan} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#name BackupPlan#name}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#rule BackupPlan#rule}
        :param advanced_backup_setting: advanced_backup_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#advanced_backup_setting BackupPlan#advanced_backup_setting}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#id BackupPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#tags BackupPlan#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#tags_all BackupPlan#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8935ca17e17be88a1ae73397f59bccb1a4d6338f6c7072da81dfb52e5dc14c8e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BackupPlanConfig(
            name=name,
            rule=rule,
            advanced_backup_setting=advanced_backup_setting,
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

    @jsii.member(jsii_name="putAdvancedBackupSetting")
    def put_advanced_backup_setting(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BackupPlanAdvancedBackupSetting", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed654e5c5419217531cc204e2489847f1450407f7a7cee980ba1726371ca739c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdvancedBackupSetting", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BackupPlanRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e626e532352ca2bee3c9c4886744a2a8b2cf582cd2ef90d43413f5edd99854f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetAdvancedBackupSetting")
    def reset_advanced_backup_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedBackupSetting", []))

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
    @jsii.member(jsii_name="advancedBackupSetting")
    def advanced_backup_setting(self) -> "BackupPlanAdvancedBackupSettingList":
        return typing.cast("BackupPlanAdvancedBackupSettingList", jsii.get(self, "advancedBackupSetting"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "BackupPlanRuleList":
        return typing.cast("BackupPlanRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="advancedBackupSettingInput")
    def advanced_backup_setting_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanAdvancedBackupSetting"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanAdvancedBackupSetting"]]], jsii.get(self, "advancedBackupSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanRule"]]], jsii.get(self, "ruleInput"))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ff3f9a43b0c2d3c0c363b47e8414eb56587d02b178e8cf2196022b591583d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f06639f3e77f6722b47e273e3325c49c07f202b10f789333eacc2ef95254d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3cae99eb188039e17565d0ae78031d1758b210181591bf604cad91ca35febab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__290ea2748fc669cca2657d649e6d95234f0f1cb37c1422451cca4451c1aeb775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.backupPlan.BackupPlanAdvancedBackupSetting",
    jsii_struct_bases=[],
    name_mapping={"backup_options": "backupOptions", "resource_type": "resourceType"},
)
class BackupPlanAdvancedBackupSetting:
    def __init__(
        self,
        *,
        backup_options: typing.Mapping[builtins.str, builtins.str],
        resource_type: builtins.str,
    ) -> None:
        '''
        :param backup_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#backup_options BackupPlan#backup_options}.
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#resource_type BackupPlan#resource_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eef6470ed6a2fb31b17bb4fcd7178ec721e7dba656085c85b96b1c0eff2bd1b)
            check_type(argname="argument backup_options", value=backup_options, expected_type=type_hints["backup_options"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_options": backup_options,
            "resource_type": resource_type,
        }

    @builtins.property
    def backup_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#backup_options BackupPlan#backup_options}.'''
        result = self._values.get("backup_options")
        assert result is not None, "Required property 'backup_options' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#resource_type BackupPlan#resource_type}.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanAdvancedBackupSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPlanAdvancedBackupSettingList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanAdvancedBackupSettingList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35eaf969822424b1e520fe4ffdf08922d3b5db98cc92933ee2b2326b23440e43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BackupPlanAdvancedBackupSettingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01997e1c2a64c71c6daf69ae2702c26588cfa53e070453da8ec6bdcca343562)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BackupPlanAdvancedBackupSettingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dde01a1c22db9f91df911a4c4335506be6214b853f0dc59f7d9f06ca188452a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07bdcb1c3d37f2dca2fcd3f1f21209ec3f22fcbd2106a071948aa4ed30f345a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f93b0cd965a487d4a2edb161dbde91e1df9c96d769238439912dcef67e83520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanAdvancedBackupSetting]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanAdvancedBackupSetting]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanAdvancedBackupSetting]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20b4b1eff3430574a6319af83ff36839a40b439c934fbea768278b550f9b80fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPlanAdvancedBackupSettingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanAdvancedBackupSettingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fa4af84f6df0fb25c07da8f6a3bf0b4d1559421e77d9f96083c099635d28e2d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="backupOptionsInput")
    def backup_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "backupOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="backupOptions")
    def backup_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "backupOptions"))

    @backup_options.setter
    def backup_options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9706722a4463b8e6699527bdf97c420cad6a6286528ba7204d3c9e5309e07b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupOptions", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9473617d45a2262c4508c4261eb94bc45b0528f46a4cee76eeeb9418f40d2c30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BackupPlanAdvancedBackupSetting, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BackupPlanAdvancedBackupSetting, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BackupPlanAdvancedBackupSetting, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a988302bb29923339b4d5c67d9670850695dfb7487773e3463e22ed6dc214ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.backupPlan.BackupPlanConfig",
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
        "rule": "rule",
        "advanced_backup_setting": "advancedBackupSetting",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class BackupPlanConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BackupPlanRule", typing.Dict[builtins.str, typing.Any]]]],
        advanced_backup_setting: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanAdvancedBackupSetting, typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#name BackupPlan#name}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#rule BackupPlan#rule}
        :param advanced_backup_setting: advanced_backup_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#advanced_backup_setting BackupPlan#advanced_backup_setting}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#id BackupPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#tags BackupPlan#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#tags_all BackupPlan#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab5e334d1693131b140308b118e29817b0ee09b70092c0610b1e9f247e92e54)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument advanced_backup_setting", value=advanced_backup_setting, expected_type=type_hints["advanced_backup_setting"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rule": rule,
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
        if advanced_backup_setting is not None:
            self._values["advanced_backup_setting"] = advanced_backup_setting
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#name BackupPlan#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#rule BackupPlan#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanRule"]], result)

    @builtins.property
    def advanced_backup_setting(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanAdvancedBackupSetting]]]:
        '''advanced_backup_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#advanced_backup_setting BackupPlan#advanced_backup_setting}
        '''
        result = self._values.get("advanced_backup_setting")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanAdvancedBackupSetting]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#id BackupPlan#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#tags BackupPlan#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#tags_all BackupPlan#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.backupPlan.BackupPlanRule",
    jsii_struct_bases=[],
    name_mapping={
        "rule_name": "ruleName",
        "target_vault_name": "targetVaultName",
        "completion_window": "completionWindow",
        "copy_action": "copyAction",
        "enable_continuous_backup": "enableContinuousBackup",
        "lifecycle": "lifecycle",
        "recovery_point_tags": "recoveryPointTags",
        "schedule": "schedule",
        "start_window": "startWindow",
    },
)
class BackupPlanRule:
    def __init__(
        self,
        *,
        rule_name: builtins.str,
        target_vault_name: builtins.str,
        completion_window: typing.Optional[jsii.Number] = None,
        copy_action: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BackupPlanRuleCopyAction", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable_continuous_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        lifecycle: typing.Optional[typing.Union["BackupPlanRuleLifecycle", typing.Dict[builtins.str, typing.Any]]] = None,
        recovery_point_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        schedule: typing.Optional[builtins.str] = None,
        start_window: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param rule_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#rule_name BackupPlan#rule_name}.
        :param target_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#target_vault_name BackupPlan#target_vault_name}.
        :param completion_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#completion_window BackupPlan#completion_window}.
        :param copy_action: copy_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#copy_action BackupPlan#copy_action}
        :param enable_continuous_backup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#enable_continuous_backup BackupPlan#enable_continuous_backup}.
        :param lifecycle: lifecycle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#lifecycle BackupPlan#lifecycle}
        :param recovery_point_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#recovery_point_tags BackupPlan#recovery_point_tags}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#schedule BackupPlan#schedule}.
        :param start_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#start_window BackupPlan#start_window}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = BackupPlanRuleLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bd8852db719f442f8383705e45c0c802f32e6c4c7e8a7f22f84045456ebec42)
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument target_vault_name", value=target_vault_name, expected_type=type_hints["target_vault_name"])
            check_type(argname="argument completion_window", value=completion_window, expected_type=type_hints["completion_window"])
            check_type(argname="argument copy_action", value=copy_action, expected_type=type_hints["copy_action"])
            check_type(argname="argument enable_continuous_backup", value=enable_continuous_backup, expected_type=type_hints["enable_continuous_backup"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument recovery_point_tags", value=recovery_point_tags, expected_type=type_hints["recovery_point_tags"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument start_window", value=start_window, expected_type=type_hints["start_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_name": rule_name,
            "target_vault_name": target_vault_name,
        }
        if completion_window is not None:
            self._values["completion_window"] = completion_window
        if copy_action is not None:
            self._values["copy_action"] = copy_action
        if enable_continuous_backup is not None:
            self._values["enable_continuous_backup"] = enable_continuous_backup
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if recovery_point_tags is not None:
            self._values["recovery_point_tags"] = recovery_point_tags
        if schedule is not None:
            self._values["schedule"] = schedule
        if start_window is not None:
            self._values["start_window"] = start_window

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#rule_name BackupPlan#rule_name}.'''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_vault_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#target_vault_name BackupPlan#target_vault_name}.'''
        result = self._values.get("target_vault_name")
        assert result is not None, "Required property 'target_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def completion_window(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#completion_window BackupPlan#completion_window}.'''
        result = self._values.get("completion_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def copy_action(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanRuleCopyAction"]]]:
        '''copy_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#copy_action BackupPlan#copy_action}
        '''
        result = self._values.get("copy_action")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BackupPlanRuleCopyAction"]]], result)

    @builtins.property
    def enable_continuous_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#enable_continuous_backup BackupPlan#enable_continuous_backup}.'''
        result = self._values.get("enable_continuous_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional["BackupPlanRuleLifecycle"]:
        '''lifecycle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#lifecycle BackupPlan#lifecycle}
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional["BackupPlanRuleLifecycle"], result)

    @builtins.property
    def recovery_point_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#recovery_point_tags BackupPlan#recovery_point_tags}.'''
        result = self._values.get("recovery_point_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#schedule BackupPlan#schedule}.'''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_window(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#start_window BackupPlan#start_window}.'''
        result = self._values.get("start_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.backupPlan.BackupPlanRuleCopyAction",
    jsii_struct_bases=[],
    name_mapping={
        "destination_vault_arn": "destinationVaultArn",
        "lifecycle": "lifecycle",
    },
)
class BackupPlanRuleCopyAction:
    def __init__(
        self,
        *,
        destination_vault_arn: builtins.str,
        lifecycle: typing.Optional[typing.Union["BackupPlanRuleCopyActionLifecycle", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_vault_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#destination_vault_arn BackupPlan#destination_vault_arn}.
        :param lifecycle: lifecycle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#lifecycle BackupPlan#lifecycle}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = BackupPlanRuleCopyActionLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49f41f8e43dd788f34b7f1d1d3811c07323dae3b864b75071bc599ecb7abff69)
            check_type(argname="argument destination_vault_arn", value=destination_vault_arn, expected_type=type_hints["destination_vault_arn"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_vault_arn": destination_vault_arn,
        }
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle

    @builtins.property
    def destination_vault_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#destination_vault_arn BackupPlan#destination_vault_arn}.'''
        result = self._values.get("destination_vault_arn")
        assert result is not None, "Required property 'destination_vault_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifecycle(self) -> typing.Optional["BackupPlanRuleCopyActionLifecycle"]:
        '''lifecycle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#lifecycle BackupPlan#lifecycle}
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional["BackupPlanRuleCopyActionLifecycle"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanRuleCopyAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.backupPlan.BackupPlanRuleCopyActionLifecycle",
    jsii_struct_bases=[],
    name_mapping={
        "cold_storage_after": "coldStorageAfter",
        "delete_after": "deleteAfter",
    },
)
class BackupPlanRuleCopyActionLifecycle:
    def __init__(
        self,
        *,
        cold_storage_after: typing.Optional[jsii.Number] = None,
        delete_after: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cold_storage_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#cold_storage_after BackupPlan#cold_storage_after}.
        :param delete_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#delete_after BackupPlan#delete_after}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6498646ceb1aa141debfa65be13e84305863ed1b15cb357e6a6ff225139f46ca)
            check_type(argname="argument cold_storage_after", value=cold_storage_after, expected_type=type_hints["cold_storage_after"])
            check_type(argname="argument delete_after", value=delete_after, expected_type=type_hints["delete_after"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cold_storage_after is not None:
            self._values["cold_storage_after"] = cold_storage_after
        if delete_after is not None:
            self._values["delete_after"] = delete_after

    @builtins.property
    def cold_storage_after(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#cold_storage_after BackupPlan#cold_storage_after}.'''
        result = self._values.get("cold_storage_after")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delete_after(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#delete_after BackupPlan#delete_after}.'''
        result = self._values.get("delete_after")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanRuleCopyActionLifecycle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPlanRuleCopyActionLifecycleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanRuleCopyActionLifecycleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__044204704a4722d44a98a473a0ed95b4e7d89252204d8707204925f6cd728871)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetColdStorageAfter")
    def reset_cold_storage_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColdStorageAfter", []))

    @jsii.member(jsii_name="resetDeleteAfter")
    def reset_delete_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAfter", []))

    @builtins.property
    @jsii.member(jsii_name="coldStorageAfterInput")
    def cold_storage_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coldStorageAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterInput")
    def delete_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="coldStorageAfter")
    def cold_storage_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coldStorageAfter"))

    @cold_storage_after.setter
    def cold_storage_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c35c723750b90726d094f4277f107b94b37a310486dc372c8754fa584192d7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coldStorageAfter", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAfter")
    def delete_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAfter"))

    @delete_after.setter
    def delete_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52c30835d840188a326d8003996a705b5f0142e18d1b6f45d73788d7148eba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAfter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPlanRuleCopyActionLifecycle]:
        return typing.cast(typing.Optional[BackupPlanRuleCopyActionLifecycle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPlanRuleCopyActionLifecycle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bda5c93e5ac40379e7052e56a15fdf8d52197aff11acc9569a5ed28c30b443b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPlanRuleCopyActionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanRuleCopyActionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a41e83bd980cf374c86268ec4e43a9d9720f1315c7cccb2ed1362979730d244)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BackupPlanRuleCopyActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33811241eafa9f9673da12babf8abf675a89da5682daf21c0cd11906bdd44ff6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BackupPlanRuleCopyActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b89b0649fa2adaf69227c0e6b14e2c9f5394fdaa6881a603d7d8eac35f1f20)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f97c71ee15715dc55d94c1da64e12e4ccba6677e716715a1286c86c2578c9f0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db15707ae3b755ed6c146cf1c756e6697a5764980170dda8698f5b9baed58106)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRuleCopyAction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRuleCopyAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRuleCopyAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e1d0027670e8f100cec2a9f337b4265d2ceed926dd9e8e6b152d591bdb9d26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPlanRuleCopyActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanRuleCopyActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc9470b8f9ef753e8c4dbcb39d03963b2282fe7f67426e2c805d05adc086ca9c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLifecycle")
    def put_lifecycle(
        self,
        *,
        cold_storage_after: typing.Optional[jsii.Number] = None,
        delete_after: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cold_storage_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#cold_storage_after BackupPlan#cold_storage_after}.
        :param delete_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#delete_after BackupPlan#delete_after}.
        '''
        value = BackupPlanRuleCopyActionLifecycle(
            cold_storage_after=cold_storage_after, delete_after=delete_after
        )

        return typing.cast(None, jsii.invoke(self, "putLifecycle", [value]))

    @jsii.member(jsii_name="resetLifecycle")
    def reset_lifecycle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycle", []))

    @builtins.property
    @jsii.member(jsii_name="lifecycle")
    def lifecycle(self) -> BackupPlanRuleCopyActionLifecycleOutputReference:
        return typing.cast(BackupPlanRuleCopyActionLifecycleOutputReference, jsii.get(self, "lifecycle"))

    @builtins.property
    @jsii.member(jsii_name="destinationVaultArnInput")
    def destination_vault_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationVaultArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleInput")
    def lifecycle_input(self) -> typing.Optional[BackupPlanRuleCopyActionLifecycle]:
        return typing.cast(typing.Optional[BackupPlanRuleCopyActionLifecycle], jsii.get(self, "lifecycleInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationVaultArn")
    def destination_vault_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationVaultArn"))

    @destination_vault_arn.setter
    def destination_vault_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b307d90f1f10359bf40f5ec0c005cb9fb1cbf940be09cd8307e5a7868f8e5e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationVaultArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BackupPlanRuleCopyAction, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BackupPlanRuleCopyAction, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BackupPlanRuleCopyAction, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d55645e0ffb69f96a371069189563321b72ddcc9503108dd2814a46eade0a6f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.backupPlan.BackupPlanRuleLifecycle",
    jsii_struct_bases=[],
    name_mapping={
        "cold_storage_after": "coldStorageAfter",
        "delete_after": "deleteAfter",
    },
)
class BackupPlanRuleLifecycle:
    def __init__(
        self,
        *,
        cold_storage_after: typing.Optional[jsii.Number] = None,
        delete_after: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cold_storage_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#cold_storage_after BackupPlan#cold_storage_after}.
        :param delete_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#delete_after BackupPlan#delete_after}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4ce6bf0352cf35ee13f44850c23564e360c4a45f1391e8ccbcea0d10067cd3e)
            check_type(argname="argument cold_storage_after", value=cold_storage_after, expected_type=type_hints["cold_storage_after"])
            check_type(argname="argument delete_after", value=delete_after, expected_type=type_hints["delete_after"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cold_storage_after is not None:
            self._values["cold_storage_after"] = cold_storage_after
        if delete_after is not None:
            self._values["delete_after"] = delete_after

    @builtins.property
    def cold_storage_after(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#cold_storage_after BackupPlan#cold_storage_after}.'''
        result = self._values.get("cold_storage_after")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delete_after(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#delete_after BackupPlan#delete_after}.'''
        result = self._values.get("delete_after")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanRuleLifecycle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPlanRuleLifecycleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanRuleLifecycleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92710c55a0af78041b9bf52ddab387c9900df60f28e33f1a99d33c2d71a3734e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetColdStorageAfter")
    def reset_cold_storage_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColdStorageAfter", []))

    @jsii.member(jsii_name="resetDeleteAfter")
    def reset_delete_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAfter", []))

    @builtins.property
    @jsii.member(jsii_name="coldStorageAfterInput")
    def cold_storage_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "coldStorageAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAfterInput")
    def delete_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="coldStorageAfter")
    def cold_storage_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "coldStorageAfter"))

    @cold_storage_after.setter
    def cold_storage_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ca499588062ce4df736547c2f2480053059e7e750069833428e8b293db4cfda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coldStorageAfter", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAfter")
    def delete_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAfter"))

    @delete_after.setter
    def delete_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d537065facd0e283afebb76db238d82b39c24416061ba4bac21861fbf1094b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAfter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPlanRuleLifecycle]:
        return typing.cast(typing.Optional[BackupPlanRuleLifecycle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BackupPlanRuleLifecycle]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e14016dde728442b48e4e6a2a9f5c601c458c885910fe1da7b88c52bcb9cee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPlanRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ffbd53b07c3d37f21d72f834f83df5d92cd50767d813f7523bd098072ba58e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BackupPlanRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104c142d71267f0037aba4f2f18d3e37acec319430878a13388e3a7a4744db4b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BackupPlanRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1df7227e798b93c0b4eeb31de6d37645c0ee797f0d1c95fccfc1b8a8b93e709)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4da22cd4289d6f334746f66c88c4b84a433be445bb6536afd6bf8e4e9294de23)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ba9764ca9b370a7d4af43860d948a174af4962bbaf69ecb563f424a5683f903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d2e4ebd5988d5d6d612d0cec8145d4c9a359da0f78832894ee851534fee3af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPlanRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.backupPlan.BackupPlanRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9c40a6f4fb9200ca43dac0aa5894396be15c1e96e90bc4b0bc88ca3500b99c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCopyAction")
    def put_copy_action(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanRuleCopyAction, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__809a28f31525f6c65b482f670ab447353d84add41ef53f203d18f0485961b2ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCopyAction", [value]))

    @jsii.member(jsii_name="putLifecycle")
    def put_lifecycle(
        self,
        *,
        cold_storage_after: typing.Optional[jsii.Number] = None,
        delete_after: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cold_storage_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#cold_storage_after BackupPlan#cold_storage_after}.
        :param delete_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/backup_plan#delete_after BackupPlan#delete_after}.
        '''
        value = BackupPlanRuleLifecycle(
            cold_storage_after=cold_storage_after, delete_after=delete_after
        )

        return typing.cast(None, jsii.invoke(self, "putLifecycle", [value]))

    @jsii.member(jsii_name="resetCompletionWindow")
    def reset_completion_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompletionWindow", []))

    @jsii.member(jsii_name="resetCopyAction")
    def reset_copy_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyAction", []))

    @jsii.member(jsii_name="resetEnableContinuousBackup")
    def reset_enable_continuous_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableContinuousBackup", []))

    @jsii.member(jsii_name="resetLifecycle")
    def reset_lifecycle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycle", []))

    @jsii.member(jsii_name="resetRecoveryPointTags")
    def reset_recovery_point_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryPointTags", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetStartWindow")
    def reset_start_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartWindow", []))

    @builtins.property
    @jsii.member(jsii_name="copyAction")
    def copy_action(self) -> BackupPlanRuleCopyActionList:
        return typing.cast(BackupPlanRuleCopyActionList, jsii.get(self, "copyAction"))

    @builtins.property
    @jsii.member(jsii_name="lifecycle")
    def lifecycle(self) -> BackupPlanRuleLifecycleOutputReference:
        return typing.cast(BackupPlanRuleLifecycleOutputReference, jsii.get(self, "lifecycle"))

    @builtins.property
    @jsii.member(jsii_name="completionWindowInput")
    def completion_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "completionWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="copyActionInput")
    def copy_action_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRuleCopyAction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRuleCopyAction]]], jsii.get(self, "copyActionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableContinuousBackupInput")
    def enable_continuous_backup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableContinuousBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleInput")
    def lifecycle_input(self) -> typing.Optional[BackupPlanRuleLifecycle]:
        return typing.cast(typing.Optional[BackupPlanRuleLifecycle], jsii.get(self, "lifecycleInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryPointTagsInput")
    def recovery_point_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "recoveryPointTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleNameInput")
    def rule_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="startWindowInput")
    def start_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="targetVaultNameInput")
    def target_vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetVaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="completionWindow")
    def completion_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "completionWindow"))

    @completion_window.setter
    def completion_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4023ea3c50a268f8dbfbc6011b3e52a81a1f3b1f72af160a27f98cb308b8615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "completionWindow", value)

    @builtins.property
    @jsii.member(jsii_name="enableContinuousBackup")
    def enable_continuous_backup(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableContinuousBackup"))

    @enable_continuous_backup.setter
    def enable_continuous_backup(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df89c612184d52f1ac1882c4da3cdd99a589b71836ef9e43787daa7abdba6961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableContinuousBackup", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryPointTags")
    def recovery_point_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "recoveryPointTags"))

    @recovery_point_tags.setter
    def recovery_point_tags(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94ebbb72e0832149078192275096215c89a6fe535183924cda0c7f92e12cf321)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryPointTags", value)

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53fddd2a17ae573d9a4365daaf949db5638b159bd7c0a0052acf009d619dae35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5d18be6c51724260c0a7d77fda489a817850d3972f1c181217b1e715efb34fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="startWindow")
    def start_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startWindow"))

    @start_window.setter
    def start_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795bd0bff647501ab91283398b4059470360e1eb9bf6760435baa5ad49440951)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startWindow", value)

    @builtins.property
    @jsii.member(jsii_name="targetVaultName")
    def target_vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetVaultName"))

    @target_vault_name.setter
    def target_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fbf39ccd849602bd7b7163b6306b9a68ed5122e0186ce940f0dbc7d1de79b76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BackupPlanRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BackupPlanRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BackupPlanRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__177055cb45e158575273d080a4ee97ae0fcf916f11909128a099f1da286829fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BackupPlan",
    "BackupPlanAdvancedBackupSetting",
    "BackupPlanAdvancedBackupSettingList",
    "BackupPlanAdvancedBackupSettingOutputReference",
    "BackupPlanConfig",
    "BackupPlanRule",
    "BackupPlanRuleCopyAction",
    "BackupPlanRuleCopyActionLifecycle",
    "BackupPlanRuleCopyActionLifecycleOutputReference",
    "BackupPlanRuleCopyActionList",
    "BackupPlanRuleCopyActionOutputReference",
    "BackupPlanRuleLifecycle",
    "BackupPlanRuleLifecycleOutputReference",
    "BackupPlanRuleList",
    "BackupPlanRuleOutputReference",
]

publication.publish()

def _typecheckingstub__8935ca17e17be88a1ae73397f59bccb1a4d6338f6c7072da81dfb52e5dc14c8e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanRule, typing.Dict[builtins.str, typing.Any]]]],
    advanced_backup_setting: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanAdvancedBackupSetting, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__ed654e5c5419217531cc204e2489847f1450407f7a7cee980ba1726371ca739c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanAdvancedBackupSetting, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e626e532352ca2bee3c9c4886744a2a8b2cf582cd2ef90d43413f5edd99854f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ff3f9a43b0c2d3c0c363b47e8414eb56587d02b178e8cf2196022b591583d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f06639f3e77f6722b47e273e3325c49c07f202b10f789333eacc2ef95254d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3cae99eb188039e17565d0ae78031d1758b210181591bf604cad91ca35febab(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__290ea2748fc669cca2657d649e6d95234f0f1cb37c1422451cca4451c1aeb775(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eef6470ed6a2fb31b17bb4fcd7178ec721e7dba656085c85b96b1c0eff2bd1b(
    *,
    backup_options: typing.Mapping[builtins.str, builtins.str],
    resource_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35eaf969822424b1e520fe4ffdf08922d3b5db98cc92933ee2b2326b23440e43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01997e1c2a64c71c6daf69ae2702c26588cfa53e070453da8ec6bdcca343562(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dde01a1c22db9f91df911a4c4335506be6214b853f0dc59f7d9f06ca188452a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07bdcb1c3d37f2dca2fcd3f1f21209ec3f22fcbd2106a071948aa4ed30f345a2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f93b0cd965a487d4a2edb161dbde91e1df9c96d769238439912dcef67e83520(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20b4b1eff3430574a6319af83ff36839a40b439c934fbea768278b550f9b80fc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanAdvancedBackupSetting]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa4af84f6df0fb25c07da8f6a3bf0b4d1559421e77d9f96083c099635d28e2d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9706722a4463b8e6699527bdf97c420cad6a6286528ba7204d3c9e5309e07b1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9473617d45a2262c4508c4261eb94bc45b0528f46a4cee76eeeb9418f40d2c30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a988302bb29923339b4d5c67d9670850695dfb7487773e3463e22ed6dc214ff(
    value: typing.Optional[typing.Union[BackupPlanAdvancedBackupSetting, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab5e334d1693131b140308b118e29817b0ee09b70092c0610b1e9f247e92e54(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanRule, typing.Dict[builtins.str, typing.Any]]]],
    advanced_backup_setting: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanAdvancedBackupSetting, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd8852db719f442f8383705e45c0c802f32e6c4c7e8a7f22f84045456ebec42(
    *,
    rule_name: builtins.str,
    target_vault_name: builtins.str,
    completion_window: typing.Optional[jsii.Number] = None,
    copy_action: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanRuleCopyAction, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enable_continuous_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    lifecycle: typing.Optional[typing.Union[BackupPlanRuleLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    recovery_point_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    schedule: typing.Optional[builtins.str] = None,
    start_window: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f41f8e43dd788f34b7f1d1d3811c07323dae3b864b75071bc599ecb7abff69(
    *,
    destination_vault_arn: builtins.str,
    lifecycle: typing.Optional[typing.Union[BackupPlanRuleCopyActionLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6498646ceb1aa141debfa65be13e84305863ed1b15cb357e6a6ff225139f46ca(
    *,
    cold_storage_after: typing.Optional[jsii.Number] = None,
    delete_after: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044204704a4722d44a98a473a0ed95b4e7d89252204d8707204925f6cd728871(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c35c723750b90726d094f4277f107b94b37a310486dc372c8754fa584192d7b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52c30835d840188a326d8003996a705b5f0142e18d1b6f45d73788d7148eba5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda5c93e5ac40379e7052e56a15fdf8d52197aff11acc9569a5ed28c30b443b3(
    value: typing.Optional[BackupPlanRuleCopyActionLifecycle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a41e83bd980cf374c86268ec4e43a9d9720f1315c7cccb2ed1362979730d244(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33811241eafa9f9673da12babf8abf675a89da5682daf21c0cd11906bdd44ff6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b89b0649fa2adaf69227c0e6b14e2c9f5394fdaa6881a603d7d8eac35f1f20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f97c71ee15715dc55d94c1da64e12e4ccba6677e716715a1286c86c2578c9f0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db15707ae3b755ed6c146cf1c756e6697a5764980170dda8698f5b9baed58106(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e1d0027670e8f100cec2a9f337b4265d2ceed926dd9e8e6b152d591bdb9d26(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRuleCopyAction]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc9470b8f9ef753e8c4dbcb39d03963b2282fe7f67426e2c805d05adc086ca9c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b307d90f1f10359bf40f5ec0c005cb9fb1cbf940be09cd8307e5a7868f8e5e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55645e0ffb69f96a371069189563321b72ddcc9503108dd2814a46eade0a6f1(
    value: typing.Optional[typing.Union[BackupPlanRuleCopyAction, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ce6bf0352cf35ee13f44850c23564e360c4a45f1391e8ccbcea0d10067cd3e(
    *,
    cold_storage_after: typing.Optional[jsii.Number] = None,
    delete_after: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92710c55a0af78041b9bf52ddab387c9900df60f28e33f1a99d33c2d71a3734e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ca499588062ce4df736547c2f2480053059e7e750069833428e8b293db4cfda(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d537065facd0e283afebb76db238d82b39c24416061ba4bac21861fbf1094b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e14016dde728442b48e4e6a2a9f5c601c458c885910fe1da7b88c52bcb9cee(
    value: typing.Optional[BackupPlanRuleLifecycle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ffbd53b07c3d37f21d72f834f83df5d92cd50767d813f7523bd098072ba58e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104c142d71267f0037aba4f2f18d3e37acec319430878a13388e3a7a4744db4b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1df7227e798b93c0b4eeb31de6d37645c0ee797f0d1c95fccfc1b8a8b93e709(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da22cd4289d6f334746f66c88c4b84a433be445bb6536afd6bf8e4e9294de23(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba9764ca9b370a7d4af43860d948a174af4962bbaf69ecb563f424a5683f903(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d2e4ebd5988d5d6d612d0cec8145d4c9a359da0f78832894ee851534fee3af(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BackupPlanRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9c40a6f4fb9200ca43dac0aa5894396be15c1e96e90bc4b0bc88ca3500b99c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809a28f31525f6c65b482f670ab447353d84add41ef53f203d18f0485961b2ed(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BackupPlanRuleCopyAction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4023ea3c50a268f8dbfbc6011b3e52a81a1f3b1f72af160a27f98cb308b8615(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df89c612184d52f1ac1882c4da3cdd99a589b71836ef9e43787daa7abdba6961(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94ebbb72e0832149078192275096215c89a6fe535183924cda0c7f92e12cf321(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fddd2a17ae573d9a4365daaf949db5638b159bd7c0a0052acf009d619dae35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5d18be6c51724260c0a7d77fda489a817850d3972f1c181217b1e715efb34fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795bd0bff647501ab91283398b4059470360e1eb9bf6760435baa5ad49440951(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbf39ccd849602bd7b7163b6306b9a68ed5122e0186ce940f0dbc7d1de79b76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__177055cb45e158575273d080a4ee97ae0fcf916f11909128a099f1da286829fe(
    value: typing.Optional[typing.Union[BackupPlanRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
