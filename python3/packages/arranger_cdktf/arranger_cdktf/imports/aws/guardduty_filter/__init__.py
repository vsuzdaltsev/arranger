'''
# `aws_guardduty_filter`

Refer to the Terraform Registory for docs: [`aws_guardduty_filter`](https://www.terraform.io/docs/providers/aws/r/guardduty_filter).
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


class GuarddutyFilter(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.guarddutyFilter.GuarddutyFilter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter aws_guardduty_filter}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union["GuarddutyFilterFindingCriteria", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        rank: jsii.Number,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter aws_guardduty_filter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#action GuarddutyFilter#action}.
        :param detector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#detector_id GuarddutyFilter#detector_id}.
        :param finding_criteria: finding_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#finding_criteria GuarddutyFilter#finding_criteria}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#name GuarddutyFilter#name}.
        :param rank: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#rank GuarddutyFilter#rank}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#description GuarddutyFilter#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#id GuarddutyFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#tags GuarddutyFilter#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#tags_all GuarddutyFilter#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d271f7f34e711b1ba017b88f7131e6f767a87a513140386efb9a9b447e9a4f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GuarddutyFilterConfig(
            action=action,
            detector_id=detector_id,
            finding_criteria=finding_criteria,
            name=name,
            rank=rank,
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

    @jsii.member(jsii_name="putFindingCriteria")
    def put_finding_criteria(
        self,
        *,
        criterion: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GuarddutyFilterFindingCriteriaCriterion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param criterion: criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#criterion GuarddutyFilter#criterion}
        '''
        value = GuarddutyFilterFindingCriteria(criterion=criterion)

        return typing.cast(None, jsii.invoke(self, "putFindingCriteria", [value]))

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
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(self) -> "GuarddutyFilterFindingCriteriaOutputReference":
        return typing.cast("GuarddutyFilterFindingCriteriaOutputReference", jsii.get(self, "findingCriteria"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="detectorIdInput")
    def detector_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="findingCriteriaInput")
    def finding_criteria_input(
        self,
    ) -> typing.Optional["GuarddutyFilterFindingCriteria"]:
        return typing.cast(typing.Optional["GuarddutyFilterFindingCriteria"], jsii.get(self, "findingCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rankInput")
    def rank_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rankInput"))

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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e43d9fd09150087b65114cc9d08f42c6ed8cd0deb81fdd962ed8a8dc57af15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70802e27cd36211c6dda4b03034f86589fb4b67acdb603cf10429442f4aca2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90162bd120a70776940725ec4454f488772a64269b3128c1e9c98e3d65248d4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6817b46607c4ef025af73b93ed77ae7b7395a8121d0e22cfc76ab7b089932e3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a60e2bf36754e2f2ef31937066403b483c6cb2e123ae0101b979e20c701e18a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rank")
    def rank(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rank"))

    @rank.setter
    def rank(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd88390cb7ebf6a8817ca1bea43b01313e86a207f4013d6c0e5aff464f54e2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rank", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8e0cd1e1b8f19b6a7360e512d129da8f2028d67579f1290c3bc21e71fa434a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8916a04e6e5ec1eb2e847304123a576b05d5bd5ae59b0c86721a3221ef67eab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.guarddutyFilter.GuarddutyFilterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "detector_id": "detectorId",
        "finding_criteria": "findingCriteria",
        "name": "name",
        "rank": "rank",
        "description": "description",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class GuarddutyFilterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union["GuarddutyFilterFindingCriteria", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        rank: jsii.Number,
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
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#action GuarddutyFilter#action}.
        :param detector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#detector_id GuarddutyFilter#detector_id}.
        :param finding_criteria: finding_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#finding_criteria GuarddutyFilter#finding_criteria}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#name GuarddutyFilter#name}.
        :param rank: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#rank GuarddutyFilter#rank}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#description GuarddutyFilter#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#id GuarddutyFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#tags GuarddutyFilter#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#tags_all GuarddutyFilter#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(finding_criteria, dict):
            finding_criteria = GuarddutyFilterFindingCriteria(**finding_criteria)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994937d288068f76f4fe0757e36254a5aa68ece3b0e6f1cd460f78caa9291e6f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument finding_criteria", value=finding_criteria, expected_type=type_hints["finding_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rank", value=rank, expected_type=type_hints["rank"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "detector_id": detector_id,
            "finding_criteria": finding_criteria,
            "name": name,
            "rank": rank,
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
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#action GuarddutyFilter#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#detector_id GuarddutyFilter#detector_id}.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_criteria(self) -> "GuarddutyFilterFindingCriteria":
        '''finding_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#finding_criteria GuarddutyFilter#finding_criteria}
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast("GuarddutyFilterFindingCriteria", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#name GuarddutyFilter#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rank(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#rank GuarddutyFilter#rank}.'''
        result = self._values.get("rank")
        assert result is not None, "Required property 'rank' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#description GuarddutyFilter#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#id GuarddutyFilter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#tags GuarddutyFilter#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#tags_all GuarddutyFilter#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyFilterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.guarddutyFilter.GuarddutyFilterFindingCriteria",
    jsii_struct_bases=[],
    name_mapping={"criterion": "criterion"},
)
class GuarddutyFilterFindingCriteria:
    def __init__(
        self,
        *,
        criterion: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GuarddutyFilterFindingCriteriaCriterion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param criterion: criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#criterion GuarddutyFilter#criterion}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d5ef6a22f4772bc476325aaab0f4e641210d115120450b5cf307a6bdb397ba)
            check_type(argname="argument criterion", value=criterion, expected_type=type_hints["criterion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "criterion": criterion,
        }

    @builtins.property
    def criterion(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GuarddutyFilterFindingCriteriaCriterion"]]:
        '''criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#criterion GuarddutyFilter#criterion}
        '''
        result = self._values.get("criterion")
        assert result is not None, "Required property 'criterion' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GuarddutyFilterFindingCriteriaCriterion"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyFilterFindingCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.guarddutyFilter.GuarddutyFilterFindingCriteriaCriterion",
    jsii_struct_bases=[],
    name_mapping={
        "field": "field",
        "equal_to": "equalTo",
        "greater_than": "greaterThan",
        "greater_than_or_equal": "greaterThanOrEqual",
        "less_than": "lessThan",
        "less_than_or_equal": "lessThanOrEqual",
        "not_equals": "notEquals",
    },
)
class GuarddutyFilterFindingCriteriaCriterion:
    def __init__(
        self,
        *,
        field: builtins.str,
        equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
        greater_than: typing.Optional[builtins.str] = None,
        greater_than_or_equal: typing.Optional[builtins.str] = None,
        less_than: typing.Optional[builtins.str] = None,
        less_than_or_equal: typing.Optional[builtins.str] = None,
        not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#field GuarddutyFilter#field}.
        :param equal_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#equals GuarddutyFilter#equals}.
        :param greater_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#greater_than GuarddutyFilter#greater_than}.
        :param greater_than_or_equal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#greater_than_or_equal GuarddutyFilter#greater_than_or_equal}.
        :param less_than: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#less_than GuarddutyFilter#less_than}.
        :param less_than_or_equal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#less_than_or_equal GuarddutyFilter#less_than_or_equal}.
        :param not_equals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#not_equals GuarddutyFilter#not_equals}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ae89709d1ce7eb3159a2365cee843230e2ddf614abd8d6f1c95b13e24193e5)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
            check_type(argname="argument greater_than", value=greater_than, expected_type=type_hints["greater_than"])
            check_type(argname="argument greater_than_or_equal", value=greater_than_or_equal, expected_type=type_hints["greater_than_or_equal"])
            check_type(argname="argument less_than", value=less_than, expected_type=type_hints["less_than"])
            check_type(argname="argument less_than_or_equal", value=less_than_or_equal, expected_type=type_hints["less_than_or_equal"])
            check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field": field,
        }
        if equal_to is not None:
            self._values["equal_to"] = equal_to
        if greater_than is not None:
            self._values["greater_than"] = greater_than
        if greater_than_or_equal is not None:
            self._values["greater_than_or_equal"] = greater_than_or_equal
        if less_than is not None:
            self._values["less_than"] = less_than
        if less_than_or_equal is not None:
            self._values["less_than_or_equal"] = less_than_or_equal
        if not_equals is not None:
            self._values["not_equals"] = not_equals

    @builtins.property
    def field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#field GuarddutyFilter#field}.'''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#equals GuarddutyFilter#equals}.'''
        result = self._values.get("equal_to")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def greater_than(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#greater_than GuarddutyFilter#greater_than}.'''
        result = self._values.get("greater_than")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def greater_than_or_equal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#greater_than_or_equal GuarddutyFilter#greater_than_or_equal}.'''
        result = self._values.get("greater_than_or_equal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def less_than(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#less_than GuarddutyFilter#less_than}.'''
        result = self._values.get("less_than")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def less_than_or_equal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#less_than_or_equal GuarddutyFilter#less_than_or_equal}.'''
        result = self._values.get("less_than_or_equal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_filter#not_equals GuarddutyFilter#not_equals}.'''
        result = self._values.get("not_equals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyFilterFindingCriteriaCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyFilterFindingCriteriaCriterionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.guarddutyFilter.GuarddutyFilterFindingCriteriaCriterionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c5c494d318f10bfda640a4ebf1f2d1b33cb733e73f4c41ee77d405fe83882a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GuarddutyFilterFindingCriteriaCriterionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28378e0402ebb50ff0c4df650880582b20f0ae676cfbfaa21a9d120f315c2e27)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GuarddutyFilterFindingCriteriaCriterionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454aae0c1e857d9911d89eafd104d0310b2c016ece844e0f53a6f2e1e7654970)
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
            type_hints = typing.get_type_hints(_typecheckingstub__009430ffdb08600350c510a204da2194498c1d4d92c59cef2b3791abd4a47682)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9b244517bd00d4be925aaccee618d44e9bd747a31ac4f6d18d252eeb56d15a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GuarddutyFilterFindingCriteriaCriterion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GuarddutyFilterFindingCriteriaCriterion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GuarddutyFilterFindingCriteriaCriterion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ed25508911fc427cd1fbfb57a2de8aed38498fe5011bcb741b54cd4a79772a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyFilterFindingCriteriaCriterionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.guarddutyFilter.GuarddutyFilterFindingCriteriaCriterionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba152d23b9660ae82428dce7c4a1bbead9937e3eef0eff134dd0d198790025d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEqualTo")
    def reset_equal_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEqualTo", []))

    @jsii.member(jsii_name="resetGreaterThan")
    def reset_greater_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGreaterThan", []))

    @jsii.member(jsii_name="resetGreaterThanOrEqual")
    def reset_greater_than_or_equal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGreaterThanOrEqual", []))

    @jsii.member(jsii_name="resetLessThan")
    def reset_less_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLessThan", []))

    @jsii.member(jsii_name="resetLessThanOrEqual")
    def reset_less_than_or_equal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLessThanOrEqual", []))

    @jsii.member(jsii_name="resetNotEquals")
    def reset_not_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotEquals", []))

    @builtins.property
    @jsii.member(jsii_name="equalToInput")
    def equal_to_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "equalToInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="greaterThanInput")
    def greater_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "greaterThanInput"))

    @builtins.property
    @jsii.member(jsii_name="greaterThanOrEqualInput")
    def greater_than_or_equal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "greaterThanOrEqualInput"))

    @builtins.property
    @jsii.member(jsii_name="lessThanInput")
    def less_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lessThanInput"))

    @builtins.property
    @jsii.member(jsii_name="lessThanOrEqualInput")
    def less_than_or_equal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lessThanOrEqualInput"))

    @builtins.property
    @jsii.member(jsii_name="notEqualsInput")
    def not_equals_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="equalTo")
    def equal_to(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "equalTo"))

    @equal_to.setter
    def equal_to(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27821333a4e58a18eb2f097b1dfd6351d8f17f08293d8bc287d9cb69694f53ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "equalTo", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7fa69132ea8a27d1a8b887fd3294dac539649d418211e512230f59740248c47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="greaterThan")
    def greater_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "greaterThan"))

    @greater_than.setter
    def greater_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79703c35ff0abd3d9c41b368eb9c6271f6194788aa4aff66150287816ff7e085)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "greaterThan", value)

    @builtins.property
    @jsii.member(jsii_name="greaterThanOrEqual")
    def greater_than_or_equal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "greaterThanOrEqual"))

    @greater_than_or_equal.setter
    def greater_than_or_equal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3433d5ead48bbcda1dbca36284f2b1e777cabaff7a841456f3a21d70466d203)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "greaterThanOrEqual", value)

    @builtins.property
    @jsii.member(jsii_name="lessThan")
    def less_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lessThan"))

    @less_than.setter
    def less_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efed3c486b1c6f702b2f9944463604c6b90a305a8727d5b1c51633a5845e0ae2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lessThan", value)

    @builtins.property
    @jsii.member(jsii_name="lessThanOrEqual")
    def less_than_or_equal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lessThanOrEqual"))

    @less_than_or_equal.setter
    def less_than_or_equal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db02820a37db6dd458315a6e463a65bcf1927f8dc63cb2b1be1b68b3f2e6a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lessThanOrEqual", value)

    @builtins.property
    @jsii.member(jsii_name="notEquals")
    def not_equals(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notEquals"))

    @not_equals.setter
    def not_equals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e355b724742e9de7ebd7541c91ba30dce6f60813808b4fc6bd6d028ed3305a63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notEquals", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GuarddutyFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GuarddutyFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GuarddutyFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b7625fb62ac82693c7b1572e60f9c0506e9b8f2578c5b7e82fa7d143964e9e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyFilterFindingCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.guarddutyFilter.GuarddutyFilterFindingCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0800229d4a21636d264c7538311d5430aeff80cfa79400ac455684cbc5efc0bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCriterion")
    def put_criterion(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GuarddutyFilterFindingCriteriaCriterion, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1fb5ec63616e2bb286dda6a853ea5921734c0737b26650b827a08e1c5d8c41a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCriterion", [value]))

    @builtins.property
    @jsii.member(jsii_name="criterion")
    def criterion(self) -> GuarddutyFilterFindingCriteriaCriterionList:
        return typing.cast(GuarddutyFilterFindingCriteriaCriterionList, jsii.get(self, "criterion"))

    @builtins.property
    @jsii.member(jsii_name="criterionInput")
    def criterion_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GuarddutyFilterFindingCriteriaCriterion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GuarddutyFilterFindingCriteriaCriterion]]], jsii.get(self, "criterionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GuarddutyFilterFindingCriteria]:
        return typing.cast(typing.Optional[GuarddutyFilterFindingCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyFilterFindingCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3122e7a7d33259675fcd3220a00a4190a14f247ed350fd9d0f67edadd9ece7ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GuarddutyFilter",
    "GuarddutyFilterConfig",
    "GuarddutyFilterFindingCriteria",
    "GuarddutyFilterFindingCriteriaCriterion",
    "GuarddutyFilterFindingCriteriaCriterionList",
    "GuarddutyFilterFindingCriteriaCriterionOutputReference",
    "GuarddutyFilterFindingCriteriaOutputReference",
]

publication.publish()

def _typecheckingstub__0d271f7f34e711b1ba017b88f7131e6f767a87a513140386efb9a9b447e9a4f4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: builtins.str,
    detector_id: builtins.str,
    finding_criteria: typing.Union[GuarddutyFilterFindingCriteria, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    rank: jsii.Number,
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

def _typecheckingstub__56e43d9fd09150087b65114cc9d08f42c6ed8cd0deb81fdd962ed8a8dc57af15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70802e27cd36211c6dda4b03034f86589fb4b67acdb603cf10429442f4aca2ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90162bd120a70776940725ec4454f488772a64269b3128c1e9c98e3d65248d4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6817b46607c4ef025af73b93ed77ae7b7395a8121d0e22cfc76ab7b089932e3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a60e2bf36754e2f2ef31937066403b483c6cb2e123ae0101b979e20c701e18a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd88390cb7ebf6a8817ca1bea43b01313e86a207f4013d6c0e5aff464f54e2e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8e0cd1e1b8f19b6a7360e512d129da8f2028d67579f1290c3bc21e71fa434a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8916a04e6e5ec1eb2e847304123a576b05d5bd5ae59b0c86721a3221ef67eab9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994937d288068f76f4fe0757e36254a5aa68ece3b0e6f1cd460f78caa9291e6f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: builtins.str,
    detector_id: builtins.str,
    finding_criteria: typing.Union[GuarddutyFilterFindingCriteria, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    rank: jsii.Number,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d5ef6a22f4772bc476325aaab0f4e641210d115120450b5cf307a6bdb397ba(
    *,
    criterion: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GuarddutyFilterFindingCriteriaCriterion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ae89709d1ce7eb3159a2365cee843230e2ddf614abd8d6f1c95b13e24193e5(
    *,
    field: builtins.str,
    equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
    greater_than: typing.Optional[builtins.str] = None,
    greater_than_or_equal: typing.Optional[builtins.str] = None,
    less_than: typing.Optional[builtins.str] = None,
    less_than_or_equal: typing.Optional[builtins.str] = None,
    not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5c494d318f10bfda640a4ebf1f2d1b33cb733e73f4c41ee77d405fe83882a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28378e0402ebb50ff0c4df650880582b20f0ae676cfbfaa21a9d120f315c2e27(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454aae0c1e857d9911d89eafd104d0310b2c016ece844e0f53a6f2e1e7654970(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009430ffdb08600350c510a204da2194498c1d4d92c59cef2b3791abd4a47682(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9b244517bd00d4be925aaccee618d44e9bd747a31ac4f6d18d252eeb56d15a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ed25508911fc427cd1fbfb57a2de8aed38498fe5011bcb741b54cd4a79772a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GuarddutyFilterFindingCriteriaCriterion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba152d23b9660ae82428dce7c4a1bbead9937e3eef0eff134dd0d198790025d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27821333a4e58a18eb2f097b1dfd6351d8f17f08293d8bc287d9cb69694f53ce(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7fa69132ea8a27d1a8b887fd3294dac539649d418211e512230f59740248c47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79703c35ff0abd3d9c41b368eb9c6271f6194788aa4aff66150287816ff7e085(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3433d5ead48bbcda1dbca36284f2b1e777cabaff7a841456f3a21d70466d203(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efed3c486b1c6f702b2f9944463604c6b90a305a8727d5b1c51633a5845e0ae2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db02820a37db6dd458315a6e463a65bcf1927f8dc63cb2b1be1b68b3f2e6a8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e355b724742e9de7ebd7541c91ba30dce6f60813808b4fc6bd6d028ed3305a63(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b7625fb62ac82693c7b1572e60f9c0506e9b8f2578c5b7e82fa7d143964e9e1(
    value: typing.Optional[typing.Union[GuarddutyFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0800229d4a21636d264c7538311d5430aeff80cfa79400ac455684cbc5efc0bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fb5ec63616e2bb286dda6a853ea5921734c0737b26650b827a08e1c5d8c41a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GuarddutyFilterFindingCriteriaCriterion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3122e7a7d33259675fcd3220a00a4190a14f247ed350fd9d0f67edadd9ece7ab(
    value: typing.Optional[GuarddutyFilterFindingCriteria],
) -> None:
    """Type checking stubs"""
    pass
