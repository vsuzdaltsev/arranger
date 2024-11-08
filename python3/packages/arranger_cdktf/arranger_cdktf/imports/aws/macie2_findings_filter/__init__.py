'''
# `aws_macie2_findings_filter`

Refer to the Terraform Registory for docs: [`aws_macie2_findings_filter`](https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter).
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


class Macie2FindingsFilter(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter aws_macie2_findings_filter}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        finding_criteria: typing.Union["Macie2FindingsFilterFindingCriteria", typing.Dict[builtins.str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter aws_macie2_findings_filter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#action Macie2FindingsFilter#action}.
        :param finding_criteria: finding_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#finding_criteria Macie2FindingsFilter#finding_criteria}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#description Macie2FindingsFilter#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#id Macie2FindingsFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#name Macie2FindingsFilter#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#name_prefix Macie2FindingsFilter#name_prefix}.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#position Macie2FindingsFilter#position}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#tags Macie2FindingsFilter#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#tags_all Macie2FindingsFilter#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947605999b0be6c619968916ed87ac81e2e0c3bc641bb405823ecf8bab6c61eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Macie2FindingsFilterConfig(
            action=action,
            finding_criteria=finding_criteria,
            description=description,
            id=id,
            name=name,
            name_prefix=name_prefix,
            position=position,
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
        criterion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2FindingsFilterFindingCriteriaCriterion", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param criterion: criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#criterion Macie2FindingsFilter#criterion}
        '''
        value = Macie2FindingsFilterFindingCriteria(criterion=criterion)

        return typing.cast(None, jsii.invoke(self, "putFindingCriteria", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPosition")
    def reset_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosition", []))

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
    def finding_criteria(self) -> "Macie2FindingsFilterFindingCriteriaOutputReference":
        return typing.cast("Macie2FindingsFilterFindingCriteriaOutputReference", jsii.get(self, "findingCriteria"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="findingCriteriaInput")
    def finding_criteria_input(
        self,
    ) -> typing.Optional["Macie2FindingsFilterFindingCriteria"]:
        return typing.cast(typing.Optional["Macie2FindingsFilterFindingCriteria"], jsii.get(self, "findingCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "positionInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f88248e24f0b14207f35fac4cb56b95a516f3adb8915eee3f3446f5af5651b9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6f427fc4b410dfde9a7fc7aea94492826abbfe11afac463ba1ad837b6b12a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66ee55c53137a494158399da681452ff47713baef965b2ff8d2029b508d9525a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9689a80841a26ff640fd80cfb8a90639b2c402b8e7514ef38c261c68a2a2e4bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf221464ee0b47e53f0a9449d294619d6aac446fb8e4cc468ddb59d49a8b81a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "position"))

    @position.setter
    def position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212bc3c40305b99ec3948ac7039e24fdee0dacb40a4b248b493233e641b0ff95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa9cfa2258029ae2c8dcc59f2d87664fadfd686af4f3bd0b89bb563d52ba01a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2cf90250d2d8c8da9d4d3137a5376d798280189e58a327ab0e231c3c0657309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilterConfig",
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
        "finding_criteria": "findingCriteria",
        "description": "description",
        "id": "id",
        "name": "name",
        "name_prefix": "namePrefix",
        "position": "position",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class Macie2FindingsFilterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        finding_criteria: typing.Union["Macie2FindingsFilterFindingCriteria", typing.Dict[builtins.str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
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
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#action Macie2FindingsFilter#action}.
        :param finding_criteria: finding_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#finding_criteria Macie2FindingsFilter#finding_criteria}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#description Macie2FindingsFilter#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#id Macie2FindingsFilter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#name Macie2FindingsFilter#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#name_prefix Macie2FindingsFilter#name_prefix}.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#position Macie2FindingsFilter#position}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#tags Macie2FindingsFilter#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#tags_all Macie2FindingsFilter#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(finding_criteria, dict):
            finding_criteria = Macie2FindingsFilterFindingCriteria(**finding_criteria)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff13c6f9cf9d1a278cccf0c6bc24655d0089cea35c8f164e6b1caeeefa34f49)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument finding_criteria", value=finding_criteria, expected_type=type_hints["finding_criteria"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "finding_criteria": finding_criteria,
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
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if position is not None:
            self._values["position"] = position
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#action Macie2FindingsFilter#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_criteria(self) -> "Macie2FindingsFilterFindingCriteria":
        '''finding_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#finding_criteria Macie2FindingsFilter#finding_criteria}
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast("Macie2FindingsFilterFindingCriteria", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#description Macie2FindingsFilter#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#id Macie2FindingsFilter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#name Macie2FindingsFilter#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#name_prefix Macie2FindingsFilter#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def position(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#position Macie2FindingsFilter#position}.'''
        result = self._values.get("position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#tags Macie2FindingsFilter#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#tags_all Macie2FindingsFilter#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2FindingsFilterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilterFindingCriteria",
    jsii_struct_bases=[],
    name_mapping={"criterion": "criterion"},
)
class Macie2FindingsFilterFindingCriteria:
    def __init__(
        self,
        *,
        criterion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Macie2FindingsFilterFindingCriteriaCriterion", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param criterion: criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#criterion Macie2FindingsFilter#criterion}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa78fd1ac6565476de899b5996a84b59c75515ece00319fe90105f3ecd73eaa)
            check_type(argname="argument criterion", value=criterion, expected_type=type_hints["criterion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if criterion is not None:
            self._values["criterion"] = criterion

    @builtins.property
    def criterion(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2FindingsFilterFindingCriteriaCriterion"]]]:
        '''criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#criterion Macie2FindingsFilter#criterion}
        '''
        result = self._values.get("criterion")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Macie2FindingsFilterFindingCriteriaCriterion"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2FindingsFilterFindingCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilterFindingCriteriaCriterion",
    jsii_struct_bases=[],
    name_mapping={
        "field": "field",
        "eq": "eq",
        "eq_exact_match": "eqExactMatch",
        "gt": "gt",
        "gte": "gte",
        "lt": "lt",
        "lte": "lte",
        "neq": "neq",
    },
)
class Macie2FindingsFilterFindingCriteriaCriterion:
    def __init__(
        self,
        *,
        field: builtins.str,
        eq: typing.Optional[typing.Sequence[builtins.str]] = None,
        eq_exact_match: typing.Optional[typing.Sequence[builtins.str]] = None,
        gt: typing.Optional[builtins.str] = None,
        gte: typing.Optional[builtins.str] = None,
        lt: typing.Optional[builtins.str] = None,
        lte: typing.Optional[builtins.str] = None,
        neq: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#field Macie2FindingsFilter#field}.
        :param eq: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#eq Macie2FindingsFilter#eq}.
        :param eq_exact_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#eq_exact_match Macie2FindingsFilter#eq_exact_match}.
        :param gt: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#gt Macie2FindingsFilter#gt}.
        :param gte: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#gte Macie2FindingsFilter#gte}.
        :param lt: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#lt Macie2FindingsFilter#lt}.
        :param lte: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#lte Macie2FindingsFilter#lte}.
        :param neq: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#neq Macie2FindingsFilter#neq}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3915d7bb87dde900a47b7acecefd6a98e0e92d191ee5c95950b0d71c09a6f7d)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
            check_type(argname="argument eq_exact_match", value=eq_exact_match, expected_type=type_hints["eq_exact_match"])
            check_type(argname="argument gt", value=gt, expected_type=type_hints["gt"])
            check_type(argname="argument gte", value=gte, expected_type=type_hints["gte"])
            check_type(argname="argument lt", value=lt, expected_type=type_hints["lt"])
            check_type(argname="argument lte", value=lte, expected_type=type_hints["lte"])
            check_type(argname="argument neq", value=neq, expected_type=type_hints["neq"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field": field,
        }
        if eq is not None:
            self._values["eq"] = eq
        if eq_exact_match is not None:
            self._values["eq_exact_match"] = eq_exact_match
        if gt is not None:
            self._values["gt"] = gt
        if gte is not None:
            self._values["gte"] = gte
        if lt is not None:
            self._values["lt"] = lt
        if lte is not None:
            self._values["lte"] = lte
        if neq is not None:
            self._values["neq"] = neq

    @builtins.property
    def field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#field Macie2FindingsFilter#field}.'''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def eq(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#eq Macie2FindingsFilter#eq}.'''
        result = self._values.get("eq")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def eq_exact_match(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#eq_exact_match Macie2FindingsFilter#eq_exact_match}.'''
        result = self._values.get("eq_exact_match")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gt(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#gt Macie2FindingsFilter#gt}.'''
        result = self._values.get("gt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gte(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#gte Macie2FindingsFilter#gte}.'''
        result = self._values.get("gte")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lt(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#lt Macie2FindingsFilter#lt}.'''
        result = self._values.get("lt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lte(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#lte Macie2FindingsFilter#lte}.'''
        result = self._values.get("lte")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def neq(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_findings_filter#neq Macie2FindingsFilter#neq}.'''
        result = self._values.get("neq")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2FindingsFilterFindingCriteriaCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2FindingsFilterFindingCriteriaCriterionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilterFindingCriteriaCriterionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb0cd7dafa19adf42deb768d5db7887bd64afcccba260a18758cc3b8f3864d88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Macie2FindingsFilterFindingCriteriaCriterionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f99461e80fc6d41dec9fbaeecbef4da3f631178ec0c13bd6c9a1f54c7e2bdabc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2FindingsFilterFindingCriteriaCriterionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37ceef5824b06a184b4757836efcdaf137a00afa60563f90c5287ce2303dd71b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__451b3d918e78163dbd13cc05de7f246378066e0a5dd76e8f21ddf603afb168dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb455f38bbce569ced4a5857ea9ec51fda5334a6ca9e175eb5f61ef465a0dba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2FindingsFilterFindingCriteriaCriterion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2FindingsFilterFindingCriteriaCriterion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2FindingsFilterFindingCriteriaCriterion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cfdba85f07c7b9868cd44054d4a7104bd982e627b159a1ffaa10cb5d0930159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2FindingsFilterFindingCriteriaCriterionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilterFindingCriteriaCriterionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14b7866c02b08913c8bc1f7e56aa888d1df7a538a38cd884e35d071743e9b2f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEq")
    def reset_eq(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEq", []))

    @jsii.member(jsii_name="resetEqExactMatch")
    def reset_eq_exact_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEqExactMatch", []))

    @jsii.member(jsii_name="resetGt")
    def reset_gt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGt", []))

    @jsii.member(jsii_name="resetGte")
    def reset_gte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGte", []))

    @jsii.member(jsii_name="resetLt")
    def reset_lt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLt", []))

    @jsii.member(jsii_name="resetLte")
    def reset_lte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLte", []))

    @jsii.member(jsii_name="resetNeq")
    def reset_neq(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNeq", []))

    @builtins.property
    @jsii.member(jsii_name="eqExactMatchInput")
    def eq_exact_match_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eqExactMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="eqInput")
    def eq_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eqInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="gteInput")
    def gte_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gteInput"))

    @builtins.property
    @jsii.member(jsii_name="gtInput")
    def gt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gtInput"))

    @builtins.property
    @jsii.member(jsii_name="lteInput")
    def lte_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lteInput"))

    @builtins.property
    @jsii.member(jsii_name="ltInput")
    def lt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ltInput"))

    @builtins.property
    @jsii.member(jsii_name="neqInput")
    def neq_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "neqInput"))

    @builtins.property
    @jsii.member(jsii_name="eq")
    def eq(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eq"))

    @eq.setter
    def eq(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e3698258075c2fbe6a57b4680d7f380a026d0cac1ed92e450caa4034f09c1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eq", value)

    @builtins.property
    @jsii.member(jsii_name="eqExactMatch")
    def eq_exact_match(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eqExactMatch"))

    @eq_exact_match.setter
    def eq_exact_match(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c321ae61538a9a015d6309ae7e83d3a75e066033e829b04480041303c03a8da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eqExactMatch", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e678cd367236e2ef92e8c06078999bbf5a37e47f1a14d90012c05f488d7fc3b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="gt")
    def gt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gt"))

    @gt.setter
    def gt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eab76ef23b4d7f4edb07c0b6da5a53aea0e4ee4dfc7f9e62dc0cf8ea6a11fe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gt", value)

    @builtins.property
    @jsii.member(jsii_name="gte")
    def gte(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gte"))

    @gte.setter
    def gte(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78f3900a4c688e03618fb4e5d5b74bf791b5299d7437ec41553af56fa4231937)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gte", value)

    @builtins.property
    @jsii.member(jsii_name="lt")
    def lt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lt"))

    @lt.setter
    def lt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e07441d45bd5585f5c0d94f26a5637c603e4a48ccf808afc5976d5ae3bde57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lt", value)

    @builtins.property
    @jsii.member(jsii_name="lte")
    def lte(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lte"))

    @lte.setter
    def lte(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba281849e827052a2410960b522488c3826d7860e0f114c4b2e584514964927)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lte", value)

    @builtins.property
    @jsii.member(jsii_name="neq")
    def neq(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "neq"))

    @neq.setter
    def neq(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b6b50c28847844c13242450561e92d3bdf881450bb79340e31ff1fb9af54f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "neq", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65efb5d125500360ac4a5305bbde4b3df18381244250b1187795fa688f5f7e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2FindingsFilterFindingCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.macie2FindingsFilter.Macie2FindingsFilterFindingCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1aca29f888a1ca632e72d3bfcf5efa91b9509e6132a001820f9a9e6f8fa48277)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCriterion")
    def put_criterion(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__512ff0d27f30efb01b6a2c9c5e80e0295f1122a33b39bc59fc2cb30724c3d263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCriterion", [value]))

    @jsii.member(jsii_name="resetCriterion")
    def reset_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCriterion", []))

    @builtins.property
    @jsii.member(jsii_name="criterion")
    def criterion(self) -> Macie2FindingsFilterFindingCriteriaCriterionList:
        return typing.cast(Macie2FindingsFilterFindingCriteriaCriterionList, jsii.get(self, "criterion"))

    @builtins.property
    @jsii.member(jsii_name="criterionInput")
    def criterion_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2FindingsFilterFindingCriteriaCriterion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2FindingsFilterFindingCriteriaCriterion]]], jsii.get(self, "criterionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Macie2FindingsFilterFindingCriteria]:
        return typing.cast(typing.Optional[Macie2FindingsFilterFindingCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2FindingsFilterFindingCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f05462222656ebdf7b64df18c2199fcb07c5d9c61f806d18b4ed137520361b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Macie2FindingsFilter",
    "Macie2FindingsFilterConfig",
    "Macie2FindingsFilterFindingCriteria",
    "Macie2FindingsFilterFindingCriteriaCriterion",
    "Macie2FindingsFilterFindingCriteriaCriterionList",
    "Macie2FindingsFilterFindingCriteriaCriterionOutputReference",
    "Macie2FindingsFilterFindingCriteriaOutputReference",
]

publication.publish()

def _typecheckingstub__947605999b0be6c619968916ed87ac81e2e0c3bc641bb405823ecf8bab6c61eb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: builtins.str,
    finding_criteria: typing.Union[Macie2FindingsFilterFindingCriteria, typing.Dict[builtins.str, typing.Any]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    position: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__f88248e24f0b14207f35fac4cb56b95a516f3adb8915eee3f3446f5af5651b9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6f427fc4b410dfde9a7fc7aea94492826abbfe11afac463ba1ad837b6b12a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ee55c53137a494158399da681452ff47713baef965b2ff8d2029b508d9525a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9689a80841a26ff640fd80cfb8a90639b2c402b8e7514ef38c261c68a2a2e4bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf221464ee0b47e53f0a9449d294619d6aac446fb8e4cc468ddb59d49a8b81a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212bc3c40305b99ec3948ac7039e24fdee0dacb40a4b248b493233e641b0ff95(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa9cfa2258029ae2c8dcc59f2d87664fadfd686af4f3bd0b89bb563d52ba01a9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2cf90250d2d8c8da9d4d3137a5376d798280189e58a327ab0e231c3c0657309(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff13c6f9cf9d1a278cccf0c6bc24655d0089cea35c8f164e6b1caeeefa34f49(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: builtins.str,
    finding_criteria: typing.Union[Macie2FindingsFilterFindingCriteria, typing.Dict[builtins.str, typing.Any]],
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    position: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa78fd1ac6565476de899b5996a84b59c75515ece00319fe90105f3ecd73eaa(
    *,
    criterion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3915d7bb87dde900a47b7acecefd6a98e0e92d191ee5c95950b0d71c09a6f7d(
    *,
    field: builtins.str,
    eq: typing.Optional[typing.Sequence[builtins.str]] = None,
    eq_exact_match: typing.Optional[typing.Sequence[builtins.str]] = None,
    gt: typing.Optional[builtins.str] = None,
    gte: typing.Optional[builtins.str] = None,
    lt: typing.Optional[builtins.str] = None,
    lte: typing.Optional[builtins.str] = None,
    neq: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0cd7dafa19adf42deb768d5db7887bd64afcccba260a18758cc3b8f3864d88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99461e80fc6d41dec9fbaeecbef4da3f631178ec0c13bd6c9a1f54c7e2bdabc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37ceef5824b06a184b4757836efcdaf137a00afa60563f90c5287ce2303dd71b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451b3d918e78163dbd13cc05de7f246378066e0a5dd76e8f21ddf603afb168dd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb455f38bbce569ced4a5857ea9ec51fda5334a6ca9e175eb5f61ef465a0dba5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cfdba85f07c7b9868cd44054d4a7104bd982e627b159a1ffaa10cb5d0930159(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Macie2FindingsFilterFindingCriteriaCriterion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b7866c02b08913c8bc1f7e56aa888d1df7a538a38cd884e35d071743e9b2f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e3698258075c2fbe6a57b4680d7f380a026d0cac1ed92e450caa4034f09c1c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c321ae61538a9a015d6309ae7e83d3a75e066033e829b04480041303c03a8da(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e678cd367236e2ef92e8c06078999bbf5a37e47f1a14d90012c05f488d7fc3b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eab76ef23b4d7f4edb07c0b6da5a53aea0e4ee4dfc7f9e62dc0cf8ea6a11fe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f3900a4c688e03618fb4e5d5b74bf791b5299d7437ec41553af56fa4231937(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e07441d45bd5585f5c0d94f26a5637c603e4a48ccf808afc5976d5ae3bde57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba281849e827052a2410960b522488c3826d7860e0f114c4b2e584514964927(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b6b50c28847844c13242450561e92d3bdf881450bb79340e31ff1fb9af54f6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65efb5d125500360ac4a5305bbde4b3df18381244250b1187795fa688f5f7e5d(
    value: typing.Optional[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aca29f888a1ca632e72d3bfcf5efa91b9509e6132a001820f9a9e6f8fa48277(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__512ff0d27f30efb01b6a2c9c5e80e0295f1122a33b39bc59fc2cb30724c3d263(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Macie2FindingsFilterFindingCriteriaCriterion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f05462222656ebdf7b64df18c2199fcb07c5d9c61f806d18b4ed137520361b(
    value: typing.Optional[Macie2FindingsFilterFindingCriteria],
) -> None:
    """Type checking stubs"""
    pass
