'''
# `aws_ec2_network_insights_analysis`

Refer to the Terraform Registory for docs: [`aws_ec2_network_insights_analysis`](https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis).
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


class Ec2NetworkInsightsAnalysis(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysis",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis aws_ec2_network_insights_analysis}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        network_insights_path_id: builtins.str,
        filter_in_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_for_completion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis aws_ec2_network_insights_analysis} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param network_insights_path_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#network_insights_path_id Ec2NetworkInsightsAnalysis#network_insights_path_id}.
        :param filter_in_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#filter_in_arns Ec2NetworkInsightsAnalysis#filter_in_arns}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#id Ec2NetworkInsightsAnalysis#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#tags Ec2NetworkInsightsAnalysis#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#tags_all Ec2NetworkInsightsAnalysis#tags_all}.
        :param wait_for_completion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#wait_for_completion Ec2NetworkInsightsAnalysis#wait_for_completion}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deac98d837ea2b1c49b145ec071b636ca932821230d69f1395b9bad533c1903b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Ec2NetworkInsightsAnalysisConfig(
            network_insights_path_id=network_insights_path_id,
            filter_in_arns=filter_in_arns,
            id=id,
            tags=tags,
            tags_all=tags_all,
            wait_for_completion=wait_for_completion,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetFilterInArns")
    def reset_filter_in_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterInArns", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetWaitForCompletion")
    def reset_wait_for_completion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForCompletion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alternatePathHints")
    def alternate_path_hints(
        self,
    ) -> "Ec2NetworkInsightsAnalysisAlternatePathHintsList":
        return typing.cast("Ec2NetworkInsightsAnalysisAlternatePathHintsList", jsii.get(self, "alternatePathHints"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="explanations")
    def explanations(self) -> "Ec2NetworkInsightsAnalysisExplanationsList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsList", jsii.get(self, "explanations"))

    @builtins.property
    @jsii.member(jsii_name="forwardPathComponents")
    def forward_path_components(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsList", jsii.get(self, "forwardPathComponents"))

    @builtins.property
    @jsii.member(jsii_name="pathFound")
    def path_found(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "pathFound"))

    @builtins.property
    @jsii.member(jsii_name="returnPathComponents")
    def return_path_components(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsList", jsii.get(self, "returnPathComponents"))

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startDate"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="statusMessage")
    def status_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusMessage"))

    @builtins.property
    @jsii.member(jsii_name="warningMessage")
    def warning_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warningMessage"))

    @builtins.property
    @jsii.member(jsii_name="filterInArnsInput")
    def filter_in_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "filterInArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInsightsPathIdInput")
    def network_insights_path_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInsightsPathIdInput"))

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
    @jsii.member(jsii_name="waitForCompletionInput")
    def wait_for_completion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForCompletionInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInArns")
    def filter_in_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "filterInArns"))

    @filter_in_arns.setter
    def filter_in_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b08f3b291326c415f8b29e217b725e1e91ba9868545e37b43c57a2acc7daad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterInArns", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__920a9ed7b069a3c385416ca4f12fdacce42d898f851a3c19b37d1681115f3608)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="networkInsightsPathId")
    def network_insights_path_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInsightsPathId"))

    @network_insights_path_id.setter
    def network_insights_path_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__985f5b0a60afaf99f650675e7e48cecd9d27d08d0adaa5757939a6717a962d17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInsightsPathId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55da799c4cd2151ecd3d19ad59f2c7293489f3c764f580e3991b4a187199bb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7928b36a1e7a98d19f6b12e26b379246787cc6edc12ee4d5097b84bf2aa20ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="waitForCompletion")
    def wait_for_completion(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForCompletion"))

    @wait_for_completion.setter
    def wait_for_completion(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7264a36bc4f9012edec9cb4d0aee7e6b72d43c1bbd940179446c8d6870320e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForCompletion", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisAlternatePathHints",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisAlternatePathHints:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisAlternatePathHints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisAlternatePathHintsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisAlternatePathHintsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__468aef1539206d551e45f38084531369e1b8aa498d09b496dfac0bc2a72881a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisAlternatePathHintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6e5b3118709267370d1f00f56470327bc9ce3c46f85fc51aa11052d2a4c6dd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisAlternatePathHintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b1a7a34c34a05980093b3b78ff9aa62ad26531a28b1324a0695507808426c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a50e85365ccc804664895e7d9cd4ae466399e82c25208b9211ed49c5d98a68d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aadb1b54fb804aa3ddda96eeeeeb0ea4fd658490468eda4242dc4c9869694182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisAlternatePathHintsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisAlternatePathHintsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8437497b9726a4c88a5b359ca53c99e69378f6f7fb2a543348f8ac618b97b483)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="componentArn")
    def component_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "componentArn"))

    @builtins.property
    @jsii.member(jsii_name="componentId")
    def component_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "componentId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisAlternatePathHints]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisAlternatePathHints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisAlternatePathHints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923cfdf124db6ed7954a520293136adb23b1ba5c3e99e380ba6341212f126a6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "network_insights_path_id": "networkInsightsPathId",
        "filter_in_arns": "filterInArns",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
        "wait_for_completion": "waitForCompletion",
    },
)
class Ec2NetworkInsightsAnalysisConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        network_insights_path_id: builtins.str,
        filter_in_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_for_completion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param network_insights_path_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#network_insights_path_id Ec2NetworkInsightsAnalysis#network_insights_path_id}.
        :param filter_in_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#filter_in_arns Ec2NetworkInsightsAnalysis#filter_in_arns}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#id Ec2NetworkInsightsAnalysis#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#tags Ec2NetworkInsightsAnalysis#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#tags_all Ec2NetworkInsightsAnalysis#tags_all}.
        :param wait_for_completion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#wait_for_completion Ec2NetworkInsightsAnalysis#wait_for_completion}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83207caa037e2cbc4669b7713c7ec3e6088be1ac81ec830ac5e56205b8ee1a8f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument network_insights_path_id", value=network_insights_path_id, expected_type=type_hints["network_insights_path_id"])
            check_type(argname="argument filter_in_arns", value=filter_in_arns, expected_type=type_hints["filter_in_arns"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument wait_for_completion", value=wait_for_completion, expected_type=type_hints["wait_for_completion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_insights_path_id": network_insights_path_id,
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
        if filter_in_arns is not None:
            self._values["filter_in_arns"] = filter_in_arns
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if wait_for_completion is not None:
            self._values["wait_for_completion"] = wait_for_completion

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
    def network_insights_path_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#network_insights_path_id Ec2NetworkInsightsAnalysis#network_insights_path_id}.'''
        result = self._values.get("network_insights_path_id")
        assert result is not None, "Required property 'network_insights_path_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_in_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#filter_in_arns Ec2NetworkInsightsAnalysis#filter_in_arns}.'''
        result = self._values.get("filter_in_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#id Ec2NetworkInsightsAnalysis#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#tags Ec2NetworkInsightsAnalysis#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#tags_all Ec2NetworkInsightsAnalysis#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def wait_for_completion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ec2_network_insights_analysis#wait_for_completion Ec2NetworkInsightsAnalysis#wait_for_completion}.'''
        result = self._values.get("wait_for_completion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanations",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanations:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAcl",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsAcl:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsAclList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e00e127d091a2471646ba2ad55accffa448151ce8ac5aaf10dbc3beadf80bb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsAclOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fb553c641c5dbe5b29f4b2bbd8c51fdd3037528de9b732611df988c0dacc4f1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsAclOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bdfcc58ff815dcf6842c99576a1e26c2b30aa66ea71a0da29c3d9ce758c1ef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adcba8f9b6dc8164692dc3a540723c1561c755fe3e5bcb70c336f88b8a333cfc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03d54885cc8b54552f1614f4d6d0a3ba2cd8e12f6871d6004fa768a50a03b8f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsAclOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ced39c47c9aed448ba05078d4ed66928123a98f23ec13c4eb1a0b3a98ec05714)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAcl]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAcl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAcl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80f98b9d7b95ad082f02ba8df7efdf13f8e65c458e6615860f590ad0d8cfb46b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsAclRule:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsAclRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsAclRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4630348f906792db0a922de2f77402b82d9a6a8452a5e1af5e6a83832263bba5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsAclRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df10f67c64f8673022a418c870ab36695e39213605077112626fb06790a8dd66)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsAclRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c14bd3f2112a4c36b451cc0c9139bfeca1c35247327ddaf14a2bc15ccabce11b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b942b7d99aadc1767025844eb3d2fa528e159e39d560d47a27730bb807c4009)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33da141e7675aac2ec4bc668a049756ff2fa7bf7c1c44f238324f0c348f819fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsAclRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b1ab732b603223d4531a2c417906d858d9e43a337b9a2d515d59ea73597f2a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="egress")
    def egress(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "egress"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeList", jsii.get(self, "portRange"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="ruleAction")
    def rule_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleAction"))

    @builtins.property
    @jsii.member(jsii_name="ruleNumber")
    def rule_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNumber"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRule]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__677262bfd28f3c063237e0b9b314ec0b5eb90806246ded72eb9cb822a086e622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dea9ab160ebb2c7dc5ac35cf5f82228065224600cc93ff62972b896b30560ecb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa03d10ea14f3d7d37b5ddfc5fc1c8489b95e2391910556bd9d7f73b4b37684)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b3d763a845240be07e5f5bb0c026a1f747b8389e535137eee10ad51b585c181)
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
            type_hints = typing.get_type_hints(_typecheckingstub__386dd27addf27b9c35359b1524be6088059bd7645c021c34cfefc13debe07ca5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4267c4090372157cef67bb26861aca7aef0f15b62fe828f0335684df284e2228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c46fb0a412f0c33b3c7493c6ed29bcf8430063e5d4caacf15a8ee520cbe0fe35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e57c806a926f35d76b9d43b6576c3d14ae530c043263faf4e90e03e504e059f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAttachedTo",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsAttachedTo:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsAttachedTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsAttachedToList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAttachedToList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3f7aec5ef7355cd8f7f6afe29ba7ae03e88911c7b282000ca9df9c019b60322)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsAttachedToOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5288b0d0deb7d08d6aad2162a53c22f74a5b6f5c43f2d4b619b519091a54351)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsAttachedToOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92c7a938516a9442da7b23b89158f986dbe8ac01dbb796ebdee8b896ae700fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03841b8e2c66d734548d95a6df5f69fb222ef39d232f068edd0a25a510b54f74)
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
            type_hints = typing.get_type_hints(_typecheckingstub__950ba09f32ba2a91fd750152561dac4bcef5397686f65ef5f7e1cfdfa1bea7e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsAttachedToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsAttachedToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b89ceb161012f996d1464e8ad73bf7d42b0746876786541bcf4e75eadcc23ba0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAttachedTo]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAttachedTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAttachedTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31917d621bb43ea69325f484019700141daeacdd95ddb746b6064e8acbd7e256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__39051c58dad894057a8e9adaf939e27b677dfb15203dfcd930b2292738970067)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b1e1c3174b79e9a2699d2b5922c125ca8aba18c1437052e07f7a7a95d0bc0e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7d328fdc24f2c666e407b5acb8d524d683e88c63d278799d2dd9003b567746)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a74afefb8ba39c1caabafdf7aa8f8d809a9f82a4ef05f2046315c173dd8d70e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e6af4e373d1b1c29e4b792a4a63216f5b9361118bf6bb9147f35cf0c8a9ae0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfd4d2195e53a1a4b7c44c880378097f536a89dcb5bd4266eb36e918769e055d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="instancePort")
    def instance_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instancePort"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerPort")
    def load_balancer_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadBalancerPort"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a6b25657eae7c15889ca2f1435a1c4be39de192667acaeb56689fce3668fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsComponent",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsComponent:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsComponent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsComponentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsComponentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fe5290fb6726adf3305ff07adac69a268ffd3c31a658aa5724b05fc821eb73c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsComponentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fccc47a6004976c7d5623c71951cc44f9baa5518da04d7247bef0fedf850690e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsComponentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d2d7021d76d644b768351e7151cf2151f4d2fe43a68ad0f12474416dc883e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__860d1c15eb7d01cd3c7ea171cdd5e2d74ee84ccdec45df387c9b2604ffbbd2ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f3ada9defb765f70b845d0721d3dea7768edcad817da96d26eafd136ed62485)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsComponentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsComponentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b26a0bb70a017fd6e75306eb0bb3fb9fbc95f728f01b16f447e45fd601501b76)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsComponent]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsComponent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsComponent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e29d49f259be08b555d95bb54ccd85328fd629244420f628ca8569e6f8977a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsCustomerGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsCustomerGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsCustomerGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af1c8e4ee7525a39d3330e638976aceb777602f6f03bfaaf3d18f95a00bb29b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d708dc591503f28f02233938156286628212c1d32fa3fe0027ded0e7ec915cf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f206b57a8ccace2b5ca803ff176275222e845c1faa5bcd3fb9919073458a01d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c08ce204028280561f0c2ef7b7e9f403218e637c5c2582ebf477d8d74df47f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__028a6782da2b45c9f3ff8cdc961f1d0ac416255c716b081145245317c1b37e92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e595cecb431d5a28316c4fb8b88992d0915293a79ab71a5eea550d2d28cd357)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsCustomerGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsCustomerGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsCustomerGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b59ddf4f639e1e02c72fe4b568ee66d1d72dfc0e9f62cd8b7a29cbc44880042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsDestination",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsDestination:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsDestinationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsDestinationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__217f3b76bbf75c18e4cff51a47d4d6c7f37c35c7176b4be56b44b2b91a08215f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd81eeff442c23eac7ab3adfcc426ad7930b0275d67fa0abf8475b2b8395307)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsDestinationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7761fd6f88bdb40ea95313dd25688811918bd747b66c33d89c1c81cbe5d160dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3a84d36e0eed8555150db781818fc3c98be3c9b1d519c44ab5afe1465161f23)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bf5370e5fd14e9f728bdd3382acd336acf92d6a00ddaa8ac7d6123a19822956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64105d79678de957a311431f77ab71a428d16a7978fb87974c027e0ae5f81bfa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestination]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e85ca6eecf3d115fd9eed72518e60dc9a45b2f6de8483dd3ef9ce821f9f746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsDestinationVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsDestinationVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsDestinationVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsDestinationVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsDestinationVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__39d42bc3146ebc83557bbaafdc1d5f271b39fb451419a2342415bc570609291e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsDestinationVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ecafde75817e9b78b4bca0b38f6b94b56ad1306c46769f327806203ee88d686)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsDestinationVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__144ca0f9c861a4b7d09729cbc7c9db1e5399c88b98a3c5709124fa19f269b79d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ab423c9d7e651e8bbba49149fff91a544fc92c720a5553171ca220f92fb0a7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eab54d68bdeac52347da4a24a4179ad673aeacfa82a317339245a3712a3d3216)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsDestinationVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsDestinationVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d6dfd4e45e319f0f430bcc054aa29241d69b80e9e7c843c1cd323ee6f26f1e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestinationVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestinationVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestinationVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76992de6eb384531972a375c3366be452c83f9d1ae4a710a96da3bef49dfbe20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b84eb51b97baec7e063bcbb414908e0b813110e8aca7554341da006768d4a31c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd9668f9d5bda4c4225166a7e14f8498394c2a9783850322520128a4630eb1c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88e4397d7b7c6dc55098e6f177e6d9d9640862eaa0eccb4c7fab09668c413f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f80f40d5ea96f981f8799f846b6af5103ee07a31dc4df9d47061e8b3b36e7a7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94edde884f5e1a78f56e82954f09c4a26df0bffa7a620184e39794dbd38132f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7095cf12d68b82c006a0bb81aae95a6d79e22c45a756393ce94434e7eaab74e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7eb05ce3c624edbbd361c86de429fb4008119f06cb97def82b1e22269202e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff613ddde15c1949fa1edbf282c7c3428af1e9a8e87db5b4be706068d46da472)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d80717816dccec036b307bd838d3998f077373825e1b1397534380af388a6673)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e860cd3c10f7ad52fdb6850cfb00eff1965bc7af2dbdb5d59cb3ba8b39a913)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64f3d39dc4830283347aa8c2e417b2e47f622f2e32d6507a2cd7680588a2cd77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b2310cb4095314ead9f1f7b32ec958b17e6a8ae78a072c686b898de436cba3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1eb3da8e512224357e0f9ea556593f9d3501957e838ec9b9e698407e919cc9a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341df15519ae1a748bbc863c31cca5163143b1b7497ff3cbdb6107f15a8414f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsInternetGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsInternetGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsInternetGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsInternetGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1490999de57557fbd47caa80b089f0802fd9db2ac92c4d29bec7b197408d1d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsInternetGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__061edd55186614d6367013fcb061fc8a375268c9a6742bcdb46c83947494d501)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsInternetGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__935700305a305091bd6ec230fa409146932afeb2ff6285f37062d07037fd4103)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0bb76fb8068adc3a003d57f3ee1c2686a5484dc00e25beff2331eb409ce0def7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__433eac513fed66509450ba329ccc3ecb305eab1ef3c505dd9ca6ea26ce0fd466)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsInternetGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsInternetGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36373b3e89714d04479ff4cdf76c1867c63a723131842c0ae31c1ce20f0afb9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsInternetGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsInternetGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsInternetGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df1b3f00a0251fdc4fa0a21078750926b7af2260f831ad267f7dfb3929937969)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisExplanationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c1d11f35ee081c03d1e0e9791184de88a4262fd6a767088cb2ecb5b3264b7fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1acb55ec2ee19bc71e65c3d2e36787babb638baa71dae11c4434d9f946a93fcc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bb99b384c5894ec9e4caec106ab51a6c5005c6ba41c5afa5c450bc0aa3ec107)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90c672e7dd42913c8fcdb833a1346c43d84038cbb8a236ecd32da6b81e49bc6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1c76838a57756d8dc55588a33931cf789053256826e4460be0c59c3e53f2665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22c90e46b7020031afdf05a253466a3159fbe6e893ce586f2828996feb5a8459)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9252a67f5e767bbfd2be0c76480beacf671444dda29ff9ef221138e3a48b15)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebec78db77f705c6bf13cd37c3223078ba9bb42c2261f80ba7ec7b82551423a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2da4c69f280944d53ed9ad103004c71739e627e55ad79accb4847a549d3a91e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5df3e7ded97e71f161ea643c431da8bd65eef44f4c910e1e7d444df95a4358f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3dc40083c1f650f274f6c89699b8164d6ed873bf3aaf349deea19dc884ecc219)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5ac007ce60d3af23d12d5f65c47c1de98c1aea1a7de3d5a192e8624c9bbfb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12e86364e64e1d287322dc8a4cacf658475410bd86e315cf08c9a8cddd00d319)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a2e2cf605f661c7ae919fd116e9a3b3e1ac849eb15b85226b995866331b6aa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a0a26b3714c8c93d45f74ba3ef2ec0afb7330fddf36048f9d51dc8cda53024)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09602a23160df14cb2f273eeb63b87f70d8491a368135a3f1da160455dd26a92)
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
            type_hints = typing.get_type_hints(_typecheckingstub__10e2dcafff9796651d3609813a0fe0fd9272b9866dbd823ff1960b57e6cee04d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3286b2a74782738f571651e8d5c75cacab024e512223b7ad52937e67c4d894fc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e89e617aadf544cf79dd969a76a59fa1591dd591d910c565c66a8f18b9c7a246)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsNatGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsNatGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsNatGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsNatGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsNatGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52b1b15f7f4250d905b3b7d4b0d93163ae0a5325f83cb3b979d34f372495ad01)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsNatGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1ec7c9936191e329e1bf71b6173ef02d4d0907ec3931453f234b2d76b6b9ba)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsNatGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1204737b174409da526b5f681da2b0419570ae7178b5557ec14b6defff5bc4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__060663051e4c63e62fc467b7640ad4fed582da4b2187f2d273156fc522ed0df9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf4c67ad79ce71c45bcbe296035b38ffd87bbfc72c5f25af27138da154981dfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsNatGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsNatGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5622d744828f4c017ec64e5d97ea82b8c65a5d9cfeeb86a37af0786e87dc0fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNatGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNatGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNatGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b96101bd9986cad80d58daf4acf5fd88173a5dc0e5185242adc296bb428762)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsNetworkInterface:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e87ba7d3f000d71519a129a02c0a5ee099a60fc20778e8b3cc8a047c542ee2d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ff2991cf6ed42d18ca18dd39840db500634018f82acb5cecf1e32305920aae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__880d33422f4a191ff9c885fe77f4d6bceba183569e774f83db205fc2d62849bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60831f56d8c75270b864ee808b0e0f9cdf5325baf57bbda49cead6a2f0712748)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f21b7eb66a736697d381242438c3275621dcbd21f189d267e9756873c39f5902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e69eb73c5998f3b7818c0c52d8add3bf71ed23d0271d296b219394981e3c6acb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNetworkInterface]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNetworkInterface], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNetworkInterface],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39139e132824ad1013f3908950cce95ccda644b0a7042c7ec1347067b8837c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisExplanationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c66ddc9193c81e8c3afaa742dce0ff0b06f4f590d0b34d35961969fa4f52711)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="acl")
    def acl(self) -> Ec2NetworkInsightsAnalysisExplanationsAclList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsAclList, jsii.get(self, "acl"))

    @builtins.property
    @jsii.member(jsii_name="aclRule")
    def acl_rule(self) -> Ec2NetworkInsightsAnalysisExplanationsAclRuleList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsAclRuleList, jsii.get(self, "aclRule"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addresses"))

    @builtins.property
    @jsii.member(jsii_name="attachedTo")
    def attached_to(self) -> Ec2NetworkInsightsAnalysisExplanationsAttachedToList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsAttachedToList, jsii.get(self, "attachedTo"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @builtins.property
    @jsii.member(jsii_name="cidrs")
    def cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cidrs"))

    @builtins.property
    @jsii.member(jsii_name="classicLoadBalancerListener")
    def classic_load_balancer_listener(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerList, jsii.get(self, "classicLoadBalancerListener"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> Ec2NetworkInsightsAnalysisExplanationsComponentList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsComponentList, jsii.get(self, "component"))

    @builtins.property
    @jsii.member(jsii_name="customerGateway")
    def customer_gateway(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayList, jsii.get(self, "customerGateway"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> Ec2NetworkInsightsAnalysisExplanationsDestinationList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsDestinationList, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="destinationVpc")
    def destination_vpc(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsDestinationVpcList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsDestinationVpcList, jsii.get(self, "destinationVpc"))

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancerListener")
    def elastic_load_balancer_listener(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerList, jsii.get(self, "elasticLoadBalancerListener"))

    @builtins.property
    @jsii.member(jsii_name="explanationCode")
    def explanation_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "explanationCode"))

    @builtins.property
    @jsii.member(jsii_name="ingressRouteTable")
    def ingress_route_table(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableList, jsii.get(self, "ingressRouteTable"))

    @builtins.property
    @jsii.member(jsii_name="internetGateway")
    def internet_gateway(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsInternetGatewayList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsInternetGatewayList, jsii.get(self, "internetGateway"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerArn")
    def load_balancer_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerArn"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerListenerPort")
    def load_balancer_listener_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadBalancerListenerPort"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerTargetGroup")
    def load_balancer_target_group(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupList, jsii.get(self, "loadBalancerTargetGroup"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerTargetGroups")
    def load_balancer_target_groups(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsList, jsii.get(self, "loadBalancerTargetGroups"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerTargetPort")
    def load_balancer_target_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadBalancerTargetPort"))

    @builtins.property
    @jsii.member(jsii_name="missingComponent")
    def missing_component(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "missingComponent"))

    @builtins.property
    @jsii.member(jsii_name="natGateway")
    def nat_gateway(self) -> Ec2NetworkInsightsAnalysisExplanationsNatGatewayList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsNatGatewayList, jsii.get(self, "natGateway"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(
        self,
    ) -> Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceList:
        return typing.cast(Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceList, jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="packetField")
    def packet_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packetField"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="portRanges")
    def port_ranges(self) -> "Ec2NetworkInsightsAnalysisExplanationsPortRangesList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsPortRangesList", jsii.get(self, "portRanges"))

    @builtins.property
    @jsii.member(jsii_name="prefixList")
    def prefix_list(self) -> "Ec2NetworkInsightsAnalysisExplanationsPrefixListList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsPrefixListList", jsii.get(self, "prefixList"))

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "protocols"))

    @builtins.property
    @jsii.member(jsii_name="routeTable")
    def route_table(self) -> "Ec2NetworkInsightsAnalysisExplanationsRouteTableList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsRouteTableList", jsii.get(self, "routeTable"))

    @builtins.property
    @jsii.member(jsii_name="routeTableRoute")
    def route_table_route(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteList", jsii.get(self, "routeTableRoute"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupList", jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupRule")
    def security_group_rule(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleList", jsii.get(self, "securityGroupRule"))

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsList", jsii.get(self, "securityGroups"))

    @builtins.property
    @jsii.member(jsii_name="sourceVpc")
    def source_vpc(self) -> "Ec2NetworkInsightsAnalysisExplanationsSourceVpcList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSourceVpcList", jsii.get(self, "sourceVpc"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> "Ec2NetworkInsightsAnalysisExplanationsSubnetList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSubnetList", jsii.get(self, "subnet"))

    @builtins.property
    @jsii.member(jsii_name="subnetRouteTable")
    def subnet_route_table(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableList", jsii.get(self, "subnetRouteTable"))

    @builtins.property
    @jsii.member(jsii_name="transitGateway")
    def transit_gateway(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayList", jsii.get(self, "transitGateway"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachment")
    def transit_gateway_attachment(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentList", jsii.get(self, "transitGatewayAttachment"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTable")
    def transit_gateway_route_table(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableList", jsii.get(self, "transitGatewayRouteTable"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableRoute")
    def transit_gateway_route_table_route(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteList", jsii.get(self, "transitGatewayRouteTableRoute"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "Ec2NetworkInsightsAnalysisExplanationsVpcList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpcList", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpoint")
    def vpc_endpoint(self) -> "Ec2NetworkInsightsAnalysisExplanationsVpcEndpointList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpcEndpointList", jsii.get(self, "vpcEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnection")
    def vpc_peering_connection(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionList", jsii.get(self, "vpcPeeringConnection"))

    @builtins.property
    @jsii.member(jsii_name="vpnConnection")
    def vpn_connection(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpnConnectionList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpnConnectionList", jsii.get(self, "vpnConnection"))

    @builtins.property
    @jsii.member(jsii_name="vpnGateway")
    def vpn_gateway(self) -> "Ec2NetworkInsightsAnalysisExplanationsVpnGatewayList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpnGatewayList", jsii.get(self, "vpnGateway"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanations]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanations], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanations],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30986f961fd562f3ba3a2f13672dd1327c330764655838390bc99244fafd1317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsPortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsPortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsPortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsPortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsPortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6ca1361f685ebb153c47e9cbfbd3c03ea1ca6b22093dc13dc3f6f4cc2d62646)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsPortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939ac38bc367bf96c9557ddd8134870ae176817acfd52807b9681cbe292378d7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsPortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2223ea04b1580abbd729f1796438766e1ae6d763c1fb565d84c2552b89562ff9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e59c6bda99b2673ba0c60b922a3ad12927416439340f66907748568dc48cc8d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2e0d5e9fb23d198796ebf3cb2b78f2ce459cc8150e2cd7e7d40793250022806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsPortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsPortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdde04b0836f5db90073581be49347ba7b5aad798e84951e077de775b72980c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869279dbce19388d1374d2e4babf8a5893afa7769c9aa7e18713dadd83fa39bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsPrefixList",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsPrefixList:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsPrefixList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsPrefixListList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsPrefixListList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de6b0a3551791e2e626ea150fad4954390874f88b6d7032b4fbce014f10599e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsPrefixListOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ff05c97eeba7b719b2b94c74f22ad3a49e92ddb758b446787c8a660a46a5729)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsPrefixListOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06284b7dad72c4c13a8bd1caf749e870eabfc807e8145443b35cd289bc655756)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8725c4d5ee57d4b408f63dad098f35bab9548c304b6c543862a97206b25d4975)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7278991bfc67a76a20fab5a0953bffca0c25b8749e03f1aa8e7c0c9cea875b61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsPrefixListOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsPrefixListOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d44f282406055b81e42b21e1a4ca426befb0cff347434929c4df18ce7f911499)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPrefixList]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPrefixList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPrefixList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41382916ff286e736dc67714ae7cf29fc71b7ddb2e80c5b7442386ea7610742d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsRouteTable",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsRouteTable:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsRouteTableList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsRouteTableList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16d2a288e628807536be213c6aa2aa0d3b295f23e5c8b883a30aadf8ad74580c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsRouteTableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b95882876bea4ba97126ad7c151c956b109a83005c16ff365adb6859bf71234)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsRouteTableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ee376141cc31dea4839f75d3d07f6ff342c8fd54eba928f61255e8d30c77a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2e55234242b1a3fa19ecd9e4eded1d05a14c768ec8462f84a45f30ae0230041)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42f2e3626f845e40b851dd71edb5ee4acb9fa24c5b732c0eff3c943dcf46ac18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsRouteTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11cd196cd7a7d3dc45f85cf737eb8be2fc317a121dfed3eddf35e26c7d1f8040)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTable]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6ce9b08be87d1a187490c1f725fc188f0c2138a1a1fd36cf919cf4430f056f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8d1969036e959f89bd7a3a741b75f9b914440d7eee9170f82b9ba246608199c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__132121932254c6561cd8cde4c27c41dc9b3b36df725377045edb52851f01cc8a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408d2186aa88b811ad46f11ff283a02c87e6965d829a803259caffafc276d5aa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db5da1242f6be408746d24fa7b47273763889413b3c3ec355fd169bbba41c930)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35156251133d2e33f59e214b37810cfbe7755b265fe1f0983fea42aac3f32de9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e2938e8dc7cdb92a859b990ba149385daf3a7a546dbae9885606bf524b8cf00)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @builtins.property
    @jsii.member(jsii_name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPrefixListId"))

    @builtins.property
    @jsii.member(jsii_name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egressOnlyInternetGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property
    @jsii.member(jsii_name="natGatewayId")
    def nat_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcPeeringConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0582e54bd0a055e88c0fec776de2d64d2730e3b29726c173028cb81819d3475b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSecurityGroup:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ccddd48ddd9318091dceaad43eac22c5396619b1938eda6d15cffa335b55e7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc352212047d3c2869767c02d741d34cd4ccb04c7733de76db0ecd77c78230e4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf578d3da75436cf73dd8fb2c16d9f856719e29221b11832748f7f7cdb1477a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7125d926386be8828d02c9dd8d376d852a9aa34e9a57d47be060619aafe8c81)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa9cfc38e1143098cfa657f31c63a1e5c7e533e1bd7cef7ad2e3cbd01f26eb33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__115f7dd2d09b1c1b21ffe054d13259966cadbccc6e042e3e2f415185f54f8e58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroup]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61880eab9ba8d0dabc570e22ae29baab8ff4c0b568f904bbf0aab69762c94a89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__310f6ad29b8e9d25a5464361e594948695c88f5a18db7084870ebf3cfc1f74df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad92be3314ba73cc6f9f353d2858d4a1f318c8372e31a61e43762a8cea894158)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c18a3ecb6c80dc1d319e5b03bfefd1746b5d398bcf175135327d36ea6fa29ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__080a8e381b1cfe9ac3d38ff95576d0dbcb1a164b84870cac4119b1d95bced14c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__84a223ca46fa50a949ac675995130402c7e95e82a11bc0ffbeb22bf5aa5d2d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5eaabbc1f619e8ef422a60c979b0b1beab304c9d1f2c052ed8443c43661adc21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(
        self,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeList":
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeList", jsii.get(self, "portRange"))

    @builtins.property
    @jsii.member(jsii_name="prefixListId")
    def prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixListId"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb69f0d0c8c6738f693628d325f7d3129c851604d748e7284ce66c028ab7e8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c7cbcc5fd1f78186d7fbbe586a2f77b0837780c760f5e02d93651761038681e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f5be533dc3b0edc73a466b21b9e61938164c71a519416e9628b1bc67bf1cde)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b76ef5fd84f8db465ac8e2fea7904277151a3c03be3923de26158f34e5f818)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcb2dd473eadc698cfecb5c9a0f6f05483e2d75fcdee5dac564ce5baf0604efd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cff0a51ce46f68dc5ede1ec38623a32d939af7bc61023a2aa5718c254c53706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__729221115b58e53d200e65489ca888c988881ef94f273c0397c7701f949f3578)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ae5fe01652db88ca3eb5a302a0d13f7b63e418841e410c8464a3e8257165969)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroups",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSecurityGroups:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSecurityGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__316f51eee3b940858079874102a4d119e8e3ff838d15ff47f9bdddb0914eb94f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84785f70465bc139bb1d12d4a93878600c8a25ee5465a0aab55fba3a6d024db9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f0fc8d2ed04a9228f369713a65f8bcdd5d2f74fe5c0a879d69287c52df2fd01)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8b08d608faf735a28a5e48601c53dbe45dc19cc3449d650a250d5b5b7d8b94c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__202e466b8fcc3324fc47c0520daa111c4518adc86b4b08e6919576d9da602279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7537d2d76a7f0255d9b3ba6c50b7070bea2bcff26ace93b3e108b4f0a8e983c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroups]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4da8422cb66a340a00cfa48f83f8784e60c44aa708fd631d8ca5b369a927005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSourceVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSourceVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSourceVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSourceVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSourceVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebc8c21335d161fad7bec637bb8dd9391d57b99df971e79412bd91cb763ce240)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSourceVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c868bf9e41da02f9d8c110896fe59c95d1faec88df53b84eb1d51711264c9b4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSourceVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be089f938ff12d4721d600f1e7519f02180c6d9504a7ef341cdf65a1e96a36cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8482056be6e3a18405f80ca2571f84e5ae60e71ffbbc59a9b6662a3481bbd832)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e77e72cdd3e6f8c1f0ae9964a27b9d1a3cf03143978e47cc1612c60c0753194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSourceVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSourceVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__da25ddcbb7cb3a2c506ae811360abc14b2a3501ee99bf9b134ecf7677e97e1fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSourceVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSourceVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSourceVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14d54d573cd9ce38a5b355ced53f4b22be963a227a22b65e8631139a182bf86d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSubnet",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSubnet:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSubnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSubnetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSubnetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__649a4008d740e0542a544d6e01eb1b2d0a502c70697263ddca64c85ad02af04d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSubnetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb451d8efc0b7e309eb8813b7a4feb4f6a6079ae98a0a3426f984fcd19a44b37)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSubnetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7342a911660807a8e723af8c5c99ed7c1798a99ea1f3b92332431b1c70f0a235)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c742eb49d6c4a6288d10c43c212c0c85ec2d40702532f7e827a800dcf93e9e66)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b35d6a42e2cc5c8f276d06ecd4c455cc98a707dbfa7f4cdc3f1c26de2ecb2f26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSubnetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSubnetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__19c5fed2ede0382f2b9f1f0aec46686a02e664973a76dde36c73842125e8b587)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnet]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c3a106102c8e10de8e3637fc88d7d7c63b0b718929be6a4c36a9589102121a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea2c09508b4e2ca80cd7d964389f802ea918ac9730fed1c3525cbd24e65b37c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6445800c000e8ad483bb6a5acc9dfde368c1041c85c24255eed32857f22799c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a3ec24dd3993641edcc0580349badeaf776d3665d038412b462e7d0b3fb99b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__43ea3b38d3ac5ea5082ce2aea33885707bf5bba8b697cfea8b64a1ff7fbb2ca0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4ac4863640cae7760b730861f78018b0fdcd5bea47987652c7df672baa1ff0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32bea34e89c7ecac6cd7279f485e5d13046d6656e9c2dc5bc65988dda2a8e6e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc838cc27b49d6f2be8012a7f2135441679fff4e3e513e4ddd60d551f6c122eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsTransitGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsTransitGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d910efa4473c9424e3eed9699e48f561e32fe9c16342d04b5eb6cefb0c6aaeb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25de659ca2f6865b31f2c0d37a0b56d91f4cfdd241decbac7283020ddee0b22b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb02d02a1ebef1ee3636477e68879b2a41fc662405fdc0b35215ba2ffd8b8d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe5bbcbf58bed1f1abe8219ed3e6401991b9bbe5eca58df70bcd6331d4fbaf3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d20ec74c6ebca3c897ea359edee7cd89f5640dfd6c07b7b1050fdc72fcf8391)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a9bd27b7eb66f13f0ce3c869be18c2c7c9430554a3f992823d3364812e69d64)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a28211fc1c5cdd818b636bb1707a22b97bc466549945748ef45379f696baad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5278ddb7ce5ad6c889276e3f79357fd2be0457be79e23c1c73de3fdd28a53608)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d587ed0410836fdfa000748623d31aac47bf3b6006303badf691dbc13c130d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110a52cc19a3a09c78e76d9a43a73dbd248c3e5b33fec4534d5600047611dda2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38f2743db61544e1400e4de2cc4c69bfdb82b545af6fdcf4d6591a814d9f00e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__36bddcf5c9827538edac36b7b63478217020f89f4056317e041582132f57d24f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__393b51feaa174fe08b947aa2fb6113e958f15c863a99abd3e8694371c14a945e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c1a7da2e0618ea18d626c986566ff91fab078d3c5f572e1edef4e14f3b1e1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fdf804e39d9628d459f4f1362da6436289f39a9a87d43b4b6a07319b1296ba4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa8c4e0eed539f6578326569afcc3533ecb8d06a736fa6bfb1320ea877f8b366)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fef2b40b30da985993a6b228a0a7a4bde7032dc88166ea98fcfb1385f9ecead)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d0e5a68169a67ec76b62b5a3b40bff34c61e29b6a7d6178df989f6274df46c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ec20593586d486ad413c1794c8b939f826973027b5559603d978c91377250aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a4f75ce4dbbee3751f4c11ff26098be5159bf4eb47a2242f483ee8913787589)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2d12088a0f8b0a7a647653458c8c0384c02ba23af8a3a2dcd6faf8acb6d1d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__288f8f74fa977aea1c6f9258dbe2807f9b5e473aa8001bba85ac39bc7ff3b825)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9aa2537f9fe1b0189fbe6b2d1fd36d3f6e9921e8f37fc6cc15ad461d64c261)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77dee7f8d6c336ffe3d4a011247796593a0569d0fc3c0ded6aba77419b634208)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce2d8c73acaf2b25ee6c16a49c83e3de786a9439d7d2f79f5a428f61044e1f93)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4275406c672833ed2ce54bc97cca3924361dda2c9f89fb14029b5815dd2ac51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c91e1b654952812aa29c5d1b154058c74516b288af2c0b7e61381ba10df106a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="attachmentId")
    def attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentId"))

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @builtins.property
    @jsii.member(jsii_name="prefixListId")
    def prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixListId"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="routeOrigin")
    def route_origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeOrigin"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c6e5f2974a19ef4fa334ddc1c9b8cc33eff91612a5c9e5a0a855522b25cd393)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsVpcEndpointList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcEndpointList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccf4f9c32cebdfee35a00693e7823d47846213be4bc80aba3b9a0973012f9ad2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpcEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd82022f2747217fddf0b6dd5d1d713f99a48ddb99e6fb8cc304aa17117b46e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpcEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a1296e6162eafd549040f8cad7824439bfcea39e0110bec1052cf4e5fc5fe9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b92ceccd18bfa5d0747064b593917bb1d8a22d793e081637790c79c901d7cef7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1a587ae680eb13388a0185679019ee865671d60b2ed19ca4d1bc84e3c0b695f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsVpcEndpointOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcEndpointOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8af5ecb563806278e8e9b4c27595268336577f059411cfa8934807b185c94295)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ae11856ea766a17087551516583e3eeb31f885604f965c150258bc5fa0b5d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisExplanationsVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d44eefd41c06bc992fc7ecc33e231b0ae1c200534cf9684097bb6864c89c2e14)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0c74bb7e17329139bef13b0454ecb6210d286b982f0c4aeb536bdc2ec9d8840)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0072df1a940f28a6016ca29550f1fff128104f90b08a0e47591909a2ba40fe7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7139cdcc4931efc79d9d31d48afa5ad230c3d5eeda6c71b271e113aa8a1969ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__754034c93afa04c492be10a14644ebaef143a96b2a7e98ae7ff71ac1f5c77d8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d579719628aa3d1c3f2bc3cc7ecc9297e196bd465175179b7963e9810cacbc68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85651662d87d1f75ff160bfb836be770f305f0c7117a0fc99d1fb9ead35a5f7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08818c3e288f143d2450f9976fc2e05e766c1ebedb656a12fe33249ea20fb423)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37eb92c0710cefe0175bb9a38118799303da9084ca96bb543cdfe4a8beefe0c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a9c484483526d6179697cda58d6633418dae3f2337fd83974bd54008b7f985)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d775167741428845b12324b9e7250eda0cf9c204d32ee5ae2f2e5e7cb4fe29c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0de6723b9d24697fdbc2a74b10480306a5a2a0deb44508f655046565096cf670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a40c6c2c6f4fca30b84abde5b8ba98d4e0612fb11360f4bb2a2266c2804b6ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e575ad42ddb24295a6f70d5db816fd34351c6197139a69a0a44495c3f4a08b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpnConnection",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsVpnConnection:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsVpnConnection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsVpnConnectionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpnConnectionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9503dfb8343c87a5a4de9e920f27c12ceddf96098d9a260080aa4ac80b8d488c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpnConnectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__018037cac3a14d9bb330a8dafab5b9fa03ae63fec506a20ed6606e83d7cc54e4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpnConnectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a1f98f830a16d1e7140c21df9228eb1d79dfc408b80c4e8a8c094d9a785bddd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af659cd17b05de304b065531fc293d09f1be579523bc6091169609a8cdb922b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64dba961e0891823c132f4de79c9b1f24dcc60bae5d4acc03344f1d19221f320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsVpnConnectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpnConnectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__242604dc41034832e387191f7034882d7728620a16c7c9b16b228f3b75db780d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnConnection]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnConnection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnConnection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a978464619d0ce6b99d9e9008b2efbc797b03238713bf7acc235a6295820e354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpnGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisExplanationsVpnGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisExplanationsVpnGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisExplanationsVpnGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpnGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__986289f7778b5e76c44604beb1b709ed9bca27da3f6220f6d834bfb258f78ed9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisExplanationsVpnGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30b5dc5c2a0a5a15ec3a208b127523fe76edf45ac846436104b9518d840d255d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisExplanationsVpnGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a47f1babff3d5bcb66939edb7def440e9648ea574a5392a40541eba8e38f9f3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9769f7cf24591e3d72819d64470ec175136bb68f06ccd076bc16f945e51b02d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb5f8b18ee9430254b3aa9547d286eb734ce158e04c1dc1bea7608bdd03edce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisExplanationsVpnGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisExplanationsVpnGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c35b08edb651ae607b6736891df2b020244037fae6a816ed304398358c3adbe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae54ce8a56cfcbd7b84b7d41ed14f8d7dab0c97fe3cf38e57fec3fbb9f27139)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponents",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponents:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f4be277a15d4725532ea29ec39b528e36365c93d042f69bde8e2b01d9953d4a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f66bd8c0e8f0d2dadcb144418540549f33c15d66aab279ffd7bc7e001bf34ddb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8e68ea0773dad223dcd079e34afe5dacf5c28dec26708ae6e0546241d95805)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d2fb3f2a34d09b2587ce7f9376bbe730a3ffe1d6a2b59c48153a075668e7649)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd17889fe74a8bfd182cefa0654498360edbf7f622447153bfcb9ac546643e17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__424f9e249ed8f83d6c3844ec58176ee053977018b90e68e9110c4b043576ce06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="egress")
    def egress(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "egress"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeList", jsii.get(self, "portRange"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="ruleAction")
    def rule_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleAction"))

    @builtins.property
    @jsii.member(jsii_name="ruleNumber")
    def rule_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNumber"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97fe45f9f0e965b9c7237e3668fb6d264a38ec89fa128a0a079fd4e4d718cb87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__348fc1fb6ec2f089163f34288028a91a98ac1600ab95c81233b7eed327200d4e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6265fb00a864f41fda4355df449ee8dc41f6c3aa5b3c369c9f82900dceace44)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e248cc8a8e80e20cc765cecbdb16f850da0eba081f255948a40c303bedf1bd9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61aab0bb22c21f69adabb2ff87cb8ca778ce453ae322c104be0be254d7e2add3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41f0b555c3917f41090c62938ee564171206f133c983f7269f42b915183cbc57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9d22a789d9024beeffd62385c8eb12f129d7cb1f1a6606e92134e85eabab868)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a5bc582049c5ede51e9c08c238a4c6107cdffe5e59cc7134a4f2bbb9e1814b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ef42c7898d3314afaf31de3068c07316d02178d6be449aba16b8911c85692e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0621268f374ee4cc21466a16cf8dd666fa82c76548764e981f88ff7cfffb6a2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0553e227e7b9af03180791f8c39b8737d68506a666d3c1e2fe0b700aaed1a216)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae2f7d87c3c03a747bb7ece4a6011844eafdf17377cd51f683dbb40db5279542)
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
            type_hints = typing.get_type_hints(_typecheckingstub__444834e838f03f846aa1b58e4c2755ccfd5e44b1cd261a6e40014e7853c8b699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8685c44ba6440cdafe9697d6434cdfd1057668fa2a50a55d69f5007e8c153b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da7411c5bd20287d67b757835c8618da7cec9c05563681dccd0cca28cadf5261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__41e78bcc50fb8e2377dc612605695fdbb1458b7314d25fa514cacc23a328015b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fad8530036d26d3acfe2ed5ac0a00766df3ce6bc18c9dd0f1ad3121bbe5469d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2f7b99090631ae8a5c4417fb7b0e06342702d7cb7afa4a7774f4738b42bdc4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__26469946d325cc9c34836252e4095ab1193214ed308440339562641a4a449df7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9735019893692e7fe7ad217eb04694846022ae00577d79080f68a67897df180f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__223c47e44d7f04a4e6828dd990c41db59a2f8938f37d0a13c3f570f2dfb55a86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="additionalDetailType")
    def additional_detail_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalDetailType"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentList, jsii.get(self, "component"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5161303359d50ef78558bb24b3fbcf7fc96cf2607d34614a8abbef0d3e8aec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6540f1042fe7c1eef743e2133d72f831c8736fb4606e296d2c063a4c22cf00d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5ad8cad5d41a1e40d1271c49fc00f1a51d4285bc510652444eea59220782c10)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2500c6f0742bb67b0c8706c8ef35a1c66ff700976fa4ca048191ba0238253308)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a0766bde9b28d64b27693a1d9b317e03d419e27e1244a330e73635453e0794b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1634e561b0b6c99ecb23ae36ee98ee5b8794252a97fafde0fd3ad2e3d469599)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__595c1381fd26d8589517a16f63bd1b9a9d7fe88a10811d6939b249174f1eadf8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d4180f0c8be71b9a10a83a223c21196275e03704150a9d4a0347ee27cf66e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsComponent",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsComponent:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsComponent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsComponentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsComponentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bde7ca74d9cf62f876a01de46c3ca972acc29e95895c03cf2bb728a01af28519)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsComponentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228295db632405aaa03b0db9e5e4a78a45f3a04c7eb642818dd9741929a763c9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsComponentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a78d0fa4b393eab05b4deeee1a7e0f5ff4198c99d41cc34f34dbfeb9e7bfd475)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea743f74fc5869c0b8ba0c42ca5a08fa18a97f7a8c5a552eb057e8a80a6bd8ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3beb0f9aa506771bea17d41d3519ec8405107790e467d3a0ef231fe9599a7ffa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsComponentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsComponentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__124413792cca55beca969496d000b02d076a46cac0dd65cef4b0ffe4bb5c7b63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsComponent]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsComponent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsComponent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21dda7270983ed59192f8fd0412bf3169fd711e56d2f3c22556ef67d2e15df16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a35ab829a1ff7d8e57753e0cad310760b0d3b0f9ef8270acd183c3141d4a312)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fdd15a6be9a19b20c45ed26eac28a17702ae472f33dc0b88ccf258baba26ce)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bc63c904808517d5b073db22a46e43806b494a262fd092df194db6a113abb68)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c559768ce5fe1ad0a38cb02125be36ddb4987dbc9d572483631abf13266375bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11a5e3fae60a39f6fa7ccf5d547f1626882c8046de2a3473f77c71d0309015b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7540738461f58ae9348fc248a83232ce2e74bf0b6d4c3f2f8a5cbe8d4f110838)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d537707df8433aff34fc4109b3519bc3e47770406406b7f1fa7927b63f3dde8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed1925883f815d97ec40b7b7b6ffb63a7a2292d0d8698413783ce5b2008eb2e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd13112a37154d47e53f1990562f4e74fe66597cf14686dbbe2b034807b9008)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b0431fe548b39c8eefac368ff9b3aba6174aa30fa558f9d5844ce7cf7e6119)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a25d30e4c946c031599ed05bbec9a2eb18f93c2bc9d64f24cdf6b7cb6bf2144f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c307c88cfda76c2a0abe59cad79eb6dd6e27d3f12487fe26c4b316e15e204e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b17f3ed7bdc5c89c89cfe7a6d5691719445fafe7e9f84b7611ccfa9d364b5536)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b3972b34376cd03a778f08ec4ef2fe6ee384a0ebb2214c0c744870f4a6be39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6ef520db25d98f4c8a776991b89b288f6ceb7fa1ac609c85b7575dcaf69cc02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a12cb913d5a05f07087cd1989d8469dfe5951a9ddef5c49190a8c2ed768f00)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e184fc23ee6c63000c84e338eac8a761514a88157e238ec811e87adc91672f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ca3035307944a80e9d95c836e380d90910f798b46f5daff24a26d05e105c566)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31f42e5a030fb618f9fddec6e7bde490d6e12082a0d052496473cb1107828cf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4acce859190ff3b318ee0768a518ec8c3566bef0e57bbc51c8cf4b866dabcc1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesList, jsii.get(self, "destinationPortRanges"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesList", jsii.get(self, "sourcePortRanges"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4715102bc8bf2d6de1ad774493e090108bb9f1cfdad76eee9c4484f29346cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f1a003cd759706d450ba1aac96305eeabc31836977b35ab542b4bf2ce971ef9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d045dac174f586df0fc4d86375eb0be2e9bead5ad4004d6da63ee55618796664)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34a2412fc4975379b9f255f161fcd1496c4b2bf1834267b66aa389b1e6ac158c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f6e3cde4b5315f429b3e2fa1f3422f4715877255b06ea26393b108443e49240)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1adee8ef57355d760371a4854a9d00479a7341a173b306658da62731a19d6afe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4be1b5e8389af99fc324ee2949ffef8ec18bd779a019713e44a9a9fcafaddc78)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001f54309d8a4782a7785950d86f213a7ead3ed7ba9ab503b80474e46504b9ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ce114dcf3d825d851020b2119c8657c2984e979e33a3449da37b32a0b429ee4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a1b417a98a78c9a15f840927e4f0eb6fbd18526312a611bab4e9d187311e5f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aaa3ff7ca2bf183b2bdeeeda84aeeda5f398fc50b7152ae0f825d6f37bf9a22)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac6b9399450afa79a5a0b94046ee404bad4f0effad818358cf7d804dcb80446b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7923aac3e73d06b5aa4fbc2d2e69d4d80f85746e07f86e413d96cc092a8f114)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7091f228c82162cf092636e2e562ae64cf5653717cbd2e6ae58c9fe1862ed502)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adac41bf8253b76da87bdbbff0595d915285d5b42a1e4c0971e2e9724af15269)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0cda8d780364fa308add7b4d25fe5e6cf9a5829d0454762409cba595f3239d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d6b1323e19ef03dd45127aa8a38caf2740c038ca7b8234b5ad7e73e900623f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0508651e470515e42f47d337e1cdac88d384f9e6c5cba62c4c660d2beadd7f53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9b71f02073b71a89fbe1e1491ed43a58d7403d2ef1b4942f30bb02dd6fc737e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89edf4a3d8366ae3e234539c6b8e0b77c2939208b48e4498ba62adcb234b6d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d4a96519832910e03a07f1f50947a224ac9570b4f6d1275348360ee1b7d35ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8246a84e28b87851090b8e31422f40623b7d4a14cf02cb593a1ea7516944f37e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd54ffa4efb6bb18479c28bcf43679a3ec2a3a2092f9748124e7eecef9ecf6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57e0e41eeebc406fdbfcf665fa9291a9438dc4f219c6f7c82fc4d5217e00723d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d4924ad1fb81fc10724334b175560ff8bf721c23b9b7a7b04bf4614bf3dbce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e74ea36dfefaf9fd6d30ac25ffb94415d9f426f6b3931cd03557561e37a7b16)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesList, jsii.get(self, "destinationPortRanges"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesList", jsii.get(self, "sourcePortRanges"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f256899db22a4f58e8df4e4600186d5b27b298a223541069fba787d46b6381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__434d46943965a634ab34624c81d4088252387a94f58d4d52e65e5c93378597d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__397fd0f36e124c17e0bd2ec46b8cc1755711d52f5514f78f652091870e24a8bf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d022c28c50e39588f26b03210ea79192dd201d40bc4d1811067c76319967345e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94bbafebd23aee3534a9f6067fcc73fcf55044ce083adfb69df8b3fe92a8a42c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1b3260c4e61c869465bedbf9463094d00e5a6de62bc67b92dd87414991ec0c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__405f529a702f55a45516735b1d0de61e1eee5f3a1ebee663050757c1eed88c52)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e927eebf5ed374cfe9cbae7fa391ad7bab3c8c7402462efb9eafd7c60ea6f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c611c81a81bc8edf6a30f33f4f1ee60fd4be546663d88b57e60c67bfc371a018)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="aclRule")
    def acl_rule(self) -> Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleList, jsii.get(self, "aclRule"))

    @builtins.property
    @jsii.member(jsii_name="additionalDetails")
    def additional_details(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsList, jsii.get(self, "additionalDetails"))

    @builtins.property
    @jsii.member(jsii_name="attachedTo")
    def attached_to(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToList, jsii.get(self, "attachedTo"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> Ec2NetworkInsightsAnalysisForwardPathComponentsComponentList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsComponentList, jsii.get(self, "component"))

    @builtins.property
    @jsii.member(jsii_name="destinationVpc")
    def destination_vpc(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcList, jsii.get(self, "destinationVpc"))

    @builtins.property
    @jsii.member(jsii_name="inboundHeader")
    def inbound_header(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderList, jsii.get(self, "inboundHeader"))

    @builtins.property
    @jsii.member(jsii_name="outboundHeader")
    def outbound_header(
        self,
    ) -> Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderList:
        return typing.cast(Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderList, jsii.get(self, "outboundHeader"))

    @builtins.property
    @jsii.member(jsii_name="routeTableRoute")
    def route_table_route(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteList", jsii.get(self, "routeTableRoute"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupRule")
    def security_group_rule(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleList", jsii.get(self, "securityGroupRule"))

    @builtins.property
    @jsii.member(jsii_name="sequenceNumber")
    def sequence_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sequenceNumber"))

    @builtins.property
    @jsii.member(jsii_name="sourceVpc")
    def source_vpc(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcList", jsii.get(self, "sourceVpc"))

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetList", jsii.get(self, "subnet"))

    @builtins.property
    @jsii.member(jsii_name="transitGateway")
    def transit_gateway(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayList", jsii.get(self, "transitGateway"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableRoute")
    def transit_gateway_route_table_route(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteList", jsii.get(self, "transitGatewayRouteTableRoute"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsVpcList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsVpcList", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponents]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c10e5e29d145e6abe75acb7e82e7719906badbfbeec4ed7ecbb7ee600e989178)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0419df00c7c7911c905d1f4fd027a80b2c8497381dc2b3240f6dbe1d77f8d549)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac908d16996f2029b93b31de7cfcd672eed4ac5c67bd02afa11ef9ae35347a16)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9e901130ca7e02151823e58a71601ef98f09bdd412c0527605b1d37406baa1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eebea91f6708ad70477986a4f9cf4d4cb9491df84c7457bc0d927b04d027dcf0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__671125df71b2849bfd36c27d4d399f18f0cba1cd58dba0eb082e648de868c3b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c8e14848949f7790865ba624cbdeee245f80d58259436c7e9f82dffecd3e2d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @builtins.property
    @jsii.member(jsii_name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPrefixListId"))

    @builtins.property
    @jsii.member(jsii_name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egressOnlyInternetGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property
    @jsii.member(jsii_name="natGatewayId")
    def nat_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcPeeringConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a004fead97aa21a4f513b7bc9d41b9658bde3d37908bdd53d877127acb17d05e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a81782ee3d6701ae2df3b1b1254d45811976e87d3ff1c0e3b3a19cf76987b3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06379bba5da9bf89d94324dc91e3cafb7301d9bc2782fc4a4e853d4e0eb8f2e2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f655a7eccc702ad11c3fa6738e25e6e1204b01f3f1eece7ecad3eb7c3a1b6cfc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23becac4bf627143cd6832f02229a78fb51de888d5fd2670712892c4f03419e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe09285afe4da481b69fa079318c51fda0c384ef47bb1295aba52bc280e4cdbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0740da5bffa58180ed170f5ca2fd740845fe2a9c7a42cde6f07733003c8e940d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(
        self,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeList":
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeList", jsii.get(self, "portRange"))

    @builtins.property
    @jsii.member(jsii_name="prefixListId")
    def prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixListId"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5884c1af9da7d451c316ac4e69f54b45abd93f02817c253c145ce81af3ac2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb87fcaf2fd24e46a8f426314c90d687053d7ef715449f11acebcfd4d6785a6c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81e847b3fabdc4bc39fe67ffe891d0f3d9a68e8ef7ca95d704fc5d2de5b534c3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06962a6cc8bc50a538164c43d217ed1a46dd19862a66c7f8ec7be5dd2a6cd181)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1393a5653903979e67a46050cbcf0c6aa866bf6d28101f1fc5e7c03abf1f0cd0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7210fedaf52a763cf6bfb76ce431d1f92d66dc252a26faf5e76d108839d3991d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce5475c9b0492302efb311881269ec3a45effb760b4a7f4d1b115ff7a98b6e75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__607e454a84a98225b8546d650582eed840d340c2e265440f56c1ee6fd378dc93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b1b3582d65b120566d282af0c61bc467c0fa6b589f4f8c1463dfff92e0eff20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d028a08cab246a13af60dd02971c1c518ec70d5034db2310d280c57635e07df)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c9ef843f91df4ee280617e1b328f991a0b971ab750604bd905a293b2100958)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9dcd2d94457ad8b52fda514d7c3268e4e4eca0e41fa35e38186249a3864abb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3a89d97716470896ad9734a94d02c4df972868d094da6a64ca7f62ebfe6ac24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__892500af324598c03616a1a70b39966944920a2eff1ad6341b6416b45b46c77c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20ca86e2072d3daa249094a2b0475a3a68ddcdddee08cf2c96e59469db9e59fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7f55a16fe476f68b2b6f1e5d3583fe8b310964e09da0979f6ec2025c49b5280)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a0c3c82ab19ab9728fb13a542a634213f4c3078d2d05d521151a8cd6d27d20)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f7bbc646c1fceb29fa1d0100bb9e07c1ba389ae1c5be749044a9f5b7ea7dc7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e93efe4817aaee7a6e8d49b8670378dedf79f086a44807032439923fdb5d5996)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49fb8c7389b75abb618b78b55ce65aa0552ed172b2765b9d2bba199cd16e6ec4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7b17dab0058f5d01b359c1209afb579560a3f4dbd618c43d301679db55b4b05)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4edaf65645066706ce81c40778380ca428369ea08d8f9443010f8d274476f41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7d6b3fb0c8ea1e3a6230fd4436df198bb6f63417b61e636464e2bdfe01626b1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8126b68320e04aeb7b1d36474b78f4a5a447192f51b2a8dd0ff6dd28c8a9694b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__094bb46d39c51b73d51c91ae9ede4ab88d67667ea8892b31664e24deebc63f01)
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
            type_hints = typing.get_type_hints(_typecheckingstub__875506589d0deb262c7d18fd7eaca7a482ac9e2d2946feb3ac3e1a3e62f71dc1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6e38d90bc2be46a89e746948fc4fc65edbf2ddcc99f747f81cebd2d96b5330c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__064c3e7c1dd80dbaf6d5764145e8b97e383526fdcbb7b2179da232e815db777b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29ec56e3971f5b82b9e85748b1574344634ba6b2f2920440966c8613f6ec764f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80ad6d849c375d3e145c7f8d2a6721dc88bc50f768e35fbdf62b6cf8f6b8b3d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ca2fc0f7db76043480b4c2230654106cec1ebab5864eb20f00ba1f42c778ce0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddbf48723714de42c8a80866d7c6625a5c2857d7df5919b632f6f14a4fd2fb52)
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
            type_hints = typing.get_type_hints(_typecheckingstub__182d335112620921e6ddc2d06f2d93ae6c16f5ab9a25ee2fd80b243d720071be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2bee91a3bc4924655272869fc1e7be1ad946e605203703a82be5ec6d63d59da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfe9ae331adfd309fd67be795c2f9c055cead54e557e89ba70c2583fb0a47ba5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="attachmentId")
    def attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentId"))

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @builtins.property
    @jsii.member(jsii_name="prefixListId")
    def prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixListId"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="routeOrigin")
    def route_origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeOrigin"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__271c1052ca42fdc87512a761713331c4b7229678174275334071945490bcd05a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisForwardPathComponentsVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisForwardPathComponentsVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisForwardPathComponentsVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1c920ed90cee3d5f769428b86d359a0f25baf9ff752370cdb446ee0eff5d5b1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisForwardPathComponentsVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a066cd081a10763fba592f92576f9dd8beeacb27b5b84f3912b5bbce6b56e85)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisForwardPathComponentsVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e837dc88052bd081ecbb2abc635bc8d610b846c34a47e922dae9ab523fcb6b1c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4447d497c71b423d555cd93eac87e93680498cdc1047507a83c7b189877f0fda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31a58f710975006f3698c97afaef9e309f662c8b8fb1da97c04e943896048d62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisForwardPathComponentsVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisForwardPathComponentsVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4c858232f80bd85980c1b945efb2af2faf65a3d40891ad5df85f9aadab4255a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ca3c1439375d73a62395400fa8c58f272381f224a6e1dd2950ddc022aebe56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponents",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponents:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55b79903ffb412640f3b2f4879231d89e4a82af0b345f1b3be47789ba8fb1a16)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7babbe6cf0c610076fbc06a9d30607ddfad7f1739f957ab955b3211eeac045a3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b6cccf72ba39927009d4682b4d164aa08dd91482d4b0872f7b809f943516070)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ccee1ae7f51014f2adb193e2629489370b12b89d6d1cf08844ff9d95181ee64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__efbf4f44b5d801c77c3785dc931f0efa82162bda90eb31fef9cc367ea9b37b1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5507374cab857796fb56223b5553b57721bd056ba02f66c6f5644b557763da4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="egress")
    def egress(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "egress"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeList", jsii.get(self, "portRange"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="ruleAction")
    def rule_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleAction"))

    @builtins.property
    @jsii.member(jsii_name="ruleNumber")
    def rule_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNumber"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1900bdd0f749b41595f199e798c7f34e00385949efe764aebbe7408044f9ccd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b2f2eddceb48dffd37d5a8ebf3105f0630b5197023cd087cc79ecefcc28ba1c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59dad7b045940a8478c45e0948255bcfaec871ad0a4d02ae2f14767fbff133e5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b9149b03746b99f72df2c66dedcc09906e6a16f15cdb0c62417a0cba73c186)
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
            type_hints = typing.get_type_hints(_typecheckingstub__066fea93051007c9d029328ec536c8805c776ad4c460e590462d2af107f1ce20)
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
            type_hints = typing.get_type_hints(_typecheckingstub__37f6c088bc0b31a1cda3aa6e710aa412e6e8e58d981d0f3dfd191e70890cf2e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e5dde6cb702447da72e78186db630a849cf686521c2b3f49d0143ed48ec21f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ce2dbfb35bca31947da0016f9d3ce2dcbb03baf6aff513f0d748b2b1f60f45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d088d2d3a15b4e6e45365f5e19a54df8aba6996aa6cb5933df78cef73dc6237e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ecfcb496a955a33b8b23c5606fcd88d17eba079c75b5e1dcd242215a97a128)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64a63b3aa725d2503fa05fabfc72f83b2ed7cafd24a66881535eeff1f7a79f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfec89d586605a204e6bf894fdb630bce94999c148e4b5f48cb7a70ec5cec58a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dedc61f535dd23cf2cb5a9a17412138709f655a2f7bb609a1fac55f667ed622e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c68fc842c304e70a8068b00f0453df605753a107f99da92626273ec6a4bb4719)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a20848b0032624b154673247e6b0931c1c7e506d49bac2f73b6ad184ce9d72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3773524d5f80eacaf0b96e2f2c46d1b964b61619f71ff7b1f9a23bc4f10a7230)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3c96d030803ea830d7cdb5efd061c33ecfe2eb4b7f9211066c59c7f3f220acf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9027b1f18233695448389db94c9cd3745efc6bf7c59c510ae86ae41b967af17)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c98a0be3d6152deac8126d7580385ac96c83c0b0a861fe8eb889ff2454f5a5b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__680051eb37713248fa4dd68acf9d43f8419bea969166dbfc08621006fe34b50c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c2fbef2f2da8a9ad29355bf0208c33dada779fd2e257b61e2ec0bcc572ae652)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="additionalDetailType")
    def additional_detail_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalDetailType"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentList, jsii.get(self, "component"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d39af8e0b70b481fe5534ee2d1abe77d0741acdcfd5dd96936f223cc74b1662f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0ef6e319a244844a311194c1d9e526d29a2e257453c8088264720f30f32fa85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4f5ca59866f3b537f1a05392ebb50d819509a86a9805ba43b863f233059967a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc69f128c1add8e8938bd5ca5b31484a71c35759325eba415b565696165b981)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e096eefb1dd554fa7e199fda23aba126212e6f6d56ff18427eb803c851edc502)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf560b62191abb6233f0e0c0e3df658bb876bebedf43696f6cfc8bb55d7d1ce0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf9cf272402a18edf3f2645f21b7512081b021c72e3f93d5bca122142f5e704d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cc12d11d8c65facc8d3399b908a2a4fdf7ff6384b025b364f031638fc462552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsComponent",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsComponent:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsComponent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsComponentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsComponentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__936aadd331efe9620087206c3523034aff90609ccc31fe10ebb66fb6266a4a57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsComponentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deda44150ccd9b909c06b88a81b19f54f00ed49e101e566d512dd29fb467956d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsComponentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571f41b4b33b802844452b0cf4bf8351764236cf500a49f388d0ba4a686a28fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b216e35f2bdf8085f0fa3a47bd39b9b2bddc08fc3df64e0d214f7aafad849cf4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb03c12cf3bce02b65fabea8fe73db7187081871260bbda109ce5e080cf2426d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsComponentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsComponentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1921747ad501cca5d644d70cce27fc041fa8e0f6ff76c427b64a601e1d0b20c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsComponent]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsComponent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsComponent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c6f1bea5818b44edce7a1d8713c17e25979a89382df0f6a0406dc61bd0ff3fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0c787bda2910b7a612326f993e36a1c8c1c058c09e21bf6fe63fb4d3af3b80e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbfbd4d7bfa378fbbfeba32b98f355528d77fc70e69bc0c9e20fc5c00796d390)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3618eb97f28ef7008f65358860de9c6cc52cc520ab7bce88e79ee7247da588)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64047869a80dda64f76a5c3ed17b2190b761f216f41eab49e31538bd78026c90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ac955aa44f47551e8a3e5bb5131e6038b24e53373af229a11fea4be7453ecd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__caaa21155b31168bb417caa7fe4264234fef6b8fa6a7a6ee52bb86cc43e4889d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f3531dce65b675ac58f3867d31dc5bf38fb37a35dcc77f4c88d15c233a1adba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7885913b808fd2f3c6f2b3f63c1a503f54c2cf7d47a64ee09d5dea8dfb5c5448)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__235aaacd5ff71afd86d354616eeae2f13f8d9cd0845d509307ea9f3657660557)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa128936c6769b5c0a4d9af366cea8c93082c520575d182c8f4ea9db667abe4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cc91172b853a0f3ed0fd93dfca07fee4d57c64438ed36d30288dbb2ea78cea3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9aeffb99c16c96cafa57791a71297ab05f7d193e0cb2393d0f027c03637a2ea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bed68477e6a26f3b208cb49e6cf11d6b5b4a75c89cd1746aaa38fdd5d16a450)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf7d0e25515dbb738c0562d25ea541306821eea4fdfdd864372b01a6896044fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7338c0b75fa15b65de51bffbd6508d98261f1bb0f9cf242ee7618efc0636739)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35de65496a4092ec48b9ed7c5a1d44db06c1c88abb96aa57a4cc8e574b34e8b9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934c85f73d225e30068bd5666db82035383ee8350c532f6f668fe6f045c9fe77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c32991c84a57a9e8a1f8cf36cfe7a28fdf7671110cd11cfd687fb456558e135a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__152b2aa1f3c18076540493dbbb18c55204f86d2bb6d05a4998a8984cc2224bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7f3400f97edd37797c238b3b085b229f0b30e039fdd48b4eb49794bc6edbce3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesList, jsii.get(self, "destinationPortRanges"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesList", jsii.get(self, "sourcePortRanges"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c316d4ea0a3b0af75451b79a2edb0df58a118702304ad39eaec2822567903622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd47fd6e52765f0b68e5e1914b1de122cf71f35dc8e2ad98615fc8f4e219869d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad555313feaf95dd5b12f5d164b1a99427ea5f0e2ed1fa1c945179095f9c5eb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9ceec6b1d7b4f5c25fe905f4e0e2fdfcb51e8495d84f040deb87f2d8a7c5f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7a445864e2fb59aebf03d6e35db8cedfae76fe79cd82c0e11edff0fd0285679)
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
            type_hints = typing.get_type_hints(_typecheckingstub__951f61addf5a668ede75bb8f4bcc48de91309430d67d81bea105cf54b549c2f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f93aea8479d7b006fadb7be98aa2c75e73de826e1629b58877167721433eb72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6173173d22de599d968a36c827191b8edc686bf0775222440032538ffdcf6c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a34f12ff6faef1db7fb784b4a85f152c2b7709316b59b625894fc40acb50fc72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0bd4cada7916b120f9d04c7c8927e905f0b829dce9d7e1dedeb61d175989c9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03dc184bf8a65d6cce21aa0d460a30424e1f54eb6816cb6994651e4fcaa2ad9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__843befebf7c8224c366fd554faece47d4d0bb11d2b6cefd811cbddae52c51316)
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
            type_hints = typing.get_type_hints(_typecheckingstub__715daf8e5f6488ef6b1653e72bee8d8b5c1d3816cf93e0ec53531d46b96f4877)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44a90a1369a1c36b9b584ffa29580daffb63c9039c0906d3d5a4b440717d664c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f856f6f4b0e8c7eeb5dbb3715a47ab00ad7a945e95b765ad41049346780465)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab04ded0dda227f6accd52fbc349c1509cea2a3c5f0ad31d3c54ed9c5edb9a5d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d859f10b7d35dbf7a908e83eb113f155383d2b3a55d100f0d6b481d73cf52e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a01bb1d98a5ff70c05570663162f9cd8dad179e7f8eaa352ef9ac634ac1d2b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec92bbb0e02dc438cb8be519c12ef665a471398d123e18f73dbd51a562e96e35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__024111aa2346940ad038b5bd276d1e0f0c9a7325b31607f9ec8b65b1e9acb75d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f971ba2b5da275a5ee0eada730ab0e47ebac8801a0cd1a773682a8452a1d16b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0fbb058dfc547b7546311261b5fa9718801048d9366281efc426a3d75e4fcb2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ece56068735e37d71a1a7b707ca5ddb6dd27c76c43529a59a0808be831b720)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb0de2cadefaf3472ff5f7e4a37cd56c9fb39b3ffb342934c27fdcc6ef6b7352)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d599724ce155f1fe0aa156defa7d98220d417b97d967faaa506106956bca74d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ed832a8364603f5ddc34993a49262833f27f71c2fdd3335275a31c83b8274e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationAddresses")
    def destination_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddresses"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRanges")
    def destination_port_ranges(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesList, jsii.get(self, "destinationPortRanges"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddresses")
    def source_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddresses"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesList", jsii.get(self, "sourcePortRanges"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da1e17c8770aa54fd94620eb39d6ac9e4eb5c6bff77e6649cc18119beb148ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2a407c89223e6ee357ba94889f638c7b380f5762e7ee6d93e2c6d297013bb38)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7266bafd00003c528c64c71f81e8de36cca83665d6cfb23ede34ef28445ad4c4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ddebc5f3c938e1ba216b8f7217d182223067426ad09f0a029d7bf4b5ee9901d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f0c0c36cd8b046291ffc3c5f85f67c95c055c1c54be0620143b0ecfe8847a26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9a86d6742744dea70fe4004e7cdbe312986fbf9149bb962e49da770aaf9f548)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c7527bb9847a8ebf3e9c20722ab9b8647c2227cd00ab6d05fa2edde09005459)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1418396315c34ef4a0fad9d2263ddc8cb14872ff18d0eb4b820793ebf5f118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c8e84a7e052b5bd987cb98d3f6797a8ad5c3038b8467c3c30a3450babfcef60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="aclRule")
    def acl_rule(self) -> Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleList, jsii.get(self, "aclRule"))

    @builtins.property
    @jsii.member(jsii_name="additionalDetails")
    def additional_details(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsList, jsii.get(self, "additionalDetails"))

    @builtins.property
    @jsii.member(jsii_name="attachedTo")
    def attached_to(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToList, jsii.get(self, "attachedTo"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> Ec2NetworkInsightsAnalysisReturnPathComponentsComponentList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsComponentList, jsii.get(self, "component"))

    @builtins.property
    @jsii.member(jsii_name="destinationVpc")
    def destination_vpc(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcList, jsii.get(self, "destinationVpc"))

    @builtins.property
    @jsii.member(jsii_name="inboundHeader")
    def inbound_header(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderList, jsii.get(self, "inboundHeader"))

    @builtins.property
    @jsii.member(jsii_name="outboundHeader")
    def outbound_header(
        self,
    ) -> Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderList:
        return typing.cast(Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderList, jsii.get(self, "outboundHeader"))

    @builtins.property
    @jsii.member(jsii_name="routeTableRoute")
    def route_table_route(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteList", jsii.get(self, "routeTableRoute"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupRule")
    def security_group_rule(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleList", jsii.get(self, "securityGroupRule"))

    @builtins.property
    @jsii.member(jsii_name="sequenceNumber")
    def sequence_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sequenceNumber"))

    @builtins.property
    @jsii.member(jsii_name="sourceVpc")
    def source_vpc(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcList", jsii.get(self, "sourceVpc"))

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetList", jsii.get(self, "subnet"))

    @builtins.property
    @jsii.member(jsii_name="transitGateway")
    def transit_gateway(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayList", jsii.get(self, "transitGateway"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableRoute")
    def transit_gateway_route_table_route(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteList", jsii.get(self, "transitGatewayRouteTableRoute"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsVpcList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsVpcList", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponents]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e85c71e6ae7eb6c1594f89872f13c135826647e94b894f84cc42bb7c6040a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff1e4c20c743c37e633bd90863cf39025b7717377d42bef74e0d4864752cf07b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3348fb55492dc94484c817c69ffa820e3dfdee737b253ab4c26ea006e76714ce)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af364533894140107549222bba3af3b47027660b3a8482f047647572a1f1a9a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7db72a7b9e6cdd5ecbf9eb269843ecf2fec6daaecd4aa9da3801ff45b38a0d0a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__58a500f292d9a82ba2cc873977fe7d3316505c27c3847bbe18188a55e229f27f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be3e0af97bdbb48e433ff3ee6a09f73bec1e01c75c172c24a76b7dd899018de5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @builtins.property
    @jsii.member(jsii_name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPrefixListId"))

    @builtins.property
    @jsii.member(jsii_name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egressOnlyInternetGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property
    @jsii.member(jsii_name="natGatewayId")
    def nat_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcPeeringConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca18d14ea1b37c1646e7b54b8c78b7c5d850d569c9ba5d221747df09cc70431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__669c4c75c167d2f06cfb66afff51989a5c0f39893df462df093727ef01c300f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70a7d3c969132124d798eebe299230af1af18803beb799ac3e5e6b5b37d6252)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b525f5430c770fa4f53021e3a95113769b17b72100e258d12aaed0d17a9de5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c59d226088d34728b0c11d43b667d4f9aa7fa07760bc06d36769715e95ec1ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4155567af479bb25984f2850c4f0349285b3f99ba3736b1e0e7ebbf0bfea39dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__211a7caa4aa1a2ab8e1ced2dcbd8795f32580053451710dc47f4556216c4e418)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(
        self,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeList":
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeList", jsii.get(self, "portRange"))

    @builtins.property
    @jsii.member(jsii_name="prefixListId")
    def prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixListId"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb352b1be14f6bc517113b31cb1b66cf65e23bce947a060944f245b8c2ce7de7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c0c92178e86d332b98250813cdca2f66f7bfe4613a39a3a308bdb0989f40d6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37906ec4c65392e27abe141248001dca7b157fd43a2ca9a9007e98115f5bf1d9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c9000b47b63f49fd0d0e4bcbe8ad096aa4d7aa232e0b518bdd3ccd3b264fca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8486274aa012ed0b94c7a798414b5602d76c97dd0e25808d3be51a53c6495be7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ff9a0fa3f433da7344555112cdd9a8f46f13a946d06805191a844632e49cf46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d93cc33474a33ddd242c5456dfa3157493dcb6f0ee90856c125815be7678549)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e45fe142fc9d5b7a49f94949bb16fb0d51c16df80ff4ae7de38b5b9506a08ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cffc814a854c87d9991d39831d445e2c40a5107f53b0872a7ea7424d42f90d2f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae876d198eafd03cdfa82ed9a2364712674c0f4cacf5726ef84a32b66a559e24)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eab37869a86439d2ead2ce8f2a27e3f90cf39ab1430b88c54eef252255628935)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adb6fc833eb5d30c06c23e516e1c7b3f8d2f335560623d0731b1631b52c1152e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__12a0c2120558c4a8b8727338ef5917a66e0ffd662dbf6eecaeb175d08c4438b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c34b794815947ed12f1e06e7cc704286efb153cf12a1c2ad0343037a16bd3505)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9628f34ae88e98cc8cd05383198235dab0dee13755831c1c5c0b9535f0cdfbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07b38807689935914218b5766a9dd0f80a248c816b6ce587d438b346ee93a605)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4aacf2b88af744f07b215f53490f910639a76eea3b833fad1aa47335c13c80b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9206afe7b9d6f3d2ef1b3e9fadac0f58fd7bde93c58a93b98d58d988ac1d9c25)
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
            type_hints = typing.get_type_hints(_typecheckingstub__499691ba4eacbad9a297262bfe4151d1c681d5211111cbe70b05e800791f6bd1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c6a643006502a381a6a1b8812a4f8a2794db7b8c5dbb89b5076efcaf538fd3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6297c43686afb0e172138b0cac943152ed44bb1bfdec14bd88d23df2bcb444d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bafb3f2b59de161d6b8e8a3c948f08b3ae6f0b6727d8f06de757b96d9dcc973b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ddd7f3b3b5e59fdc31452ccc94d96e34a67bd2417a01a88900377e9cdbfcef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876352ae1974b771b94d733ace4d3a44340e2a6fa900b42a0d83ae78aaa8f3b1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c3d6715a9f11c98a88725467821031c2082ae44617485451ae4edb591f597d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4bc1fd60f4a002115a75749a515d8ff9206e28487fd1576d79c1e26a3ba6ebb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3e7d7ad8aba2733f09e645646bf50ea56d8da165d34b8e3ed8977168b3ed6d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce1d11bc46056e391236d346e67d58fa6b2da9d8f6e09d01e610304b9ef0a4b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681538e8a369f5b0789cbcecd29e04051c9b1d2d44e2077af0201caef48f6b9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dbb9364d84de0d2a83a865c66c443f2601dccb42aebdfda3dcc0724f7b835ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f54b7029b08e5dc14ebb2e76b0dcb93ad1333f4cbaa8bb712a38417c91596d2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01647d1887de46837ca00dc21b707ca7e0d7fab3a87ae18317c60e23c2004c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eed8fd30ed84d15857a50804803a182e592c3052a2b350c1b087eaff543bde50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__206f582b07792e0a684be8dfb33929607a4b78ee5bdd89cdb1bf877737423ebe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c25736989aa5f3666c59c5657548d35973ab58035c8ad7010b28e19506c2c93)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="attachmentId")
    def attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentId"))

    @builtins.property
    @jsii.member(jsii_name="destinationCidr")
    def destination_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidr"))

    @builtins.property
    @jsii.member(jsii_name="prefixListId")
    def prefix_list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixListId"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="routeOrigin")
    def route_origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeOrigin"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b4123de035ed385d3a77e57ec36ef424a834f617b26d401ba43b25439945d60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsVpc",
    jsii_struct_bases=[],
    name_mapping={},
)
class Ec2NetworkInsightsAnalysisReturnPathComponentsVpc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2NetworkInsightsAnalysisReturnPathComponentsVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Ec2NetworkInsightsAnalysisReturnPathComponentsVpcList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsVpcList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad4b9c6a1f8ed919eba6fa96fbbd1cea9bd5074e748f0f855abe63de75817beb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Ec2NetworkInsightsAnalysisReturnPathComponentsVpcOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0755dca0dfb7581daa9a96407cc17949d72e83a84b29167dec5b38262e244d71)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Ec2NetworkInsightsAnalysisReturnPathComponentsVpcOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16efcefa51060e868405d54bac16f267cf5cf13f6509170084214e678026caeb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42dfbfb3445f1f09083cb50bb98eaa33649ecbeb91b8adbccb09bbe6faa7c432)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47d97aa16da179187de9762c8d43cba08ffb7a865dd27cff2a14a1fb89af634a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class Ec2NetworkInsightsAnalysisReturnPathComponentsVpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ec2NetworkInsightsAnalysis.Ec2NetworkInsightsAnalysisReturnPathComponentsVpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a515bbdec62020aadbbd0b5cd967f0ba3d8c3b8e7a24a016f04608b8ea7704d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsVpc]:
        return typing.cast(typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsVpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a53ec4ef52c6a49b7198cc97a10f1b6646dc9fb422a18d25ba857ad4df9852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Ec2NetworkInsightsAnalysis",
    "Ec2NetworkInsightsAnalysisAlternatePathHints",
    "Ec2NetworkInsightsAnalysisAlternatePathHintsList",
    "Ec2NetworkInsightsAnalysisAlternatePathHintsOutputReference",
    "Ec2NetworkInsightsAnalysisConfig",
    "Ec2NetworkInsightsAnalysisExplanations",
    "Ec2NetworkInsightsAnalysisExplanationsAcl",
    "Ec2NetworkInsightsAnalysisExplanationsAclList",
    "Ec2NetworkInsightsAnalysisExplanationsAclOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsAclRule",
    "Ec2NetworkInsightsAnalysisExplanationsAclRuleList",
    "Ec2NetworkInsightsAnalysisExplanationsAclRuleOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange",
    "Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeList",
    "Ec2NetworkInsightsAnalysisExplanationsAclRulePortRangeOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsAttachedTo",
    "Ec2NetworkInsightsAnalysisExplanationsAttachedToList",
    "Ec2NetworkInsightsAnalysisExplanationsAttachedToOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener",
    "Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerList",
    "Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListenerOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsComponent",
    "Ec2NetworkInsightsAnalysisExplanationsComponentList",
    "Ec2NetworkInsightsAnalysisExplanationsComponentOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsCustomerGateway",
    "Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayList",
    "Ec2NetworkInsightsAnalysisExplanationsCustomerGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsDestination",
    "Ec2NetworkInsightsAnalysisExplanationsDestinationList",
    "Ec2NetworkInsightsAnalysisExplanationsDestinationOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsDestinationVpc",
    "Ec2NetworkInsightsAnalysisExplanationsDestinationVpcList",
    "Ec2NetworkInsightsAnalysisExplanationsDestinationVpcOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener",
    "Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerList",
    "Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListenerOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable",
    "Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableList",
    "Ec2NetworkInsightsAnalysisExplanationsIngressRouteTableOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsInternetGateway",
    "Ec2NetworkInsightsAnalysisExplanationsInternetGatewayList",
    "Ec2NetworkInsightsAnalysisExplanationsInternetGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsList",
    "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup",
    "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupList",
    "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups",
    "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsList",
    "Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroupsOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsNatGateway",
    "Ec2NetworkInsightsAnalysisExplanationsNatGatewayList",
    "Ec2NetworkInsightsAnalysisExplanationsNatGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsNetworkInterface",
    "Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceList",
    "Ec2NetworkInsightsAnalysisExplanationsNetworkInterfaceOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsPortRanges",
    "Ec2NetworkInsightsAnalysisExplanationsPortRangesList",
    "Ec2NetworkInsightsAnalysisExplanationsPortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsPrefixList",
    "Ec2NetworkInsightsAnalysisExplanationsPrefixListList",
    "Ec2NetworkInsightsAnalysisExplanationsPrefixListOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsRouteTable",
    "Ec2NetworkInsightsAnalysisExplanationsRouteTableList",
    "Ec2NetworkInsightsAnalysisExplanationsRouteTableOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute",
    "Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteList",
    "Ec2NetworkInsightsAnalysisExplanationsRouteTableRouteOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroup",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupList",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleList",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRuleOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeList",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRangeOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroups",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsList",
    "Ec2NetworkInsightsAnalysisExplanationsSecurityGroupsOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSourceVpc",
    "Ec2NetworkInsightsAnalysisExplanationsSourceVpcList",
    "Ec2NetworkInsightsAnalysisExplanationsSourceVpcOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSubnet",
    "Ec2NetworkInsightsAnalysisExplanationsSubnetList",
    "Ec2NetworkInsightsAnalysisExplanationsSubnetOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable",
    "Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableList",
    "Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTableOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGateway",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentList",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachmentOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayList",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableList",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteList",
    "Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRouteOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsVpc",
    "Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint",
    "Ec2NetworkInsightsAnalysisExplanationsVpcEndpointList",
    "Ec2NetworkInsightsAnalysisExplanationsVpcEndpointOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsVpcList",
    "Ec2NetworkInsightsAnalysisExplanationsVpcOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection",
    "Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionList",
    "Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnectionOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsVpnConnection",
    "Ec2NetworkInsightsAnalysisExplanationsVpnConnectionList",
    "Ec2NetworkInsightsAnalysisExplanationsVpnConnectionOutputReference",
    "Ec2NetworkInsightsAnalysisExplanationsVpnGateway",
    "Ec2NetworkInsightsAnalysisExplanationsVpnGatewayList",
    "Ec2NetworkInsightsAnalysisExplanationsVpnGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponents",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRuleOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRangeOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponentOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedToOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsComponent",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsComponentList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsComponentOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpcOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRouteOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRuleOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRangeOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpcOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsSubnetOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRouteOutputReference",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsVpc",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsVpcList",
    "Ec2NetworkInsightsAnalysisForwardPathComponentsVpcOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponents",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRuleOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRangeOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponentOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedToOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsComponent",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsComponentList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsComponentOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpcOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRangesOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRouteOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRuleOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRangeOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpcOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsSubnetOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRouteOutputReference",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsVpc",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsVpcList",
    "Ec2NetworkInsightsAnalysisReturnPathComponentsVpcOutputReference",
]

