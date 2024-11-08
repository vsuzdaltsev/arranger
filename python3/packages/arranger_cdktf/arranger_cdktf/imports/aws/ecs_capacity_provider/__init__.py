'''
# `aws_ecs_capacity_provider`

Refer to the Terraform Registory for docs: [`aws_ecs_capacity_provider`](https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider).
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


class EcsCapacityProvider(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsCapacityProvider.EcsCapacityProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider aws_ecs_capacity_provider}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        auto_scaling_group_provider: typing.Union["EcsCapacityProviderAutoScalingGroupProvider", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider aws_ecs_capacity_provider} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auto_scaling_group_provider: auto_scaling_group_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_provider EcsCapacityProvider#auto_scaling_group_provider}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#name EcsCapacityProvider#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#id EcsCapacityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags EcsCapacityProvider#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags_all EcsCapacityProvider#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ed448b82bbb1e4e6a42e68762cafeac0052fab27a16b1e42d25bbfa58dcb0b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsCapacityProviderConfig(
            auto_scaling_group_provider=auto_scaling_group_provider,
            name=name,
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

    @jsii.member(jsii_name="putAutoScalingGroupProvider")
    def put_auto_scaling_group_provider(
        self,
        *,
        auto_scaling_group_arn: builtins.str,
        managed_scaling: typing.Optional[typing.Union["EcsCapacityProviderAutoScalingGroupProviderManagedScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        managed_termination_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_scaling_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_arn EcsCapacityProvider#auto_scaling_group_arn}.
        :param managed_scaling: managed_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_scaling EcsCapacityProvider#managed_scaling}
        :param managed_termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_termination_protection EcsCapacityProvider#managed_termination_protection}.
        '''
        value = EcsCapacityProviderAutoScalingGroupProvider(
            auto_scaling_group_arn=auto_scaling_group_arn,
            managed_scaling=managed_scaling,
            managed_termination_protection=managed_termination_protection,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScalingGroupProvider", [value]))

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
    @jsii.member(jsii_name="autoScalingGroupProvider")
    def auto_scaling_group_provider(
        self,
    ) -> "EcsCapacityProviderAutoScalingGroupProviderOutputReference":
        return typing.cast("EcsCapacityProviderAutoScalingGroupProviderOutputReference", jsii.get(self, "autoScalingGroupProvider"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupProviderInput")
    def auto_scaling_group_provider_input(
        self,
    ) -> typing.Optional["EcsCapacityProviderAutoScalingGroupProvider"]:
        return typing.cast(typing.Optional["EcsCapacityProviderAutoScalingGroupProvider"], jsii.get(self, "autoScalingGroupProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__bd2cefd0ace90771607900be582404cb0afd4097eb76b568467285dcb618dd74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__250f81448b5fa3352de7371249224f53231c6d812d7bb0add505f4dc0252f3a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e3542871cc6384b7c8cf72cf3fc486d4954633c4b70c10d1916332f8e3d8da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__644d658ff30c40543931365893e0e15680d3834155811e3f2d44222d8e448440)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.ecsCapacityProvider.EcsCapacityProviderAutoScalingGroupProvider",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group_arn": "autoScalingGroupArn",
        "managed_scaling": "managedScaling",
        "managed_termination_protection": "managedTerminationProtection",
    },
)
class EcsCapacityProviderAutoScalingGroupProvider:
    def __init__(
        self,
        *,
        auto_scaling_group_arn: builtins.str,
        managed_scaling: typing.Optional[typing.Union["EcsCapacityProviderAutoScalingGroupProviderManagedScaling", typing.Dict[builtins.str, typing.Any]]] = None,
        managed_termination_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_scaling_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_arn EcsCapacityProvider#auto_scaling_group_arn}.
        :param managed_scaling: managed_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_scaling EcsCapacityProvider#managed_scaling}
        :param managed_termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_termination_protection EcsCapacityProvider#managed_termination_protection}.
        '''
        if isinstance(managed_scaling, dict):
            managed_scaling = EcsCapacityProviderAutoScalingGroupProviderManagedScaling(**managed_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e616cba175bdc430a8a622984869d094668671f59f2fb43d60b5ed589c61d583)
            check_type(argname="argument auto_scaling_group_arn", value=auto_scaling_group_arn, expected_type=type_hints["auto_scaling_group_arn"])
            check_type(argname="argument managed_scaling", value=managed_scaling, expected_type=type_hints["managed_scaling"])
            check_type(argname="argument managed_termination_protection", value=managed_termination_protection, expected_type=type_hints["managed_termination_protection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_group_arn": auto_scaling_group_arn,
        }
        if managed_scaling is not None:
            self._values["managed_scaling"] = managed_scaling
        if managed_termination_protection is not None:
            self._values["managed_termination_protection"] = managed_termination_protection

    @builtins.property
    def auto_scaling_group_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_arn EcsCapacityProvider#auto_scaling_group_arn}.'''
        result = self._values.get("auto_scaling_group_arn")
        assert result is not None, "Required property 'auto_scaling_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_scaling(
        self,
    ) -> typing.Optional["EcsCapacityProviderAutoScalingGroupProviderManagedScaling"]:
        '''managed_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_scaling EcsCapacityProvider#managed_scaling}
        '''
        result = self._values.get("managed_scaling")
        return typing.cast(typing.Optional["EcsCapacityProviderAutoScalingGroupProviderManagedScaling"], result)

    @builtins.property
    def managed_termination_protection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#managed_termination_protection EcsCapacityProvider#managed_termination_protection}.'''
        result = self._values.get("managed_termination_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsCapacityProviderAutoScalingGroupProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsCapacityProvider.EcsCapacityProviderAutoScalingGroupProviderManagedScaling",
    jsii_struct_bases=[],
    name_mapping={
        "instance_warmup_period": "instanceWarmupPeriod",
        "maximum_scaling_step_size": "maximumScalingStepSize",
        "minimum_scaling_step_size": "minimumScalingStepSize",
        "status": "status",
        "target_capacity": "targetCapacity",
    },
)
class EcsCapacityProviderAutoScalingGroupProviderManagedScaling:
    def __init__(
        self,
        *,
        instance_warmup_period: typing.Optional[jsii.Number] = None,
        maximum_scaling_step_size: typing.Optional[jsii.Number] = None,
        minimum_scaling_step_size: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        target_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_warmup_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#instance_warmup_period EcsCapacityProvider#instance_warmup_period}.
        :param maximum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#maximum_scaling_step_size EcsCapacityProvider#maximum_scaling_step_size}.
        :param minimum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#minimum_scaling_step_size EcsCapacityProvider#minimum_scaling_step_size}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#status EcsCapacityProvider#status}.
        :param target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#target_capacity EcsCapacityProvider#target_capacity}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc8dc3bb7374e54351d42dba9a5f6918255febcb05d94a65ca01d476a8438547)
            check_type(argname="argument instance_warmup_period", value=instance_warmup_period, expected_type=type_hints["instance_warmup_period"])
            check_type(argname="argument maximum_scaling_step_size", value=maximum_scaling_step_size, expected_type=type_hints["maximum_scaling_step_size"])
            check_type(argname="argument minimum_scaling_step_size", value=minimum_scaling_step_size, expected_type=type_hints["minimum_scaling_step_size"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument target_capacity", value=target_capacity, expected_type=type_hints["target_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_warmup_period is not None:
            self._values["instance_warmup_period"] = instance_warmup_period
        if maximum_scaling_step_size is not None:
            self._values["maximum_scaling_step_size"] = maximum_scaling_step_size
        if minimum_scaling_step_size is not None:
            self._values["minimum_scaling_step_size"] = minimum_scaling_step_size
        if status is not None:
            self._values["status"] = status
        if target_capacity is not None:
            self._values["target_capacity"] = target_capacity

    @builtins.property
    def instance_warmup_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#instance_warmup_period EcsCapacityProvider#instance_warmup_period}.'''
        result = self._values.get("instance_warmup_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_scaling_step_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#maximum_scaling_step_size EcsCapacityProvider#maximum_scaling_step_size}.'''
        result = self._values.get("maximum_scaling_step_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_scaling_step_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#minimum_scaling_step_size EcsCapacityProvider#minimum_scaling_step_size}.'''
        result = self._values.get("minimum_scaling_step_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#status EcsCapacityProvider#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#target_capacity EcsCapacityProvider#target_capacity}.'''
        result = self._values.get("target_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsCapacityProviderAutoScalingGroupProviderManagedScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsCapacityProvider.EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7eeb56b323281bbd90a727b870db265a03467635bc052cce1609ab8ddebad651)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceWarmupPeriod")
    def reset_instance_warmup_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceWarmupPeriod", []))

    @jsii.member(jsii_name="resetMaximumScalingStepSize")
    def reset_maximum_scaling_step_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumScalingStepSize", []))

    @jsii.member(jsii_name="resetMinimumScalingStepSize")
    def reset_minimum_scaling_step_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumScalingStepSize", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetTargetCapacity")
    def reset_target_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="instanceWarmupPeriodInput")
    def instance_warmup_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceWarmupPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumScalingStepSizeInput")
    def maximum_scaling_step_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumScalingStepSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumScalingStepSizeInput")
    def minimum_scaling_step_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumScalingStepSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="targetCapacityInput")
    def target_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceWarmupPeriod")
    def instance_warmup_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceWarmupPeriod"))

    @instance_warmup_period.setter
    def instance_warmup_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25265baa39bf05e7434d47eddd0566c15579ced09e67eb5387e3525390803b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceWarmupPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="maximumScalingStepSize")
    def maximum_scaling_step_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumScalingStepSize"))

    @maximum_scaling_step_size.setter
    def maximum_scaling_step_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adde81c3ffc5b9983889b1f51b9d6eef7b912e0aaaedaad652d33ce2f6887abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumScalingStepSize", value)

    @builtins.property
    @jsii.member(jsii_name="minimumScalingStepSize")
    def minimum_scaling_step_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumScalingStepSize"))

    @minimum_scaling_step_size.setter
    def minimum_scaling_step_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e394e7ee0b385ce1664fe84c00f151784cda87e46c7ad02621c77e6417805cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumScalingStepSize", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd0d3d1e7895c8935a8858ad92139407790aaacd775b52af21051453e3205df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="targetCapacity")
    def target_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetCapacity"))

    @target_capacity.setter
    def target_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf1931698fb232ebbb1fd3b16a360870bd73a85c7e27107203e64421dbbd4810)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling]:
        return typing.cast(typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0306bd4a1bd4d7fc9fcb9d8312193d91f3cd602f611cad1b10d9a26691d67dfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsCapacityProviderAutoScalingGroupProviderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsCapacityProvider.EcsCapacityProviderAutoScalingGroupProviderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98748aba0b2e24648d50dd7f2b387d1d499549444c2030f96e6346c0703263c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putManagedScaling")
    def put_managed_scaling(
        self,
        *,
        instance_warmup_period: typing.Optional[jsii.Number] = None,
        maximum_scaling_step_size: typing.Optional[jsii.Number] = None,
        minimum_scaling_step_size: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
        target_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_warmup_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#instance_warmup_period EcsCapacityProvider#instance_warmup_period}.
        :param maximum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#maximum_scaling_step_size EcsCapacityProvider#maximum_scaling_step_size}.
        :param minimum_scaling_step_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#minimum_scaling_step_size EcsCapacityProvider#minimum_scaling_step_size}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#status EcsCapacityProvider#status}.
        :param target_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#target_capacity EcsCapacityProvider#target_capacity}.
        '''
        value = EcsCapacityProviderAutoScalingGroupProviderManagedScaling(
            instance_warmup_period=instance_warmup_period,
            maximum_scaling_step_size=maximum_scaling_step_size,
            minimum_scaling_step_size=minimum_scaling_step_size,
            status=status,
            target_capacity=target_capacity,
        )

        return typing.cast(None, jsii.invoke(self, "putManagedScaling", [value]))

    @jsii.member(jsii_name="resetManagedScaling")
    def reset_managed_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedScaling", []))

    @jsii.member(jsii_name="resetManagedTerminationProtection")
    def reset_managed_termination_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedTerminationProtection", []))

    @builtins.property
    @jsii.member(jsii_name="managedScaling")
    def managed_scaling(
        self,
    ) -> EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference:
        return typing.cast(EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference, jsii.get(self, "managedScaling"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupArnInput")
    def auto_scaling_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="managedScalingInput")
    def managed_scaling_input(
        self,
    ) -> typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling]:
        return typing.cast(typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling], jsii.get(self, "managedScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="managedTerminationProtectionInput")
    def managed_termination_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedTerminationProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoScalingGroupArn"))

    @auto_scaling_group_arn.setter
    def auto_scaling_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b68b4349ffae1b211d591c2db2573f36796e9773db5e2f267e53d4f67575ebb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="managedTerminationProtection")
    def managed_termination_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedTerminationProtection"))

    @managed_termination_protection.setter
    def managed_termination_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923b07faac7181dd4f5167752601abaa9331ecae87d471c7fd5b174161333e79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedTerminationProtection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsCapacityProviderAutoScalingGroupProvider]:
        return typing.cast(typing.Optional[EcsCapacityProviderAutoScalingGroupProvider], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsCapacityProviderAutoScalingGroupProvider],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8536df534c0e009b75eaff4bd44aa82824c262a959f660480f2cc7ff6b12778d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ecsCapacityProvider.EcsCapacityProviderConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auto_scaling_group_provider": "autoScalingGroupProvider",
        "name": "name",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class EcsCapacityProviderConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        auto_scaling_group_provider: typing.Union[EcsCapacityProviderAutoScalingGroupProvider, typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
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
        :param auto_scaling_group_provider: auto_scaling_group_provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_provider EcsCapacityProvider#auto_scaling_group_provider}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#name EcsCapacityProvider#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#id EcsCapacityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags EcsCapacityProvider#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags_all EcsCapacityProvider#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_scaling_group_provider, dict):
            auto_scaling_group_provider = EcsCapacityProviderAutoScalingGroupProvider(**auto_scaling_group_provider)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__636cde164082fa9e6b6fa2b7e78641ea8b8a5455cfb9ef5800b93fc22f818918)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auto_scaling_group_provider", value=auto_scaling_group_provider, expected_type=type_hints["auto_scaling_group_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_group_provider": auto_scaling_group_provider,
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
    def auto_scaling_group_provider(
        self,
    ) -> EcsCapacityProviderAutoScalingGroupProvider:
        '''auto_scaling_group_provider block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#auto_scaling_group_provider EcsCapacityProvider#auto_scaling_group_provider}
        '''
        result = self._values.get("auto_scaling_group_provider")
        assert result is not None, "Required property 'auto_scaling_group_provider' is missing"
        return typing.cast(EcsCapacityProviderAutoScalingGroupProvider, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#name EcsCapacityProvider#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#id EcsCapacityProvider#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags EcsCapacityProvider#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_capacity_provider#tags_all EcsCapacityProvider#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsCapacityProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EcsCapacityProvider",
    "EcsCapacityProviderAutoScalingGroupProvider",
    "EcsCapacityProviderAutoScalingGroupProviderManagedScaling",
    "EcsCapacityProviderAutoScalingGroupProviderManagedScalingOutputReference",
    "EcsCapacityProviderAutoScalingGroupProviderOutputReference",
    "EcsCapacityProviderConfig",
]

publication.publish()

def _typecheckingstub__80ed448b82bbb1e4e6a42e68762cafeac0052fab27a16b1e42d25bbfa58dcb0b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    auto_scaling_group_provider: typing.Union[EcsCapacityProviderAutoScalingGroupProvider, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
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

def _typecheckingstub__bd2cefd0ace90771607900be582404cb0afd4097eb76b568467285dcb618dd74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250f81448b5fa3352de7371249224f53231c6d812d7bb0add505f4dc0252f3a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e3542871cc6384b7c8cf72cf3fc486d4954633c4b70c10d1916332f8e3d8da(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644d658ff30c40543931365893e0e15680d3834155811e3f2d44222d8e448440(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e616cba175bdc430a8a622984869d094668671f59f2fb43d60b5ed589c61d583(
    *,
    auto_scaling_group_arn: builtins.str,
    managed_scaling: typing.Optional[typing.Union[EcsCapacityProviderAutoScalingGroupProviderManagedScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    managed_termination_protection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc8dc3bb7374e54351d42dba9a5f6918255febcb05d94a65ca01d476a8438547(
    *,
    instance_warmup_period: typing.Optional[jsii.Number] = None,
    maximum_scaling_step_size: typing.Optional[jsii.Number] = None,
    minimum_scaling_step_size: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
    target_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eeb56b323281bbd90a727b870db265a03467635bc052cce1609ab8ddebad651(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25265baa39bf05e7434d47eddd0566c15579ced09e67eb5387e3525390803b26(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adde81c3ffc5b9983889b1f51b9d6eef7b912e0aaaedaad652d33ce2f6887abb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e394e7ee0b385ce1664fe84c00f151784cda87e46c7ad02621c77e6417805cb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd0d3d1e7895c8935a8858ad92139407790aaacd775b52af21051453e3205df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf1931698fb232ebbb1fd3b16a360870bd73a85c7e27107203e64421dbbd4810(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0306bd4a1bd4d7fc9fcb9d8312193d91f3cd602f611cad1b10d9a26691d67dfe(
    value: typing.Optional[EcsCapacityProviderAutoScalingGroupProviderManagedScaling],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98748aba0b2e24648d50dd7f2b387d1d499549444c2030f96e6346c0703263c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b68b4349ffae1b211d591c2db2573f36796e9773db5e2f267e53d4f67575ebb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923b07faac7181dd4f5167752601abaa9331ecae87d471c7fd5b174161333e79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8536df534c0e009b75eaff4bd44aa82824c262a959f660480f2cc7ff6b12778d(
    value: typing.Optional[EcsCapacityProviderAutoScalingGroupProvider],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__636cde164082fa9e6b6fa2b7e78641ea8b8a5455cfb9ef5800b93fc22f818918(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    auto_scaling_group_provider: typing.Union[EcsCapacityProviderAutoScalingGroupProvider, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
