'''
# `aws_ce_cost_category`

Refer to the Terraform Registory for docs: [`aws_ce_cost_category`](https://www.terraform.io/docs/providers/aws/r/ce_cost_category).
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


class CeCostCategory(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategory",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category aws_ce_cost_category}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRule", typing.Dict[builtins.str, typing.Any]]]],
        rule_version: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        effective_start: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        split_charge_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category aws_ce_cost_category} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#name CeCostCategory#name}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        :param rule_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule_version CeCostCategory#rule_version}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#default_value CeCostCategory#default_value}.
        :param effective_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#effective_start CeCostCategory#effective_start}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#id CeCostCategory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param split_charge_rule: split_charge_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#split_charge_rule CeCostCategory#split_charge_rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags_all CeCostCategory#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75440b9b75c64b278b60fa88506ddf52a78638e2efc77590d9eefa91efa60fa0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CeCostCategoryConfig(
            name=name,
            rule=rule,
            rule_version=rule_version,
            default_value=default_value,
            effective_start=effective_start,
            id=id,
            split_charge_rule=split_charge_rule,
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

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__255f55aa1e3a853e33467c04c1d3853dbe033af998923800b1b17a91f355180d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putSplitChargeRule")
    def put_split_charge_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e13ae21294b769a7836a99c4e27316e93b6a5edbfc189c2a6ee2ae1b7f6acf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSplitChargeRule", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetEffectiveStart")
    def reset_effective_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffectiveStart", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSplitChargeRule")
    def reset_split_charge_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplitChargeRule", []))

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
    @jsii.member(jsii_name="effectiveEnd")
    def effective_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveEnd"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "CeCostCategoryRuleList":
        return typing.cast("CeCostCategoryRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="splitChargeRule")
    def split_charge_rule(self) -> "CeCostCategorySplitChargeRuleList":
        return typing.cast("CeCostCategorySplitChargeRuleList", jsii.get(self, "splitChargeRule"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="effectiveStartInput")
    def effective_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectiveStartInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleVersionInput")
    def rule_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="splitChargeRuleInput")
    def split_charge_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]], jsii.get(self, "splitChargeRuleInput"))

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
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48dd229f6608b337d1dad09fa5dcd5c96f12460a6acc47c3858932f801af5731)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="effectiveStart")
    def effective_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveStart"))

    @effective_start.setter
    def effective_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f5c39e7527ad6612b8f0acc6104926770ab37b49b8f4c239a0559bcca87d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effectiveStart", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74090bf9825f10058475a7721564298c69ee99421ffecc1e22550427b5ba13ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ddb9b061fc93be1b31d408fab187b3b54d4e4ffa18d158fcb34452f91d5b606)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleVersion")
    def rule_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleVersion"))

    @rule_version.setter
    def rule_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08909c3a57fa51768a2176cfb23e6fcc063dd6c975829af70970d0b8774562c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90307086384b2ea8d3135c1f2ce6ac7098157bc8c24c7654561def2146a724a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c46732361d523bb8efad4fd899a48f2d6712bc83c70112bdc5b1ae6d7e53f911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryConfig",
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
        "rule_version": "ruleVersion",
        "default_value": "defaultValue",
        "effective_start": "effectiveStart",
        "id": "id",
        "split_charge_rule": "splitChargeRule",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CeCostCategoryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRule", typing.Dict[builtins.str, typing.Any]]]],
        rule_version: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        effective_start: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        split_charge_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#name CeCostCategory#name}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        :param rule_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule_version CeCostCategory#rule_version}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#default_value CeCostCategory#default_value}.
        :param effective_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#effective_start CeCostCategory#effective_start}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#id CeCostCategory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param split_charge_rule: split_charge_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#split_charge_rule CeCostCategory#split_charge_rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags_all CeCostCategory#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0987c02944a20f9724b79b26e9eba1ca3d64f81ac5bc77ea23fc4607c0a714dc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_version", value=rule_version, expected_type=type_hints["rule_version"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument effective_start", value=effective_start, expected_type=type_hints["effective_start"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument split_charge_rule", value=split_charge_rule, expected_type=type_hints["split_charge_rule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rule": rule,
            "rule_version": rule_version,
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
        if default_value is not None:
            self._values["default_value"] = default_value
        if effective_start is not None:
            self._values["effective_start"] = effective_start
        if id is not None:
            self._values["id"] = id
        if split_charge_rule is not None:
            self._values["split_charge_rule"] = split_charge_rule
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#name CeCostCategory#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRule"]], result)

    @builtins.property
    def rule_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule_version CeCostCategory#rule_version}.'''
        result = self._values.get("rule_version")
        assert result is not None, "Required property 'rule_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#default_value CeCostCategory#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def effective_start(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#effective_start CeCostCategory#effective_start}.'''
        result = self._values.get("effective_start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#id CeCostCategory#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def split_charge_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]]:
        '''split_charge_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#split_charge_rule CeCostCategory#split_charge_rule}
        '''
        result = self._values.get("split_charge_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags_all CeCostCategory#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRule",
    jsii_struct_bases=[],
    name_mapping={
        "inherited_value": "inheritedValue",
        "rule": "rule",
        "type": "type",
        "value": "value",
    },
)
class CeCostCategoryRule:
    def __init__(
        self,
        *,
        inherited_value: typing.Optional[typing.Union["CeCostCategoryRuleInheritedValue", typing.Dict[builtins.str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union["CeCostCategoryRuleRule", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inherited_value: inherited_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#inherited_value CeCostCategory#inherited_value}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#value CeCostCategory#value}.
        '''
        if isinstance(inherited_value, dict):
            inherited_value = CeCostCategoryRuleInheritedValue(**inherited_value)
        if isinstance(rule, dict):
            rule = CeCostCategoryRuleRule(**rule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66eca5690fce549362071095fd505f569ca4dd61a0dac063c6aae40ce8e8f44)
            check_type(argname="argument inherited_value", value=inherited_value, expected_type=type_hints["inherited_value"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inherited_value is not None:
            self._values["inherited_value"] = inherited_value
        if rule is not None:
            self._values["rule"] = rule
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def inherited_value(self) -> typing.Optional["CeCostCategoryRuleInheritedValue"]:
        '''inherited_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#inherited_value CeCostCategory#inherited_value}
        '''
        result = self._values.get("inherited_value")
        return typing.cast(typing.Optional["CeCostCategoryRuleInheritedValue"], result)

    @builtins.property
    def rule(self) -> typing.Optional["CeCostCategoryRuleRule"]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional["CeCostCategoryRuleRule"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#value CeCostCategory#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleInheritedValue",
    jsii_struct_bases=[],
    name_mapping={"dimension_key": "dimensionKey", "dimension_name": "dimensionName"},
)
class CeCostCategoryRuleInheritedValue:
    def __init__(
        self,
        *,
        dimension_key: typing.Optional[builtins.str] = None,
        dimension_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dimension_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_key CeCostCategory#dimension_key}.
        :param dimension_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_name CeCostCategory#dimension_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3e7b866516aaaa346d857c152b5190c207d4835c32db072982cd3f225861b6)
            check_type(argname="argument dimension_key", value=dimension_key, expected_type=type_hints["dimension_key"])
            check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dimension_key is not None:
            self._values["dimension_key"] = dimension_key
        if dimension_name is not None:
            self._values["dimension_name"] = dimension_name

    @builtins.property
    def dimension_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_key CeCostCategory#dimension_key}.'''
        result = self._values.get("dimension_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimension_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_name CeCostCategory#dimension_name}.'''
        result = self._values.get("dimension_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleInheritedValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleInheritedValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleInheritedValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c44b483451a1ed0966bb036b415837e4c17a4393add78918afed17c7205a3e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDimensionKey")
    def reset_dimension_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensionKey", []))

    @jsii.member(jsii_name="resetDimensionName")
    def reset_dimension_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensionName", []))

    @builtins.property
    @jsii.member(jsii_name="dimensionKeyInput")
    def dimension_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dimensionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionNameInput")
    def dimension_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dimensionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionKey")
    def dimension_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dimensionKey"))

    @dimension_key.setter
    def dimension_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47792e56a7ee49f508272b475d1020c0303a6678c2cab4c1b03939301c79f8ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensionKey", value)

    @builtins.property
    @jsii.member(jsii_name="dimensionName")
    def dimension_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dimensionName"))

    @dimension_name.setter
    def dimension_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5711601f15ebfc7dfd7d85b97cf23ffe0470f3aa6dc5cdd82f5665f4bb00239a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensionName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleInheritedValue]:
        return typing.cast(typing.Optional[CeCostCategoryRuleInheritedValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleInheritedValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e571b76f090f5ab1779d7f58d5b47612fd38006768b6cdda0fe8db2f8bb1275e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bb7ff5914e73f97eb237a6ace5d0398df8f9c3fbfd9ca2a4165f7d14c124ce6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CeCostCategoryRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d1826e6f6893646342b900a3d45cd049b0bdee62966a938f4b07a4f23ad38c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategoryRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc725f3d050d7b42f121447b3d87e6a2c432c475b9cb432d965be89f7e035334)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d986aba3ea6cc1cc23fa8655217eebed6690bfc683e7aa12938438a08aaeeb26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__76d21953f5f3f08d3c51740e0654f9628c0d303a57f45356b9ce7c991c74b82d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2943d8a987f5e31919ee3132625963d21b43e5f1a1005f9bd36ac5762a820802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__402660241b1360cbf785072b52fbfdc4c8e608672ee656122a5ff39d8729526d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putInheritedValue")
    def put_inherited_value(
        self,
        *,
        dimension_key: typing.Optional[builtins.str] = None,
        dimension_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dimension_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_key CeCostCategory#dimension_key}.
        :param dimension_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_name CeCostCategory#dimension_name}.
        '''
        value = CeCostCategoryRuleInheritedValue(
            dimension_key=dimension_key, dimension_name=dimension_name
        )

        return typing.cast(None, jsii.invoke(self, "putInheritedValue", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["CeCostCategoryRuleRuleNot", typing.Dict[builtins.str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleOr", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#and CeCostCategory#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#not CeCostCategory#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#or CeCostCategory#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        value = CeCostCategoryRuleRule(
            and_=and_,
            cost_category=cost_category,
            dimension=dimension,
            not_=not_,
            or_=or_,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetInheritedValue")
    def reset_inherited_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInheritedValue", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="inheritedValue")
    def inherited_value(self) -> CeCostCategoryRuleInheritedValueOutputReference:
        return typing.cast(CeCostCategoryRuleInheritedValueOutputReference, jsii.get(self, "inheritedValue"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "CeCostCategoryRuleRuleOutputReference":
        return typing.cast("CeCostCategoryRuleRuleOutputReference", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="inheritedValueInput")
    def inherited_value_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleInheritedValue]:
        return typing.cast(typing.Optional[CeCostCategoryRuleInheritedValue], jsii.get(self, "inheritedValueInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional["CeCostCategoryRuleRule"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRule"], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b4890af948022ecca63e7d82a0b8dd09c5578f6972eb65531b12049852d596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e89ee65125e1131c981190443311f67f52c814f45d140ccd49dca7c24ded448f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategoryRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategoryRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategoryRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5c35943bb206235f29af10942260e271280e01a6c2d4921a6d373b289fe7f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRule",
    jsii_struct_bases=[],
    name_mapping={
        "and_": "and",
        "cost_category": "costCategory",
        "dimension": "dimension",
        "not_": "not",
        "or_": "or",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRule:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleAnd", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["CeCostCategoryRuleRuleNot", typing.Dict[builtins.str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleOr", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#and CeCostCategory#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#not CeCostCategory#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#or CeCostCategory#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleDimension(**dimension)
        if isinstance(not_, dict):
            not_ = CeCostCategoryRuleRuleNot(**not_)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912a57c258203db0ba6f037134e265929a9d789f01b6795348a225c4df16cb01)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument not_", value=not_, expected_type=type_hints["not_"])
            check_type(argname="argument or_", value=or_, expected_type=type_hints["or_"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if not_ is not None:
            self._values["not_"] = not_
        if or_ is not None:
            self._values["or_"] = or_
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRuleRuleAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#and CeCostCategory#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRuleRuleAnd"]]], result)

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleDimension"], result)

    @builtins.property
    def not_(self) -> typing.Optional["CeCostCategoryRuleRuleNot"]:
        '''not block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#not CeCostCategory#not}
        '''
        result = self._values.get("not_")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNot"], result)

    @builtins.property
    def or_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRuleRuleOr"]]]:
        '''or block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#or CeCostCategory#or}
        '''
        result = self._values.get("or_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategoryRuleRuleOr"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAnd",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRuleAnd:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleAndCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleAndDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleAndTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleAndCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleAndDimension(**dimension)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleAndTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59445027adaaa7702bf5cebce72e266927f8b94a2f14433e5b50072ba601501)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleAndCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleAndDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleAndTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleAndCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646060cc742b20f9b83b0c6161fba479893378ac9f50f208b75fe17cefacecdc)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAndCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleAndCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndCostCategoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d8d558ce21fce9a4f316dbdd79faa3444ea48b09358d5cb9c4aaa0cc5dc5c71)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f96881e70e097f1543dc793dadedfbe4eb7595f236fe9ffceee72ab8e8006492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772d66731a24dc8d051fab8aed775964420d725b3da06ccdd1a8f534a356c691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eebdf7f2937558d2f64d6c1a328c3cd153ee5fd5c68e682413106eaff38be76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleAndCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleAndCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0173406281a410f09c6da440d1de1103de655bd72e0ec0a33e1fcf671550788d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleAndDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4c1702336d813b3f9442f50e646397fc7f935612d06bf041fea0146d3b9c92)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAndDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleAndDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__15098709c6bd92fa53eec8d3a597a6f15dbf551b15714b03abdccc3dd5e6f8dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__caf1fc4e677bc2224c5ddc932ede645e35622a13c11828ac3dab46a54b51711b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5fca66afee957afd7470f42323452d637af89890eae695303b40053c135c33b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0571792eb57d69296cb34a4a52e6f149e4b246f6ef7051f207ab1617ea50994e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleAndDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleAndDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c170dbced4a865c33215b3262bf443d0aab105839d2d3e0633fdef5a56424e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleAndList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2966deb7ff09c80f0ebe336627d73c7f5d3b6a8db99476601d4f439af4c8d178)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CeCostCategoryRuleRuleAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5530baf1be898481e31948370a94ad7b5e045383f065440af83335c6f59f364)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategoryRuleRuleAndOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1ca3987a0cf681b43fd11c87b7d9c71ba3203a993c12527211ce95159a8b4d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc9e6612d761da8797bf75d57cd0479d28c19bda61caa12809b8f536e6a97b48)
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
            type_hints = typing.get_type_hints(_typecheckingstub__afc0ef6bbcf70a207c8ac4bdd81bfc093b26e3c3a75a47d538042d4923e89c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7cdba877e69997bcaad98db2166b46d316d804bdedb86f76bcefa1547168f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleAndOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1edb39b837373e31d5765958d9bc449c3c71c2d866669213412f97074752013)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleAndCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleAndDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleAndTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleAndCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleAndCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleAndDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleAndDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleAndTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleAndTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleAndCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleAndDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleAndTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209bf8dc1348d1edbae538c3ab0beeead731bd4b8389409b59138a860acb0c77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleAndTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6155a7e9f575dfe5e3b80f779937bb2b961ebf44b8b4b53383df7f8ac12af5ae)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAndTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleAndTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleAndTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37ee162929ec95a8a9443bbcb6ea14444bdc2c129ad2d0de84264c412d838d7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d68faf093799c2a266157a110aaa48e01eb5a4fccf36feed503d601c2c03160e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d6df80e0ce2a0e01a4582fd75266fe793307ebb073b6e9aa7aefae55e361743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a599824da895759112d5e52a2b4d5bbc0d692dc8dab655cce9a712c945deba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleAndTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleAndTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c789d5aff6b259963c3bb39b411190591fc0cd5061343205d1780d5c1ec74ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8a2203aca46d423ba9e33da28ba0e97be4a0256fb03cbc6993f671a4952c21)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleCostCategoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84961cb6733f451a5dc42b5fdf24b39a17f968ca624f5abbeb471d71463a7d99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__872f1a049880486cfe40f53a178d6194858b76317cb0d707c3d446a53b6332c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__097540e46dbdcbe8e30f488c8d6c0a2e57a8d2e2ca068322cf6a7028c399d1d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffb92f3bedbc1c8fba7b59477f42f0cbb181aaa9b99e1bdc8812a936db3a34a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ccf235b0f4b0ecd4c7f11a94fef8c33ccd6ca1b0e67cf55b8d53c2424ceaaa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479c56eb7010e377300cd964328d2aaeb9c5d84bf2f5a22da16d9e26a029c31c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf9a2aa488d1eb645c2e37acf83791132958f055e7e0cf996fd68fc386a9e834)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__9271d89a6da4cf5ec46be9d5fab46365f925a5899d117f019060edffbcc90bf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1c17dcbe1ce0460cb79d07df06362422fb25b664eacce94ae5a692388de0c22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e444555680aa246a038d7030b7ef528313cbf712a22639f59faef3d940e2122f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af5883c7de1beca72dfc353bc7f79fadaa7a3b7ce789ec72a2f5a24270857a3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNot",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRuleNot:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleNotCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleNotDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleNotTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleNotCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleNotDimension(**dimension)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleNotTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__412b90cfb480431a3e15985be2b2b24e7022477ae17e3dd57979d675cecff8f9)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleNotCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleNotDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleNotTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleNotCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32ccb52a6494e690ce882c7aca33d971831d080f8515ac2bd8b2c1b298014e9)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNotCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleNotCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotCostCategoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f7369786cd10611608754cfa840aa8a2c5b3201e3a8a1f177bf7a18c1831f3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__79c9664bec92cacc1d869e73b7b15eb98afaa3d60746f2da0210dc9384669d5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c739b9047f267b651160b79aa3a0058c1e3ee67eef108ff8865cac11950571ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5acad114a74d2fcbb96886d03b22eb2f25649fe5a0e25ad96793560aea7b0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNotCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleNotCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789e408c423ae9ec789abb6d001ce9426bbaf36504e56e3038fa85ab4b054fb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleNotDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38570d38a6f71dee3ca5e9894ab9130b5479f8ea089bea827fc0f98452088d91)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNotDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleNotDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__614f0b86ac39aefdca5312f71fff9ee82b287cd0cc2fb65e143ffd6ab3bd23c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0ee9f45b3fdf7ad5523f8a24470561dc2904cebbc94312542b94a9a3baaffbb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9257124a9922eab25026f8ff5200f037b566f8e29a1c722934ca05e29fdbc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d84633605f7b82a14e9e5a84b1105893dec7687bb692da2dfd3e2db8338c020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNotDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleNotDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc420641543e02fe30193d58ea0b6caf396e3abe4af6e9329d1c4036bc0cf890)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleNotOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__508eb83b0d578179d322a4a6a075afd35cabb1ba113cf636e256aa26919e10be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleNotCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleNotDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleNotTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleNotCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleNotCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleNotDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleNotDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleNotTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleNotTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleNotCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleNotDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleNotTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNot]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CeCostCategoryRuleRuleNot]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dacb0e8533f409a628eb97d0bcbbc02af99d83cb8a8438024c6d5bd12eb221a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleNotTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bf8cd0eb64edf485ccdc301c36ff550aad44fbc0b36333e443beab2ad522cd0)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNotTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleNotTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleNotTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f5c62f0090551b1fb04010bf886a62863611194ef72962752ff600430b34c2c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__babc7ad603c744e8a6714a9cb66cfbcb60d86e794514ca979b092827b200edc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f3a182a3aed660e88aa9cc59380bf3e033677ebf7a87af404aa91b6a65cbcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b227f18a59e83e30802ba2e91549d4c60e95550320c5f6cc669b839cf8ce06c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNotTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleNotTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf499a6739c0fc6d3378118e21bb573983d338f7f669fb4537effeeb9296c915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOr",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRuleOr:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleOrCostCategory", typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleOrDimension", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleOrTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleOrCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleOrDimension(**dimension)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleOrTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a04bab51a39123d48e819f109448a5160655127c79d5c8b6ad987bec72a36c6)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleOrCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleOrDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleOrTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleOrCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78325c80846045a7f0ed5ab352fe4b1747141c383a3770e444174df9d954e281)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOrCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleOrCostCategoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrCostCategoryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__68ef0cf3facd9e44d0b8be100b1dd304378418931742401b0c7448169c96a3f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d12f5720a443f6f6c32462ad1ef27e2a75f449d218254f3a9f4aa4df6f764eea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff46dafd8d83946a6d33b858b1f38bbd1c14fcbc0a30e0e7ecc7f0f6f6821ade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c163db920ab68ac1d1e0d20201b27040c5b90b42da947ad305aed39fce723bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleOrCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleOrCostCategory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f943af977c247b579b649fa968628f4d749cf61b765af526428f437bfdd1893)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleOrDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbd002fba34c1ccf72f7a776e8506838de6d849de379733863640d4864d33374)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOrDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleOrDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f335b246bfe6cd1fe2ebf9a23ea3103ab643f11bce7432f2cfa0f3c3b83bca28)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__4809733aac0e3b2f950bb2bd4cf9fbfe9e5f1cd6271561a7ff48be79b2ac1a27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e967efa0a480617077e1bca1f4df0143dcc7319e161996e2e3c4796d0cacf569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3b62297d88474f1ec231ab3af1e0e60d7a9f005bd187f6292519a848fe9b7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleOrDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleOrDimension],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0da436724840c564d76cac66557e0ff8401a3101f6586f45e1923517d04e63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleOrList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7554e15ae7cab89428e7bfe0b034a107f107849c936255d6ddfe373f59998f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CeCostCategoryRuleRuleOrOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc512eafdb19e1bba01d1da60c14a695e56616d8c10ee478abd4d76bb77c225)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategoryRuleRuleOrOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bec542529f02ab3dcf077794210751c875d6cde8d912950fc7b88add1cd5c26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__620f93bfd058fcc146d175be01eff69abdc2ded6baa75930f6332f4dd96b5a80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__481fac59d666a3455579a151365944736f5e05ac9e79c175753d8923fd916eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c636d086d26ea72dd339f8ecba6383c2ed493b5ce4abaa5043100c4ce9debe38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleOrOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd79738c3317c62303d99ecb5ca9ed7f78c00dd09a10c9393a0c1a6d6370b10d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleOrCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleOrDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleOrTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleOrCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleOrCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleOrDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleOrDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleOrTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleOrTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleOrCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleOrDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleOrTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ef2c4261bd36113df92af095806fc86ac475bffe7bd74146bfed3044a58b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleOrTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9359d999dfacf062b2fc508cfee495f0b9d549e62cdb6b1d67ccf175bd199aca)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOrTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleOrTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOrTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4077300a8565117993228b39c903f6d2be2c24d1131e9328ba5ebc5f039fa8e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0b4e3fdec4b177ed3784955cf222f2af51285a108e50c9a57b9226a4160b802a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7d0ded6dc1ff250de01c01ad712f943c11a22689d833ec5ce468ba84d95954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06fa2eed99b98778e49814458a8bf0f57eef378dbd1f78e2fed3f57c913bc9f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleOrTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleOrTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__987c4f3761f15cb7799dab429431ba1471f06a0b804284de7e39c454f55e9099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a2d5f452e0276133b55fb38d8b25fa84109e2c0c85fb1ff7d7b566e2fe1a4c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleAnd, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d80d40643143b512d4028680ee31de686cde8f5bc7482f8ad23d415d7e78d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putNot")
    def put_not(
        self,
        *,
        cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotDimension, typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotTags, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        value = CeCostCategoryRuleRuleNot(
            cost_category=cost_category, dimension=dimension, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putNot", [value]))

    @jsii.member(jsii_name="putOr")
    def put_or(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleOr, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39de827e45779199f3a4f9488d08a27461d094bf070aa219c6b413b624aa2aaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOr", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetNot")
    def reset_not(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNot", []))

    @jsii.member(jsii_name="resetOr")
    def reset_or(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOr", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> CeCostCategoryRuleRuleAndList:
        return typing.cast(CeCostCategoryRuleRuleAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="not")
    def not_(self) -> CeCostCategoryRuleRuleNotOutputReference:
        return typing.cast(CeCostCategoryRuleRuleNotOutputReference, jsii.get(self, "not"))

    @builtins.property
    @jsii.member(jsii_name="or")
    def or_(self) -> CeCostCategoryRuleRuleOrList:
        return typing.cast(CeCostCategoryRuleRuleOrList, jsii.get(self, "or"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="notInput")
    def not_input(self) -> typing.Optional[CeCostCategoryRuleRuleNot]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNot], jsii.get(self, "notInput"))

    @builtins.property
    @jsii.member(jsii_name="orInput")
    def or_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]], jsii.get(self, "orInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRule]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CeCostCategoryRuleRule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b4707e055a7989236fb76851eca752ae443d6a51094edd1fbd8264f7cc6e2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ccc6daa294ef3c9dae0be66d5e59f21d7868f670841a986d180719bbc9cce6)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategoryRuleRuleTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b1061aa8d593cdcde3ac248b14da8c982f3c42c275a88216f23abbe0753dfb5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e59ebbb65d99738d595fa7e081422807bdb706101acdff34bb042482c090e3bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd3b042d4a4a5097f4b705a4ed580b976eb99f7c9f7ba895f539f31ffeeabce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34766630f4343dea49e669911f5a0739655e64b32abe370168b1951a0b781ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c12b7e6caeaab1f784e7ce8192f7bf57faf1c9d770927dc041657dbaa86706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategorySplitChargeRule",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "source": "source",
        "targets": "targets",
        "parameter": "parameter",
    },
)
class CeCostCategorySplitChargeRule:
    def __init__(
        self,
        *,
        method: builtins.str,
        source: builtins.str,
        targets: typing.Sequence[builtins.str],
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRuleParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#method CeCostCategory#method}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#source CeCostCategory#source}.
        :param targets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#targets CeCostCategory#targets}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#parameter CeCostCategory#parameter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf300ec26553ab40cd204547a0d715096ffc4b009483c0fa4db1ca71bf12d3cd)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "method": method,
            "source": source,
            "targets": targets,
        }
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#method CeCostCategory#method}.'''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#source CeCostCategory#source}.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#targets CeCostCategory#targets}.'''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#parameter CeCostCategory#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategorySplitChargeRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategorySplitChargeRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategorySplitChargeRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72f6cb6a2858928d249d62a50fe2fc13dd65a4d07b19f7b8769eb1940e0c29a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CeCostCategorySplitChargeRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__644f7794964d1201f2513fe04b251b343e69502453903c53fc7b1f4aba5b59c6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategorySplitChargeRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca10476d9cb36183ac3dbea96cb1b83950feff192e30df7a7058610ce582e182)
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
            type_hints = typing.get_type_hints(_typecheckingstub__75d4be006a7a357e5003999e2383057f2f2352c2885771f494d52514ad19d9ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1cf57ff0ce8686131e5cac8dbeebdd7b1683be2cbf4a9fba0c86ebda7ea189e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1bf4333a9f59a286fdaa5019cf1f43e8ee50cdd94c718a2e746d0b5a12d1b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategorySplitChargeRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategorySplitChargeRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21411140ef4626031c1ce48ecadeca60d721fc031c6896fa10263030f0fb14bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRuleParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dbda78ddad5dc905887e8cb5a86162368ec5f20d702ebc3768e647af3276af4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "CeCostCategorySplitChargeRuleParameterList":
        return typing.cast("CeCostCategorySplitChargeRuleParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d901e1ea652a302833c98a56a09755e7b0f29cb516d932c1708dd9e59fa728ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8582de8cf54100b58f93831bd75ce2eff56fe96c9afd7d86ad3915dcf5ecda3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targets"))

    @targets.setter
    def targets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b52ceeee277bd37befbf2b154d4123bc1bda0a3c2579cea058caeffa51181080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategorySplitChargeRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategorySplitChargeRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategorySplitChargeRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddc8080954fef589ad040a2b44a243145fbafbe0ff75ccf456c43ce7503e38fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ceCostCategory.CeCostCategorySplitChargeRuleParameter",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "values": "values"},
)
class CeCostCategorySplitChargeRuleParameter:
    def __init__(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14623ee0cdede8bab0d33844b40f37baaa50e5ba56846bfa2034ccf8bddb28cd)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategorySplitChargeRuleParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategorySplitChargeRuleParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategorySplitChargeRuleParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfca43cde76ecabeb329de44bc4edaedcc554d118408a18795ba0310901df027)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CeCostCategorySplitChargeRuleParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333c85d789ef7af1c223de42a1c4fb4648062925d85a6ac2035a343f5d1d7be8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategorySplitChargeRuleParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__515e1fea3a0185183d3e18d7453f201d34f2090226717a7205f8bcdf2ab483a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0bc65a5c4bea537aabf868bf8b42b102b5fb3b48ac6d47a530dd5e8ebc03b583)
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
            type_hints = typing.get_type_hints(_typecheckingstub__887f77099b5554b0580aeabdccfa74aba93613f5adcd5fb9678d8bfd693f1918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7986b56f4503444f5559db8fc845470d6738b868f939365d3eee99437a7b5f68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategorySplitChargeRuleParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ceCostCategory.CeCostCategorySplitChargeRuleParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec77500891cd88744b9f4d8effdd1b7dd6ddd506a706c9638be72edd1b17150e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a95e4c75a3936daa260c4b36f320802e69ee3ed85e2d3a2d3892d4506d90f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f366776e4534d09243e73ba034755a6aa0ea46456bcd2836936d8f2eea202fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e162321447461c3280b86b8d678d6546f4d9df2fbd19c604c9ca6c1d65aabac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CeCostCategory",
    "CeCostCategoryConfig",
    "CeCostCategoryRule",
    "CeCostCategoryRuleInheritedValue",
    "CeCostCategoryRuleInheritedValueOutputReference",
    "CeCostCategoryRuleList",
    "CeCostCategoryRuleOutputReference",
    "CeCostCategoryRuleRule",
    "CeCostCategoryRuleRuleAnd",
    "CeCostCategoryRuleRuleAndCostCategory",
    "CeCostCategoryRuleRuleAndCostCategoryOutputReference",
    "CeCostCategoryRuleRuleAndDimension",
    "CeCostCategoryRuleRuleAndDimensionOutputReference",
    "CeCostCategoryRuleRuleAndList",
    "CeCostCategoryRuleRuleAndOutputReference",
    "CeCostCategoryRuleRuleAndTags",
    "CeCostCategoryRuleRuleAndTagsOutputReference",
    "CeCostCategoryRuleRuleCostCategory",
    "CeCostCategoryRuleRuleCostCategoryOutputReference",
    "CeCostCategoryRuleRuleDimension",
    "CeCostCategoryRuleRuleDimensionOutputReference",
    "CeCostCategoryRuleRuleNot",
    "CeCostCategoryRuleRuleNotCostCategory",
    "CeCostCategoryRuleRuleNotCostCategoryOutputReference",
    "CeCostCategoryRuleRuleNotDimension",
    "CeCostCategoryRuleRuleNotDimensionOutputReference",
    "CeCostCategoryRuleRuleNotOutputReference",
    "CeCostCategoryRuleRuleNotTags",
    "CeCostCategoryRuleRuleNotTagsOutputReference",
    "CeCostCategoryRuleRuleOr",
    "CeCostCategoryRuleRuleOrCostCategory",
    "CeCostCategoryRuleRuleOrCostCategoryOutputReference",
    "CeCostCategoryRuleRuleOrDimension",
    "CeCostCategoryRuleRuleOrDimensionOutputReference",
    "CeCostCategoryRuleRuleOrList",
    "CeCostCategoryRuleRuleOrOutputReference",
    "CeCostCategoryRuleRuleOrTags",
    "CeCostCategoryRuleRuleOrTagsOutputReference",
    "CeCostCategoryRuleRuleOutputReference",
    "CeCostCategoryRuleRuleTags",
    "CeCostCategoryRuleRuleTagsOutputReference",
    "CeCostCategorySplitChargeRule",
    "CeCostCategorySplitChargeRuleList",
    "CeCostCategorySplitChargeRuleOutputReference",
    "CeCostCategorySplitChargeRuleParameter",
    "CeCostCategorySplitChargeRuleParameterList",
    "CeCostCategorySplitChargeRuleParameterOutputReference",
]

publication.publish()

def _typecheckingstub__75440b9b75c64b278b60fa88506ddf52a78638e2efc77590d9eefa91efa60fa0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRule, typing.Dict[builtins.str, typing.Any]]]],
    rule_version: builtins.str,
    default_value: typing.Optional[builtins.str] = None,
    effective_start: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    split_charge_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__255f55aa1e3a853e33467c04c1d3853dbe033af998923800b1b17a91f355180d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e13ae21294b769a7836a99c4e27316e93b6a5edbfc189c2a6ee2ae1b7f6acf8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48dd229f6608b337d1dad09fa5dcd5c96f12460a6acc47c3858932f801af5731(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f5c39e7527ad6612b8f0acc6104926770ab37b49b8f4c239a0559bcca87d80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74090bf9825f10058475a7721564298c69ee99421ffecc1e22550427b5ba13ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ddb9b061fc93be1b31d408fab187b3b54d4e4ffa18d158fcb34452f91d5b606(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08909c3a57fa51768a2176cfb23e6fcc063dd6c975829af70970d0b8774562c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90307086384b2ea8d3135c1f2ce6ac7098157bc8c24c7654561def2146a724a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46732361d523bb8efad4fd899a48f2d6712bc83c70112bdc5b1ae6d7e53f911(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0987c02944a20f9724b79b26e9eba1ca3d64f81ac5bc77ea23fc4607c0a714dc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRule, typing.Dict[builtins.str, typing.Any]]]],
    rule_version: builtins.str,
    default_value: typing.Optional[builtins.str] = None,
    effective_start: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    split_charge_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66eca5690fce549362071095fd505f569ca4dd61a0dac063c6aae40ce8e8f44(
    *,
    inherited_value: typing.Optional[typing.Union[CeCostCategoryRuleInheritedValue, typing.Dict[builtins.str, typing.Any]]] = None,
    rule: typing.Optional[typing.Union[CeCostCategoryRuleRule, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3e7b866516aaaa346d857c152b5190c207d4835c32db072982cd3f225861b6(
    *,
    dimension_key: typing.Optional[builtins.str] = None,
    dimension_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c44b483451a1ed0966bb036b415837e4c17a4393add78918afed17c7205a3e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47792e56a7ee49f508272b475d1020c0303a6678c2cab4c1b03939301c79f8ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5711601f15ebfc7dfd7d85b97cf23ffe0470f3aa6dc5cdd82f5665f4bb00239a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e571b76f090f5ab1779d7f58d5b47612fd38006768b6cdda0fe8db2f8bb1275e(
    value: typing.Optional[CeCostCategoryRuleInheritedValue],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bb7ff5914e73f97eb237a6ace5d0398df8f9c3fbfd9ca2a4165f7d14c124ce6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d1826e6f6893646342b900a3d45cd049b0bdee62966a938f4b07a4f23ad38c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc725f3d050d7b42f121447b3d87e6a2c432c475b9cb432d965be89f7e035334(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d986aba3ea6cc1cc23fa8655217eebed6690bfc683e7aa12938438a08aaeeb26(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d21953f5f3f08d3c51740e0654f9628c0d303a57f45356b9ce7c991c74b82d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2943d8a987f5e31919ee3132625963d21b43e5f1a1005f9bd36ac5762a820802(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402660241b1360cbf785072b52fbfdc4c8e608672ee656122a5ff39d8729526d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b4890af948022ecca63e7d82a0b8dd09c5578f6972eb65531b12049852d596(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e89ee65125e1131c981190443311f67f52c814f45d140ccd49dca7c24ded448f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5c35943bb206235f29af10942260e271280e01a6c2d4921a6d373b289fe7f8(
    value: typing.Optional[typing.Union[CeCostCategoryRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912a57c258203db0ba6f037134e265929a9d789f01b6795348a225c4df16cb01(
    *,
    and_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleAnd, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    not_: typing.Optional[typing.Union[CeCostCategoryRuleRuleNot, typing.Dict[builtins.str, typing.Any]]] = None,
    or_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleOr, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59445027adaaa7702bf5cebce72e266927f8b94a2f14433e5b50072ba601501(
    *,
    cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleAndCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleAndDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleAndTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646060cc742b20f9b83b0c6161fba479893378ac9f50f208b75fe17cefacecdc(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8d558ce21fce9a4f316dbdd79faa3444ea48b09358d5cb9c4aaa0cc5dc5c71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96881e70e097f1543dc793dadedfbe4eb7595f236fe9ffceee72ab8e8006492(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772d66731a24dc8d051fab8aed775964420d725b3da06ccdd1a8f534a356c691(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eebdf7f2937558d2f64d6c1a328c3cd153ee5fd5c68e682413106eaff38be76(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0173406281a410f09c6da440d1de1103de655bd72e0ec0a33e1fcf671550788d(
    value: typing.Optional[CeCostCategoryRuleRuleAndCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4c1702336d813b3f9442f50e646397fc7f935612d06bf041fea0146d3b9c92(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15098709c6bd92fa53eec8d3a597a6f15dbf551b15714b03abdccc3dd5e6f8dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf1fc4e677bc2224c5ddc932ede645e35622a13c11828ac3dab46a54b51711b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5fca66afee957afd7470f42323452d637af89890eae695303b40053c135c33b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0571792eb57d69296cb34a4a52e6f149e4b246f6ef7051f207ab1617ea50994e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c170dbced4a865c33215b3262bf443d0aab105839d2d3e0633fdef5a56424e2(
    value: typing.Optional[CeCostCategoryRuleRuleAndDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2966deb7ff09c80f0ebe336627d73c7f5d3b6a8db99476601d4f439af4c8d178(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5530baf1be898481e31948370a94ad7b5e045383f065440af83335c6f59f364(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1ca3987a0cf681b43fd11c87b7d9c71ba3203a993c12527211ce95159a8b4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9e6612d761da8797bf75d57cd0479d28c19bda61caa12809b8f536e6a97b48(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc0ef6bbcf70a207c8ac4bdd81bfc093b26e3c3a75a47d538042d4923e89c23(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7cdba877e69997bcaad98db2166b46d316d804bdedb86f76bcefa1547168f44(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1edb39b837373e31d5765958d9bc449c3c71c2d866669213412f97074752013(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209bf8dc1348d1edbae538c3ab0beeead731bd4b8389409b59138a860acb0c77(
    value: typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6155a7e9f575dfe5e3b80f779937bb2b961ebf44b8b4b53383df7f8ac12af5ae(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37ee162929ec95a8a9443bbcb6ea14444bdc2c129ad2d0de84264c412d838d7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68faf093799c2a266157a110aaa48e01eb5a4fccf36feed503d601c2c03160e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d6df80e0ce2a0e01a4582fd75266fe793307ebb073b6e9aa7aefae55e361743(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a599824da895759112d5e52a2b4d5bbc0d692dc8dab655cce9a712c945deba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c789d5aff6b259963c3bb39b411190591fc0cd5061343205d1780d5c1ec74ab(
    value: typing.Optional[CeCostCategoryRuleRuleAndTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8a2203aca46d423ba9e33da28ba0e97be4a0256fb03cbc6993f671a4952c21(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84961cb6733f451a5dc42b5fdf24b39a17f968ca624f5abbeb471d71463a7d99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__872f1a049880486cfe40f53a178d6194858b76317cb0d707c3d446a53b6332c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097540e46dbdcbe8e30f488c8d6c0a2e57a8d2e2ca068322cf6a7028c399d1d1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffb92f3bedbc1c8fba7b59477f42f0cbb181aaa9b99e1bdc8812a936db3a34a2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ccf235b0f4b0ecd4c7f11a94fef8c33ccd6ca1b0e67cf55b8d53c2424ceaaa4(
    value: typing.Optional[CeCostCategoryRuleRuleCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479c56eb7010e377300cd964328d2aaeb9c5d84bf2f5a22da16d9e26a029c31c(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9a2aa488d1eb645c2e37acf83791132958f055e7e0cf996fd68fc386a9e834(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9271d89a6da4cf5ec46be9d5fab46365f925a5899d117f019060edffbcc90bf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c17dcbe1ce0460cb79d07df06362422fb25b664eacce94ae5a692388de0c22(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e444555680aa246a038d7030b7ef528313cbf712a22639f59faef3d940e2122f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5883c7de1beca72dfc353bc7f79fadaa7a3b7ce789ec72a2f5a24270857a3b(
    value: typing.Optional[CeCostCategoryRuleRuleDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__412b90cfb480431a3e15985be2b2b24e7022477ae17e3dd57979d675cecff8f9(
    *,
    cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32ccb52a6494e690ce882c7aca33d971831d080f8515ac2bd8b2c1b298014e9(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f7369786cd10611608754cfa840aa8a2c5b3201e3a8a1f177bf7a18c1831f3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c9664bec92cacc1d869e73b7b15eb98afaa3d60746f2da0210dc9384669d5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c739b9047f267b651160b79aa3a0058c1e3ee67eef108ff8865cac11950571ca(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5acad114a74d2fcbb96886d03b22eb2f25649fe5a0e25ad96793560aea7b0c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789e408c423ae9ec789abb6d001ce9426bbaf36504e56e3038fa85ab4b054fb4(
    value: typing.Optional[CeCostCategoryRuleRuleNotCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38570d38a6f71dee3ca5e9894ab9130b5479f8ea089bea827fc0f98452088d91(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__614f0b86ac39aefdca5312f71fff9ee82b287cd0cc2fb65e143ffd6ab3bd23c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee9f45b3fdf7ad5523f8a24470561dc2904cebbc94312542b94a9a3baaffbb0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9257124a9922eab25026f8ff5200f037b566f8e29a1c722934ca05e29fdbc9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d84633605f7b82a14e9e5a84b1105893dec7687bb692da2dfd3e2db8338c020(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc420641543e02fe30193d58ea0b6caf396e3abe4af6e9329d1c4036bc0cf890(
    value: typing.Optional[CeCostCategoryRuleRuleNotDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508eb83b0d578179d322a4a6a075afd35cabb1ba113cf636e256aa26919e10be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dacb0e8533f409a628eb97d0bcbbc02af99d83cb8a8438024c6d5bd12eb221a4(
    value: typing.Optional[CeCostCategoryRuleRuleNot],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf8cd0eb64edf485ccdc301c36ff550aad44fbc0b36333e443beab2ad522cd0(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f5c62f0090551b1fb04010bf886a62863611194ef72962752ff600430b34c2c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babc7ad603c744e8a6714a9cb66cfbcb60d86e794514ca979b092827b200edc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f3a182a3aed660e88aa9cc59380bf3e033677ebf7a87af404aa91b6a65cbcb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b227f18a59e83e30802ba2e91549d4c60e95550320c5f6cc669b839cf8ce06c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf499a6739c0fc6d3378118e21bb573983d338f7f669fb4537effeeb9296c915(
    value: typing.Optional[CeCostCategoryRuleRuleNotTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a04bab51a39123d48e819f109448a5160655127c79d5c8b6ad987bec72a36c6(
    *,
    cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleOrCostCategory, typing.Dict[builtins.str, typing.Any]]] = None,
    dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleOrDimension, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleOrTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78325c80846045a7f0ed5ab352fe4b1747141c383a3770e444174df9d954e281(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68ef0cf3facd9e44d0b8be100b1dd304378418931742401b0c7448169c96a3f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12f5720a443f6f6c32462ad1ef27e2a75f449d218254f3a9f4aa4df6f764eea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff46dafd8d83946a6d33b858b1f38bbd1c14fcbc0a30e0e7ecc7f0f6f6821ade(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c163db920ab68ac1d1e0d20201b27040c5b90b42da947ad305aed39fce723bfb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f943af977c247b579b649fa968628f4d749cf61b765af526428f437bfdd1893(
    value: typing.Optional[CeCostCategoryRuleRuleOrCostCategory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd002fba34c1ccf72f7a776e8506838de6d849de379733863640d4864d33374(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f335b246bfe6cd1fe2ebf9a23ea3103ab643f11bce7432f2cfa0f3c3b83bca28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4809733aac0e3b2f950bb2bd4cf9fbfe9e5f1cd6271561a7ff48be79b2ac1a27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e967efa0a480617077e1bca1f4df0143dcc7319e161996e2e3c4796d0cacf569(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3b62297d88474f1ec231ab3af1e0e60d7a9f005bd187f6292519a848fe9b7d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0da436724840c564d76cac66557e0ff8401a3101f6586f45e1923517d04e63(
    value: typing.Optional[CeCostCategoryRuleRuleOrDimension],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7554e15ae7cab89428e7bfe0b034a107f107849c936255d6ddfe373f59998f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc512eafdb19e1bba01d1da60c14a695e56616d8c10ee478abd4d76bb77c225(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bec542529f02ab3dcf077794210751c875d6cde8d912950fc7b88add1cd5c26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620f93bfd058fcc146d175be01eff69abdc2ded6baa75930f6332f4dd96b5a80(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481fac59d666a3455579a151365944736f5e05ac9e79c175753d8923fd916eab(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c636d086d26ea72dd339f8ecba6383c2ed493b5ce4abaa5043100c4ce9debe38(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd79738c3317c62303d99ecb5ca9ed7f78c00dd09a10c9393a0c1a6d6370b10d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ef2c4261bd36113df92af095806fc86ac475bffe7bd74146bfed3044a58b18(
    value: typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9359d999dfacf062b2fc508cfee495f0b9d549e62cdb6b1d67ccf175bd199aca(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4077300a8565117993228b39c903f6d2be2c24d1131e9328ba5ebc5f039fa8e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4e3fdec4b177ed3784955cf222f2af51285a108e50c9a57b9226a4160b802a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7d0ded6dc1ff250de01c01ad712f943c11a22689d833ec5ce468ba84d95954(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06fa2eed99b98778e49814458a8bf0f57eef378dbd1f78e2fed3f57c913bc9f2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__987c4f3761f15cb7799dab429431ba1471f06a0b804284de7e39c454f55e9099(
    value: typing.Optional[CeCostCategoryRuleRuleOrTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2d5f452e0276133b55fb38d8b25fa84109e2c0c85fb1ff7d7b566e2fe1a4c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d80d40643143b512d4028680ee31de686cde8f5bc7482f8ad23d415d7e78d27(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleAnd, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39de827e45779199f3a4f9488d08a27461d094bf070aa219c6b413b624aa2aaa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleOr, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4707e055a7989236fb76851eca752ae443d6a51094edd1fbd8264f7cc6e2e0(
    value: typing.Optional[CeCostCategoryRuleRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ccc6daa294ef3c9dae0be66d5e59f21d7868f670841a986d180719bbc9cce6(
    *,
    key: typing.Optional[builtins.str] = None,
    match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b1061aa8d593cdcde3ac248b14da8c982f3c42c275a88216f23abbe0753dfb5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59ebbb65d99738d595fa7e081422807bdb706101acdff34bb042482c090e3bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd3b042d4a4a5097f4b705a4ed580b976eb99f7c9f7ba895f539f31ffeeabce(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34766630f4343dea49e669911f5a0739655e64b32abe370168b1951a0b781ef0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c12b7e6caeaab1f784e7ce8192f7bf57faf1c9d770927dc041657dbaa86706(
    value: typing.Optional[CeCostCategoryRuleRuleTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf300ec26553ab40cd204547a0d715096ffc4b009483c0fa4db1ca71bf12d3cd(
    *,
    method: builtins.str,
    source: builtins.str,
    targets: typing.Sequence[builtins.str],
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRuleParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f6cb6a2858928d249d62a50fe2fc13dd65a4d07b19f7b8769eb1940e0c29a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644f7794964d1201f2513fe04b251b343e69502453903c53fc7b1f4aba5b59c6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca10476d9cb36183ac3dbea96cb1b83950feff192e30df7a7058610ce582e182(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d4be006a7a357e5003999e2383057f2f2352c2885771f494d52514ad19d9ba(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cf57ff0ce8686131e5cac8dbeebdd7b1683be2cbf4a9fba0c86ebda7ea189e6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1bf4333a9f59a286fdaa5019cf1f43e8ee50cdd94c718a2e746d0b5a12d1b52(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21411140ef4626031c1ce48ecadeca60d721fc031c6896fa10263030f0fb14bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbda78ddad5dc905887e8cb5a86162368ec5f20d702ebc3768e647af3276af4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRuleParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d901e1ea652a302833c98a56a09755e7b0f29cb516d932c1708dd9e59fa728ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8582de8cf54100b58f93831bd75ce2eff56fe96c9afd7d86ad3915dcf5ecda3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52ceeee277bd37befbf2b154d4123bc1bda0a3c2579cea058caeffa51181080(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc8080954fef589ad040a2b44a243145fbafbe0ff75ccf456c43ce7503e38fd(
    value: typing.Optional[typing.Union[CeCostCategorySplitChargeRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14623ee0cdede8bab0d33844b40f37baaa50e5ba56846bfa2034ccf8bddb28cd(
    *,
    type: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfca43cde76ecabeb329de44bc4edaedcc554d118408a18795ba0310901df027(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333c85d789ef7af1c223de42a1c4fb4648062925d85a6ac2035a343f5d1d7be8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__515e1fea3a0185183d3e18d7453f201d34f2090226717a7205f8bcdf2ab483a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc65a5c4bea537aabf868bf8b42b102b5fb3b48ac6d47a530dd5e8ebc03b583(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__887f77099b5554b0580aeabdccfa74aba93613f5adcd5fb9678d8bfd693f1918(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7986b56f4503444f5559db8fc845470d6738b868f939365d3eee99437a7b5f68(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec77500891cd88744b9f4d8effdd1b7dd6ddd506a706c9638be72edd1b17150e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a95e4c75a3936daa260c4b36f320802e69ee3ed85e2d3a2d3892d4506d90f38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f366776e4534d09243e73ba034755a6aa0ea46456bcd2836936d8f2eea202fd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e162321447461c3280b86b8d678d6546f4d9df2fbd19c604c9ca6c1d65aabac7(
    value: typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
