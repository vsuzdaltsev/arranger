'''
# `aws_ssm_patch_baseline`

Refer to the Terraform Registory for docs: [`aws_ssm_patch_baseline`](https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline).
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


class SsmPatchBaseline(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaseline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline aws_ssm_patch_baseline}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        approval_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineGlobalFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineSource", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline aws_ssm_patch_baseline} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.
        :param approval_rule: approval_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approval_rule SsmPatchBaseline#approval_rule}
        :param approved_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches SsmPatchBaseline#approved_patches}.
        :param approved_patches_compliance_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_compliance_level SsmPatchBaseline#approved_patches_compliance_level}.
        :param approved_patches_enable_non_security: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_enable_non_security SsmPatchBaseline#approved_patches_enable_non_security}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#description SsmPatchBaseline#description}.
        :param global_filter: global_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#global_filter SsmPatchBaseline#global_filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#id SsmPatchBaseline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operating_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#operating_system SsmPatchBaseline#operating_system}.
        :param rejected_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches SsmPatchBaseline#rejected_patches}.
        :param rejected_patches_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches_action SsmPatchBaseline#rejected_patches_action}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#source SsmPatchBaseline#source}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags SsmPatchBaseline#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags_all SsmPatchBaseline#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6cddead20dfbe5bca89a09c7d03fcbbb520ff872707ab85a39ea4b72ebd390)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmPatchBaselineConfig(
            name=name,
            approval_rule=approval_rule,
            approved_patches=approved_patches,
            approved_patches_compliance_level=approved_patches_compliance_level,
            approved_patches_enable_non_security=approved_patches_enable_non_security,
            description=description,
            global_filter=global_filter,
            id=id,
            operating_system=operating_system,
            rejected_patches=rejected_patches,
            rejected_patches_action=rejected_patches_action,
            source=source,
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

    @jsii.member(jsii_name="putApprovalRule")
    def put_approval_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eac21edcc3fdd9b43a95871369d9cd810a138373f09e0cb0101522b685b9b37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApprovalRule", [value]))

    @jsii.member(jsii_name="putGlobalFilter")
    def put_global_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineGlobalFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04d2ba15ee3d2210594f8f8955f76239f45a2b5bb1f5e8aea866df84c4bcbd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGlobalFilter", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineSource", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__378f0c17dd8854e8f683e8943002173945309a0424a7b692f45093f3d3c01aac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetApprovalRule")
    def reset_approval_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalRule", []))

    @jsii.member(jsii_name="resetApprovedPatches")
    def reset_approved_patches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovedPatches", []))

    @jsii.member(jsii_name="resetApprovedPatchesComplianceLevel")
    def reset_approved_patches_compliance_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovedPatchesComplianceLevel", []))

    @jsii.member(jsii_name="resetApprovedPatchesEnableNonSecurity")
    def reset_approved_patches_enable_non_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovedPatchesEnableNonSecurity", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGlobalFilter")
    def reset_global_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOperatingSystem")
    def reset_operating_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperatingSystem", []))

    @jsii.member(jsii_name="resetRejectedPatches")
    def reset_rejected_patches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectedPatches", []))

    @jsii.member(jsii_name="resetRejectedPatchesAction")
    def reset_rejected_patches_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectedPatchesAction", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

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
    @jsii.member(jsii_name="approvalRule")
    def approval_rule(self) -> "SsmPatchBaselineApprovalRuleList":
        return typing.cast("SsmPatchBaselineApprovalRuleList", jsii.get(self, "approvalRule"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="globalFilter")
    def global_filter(self) -> "SsmPatchBaselineGlobalFilterList":
        return typing.cast("SsmPatchBaselineGlobalFilterList", jsii.get(self, "globalFilter"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "SsmPatchBaselineSourceList":
        return typing.cast("SsmPatchBaselineSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="approvalRuleInput")
    def approval_rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineApprovalRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineApprovalRule"]]], jsii.get(self, "approvalRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesComplianceLevelInput")
    def approved_patches_compliance_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvedPatchesComplianceLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurityInput")
    def approved_patches_enable_non_security_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "approvedPatchesEnableNonSecurityInput"))

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesInput")
    def approved_patches_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "approvedPatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="globalFilterInput")
    def global_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]], jsii.get(self, "globalFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatingSystemInput")
    def operating_system_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesActionInput")
    def rejected_patches_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rejectedPatchesActionInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesInput")
    def rejected_patches_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rejectedPatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineSource"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineSource"]]], jsii.get(self, "sourceInput"))

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
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "approvedPatches"))

    @approved_patches.setter
    def approved_patches(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0720ac5ded38bde33fe038c64aa5d2aa08edf1f27b80a11e7e6f4eefdeb9d36d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatches", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approvedPatchesComplianceLevel"))

    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1199fd69a006e4a784d8067ef1ee5845cf9547eb3ffab1d901c3dc3b6542c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatchesComplianceLevel", value)

    @builtins.property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "approvedPatchesEnableNonSecurity"))

    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__835e67181ec6a2a623b924ef5ff598adafbcfdae0bc10b3825286ef8d753d012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvedPatchesEnableNonSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b0c59237afc3a6532dc8cb800a4d66df3cd91b72025d493d8ea55d8c047613)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3e2b441d443b4c6101d0a66aa9a6cae981ea25dad46949f3ab140b0db47310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0836058f52e3f3c0c73466c90884cf61d7936e2553a8d23fe03a61255a8940d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54efd302d2d189d303a3a883dae81e3a534d4392ac75bfbe198c858535c78585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rejectedPatches"))

    @rejected_patches.setter
    def rejected_patches(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e0ffcf31b745f3444c37573b81de2960c0bf7351131bdb4744d634fa59cda2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectedPatches", value)

    @builtins.property
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rejectedPatchesAction"))

    @rejected_patches_action.setter
    def rejected_patches_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ae00417f0361628b9d258a85f2ec0a70ca628cad5c748bde690ee925b24e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectedPatchesAction", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7d3c1a37acf68e2fdb264a191301d9e24b66ab953e8667a919be0f964d43847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d342dc3b392919930b15f13390499a5c4044a2e48c294f213776a51d3e3088d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineApprovalRule",
    jsii_struct_bases=[],
    name_mapping={
        "patch_filter": "patchFilter",
        "approve_after_days": "approveAfterDays",
        "approve_until_date": "approveUntilDate",
        "compliance_level": "complianceLevel",
        "enable_non_security": "enableNonSecurity",
    },
)
class SsmPatchBaselineApprovalRule:
    def __init__(
        self,
        *,
        patch_filter: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRulePatchFilter", typing.Dict[builtins.str, typing.Any]]]],
        approve_after_days: typing.Optional[jsii.Number] = None,
        approve_until_date: typing.Optional[builtins.str] = None,
        compliance_level: typing.Optional[builtins.str] = None,
        enable_non_security: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param patch_filter: patch_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#patch_filter SsmPatchBaseline#patch_filter}
        :param approve_after_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_after_days SsmPatchBaseline#approve_after_days}.
        :param approve_until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_until_date SsmPatchBaseline#approve_until_date}.
        :param compliance_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#compliance_level SsmPatchBaseline#compliance_level}.
        :param enable_non_security: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#enable_non_security SsmPatchBaseline#enable_non_security}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfad20be64dcb7d3f7b43416057c1c7b4839c7aae134d9e98f615ad96b3d8acd)
            check_type(argname="argument patch_filter", value=patch_filter, expected_type=type_hints["patch_filter"])
            check_type(argname="argument approve_after_days", value=approve_after_days, expected_type=type_hints["approve_after_days"])
            check_type(argname="argument approve_until_date", value=approve_until_date, expected_type=type_hints["approve_until_date"])
            check_type(argname="argument compliance_level", value=compliance_level, expected_type=type_hints["compliance_level"])
            check_type(argname="argument enable_non_security", value=enable_non_security, expected_type=type_hints["enable_non_security"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "patch_filter": patch_filter,
        }
        if approve_after_days is not None:
            self._values["approve_after_days"] = approve_after_days
        if approve_until_date is not None:
            self._values["approve_until_date"] = approve_until_date
        if compliance_level is not None:
            self._values["compliance_level"] = compliance_level
        if enable_non_security is not None:
            self._values["enable_non_security"] = enable_non_security

    @builtins.property
    def patch_filter(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]]:
        '''patch_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#patch_filter SsmPatchBaseline#patch_filter}
        '''
        result = self._values.get("patch_filter")
        assert result is not None, "Required property 'patch_filter' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]], result)

    @builtins.property
    def approve_after_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_after_days SsmPatchBaseline#approve_after_days}.'''
        result = self._values.get("approve_after_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def approve_until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approve_until_date SsmPatchBaseline#approve_until_date}.'''
        result = self._values.get("approve_until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compliance_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#compliance_level SsmPatchBaseline#compliance_level}.'''
        result = self._values.get("compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#enable_non_security SsmPatchBaseline#enable_non_security}.'''
        result = self._values.get("enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineApprovalRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineApprovalRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineApprovalRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04af79cba45242f606887fd5e27fe734e1d594416143adb6e7f26347f5a6fc0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmPatchBaselineApprovalRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c57cc5223d582219f33e8c5b0bb42587ceddb2c4107d93f6ffa23a90ab12bd9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineApprovalRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2258f755006e4ed6537a9933741dd214f4570d45955b878a6696715b47f70db1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7f715949cb0b65a0bca25f4a686d69c101669318437df84022d4dc699e25ad8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c01b89139da74de368d2dcfc109cd8ee6addec9da3567e99059f762e7bced820)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a54da3623982b787207e0fb6ae7aa54b7cc2e1661d8456daa08a6baa1ccb8f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineApprovalRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineApprovalRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e47ea183b0af9be4fff60eb3d4ed5a0869369cbb0dfb5311a54e920d4e5fe04f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPatchFilter")
    def put_patch_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineApprovalRulePatchFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7332391da906bd90cf7e893d6df98bb8798d4dee888055a247c56721b06bb042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPatchFilter", [value]))

    @jsii.member(jsii_name="resetApproveAfterDays")
    def reset_approve_after_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApproveAfterDays", []))

    @jsii.member(jsii_name="resetApproveUntilDate")
    def reset_approve_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApproveUntilDate", []))

    @jsii.member(jsii_name="resetComplianceLevel")
    def reset_compliance_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplianceLevel", []))

    @jsii.member(jsii_name="resetEnableNonSecurity")
    def reset_enable_non_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableNonSecurity", []))

    @builtins.property
    @jsii.member(jsii_name="patchFilter")
    def patch_filter(self) -> "SsmPatchBaselineApprovalRulePatchFilterList":
        return typing.cast("SsmPatchBaselineApprovalRulePatchFilterList", jsii.get(self, "patchFilter"))

    @builtins.property
    @jsii.member(jsii_name="approveAfterDaysInput")
    def approve_after_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "approveAfterDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="approveUntilDateInput")
    def approve_until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approveUntilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="complianceLevelInput")
    def compliance_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="enableNonSecurityInput")
    def enable_non_security_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableNonSecurityInput"))

    @builtins.property
    @jsii.member(jsii_name="patchFilterInput")
    def patch_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineApprovalRulePatchFilter"]]], jsii.get(self, "patchFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="approveAfterDays")
    def approve_after_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "approveAfterDays"))

    @approve_after_days.setter
    def approve_after_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__936af47d58f5c603647e20d75e47f39bc205adf78d140029d6855a9323e01bd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approveAfterDays", value)

    @builtins.property
    @jsii.member(jsii_name="approveUntilDate")
    def approve_until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "approveUntilDate"))

    @approve_until_date.setter
    def approve_until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e3671a8ec87eb7903640e859f181fa2acaf898c1f9ca019be5655c860d2b25b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approveUntilDate", value)

    @builtins.property
    @jsii.member(jsii_name="complianceLevel")
    def compliance_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complianceLevel"))

    @compliance_level.setter
    def compliance_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6bab84d2af8618ca38dd30be9d6efd07ad800a6693d27f990c16d529bb686d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceLevel", value)

    @builtins.property
    @jsii.member(jsii_name="enableNonSecurity")
    def enable_non_security(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableNonSecurity"))

    @enable_non_security.setter
    def enable_non_security(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08d177a62ad70b2208f9757817d492857705c557f89ea02b8746c56ba6683554)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNonSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d00ae3aa1ae9571ca9e2babf3a7c47cddfad112f67b8d59a25dbba01afe583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineApprovalRulePatchFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmPatchBaselineApprovalRulePatchFilter:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe4459a160fd5f7e9d9ff197d851f35f008f5b9f49c929717a00e722d435b532)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineApprovalRulePatchFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineApprovalRulePatchFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineApprovalRulePatchFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40c3b8ede691c540cbd6b5f413bd6d2b39328c4af98c00cfa770b7b71086a623)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmPatchBaselineApprovalRulePatchFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f76b1200487cc9d6cbf29e7aabee90c7de8fff7e26499e28ae6fe97722b0a23d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineApprovalRulePatchFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__516a8a398b15b42bd1c6916a03bc7f3cd83dd57e43d11d170bf54361bbdbfbb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2183d339af46ab273c72d048e82b92274a1271cbcfd7df2cbb4003d9115a0803)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f98f5696059c5c692c2008f43752c7114fda0246a896bc60b7c30ceb10eba044)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d7bb69586b3e7520752495162fc51741b9ea528b4688487dc5adb6c788256b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineApprovalRulePatchFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineApprovalRulePatchFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__25e3d1d7401dea0ba03bc38641fe87febf64b92db3767778c0f08856c582580b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__1ddedc3684ae5b64f739a475e509b877cff03b86f88043894359414e89de81db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e99cd8581c5e5d95c80ef02f44f597e71f42282b603411b97a9ed5cd7f134eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc20051e426641fca8500759883c2e19108f427572d41eb8569aa1a2a6e76707)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineConfig",
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
        "approval_rule": "approvalRule",
        "approved_patches": "approvedPatches",
        "approved_patches_compliance_level": "approvedPatchesComplianceLevel",
        "approved_patches_enable_non_security": "approvedPatchesEnableNonSecurity",
        "description": "description",
        "global_filter": "globalFilter",
        "id": "id",
        "operating_system": "operatingSystem",
        "rejected_patches": "rejectedPatches",
        "rejected_patches_action": "rejectedPatchesAction",
        "source": "source",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SsmPatchBaselineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        approval_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineGlobalFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmPatchBaselineSource", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.
        :param approval_rule: approval_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approval_rule SsmPatchBaseline#approval_rule}
        :param approved_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches SsmPatchBaseline#approved_patches}.
        :param approved_patches_compliance_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_compliance_level SsmPatchBaseline#approved_patches_compliance_level}.
        :param approved_patches_enable_non_security: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_enable_non_security SsmPatchBaseline#approved_patches_enable_non_security}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#description SsmPatchBaseline#description}.
        :param global_filter: global_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#global_filter SsmPatchBaseline#global_filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#id SsmPatchBaseline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operating_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#operating_system SsmPatchBaseline#operating_system}.
        :param rejected_patches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches SsmPatchBaseline#rejected_patches}.
        :param rejected_patches_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches_action SsmPatchBaseline#rejected_patches_action}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#source SsmPatchBaseline#source}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags SsmPatchBaseline#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags_all SsmPatchBaseline#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3d161c12fd229ebea87f9ff36a26334005198c29bf0db18814cb666fc1d8f5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument approval_rule", value=approval_rule, expected_type=type_hints["approval_rule"])
            check_type(argname="argument approved_patches", value=approved_patches, expected_type=type_hints["approved_patches"])
            check_type(argname="argument approved_patches_compliance_level", value=approved_patches_compliance_level, expected_type=type_hints["approved_patches_compliance_level"])
            check_type(argname="argument approved_patches_enable_non_security", value=approved_patches_enable_non_security, expected_type=type_hints["approved_patches_enable_non_security"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument global_filter", value=global_filter, expected_type=type_hints["global_filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument rejected_patches", value=rejected_patches, expected_type=type_hints["rejected_patches"])
            check_type(argname="argument rejected_patches_action", value=rejected_patches_action, expected_type=type_hints["rejected_patches_action"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
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
        if approval_rule is not None:
            self._values["approval_rule"] = approval_rule
        if approved_patches is not None:
            self._values["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            self._values["approved_patches_compliance_level"] = approved_patches_compliance_level
        if approved_patches_enable_non_security is not None:
            self._values["approved_patches_enable_non_security"] = approved_patches_enable_non_security
        if description is not None:
            self._values["description"] = description
        if global_filter is not None:
            self._values["global_filter"] = global_filter
        if id is not None:
            self._values["id"] = id
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if rejected_patches is not None:
            self._values["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            self._values["rejected_patches_action"] = rejected_patches_action
        if source is not None:
            self._values["source"] = source
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]]:
        '''approval_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approval_rule SsmPatchBaseline#approval_rule}
        '''
        result = self._values.get("approval_rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]], result)

    @builtins.property
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches SsmPatchBaseline#approved_patches}.'''
        result = self._values.get("approved_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_compliance_level SsmPatchBaseline#approved_patches_compliance_level}.'''
        result = self._values.get("approved_patches_compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#approved_patches_enable_non_security SsmPatchBaseline#approved_patches_enable_non_security}.'''
        result = self._values.get("approved_patches_enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#description SsmPatchBaseline#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]]:
        '''global_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#global_filter SsmPatchBaseline#global_filter}
        '''
        result = self._values.get("global_filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineGlobalFilter"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#id SsmPatchBaseline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#operating_system SsmPatchBaseline#operating_system}.'''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches SsmPatchBaseline#rejected_patches}.'''
        result = self._values.get("rejected_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#rejected_patches_action SsmPatchBaseline#rejected_patches_action}.'''
        result = self._values.get("rejected_patches_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineSource"]]]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#source SsmPatchBaseline#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmPatchBaselineSource"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags SsmPatchBaseline#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#tags_all SsmPatchBaseline#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineGlobalFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmPatchBaselineGlobalFilter:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__828e76cb1dbbb1a421a05a08cd38b7f71668740c779798dbc3fc5f7db843fc05)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#key SsmPatchBaseline#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#values SsmPatchBaseline#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineGlobalFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineGlobalFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineGlobalFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55b47abb622618a8b8d5c8b6c00254b7ee67b18d0f7991dae7073e757cf4ce57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmPatchBaselineGlobalFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb7a04b43ba94b00ccc9d0d581e94ac5a83e73da80a8ad3b85ad515485ad324)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineGlobalFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__933f434f8af35659bb08a3f2498b311095c69c3291adc198e3a2490aa4f0919c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecae76580e29b879a6ae9fb17f9baf1177cdc5260a5c008ee1d53cff71984410)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0f9682cd5c880fe1366cc07259a2a636013cdf7bde7e4411113bfd8dc353a59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7834a9da73a7a10ef3687cf5e9fd551b92d3340bee27cb076fc1930a411c952a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineGlobalFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineGlobalFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e705a0043e84204f5a6720be7f031deb108903f918e6bc750104db54be347b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__6f271e262ea6a447d3b48c5560b734eb870791bb2168fa8f29b05ffac8aca119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a368f0477d6acc02c8c9734974ebbf2f7061ea692534a36d0780963617e2d30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7151e114bffc92b81bef94deaa7cb4984016a729c7c560cca701005f4037defd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineSource",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "name": "name",
        "products": "products",
    },
)
class SsmPatchBaselineSource:
    def __init__(
        self,
        *,
        configuration: builtins.str,
        name: builtins.str,
        products: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#configuration SsmPatchBaseline#configuration}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.
        :param products: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#products SsmPatchBaseline#products}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8fa3ac1af50f8b04d60ce7bf3af9722334bbb36da34959119deacb150dc3b8b)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument products", value=products, expected_type=type_hints["products"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "name": name,
            "products": products,
        }

    @builtins.property
    def configuration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#configuration SsmPatchBaseline#configuration}.'''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#name SsmPatchBaseline#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def products(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline#products SsmPatchBaseline#products}.'''
        result = self._values.get("products")
        assert result is not None, "Required property 'products' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmPatchBaselineSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmPatchBaselineSourceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineSourceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7dff9d619576f528b3dfad35d48146dca9ba693f6b09b333270666e8b1310e46)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SsmPatchBaselineSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903f487cc96439af1aa0fa8459834e3b0f2e6ba2be04c170a1b2210fd14dd7bb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmPatchBaselineSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__151fa4edd425a7041b73c2a9fc8ffb84f58fecbf5ba92326855ad3661507f064)
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
            type_hints = typing.get_type_hints(_typecheckingstub__40e01629064c7f6a2e3c2af4374e8b96b0fe2be30630cc7ece04881de78ac1e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f3361d8eb3f1cb69983d5b3c36ca3caa031186c85aa6334220bc2c6973fa288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineSource]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c7db65e5eb55b50911ebe73da85c4664fa20f3999b8a81dbd031ab3b4478c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmPatchBaselineSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmPatchBaseline.SsmPatchBaselineSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c25c250d087a90552aaf71dc25f65e935649aee796f8c1ce03b1e935cdde689a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productsInput")
    def products_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "productsInput"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a9a58a10803fec5a14255578f3e1dc195ad0d9e57945f973491b75f985f647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f657849cc8e5cf864c9cb7debbf9082bd84d7c320587da1f51ae8f4507216ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="products")
    def products(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "products"))

    @products.setter
    def products(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fba686753377c988bfdff7f5b83d6cf3138fd75b7ea02a906eb360e5d7ba196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "products", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmPatchBaselineSource, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmPatchBaselineSource, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmPatchBaselineSource, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c013885e3da57b0f42bc0e8f3448e7c182644b5a00cba8225c9ce15a1beb24cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SsmPatchBaseline",
    "SsmPatchBaselineApprovalRule",
    "SsmPatchBaselineApprovalRuleList",
    "SsmPatchBaselineApprovalRuleOutputReference",
    "SsmPatchBaselineApprovalRulePatchFilter",
    "SsmPatchBaselineApprovalRulePatchFilterList",
    "SsmPatchBaselineApprovalRulePatchFilterOutputReference",
    "SsmPatchBaselineConfig",
    "SsmPatchBaselineGlobalFilter",
    "SsmPatchBaselineGlobalFilterList",
    "SsmPatchBaselineGlobalFilterOutputReference",
    "SsmPatchBaselineSource",
    "SsmPatchBaselineSourceList",
    "SsmPatchBaselineSourceOutputReference",
]

publication.publish()

def _typecheckingstub__9d6cddead20dfbe5bca89a09c7d03fcbbb520ff872707ab85a39ea4b72ebd390(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    approval_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    approved_patches_compliance_level: typing.Optional[builtins.str] = None,
    approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    global_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineGlobalFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    operating_system: typing.Optional[builtins.str] = None,
    rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    rejected_patches_action: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineSource, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__8eac21edcc3fdd9b43a95871369d9cd810a138373f09e0cb0101522b685b9b37(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04d2ba15ee3d2210594f8f8955f76239f45a2b5bb1f5e8aea866df84c4bcbd1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineGlobalFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__378f0c17dd8854e8f683e8943002173945309a0424a7b692f45093f3d3c01aac(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineSource, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0720ac5ded38bde33fe038c64aa5d2aa08edf1f27b80a11e7e6f4eefdeb9d36d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1199fd69a006e4a784d8067ef1ee5845cf9547eb3ffab1d901c3dc3b6542c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__835e67181ec6a2a623b924ef5ff598adafbcfdae0bc10b3825286ef8d753d012(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b0c59237afc3a6532dc8cb800a4d66df3cd91b72025d493d8ea55d8c047613(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3e2b441d443b4c6101d0a66aa9a6cae981ea25dad46949f3ab140b0db47310(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0836058f52e3f3c0c73466c90884cf61d7936e2553a8d23fe03a61255a8940d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54efd302d2d189d303a3a883dae81e3a534d4392ac75bfbe198c858535c78585(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e0ffcf31b745f3444c37573b81de2960c0bf7351131bdb4744d634fa59cda2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ae00417f0361628b9d258a85f2ec0a70ca628cad5c748bde690ee925b24e25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7d3c1a37acf68e2fdb264a191301d9e24b66ab953e8667a919be0f964d43847(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d342dc3b392919930b15f13390499a5c4044a2e48c294f213776a51d3e3088d7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfad20be64dcb7d3f7b43416057c1c7b4839c7aae134d9e98f615ad96b3d8acd(
    *,
    patch_filter: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, typing.Dict[builtins.str, typing.Any]]]],
    approve_after_days: typing.Optional[jsii.Number] = None,
    approve_until_date: typing.Optional[builtins.str] = None,
    compliance_level: typing.Optional[builtins.str] = None,
    enable_non_security: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04af79cba45242f606887fd5e27fe734e1d594416143adb6e7f26347f5a6fc0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c57cc5223d582219f33e8c5b0bb42587ceddb2c4107d93f6ffa23a90ab12bd9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2258f755006e4ed6537a9933741dd214f4570d45955b878a6696715b47f70db1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f715949cb0b65a0bca25f4a686d69c101669318437df84022d4dc699e25ad8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01b89139da74de368d2dcfc109cd8ee6addec9da3567e99059f762e7bced820(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a54da3623982b787207e0fb6ae7aa54b7cc2e1661d8456daa08a6baa1ccb8f2d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47ea183b0af9be4fff60eb3d4ed5a0869369cbb0dfb5311a54e920d4e5fe04f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7332391da906bd90cf7e893d6df98bb8798d4dee888055a247c56721b06bb042(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936af47d58f5c603647e20d75e47f39bc205adf78d140029d6855a9323e01bd7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e3671a8ec87eb7903640e859f181fa2acaf898c1f9ca019be5655c860d2b25b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6bab84d2af8618ca38dd30be9d6efd07ad800a6693d27f990c16d529bb686d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08d177a62ad70b2208f9757817d492857705c557f89ea02b8746c56ba6683554(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d00ae3aa1ae9571ca9e2babf3a7c47cddfad112f67b8d59a25dbba01afe583(
    value: typing.Optional[typing.Union[SsmPatchBaselineApprovalRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4459a160fd5f7e9d9ff197d851f35f008f5b9f49c929717a00e722d435b532(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c3b8ede691c540cbd6b5f413bd6d2b39328c4af98c00cfa770b7b71086a623(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76b1200487cc9d6cbf29e7aabee90c7de8fff7e26499e28ae6fe97722b0a23d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__516a8a398b15b42bd1c6916a03bc7f3cd83dd57e43d11d170bf54361bbdbfbb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2183d339af46ab273c72d048e82b92274a1271cbcfd7df2cbb4003d9115a0803(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98f5696059c5c692c2008f43752c7114fda0246a896bc60b7c30ceb10eba044(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d7bb69586b3e7520752495162fc51741b9ea528b4688487dc5adb6c788256b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineApprovalRulePatchFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e3d1d7401dea0ba03bc38641fe87febf64b92db3767778c0f08856c582580b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ddedc3684ae5b64f739a475e509b877cff03b86f88043894359414e89de81db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e99cd8581c5e5d95c80ef02f44f597e71f42282b603411b97a9ed5cd7f134eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc20051e426641fca8500759883c2e19108f427572d41eb8569aa1a2a6e76707(
    value: typing.Optional[typing.Union[SsmPatchBaselineApprovalRulePatchFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3d161c12fd229ebea87f9ff36a26334005198c29bf0db18814cb666fc1d8f5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    approval_rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineApprovalRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    approved_patches_compliance_level: typing.Optional[builtins.str] = None,
    approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    global_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineGlobalFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    operating_system: typing.Optional[builtins.str] = None,
    rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
    rejected_patches_action: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmPatchBaselineSource, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__828e76cb1dbbb1a421a05a08cd38b7f71668740c779798dbc3fc5f7db843fc05(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b47abb622618a8b8d5c8b6c00254b7ee67b18d0f7991dae7073e757cf4ce57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb7a04b43ba94b00ccc9d0d581e94ac5a83e73da80a8ad3b85ad515485ad324(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__933f434f8af35659bb08a3f2498b311095c69c3291adc198e3a2490aa4f0919c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecae76580e29b879a6ae9fb17f9baf1177cdc5260a5c008ee1d53cff71984410(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f9682cd5c880fe1366cc07259a2a636013cdf7bde7e4411113bfd8dc353a59(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7834a9da73a7a10ef3687cf5e9fd551b92d3340bee27cb076fc1930a411c952a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineGlobalFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e705a0043e84204f5a6720be7f031deb108903f918e6bc750104db54be347b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f271e262ea6a447d3b48c5560b734eb870791bb2168fa8f29b05ffac8aca119(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a368f0477d6acc02c8c9734974ebbf2f7061ea692534a36d0780963617e2d30(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7151e114bffc92b81bef94deaa7cb4984016a729c7c560cca701005f4037defd(
    value: typing.Optional[typing.Union[SsmPatchBaselineGlobalFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8fa3ac1af50f8b04d60ce7bf3af9722334bbb36da34959119deacb150dc3b8b(
    *,
    configuration: builtins.str,
    name: builtins.str,
    products: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dff9d619576f528b3dfad35d48146dca9ba693f6b09b333270666e8b1310e46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903f487cc96439af1aa0fa8459834e3b0f2e6ba2be04c170a1b2210fd14dd7bb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151fa4edd425a7041b73c2a9fc8ffb84f58fecbf5ba92326855ad3661507f064(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e01629064c7f6a2e3c2af4374e8b96b0fe2be30630cc7ece04881de78ac1e4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3361d8eb3f1cb69983d5b3c36ca3caa031186c85aa6334220bc2c6973fa288(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c7db65e5eb55b50911ebe73da85c4664fa20f3999b8a81dbd031ab3b4478c8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmPatchBaselineSource]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25c250d087a90552aaf71dc25f65e935649aee796f8c1ce03b1e935cdde689a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a9a58a10803fec5a14255578f3e1dc195ad0d9e57945f973491b75f985f647(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f657849cc8e5cf864c9cb7debbf9082bd84d7c320587da1f51ae8f4507216ca0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fba686753377c988bfdff7f5b83d6cf3138fd75b7ea02a906eb360e5d7ba196(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c013885e3da57b0f42bc0e8f3448e7c182644b5a00cba8225c9ce15a1beb24cd(
    value: typing.Optional[typing.Union[SsmPatchBaselineSource, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