publication.publish()

def _typecheckingstub__deac98d837ea2b1c49b145ec071b636ca932821230d69f1395b9bad533c1903b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    network_insights_path_id: builtins.str,
    filter_in_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    wait_for_completion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__8b08f3b291326c415f8b29e217b725e1e91ba9868545e37b43c57a2acc7daad1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__920a9ed7b069a3c385416ca4f12fdacce42d898f851a3c19b37d1681115f3608(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985f5b0a60afaf99f650675e7e48cecd9d27d08d0adaa5757939a6717a962d17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55da799c4cd2151ecd3d19ad59f2c7293489f3c764f580e3991b4a187199bb4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7928b36a1e7a98d19f6b12e26b379246787cc6edc12ee4d5097b84bf2aa20ad(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7264a36bc4f9012edec9cb4d0aee7e6b72d43c1bbd940179446c8d6870320e0a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__468aef1539206d551e45f38084531369e1b8aa498d09b496dfac0bc2a72881a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6e5b3118709267370d1f00f56470327bc9ce3c46f85fc51aa11052d2a4c6dd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b1a7a34c34a05980093b3b78ff9aa62ad26531a28b1324a0695507808426c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50e85365ccc804664895e7d9cd4ae466399e82c25208b9211ed49c5d98a68d1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aadb1b54fb804aa3ddda96eeeeeb0ea4fd658490468eda4242dc4c9869694182(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8437497b9726a4c88a5b359ca53c99e69378f6f7fb2a543348f8ac618b97b483(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923cfdf124db6ed7954a520293136adb23b1ba5c3e99e380ba6341212f126a6e(
    value: typing.Optional[Ec2NetworkInsightsAnalysisAlternatePathHints],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83207caa037e2cbc4669b7713c7ec3e6088be1ac81ec830ac5e56205b8ee1a8f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    network_insights_path_id: builtins.str,
    filter_in_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    wait_for_completion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e00e127d091a2471646ba2ad55accffa448151ce8ac5aaf10dbc3beadf80bb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb553c641c5dbe5b29f4b2bbd8c51fdd3037528de9b732611df988c0dacc4f1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bdfcc58ff815dcf6842c99576a1e26c2b30aa66ea71a0da29c3d9ce758c1ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adcba8f9b6dc8164692dc3a540723c1561c755fe3e5bcb70c336f88b8a333cfc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d54885cc8b54552f1614f4d6d0a3ba2cd8e12f6871d6004fa768a50a03b8f3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced39c47c9aed448ba05078d4ed66928123a98f23ec13c4eb1a0b3a98ec05714(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80f98b9d7b95ad082f02ba8df7efdf13f8e65c458e6615860f590ad0d8cfb46b(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAcl],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4630348f906792db0a922de2f77402b82d9a6a8452a5e1af5e6a83832263bba5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df10f67c64f8673022a418c870ab36695e39213605077112626fb06790a8dd66(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c14bd3f2112a4c36b451cc0c9139bfeca1c35247327ddaf14a2bc15ccabce11b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b942b7d99aadc1767025844eb3d2fa528e159e39d560d47a27730bb807c4009(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33da141e7675aac2ec4bc668a049756ff2fa7bf7c1c44f238324f0c348f819fe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1ab732b603223d4531a2c417906d858d9e43a337b9a2d515d59ea73597f2a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677262bfd28f3c063237e0b9b314ec0b5eb90806246ded72eb9cb822a086e622(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea9ab160ebb2c7dc5ac35cf5f82228065224600cc93ff62972b896b30560ecb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa03d10ea14f3d7d37b5ddfc5fc1c8489b95e2391910556bd9d7f73b4b37684(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b3d763a845240be07e5f5bb0c026a1f747b8389e535137eee10ad51b585c181(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386dd27addf27b9c35359b1524be6088059bd7645c021c34cfefc13debe07ca5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4267c4090372157cef67bb26861aca7aef0f15b62fe828f0335684df284e2228(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46fb0a412f0c33b3c7493c6ed29bcf8430063e5d4caacf15a8ee520cbe0fe35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e57c806a926f35d76b9d43b6576c3d14ae530c043263faf4e90e03e504e059f(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAclRulePortRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f7aec5ef7355cd8f7f6afe29ba7ae03e88911c7b282000ca9df9c019b60322(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5288b0d0deb7d08d6aad2162a53c22f74a5b6f5c43f2d4b619b519091a54351(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92c7a938516a9442da7b23b89158f986dbe8ac01dbb796ebdee8b896ae700fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03841b8e2c66d734548d95a6df5f69fb222ef39d232f068edd0a25a510b54f74(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__950ba09f32ba2a91fd750152561dac4bcef5397686f65ef5f7e1cfdfa1bea7e9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89ceb161012f996d1464e8ad73bf7d42b0746876786541bcf4e75eadcc23ba0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31917d621bb43ea69325f484019700141daeacdd95ddb746b6064e8acbd7e256(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsAttachedTo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39051c58dad894057a8e9adaf939e27b677dfb15203dfcd930b2292738970067(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b1e1c3174b79e9a2699d2b5922c125ca8aba18c1437052e07f7a7a95d0bc0e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7d328fdc24f2c666e407b5acb8d524d683e88c63d278799d2dd9003b567746(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a74afefb8ba39c1caabafdf7aa8f8d809a9f82a4ef05f2046315c173dd8d70e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e6af4e373d1b1c29e4b792a4a63216f5b9361118bf6bb9147f35cf0c8a9ae0c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfd4d2195e53a1a4b7c44c880378097f536a89dcb5bd4266eb36e918769e055d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a6b25657eae7c15889ca2f1435a1c4be39de192667acaeb56689fce3668fd4(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsClassicLoadBalancerListener],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe5290fb6726adf3305ff07adac69a268ffd3c31a658aa5724b05fc821eb73c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fccc47a6004976c7d5623c71951cc44f9baa5518da04d7247bef0fedf850690e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d2d7021d76d644b768351e7151cf2151f4d2fe43a68ad0f12474416dc883e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860d1c15eb7d01cd3c7ea171cdd5e2d74ee84ccdec45df387c9b2604ffbbd2ad(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3ada9defb765f70b845d0721d3dea7768edcad817da96d26eafd136ed62485(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b26a0bb70a017fd6e75306eb0bb3fb9fbc95f728f01b16f447e45fd601501b76(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e29d49f259be08b555d95bb54ccd85328fd629244420f628ca8569e6f8977a9(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsComponent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af1c8e4ee7525a39d3330e638976aceb777602f6f03bfaaf3d18f95a00bb29b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d708dc591503f28f02233938156286628212c1d32fa3fe0027ded0e7ec915cf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f206b57a8ccace2b5ca803ff176275222e845c1faa5bcd3fb9919073458a01d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c08ce204028280561f0c2ef7b7e9f403218e637c5c2582ebf477d8d74df47f2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028a6782da2b45c9f3ff8cdc961f1d0ac416255c716b081145245317c1b37e92(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e595cecb431d5a28316c4fb8b88992d0915293a79ab71a5eea550d2d28cd357(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b59ddf4f639e1e02c72fe4b568ee66d1d72dfc0e9f62cd8b7a29cbc44880042(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsCustomerGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217f3b76bbf75c18e4cff51a47d4d6c7f37c35c7176b4be56b44b2b91a08215f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd81eeff442c23eac7ab3adfcc426ad7930b0275d67fa0abf8475b2b8395307(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7761fd6f88bdb40ea95313dd25688811918bd747b66c33d89c1c81cbe5d160dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a84d36e0eed8555150db781818fc3c98be3c9b1d519c44ab5afe1465161f23(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf5370e5fd14e9f728bdd3382acd336acf92d6a00ddaa8ac7d6123a19822956(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64105d79678de957a311431f77ab71a428d16a7978fb87974c027e0ae5f81bfa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e85ca6eecf3d115fd9eed72518e60dc9a45b2f6de8483dd3ef9ce821f9f746(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d42bc3146ebc83557bbaafdc1d5f271b39fb451419a2342415bc570609291e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ecafde75817e9b78b4bca0b38f6b94b56ad1306c46769f327806203ee88d686(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__144ca0f9c861a4b7d09729cbc7c9db1e5399c88b98a3c5709124fa19f269b79d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab423c9d7e651e8bbba49149fff91a544fc92c720a5553171ca220f92fb0a7c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eab54d68bdeac52347da4a24a4179ad673aeacfa82a317339245a3712a3d3216(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6dfd4e45e319f0f430bcc054aa29241d69b80e9e7c843c1cd323ee6f26f1e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76992de6eb384531972a375c3366be452c83f9d1ae4a710a96da3bef49dfbe20(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsDestinationVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84eb51b97baec7e063bcbb414908e0b813110e8aca7554341da006768d4a31c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd9668f9d5bda4c4225166a7e14f8498394c2a9783850322520128a4630eb1c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88e4397d7b7c6dc55098e6f177e6d9d9640862eaa0eccb4c7fab09668c413f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f80f40d5ea96f981f8799f846b6af5103ee07a31dc4df9d47061e8b3b36e7a7e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94edde884f5e1a78f56e82954f09c4a26df0bffa7a620184e39794dbd38132f2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7095cf12d68b82c006a0bb81aae95a6d79e22c45a756393ce94434e7eaab74e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7eb05ce3c624edbbd361c86de429fb4008119f06cb97def82b1e22269202e3(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsElasticLoadBalancerListener],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff613ddde15c1949fa1edbf282c7c3428af1e9a8e87db5b4be706068d46da472(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80717816dccec036b307bd838d3998f077373825e1b1397534380af388a6673(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e860cd3c10f7ad52fdb6850cfb00eff1965bc7af2dbdb5d59cb3ba8b39a913(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f3d39dc4830283347aa8c2e417b2e47f622f2e32d6507a2cd7680588a2cd77(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2310cb4095314ead9f1f7b32ec958b17e6a8ae78a072c686b898de436cba3c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1eb3da8e512224357e0f9ea556593f9d3501957e838ec9b9e698407e919cc9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341df15519ae1a748bbc863c31cca5163143b1b7497ff3cbdb6107f15a8414f2(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsIngressRouteTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1490999de57557fbd47caa80b089f0802fd9db2ac92c4d29bec7b197408d1d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__061edd55186614d6367013fcb061fc8a375268c9a6742bcdb46c83947494d501(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935700305a305091bd6ec230fa409146932afeb2ff6285f37062d07037fd4103(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb76fb8068adc3a003d57f3ee1c2686a5484dc00e25beff2331eb409ce0def7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__433eac513fed66509450ba329ccc3ecb305eab1ef3c505dd9ca6ea26ce0fd466(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36373b3e89714d04479ff4cdf76c1867c63a723131842c0ae31c1ce20f0afb9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df1b3f00a0251fdc4fa0a21078750926b7af2260f831ad267f7dfb3929937969(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsInternetGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1d11f35ee081c03d1e0e9791184de88a4262fd6a767088cb2ecb5b3264b7fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1acb55ec2ee19bc71e65c3d2e36787babb638baa71dae11c4434d9f946a93fcc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb99b384c5894ec9e4caec106ab51a6c5005c6ba41c5afa5c450bc0aa3ec107(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c672e7dd42913c8fcdb833a1346c43d84038cbb8a236ecd32da6b81e49bc6c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c76838a57756d8dc55588a33931cf789053256826e4460be0c59c3e53f2665(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c90e46b7020031afdf05a253466a3159fbe6e893ce586f2828996feb5a8459(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9252a67f5e767bbfd2be0c76480beacf671444dda29ff9ef221138e3a48b15(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebec78db77f705c6bf13cd37c3223078ba9bb42c2261f80ba7ec7b82551423a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2da4c69f280944d53ed9ad103004c71739e627e55ad79accb4847a549d3a91e3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5df3e7ded97e71f161ea643c431da8bd65eef44f4c910e1e7d444df95a4358f0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc40083c1f650f274f6c89699b8164d6ed873bf3aaf349deea19dc884ecc219(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5ac007ce60d3af23d12d5f65c47c1de98c1aea1a7de3d5a192e8624c9bbfb3(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12e86364e64e1d287322dc8a4cacf658475410bd86e315cf08c9a8cddd00d319(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a2e2cf605f661c7ae919fd116e9a3b3e1ac849eb15b85226b995866331b6aa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a0a26b3714c8c93d45f74ba3ef2ec0afb7330fddf36048f9d51dc8cda53024(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09602a23160df14cb2f273eeb63b87f70d8491a368135a3f1da160455dd26a92(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e2dcafff9796651d3609813a0fe0fd9272b9866dbd823ff1960b57e6cee04d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3286b2a74782738f571651e8d5c75cacab024e512223b7ad52937e67c4d894fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e89e617aadf544cf79dd969a76a59fa1591dd591d910c565c66a8f18b9c7a246(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsLoadBalancerTargetGroups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b1b15f7f4250d905b3b7d4b0d93163ae0a5325f83cb3b979d34f372495ad01(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1ec7c9936191e329e1bf71b6173ef02d4d0907ec3931453f234b2d76b6b9ba(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1204737b174409da526b5f681da2b0419570ae7178b5557ec14b6defff5bc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060663051e4c63e62fc467b7640ad4fed582da4b2187f2d273156fc522ed0df9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4c67ad79ce71c45bcbe296035b38ffd87bbfc72c5f25af27138da154981dfe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5622d744828f4c017ec64e5d97ea82b8c65a5d9cfeeb86a37af0786e87dc0fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b96101bd9986cad80d58daf4acf5fd88173a5dc0e5185242adc296bb428762(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNatGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e87ba7d3f000d71519a129a02c0a5ee099a60fc20778e8b3cc8a047c542ee2d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ff2991cf6ed42d18ca18dd39840db500634018f82acb5cecf1e32305920aae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__880d33422f4a191ff9c885fe77f4d6bceba183569e774f83db205fc2d62849bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60831f56d8c75270b864ee808b0e0f9cdf5325baf57bbda49cead6a2f0712748(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21b7eb66a736697d381242438c3275621dcbd21f189d267e9756873c39f5902(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69eb73c5998f3b7818c0c52d8add3bf71ed23d0271d296b219394981e3c6acb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39139e132824ad1013f3908950cce95ccda644b0a7042c7ec1347067b8837c72(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsNetworkInterface],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c66ddc9193c81e8c3afaa742dce0ff0b06f4f590d0b34d35961969fa4f52711(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30986f961fd562f3ba3a2f13672dd1327c330764655838390bc99244fafd1317(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanations],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ca1361f685ebb153c47e9cbfbd3c03ea1ca6b22093dc13dc3f6f4cc2d62646(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939ac38bc367bf96c9557ddd8134870ae176817acfd52807b9681cbe292378d7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2223ea04b1580abbd729f1796438766e1ae6d763c1fb565d84c2552b89562ff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e59c6bda99b2673ba0c60b922a3ad12927416439340f66907748568dc48cc8d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e0d5e9fb23d198796ebf3cb2b78f2ce459cc8150e2cd7e7d40793250022806(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdde04b0836f5db90073581be49347ba7b5aad798e84951e077de775b72980c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869279dbce19388d1374d2e4babf8a5893afa7769c9aa7e18713dadd83fa39bb(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6b0a3551791e2e626ea150fad4954390874f88b6d7032b4fbce014f10599e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff05c97eeba7b719b2b94c74f22ad3a49e92ddb758b446787c8a660a46a5729(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06284b7dad72c4c13a8bd1caf749e870eabfc807e8145443b35cd289bc655756(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8725c4d5ee57d4b408f63dad098f35bab9548c304b6c543862a97206b25d4975(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7278991bfc67a76a20fab5a0953bffca0c25b8749e03f1aa8e7c0c9cea875b61(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d44f282406055b81e42b21e1a4ca426befb0cff347434929c4df18ce7f911499(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41382916ff286e736dc67714ae7cf29fc71b7ddb2e80c5b7442386ea7610742d(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsPrefixList],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d2a288e628807536be213c6aa2aa0d3b295f23e5c8b883a30aadf8ad74580c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b95882876bea4ba97126ad7c151c956b109a83005c16ff365adb6859bf71234(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ee376141cc31dea4839f75d3d07f6ff342c8fd54eba928f61255e8d30c77a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e55234242b1a3fa19ecd9e4eded1d05a14c768ec8462f84a45f30ae0230041(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f2e3626f845e40b851dd71edb5ee4acb9fa24c5b732c0eff3c943dcf46ac18(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cd196cd7a7d3dc45f85cf737eb8be2fc317a121dfed3eddf35e26c7d1f8040(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6ce9b08be87d1a187490c1f725fc188f0c2138a1a1fd36cf919cf4430f056f(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d1969036e959f89bd7a3a741b75f9b914440d7eee9170f82b9ba246608199c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__132121932254c6561cd8cde4c27c41dc9b3b36df725377045edb52851f01cc8a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408d2186aa88b811ad46f11ff283a02c87e6965d829a803259caffafc276d5aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db5da1242f6be408746d24fa7b47273763889413b3c3ec355fd169bbba41c930(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35156251133d2e33f59e214b37810cfbe7755b265fe1f0983fea42aac3f32de9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2938e8dc7cdb92a859b990ba149385daf3a7a546dbae9885606bf524b8cf00(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0582e54bd0a055e88c0fec776de2d64d2730e3b29726c173028cb81819d3475b(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsRouteTableRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ccddd48ddd9318091dceaad43eac22c5396619b1938eda6d15cffa335b55e7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc352212047d3c2869767c02d741d34cd4ccb04c7733de76db0ecd77c78230e4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf578d3da75436cf73dd8fb2c16d9f856719e29221b11832748f7f7cdb1477a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7125d926386be8828d02c9dd8d376d852a9aa34e9a57d47be060619aafe8c81(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa9cfc38e1143098cfa657f31c63a1e5c7e533e1bd7cef7ad2e3cbd01f26eb33(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115f7dd2d09b1c1b21ffe054d13259966cadbccc6e042e3e2f415185f54f8e58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61880eab9ba8d0dabc570e22ae29baab8ff4c0b568f904bbf0aab69762c94a89(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__310f6ad29b8e9d25a5464361e594948695c88f5a18db7084870ebf3cfc1f74df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad92be3314ba73cc6f9f353d2858d4a1f318c8372e31a61e43762a8cea894158(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c18a3ecb6c80dc1d319e5b03bfefd1746b5d398bcf175135327d36ea6fa29ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__080a8e381b1cfe9ac3d38ff95576d0dbcb1a164b84870cac4119b1d95bced14c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a223ca46fa50a949ac675995130402c7e95e82a11bc0ffbeb22bf5aa5d2d68(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eaabbc1f619e8ef422a60c979b0b1beab304c9d1f2c052ed8443c43661adc21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb69f0d0c8c6738f693628d325f7d3129c851604d748e7284ce66c028ab7e8a(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c7cbcc5fd1f78186d7fbbe586a2f77b0837780c760f5e02d93651761038681e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f5be533dc3b0edc73a466b21b9e61938164c71a519416e9628b1bc67bf1cde(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b76ef5fd84f8db465ac8e2fea7904277151a3c03be3923de26158f34e5f818(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb2dd473eadc698cfecb5c9a0f6f05483e2d75fcdee5dac564ce5baf0604efd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cff0a51ce46f68dc5ede1ec38623a32d939af7bc61023a2aa5718c254c53706(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__729221115b58e53d200e65489ca888c988881ef94f273c0397c7701f949f3578(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae5fe01652db88ca3eb5a302a0d13f7b63e418841e410c8464a3e8257165969(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroupRulePortRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__316f51eee3b940858079874102a4d119e8e3ff838d15ff47f9bdddb0914eb94f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84785f70465bc139bb1d12d4a93878600c8a25ee5465a0aab55fba3a6d024db9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0fc8d2ed04a9228f369713a65f8bcdd5d2f74fe5c0a879d69287c52df2fd01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b08d608faf735a28a5e48601c53dbe45dc19cc3449d650a250d5b5b7d8b94c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__202e466b8fcc3324fc47c0520daa111c4518adc86b4b08e6919576d9da602279(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7537d2d76a7f0255d9b3ba6c50b7070bea2bcff26ace93b3e108b4f0a8e983c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4da8422cb66a340a00cfa48f83f8784e60c44aa708fd631d8ca5b369a927005(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSecurityGroups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc8c21335d161fad7bec637bb8dd9391d57b99df971e79412bd91cb763ce240(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c868bf9e41da02f9d8c110896fe59c95d1faec88df53b84eb1d51711264c9b4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be089f938ff12d4721d600f1e7519f02180c6d9504a7ef341cdf65a1e96a36cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8482056be6e3a18405f80ca2571f84e5ae60e71ffbbc59a9b6662a3481bbd832(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e77e72cdd3e6f8c1f0ae9964a27b9d1a3cf03143978e47cc1612c60c0753194(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da25ddcbb7cb3a2c506ae811360abc14b2a3501ee99bf9b134ecf7677e97e1fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14d54d573cd9ce38a5b355ced53f4b22be963a227a22b65e8631139a182bf86d(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSourceVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__649a4008d740e0542a544d6e01eb1b2d0a502c70697263ddca64c85ad02af04d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb451d8efc0b7e309eb8813b7a4feb4f6a6079ae98a0a3426f984fcd19a44b37(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7342a911660807a8e723af8c5c99ed7c1798a99ea1f3b92332431b1c70f0a235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c742eb49d6c4a6288d10c43c212c0c85ec2d40702532f7e827a800dcf93e9e66(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b35d6a42e2cc5c8f276d06ecd4c455cc98a707dbfa7f4cdc3f1c26de2ecb2f26(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c5fed2ede0382f2b9f1f0aec46686a02e664973a76dde36c73842125e8b587(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c3a106102c8e10de8e3637fc88d7d7c63b0b718929be6a4c36a9589102121a(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2c09508b4e2ca80cd7d964389f802ea918ac9730fed1c3525cbd24e65b37c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6445800c000e8ad483bb6a5acc9dfde368c1041c85c24255eed32857f22799c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a3ec24dd3993641edcc0580349badeaf776d3665d038412b462e7d0b3fb99b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ea3b38d3ac5ea5082ce2aea33885707bf5bba8b697cfea8b64a1ff7fbb2ca0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ac4863640cae7760b730861f78018b0fdcd5bea47987652c7df672baa1ff0c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32bea34e89c7ecac6cd7279f485e5d13046d6656e9c2dc5bc65988dda2a8e6e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc838cc27b49d6f2be8012a7f2135441679fff4e3e513e4ddd60d551f6c122eb(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsSubnetRouteTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d910efa4473c9424e3eed9699e48f561e32fe9c16342d04b5eb6cefb0c6aaeb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25de659ca2f6865b31f2c0d37a0b56d91f4cfdd241decbac7283020ddee0b22b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cb02d02a1ebef1ee3636477e68879b2a41fc662405fdc0b35215ba2ffd8b8d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe5bbcbf58bed1f1abe8219ed3e6401991b9bbe5eca58df70bcd6331d4fbaf3c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d20ec74c6ebca3c897ea359edee7cd89f5640dfd6c07b7b1050fdc72fcf8391(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9bd27b7eb66f13f0ce3c869be18c2c7c9430554a3f992823d3364812e69d64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a28211fc1c5cdd818b636bb1707a22b97bc466549945748ef45379f696baad(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayAttachment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5278ddb7ce5ad6c889276e3f79357fd2be0457be79e23c1c73de3fdd28a53608(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d587ed0410836fdfa000748623d31aac47bf3b6006303badf691dbc13c130d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110a52cc19a3a09c78e76d9a43a73dbd248c3e5b33fec4534d5600047611dda2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f2743db61544e1400e4de2cc4c69bfdb82b545af6fdcf4d6591a814d9f00e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36bddcf5c9827538edac36b7b63478217020f89f4056317e041582132f57d24f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393b51feaa174fe08b947aa2fb6113e958f15c863a99abd3e8694371c14a945e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c1a7da2e0618ea18d626c986566ff91fab078d3c5f572e1edef4e14f3b1e1e(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fdf804e39d9628d459f4f1362da6436289f39a9a87d43b4b6a07319b1296ba4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa8c4e0eed539f6578326569afcc3533ecb8d06a736fa6bfb1320ea877f8b366(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fef2b40b30da985993a6b228a0a7a4bde7032dc88166ea98fcfb1385f9ecead(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d0e5a68169a67ec76b62b5a3b40bff34c61e29b6a7d6178df989f6274df46c0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ec20593586d486ad413c1794c8b939f826973027b5559603d978c91377250aa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4f75ce4dbbee3751f4c11ff26098be5159bf4eb47a2242f483ee8913787589(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2d12088a0f8b0a7a647653458c8c0384c02ba23af8a3a2dcd6faf8acb6d1d7(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__288f8f74fa977aea1c6f9258dbe2807f9b5e473aa8001bba85ac39bc7ff3b825(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9aa2537f9fe1b0189fbe6b2d1fd36d3f6e9921e8f37fc6cc15ad461d64c261(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77dee7f8d6c336ffe3d4a011247796593a0569d0fc3c0ded6aba77419b634208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2d8c73acaf2b25ee6c16a49c83e3de786a9439d7d2f79f5a428f61044e1f93(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4275406c672833ed2ce54bc97cca3924361dda2c9f89fb14029b5815dd2ac51(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c91e1b654952812aa29c5d1b154058c74516b288af2c0b7e61381ba10df106a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6e5f2974a19ef4fa334ddc1c9b8cc33eff91612a5c9e5a0a855522b25cd393(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsTransitGatewayRouteTableRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf4f9c32cebdfee35a00693e7823d47846213be4bc80aba3b9a0973012f9ad2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd82022f2747217fddf0b6dd5d1d713f99a48ddb99e6fb8cc304aa17117b46e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a1296e6162eafd549040f8cad7824439bfcea39e0110bec1052cf4e5fc5fe9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92ceccd18bfa5d0747064b593917bb1d8a22d793e081637790c79c901d7cef7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a587ae680eb13388a0185679019ee865671d60b2ed19ca4d1bc84e3c0b695f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af5ecb563806278e8e9b4c27595268336577f059411cfa8934807b185c94295(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ae11856ea766a17087551516583e3eeb31f885604f965c150258bc5fa0b5d7(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcEndpoint],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d44eefd41c06bc992fc7ecc33e231b0ae1c200534cf9684097bb6864c89c2e14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0c74bb7e17329139bef13b0454ecb6210d286b982f0c4aeb536bdc2ec9d8840(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0072df1a940f28a6016ca29550f1fff128104f90b08a0e47591909a2ba40fe7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7139cdcc4931efc79d9d31d48afa5ad230c3d5eeda6c71b271e113aa8a1969ec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754034c93afa04c492be10a14644ebaef143a96b2a7e98ae7ff71ac1f5c77d8a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d579719628aa3d1c3f2bc3cc7ecc9297e196bd465175179b7963e9810cacbc68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85651662d87d1f75ff160bfb836be770f305f0c7117a0fc99d1fb9ead35a5f7a(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08818c3e288f143d2450f9976fc2e05e766c1ebedb656a12fe33249ea20fb423(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37eb92c0710cefe0175bb9a38118799303da9084ca96bb543cdfe4a8beefe0c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a9c484483526d6179697cda58d6633418dae3f2337fd83974bd54008b7f985(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d775167741428845b12324b9e7250eda0cf9c204d32ee5ae2f2e5e7cb4fe29c0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de6723b9d24697fdbc2a74b10480306a5a2a0deb44508f655046565096cf670(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a40c6c2c6f4fca30b84abde5b8ba98d4e0612fb11360f4bb2a2266c2804b6ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e575ad42ddb24295a6f70d5db816fd34351c6197139a69a0a44495c3f4a08b(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpcPeeringConnection],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9503dfb8343c87a5a4de9e920f27c12ceddf96098d9a260080aa4ac80b8d488c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018037cac3a14d9bb330a8dafab5b9fa03ae63fec506a20ed6606e83d7cc54e4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1f98f830a16d1e7140c21df9228eb1d79dfc408b80c4e8a8c094d9a785bddd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af659cd17b05de304b065531fc293d09f1be579523bc6091169609a8cdb922b6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64dba961e0891823c132f4de79c9b1f24dcc60bae5d4acc03344f1d19221f320(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242604dc41034832e387191f7034882d7728620a16c7c9b16b228f3b75db780d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a978464619d0ce6b99d9e9008b2efbc797b03238713bf7acc235a6295820e354(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnConnection],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986289f7778b5e76c44604beb1b709ed9bca27da3f6220f6d834bfb258f78ed9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b5dc5c2a0a5a15ec3a208b127523fe76edf45ac846436104b9518d840d255d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a47f1babff3d5bcb66939edb7def440e9648ea574a5392a40541eba8e38f9f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9769f7cf24591e3d72819d64470ec175136bb68f06ccd076bc16f945e51b02d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb5f8b18ee9430254b3aa9547d286eb734ce158e04c1dc1bea7608bdd03edce2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c35b08edb651ae607b6736891df2b020244037fae6a816ed304398358c3adbe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae54ce8a56cfcbd7b84b7d41ed14f8d7dab0c97fe3cf38e57fec3fbb9f27139(
    value: typing.Optional[Ec2NetworkInsightsAnalysisExplanationsVpnGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4be277a15d4725532ea29ec39b528e36365c93d042f69bde8e2b01d9953d4a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f66bd8c0e8f0d2dadcb144418540549f33c15d66aab279ffd7bc7e001bf34ddb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8e68ea0773dad223dcd079e34afe5dacf5c28dec26708ae6e0546241d95805(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2fb3f2a34d09b2587ce7f9376bbe730a3ffe1d6a2b59c48153a075668e7649(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd17889fe74a8bfd182cefa0654498360edbf7f622447153bfcb9ac546643e17(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__424f9e249ed8f83d6c3844ec58176ee053977018b90e68e9110c4b043576ce06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97fe45f9f0e965b9c7237e3668fb6d264a38ec89fa128a0a079fd4e4d718cb87(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348fc1fb6ec2f089163f34288028a91a98ac1600ab95c81233b7eed327200d4e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6265fb00a864f41fda4355df449ee8dc41f6c3aa5b3c369c9f82900dceace44(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e248cc8a8e80e20cc765cecbdb16f850da0eba081f255948a40c303bedf1bd9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61aab0bb22c21f69adabb2ff87cb8ca778ce453ae322c104be0be254d7e2add3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f0b555c3917f41090c62938ee564171206f133c983f7269f42b915183cbc57(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d22a789d9024beeffd62385c8eb12f129d7cb1f1a6606e92134e85eabab868(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a5bc582049c5ede51e9c08c238a4c6107cdffe5e59cc7134a4f2bbb9e1814b(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAclRulePortRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef42c7898d3314afaf31de3068c07316d02178d6be449aba16b8911c85692e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0621268f374ee4cc21466a16cf8dd666fa82c76548764e981f88ff7cfffb6a2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0553e227e7b9af03180791f8c39b8737d68506a666d3c1e2fe0b700aaed1a216(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae2f7d87c3c03a747bb7ece4a6011844eafdf17377cd51f683dbb40db5279542(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444834e838f03f846aa1b58e4c2755ccfd5e44b1cd261a6e40014e7853c8b699(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8685c44ba6440cdafe9697d6434cdfd1057668fa2a50a55d69f5007e8c153b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da7411c5bd20287d67b757835c8618da7cec9c05563681dccd0cca28cadf5261(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetailsComponent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41e78bcc50fb8e2377dc612605695fdbb1458b7314d25fa514cacc23a328015b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fad8530036d26d3acfe2ed5ac0a00766df3ce6bc18c9dd0f1ad3121bbe5469d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f7b99090631ae8a5c4417fb7b0e06342702d7cb7afa4a7774f4738b42bdc4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26469946d325cc9c34836252e4095ab1193214ed308440339562641a4a449df7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9735019893692e7fe7ad217eb04694846022ae00577d79080f68a67897df180f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__223c47e44d7f04a4e6828dd990c41db59a2f8938f37d0a13c3f570f2dfb55a86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5161303359d50ef78558bb24b3fbcf7fc96cf2607d34614a8abbef0d3e8aec2(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAdditionalDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6540f1042fe7c1eef743e2133d72f831c8736fb4606e296d2c063a4c22cf00d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ad8cad5d41a1e40d1271c49fc00f1a51d4285bc510652444eea59220782c10(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2500c6f0742bb67b0c8706c8ef35a1c66ff700976fa4ca048191ba0238253308(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0766bde9b28d64b27693a1d9b317e03d419e27e1244a330e73635453e0794b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1634e561b0b6c99ecb23ae36ee98ee5b8794252a97fafde0fd3ad2e3d469599(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595c1381fd26d8589517a16f63bd1b9a9d7fe88a10811d6939b249174f1eadf8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d4180f0c8be71b9a10a83a223c21196275e03704150a9d4a0347ee27cf66e9(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsAttachedTo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde7ca74d9cf62f876a01de46c3ca972acc29e95895c03cf2bb728a01af28519(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228295db632405aaa03b0db9e5e4a78a45f3a04c7eb642818dd9741929a763c9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a78d0fa4b393eab05b4deeee1a7e0f5ff4198c99d41cc34f34dbfeb9e7bfd475(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea743f74fc5869c0b8ba0c42ca5a08fa18a97f7a8c5a552eb057e8a80a6bd8ca(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3beb0f9aa506771bea17d41d3519ec8405107790e467d3a0ef231fe9599a7ffa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124413792cca55beca969496d000b02d076a46cac0dd65cef4b0ffe4bb5c7b63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21dda7270983ed59192f8fd0412bf3169fd711e56d2f3c22556ef67d2e15df16(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsComponent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a35ab829a1ff7d8e57753e0cad310760b0d3b0f9ef8270acd183c3141d4a312(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fdd15a6be9a19b20c45ed26eac28a17702ae472f33dc0b88ccf258baba26ce(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc63c904808517d5b073db22a46e43806b494a262fd092df194db6a113abb68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c559768ce5fe1ad0a38cb02125be36ddb4987dbc9d572483631abf13266375bb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a5e3fae60a39f6fa7ccf5d547f1626882c8046de2a3473f77c71d0309015b8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7540738461f58ae9348fc248a83232ce2e74bf0b6d4c3f2f8a5cbe8d4f110838(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d537707df8433aff34fc4109b3519bc3e47770406406b7f1fa7927b63f3dde8(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsDestinationVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1925883f815d97ec40b7b7b6ffb63a7a2292d0d8698413783ce5b2008eb2e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd13112a37154d47e53f1990562f4e74fe66597cf14686dbbe2b034807b9008(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b0431fe548b39c8eefac368ff9b3aba6174aa30fa558f9d5844ce7cf7e6119(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25d30e4c946c031599ed05bbec9a2eb18f93c2bc9d64f24cdf6b7cb6bf2144f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c307c88cfda76c2a0abe59cad79eb6dd6e27d3f12487fe26c4b316e15e204e2d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b17f3ed7bdc5c89c89cfe7a6d5691719445fafe7e9f84b7611ccfa9d364b5536(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b3972b34376cd03a778f08ec4ef2fe6ee384a0ebb2214c0c744870f4a6be39(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderDestinationPortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ef520db25d98f4c8a776991b89b288f6ceb7fa1ac609c85b7575dcaf69cc02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a12cb913d5a05f07087cd1989d8469dfe5951a9ddef5c49190a8c2ed768f00(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e184fc23ee6c63000c84e338eac8a761514a88157e238ec811e87adc91672f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca3035307944a80e9d95c836e380d90910f798b46f5daff24a26d05e105c566(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31f42e5a030fb618f9fddec6e7bde490d6e12082a0d052496473cb1107828cf0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4acce859190ff3b318ee0768a518ec8c3566bef0e57bbc51c8cf4b866dabcc1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4715102bc8bf2d6de1ad774493e090108bb9f1cfdad76eee9c4484f29346cc0(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f1a003cd759706d450ba1aac96305eeabc31836977b35ab542b4bf2ce971ef9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d045dac174f586df0fc4d86375eb0be2e9bead5ad4004d6da63ee55618796664(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a2412fc4975379b9f255f161fcd1496c4b2bf1834267b66aa389b1e6ac158c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6e3cde4b5315f429b3e2fa1f3422f4715877255b06ea26393b108443e49240(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1adee8ef57355d760371a4854a9d00479a7341a173b306658da62731a19d6afe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be1b5e8389af99fc324ee2949ffef8ec18bd779a019713e44a9a9fcafaddc78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001f54309d8a4782a7785950d86f213a7ead3ed7ba9ab503b80474e46504b9ae(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsInboundHeaderSourcePortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce114dcf3d825d851020b2119c8657c2984e979e33a3449da37b32a0b429ee4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a1b417a98a78c9a15f840927e4f0eb6fbd18526312a611bab4e9d187311e5f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aaa3ff7ca2bf183b2bdeeeda84aeeda5f398fc50b7152ae0f825d6f37bf9a22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6b9399450afa79a5a0b94046ee404bad4f0effad818358cf7d804dcb80446b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7923aac3e73d06b5aa4fbc2d2e69d4d80f85746e07f86e413d96cc092a8f114(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7091f228c82162cf092636e2e562ae64cf5653717cbd2e6ae58c9fe1862ed502(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adac41bf8253b76da87bdbbff0595d915285d5b42a1e4c0971e2e9724af15269(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0cda8d780364fa308add7b4d25fe5e6cf9a5829d0454762409cba595f3239d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6b1323e19ef03dd45127aa8a38caf2740c038ca7b8234b5ad7e73e900623f2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0508651e470515e42f47d337e1cdac88d384f9e6c5cba62c4c660d2beadd7f53(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9b71f02073b71a89fbe1e1491ed43a58d7403d2ef1b4942f30bb02dd6fc737e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89edf4a3d8366ae3e234539c6b8e0b77c2939208b48e4498ba62adcb234b6d5e(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderDestinationPortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4a96519832910e03a07f1f50947a224ac9570b4f6d1275348360ee1b7d35ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8246a84e28b87851090b8e31422f40623b7d4a14cf02cb593a1ea7516944f37e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd54ffa4efb6bb18479c28bcf43679a3ec2a3a2092f9748124e7eecef9ecf6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57e0e41eeebc406fdbfcf665fa9291a9438dc4f219c6f7c82fc4d5217e00723d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d4924ad1fb81fc10724334b175560ff8bf721c23b9b7a7b04bf4614bf3dbce7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e74ea36dfefaf9fd6d30ac25ffb94415d9f426f6b3931cd03557561e37a7b16(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f256899db22a4f58e8df4e4600186d5b27b298a223541069fba787d46b6381(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434d46943965a634ab34624c81d4088252387a94f58d4d52e65e5c93378597d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397fd0f36e124c17e0bd2ec46b8cc1755711d52f5514f78f652091870e24a8bf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d022c28c50e39588f26b03210ea79192dd201d40bc4d1811067c76319967345e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bbafebd23aee3534a9f6067fcc73fcf55044ce083adfb69df8b3fe92a8a42c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b3260c4e61c869465bedbf9463094d00e5a6de62bc67b92dd87414991ec0c5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405f529a702f55a45516735b1d0de61e1eee5f3a1ebee663050757c1eed88c52(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e927eebf5ed374cfe9cbae7fa391ad7bab3c8c7402462efb9eafd7c60ea6f9(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsOutboundHeaderSourcePortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c611c81a81bc8edf6a30f33f4f1ee60fd4be546663d88b57e60c67bfc371a018(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c10e5e29d145e6abe75acb7e82e7719906badbfbeec4ed7ecbb7ee600e989178(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponents],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0419df00c7c7911c905d1f4fd027a80b2c8497381dc2b3240f6dbe1d77f8d549(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac908d16996f2029b93b31de7cfcd672eed4ac5c67bd02afa11ef9ae35347a16(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9e901130ca7e02151823e58a71601ef98f09bdd412c0527605b1d37406baa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebea91f6708ad70477986a4f9cf4d4cb9491df84c7457bc0d927b04d027dcf0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671125df71b2849bfd36c27d4d399f18f0cba1cd58dba0eb082e648de868c3b4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8e14848949f7790865ba624cbdeee245f80d58259436c7e9f82dffecd3e2d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a004fead97aa21a4f513b7bc9d41b9658bde3d37908bdd53d877127acb17d05e(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsRouteTableRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a81782ee3d6701ae2df3b1b1254d45811976e87d3ff1c0e3b3a19cf76987b3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06379bba5da9bf89d94324dc91e3cafb7301d9bc2782fc4a4e853d4e0eb8f2e2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f655a7eccc702ad11c3fa6738e25e6e1204b01f3f1eece7ecad3eb7c3a1b6cfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23becac4bf627143cd6832f02229a78fb51de888d5fd2670712892c4f03419e3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe09285afe4da481b69fa079318c51fda0c384ef47bb1295aba52bc280e4cdbe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0740da5bffa58180ed170f5ca2fd740845fe2a9c7a42cde6f07733003c8e940d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5884c1af9da7d451c316ac4e69f54b45abd93f02817c253c145ce81af3ac2d(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb87fcaf2fd24e46a8f426314c90d687053d7ef715449f11acebcfd4d6785a6c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81e847b3fabdc4bc39fe67ffe891d0f3d9a68e8ef7ca95d704fc5d2de5b534c3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06962a6cc8bc50a538164c43d217ed1a46dd19862a66c7f8ec7be5dd2a6cd181(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1393a5653903979e67a46050cbcf0c6aa866bf6d28101f1fc5e7c03abf1f0cd0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7210fedaf52a763cf6bfb76ce431d1f92d66dc252a26faf5e76d108839d3991d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5475c9b0492302efb311881269ec3a45effb760b4a7f4d1b115ff7a98b6e75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607e454a84a98225b8546d650582eed840d340c2e265440f56c1ee6fd378dc93(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSecurityGroupRulePortRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b1b3582d65b120566d282af0c61bc467c0fa6b589f4f8c1463dfff92e0eff20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d028a08cab246a13af60dd02971c1c518ec70d5034db2310d280c57635e07df(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c9ef843f91df4ee280617e1b328f991a0b971ab750604bd905a293b2100958(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9dcd2d94457ad8b52fda514d7c3268e4e4eca0e41fa35e38186249a3864abb7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a89d97716470896ad9734a94d02c4df972868d094da6a64ca7f62ebfe6ac24(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__892500af324598c03616a1a70b39966944920a2eff1ad6341b6416b45b46c77c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ca86e2072d3daa249094a2b0475a3a68ddcdddee08cf2c96e59469db9e59fa(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSourceVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f55a16fe476f68b2b6f1e5d3583fe8b310964e09da0979f6ec2025c49b5280(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a0c3c82ab19ab9728fb13a542a634213f4c3078d2d05d521151a8cd6d27d20(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f7bbc646c1fceb29fa1d0100bb9e07c1ba389ae1c5be749044a9f5b7ea7dc7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93efe4817aaee7a6e8d49b8670378dedf79f086a44807032439923fdb5d5996(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fb8c7389b75abb618b78b55ce65aa0552ed172b2765b9d2bba199cd16e6ec4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b17dab0058f5d01b359c1209afb579560a3f4dbd618c43d301679db55b4b05(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4edaf65645066706ce81c40778380ca428369ea08d8f9443010f8d274476f41(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsSubnet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d6b3fb0c8ea1e3a6230fd4436df198bb6f63417b61e636464e2bdfe01626b1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8126b68320e04aeb7b1d36474b78f4a5a447192f51b2a8dd0ff6dd28c8a9694b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094bb46d39c51b73d51c91ae9ede4ab88d67667ea8892b31664e24deebc63f01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__875506589d0deb262c7d18fd7eaca7a482ac9e2d2946feb3ac3e1a3e62f71dc1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e38d90bc2be46a89e746948fc4fc65edbf2ddcc99f747f81cebd2d96b5330c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__064c3e7c1dd80dbaf6d5764145e8b97e383526fdcbb7b2179da232e815db777b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ec56e3971f5b82b9e85748b1574344634ba6b2f2920440966c8613f6ec764f(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ad6d849c375d3e145c7f8d2a6721dc88bc50f768e35fbdf62b6cf8f6b8b3d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ca2fc0f7db76043480b4c2230654106cec1ebab5864eb20f00ba1f42c778ce0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddbf48723714de42c8a80866d7c6625a5c2857d7df5919b632f6f14a4fd2fb52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182d335112620921e6ddc2d06f2d93ae6c16f5ab9a25ee2fd80b243d720071be(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2bee91a3bc4924655272869fc1e7be1ad946e605203703a82be5ec6d63d59da(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfe9ae331adfd309fd67be795c2f9c055cead54e557e89ba70c2583fb0a47ba5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271c1052ca42fdc87512a761713331c4b7229678174275334071945490bcd05a(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsTransitGatewayRouteTableRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c920ed90cee3d5f769428b86d359a0f25baf9ff752370cdb446ee0eff5d5b1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a066cd081a10763fba592f92576f9dd8beeacb27b5b84f3912b5bbce6b56e85(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e837dc88052bd081ecbb2abc635bc8d610b846c34a47e922dae9ab523fcb6b1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4447d497c71b423d555cd93eac87e93680498cdc1047507a83c7b189877f0fda(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a58f710975006f3698c97afaef9e309f662c8b8fb1da97c04e943896048d62(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c858232f80bd85980c1b945efb2af2faf65a3d40891ad5df85f9aadab4255a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ca3c1439375d73a62395400fa8c58f272381f224a6e1dd2950ddc022aebe56(
    value: typing.Optional[Ec2NetworkInsightsAnalysisForwardPathComponentsVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b79903ffb412640f3b2f4879231d89e4a82af0b345f1b3be47789ba8fb1a16(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7babbe6cf0c610076fbc06a9d30607ddfad7f1739f957ab955b3211eeac045a3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b6cccf72ba39927009d4682b4d164aa08dd91482d4b0872f7b809f943516070(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ccee1ae7f51014f2adb193e2629489370b12b89d6d1cf08844ff9d95181ee64(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efbf4f44b5d801c77c3785dc931f0efa82162bda90eb31fef9cc367ea9b37b1e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5507374cab857796fb56223b5553b57721bd056ba02f66c6f5644b557763da4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1900bdd0f749b41595f199e798c7f34e00385949efe764aebbe7408044f9ccd6(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2f2eddceb48dffd37d5a8ebf3105f0630b5197023cd087cc79ecefcc28ba1c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59dad7b045940a8478c45e0948255bcfaec871ad0a4d02ae2f14767fbff133e5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b9149b03746b99f72df2c66dedcc09906e6a16f15cdb0c62417a0cba73c186(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__066fea93051007c9d029328ec536c8805c776ad4c460e590462d2af107f1ce20(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f6c088bc0b31a1cda3aa6e710aa412e6e8e58d981d0f3dfd191e70890cf2e3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5dde6cb702447da72e78186db630a849cf686521c2b3f49d0143ed48ec21f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ce2dbfb35bca31947da0016f9d3ce2dcbb03baf6aff513f0d748b2b1f60f45(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAclRulePortRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d088d2d3a15b4e6e45365f5e19a54df8aba6996aa6cb5933df78cef73dc6237e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ecfcb496a955a33b8b23c5606fcd88d17eba079c75b5e1dcd242215a97a128(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64a63b3aa725d2503fa05fabfc72f83b2ed7cafd24a66881535eeff1f7a79f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfec89d586605a204e6bf894fdb630bce94999c148e4b5f48cb7a70ec5cec58a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedc61f535dd23cf2cb5a9a17412138709f655a2f7bb609a1fac55f667ed622e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c68fc842c304e70a8068b00f0453df605753a107f99da92626273ec6a4bb4719(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a20848b0032624b154673247e6b0931c1c7e506d49bac2f73b6ad184ce9d72(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetailsComponent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3773524d5f80eacaf0b96e2f2c46d1b964b61619f71ff7b1f9a23bc4f10a7230(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c96d030803ea830d7cdb5efd061c33ecfe2eb4b7f9211066c59c7f3f220acf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9027b1f18233695448389db94c9cd3745efc6bf7c59c510ae86ae41b967af17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c98a0be3d6152deac8126d7580385ac96c83c0b0a861fe8eb889ff2454f5a5b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__680051eb37713248fa4dd68acf9d43f8419bea969166dbfc08621006fe34b50c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2fbef2f2da8a9ad29355bf0208c33dada779fd2e257b61e2ec0bcc572ae652(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d39af8e0b70b481fe5534ee2d1abe77d0741acdcfd5dd96936f223cc74b1662f(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAdditionalDetails],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ef6e319a244844a311194c1d9e526d29a2e257453c8088264720f30f32fa85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4f5ca59866f3b537f1a05392ebb50d819509a86a9805ba43b863f233059967a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cc69f128c1add8e8938bd5ca5b31484a71c35759325eba415b565696165b981(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e096eefb1dd554fa7e199fda23aba126212e6f6d56ff18427eb803c851edc502(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf560b62191abb6233f0e0c0e3df658bb876bebedf43696f6cfc8bb55d7d1ce0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf9cf272402a18edf3f2645f21b7512081b021c72e3f93d5bca122142f5e704d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cc12d11d8c65facc8d3399b908a2a4fdf7ff6384b025b364f031638fc462552(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsAttachedTo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936aadd331efe9620087206c3523034aff90609ccc31fe10ebb66fb6266a4a57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deda44150ccd9b909c06b88a81b19f54f00ed49e101e566d512dd29fb467956d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571f41b4b33b802844452b0cf4bf8351764236cf500a49f388d0ba4a686a28fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b216e35f2bdf8085f0fa3a47bd39b9b2bddc08fc3df64e0d214f7aafad849cf4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb03c12cf3bce02b65fabea8fe73db7187081871260bbda109ce5e080cf2426d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1921747ad501cca5d644d70cce27fc041fa8e0f6ff76c427b64a601e1d0b20c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c6f1bea5818b44edce7a1d8713c17e25979a89382df0f6a0406dc61bd0ff3fb(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsComponent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c787bda2910b7a612326f993e36a1c8c1c058c09e21bf6fe63fb4d3af3b80e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfbd4d7bfa378fbbfeba32b98f355528d77fc70e69bc0c9e20fc5c00796d390(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3618eb97f28ef7008f65358860de9c6cc52cc520ab7bce88e79ee7247da588(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64047869a80dda64f76a5c3ed17b2190b761f216f41eab49e31538bd78026c90(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ac955aa44f47551e8a3e5bb5131e6038b24e53373af229a11fea4be7453ecd7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caaa21155b31168bb417caa7fe4264234fef6b8fa6a7a6ee52bb86cc43e4889d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f3531dce65b675ac58f3867d31dc5bf38fb37a35dcc77f4c88d15c233a1adba(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsDestinationVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7885913b808fd2f3c6f2b3f63c1a503f54c2cf7d47a64ee09d5dea8dfb5c5448(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235aaacd5ff71afd86d354616eeae2f13f8d9cd0845d509307ea9f3657660557(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa128936c6769b5c0a4d9af366cea8c93082c520575d182c8f4ea9db667abe4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc91172b853a0f3ed0fd93dfca07fee4d57c64438ed36d30288dbb2ea78cea3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aeffb99c16c96cafa57791a71297ab05f7d193e0cb2393d0f027c03637a2ea3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bed68477e6a26f3b208cb49e6cf11d6b5b4a75c89cd1746aaa38fdd5d16a450(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf7d0e25515dbb738c0562d25ea541306821eea4fdfdd864372b01a6896044fd(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderDestinationPortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7338c0b75fa15b65de51bffbd6508d98261f1bb0f9cf242ee7618efc0636739(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35de65496a4092ec48b9ed7c5a1d44db06c1c88abb96aa57a4cc8e574b34e8b9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934c85f73d225e30068bd5666db82035383ee8350c532f6f668fe6f045c9fe77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32991c84a57a9e8a1f8cf36cfe7a28fdf7671110cd11cfd687fb456558e135a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152b2aa1f3c18076540493dbbb18c55204f86d2bb6d05a4998a8984cc2224bae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f3400f97edd37797c238b3b085b229f0b30e039fdd48b4eb49794bc6edbce3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c316d4ea0a3b0af75451b79a2edb0df58a118702304ad39eaec2822567903622(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd47fd6e52765f0b68e5e1914b1de122cf71f35dc8e2ad98615fc8f4e219869d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad555313feaf95dd5b12f5d164b1a99427ea5f0e2ed1fa1c945179095f9c5eb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9ceec6b1d7b4f5c25fe905f4e0e2fdfcb51e8495d84f040deb87f2d8a7c5f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7a445864e2fb59aebf03d6e35db8cedfae76fe79cd82c0e11edff0fd0285679(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__951f61addf5a668ede75bb8f4bcc48de91309430d67d81bea105cf54b549c2f9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f93aea8479d7b006fadb7be98aa2c75e73de826e1629b58877167721433eb72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6173173d22de599d968a36c827191b8edc686bf0775222440032538ffdcf6c7(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsInboundHeaderSourcePortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34f12ff6faef1db7fb784b4a85f152c2b7709316b59b625894fc40acb50fc72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0bd4cada7916b120f9d04c7c8927e905f0b829dce9d7e1dedeb61d175989c9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03dc184bf8a65d6cce21aa0d460a30424e1f54eb6816cb6994651e4fcaa2ad9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843befebf7c8224c366fd554faece47d4d0bb11d2b6cefd811cbddae52c51316(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715daf8e5f6488ef6b1653e72bee8d8b5c1d3816cf93e0ec53531d46b96f4877(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a90a1369a1c36b9b584ffa29580daffb63c9039c0906d3d5a4b440717d664c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f856f6f4b0e8c7eeb5dbb3715a47ab00ad7a945e95b765ad41049346780465(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab04ded0dda227f6accd52fbc349c1509cea2a3c5f0ad31d3c54ed9c5edb9a5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d859f10b7d35dbf7a908e83eb113f155383d2b3a55d100f0d6b481d73cf52e7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a01bb1d98a5ff70c05570663162f9cd8dad179e7f8eaa352ef9ac634ac1d2b4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec92bbb0e02dc438cb8be519c12ef665a471398d123e18f73dbd51a562e96e35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__024111aa2346940ad038b5bd276d1e0f0c9a7325b31607f9ec8b65b1e9acb75d(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderDestinationPortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f971ba2b5da275a5ee0eada730ab0e47ebac8801a0cd1a773682a8452a1d16b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0fbb058dfc547b7546311261b5fa9718801048d9366281efc426a3d75e4fcb2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ece56068735e37d71a1a7b707ca5ddb6dd27c76c43529a59a0808be831b720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb0de2cadefaf3472ff5f7e4a37cd56c9fb39b3ffb342934c27fdcc6ef6b7352(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d599724ce155f1fe0aa156defa7d98220d417b97d967faaa506106956bca74d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed832a8364603f5ddc34993a49262833f27f71c2fdd3335275a31c83b8274e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da1e17c8770aa54fd94620eb39d6ac9e4eb5c6bff77e6649cc18119beb148ac(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a407c89223e6ee357ba94889f638c7b380f5762e7ee6d93e2c6d297013bb38(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7266bafd00003c528c64c71f81e8de36cca83665d6cfb23ede34ef28445ad4c4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ddebc5f3c938e1ba216b8f7217d182223067426ad09f0a029d7bf4b5ee9901d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0c0c36cd8b046291ffc3c5f85f67c95c055c1c54be0620143b0ecfe8847a26(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a86d6742744dea70fe4004e7cdbe312986fbf9149bb962e49da770aaf9f548(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7527bb9847a8ebf3e9c20722ab9b8647c2227cd00ab6d05fa2edde09005459(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1418396315c34ef4a0fad9d2263ddc8cb14872ff18d0eb4b820793ebf5f118(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsOutboundHeaderSourcePortRanges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c8e84a7e052b5bd987cb98d3f6797a8ad5c3038b8467c3c30a3450babfcef60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e85c71e6ae7eb6c1594f89872f13c135826647e94b894f84cc42bb7c6040a1(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponents],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff1e4c20c743c37e633bd90863cf39025b7717377d42bef74e0d4864752cf07b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3348fb55492dc94484c817c69ffa820e3dfdee737b253ab4c26ea006e76714ce(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af364533894140107549222bba3af3b47027660b3a8482f047647572a1f1a9a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db72a7b9e6cdd5ecbf9eb269843ecf2fec6daaecd4aa9da3801ff45b38a0d0a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a500f292d9a82ba2cc873977fe7d3316505c27c3847bbe18188a55e229f27f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be3e0af97bdbb48e433ff3ee6a09f73bec1e01c75c172c24a76b7dd899018de5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca18d14ea1b37c1646e7b54b8c78b7c5d850d569c9ba5d221747df09cc70431(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsRouteTableRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669c4c75c167d2f06cfb66afff51989a5c0f39893df462df093727ef01c300f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70a7d3c969132124d798eebe299230af1af18803beb799ac3e5e6b5b37d6252(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b525f5430c770fa4f53021e3a95113769b17b72100e258d12aaed0d17a9de5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c59d226088d34728b0c11d43b667d4f9aa7fa07760bc06d36769715e95ec1ac(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4155567af479bb25984f2850c4f0349285b3f99ba3736b1e0e7ebbf0bfea39dd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211a7caa4aa1a2ab8e1ced2dcbd8795f32580053451710dc47f4556216c4e418(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb352b1be14f6bc517113b31cb1b66cf65e23bce947a060944f245b8c2ce7de7(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c0c92178e86d332b98250813cdca2f66f7bfe4613a39a3a308bdb0989f40d6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37906ec4c65392e27abe141248001dca7b157fd43a2ca9a9007e98115f5bf1d9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c9000b47b63f49fd0d0e4bcbe8ad096aa4d7aa232e0b518bdd3ccd3b264fca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8486274aa012ed0b94c7a798414b5602d76c97dd0e25808d3be51a53c6495be7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff9a0fa3f433da7344555112cdd9a8f46f13a946d06805191a844632e49cf46(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d93cc33474a33ddd242c5456dfa3157493dcb6f0ee90856c125815be7678549(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e45fe142fc9d5b7a49f94949bb16fb0d51c16df80ff4ae7de38b5b9506a08ea(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSecurityGroupRulePortRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffc814a854c87d9991d39831d445e2c40a5107f53b0872a7ea7424d42f90d2f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae876d198eafd03cdfa82ed9a2364712674c0f4cacf5726ef84a32b66a559e24(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eab37869a86439d2ead2ce8f2a27e3f90cf39ab1430b88c54eef252255628935(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb6fc833eb5d30c06c23e516e1c7b3f8d2f335560623d0731b1631b52c1152e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a0c2120558c4a8b8727338ef5917a66e0ffd662dbf6eecaeb175d08c4438b8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c34b794815947ed12f1e06e7cc704286efb153cf12a1c2ad0343037a16bd3505(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9628f34ae88e98cc8cd05383198235dab0dee13755831c1c5c0b9535f0cdfbe(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSourceVpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b38807689935914218b5766a9dd0f80a248c816b6ce587d438b346ee93a605(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4aacf2b88af744f07b215f53490f910639a76eea3b833fad1aa47335c13c80b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9206afe7b9d6f3d2ef1b3e9fadac0f58fd7bde93c58a93b98d58d988ac1d9c25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499691ba4eacbad9a297262bfe4151d1c681d5211111cbe70b05e800791f6bd1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6a643006502a381a6a1b8812a4f8a2794db7b8c5dbb89b5076efcaf538fd3e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6297c43686afb0e172138b0cac943152ed44bb1bfdec14bd88d23df2bcb444d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bafb3f2b59de161d6b8e8a3c948f08b3ae6f0b6727d8f06de757b96d9dcc973b(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsSubnet],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ddd7f3b3b5e59fdc31452ccc94d96e34a67bd2417a01a88900377e9cdbfcef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876352ae1974b771b94d733ace4d3a44340e2a6fa900b42a0d83ae78aaa8f3b1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c3d6715a9f11c98a88725467821031c2082ae44617485451ae4edb591f597d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4bc1fd60f4a002115a75749a515d8ff9206e28487fd1576d79c1e26a3ba6ebb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e7d7ad8aba2733f09e645646bf50ea56d8da165d34b8e3ed8977168b3ed6d4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1d11bc46056e391236d346e67d58fa6b2da9d8f6e09d01e610304b9ef0a4b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681538e8a369f5b0789cbcecd29e04051c9b1d2d44e2077af0201caef48f6b9f(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGateway],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dbb9364d84de0d2a83a865c66c443f2601dccb42aebdfda3dcc0724f7b835ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f54b7029b08e5dc14ebb2e76b0dcb93ad1333f4cbaa8bb712a38417c91596d2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01647d1887de46837ca00dc21b707ca7e0d7fab3a87ae18317c60e23c2004c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed8fd30ed84d15857a50804803a182e592c3052a2b350c1b087eaff543bde50(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__206f582b07792e0a684be8dfb33929607a4b78ee5bdd89cdb1bf877737423ebe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c25736989aa5f3666c59c5657548d35973ab58035c8ad7010b28e19506c2c93(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4123de035ed385d3a77e57ec36ef424a834f617b26d401ba43b25439945d60(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsTransitGatewayRouteTableRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4b9c6a1f8ed919eba6fa96fbbd1cea9bd5074e748f0f855abe63de75817beb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0755dca0dfb7581daa9a96407cc17949d72e83a84b29167dec5b38262e244d71(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16efcefa51060e868405d54bac16f267cf5cf13f6509170084214e678026caeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42dfbfb3445f1f09083cb50bb98eaa33649ecbeb91b8adbccb09bbe6faa7c432(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d97aa16da179187de9762c8d43cba08ffb7a865dd27cff2a14a1fb89af634a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a515bbdec62020aadbbd0b5cd967f0ba3d8c3b8e7a24a016f04608b8ea7704d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a53ec4ef52c6a49b7198cc97a10f1b6646dc9fb422a18d25ba857ad4df9852(
    value: typing.Optional[Ec2NetworkInsightsAnalysisReturnPathComponentsVpc],
) -> None:
    """Type checking stubs"""
    pass
