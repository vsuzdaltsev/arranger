'''
# `aws_autoscalingplans_scaling_plan`

Refer to the Terraform Registory for docs: [`aws_autoscalingplans_scaling_plan`](https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan).
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


class AutoscalingplansScalingPlan(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlan",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan aws_autoscalingplans_scaling_plan}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        application_source: typing.Union["AutoscalingplansScalingPlanApplicationSource", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        scaling_instruction: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanScalingInstruction", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan aws_autoscalingplans_scaling_plan} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param application_source: application_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#application_source AutoscalingplansScalingPlan#application_source}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#name AutoscalingplansScalingPlan#name}.
        :param scaling_instruction: scaling_instruction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scaling_instruction AutoscalingplansScalingPlan#scaling_instruction}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#id AutoscalingplansScalingPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f10dc03a1f67fc4e136bd5faedc45161ec9ad72da74f3efa5cacfb2ee2e69b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingplansScalingPlanConfig(
            application_source=application_source,
            name=name,
            scaling_instruction=scaling_instruction,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApplicationSource")
    def put_application_source(
        self,
        *,
        cloudformation_stack_arn: typing.Optional[builtins.str] = None,
        tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanApplicationSourceTagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cloudformation_stack_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#cloudformation_stack_arn AutoscalingplansScalingPlan#cloudformation_stack_arn}.
        :param tag_filter: tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#tag_filter AutoscalingplansScalingPlan#tag_filter}
        '''
        value = AutoscalingplansScalingPlanApplicationSource(
            cloudformation_stack_arn=cloudformation_stack_arn, tag_filter=tag_filter
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationSource", [value]))

    @jsii.member(jsii_name="putScalingInstruction")
    def put_scaling_instruction(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanScalingInstruction", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09f17307811092974227461d9afe889b366eb3f6a6e3395e85c0347c449c3ac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScalingInstruction", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="applicationSource")
    def application_source(
        self,
    ) -> "AutoscalingplansScalingPlanApplicationSourceOutputReference":
        return typing.cast("AutoscalingplansScalingPlanApplicationSourceOutputReference", jsii.get(self, "applicationSource"))

    @builtins.property
    @jsii.member(jsii_name="scalingInstruction")
    def scaling_instruction(
        self,
    ) -> "AutoscalingplansScalingPlanScalingInstructionList":
        return typing.cast("AutoscalingplansScalingPlanScalingInstructionList", jsii.get(self, "scalingInstruction"))

    @builtins.property
    @jsii.member(jsii_name="scalingPlanVersion")
    def scaling_plan_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingPlanVersion"))

    @builtins.property
    @jsii.member(jsii_name="applicationSourceInput")
    def application_source_input(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanApplicationSource"]:
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanApplicationSource"], jsii.get(self, "applicationSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingInstructionInput")
    def scaling_instruction_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstruction"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstruction"]]], jsii.get(self, "scalingInstructionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72f9a5a3762b89895534935b0f28e497aa1fd12a1e413f62005807ddd7aa7c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358fbf3483f3f4ce83d7de16fa170e1ef305392c6293f7f9ae72439fa247b2b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanApplicationSource",
    jsii_struct_bases=[],
    name_mapping={
        "cloudformation_stack_arn": "cloudformationStackArn",
        "tag_filter": "tagFilter",
    },
)
class AutoscalingplansScalingPlanApplicationSource:
    def __init__(
        self,
        *,
        cloudformation_stack_arn: typing.Optional[builtins.str] = None,
        tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanApplicationSourceTagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cloudformation_stack_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#cloudformation_stack_arn AutoscalingplansScalingPlan#cloudformation_stack_arn}.
        :param tag_filter: tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#tag_filter AutoscalingplansScalingPlan#tag_filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb834a6a14d839465da6d725c9ccf8c2f15a7001e65641c17379c5038351bea1)
            check_type(argname="argument cloudformation_stack_arn", value=cloudformation_stack_arn, expected_type=type_hints["cloudformation_stack_arn"])
            check_type(argname="argument tag_filter", value=tag_filter, expected_type=type_hints["tag_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudformation_stack_arn is not None:
            self._values["cloudformation_stack_arn"] = cloudformation_stack_arn
        if tag_filter is not None:
            self._values["tag_filter"] = tag_filter

    @builtins.property
    def cloudformation_stack_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#cloudformation_stack_arn AutoscalingplansScalingPlan#cloudformation_stack_arn}.'''
        result = self._values.get("cloudformation_stack_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanApplicationSourceTagFilter"]]]:
        '''tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#tag_filter AutoscalingplansScalingPlan#tag_filter}
        '''
        result = self._values.get("tag_filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanApplicationSourceTagFilter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanApplicationSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingplansScalingPlanApplicationSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanApplicationSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3c1bad5b2816708db28518700dcec48d57ebfc9893d790efdb4c9cc4d779182)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTagFilter")
    def put_tag_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanApplicationSourceTagFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a57d672eeb8968b234d1942ef3738e6602ce2c46b3ea60975923701b84ab3080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagFilter", [value]))

    @jsii.member(jsii_name="resetCloudformationStackArn")
    def reset_cloudformation_stack_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudformationStackArn", []))

    @jsii.member(jsii_name="resetTagFilter")
    def reset_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagFilter", []))

    @builtins.property
    @jsii.member(jsii_name="tagFilter")
    def tag_filter(self) -> "AutoscalingplansScalingPlanApplicationSourceTagFilterList":
        return typing.cast("AutoscalingplansScalingPlanApplicationSourceTagFilterList", jsii.get(self, "tagFilter"))

    @builtins.property
    @jsii.member(jsii_name="cloudformationStackArnInput")
    def cloudformation_stack_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudformationStackArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tagFilterInput")
    def tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanApplicationSourceTagFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanApplicationSourceTagFilter"]]], jsii.get(self, "tagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudformationStackArn")
    def cloudformation_stack_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudformationStackArn"))

    @cloudformation_stack_arn.setter
    def cloudformation_stack_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea626d12ced9799be5a590d75543c0d07e88ab4f75e7b650fd3a9f3f59bc7bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudformationStackArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanApplicationSource]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanApplicationSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingplansScalingPlanApplicationSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8194e35ef2a739e20189523ea3be4c87cebc75f8b887a945caaa39126506f158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanApplicationSourceTagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class AutoscalingplansScalingPlanApplicationSourceTagFilter:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#key AutoscalingplansScalingPlan#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#values AutoscalingplansScalingPlan#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a15fec4220b3ebf9187dd18d76c8bfe67135a892a68e7417d3f4fde53e89a8)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#key AutoscalingplansScalingPlan#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#values AutoscalingplansScalingPlan#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanApplicationSourceTagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingplansScalingPlanApplicationSourceTagFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanApplicationSourceTagFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9de03fd3cb141d21c2157c5a157ad3bcd36817cd4a9234019a7fad76ae42138)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingplansScalingPlanApplicationSourceTagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30640161a5cf14c1b3f8eefe0c54b253630361bdd71ce2cd582953e76accbcd1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingplansScalingPlanApplicationSourceTagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52552cddbf8b31fd8d4a2d86c1e7e2dfaf2732361b2a07b6f0e3f96b639d1bfb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__049ab1bac59e0614183b8320989a72f6353a84df1432b30e1feec7acf4790a48)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea40d91f280583ed47b8752fe84b82d0cf43a9714f8f3b4fb42c5bf326237d5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanApplicationSourceTagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanApplicationSourceTagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanApplicationSourceTagFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1520cfe66e5eca84322fbbe6f03708f999640b23689471d1380bed606aa95a02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingplansScalingPlanApplicationSourceTagFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanApplicationSourceTagFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8b9ba71f5048fd6d29839cf632b9a6d072f9c72780cb4e52cc00ce988250c70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__65b65e8de0bc2babf6244f1d5056da041b3ae9b23f5369051b295d3149eb2bd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e494a12d196438470b396dd676c5c609c94ae23373f167f13b079321e2cd06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingplansScalingPlanApplicationSourceTagFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingplansScalingPlanApplicationSourceTagFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingplansScalingPlanApplicationSourceTagFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__241a4587c808d1cb37321253a7fa1d0dad876ea37f74afdc7bfd2360dfa6c31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "application_source": "applicationSource",
        "name": "name",
        "scaling_instruction": "scalingInstruction",
        "id": "id",
    },
)
class AutoscalingplansScalingPlanConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        application_source: typing.Union[AutoscalingplansScalingPlanApplicationSource, typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        scaling_instruction: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanScalingInstruction", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param application_source: application_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#application_source AutoscalingplansScalingPlan#application_source}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#name AutoscalingplansScalingPlan#name}.
        :param scaling_instruction: scaling_instruction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scaling_instruction AutoscalingplansScalingPlan#scaling_instruction}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#id AutoscalingplansScalingPlan#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(application_source, dict):
            application_source = AutoscalingplansScalingPlanApplicationSource(**application_source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a383b3d1e5d5e7312b349b62ef7d9504b03e1f11955125f377b92e8f77557059)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument application_source", value=application_source, expected_type=type_hints["application_source"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scaling_instruction", value=scaling_instruction, expected_type=type_hints["scaling_instruction"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_source": application_source,
            "name": name,
            "scaling_instruction": scaling_instruction,
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
    def application_source(self) -> AutoscalingplansScalingPlanApplicationSource:
        '''application_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#application_source AutoscalingplansScalingPlan#application_source}
        '''
        result = self._values.get("application_source")
        assert result is not None, "Required property 'application_source' is missing"
        return typing.cast(AutoscalingplansScalingPlanApplicationSource, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#name AutoscalingplansScalingPlan#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scaling_instruction(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstruction"]]:
        '''scaling_instruction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scaling_instruction AutoscalingplansScalingPlan#scaling_instruction}
        '''
        result = self._values.get("scaling_instruction")
        assert result is not None, "Required property 'scaling_instruction' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstruction"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#id AutoscalingplansScalingPlan#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstruction",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "target_tracking_configuration": "targetTrackingConfiguration",
        "customized_load_metric_specification": "customizedLoadMetricSpecification",
        "disable_dynamic_scaling": "disableDynamicScaling",
        "predefined_load_metric_specification": "predefinedLoadMetricSpecification",
        "predictive_scaling_max_capacity_behavior": "predictiveScalingMaxCapacityBehavior",
        "predictive_scaling_max_capacity_buffer": "predictiveScalingMaxCapacityBuffer",
        "predictive_scaling_mode": "predictiveScalingMode",
        "scaling_policy_update_behavior": "scalingPolicyUpdateBehavior",
        "scheduled_action_buffer_time": "scheduledActionBufferTime",
    },
)
class AutoscalingplansScalingPlanScalingInstruction:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        target_tracking_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        customized_load_metric_specification: typing.Optional[typing.Union["AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_dynamic_scaling: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        predefined_load_metric_specification: typing.Optional[typing.Union["AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        predictive_scaling_max_capacity_behavior: typing.Optional[builtins.str] = None,
        predictive_scaling_max_capacity_buffer: typing.Optional[jsii.Number] = None,
        predictive_scaling_mode: typing.Optional[builtins.str] = None,
        scaling_policy_update_behavior: typing.Optional[builtins.str] = None,
        scheduled_action_buffer_time: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#max_capacity AutoscalingplansScalingPlan#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#min_capacity AutoscalingplansScalingPlan#min_capacity}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_id AutoscalingplansScalingPlan#resource_id}.
        :param scalable_dimension: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scalable_dimension AutoscalingplansScalingPlan#scalable_dimension}.
        :param service_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#service_namespace AutoscalingplansScalingPlan#service_namespace}.
        :param target_tracking_configuration: target_tracking_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#target_tracking_configuration AutoscalingplansScalingPlan#target_tracking_configuration}
        :param customized_load_metric_specification: customized_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#customized_load_metric_specification AutoscalingplansScalingPlan#customized_load_metric_specification}
        :param disable_dynamic_scaling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#disable_dynamic_scaling AutoscalingplansScalingPlan#disable_dynamic_scaling}.
        :param predefined_load_metric_specification: predefined_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_load_metric_specification AutoscalingplansScalingPlan#predefined_load_metric_specification}
        :param predictive_scaling_max_capacity_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predictive_scaling_max_capacity_behavior AutoscalingplansScalingPlan#predictive_scaling_max_capacity_behavior}.
        :param predictive_scaling_max_capacity_buffer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predictive_scaling_max_capacity_buffer AutoscalingplansScalingPlan#predictive_scaling_max_capacity_buffer}.
        :param predictive_scaling_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predictive_scaling_mode AutoscalingplansScalingPlan#predictive_scaling_mode}.
        :param scaling_policy_update_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scaling_policy_update_behavior AutoscalingplansScalingPlan#scaling_policy_update_behavior}.
        :param scheduled_action_buffer_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scheduled_action_buffer_time AutoscalingplansScalingPlan#scheduled_action_buffer_time}.
        '''
        if isinstance(customized_load_metric_specification, dict):
            customized_load_metric_specification = AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification(**customized_load_metric_specification)
        if isinstance(predefined_load_metric_specification, dict):
            predefined_load_metric_specification = AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification(**predefined_load_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d619eb73ef21d1402bf4f7dee8530d05d597198010ed2678dab3be85f9bcfa)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument target_tracking_configuration", value=target_tracking_configuration, expected_type=type_hints["target_tracking_configuration"])
            check_type(argname="argument customized_load_metric_specification", value=customized_load_metric_specification, expected_type=type_hints["customized_load_metric_specification"])
            check_type(argname="argument disable_dynamic_scaling", value=disable_dynamic_scaling, expected_type=type_hints["disable_dynamic_scaling"])
            check_type(argname="argument predefined_load_metric_specification", value=predefined_load_metric_specification, expected_type=type_hints["predefined_load_metric_specification"])
            check_type(argname="argument predictive_scaling_max_capacity_behavior", value=predictive_scaling_max_capacity_behavior, expected_type=type_hints["predictive_scaling_max_capacity_behavior"])
            check_type(argname="argument predictive_scaling_max_capacity_buffer", value=predictive_scaling_max_capacity_buffer, expected_type=type_hints["predictive_scaling_max_capacity_buffer"])
            check_type(argname="argument predictive_scaling_mode", value=predictive_scaling_mode, expected_type=type_hints["predictive_scaling_mode"])
            check_type(argname="argument scaling_policy_update_behavior", value=scaling_policy_update_behavior, expected_type=type_hints["scaling_policy_update_behavior"])
            check_type(argname="argument scheduled_action_buffer_time", value=scheduled_action_buffer_time, expected_type=type_hints["scheduled_action_buffer_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
            "target_tracking_configuration": target_tracking_configuration,
        }
        if customized_load_metric_specification is not None:
            self._values["customized_load_metric_specification"] = customized_load_metric_specification
        if disable_dynamic_scaling is not None:
            self._values["disable_dynamic_scaling"] = disable_dynamic_scaling
        if predefined_load_metric_specification is not None:
            self._values["predefined_load_metric_specification"] = predefined_load_metric_specification
        if predictive_scaling_max_capacity_behavior is not None:
            self._values["predictive_scaling_max_capacity_behavior"] = predictive_scaling_max_capacity_behavior
        if predictive_scaling_max_capacity_buffer is not None:
            self._values["predictive_scaling_max_capacity_buffer"] = predictive_scaling_max_capacity_buffer
        if predictive_scaling_mode is not None:
            self._values["predictive_scaling_mode"] = predictive_scaling_mode
        if scaling_policy_update_behavior is not None:
            self._values["scaling_policy_update_behavior"] = scaling_policy_update_behavior
        if scheduled_action_buffer_time is not None:
            self._values["scheduled_action_buffer_time"] = scheduled_action_buffer_time

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#max_capacity AutoscalingplansScalingPlan#max_capacity}.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#min_capacity AutoscalingplansScalingPlan#min_capacity}.'''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_id AutoscalingplansScalingPlan#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scalable_dimension AutoscalingplansScalingPlan#scalable_dimension}.'''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#service_namespace AutoscalingplansScalingPlan#service_namespace}.'''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_tracking_configuration(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration"]]:
        '''target_tracking_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#target_tracking_configuration AutoscalingplansScalingPlan#target_tracking_configuration}
        '''
        result = self._values.get("target_tracking_configuration")
        assert result is not None, "Required property 'target_tracking_configuration' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration"]], result)

    @builtins.property
    def customized_load_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification"]:
        '''customized_load_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#customized_load_metric_specification AutoscalingplansScalingPlan#customized_load_metric_specification}
        '''
        result = self._values.get("customized_load_metric_specification")
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification"], result)

    @builtins.property
    def disable_dynamic_scaling(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#disable_dynamic_scaling AutoscalingplansScalingPlan#disable_dynamic_scaling}.'''
        result = self._values.get("disable_dynamic_scaling")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def predefined_load_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification"]:
        '''predefined_load_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_load_metric_specification AutoscalingplansScalingPlan#predefined_load_metric_specification}
        '''
        result = self._values.get("predefined_load_metric_specification")
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification"], result)

    @builtins.property
    def predictive_scaling_max_capacity_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predictive_scaling_max_capacity_behavior AutoscalingplansScalingPlan#predictive_scaling_max_capacity_behavior}.'''
        result = self._values.get("predictive_scaling_max_capacity_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def predictive_scaling_max_capacity_buffer(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predictive_scaling_max_capacity_buffer AutoscalingplansScalingPlan#predictive_scaling_max_capacity_buffer}.'''
        result = self._values.get("predictive_scaling_max_capacity_buffer")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def predictive_scaling_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predictive_scaling_mode AutoscalingplansScalingPlan#predictive_scaling_mode}.'''
        result = self._values.get("predictive_scaling_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_policy_update_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scaling_policy_update_behavior AutoscalingplansScalingPlan#scaling_policy_update_behavior}.'''
        result = self._values.get("scaling_policy_update_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_action_buffer_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scheduled_action_buffer_time AutoscalingplansScalingPlan#scheduled_action_buffer_time}.'''
        result = self._values.get("scheduled_action_buffer_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanScalingInstruction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "statistic": "statistic",
        "dimensions": "dimensions",
        "unit": "unit",
    },
)
class AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#metric_name AutoscalingplansScalingPlan#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#namespace AutoscalingplansScalingPlan#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#statistic AutoscalingplansScalingPlan#statistic}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#dimensions AutoscalingplansScalingPlan#dimensions}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#unit AutoscalingplansScalingPlan#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c83b7d762bb9e8c4e8e7b40608cceddc691587b6f705b01fc76772270f733ca)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "statistic": statistic,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#metric_name AutoscalingplansScalingPlan#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#namespace AutoscalingplansScalingPlan#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#statistic AutoscalingplansScalingPlan#statistic}.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#dimensions AutoscalingplansScalingPlan#dimensions}.'''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#unit AutoscalingplansScalingPlan#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87d9f56de1c3ece837f8e70528a9a0c13419c7bb8463d725b45228bc3d2288d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b1f0566dfd002dc2590132a378cc48f93e236dffcb2d087d33c38eebbc05e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742f25310183161bbcd9048f64b6b06d9e8f4172cb74c59c1e98cd22c65b9bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068aaee26e1a77a51d269efb1aab2f68f592e7559ecef0682f298bd934bccba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1410150e9a2ccf2cd69f11a13e58d231fadc7c16e984d3510ad29f43599ad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c5442ed1b3a57aa4231869d0f4a35a20579b531eb795e8b3ce6dde8ea466964)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1799d21ca7363dbf9f80bcd3527200e9cdf54ca3ceea09501a10e240adb4b7b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingplansScalingPlanScalingInstructionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e1cd0fdb00cc6561ff8900804b230db3ebf991a79f098e913f4a4beba1d99bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingplansScalingPlanScalingInstructionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b062965d44863ed88643f1596b91f768f0937ada778b0b7ddb98d241ef855229)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingplansScalingPlanScalingInstructionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5828feed030a6d4154044b8da109e023bae88f1316b451ac02443a2a1f6848fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14e4eb0200c65538d47cae66f77fb864923ec24716b84816351ea1460666d938)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7cad00f76ba12d3b13882d7493ab7768d5ab5253f995b9cd6eb99bc43f58b9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstruction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstruction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstruction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4144c0997fb5bfe476e3369f76a0549285794f84082e96acef13a125d7eb5241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingplansScalingPlanScalingInstructionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__392e0fd72bdba740b164b5157fe7c5e980326bacd26327ad1b170ef7f664d24b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomizedLoadMetricSpecification")
    def put_customized_load_metric_specification(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#metric_name AutoscalingplansScalingPlan#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#namespace AutoscalingplansScalingPlan#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#statistic AutoscalingplansScalingPlan#statistic}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#dimensions AutoscalingplansScalingPlan#dimensions}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#unit AutoscalingplansScalingPlan#unit}.
        '''
        value = AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification(
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            dimensions=dimensions,
            unit=unit,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedLoadMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedLoadMetricSpecification")
    def put_predefined_load_metric_specification(
        self,
        *,
        predefined_load_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_load_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_load_metric_type AutoscalingplansScalingPlan#predefined_load_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_label AutoscalingplansScalingPlan#resource_label}.
        '''
        value = AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification(
            predefined_load_metric_type=predefined_load_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedLoadMetricSpecification", [value]))

    @jsii.member(jsii_name="putTargetTrackingConfiguration")
    def put_target_tracking_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7773ad72e2c19f7a56a36cb11609f675e0f49278ce3aaae92be5328b47c133e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetTrackingConfiguration", [value]))

    @jsii.member(jsii_name="resetCustomizedLoadMetricSpecification")
    def reset_customized_load_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedLoadMetricSpecification", []))

    @jsii.member(jsii_name="resetDisableDynamicScaling")
    def reset_disable_dynamic_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableDynamicScaling", []))

    @jsii.member(jsii_name="resetPredefinedLoadMetricSpecification")
    def reset_predefined_load_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedLoadMetricSpecification", []))

    @jsii.member(jsii_name="resetPredictiveScalingMaxCapacityBehavior")
    def reset_predictive_scaling_max_capacity_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredictiveScalingMaxCapacityBehavior", []))

    @jsii.member(jsii_name="resetPredictiveScalingMaxCapacityBuffer")
    def reset_predictive_scaling_max_capacity_buffer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredictiveScalingMaxCapacityBuffer", []))

    @jsii.member(jsii_name="resetPredictiveScalingMode")
    def reset_predictive_scaling_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredictiveScalingMode", []))

    @jsii.member(jsii_name="resetScalingPolicyUpdateBehavior")
    def reset_scaling_policy_update_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingPolicyUpdateBehavior", []))

    @jsii.member(jsii_name="resetScheduledActionBufferTime")
    def reset_scheduled_action_buffer_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledActionBufferTime", []))

    @builtins.property
    @jsii.member(jsii_name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecificationOutputReference:
        return typing.cast(AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecificationOutputReference, jsii.get(self, "customizedLoadMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> "AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecificationOutputReference":
        return typing.cast("AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecificationOutputReference", jsii.get(self, "predefinedLoadMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingConfiguration")
    def target_tracking_configuration(
        self,
    ) -> "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationList":
        return typing.cast("AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationList", jsii.get(self, "targetTrackingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="customizedLoadMetricSpecificationInput")
    def customized_load_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification], jsii.get(self, "customizedLoadMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableDynamicScalingInput")
    def disable_dynamic_scaling_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableDynamicScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricSpecificationInput")
    def predefined_load_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification"], jsii.get(self, "predefinedLoadMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingMaxCapacityBehaviorInput")
    def predictive_scaling_max_capacity_behavior_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predictiveScalingMaxCapacityBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingMaxCapacityBufferInput")
    def predictive_scaling_max_capacity_buffer_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "predictiveScalingMaxCapacityBufferInput"))

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingModeInput")
    def predictive_scaling_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predictiveScalingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="scalableDimensionInput")
    def scalable_dimension_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalableDimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyUpdateBehaviorInput")
    def scaling_policy_update_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalingPolicyUpdateBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledActionBufferTimeInput")
    def scheduled_action_buffer_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduledActionBufferTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNamespaceInput")
    def service_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingConfigurationInput")
    def target_tracking_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration"]]], jsii.get(self, "targetTrackingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableDynamicScaling")
    def disable_dynamic_scaling(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableDynamicScaling"))

    @disable_dynamic_scaling.setter
    def disable_dynamic_scaling(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ce4363403f8a24c323c0989d6b8e8fdb73955c0020b494b141012f5916d5c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableDynamicScaling", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6c336fe21e6635ee57ceb90ed0dc61933a7ab00d4a72af4147e89a71281d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ab893310c6fc9aedbbc4d16fa5d17eef0829a06ec63cad691c6d5b7dbb2553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingMaxCapacityBehavior")
    def predictive_scaling_max_capacity_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predictiveScalingMaxCapacityBehavior"))

    @predictive_scaling_max_capacity_behavior.setter
    def predictive_scaling_max_capacity_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a239156fbdf9703bbca2a66ec81d61f50489fbfcf2c0fd887e6c65944622cb8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predictiveScalingMaxCapacityBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingMaxCapacityBuffer")
    def predictive_scaling_max_capacity_buffer(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "predictiveScalingMaxCapacityBuffer"))

    @predictive_scaling_max_capacity_buffer.setter
    def predictive_scaling_max_capacity_buffer(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a643eefbeee6e1a7feeb97f7dd4101d8032227cc85a51762024a6570c1baf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predictiveScalingMaxCapacityBuffer", value)

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingMode")
    def predictive_scaling_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predictiveScalingMode"))

    @predictive_scaling_mode.setter
    def predictive_scaling_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b60b017838d4e3e67ac0d49e255c58eb83ef8b2bf94486b6410233fc12c243d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predictiveScalingMode", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aaa5486442c3319eacbf1f7a420c5d20b777343de5a268d999c78bae1d5b9eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef5d46887084bf45a01de50db24088c5bf5f169b1cec4300905b7815170ef12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalableDimension", value)

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyUpdateBehavior")
    def scaling_policy_update_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scalingPolicyUpdateBehavior"))

    @scaling_policy_update_behavior.setter
    def scaling_policy_update_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442df57875773f9180720d27bfe7aaf72a1e392bd831707a8170469c1eb61bba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingPolicyUpdateBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledActionBufferTime")
    def scheduled_action_buffer_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scheduledActionBufferTime"))

    @scheduled_action_buffer_time.setter
    def scheduled_action_buffer_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45284612816b189613904c4858de0e458ddfc932d8a66f099298b75864bfd54d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActionBufferTime", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c9a1df5ca37b1358faaaaa3da6232f696b3bea6784ae09eff9c59e7ead6366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstruction, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstruction, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstruction, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e05958771a83aa32c8374793603b30aa036ef510941a7eeddcf3468c4d9b55e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_load_metric_type": "predefinedLoadMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification:
    def __init__(
        self,
        *,
        predefined_load_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_load_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_load_metric_type AutoscalingplansScalingPlan#predefined_load_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_label AutoscalingplansScalingPlan#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da8e1c0173f3135d42ecd01e4357502012df2636b191219d4f0a240c0001b1c)
            check_type(argname="argument predefined_load_metric_type", value=predefined_load_metric_type, expected_type=type_hints["predefined_load_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_load_metric_type": predefined_load_metric_type,
        }
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def predefined_load_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_load_metric_type AutoscalingplansScalingPlan#predefined_load_metric_type}.'''
        result = self._values.get("predefined_load_metric_type")
        assert result is not None, "Required property 'predefined_load_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_label AutoscalingplansScalingPlan#resource_label}.'''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a82e19ee4ce4d22aa3e0a339800ba40bb27cc8218fec4e1acf18d9256158532)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResourceLabel")
    def reset_resource_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabel", []))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricTypeInput")
    def predefined_load_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedLoadMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricType")
    def predefined_load_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedLoadMetricType"))

    @predefined_load_metric_type.setter
    def predefined_load_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f5681857cf5d328b8f38c906d9028b7b0ddb313922e4edb2c6261cf6ebb80c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedLoadMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4ba07d5c29f0591644ba0e84f997667f83e2c9226e6388df8411ac7785d8bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33c3b65e6d12a4b08e773bf076ac95fb7bce72c5b7960e7db97ecb3612805ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_scaling_metric_specification": "customizedScalingMetricSpecification",
        "disable_scale_in": "disableScaleIn",
        "estimated_instance_warmup": "estimatedInstanceWarmup",
        "predefined_scaling_metric_specification": "predefinedScalingMetricSpecification",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
    },
)
class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_scaling_metric_specification: typing.Optional[typing.Union["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        predefined_scaling_metric_specification: typing.Optional[typing.Union["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_in_cooldown: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#target_value AutoscalingplansScalingPlan#target_value}.
        :param customized_scaling_metric_specification: customized_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#customized_scaling_metric_specification AutoscalingplansScalingPlan#customized_scaling_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#disable_scale_in AutoscalingplansScalingPlan#disable_scale_in}.
        :param estimated_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#estimated_instance_warmup AutoscalingplansScalingPlan#estimated_instance_warmup}.
        :param predefined_scaling_metric_specification: predefined_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_scaling_metric_specification AutoscalingplansScalingPlan#predefined_scaling_metric_specification}
        :param scale_in_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scale_in_cooldown AutoscalingplansScalingPlan#scale_in_cooldown}.
        :param scale_out_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scale_out_cooldown AutoscalingplansScalingPlan#scale_out_cooldown}.
        '''
        if isinstance(customized_scaling_metric_specification, dict):
            customized_scaling_metric_specification = AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification(**customized_scaling_metric_specification)
        if isinstance(predefined_scaling_metric_specification, dict):
            predefined_scaling_metric_specification = AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification(**predefined_scaling_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c6ee08e5ead2791fdb599bcba4342d7bf4b5d1d37399e5994f9e0e9eb8e9903)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_scaling_metric_specification", value=customized_scaling_metric_specification, expected_type=type_hints["customized_scaling_metric_specification"])
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument estimated_instance_warmup", value=estimated_instance_warmup, expected_type=type_hints["estimated_instance_warmup"])
            check_type(argname="argument predefined_scaling_metric_specification", value=predefined_scaling_metric_specification, expected_type=type_hints["predefined_scaling_metric_specification"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_scaling_metric_specification is not None:
            self._values["customized_scaling_metric_specification"] = customized_scaling_metric_specification
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if estimated_instance_warmup is not None:
            self._values["estimated_instance_warmup"] = estimated_instance_warmup
        if predefined_scaling_metric_specification is not None:
            self._values["predefined_scaling_metric_specification"] = predefined_scaling_metric_specification
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#target_value AutoscalingplansScalingPlan#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_scaling_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification"]:
        '''customized_scaling_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#customized_scaling_metric_specification AutoscalingplansScalingPlan#customized_scaling_metric_specification}
        '''
        result = self._values.get("customized_scaling_metric_specification")
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification"], result)

    @builtins.property
    def disable_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#disable_scale_in AutoscalingplansScalingPlan#disable_scale_in}.'''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#estimated_instance_warmup AutoscalingplansScalingPlan#estimated_instance_warmup}.'''
        result = self._values.get("estimated_instance_warmup")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def predefined_scaling_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification"]:
        '''predefined_scaling_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_scaling_metric_specification AutoscalingplansScalingPlan#predefined_scaling_metric_specification}
        '''
        result = self._values.get("predefined_scaling_metric_specification")
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification"], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scale_in_cooldown AutoscalingplansScalingPlan#scale_in_cooldown}.'''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#scale_out_cooldown AutoscalingplansScalingPlan#scale_out_cooldown}.'''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "statistic": "statistic",
        "dimensions": "dimensions",
        "unit": "unit",
    },
)
class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#metric_name AutoscalingplansScalingPlan#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#namespace AutoscalingplansScalingPlan#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#statistic AutoscalingplansScalingPlan#statistic}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#dimensions AutoscalingplansScalingPlan#dimensions}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#unit AutoscalingplansScalingPlan#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e9458ce2487c8bdc94839e6a549b8bb47df298a9e2340a70382492ee478bdd7)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "statistic": statistic,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#metric_name AutoscalingplansScalingPlan#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#namespace AutoscalingplansScalingPlan#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#statistic AutoscalingplansScalingPlan#statistic}.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#dimensions AutoscalingplansScalingPlan#dimensions}.'''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#unit AutoscalingplansScalingPlan#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__75e690ddbe9d737200b0c783699adbec9a47d71c60e0d7e8417de85bafbc5015)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3ea6348402711f230ddcb2e642b5bfc3520281b63cb1e4fb1ca3dd63cdc5cae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d94f8aca4476bf38526c8e9e5f459a2db35798d497273e43e142e3adf2a7dc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0affeea55d78bfd607c76b9e4affcb85a679907ff62efc6040c1c6bc86c7a319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d91df8fc35db8d3b1ece8683a64ea460b0cf8f1dbc691e51a0497bfa3587e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78e7d4d0fdd56318dcae5472216d3e03da7bb95a86f7fee9b4254c7ce3058122)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d63b1ac29c6cccd9f7c888a1119faa6d03c94ea534036d7a85dcd56f965ccfd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86610d6a0afbd81a9baad57dde2a86b9a6819d3711a95abe77a9d59648dacbc8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__038c51796db0d1453f840640a69ce4482e3ec4d62c5921435ccd6cf378c40971)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74cb441e03ec7ab37b0347498b45e2c4e0e7d094a9936a7b2d382d2ee7134d30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ea0a7469acb6aa6aa48eafc52a636977b0e691c8bf0fbec719007d30eb2e662)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aaf319c9f4612b2011ae0b34590c2c792bcc3133594a0a027be6ad519ac98552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd2872b35b7e6f47076c87274cbadfb9f463d469a464af44cf1f58f417efa83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e3e23a245b36f0ac95cb393b0945fdcfcfbb3e537ca2c268fd2796df8178a5d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomizedScalingMetricSpecification")
    def put_customized_scaling_metric_specification(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#metric_name AutoscalingplansScalingPlan#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#namespace AutoscalingplansScalingPlan#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#statistic AutoscalingplansScalingPlan#statistic}.
        :param dimensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#dimensions AutoscalingplansScalingPlan#dimensions}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#unit AutoscalingplansScalingPlan#unit}.
        '''
        value = AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification(
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            dimensions=dimensions,
            unit=unit,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedScalingMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedScalingMetricSpecification")
    def put_predefined_scaling_metric_specification(
        self,
        *,
        predefined_scaling_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_scaling_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_scaling_metric_type AutoscalingplansScalingPlan#predefined_scaling_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_label AutoscalingplansScalingPlan#resource_label}.
        '''
        value = AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification(
            predefined_scaling_metric_type=predefined_scaling_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedScalingMetricSpecification", [value]))

    @jsii.member(jsii_name="resetCustomizedScalingMetricSpecification")
    def reset_customized_scaling_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedScalingMetricSpecification", []))

    @jsii.member(jsii_name="resetDisableScaleIn")
    def reset_disable_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableScaleIn", []))

    @jsii.member(jsii_name="resetEstimatedInstanceWarmup")
    def reset_estimated_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEstimatedInstanceWarmup", []))

    @jsii.member(jsii_name="resetPredefinedScalingMetricSpecification")
    def reset_predefined_scaling_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedScalingMetricSpecification", []))

    @jsii.member(jsii_name="resetScaleInCooldown")
    def reset_scale_in_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInCooldown", []))

    @jsii.member(jsii_name="resetScaleOutCooldown")
    def reset_scale_out_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleOutCooldown", []))

    @builtins.property
    @jsii.member(jsii_name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationOutputReference:
        return typing.cast(AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationOutputReference, jsii.get(self, "customizedScalingMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationOutputReference":
        return typing.cast("AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationOutputReference", jsii.get(self, "predefinedScalingMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedScalingMetricSpecificationInput")
    def customized_scaling_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification], jsii.get(self, "customizedScalingMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleInInput")
    def disable_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="estimatedInstanceWarmupInput")
    def estimated_instance_warmup_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "estimatedInstanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricSpecificationInput")
    def predefined_scaling_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification"], jsii.get(self, "predefinedScalingMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInCooldownInput")
    def scale_in_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleInCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleOutCooldownInput")
    def scale_out_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleOutCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValueInput")
    def target_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetValueInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleIn")
    def disable_scale_in(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableScaleIn"))

    @disable_scale_in.setter
    def disable_scale_in(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a50a3adc08ab914a2157a27748125b8dbade7af980ff06fba57728664bb9469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "estimatedInstanceWarmup"))

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b6c41223c5266f3102bc0906323ac245813f3bc477a923f4d1d4f51d3da2ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "estimatedInstanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="scaleInCooldown")
    def scale_in_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleInCooldown"))

    @scale_in_cooldown.setter
    def scale_in_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef905c8da8cd8f3bc6a04610c106255abf82334d2045b44f38abf8451d1e15d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleInCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="scaleOutCooldown")
    def scale_out_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleOutCooldown"))

    @scale_out_cooldown.setter
    def scale_out_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32777f9d8404388e2f98dc1600540f915dc743197e3ea56596f427ca59e195be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleOutCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f86ea1ee2b8fc791a69b234c9809ccef620b2873a724f948300ff9ad92cee31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f9defb1a6755266c3c7d2d8ed878669060e39a20848f27a8afb0badb94588a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_scaling_metric_type": "predefinedScalingMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification:
    def __init__(
        self,
        *,
        predefined_scaling_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_scaling_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_scaling_metric_type AutoscalingplansScalingPlan#predefined_scaling_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_label AutoscalingplansScalingPlan#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4277ae9ad587dee6fd02dbcb37da5a314d1ecb671958917c5cdd4195246418d)
            check_type(argname="argument predefined_scaling_metric_type", value=predefined_scaling_metric_type, expected_type=type_hints["predefined_scaling_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_scaling_metric_type": predefined_scaling_metric_type,
        }
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def predefined_scaling_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#predefined_scaling_metric_type AutoscalingplansScalingPlan#predefined_scaling_metric_type}.'''
        result = self._values.get("predefined_scaling_metric_type")
        assert result is not None, "Required property 'predefined_scaling_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscalingplans_scaling_plan#resource_label AutoscalingplansScalingPlan#resource_label}.'''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingplansScalingPlan.AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53ab9f7d7377e12579a696fedac2384296ce96612e3f7f1a929e19d254f46477)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResourceLabel")
    def reset_resource_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabel", []))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricTypeInput")
    def predefined_scaling_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedScalingMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricType")
    def predefined_scaling_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedScalingMetricType"))

    @predefined_scaling_metric_type.setter
    def predefined_scaling_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a5a5d89fed170b2121afb7db68511ccde64e844d729d1874557c3d87c030b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedScalingMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d2fdf261422b64ed8428be85b00d4d4a258926b76884bfd09ab6ce217f6903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47eac1e5a7f165bb5d7838a41dc7a1d078345ec5eb6456a279c2cd387b4d602)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AutoscalingplansScalingPlan",
    "AutoscalingplansScalingPlanApplicationSource",
    "AutoscalingplansScalingPlanApplicationSourceOutputReference",
    "AutoscalingplansScalingPlanApplicationSourceTagFilter",
    "AutoscalingplansScalingPlanApplicationSourceTagFilterList",
    "AutoscalingplansScalingPlanApplicationSourceTagFilterOutputReference",
    "AutoscalingplansScalingPlanConfig",
    "AutoscalingplansScalingPlanScalingInstruction",
    "AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification",
    "AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecificationOutputReference",
    "AutoscalingplansScalingPlanScalingInstructionList",
    "AutoscalingplansScalingPlanScalingInstructionOutputReference",
    "AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification",
    "AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecificationOutputReference",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationOutputReference",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationList",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationOutputReference",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification",
    "AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationOutputReference",
]

publication.publish()

def _typecheckingstub__a7f10dc03a1f67fc4e136bd5faedc45161ec9ad72da74f3efa5cacfb2ee2e69b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    application_source: typing.Union[AutoscalingplansScalingPlanApplicationSource, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    scaling_instruction: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanScalingInstruction, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__09f17307811092974227461d9afe889b366eb3f6a6e3395e85c0347c449c3ac4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanScalingInstruction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72f9a5a3762b89895534935b0f28e497aa1fd12a1e413f62005807ddd7aa7c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358fbf3483f3f4ce83d7de16fa170e1ef305392c6293f7f9ae72439fa247b2b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb834a6a14d839465da6d725c9ccf8c2f15a7001e65641c17379c5038351bea1(
    *,
    cloudformation_stack_arn: typing.Optional[builtins.str] = None,
    tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanApplicationSourceTagFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c1bad5b2816708db28518700dcec48d57ebfc9893d790efdb4c9cc4d779182(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a57d672eeb8968b234d1942ef3738e6602ce2c46b3ea60975923701b84ab3080(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanApplicationSourceTagFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea626d12ced9799be5a590d75543c0d07e88ab4f75e7b650fd3a9f3f59bc7bdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8194e35ef2a739e20189523ea3be4c87cebc75f8b887a945caaa39126506f158(
    value: typing.Optional[AutoscalingplansScalingPlanApplicationSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a15fec4220b3ebf9187dd18d76c8bfe67135a892a68e7417d3f4fde53e89a8(
    *,
    key: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9de03fd3cb141d21c2157c5a157ad3bcd36817cd4a9234019a7fad76ae42138(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30640161a5cf14c1b3f8eefe0c54b253630361bdd71ce2cd582953e76accbcd1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52552cddbf8b31fd8d4a2d86c1e7e2dfaf2732361b2a07b6f0e3f96b639d1bfb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049ab1bac59e0614183b8320989a72f6353a84df1432b30e1feec7acf4790a48(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea40d91f280583ed47b8752fe84b82d0cf43a9714f8f3b4fb42c5bf326237d5d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1520cfe66e5eca84322fbbe6f03708f999640b23689471d1380bed606aa95a02(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanApplicationSourceTagFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b9ba71f5048fd6d29839cf632b9a6d072f9c72780cb4e52cc00ce988250c70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b65e8de0bc2babf6244f1d5056da041b3ae9b23f5369051b295d3149eb2bd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e494a12d196438470b396dd676c5c609c94ae23373f167f13b079321e2cd06(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__241a4587c808d1cb37321253a7fa1d0dad876ea37f74afdc7bfd2360dfa6c31d(
    value: typing.Optional[typing.Union[AutoscalingplansScalingPlanApplicationSourceTagFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a383b3d1e5d5e7312b349b62ef7d9504b03e1f11955125f377b92e8f77557059(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    application_source: typing.Union[AutoscalingplansScalingPlanApplicationSource, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    scaling_instruction: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanScalingInstruction, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d619eb73ef21d1402bf4f7dee8530d05d597198010ed2678dab3be85f9bcfa(
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: builtins.str,
    target_tracking_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    customized_load_metric_specification: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_dynamic_scaling: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    predefined_load_metric_specification: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    predictive_scaling_max_capacity_behavior: typing.Optional[builtins.str] = None,
    predictive_scaling_max_capacity_buffer: typing.Optional[jsii.Number] = None,
    predictive_scaling_mode: typing.Optional[builtins.str] = None,
    scaling_policy_update_behavior: typing.Optional[builtins.str] = None,
    scheduled_action_buffer_time: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c83b7d762bb9e8c4e8e7b40608cceddc691587b6f705b01fc76772270f733ca(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    statistic: builtins.str,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d9f56de1c3ece837f8e70528a9a0c13419c7bb8463d725b45228bc3d2288d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b1f0566dfd002dc2590132a378cc48f93e236dffcb2d087d33c38eebbc05e0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742f25310183161bbcd9048f64b6b06d9e8f4172cb74c59c1e98cd22c65b9bd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068aaee26e1a77a51d269efb1aab2f68f592e7559ecef0682f298bd934bccba5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1410150e9a2ccf2cd69f11a13e58d231fadc7c16e984d3510ad29f43599ad1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c5442ed1b3a57aa4231869d0f4a35a20579b531eb795e8b3ce6dde8ea466964(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1799d21ca7363dbf9f80bcd3527200e9cdf54ca3ceea09501a10e240adb4b7b7(
    value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionCustomizedLoadMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e1cd0fdb00cc6561ff8900804b230db3ebf991a79f098e913f4a4beba1d99bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b062965d44863ed88643f1596b91f768f0937ada778b0b7ddb98d241ef855229(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5828feed030a6d4154044b8da109e023bae88f1316b451ac02443a2a1f6848fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e4eb0200c65538d47cae66f77fb864923ec24716b84816351ea1460666d938(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7cad00f76ba12d3b13882d7493ab7768d5ab5253f995b9cd6eb99bc43f58b9a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4144c0997fb5bfe476e3369f76a0549285794f84082e96acef13a125d7eb5241(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstruction]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__392e0fd72bdba740b164b5157fe7c5e980326bacd26327ad1b170ef7f664d24b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7773ad72e2c19f7a56a36cb11609f675e0f49278ce3aaae92be5328b47c133e6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ce4363403f8a24c323c0989d6b8e8fdb73955c0020b494b141012f5916d5c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6c336fe21e6635ee57ceb90ed0dc61933a7ab00d4a72af4147e89a71281d82(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ab893310c6fc9aedbbc4d16fa5d17eef0829a06ec63cad691c6d5b7dbb2553(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a239156fbdf9703bbca2a66ec81d61f50489fbfcf2c0fd887e6c65944622cb8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a643eefbeee6e1a7feeb97f7dd4101d8032227cc85a51762024a6570c1baf4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b60b017838d4e3e67ac0d49e255c58eb83ef8b2bf94486b6410233fc12c243d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aaa5486442c3319eacbf1f7a420c5d20b777343de5a268d999c78bae1d5b9eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef5d46887084bf45a01de50db24088c5bf5f169b1cec4300905b7815170ef12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442df57875773f9180720d27bfe7aaf72a1e392bd831707a8170469c1eb61bba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45284612816b189613904c4858de0e458ddfc932d8a66f099298b75864bfd54d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c9a1df5ca37b1358faaaaa3da6232f696b3bea6784ae09eff9c59e7ead6366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e05958771a83aa32c8374793603b30aa036ef510941a7eeddcf3468c4d9b55e0(
    value: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstruction, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da8e1c0173f3135d42ecd01e4357502012df2636b191219d4f0a240c0001b1c(
    *,
    predefined_load_metric_type: builtins.str,
    resource_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a82e19ee4ce4d22aa3e0a339800ba40bb27cc8218fec4e1acf18d9256158532(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f5681857cf5d328b8f38c906d9028b7b0ddb313922e4edb2c6261cf6ebb80c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4ba07d5c29f0591644ba0e84f997667f83e2c9226e6388df8411ac7785d8bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33c3b65e6d12a4b08e773bf076ac95fb7bce72c5b7960e7db97ecb3612805ce(
    value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionPredefinedLoadMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6ee08e5ead2791fdb599bcba4342d7bf4b5d1d37399e5994f9e0e9eb8e9903(
    *,
    target_value: jsii.Number,
    customized_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    estimated_instance_warmup: typing.Optional[jsii.Number] = None,
    predefined_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_in_cooldown: typing.Optional[jsii.Number] = None,
    scale_out_cooldown: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9458ce2487c8bdc94839e6a549b8bb47df298a9e2340a70382492ee478bdd7(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    statistic: builtins.str,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e690ddbe9d737200b0c783699adbec9a47d71c60e0d7e8417de85bafbc5015(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ea6348402711f230ddcb2e642b5bfc3520281b63cb1e4fb1ca3dd63cdc5cae(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d94f8aca4476bf38526c8e9e5f459a2db35798d497273e43e142e3adf2a7dc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0affeea55d78bfd607c76b9e4affcb85a679907ff62efc6040c1c6bc86c7a319(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d91df8fc35db8d3b1ece8683a64ea460b0cf8f1dbc691e51a0497bfa3587e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e7d4d0fdd56318dcae5472216d3e03da7bb95a86f7fee9b4254c7ce3058122(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63b1ac29c6cccd9f7c888a1119faa6d03c94ea534036d7a85dcd56f965ccfd6(
    value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86610d6a0afbd81a9baad57dde2a86b9a6819d3711a95abe77a9d59648dacbc8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__038c51796db0d1453f840640a69ce4482e3ec4d62c5921435ccd6cf378c40971(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74cb441e03ec7ab37b0347498b45e2c4e0e7d094a9936a7b2d382d2ee7134d30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea0a7469acb6aa6aa48eafc52a636977b0e691c8bf0fbec719007d30eb2e662(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf319c9f4612b2011ae0b34590c2c792bcc3133594a0a027be6ad519ac98552(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd2872b35b7e6f47076c87274cbadfb9f463d469a464af44cf1f58f417efa83(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3e23a245b36f0ac95cb393b0945fdcfcfbb3e537ca2c268fd2796df8178a5d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a50a3adc08ab914a2157a27748125b8dbade7af980ff06fba57728664bb9469(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b6c41223c5266f3102bc0906323ac245813f3bc477a923f4d1d4f51d3da2ed(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef905c8da8cd8f3bc6a04610c106255abf82334d2045b44f38abf8451d1e15d8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32777f9d8404388e2f98dc1600540f915dc743197e3ea56596f427ca59e195be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f86ea1ee2b8fc791a69b234c9809ccef620b2873a724f948300ff9ad92cee31(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f9defb1a6755266c3c7d2d8ed878669060e39a20848f27a8afb0badb94588a(
    value: typing.Optional[typing.Union[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4277ae9ad587dee6fd02dbcb37da5a314d1ecb671958917c5cdd4195246418d(
    *,
    predefined_scaling_metric_type: builtins.str,
    resource_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ab9f7d7377e12579a696fedac2384296ce96612e3f7f1a929e19d254f46477(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a5a5d89fed170b2121afb7db68511ccde64e844d729d1874557c3d87c030b10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d2fdf261422b64ed8428be85b00d4d4a258926b76884bfd09ab6ce217f6903(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47eac1e5a7f165bb5d7838a41dc7a1d078345ec5eb6456a279c2cd387b4d602(
    value: typing.Optional[AutoscalingplansScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass
