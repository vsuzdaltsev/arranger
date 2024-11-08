'''
# `aws_emr_managed_scaling_policy`

Refer to the Terraform Registory for docs: [`aws_emr_managed_scaling_policy`](https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy).
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


class EmrManagedScalingPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrManagedScalingPolicy.EmrManagedScalingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy aws_emr_managed_scaling_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        compute_limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrManagedScalingPolicyComputeLimits", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy aws_emr_managed_scaling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#cluster_id EmrManagedScalingPolicy#cluster_id}.
        :param compute_limits: compute_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#compute_limits EmrManagedScalingPolicy#compute_limits}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#id EmrManagedScalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20389d6f5c5b0753152a1aef13fae3331f5d00df7a1d8d40f1a4ff5eb7428df4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EmrManagedScalingPolicyConfig(
            cluster_id=cluster_id,
            compute_limits=compute_limits,
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

    @jsii.member(jsii_name="putComputeLimits")
    def put_compute_limits(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EmrManagedScalingPolicyComputeLimits", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f135b12410f12319c6f3e69e5baaac4f0e6b4e866b6357445e56a2efcc4d275)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putComputeLimits", [value]))

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
    @jsii.member(jsii_name="computeLimits")
    def compute_limits(self) -> "EmrManagedScalingPolicyComputeLimitsList":
        return typing.cast("EmrManagedScalingPolicyComputeLimitsList", jsii.get(self, "computeLimits"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="computeLimitsInput")
    def compute_limits_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrManagedScalingPolicyComputeLimits"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EmrManagedScalingPolicyComputeLimits"]]], jsii.get(self, "computeLimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8122e4de39fad6653a0d36b0987adfa2415ac47c05083f0dbf89ef058c5295a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d11b168998b268c7f3c055bfc0eb862726de93fde757da37af0928d9dbb2a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.emrManagedScalingPolicy.EmrManagedScalingPolicyComputeLimits",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_capacity_units": "maximumCapacityUnits",
        "minimum_capacity_units": "minimumCapacityUnits",
        "unit_type": "unitType",
        "maximum_core_capacity_units": "maximumCoreCapacityUnits",
        "maximum_ondemand_capacity_units": "maximumOndemandCapacityUnits",
    },
)
class EmrManagedScalingPolicyComputeLimits:
    def __init__(
        self,
        *,
        maximum_capacity_units: jsii.Number,
        minimum_capacity_units: jsii.Number,
        unit_type: builtins.str,
        maximum_core_capacity_units: typing.Optional[jsii.Number] = None,
        maximum_ondemand_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#maximum_capacity_units EmrManagedScalingPolicy#maximum_capacity_units}.
        :param minimum_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#minimum_capacity_units EmrManagedScalingPolicy#minimum_capacity_units}.
        :param unit_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#unit_type EmrManagedScalingPolicy#unit_type}.
        :param maximum_core_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#maximum_core_capacity_units EmrManagedScalingPolicy#maximum_core_capacity_units}.
        :param maximum_ondemand_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#maximum_ondemand_capacity_units EmrManagedScalingPolicy#maximum_ondemand_capacity_units}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__148de4c11015a30a451e5037daab3491baa96a582da701cd7813b415ed594a37)
            check_type(argname="argument maximum_capacity_units", value=maximum_capacity_units, expected_type=type_hints["maximum_capacity_units"])
            check_type(argname="argument minimum_capacity_units", value=minimum_capacity_units, expected_type=type_hints["minimum_capacity_units"])
            check_type(argname="argument unit_type", value=unit_type, expected_type=type_hints["unit_type"])
            check_type(argname="argument maximum_core_capacity_units", value=maximum_core_capacity_units, expected_type=type_hints["maximum_core_capacity_units"])
            check_type(argname="argument maximum_ondemand_capacity_units", value=maximum_ondemand_capacity_units, expected_type=type_hints["maximum_ondemand_capacity_units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "maximum_capacity_units": maximum_capacity_units,
            "minimum_capacity_units": minimum_capacity_units,
            "unit_type": unit_type,
        }
        if maximum_core_capacity_units is not None:
            self._values["maximum_core_capacity_units"] = maximum_core_capacity_units
        if maximum_ondemand_capacity_units is not None:
            self._values["maximum_ondemand_capacity_units"] = maximum_ondemand_capacity_units

    @builtins.property
    def maximum_capacity_units(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#maximum_capacity_units EmrManagedScalingPolicy#maximum_capacity_units}.'''
        result = self._values.get("maximum_capacity_units")
        assert result is not None, "Required property 'maximum_capacity_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minimum_capacity_units(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#minimum_capacity_units EmrManagedScalingPolicy#minimum_capacity_units}.'''
        result = self._values.get("minimum_capacity_units")
        assert result is not None, "Required property 'minimum_capacity_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unit_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#unit_type EmrManagedScalingPolicy#unit_type}.'''
        result = self._values.get("unit_type")
        assert result is not None, "Required property 'unit_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maximum_core_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#maximum_core_capacity_units EmrManagedScalingPolicy#maximum_core_capacity_units}.'''
        result = self._values.get("maximum_core_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_ondemand_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#maximum_ondemand_capacity_units EmrManagedScalingPolicy#maximum_ondemand_capacity_units}.'''
        result = self._values.get("maximum_ondemand_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrManagedScalingPolicyComputeLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrManagedScalingPolicyComputeLimitsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrManagedScalingPolicy.EmrManagedScalingPolicyComputeLimitsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71460b3e23871c15e9a2ce1c54744e83e1c692bb2f8c058134e88142c7894317)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EmrManagedScalingPolicyComputeLimitsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3720c1d1e6fd93c03743d0c93f658356025c8f1913e13a7fc6c7c0e85d551971)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrManagedScalingPolicyComputeLimitsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a6d7587f0b3d1a410287263f44dd8912b09cb7f93126af660ce6673ff8babc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e736dfa68e0a8273283d1ee10e4c2f8c4970884e3aec44c885b414bc34bc7624)
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
            type_hints = typing.get_type_hints(_typecheckingstub__44689303c0f1db8972f0c7550b1199cf4e6430690286968beaa474edb5f1a6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrManagedScalingPolicyComputeLimits]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrManagedScalingPolicyComputeLimits]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrManagedScalingPolicyComputeLimits]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef94cded0f4af8af25999e13f2590682d162828b7564f655d51225c0ed72705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrManagedScalingPolicyComputeLimitsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.emrManagedScalingPolicy.EmrManagedScalingPolicyComputeLimitsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2efb6eeb7e3e3c3040169ab6f825112dd15360a8fe3582a143b358a542870203)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaximumCoreCapacityUnits")
    def reset_maximum_core_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumCoreCapacityUnits", []))

    @jsii.member(jsii_name="resetMaximumOndemandCapacityUnits")
    def reset_maximum_ondemand_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumOndemandCapacityUnits", []))

    @builtins.property
    @jsii.member(jsii_name="maximumCapacityUnitsInput")
    def maximum_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCoreCapacityUnitsInput")
    def maximum_core_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCoreCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumOndemandCapacityUnitsInput")
    def maximum_ondemand_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumOndemandCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumCapacityUnitsInput")
    def minimum_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="unitTypeInput")
    def unit_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCapacityUnits")
    def maximum_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCapacityUnits"))

    @maximum_capacity_units.setter
    def maximum_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b596f691f5a116858445926187615be427bbf916ca4e5aaf8f2fae4212c116a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="maximumCoreCapacityUnits")
    def maximum_core_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCoreCapacityUnits"))

    @maximum_core_capacity_units.setter
    def maximum_core_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d50eba2fc2da1a5a04b8209cb69a06afcc8e0442f311a789f1907e0439a311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCoreCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="maximumOndemandCapacityUnits")
    def maximum_ondemand_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumOndemandCapacityUnits"))

    @maximum_ondemand_capacity_units.setter
    def maximum_ondemand_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4625d61339a20b63ff8aab99e06cd3c286eb40f4b7ab65d5ffb22bbe9bbe7455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumOndemandCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="minimumCapacityUnits")
    def minimum_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumCapacityUnits"))

    @minimum_capacity_units.setter
    def minimum_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a363104ed26ca01049cab3e3c1c1e1f9a045f8f5cdaee8d747295edda92e6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="unitType")
    def unit_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unitType"))

    @unit_type.setter
    def unit_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16ba1a7cf4b515554c4bf465adbb76e5790ac2814aa9963dc832a0ab3e519a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unitType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrManagedScalingPolicyComputeLimits, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrManagedScalingPolicyComputeLimits, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrManagedScalingPolicyComputeLimits, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da2d3e0095b06d2fac49d1c20c1b287e8b801d310ae9c64b4bf4fd1c5836aebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.emrManagedScalingPolicy.EmrManagedScalingPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "compute_limits": "computeLimits",
        "id": "id",
    },
)
class EmrManagedScalingPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_id: builtins.str,
        compute_limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrManagedScalingPolicyComputeLimits, typing.Dict[builtins.str, typing.Any]]]],
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
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#cluster_id EmrManagedScalingPolicy#cluster_id}.
        :param compute_limits: compute_limits block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#compute_limits EmrManagedScalingPolicy#compute_limits}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#id EmrManagedScalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34eff1474520cdae77c09c0e0a9357b667f917376b611a895215c671fdbb632)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument compute_limits", value=compute_limits, expected_type=type_hints["compute_limits"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
            "compute_limits": compute_limits,
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
    def cluster_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#cluster_id EmrManagedScalingPolicy#cluster_id}.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_limits(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrManagedScalingPolicyComputeLimits]]:
        '''compute_limits block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#compute_limits EmrManagedScalingPolicy#compute_limits}
        '''
        result = self._values.get("compute_limits")
        assert result is not None, "Required property 'compute_limits' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrManagedScalingPolicyComputeLimits]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_managed_scaling_policy#id EmrManagedScalingPolicy#id}.

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
        return "EmrManagedScalingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EmrManagedScalingPolicy",
    "EmrManagedScalingPolicyComputeLimits",
    "EmrManagedScalingPolicyComputeLimitsList",
    "EmrManagedScalingPolicyComputeLimitsOutputReference",
    "EmrManagedScalingPolicyConfig",
]

publication.publish()

def _typecheckingstub__20389d6f5c5b0753152a1aef13fae3331f5d00df7a1d8d40f1a4ff5eb7428df4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: builtins.str,
    compute_limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrManagedScalingPolicyComputeLimits, typing.Dict[builtins.str, typing.Any]]]],
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

def _typecheckingstub__8f135b12410f12319c6f3e69e5baaac4f0e6b4e866b6357445e56a2efcc4d275(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrManagedScalingPolicyComputeLimits, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8122e4de39fad6653a0d36b0987adfa2415ac47c05083f0dbf89ef058c5295a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d11b168998b268c7f3c055bfc0eb862726de93fde757da37af0928d9dbb2a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__148de4c11015a30a451e5037daab3491baa96a582da701cd7813b415ed594a37(
    *,
    maximum_capacity_units: jsii.Number,
    minimum_capacity_units: jsii.Number,
    unit_type: builtins.str,
    maximum_core_capacity_units: typing.Optional[jsii.Number] = None,
    maximum_ondemand_capacity_units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71460b3e23871c15e9a2ce1c54744e83e1c692bb2f8c058134e88142c7894317(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3720c1d1e6fd93c03743d0c93f658356025c8f1913e13a7fc6c7c0e85d551971(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a6d7587f0b3d1a410287263f44dd8912b09cb7f93126af660ce6673ff8babc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e736dfa68e0a8273283d1ee10e4c2f8c4970884e3aec44c885b414bc34bc7624(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44689303c0f1db8972f0c7550b1199cf4e6430690286968beaa474edb5f1a6d1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef94cded0f4af8af25999e13f2590682d162828b7564f655d51225c0ed72705(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EmrManagedScalingPolicyComputeLimits]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efb6eeb7e3e3c3040169ab6f825112dd15360a8fe3582a143b358a542870203(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b596f691f5a116858445926187615be427bbf916ca4e5aaf8f2fae4212c116a7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d50eba2fc2da1a5a04b8209cb69a06afcc8e0442f311a789f1907e0439a311(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4625d61339a20b63ff8aab99e06cd3c286eb40f4b7ab65d5ffb22bbe9bbe7455(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a363104ed26ca01049cab3e3c1c1e1f9a045f8f5cdaee8d747295edda92e6b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ba1a7cf4b515554c4bf465adbb76e5790ac2814aa9963dc832a0ab3e519a79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da2d3e0095b06d2fac49d1c20c1b287e8b801d310ae9c64b4bf4fd1c5836aebd(
    value: typing.Optional[typing.Union[EmrManagedScalingPolicyComputeLimits, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34eff1474520cdae77c09c0e0a9357b667f917376b611a895215c671fdbb632(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_id: builtins.str,
    compute_limits: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EmrManagedScalingPolicyComputeLimits, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
