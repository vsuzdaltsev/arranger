'''
# `aws_autoscaling_policy`

Refer to the Terraform Registory for docs: [`aws_autoscaling_policy`](https://www.terraform.io/docs/providers/aws/r/autoscaling_policy).
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


class AutoscalingPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy aws_autoscaling_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        autoscaling_group_name: builtins.str,
        name: builtins.str,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_type: typing.Optional[builtins.str] = None,
        predictive_scaling_configuration: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        scaling_adjustment: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyStepAdjustment", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_tracking_configuration: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy aws_autoscaling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#autoscaling_group_name AutoscalingPolicy#autoscaling_group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#adjustment_type AutoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#cooldown AutoscalingPolicy#cooldown}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#enabled AutoscalingPolicy#enabled}.
        :param estimated_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#estimated_instance_warmup AutoscalingPolicy#estimated_instance_warmup}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_aggregation_type AutoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#min_adjustment_magnitude AutoscalingPolicy#min_adjustment_magnitude}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#policy_type AutoscalingPolicy#policy_type}.
        :param predictive_scaling_configuration: predictive_scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predictive_scaling_configuration AutoscalingPolicy#predictive_scaling_configuration}
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#step_adjustment AutoscalingPolicy#step_adjustment}
        :param target_tracking_configuration: target_tracking_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_tracking_configuration AutoscalingPolicy#target_tracking_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c771ea35817bd88a6d6b42bd8c66e61b3bf14e6ff8f5e57a58991f77771e54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutoscalingPolicyConfig(
            autoscaling_group_name=autoscaling_group_name,
            name=name,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            enabled=enabled,
            estimated_instance_warmup=estimated_instance_warmup,
            id=id,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            policy_type=policy_type,
            predictive_scaling_configuration=predictive_scaling_configuration,
            scaling_adjustment=scaling_adjustment,
            step_adjustment=step_adjustment,
            target_tracking_configuration=target_tracking_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPredictiveScalingConfiguration")
    def put_predictive_scaling_configuration(
        self,
        *,
        metric_specification: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification", typing.Dict[builtins.str, typing.Any]],
        max_capacity_breach_behavior: typing.Optional[builtins.str] = None,
        max_capacity_buffer: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        scheduling_buffer_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_specification: metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_specification AutoscalingPolicy#metric_specification}
        :param max_capacity_breach_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_breach_behavior AutoscalingPolicy#max_capacity_breach_behavior}.
        :param max_capacity_buffer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_buffer AutoscalingPolicy#max_capacity_buffer}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#mode AutoscalingPolicy#mode}.
        :param scheduling_buffer_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scheduling_buffer_time AutoscalingPolicy#scheduling_buffer_time}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfiguration(
            metric_specification=metric_specification,
            max_capacity_breach_behavior=max_capacity_breach_behavior,
            max_capacity_buffer=max_capacity_buffer,
            mode=mode,
            scheduling_buffer_time=scheduling_buffer_time,
        )

        return typing.cast(None, jsii.invoke(self, "putPredictiveScalingConfiguration", [value]))

    @jsii.member(jsii_name="putStepAdjustment")
    def put_step_adjustment(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyStepAdjustment", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0cd4adbd01618f7081b952add866eb4439359e77aff92c88ec663c541e7b1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStepAdjustment", [value]))

    @jsii.member(jsii_name="putTargetTrackingConfiguration")
    def put_target_tracking_configuration(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_metric_specification AutoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#disable_scale_in AutoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_specification AutoscalingPolicy#predefined_metric_specification}
        '''
        value = AutoscalingPolicyTargetTrackingConfiguration(
            target_value=target_value,
            customized_metric_specification=customized_metric_specification,
            disable_scale_in=disable_scale_in,
            predefined_metric_specification=predefined_metric_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetTrackingConfiguration", [value]))

    @jsii.member(jsii_name="resetAdjustmentType")
    def reset_adjustment_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustmentType", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEstimatedInstanceWarmup")
    def reset_estimated_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEstimatedInstanceWarmup", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetricAggregationType")
    def reset_metric_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricAggregationType", []))

    @jsii.member(jsii_name="resetMinAdjustmentMagnitude")
    def reset_min_adjustment_magnitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinAdjustmentMagnitude", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @jsii.member(jsii_name="resetPredictiveScalingConfiguration")
    def reset_predictive_scaling_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredictiveScalingConfiguration", []))

    @jsii.member(jsii_name="resetScalingAdjustment")
    def reset_scaling_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingAdjustment", []))

    @jsii.member(jsii_name="resetStepAdjustment")
    def reset_step_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepAdjustment", []))

    @jsii.member(jsii_name="resetTargetTrackingConfiguration")
    def reset_target_tracking_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTrackingConfiguration", []))

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
    @jsii.member(jsii_name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationOutputReference", jsii.get(self, "predictiveScalingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustment")
    def step_adjustment(self) -> "AutoscalingPolicyStepAdjustmentList":
        return typing.cast("AutoscalingPolicyStepAdjustmentList", jsii.get(self, "stepAdjustment"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingConfiguration")
    def target_tracking_configuration(
        self,
    ) -> "AutoscalingPolicyTargetTrackingConfigurationOutputReference":
        return typing.cast("AutoscalingPolicyTargetTrackingConfigurationOutputReference", jsii.get(self, "targetTrackingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentTypeInput")
    def adjustment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupNameInput")
    def autoscaling_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="estimatedInstanceWarmupInput")
    def estimated_instance_warmup_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "estimatedInstanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metricAggregationTypeInput")
    def metric_aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricAggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitudeInput")
    def min_adjustment_magnitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minAdjustmentMagnitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="predictiveScalingConfigurationInput")
    def predictive_scaling_configuration_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"], jsii.get(self, "predictiveScalingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustmentInput")
    def scaling_adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scalingAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustmentInput")
    def step_adjustment_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]], jsii.get(self, "stepAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingConfigurationInput")
    def target_tracking_configuration_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"]:
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"], jsii.get(self, "targetTrackingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentType")
    def adjustment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustmentType"))

    @adjustment_type.setter
    def adjustment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f29eeb343e5e6fc94f79425583542067ccb9a824ea3755e87e9d5f78011a104)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustmentType", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupName")
    def autoscaling_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingGroupName"))

    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c8f9aae878aca43beaea830f1de022cfe88f2cdc10b6137798efcd55a26e22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0578eb8319f8ca93cc3d10e7c76928cb438109c5ddbbc47a3593e443bc3954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__565590b9a616cae0c410d4f1adac35ec234e7deacaf6d3075b35fdab10f0d95e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "estimatedInstanceWarmup"))

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2836594ed8440e910cdfe83edcf0c2cfa6137fbf2bcb763829256cab30a52845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "estimatedInstanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0c569c0aab34d5dcc1ab644c0534d5bca61774ea512621670bc95037acd2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metricAggregationType")
    def metric_aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricAggregationType"))

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc80ce120aa0d7483319ea0652ff260961fdc8bbd830bfb36c84a33fcc83a60a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricAggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minAdjustmentMagnitude"))

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c11c2583c0a76c21c7ad33ad9592fa45e83bb05ac714d002704536a3a26bcfc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minAdjustmentMagnitude", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6fa356d09a66b343614ecc525b596ea256389017d2fd374d78c4163b025f789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64a7a096d50283b29a5f59747825d3861121f0cccf088f344f5ad7d24f5a0666)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingAdjustment"))

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f42047491b6c5bea67497729bd4c35bf5c1bac722bec3d4b633c8e0b98d575c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingAdjustment", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "autoscaling_group_name": "autoscalingGroupName",
        "name": "name",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "enabled": "enabled",
        "estimated_instance_warmup": "estimatedInstanceWarmup",
        "id": "id",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "policy_type": "policyType",
        "predictive_scaling_configuration": "predictiveScalingConfiguration",
        "scaling_adjustment": "scalingAdjustment",
        "step_adjustment": "stepAdjustment",
        "target_tracking_configuration": "targetTrackingConfiguration",
    },
)
class AutoscalingPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        autoscaling_group_name: builtins.str,
        name: builtins.str,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_type: typing.Optional[builtins.str] = None,
        predictive_scaling_configuration: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        scaling_adjustment: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyStepAdjustment", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_tracking_configuration: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param autoscaling_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#autoscaling_group_name AutoscalingPolicy#autoscaling_group_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#adjustment_type AutoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#cooldown AutoscalingPolicy#cooldown}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#enabled AutoscalingPolicy#enabled}.
        :param estimated_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#estimated_instance_warmup AutoscalingPolicy#estimated_instance_warmup}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_aggregation_type AutoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#min_adjustment_magnitude AutoscalingPolicy#min_adjustment_magnitude}.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#policy_type AutoscalingPolicy#policy_type}.
        :param predictive_scaling_configuration: predictive_scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predictive_scaling_configuration AutoscalingPolicy#predictive_scaling_configuration}
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#step_adjustment AutoscalingPolicy#step_adjustment}
        :param target_tracking_configuration: target_tracking_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_tracking_configuration AutoscalingPolicy#target_tracking_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(predictive_scaling_configuration, dict):
            predictive_scaling_configuration = AutoscalingPolicyPredictiveScalingConfiguration(**predictive_scaling_configuration)
        if isinstance(target_tracking_configuration, dict):
            target_tracking_configuration = AutoscalingPolicyTargetTrackingConfiguration(**target_tracking_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a9ea1321b9a0f4c8fe0104c6b04d2f83d184e0e74c7a42f259e0db67fbd4bdf)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument autoscaling_group_name", value=autoscaling_group_name, expected_type=type_hints["autoscaling_group_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument estimated_instance_warmup", value=estimated_instance_warmup, expected_type=type_hints["estimated_instance_warmup"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument predictive_scaling_configuration", value=predictive_scaling_configuration, expected_type=type_hints["predictive_scaling_configuration"])
            check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
            check_type(argname="argument step_adjustment", value=step_adjustment, expected_type=type_hints["step_adjustment"])
            check_type(argname="argument target_tracking_configuration", value=target_tracking_configuration, expected_type=type_hints["target_tracking_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "autoscaling_group_name": autoscaling_group_name,
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
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if enabled is not None:
            self._values["enabled"] = enabled
        if estimated_instance_warmup is not None:
            self._values["estimated_instance_warmup"] = estimated_instance_warmup
        if id is not None:
            self._values["id"] = id
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if policy_type is not None:
            self._values["policy_type"] = policy_type
        if predictive_scaling_configuration is not None:
            self._values["predictive_scaling_configuration"] = predictive_scaling_configuration
        if scaling_adjustment is not None:
            self._values["scaling_adjustment"] = scaling_adjustment
        if step_adjustment is not None:
            self._values["step_adjustment"] = step_adjustment
        if target_tracking_configuration is not None:
            self._values["target_tracking_configuration"] = target_tracking_configuration

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
    def autoscaling_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#autoscaling_group_name AutoscalingPolicy#autoscaling_group_name}.'''
        result = self._values.get("autoscaling_group_name")
        assert result is not None, "Required property 'autoscaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#adjustment_type AutoscalingPolicy#adjustment_type}.'''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#cooldown AutoscalingPolicy#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#enabled AutoscalingPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#estimated_instance_warmup AutoscalingPolicy#estimated_instance_warmup}.'''
        result = self._values.get("estimated_instance_warmup")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_aggregation_type AutoscalingPolicy#metric_aggregation_type}.'''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#min_adjustment_magnitude AutoscalingPolicy#min_adjustment_magnitude}.'''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#policy_type AutoscalingPolicy#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def predictive_scaling_configuration(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"]:
        '''predictive_scaling_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predictive_scaling_configuration AutoscalingPolicy#predictive_scaling_configuration}
        '''
        result = self._values.get("predictive_scaling_configuration")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfiguration"], result)

    @builtins.property
    def scaling_adjustment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.'''
        result = self._values.get("scaling_adjustment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_adjustment(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]]:
        '''step_adjustment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#step_adjustment AutoscalingPolicy#step_adjustment}
        '''
        result = self._values.get("step_adjustment")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyStepAdjustment"]]], result)

    @builtins.property
    def target_tracking_configuration(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"]:
        '''target_tracking_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_tracking_configuration AutoscalingPolicy#target_tracking_configuration}
        '''
        result = self._values.get("target_tracking_configuration")
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "metric_specification": "metricSpecification",
        "max_capacity_breach_behavior": "maxCapacityBreachBehavior",
        "max_capacity_buffer": "maxCapacityBuffer",
        "mode": "mode",
        "scheduling_buffer_time": "schedulingBufferTime",
    },
)
class AutoscalingPolicyPredictiveScalingConfiguration:
    def __init__(
        self,
        *,
        metric_specification: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification", typing.Dict[builtins.str, typing.Any]],
        max_capacity_breach_behavior: typing.Optional[builtins.str] = None,
        max_capacity_buffer: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        scheduling_buffer_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_specification: metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_specification AutoscalingPolicy#metric_specification}
        :param max_capacity_breach_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_breach_behavior AutoscalingPolicy#max_capacity_breach_behavior}.
        :param max_capacity_buffer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_buffer AutoscalingPolicy#max_capacity_buffer}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#mode AutoscalingPolicy#mode}.
        :param scheduling_buffer_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scheduling_buffer_time AutoscalingPolicy#scheduling_buffer_time}.
        '''
        if isinstance(metric_specification, dict):
            metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification(**metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4daa98ddb68bfbb790a88d8c0b7233896163559b2c2f95e4849d102a8bdfaeca)
            check_type(argname="argument metric_specification", value=metric_specification, expected_type=type_hints["metric_specification"])
            check_type(argname="argument max_capacity_breach_behavior", value=max_capacity_breach_behavior, expected_type=type_hints["max_capacity_breach_behavior"])
            check_type(argname="argument max_capacity_buffer", value=max_capacity_buffer, expected_type=type_hints["max_capacity_buffer"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument scheduling_buffer_time", value=scheduling_buffer_time, expected_type=type_hints["scheduling_buffer_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_specification": metric_specification,
        }
        if max_capacity_breach_behavior is not None:
            self._values["max_capacity_breach_behavior"] = max_capacity_breach_behavior
        if max_capacity_buffer is not None:
            self._values["max_capacity_buffer"] = max_capacity_buffer
        if mode is not None:
            self._values["mode"] = mode
        if scheduling_buffer_time is not None:
            self._values["scheduling_buffer_time"] = scheduling_buffer_time

    @builtins.property
    def metric_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification":
        '''metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_specification AutoscalingPolicy#metric_specification}
        '''
        result = self._values.get("metric_specification")
        assert result is not None, "Required property 'metric_specification' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification", result)

    @builtins.property
    def max_capacity_breach_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_breach_behavior AutoscalingPolicy#max_capacity_breach_behavior}.'''
        result = self._values.get("max_capacity_breach_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity_buffer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#max_capacity_buffer AutoscalingPolicy#max_capacity_buffer}.'''
        result = self._values.get("max_capacity_buffer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#mode AutoscalingPolicy#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_buffer_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scheduling_buffer_time AutoscalingPolicy#scheduling_buffer_time}.'''
        result = self._values.get("scheduling_buffer_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_capacity_metric_specification": "customizedCapacityMetricSpecification",
        "customized_load_metric_specification": "customizedLoadMetricSpecification",
        "customized_scaling_metric_specification": "customizedScalingMetricSpecification",
        "predefined_load_metric_specification": "predefinedLoadMetricSpecification",
        "predefined_metric_pair_specification": "predefinedMetricPairSpecification",
        "predefined_scaling_metric_specification": "predefinedScalingMetricSpecification",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_capacity_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        customized_load_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        customized_scaling_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        predefined_load_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        predefined_metric_pair_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        predefined_scaling_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_capacity_metric_specification: customized_capacity_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_capacity_metric_specification AutoscalingPolicy#customized_capacity_metric_specification}
        :param customized_load_metric_specification: customized_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_load_metric_specification AutoscalingPolicy#customized_load_metric_specification}
        :param customized_scaling_metric_specification: customized_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_scaling_metric_specification AutoscalingPolicy#customized_scaling_metric_specification}
        :param predefined_load_metric_specification: predefined_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_load_metric_specification AutoscalingPolicy#predefined_load_metric_specification}
        :param predefined_metric_pair_specification: predefined_metric_pair_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_pair_specification AutoscalingPolicy#predefined_metric_pair_specification}
        :param predefined_scaling_metric_specification: predefined_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_scaling_metric_specification AutoscalingPolicy#predefined_scaling_metric_specification}
        '''
        if isinstance(customized_capacity_metric_specification, dict):
            customized_capacity_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(**customized_capacity_metric_specification)
        if isinstance(customized_load_metric_specification, dict):
            customized_load_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(**customized_load_metric_specification)
        if isinstance(customized_scaling_metric_specification, dict):
            customized_scaling_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(**customized_scaling_metric_specification)
        if isinstance(predefined_load_metric_specification, dict):
            predefined_load_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(**predefined_load_metric_specification)
        if isinstance(predefined_metric_pair_specification, dict):
            predefined_metric_pair_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(**predefined_metric_pair_specification)
        if isinstance(predefined_scaling_metric_specification, dict):
            predefined_scaling_metric_specification = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(**predefined_scaling_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9291fd8e46eba9da50ee0b2123b030afadd776c17e265feefb2ffa4c9af94e95)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_capacity_metric_specification", value=customized_capacity_metric_specification, expected_type=type_hints["customized_capacity_metric_specification"])
            check_type(argname="argument customized_load_metric_specification", value=customized_load_metric_specification, expected_type=type_hints["customized_load_metric_specification"])
            check_type(argname="argument customized_scaling_metric_specification", value=customized_scaling_metric_specification, expected_type=type_hints["customized_scaling_metric_specification"])
            check_type(argname="argument predefined_load_metric_specification", value=predefined_load_metric_specification, expected_type=type_hints["predefined_load_metric_specification"])
            check_type(argname="argument predefined_metric_pair_specification", value=predefined_metric_pair_specification, expected_type=type_hints["predefined_metric_pair_specification"])
            check_type(argname="argument predefined_scaling_metric_specification", value=predefined_scaling_metric_specification, expected_type=type_hints["predefined_scaling_metric_specification"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_capacity_metric_specification is not None:
            self._values["customized_capacity_metric_specification"] = customized_capacity_metric_specification
        if customized_load_metric_specification is not None:
            self._values["customized_load_metric_specification"] = customized_load_metric_specification
        if customized_scaling_metric_specification is not None:
            self._values["customized_scaling_metric_specification"] = customized_scaling_metric_specification
        if predefined_load_metric_specification is not None:
            self._values["predefined_load_metric_specification"] = predefined_load_metric_specification
        if predefined_metric_pair_specification is not None:
            self._values["predefined_metric_pair_specification"] = predefined_metric_pair_specification
        if predefined_scaling_metric_specification is not None:
            self._values["predefined_scaling_metric_specification"] = predefined_scaling_metric_specification

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_capacity_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification"]:
        '''customized_capacity_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_capacity_metric_specification AutoscalingPolicy#customized_capacity_metric_specification}
        '''
        result = self._values.get("customized_capacity_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification"], result)

    @builtins.property
    def customized_load_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification"]:
        '''customized_load_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_load_metric_specification AutoscalingPolicy#customized_load_metric_specification}
        '''
        result = self._values.get("customized_load_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification"], result)

    @builtins.property
    def customized_scaling_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification"]:
        '''customized_scaling_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_scaling_metric_specification AutoscalingPolicy#customized_scaling_metric_specification}
        '''
        result = self._values.get("customized_scaling_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification"], result)

    @builtins.property
    def predefined_load_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"]:
        '''predefined_load_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_load_metric_specification AutoscalingPolicy#predefined_load_metric_specification}
        '''
        result = self._values.get("predefined_load_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"], result)

    @builtins.property
    def predefined_metric_pair_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"]:
        '''predefined_metric_pair_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_pair_specification AutoscalingPolicy#predefined_metric_pair_specification}
        '''
        result = self._values.get("predefined_metric_pair_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"], result)

    @builtins.property
    def predefined_scaling_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"]:
        '''predefined_scaling_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_scaling_metric_specification AutoscalingPolicy#predefined_scaling_metric_specification}
        '''
        result = self._values.get("predefined_scaling_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={"metric_data_queries": "metricDataQueries"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification:
    def __init__(
        self,
        *,
        metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59d545fa55e3e4f5e2a5b62eac769f31b4d3be255ebfdc61943d88845c56c3e1)
            check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_data_queries": metric_data_queries,
        }

    @builtins.property
    def metric_data_queries(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries"]]:
        '''metric_data_queries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        result = self._values.get("metric_data_queries")
        assert result is not None, "Required property 'metric_data_queries' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "expression": "expression",
        "label": "label",
        "metric_stat": "metricStat",
        "return_data": "returnData",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries:
    def __init__(
        self,
        *,
        id: builtins.str,
        expression: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        metric_stat: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat", typing.Dict[builtins.str, typing.Any]]] = None,
        return_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.
        :param metric_stat: metric_stat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        :param return_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.
        '''
        if isinstance(metric_stat, dict):
            metric_stat = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8137a330670fab2a66d130c4c9c8c5962ea3e0752748c1e0daf0f0446f3a213c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if expression is not None:
            self._values["expression"] = expression
        if label is not None:
            self._values["label"] = label
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if return_data is not None:
            self._values["return_data"] = return_data

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_stat(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat"]:
        '''metric_stat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat"], result)

    @builtins.property
    def return_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.'''
        result = self._values.get("return_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e87e3f3e9cc8a931812bf8bbfe6731676e31155986af24bc6f92c83a4886cc9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__836bc7dba5788164b03370ce2db1cb0516906d2721573373917f253f6f28aece)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61291fee044a1a68e1a1a489dd5e930c04655bccfeae1413caac57480fb45c51)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff81127e21b951886073dccff35fdf10b2b56e5645e14aacd960bd2ca45f8e1e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dab42ae74b34d5ed91ad6ee3d950cfbdc52f3bfa89e812e413ae6c93b05809ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4241ca68ab9759b2db12832622a0f18f0108e5201016d4c560fb8bc77d4b0629)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat:
    def __init__(
        self,
        *,
        metric: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric", typing.Dict[builtins.str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if isinstance(metric, dict):
            metric = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric(**metric)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb48e42115ac870e0958edb23d9ad6688dee8a439cecd30d2cfd25106970c231)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
            "stat": stat,
        }
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric", result)

    @builtins.property
    def stat(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.'''
        result = self._values.get("stat")
        assert result is not None, "Required property 'stat' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "dimensions": "dimensions",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1553f1b141cb646a353642e2cfe7a0c308c142a18f09a65cdc232aab894bd6)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e6a5a1e373704b2e8b0c8044574b0b312e8ff7e91b3df5702845eb32f71f66a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfecba9f1caca0b5b087e6c535beb2466d77c967ff02cddf4cc333e9e2f3991d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da8e2377c91303af1b33c394cde4d9283827fa14304b48224477be701ed81b6a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbab6020d9942843e20ef24c21e178bad8ca97812e75f36d448e15b44bbe0bf9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af59eb1e1bc626661166695d025fd9e53032e54b7b04837ac0d6a2fd5bc2c9e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33be1380736cc4891fae8d9deede3257237f29cc69b2fef6a8eed921160e8490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e9f930e7b80643ec89d47c16929655d460edf7b7695aee1f52cf934a1b5f89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__51a1f09395685eff59e2c8a8f64cd190b4e74aebd456b9020d9aaf99142409d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa544191117f9dad2a10a662c6020df3f6d35cef04f03d62a2030b360096c5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__694fb99477a0ff0af51a0bc6db389d29eb99be8a498a1489c49c5270e64ed251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb76ccbb1f7fc477e4a9b2a83cdd1f2f401a9d5ffa244c700b9a3a5bfb46ea27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a25f377fa5178cb5ce0c159ef7e7e6de34ba2db8d74486540ed6bcaab4fe5ff5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6e342ea68ce79c7bd7fbda34147d255cead364ccdc621248c4b8d2e2a86d36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8035169c4ba89bdffe586774208a650f3c6de70d9a93d39cef2fe75292d2f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ee6c6fd2e3936759728e8f609d2ff51b7c8e11a69ad99824eb4b21bd178795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a12ef1f90ec7f62a082892d1bdd8f1135068f2a4c2640d68fc03db2b0ec4f9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__93d9fa04cd093bd81e24bbb4062b67ea4871a5c36bf5ad3966a8eb09e259043d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric(
            metric_name=metric_name, namespace=namespace, dimensions=dimensions
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="statInput")
    def stat_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9ee7fa74976e499c57cf52fd7324bdb7dde591eab109b4dbed9320999d4054c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2bb591d87637a1e00ae38745a57ccf19aba51c6d993a721031ce1f93feac92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64497c134114eb3f8e2c791c3ecae94e152c49fb93926b1c88a487fdeeacf502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e01a4222f3caea2efd9e82f94ebcf6cba9bdfcab9f5d3e7fa761c27f8452970e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMetricStat")
    def put_metric_stat(
        self,
        *,
        metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[builtins.str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat(
            metric=metric, stat=stat, unit=unit
        )

        return typing.cast(None, jsii.invoke(self, "putMetricStat", [value]))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetMetricStat")
    def reset_metric_stat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricStat", []))

    @jsii.member(jsii_name="resetReturnData")
    def reset_return_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnData", []))

    @builtins.property
    @jsii.member(jsii_name="metricStat")
    def metric_stat(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference, jsii.get(self, "metricStat"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricStatInput")
    def metric_stat_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "metricStatInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataInput")
    def return_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnDataInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd1efa6151e073c9e3ca134ac86450b49fa8c0c87255af80b2deb9ce4983111e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__507c8619eeea33727eaeec973ff4360f4d55144e59649a10460cfd9807faac89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c17d3d5cf28f44b134908c1fda239361789f17f2544d8b1f588edc79ecb9e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="returnData")
    def return_data(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "returnData"))

    @return_data.setter
    def return_data(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0af0a9999c45cee379f86960110d5bf9b9693f602970ed58ef3cd1a484fa2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b0ad1a435cf033dee6e4a410deec3d9b817df55038424457c724c95db414102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0f026cea54ff886476119ad13fc486496e68b57a83f39bf5f2782beddded498)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDataQueries")
    def put_metric_data_queries(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50b116ea71fb92b6b30d3c161ed5a5ef44b92c27f6fb844fa71f745ffd94bcde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDataQueries", [value]))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList, jsii.get(self, "metricDataQueries"))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueriesInput")
    def metric_data_queries_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]], jsii.get(self, "metricDataQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cc21d7199167dd6c8e3fa8909010dd8e987447f0ab6305d8886e37228bba5aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={"metric_data_queries": "metricDataQueries"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification:
    def __init__(
        self,
        *,
        metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef97a4f5752e5fa9b69b9ecc2a8fc9a472af97531903847d2ca134d6a2d56f03)
            check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_data_queries": metric_data_queries,
        }

    @builtins.property
    def metric_data_queries(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries"]]:
        '''metric_data_queries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        result = self._values.get("metric_data_queries")
        assert result is not None, "Required property 'metric_data_queries' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "expression": "expression",
        "label": "label",
        "metric_stat": "metricStat",
        "return_data": "returnData",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries:
    def __init__(
        self,
        *,
        id: builtins.str,
        expression: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        metric_stat: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat", typing.Dict[builtins.str, typing.Any]]] = None,
        return_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.
        :param metric_stat: metric_stat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        :param return_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.
        '''
        if isinstance(metric_stat, dict):
            metric_stat = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e9d2bd6300db79eeb092f68850eadcb5fa65f828f8fe00cb4743bda81c4561a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if expression is not None:
            self._values["expression"] = expression
        if label is not None:
            self._values["label"] = label
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if return_data is not None:
            self._values["return_data"] = return_data

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_stat(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat"]:
        '''metric_stat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat"], result)

    @builtins.property
    def return_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.'''
        result = self._values.get("return_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fac17fca53c8728ff9d7a58278825ac611082039b6e1a90f9c20bf9432cdd06b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d65a0c2bc29fed4b7fdabe672a9b98f8a66e942e50f84725d86859757cc1a519)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9143e8a84a33d8c9477c27ce3b4cb15abd9fa719442ebfb9ea84ee4fc907a357)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a41fee23bc5aac64371bece1b6d7a0c62aba6fd7a468a25457bee685fdb8e50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4322a8f25dcf88470b5c03cb527196483b807b7a1c049ea899976fb479767c76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1085e6ee9700adda28fd5c13272db6d539268005ce9f12fd4f30284a8bff8f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat:
    def __init__(
        self,
        *,
        metric: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric", typing.Dict[builtins.str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if isinstance(metric, dict):
            metric = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric(**metric)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64252d35724fccebef5d0be0b902f3599e76be6ee7e2e75ef120642ff2b413dc)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
            "stat": stat,
        }
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric", result)

    @builtins.property
    def stat(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.'''
        result = self._values.get("stat")
        assert result is not None, "Required property 'stat' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "dimensions": "dimensions",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6e7d5b86df66fb145e73d88bd25f306739625353bc45c56d903cebb16548b9)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__103b2057d6ffc6484d5c4be3fdb2bb805c2ec4033580375e7ab9867148bdfe6c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a414302a77facc3b59b981872ec9f113b78cff23fc61c7adcd342c74568b358)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06d52eb8dc7f987eaac87529cede5ba423ac19c23a4e34b0d6799df097e2778f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efa20e7415d57744fa01d6c718cbe057fe239683943ed9f7fcbfdca02d9ca0e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7aa990342f424cc5f04bf5eb744634c0eadd9bc8679c1b11c96768e0ccd393f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__59366954adafb48d5ef89d16d1b6ebb427a8c6a736f96ee884e53360bf2cb097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4bfcf681d6d5cab9613b28cb891db01f8ffe60bc8d9ebf257fc4e711da6dd9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d3d36dcd5f8308a7e048a45b28fd7ab35fc59cd966fa020cd415277ed4cd77d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b021eafbab75eb3cf74e5f8a09602654edf7dcba955c58d397c3613658d7993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a5c2ff9c199d5ec2ba6dccab9f685165056d4d87bc7460c6c88802ac19ee22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09972a44b39bd616c2da74cfc9e76f57edb9013806ab6730755cc897f34c17cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__babf6bf130e939a7209ca880c1bbd8626836bee504621fb94ed6f4e28ac34232)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__136b62b741544241dd54e2984a72fd451b995b9267b51ab1fa5b7c324314a6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d56949429844362eb41fbb80c429ebb94244fb8331ea11fe742e5d6a77781fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d965d1477be91c80d8d0a73f946b87431af34f020a35be597e4d1b689ec4c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf3269a0cc5838f4347a3dbf92fe0e0d404dbd76983000a5828506d34f54a76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7378b7aeb6d225145209e2e3d4e20851753713a4920889348197fdb4e873f40b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric(
            metric_name=metric_name, namespace=namespace, dimensions=dimensions
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="statInput")
    def stat_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7280ff3f1711e7cfd3c915b026549ec7b90c9224f4c7e1d3666812f559e0b29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d45e077afddf2a160ce01bcce8659df757081477c10b6267e5d762c38af666d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785f0cf452a63c07a38fcd5c5fe15ad3c081dacc8ffa8ad383c39cabf6c1eaa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffc60fe2bd9fb5c15d1c1b748475eb50dfdec4d1f72737d5aef27615587400cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMetricStat")
    def put_metric_stat(
        self,
        *,
        metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[builtins.str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat(
            metric=metric, stat=stat, unit=unit
        )

        return typing.cast(None, jsii.invoke(self, "putMetricStat", [value]))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetMetricStat")
    def reset_metric_stat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricStat", []))

    @jsii.member(jsii_name="resetReturnData")
    def reset_return_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnData", []))

    @builtins.property
    @jsii.member(jsii_name="metricStat")
    def metric_stat(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference, jsii.get(self, "metricStat"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricStatInput")
    def metric_stat_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "metricStatInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataInput")
    def return_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnDataInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__232c1b07d1bb5a8db94a4d0eac200db8b05327523bda171a51fc87f96235779f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f73ec7a7701c9b69ab11d19447023223a167883a8461f8feaba884ede2dea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043ff655469d6a7e75e24ecb18ff9b404bb20690172df654fc1bd48bdb415d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="returnData")
    def return_data(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "returnData"))

    @return_data.setter
    def return_data(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d860073aa5e22a705a44ff5eafc186e996873544ca7265935fc16293872bd4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63563319ec3caddfb5657c16986b15dc733e4ee84e8a7ffec28a82414226bbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aba65297025445104042bde1deeb1a968685e198acb7691c392f8b391543d175)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDataQueries")
    def put_metric_data_queries(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796675a624900954836ff5a5b51a444b914b5aaf48ed050d6196d8422e6fa3c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDataQueries", [value]))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList, jsii.get(self, "metricDataQueries"))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueriesInput")
    def metric_data_queries_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]], jsii.get(self, "metricDataQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd795f40e97623d2e8c0658bff3d64172719d536a205eb0945cfcd75058302c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={"metric_data_queries": "metricDataQueries"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification:
    def __init__(
        self,
        *,
        metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff80ceea99e2b2debea6ec4323d58c43b810ec00b50f1326dab0e7a151a039d)
            check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_data_queries": metric_data_queries,
        }

    @builtins.property
    def metric_data_queries(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries"]]:
        '''metric_data_queries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        result = self._values.get("metric_data_queries")
        assert result is not None, "Required property 'metric_data_queries' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "expression": "expression",
        "label": "label",
        "metric_stat": "metricStat",
        "return_data": "returnData",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries:
    def __init__(
        self,
        *,
        id: builtins.str,
        expression: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        metric_stat: typing.Optional[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat", typing.Dict[builtins.str, typing.Any]]] = None,
        return_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.
        :param metric_stat: metric_stat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        :param return_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.
        '''
        if isinstance(metric_stat, dict):
            metric_stat = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d0729194123ceb7c836afcc32056e66f34907ec93c15e7abacd14f03f2f041)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if expression is not None:
            self._values["expression"] = expression
        if label is not None:
            self._values["label"] = label
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if return_data is not None:
            self._values["return_data"] = return_data

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#id AutoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#expression AutoscalingPolicy#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#label AutoscalingPolicy#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_stat(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat"]:
        '''metric_stat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_stat AutoscalingPolicy#metric_stat}
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat"], result)

    @builtins.property
    def return_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#return_data AutoscalingPolicy#return_data}.'''
        result = self._values.get("return_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e00db678cd1f25a9479e281b3a8783eb9739678584f54219faf2b3d3cfae1237)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c03ccd0e569311b0f0f58eb2e61799efa23ce92334e2dfb961a86a91a1c2c9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e4c26449383f65f56938c0d634ff388c080e763b98e5035fbb1de97206ba51)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07d40ce2a614308e1e74e68d40692296606166da4c4bf58c87ddd96b2ada84fc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f882fa72886216cec45d64ae7a5145a499ebb2dbb993972c7bdee040875e94ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca509078559bc12be927aa431062d1bd4f0a4abd100e698f48d1faa76f80b912)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat:
    def __init__(
        self,
        *,
        metric: typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric", typing.Dict[builtins.str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if isinstance(metric, dict):
            metric = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric(**metric)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2353053dadad55b11db1326eba9b272ad0f141ce1cf8583604e1d81a3ad353d2)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
            "stat": stat,
        }
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric", result)

    @builtins.property
    def stat(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.'''
        result = self._values.get("stat")
        assert result is not None, "Required property 'stat' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "dimensions": "dimensions",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a3fbb35361bf60541f6e71168f1b8f178519ac98c8c6d4f9f0fe66b7abaec9f)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966b9fdc10d764d3ff2a27acf786eeb27a682e1bbf4076e61b0d9f07c3b3dd62)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b3cdd1355ca9f3c289db8574bab1b51ea606931675f30a83113c8d43047f292)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076c368efdf770d506d9f90c70caa19e9888b7535eba05cf4fbee8acd3a1eb9b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f11b1473dfa78280bbcbc7e6e52860669ac8ce7d5f540dbfb277a7775835fc28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__75e22d3182604821442d1c9c4f98149b9eedd5443f41f7bc5419ea648d113791)
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
            type_hints = typing.get_type_hints(_typecheckingstub__343e17a8cddca7103a3853638e92661d7f499a05bfe6385b84ad318009f1490c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5913288f81228fbbaea25878b13ec7db46bd224546608d573bdff369286b8d17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a94852910c493c35b9f0a5cd9ddbdc24c99e17213dd273d31faf32fa2459a6c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea7352f1c1c0979dd2b2f426d74fe4c8c9146ceebf03b6deaaaa134568beb356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d40c595d8820cfa246e4a3eab665c453e4505a778e8d32ccf8617aeac3f0d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__129cc1cf25c356765b51d6e4b8dbde852a42606eabf0df8fc6228d06bb89d31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc083196cb668b93b0d8d418dc5c1f2a9453578f8fe84695e95c6498bc586c0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910fb863721d34993c1b320474a24e2d83b3472fed9b925a8886cace1e11b469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8f84f8b2b5cfbce1b9b67f096458feab9a9fe5a931b2e231f56c3e1e5f063c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3c2bc6b438be6ad42b2e929d037340d68154e9eaca7103701732de209f8b79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38275b0e1cf5624a69e2ff80937ec099f6f127b5c81598bf4f897daef913a236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9620f3f5e9c7a3c4124ff2ed23f5dec622612f437dece262effd21bcdd2e728a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#dimensions AutoscalingPolicy#dimensions}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric(
            metric_name=metric_name, namespace=namespace, dimensions=dimensions
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="statInput")
    def stat_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__029a410326e09b10c537b032b2ac00319eec5af474f8e7a0fff945b92da3f776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d00ded0096a230f917895fb2aa2cf6e440b683cdf48cb444658c5c1cd39639ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__512ebeec4f07baf4e381884fbfd3cd20ce9b79d19385af0750a61804517254b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__399aa130ce3f06612d033f703c5b9c0cf8a433b7009ac85c58d9e0c8115e49ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMetricStat")
    def put_metric_stat(
        self,
        *,
        metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[builtins.str, typing.Any]],
        stat: builtins.str,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric AutoscalingPolicy#metric}
        :param stat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#stat AutoscalingPolicy#stat}.
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat(
            metric=metric, stat=stat, unit=unit
        )

        return typing.cast(None, jsii.invoke(self, "putMetricStat", [value]))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetMetricStat")
    def reset_metric_stat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricStat", []))

    @jsii.member(jsii_name="resetReturnData")
    def reset_return_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnData", []))

    @builtins.property
    @jsii.member(jsii_name="metricStat")
    def metric_stat(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference, jsii.get(self, "metricStat"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricStatInput")
    def metric_stat_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat], jsii.get(self, "metricStatInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataInput")
    def return_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "returnDataInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab32315e44d946fb0f0d2fc2b49e3184b1ecc51175f60165c70960dcb21cbdaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b777e61c8756eb55a8af5e1273eafd986446a18c34c213406329157acdbb889)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19959b3e6d888fd1170b39953ae3b75f0f08b3b3cedeb6f15487bc81cd0914b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="returnData")
    def return_data(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "returnData"))

    @return_data.setter
    def return_data(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f62cddfb2178c15d1cf803a924f402a4ceb7a49d14595dc73455beefaacc12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__525ce3b4032dac8eba4cd4241edebe1b8e8c5b02053bb3eee643d2810a1282b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccf2f6a8b11696251ebd9ea75d0505c504e37c450ce3142c31a6516810b6aa97)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDataQueries")
    def put_metric_data_queries(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf5dba7fad0cb1af8bd90d347c6c0372c468de7da3b56569fae37d1c208b0361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDataQueries", [value]))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList, jsii.get(self, "metricDataQueries"))

    @builtins.property
    @jsii.member(jsii_name="metricDataQueriesInput")
    def metric_data_queries_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]], jsii.get(self, "metricDataQueriesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bc53e86f9f12277932936912fc32ba15ef479ee078c7e92eb5533b3806a59a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5ee72804c747f41ed5c543ea19d91720bd94149e66d792c02de9c6e4bb45d7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomizedCapacityMetricSpecification")
    def put_customized_capacity_metric_specification(
        self,
        *,
        metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(
            metric_data_queries=metric_data_queries
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedCapacityMetricSpecification", [value]))

    @jsii.member(jsii_name="putCustomizedLoadMetricSpecification")
    def put_customized_load_metric_specification(
        self,
        *,
        metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(
            metric_data_queries=metric_data_queries
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedLoadMetricSpecification", [value]))

    @jsii.member(jsii_name="putCustomizedScalingMetricSpecification")
    def put_customized_scaling_metric_specification(
        self,
        *,
        metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param metric_data_queries: metric_data_queries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_data_queries AutoscalingPolicy#metric_data_queries}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(
            metric_data_queries=metric_data_queries
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedScalingMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedLoadMetricSpecification")
    def put_predefined_load_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedLoadMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedMetricPairSpecification")
    def put_predefined_metric_pair_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedMetricPairSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedScalingMetricSpecification")
    def put_predefined_scaling_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedScalingMetricSpecification", [value]))

    @jsii.member(jsii_name="resetCustomizedCapacityMetricSpecification")
    def reset_customized_capacity_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedCapacityMetricSpecification", []))

    @jsii.member(jsii_name="resetCustomizedLoadMetricSpecification")
    def reset_customized_load_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedLoadMetricSpecification", []))

    @jsii.member(jsii_name="resetCustomizedScalingMetricSpecification")
    def reset_customized_scaling_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedScalingMetricSpecification", []))

    @jsii.member(jsii_name="resetPredefinedLoadMetricSpecification")
    def reset_predefined_load_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedLoadMetricSpecification", []))

    @jsii.member(jsii_name="resetPredefinedMetricPairSpecification")
    def reset_predefined_metric_pair_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedMetricPairSpecification", []))

    @jsii.member(jsii_name="resetPredefinedScalingMetricSpecification")
    def reset_predefined_scaling_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedScalingMetricSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="customizedCapacityMetricSpecification")
    def customized_capacity_metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference, jsii.get(self, "customizedCapacityMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference, jsii.get(self, "customizedLoadMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference, jsii.get(self, "customizedScalingMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference", jsii.get(self, "predefinedLoadMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricPairSpecification")
    def predefined_metric_pair_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference", jsii.get(self, "predefinedMetricPairSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference", jsii.get(self, "predefinedScalingMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedCapacityMetricSpecificationInput")
    def customized_capacity_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification], jsii.get(self, "customizedCapacityMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="customizedLoadMetricSpecificationInput")
    def customized_load_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification], jsii.get(self, "customizedLoadMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="customizedScalingMetricSpecificationInput")
    def customized_scaling_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification], jsii.get(self, "customizedScalingMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedLoadMetricSpecificationInput")
    def predefined_load_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification"], jsii.get(self, "predefinedLoadMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricPairSpecificationInput")
    def predefined_metric_pair_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification"], jsii.get(self, "predefinedMetricPairSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedScalingMetricSpecificationInput")
    def predefined_scaling_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification"], jsii.get(self, "predefinedScalingMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValueInput")
    def target_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetValueInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__576fe0387a7d089a02db91edd4123e776655bd7360dd52fcd9d6ec8d2ee5bd19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c285851edacf0ad2ea3f1856063c2bf24fce7820b5d642949e9298e4264ed9fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67567f772d46122a62d7e3bddc67ac64df67d2e4315504435828a3b4b34bcb37)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
            "resource_label": resource_label,
        }

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        assert result is not None, "Required property 'resource_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44e50ea1b2b6ce22f094388a5c11ef51b55378f6f966627bb1bf24ebf6b28b39)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cf7c00be787f140d0724e89ffe0348dced00ff626faf8fe2b961e7396a4bee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e41b6ec1c8522de84d64dfb7424a0cbb51fb51f3e1a3405e74b98d11f63b1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f07d2393ef334b24f1d86474b23c20341ce6835a19ccd101e1c17fe6dd7d6315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad52c84b24e6745994b2af46209470ae75551a185d81b58ae95a12f396ddbe7)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
            "resource_label": resource_label,
        }

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        assert result is not None, "Required property 'resource_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__124eb5b26383ba72dbeff26a4e556bbcd618aeaa307c53158a4e0671a2e8bd17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f59a3343df82f4ca368abf3da2b98acd52cc24e067a467674c3ff47006eb3a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba219afa34c9f0664f722fcd35e58751119404462f67cc6b69f48f8b43b9585d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b6d515923cec8f2ee508d738b9db2fc1b2bedd39f2d20f80fa33aad5e3c689f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: builtins.str,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d62fdb15420670189d4ed5661c7e76fc31e13dd17198dba2c77f22453c29b617)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
            "resource_label": resource_label,
        }

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        assert result is not None, "Required property 'resource_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7a79bd1efe1eff92993d4fa9cd3fb4da8d49625ddfadea36b3eda2cf29a3102)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1912d828e0a69f31f586db14fb1a5fc82847440684afaf4329fd025139afe4d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe68a8097bb2d9717aa39c5915de84d60ba61149dc1f930b824d4c4d34efe52c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77601bfd63c07d45c48d943b07254077b27b0fcd517def23b408a978f3201bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyPredictiveScalingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyPredictiveScalingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c49cb47169cae9d8910ee2315e0b0c2e581d1fcf9435b4f44576aa4fd03103e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricSpecification")
    def put_metric_specification(
        self,
        *,
        target_value: jsii.Number,
        customized_capacity_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        customized_load_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        customized_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        predefined_load_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        predefined_metric_pair_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        predefined_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_capacity_metric_specification: customized_capacity_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_capacity_metric_specification AutoscalingPolicy#customized_capacity_metric_specification}
        :param customized_load_metric_specification: customized_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_load_metric_specification AutoscalingPolicy#customized_load_metric_specification}
        :param customized_scaling_metric_specification: customized_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_scaling_metric_specification AutoscalingPolicy#customized_scaling_metric_specification}
        :param predefined_load_metric_specification: predefined_load_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_load_metric_specification AutoscalingPolicy#predefined_load_metric_specification}
        :param predefined_metric_pair_specification: predefined_metric_pair_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_pair_specification AutoscalingPolicy#predefined_metric_pair_specification}
        :param predefined_scaling_metric_specification: predefined_scaling_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_scaling_metric_specification AutoscalingPolicy#predefined_scaling_metric_specification}
        '''
        value = AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification(
            target_value=target_value,
            customized_capacity_metric_specification=customized_capacity_metric_specification,
            customized_load_metric_specification=customized_load_metric_specification,
            customized_scaling_metric_specification=customized_scaling_metric_specification,
            predefined_load_metric_specification=predefined_load_metric_specification,
            predefined_metric_pair_specification=predefined_metric_pair_specification,
            predefined_scaling_metric_specification=predefined_scaling_metric_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putMetricSpecification", [value]))

    @jsii.member(jsii_name="resetMaxCapacityBreachBehavior")
    def reset_max_capacity_breach_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacityBreachBehavior", []))

    @jsii.member(jsii_name="resetMaxCapacityBuffer")
    def reset_max_capacity_buffer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacityBuffer", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSchedulingBufferTime")
    def reset_scheduling_buffer_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulingBufferTime", []))

    @builtins.property
    @jsii.member(jsii_name="metricSpecification")
    def metric_specification(
        self,
    ) -> AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference, jsii.get(self, "metricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBreachBehaviorInput")
    def max_capacity_breach_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxCapacityBreachBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBufferInput")
    def max_capacity_buffer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxCapacityBufferInput"))

    @builtins.property
    @jsii.member(jsii_name="metricSpecificationInput")
    def metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification], jsii.get(self, "metricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingBufferTimeInput")
    def scheduling_buffer_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingBufferTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBreachBehavior")
    def max_capacity_breach_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacityBreachBehavior"))

    @max_capacity_breach_behavior.setter
    def max_capacity_breach_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619d8aba354f832ab96b0e87cc23e57ad94ee3a67f0364a0c79d69ad8f4166c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacityBreachBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacityBuffer")
    def max_capacity_buffer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxCapacityBuffer"))

    @max_capacity_buffer.setter
    def max_capacity_buffer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71f5596c914b34bb1dd74019e06011fa844f45af4285186b2a712b7533fde19e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacityBuffer", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff1e691b2166594e714befc2f16350cf47948f91fdf4aebbd48c6b9e22d79f9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingBufferTime")
    def scheduling_buffer_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulingBufferTime"))

    @scheduling_buffer_time.setter
    def scheduling_buffer_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4dbdf253a944dc5dc108c42169b6ca4e48ac51f5d2b70a15081c77d0b8b68b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingBufferTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration]:
        return typing.cast(typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001cc877b07f995a37b551c4114bd9325f1a64bb7f63d2bcb1ed6db2f1cad085)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyStepAdjustment",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_adjustment": "scalingAdjustment",
        "metric_interval_lower_bound": "metricIntervalLowerBound",
        "metric_interval_upper_bound": "metricIntervalUpperBound",
    },
)
class AutoscalingPolicyStepAdjustment:
    def __init__(
        self,
        *,
        scaling_adjustment: jsii.Number,
        metric_interval_lower_bound: typing.Optional[builtins.str] = None,
        metric_interval_upper_bound: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.
        :param metric_interval_lower_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_lower_bound AutoscalingPolicy#metric_interval_lower_bound}.
        :param metric_interval_upper_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_upper_bound AutoscalingPolicy#metric_interval_upper_bound}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d20c74f4eb215c6f01a2400ea2841dca0156afece4399d39866d7b19315e8e)
            check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
            check_type(argname="argument metric_interval_lower_bound", value=metric_interval_lower_bound, expected_type=type_hints["metric_interval_lower_bound"])
            check_type(argname="argument metric_interval_upper_bound", value=metric_interval_upper_bound, expected_type=type_hints["metric_interval_upper_bound"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scaling_adjustment": scaling_adjustment,
        }
        if metric_interval_lower_bound is not None:
            self._values["metric_interval_lower_bound"] = metric_interval_lower_bound
        if metric_interval_upper_bound is not None:
            self._values["metric_interval_upper_bound"] = metric_interval_upper_bound

    @builtins.property
    def scaling_adjustment(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#scaling_adjustment AutoscalingPolicy#scaling_adjustment}.'''
        result = self._values.get("scaling_adjustment")
        assert result is not None, "Required property 'scaling_adjustment' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metric_interval_lower_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_lower_bound AutoscalingPolicy#metric_interval_lower_bound}.'''
        result = self._values.get("metric_interval_lower_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_interval_upper_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_interval_upper_bound AutoscalingPolicy#metric_interval_upper_bound}.'''
        result = self._values.get("metric_interval_upper_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyStepAdjustment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyStepAdjustmentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyStepAdjustmentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74406d5ae07289b5b74ad161309c2cbb2042a38ee0081b39eac6218b807dbe9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyStepAdjustmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__021253259577d227d189715b41fe29f7276c1735003923da60aa513c299454dc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyStepAdjustmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc339413b9b01774a0f712030b95522f007c1dbecefbb48599f5d6137b833846)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a153405823b0516b6b32b5ae5fdb5e766159b4850ea958401a81e76b30d9a9af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ef4f404aaee3ecdfb8902359af48b1a1c2e355921800699ea7de43cc3420370)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f039e9d73f242a1fc94ec058be6b44c2f21ebd669afc6290b6df7928c70f98f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyStepAdjustmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyStepAdjustmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c841575dcea72b08123eabd2eae79b8e497bb922b2b4e04e830e661aeb45e34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMetricIntervalLowerBound")
    def reset_metric_interval_lower_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricIntervalLowerBound", []))

    @jsii.member(jsii_name="resetMetricIntervalUpperBound")
    def reset_metric_interval_upper_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricIntervalUpperBound", []))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalLowerBoundInput")
    def metric_interval_lower_bound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIntervalLowerBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBoundInput")
    def metric_interval_upper_bound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIntervalUpperBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustmentInput")
    def scaling_adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scalingAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalLowerBound"))

    @metric_interval_lower_bound.setter
    def metric_interval_lower_bound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d9a53dc3db6c00e455ebd3320cfc26ae22eebf6d4b896a206e8c4cf9de6e68e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalLowerBound", value)

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalUpperBound"))

    @metric_interval_upper_bound.setter
    def metric_interval_upper_bound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb23079e4e942471a6fc0ad6b14d116388f8ade7a051e896587462f5ec18eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalUpperBound", value)

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingAdjustment"))

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f0935397699c628480c3e52d41ea838ccdad10921cbbee6d90dc170235a050)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingAdjustment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f3090252ac83359d06a157465cae2f7b5c21761c1f424a8f993eff414dd88e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_metric_specification": "customizedMetricSpecification",
        "disable_scale_in": "disableScaleIn",
        "predefined_metric_specification": "predefinedMetricSpecification",
    },
)
class AutoscalingPolicyTargetTrackingConfiguration:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_metric_specification AutoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#disable_scale_in AutoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_specification AutoscalingPolicy#predefined_metric_specification}
        '''
        if isinstance(customized_metric_specification, dict):
            customized_metric_specification = AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification(**customized_metric_specification)
        if isinstance(predefined_metric_specification, dict):
            predefined_metric_specification = AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification(**predefined_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f37c7cfac5681455295d06bf101533dd5b2ab8265175f9aa160c55cfc0a892)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_metric_specification", value=customized_metric_specification, expected_type=type_hints["customized_metric_specification"])
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument predefined_metric_specification", value=predefined_metric_specification, expected_type=type_hints["predefined_metric_specification"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_metric_specification is not None:
            self._values["customized_metric_specification"] = customized_metric_specification
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if predefined_metric_specification is not None:
            self._values["predefined_metric_specification"] = predefined_metric_specification

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#target_value AutoscalingPolicy#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification"]:
        '''customized_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#customized_metric_specification AutoscalingPolicy#customized_metric_specification}
        '''
        result = self._values.get("customized_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification"], result)

    @builtins.property
    def disable_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#disable_scale_in AutoscalingPolicy#disable_scale_in}.'''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def predefined_metric_specification(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"]:
        '''predefined_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_specification AutoscalingPolicy#predefined_metric_specification}
        '''
        result = self._values.get("predefined_metric_specification")
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "statistic": "statistic",
        "metric_dimension": "metricDimension",
        "unit": "unit",
    },
)
class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        metric_dimension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension", typing.Dict[builtins.str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#statistic AutoscalingPolicy#statistic}.
        :param metric_dimension: metric_dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_dimension AutoscalingPolicy#metric_dimension}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deacc0f616370662ba319b9d4fd9504d7598e955230c011722246e721262a17c)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument metric_dimension", value=metric_dimension, expected_type=type_hints["metric_dimension"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "statistic": statistic,
        }
        if metric_dimension is not None:
            self._values["metric_dimension"] = metric_dimension
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#statistic AutoscalingPolicy#statistic}.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_dimension(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension"]]]:
        '''metric_dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_dimension AutoscalingPolicy#metric_dimension}
        '''
        result = self._values.get("metric_dimension")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension"]]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0251fa0824af46b744ae739dc0bf2a2342a2e0416962a6bd1304227b823d0c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#name AutoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#value AutoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e95b8b4d0934432604ab87bbb7ede35e3b7f6f269ae8811a17ce95cdf400d624)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee6bc00a25e93f1b5247ca616c15cf1a77a4f15231e0cd1c0d3d12b3f01de83)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efdb36ecb2103899553befe5231b2b7b1c85ba1bf377d3e6fc323b237036202c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe64aac80ee1375832abad82867ee34e0ae8d80027911bf1c4d20cbf92012f67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__026fbe3ba58ce1bc1c7d9ac0220c24b7b47e7d2073ed642901045eb7a33297b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf3276173a06f261356d07bc21d57c270eeee1f712c972e00a6f0ef7e079efa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5677f20107d717afa06b32e355194f952c3648d5994fbc1a86f9d8771450ac5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf773b123bbe2b23b466d2fd50460f6c9f38cdacd210f84d16c65c4c84f177bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfdaac1f4a4178345f3c18d46c4e616e747acc687263ec51be49429408779c8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0b33715c9b8e6c6505f0830721f168658736bc3204bdc9eb7fedf389e11c5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__153ad1bb1dca22ffb12209a67b7a5193ad3903bc207902b81e8168a01ea078c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricDimension")
    def put_metric_dimension(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a0ddcdecfd6db623913254646a9f7e055ccff5af02c5bb1da47deb47ff47bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricDimension", [value]))

    @jsii.member(jsii_name="resetMetricDimension")
    def reset_metric_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricDimension", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="metricDimension")
    def metric_dimension(
        self,
    ) -> AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList:
        return typing.cast(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList, jsii.get(self, "metricDimension"))

    @builtins.property
    @jsii.member(jsii_name="metricDimensionInput")
    def metric_dimension_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]], jsii.get(self, "metricDimensionInput"))

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
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a0403c46bfa9e8f1af546b8dbed7ec1cb472f70482578cdb9282ba5e33ee41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcaae2ca45199c949a5d93e8debd83bb74d50447063a81002bd6709eaf79e858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790f696f642d2fd819ad70c0eb80ea023b22937be41ff758635e25f2d6ee8fa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__873b0ff74e6e2ee63a0fda1c4677654f6cde08e7b539c43ee81b9a21f88086b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eadc5b2cba0f39df32fc10383acb82b82ba722fd62ddc0c1669f949cd5c61b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingPolicyTargetTrackingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f7292e6e1514eb1bc5bd40d56a3b3a43c83fd4130d61c1feaa620a0844cb9b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomizedMetricSpecification")
    def put_customized_metric_specification(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        metric_dimension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, typing.Dict[builtins.str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_name AutoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#namespace AutoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#statistic AutoscalingPolicy#statistic}.
        :param metric_dimension: metric_dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#metric_dimension AutoscalingPolicy#metric_dimension}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#unit AutoscalingPolicy#unit}.
        '''
        value = AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification(
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            metric_dimension=metric_dimension,
            unit=unit,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedMetricSpecification")
    def put_predefined_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        value = AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedMetricSpecification", [value]))

    @jsii.member(jsii_name="resetCustomizedMetricSpecification")
    def reset_customized_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedMetricSpecification", []))

    @jsii.member(jsii_name="resetDisableScaleIn")
    def reset_disable_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableScaleIn", []))

    @jsii.member(jsii_name="resetPredefinedMetricSpecification")
    def reset_predefined_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedMetricSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference:
        return typing.cast(AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference, jsii.get(self, "customizedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecification")
    def predefined_metric_specification(
        self,
    ) -> "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference":
        return typing.cast("AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference", jsii.get(self, "predefinedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecificationInput")
    def customized_metric_specification_input(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification], jsii.get(self, "customizedMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleInInput")
    def disable_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecificationInput")
    def predefined_metric_specification_input(
        self,
    ) -> typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"]:
        return typing.cast(typing.Optional["AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification"], jsii.get(self, "predefinedMetricSpecificationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7d8caa1841f7ca62e69f6b97a697b7050afc869ab8b28a310a8ca1cdb677f8c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaf22f63014257f00fdb474296dcc2d45325d8ab38ab868adad8c288b11c702b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfiguration]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyTargetTrackingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d908c73ce9d857e1c1da679dd2d78944ed783e9aa7da697774d1c5ed33b650c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ce1a4cc681260cac9db21cdc8f492175491c498e499aa8515a8503d316dd33)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
        }
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#predefined_metric_type AutoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_policy#resource_label AutoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.autoscalingPolicy.AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bde52df456711af3450e22262d8d8143a5a2304115442f9077f978f279caafb3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResourceLabel")
    def reset_resource_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabel", []))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844009a943f21cb6e7ffcfa4fd4b1642aa16b8cf5007a58fe005e69623816029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ef763118357149238001e674a8e56c97530470c440860569be6614f3dbf3b39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification]:
        return typing.cast(typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5c0218df9ce67def3892479a4dd727d35d3fbe56466ef1b2e8f5dc9e4754dbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AutoscalingPolicy",
    "AutoscalingPolicyConfig",
    "AutoscalingPolicyPredictiveScalingConfiguration",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsList",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensionsOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification",
    "AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationOutputReference",
    "AutoscalingPolicyPredictiveScalingConfigurationOutputReference",
    "AutoscalingPolicyStepAdjustment",
    "AutoscalingPolicyStepAdjustmentList",
    "AutoscalingPolicyStepAdjustmentOutputReference",
    "AutoscalingPolicyTargetTrackingConfiguration",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionList",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutputReference",
    "AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutputReference",
    "AutoscalingPolicyTargetTrackingConfigurationOutputReference",
    "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification",
    "AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutputReference",
]

publication.publish()

def _typecheckingstub__e3c771ea35817bd88a6d6b42bd8c66e61b3bf14e6ff8f5e57a58991f77771e54(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    autoscaling_group_name: builtins.str,
    name: builtins.str,
    adjustment_type: typing.Optional[builtins.str] = None,
    cooldown: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    estimated_instance_warmup: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    metric_aggregation_type: typing.Optional[builtins.str] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    policy_type: typing.Optional[builtins.str] = None,
    predictive_scaling_configuration: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    scaling_adjustment: typing.Optional[jsii.Number] = None,
    step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyStepAdjustment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_tracking_configuration: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__2f0cd4adbd01618f7081b952add866eb4439359e77aff92c88ec663c541e7b1e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyStepAdjustment, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f29eeb343e5e6fc94f79425583542067ccb9a824ea3755e87e9d5f78011a104(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c8f9aae878aca43beaea830f1de022cfe88f2cdc10b6137798efcd55a26e22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0578eb8319f8ca93cc3d10e7c76928cb438109c5ddbbc47a3593e443bc3954(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__565590b9a616cae0c410d4f1adac35ec234e7deacaf6d3075b35fdab10f0d95e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2836594ed8440e910cdfe83edcf0c2cfa6137fbf2bcb763829256cab30a52845(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac0c569c0aab34d5dcc1ab644c0534d5bca61774ea512621670bc95037acd2e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc80ce120aa0d7483319ea0652ff260961fdc8bbd830bfb36c84a33fcc83a60a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c11c2583c0a76c21c7ad33ad9592fa45e83bb05ac714d002704536a3a26bcfc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6fa356d09a66b343614ecc525b596ea256389017d2fd374d78c4163b025f789(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a7a096d50283b29a5f59747825d3861121f0cccf088f344f5ad7d24f5a0666(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f42047491b6c5bea67497729bd4c35bf5c1bac722bec3d4b633c8e0b98d575c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9ea1321b9a0f4c8fe0104c6b04d2f83d184e0e74c7a42f259e0db67fbd4bdf(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    autoscaling_group_name: builtins.str,
    name: builtins.str,
    adjustment_type: typing.Optional[builtins.str] = None,
    cooldown: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    estimated_instance_warmup: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    metric_aggregation_type: typing.Optional[builtins.str] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    policy_type: typing.Optional[builtins.str] = None,
    predictive_scaling_configuration: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    scaling_adjustment: typing.Optional[jsii.Number] = None,
    step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyStepAdjustment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_tracking_configuration: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4daa98ddb68bfbb790a88d8c0b7233896163559b2c2f95e4849d102a8bdfaeca(
    *,
    metric_specification: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification, typing.Dict[builtins.str, typing.Any]],
    max_capacity_breach_behavior: typing.Optional[builtins.str] = None,
    max_capacity_buffer: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    scheduling_buffer_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9291fd8e46eba9da50ee0b2123b030afadd776c17e265feefb2ffa4c9af94e95(
    *,
    target_value: jsii.Number,
    customized_capacity_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    customized_load_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    customized_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    predefined_load_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    predefined_metric_pair_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    predefined_scaling_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59d545fa55e3e4f5e2a5b62eac769f31b4d3be255ebfdc61943d88845c56c3e1(
    *,
    metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8137a330670fab2a66d130c4c9c8c5962ea3e0752748c1e0daf0f0446f3a213c(
    *,
    id: builtins.str,
    expression: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat, typing.Dict[builtins.str, typing.Any]]] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e87e3f3e9cc8a931812bf8bbfe6731676e31155986af24bc6f92c83a4886cc9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__836bc7dba5788164b03370ce2db1cb0516906d2721573373917f253f6f28aece(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61291fee044a1a68e1a1a489dd5e930c04655bccfeae1413caac57480fb45c51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff81127e21b951886073dccff35fdf10b2b56e5645e14aacd960bd2ca45f8e1e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dab42ae74b34d5ed91ad6ee3d950cfbdc52f3bfa89e812e413ae6c93b05809ab(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4241ca68ab9759b2db12832622a0f18f0108e5201016d4c560fb8bc77d4b0629(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb48e42115ac870e0958edb23d9ad6688dee8a439cecd30d2cfd25106970c231(
    *,
    metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[builtins.str, typing.Any]],
    stat: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1553f1b141cb646a353642e2cfe7a0c308c142a18f09a65cdc232aab894bd6(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e6a5a1e373704b2e8b0c8044574b0b312e8ff7e91b3df5702845eb32f71f66a(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfecba9f1caca0b5b087e6c535beb2466d77c967ff02cddf4cc333e9e2f3991d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da8e2377c91303af1b33c394cde4d9283827fa14304b48224477be701ed81b6a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbab6020d9942843e20ef24c21e178bad8ca97812e75f36d448e15b44bbe0bf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af59eb1e1bc626661166695d025fd9e53032e54b7b04837ac0d6a2fd5bc2c9e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33be1380736cc4891fae8d9deede3257237f29cc69b2fef6a8eed921160e8490(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e9f930e7b80643ec89d47c16929655d460edf7b7695aee1f52cf934a1b5f89(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a1f09395685eff59e2c8a8f64cd190b4e74aebd456b9020d9aaf99142409d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa544191117f9dad2a10a662c6020df3f6d35cef04f03d62a2030b360096c5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694fb99477a0ff0af51a0bc6db389d29eb99be8a498a1489c49c5270e64ed251(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb76ccbb1f7fc477e4a9b2a83cdd1f2f401a9d5ffa244c700b9a3a5bfb46ea27(
    value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25f377fa5178cb5ce0c159ef7e7e6de34ba2db8d74486540ed6bcaab4fe5ff5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6e342ea68ce79c7bd7fbda34147d255cead364ccdc621248c4b8d2e2a86d36(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8035169c4ba89bdffe586774208a650f3c6de70d9a93d39cef2fe75292d2f87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ee6c6fd2e3936759728e8f609d2ff51b7c8e11a69ad99824eb4b21bd178795(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a12ef1f90ec7f62a082892d1bdd8f1135068f2a4c2640d68fc03db2b0ec4f9d(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStatMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d9fa04cd093bd81e24bbb4062b67ea4871a5c36bf5ad3966a8eb09e259043d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ee7fa74976e499c57cf52fd7324bdb7dde591eab109b4dbed9320999d4054c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2bb591d87637a1e00ae38745a57ccf19aba51c6d993a721031ce1f93feac92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64497c134114eb3f8e2c791c3ecae94e152c49fb93926b1c88a487fdeeacf502(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueriesMetricStat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e01a4222f3caea2efd9e82f94ebcf6cba9bdfcab9f5d3e7fa761c27f8452970e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1efa6151e073c9e3ca134ac86450b49fa8c0c87255af80b2deb9ce4983111e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__507c8619eeea33727eaeec973ff4360f4d55144e59649a10460cfd9807faac89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c17d3d5cf28f44b134908c1fda239361789f17f2544d8b1f588edc79ecb9e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0af0a9999c45cee379f86960110d5bf9b9693f602970ed58ef3cd1a484fa2ce(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0ad1a435cf033dee6e4a410deec3d9b817df55038424457c724c95db414102(
    value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0f026cea54ff886476119ad13fc486496e68b57a83f39bf5f2782beddded498(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b116ea71fb92b6b30d3c161ed5a5ef44b92c27f6fb844fa71f745ffd94bcde(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cc21d7199167dd6c8e3fa8909010dd8e987447f0ab6305d8886e37228bba5aa(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef97a4f5752e5fa9b69b9ecc2a8fc9a472af97531903847d2ca134d6a2d56f03(
    *,
    metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9d2bd6300db79eeb092f68850eadcb5fa65f828f8fe00cb4743bda81c4561a(
    *,
    id: builtins.str,
    expression: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat, typing.Dict[builtins.str, typing.Any]]] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac17fca53c8728ff9d7a58278825ac611082039b6e1a90f9c20bf9432cdd06b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d65a0c2bc29fed4b7fdabe672a9b98f8a66e942e50f84725d86859757cc1a519(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9143e8a84a33d8c9477c27ce3b4cb15abd9fa719442ebfb9ea84ee4fc907a357(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a41fee23bc5aac64371bece1b6d7a0c62aba6fd7a468a25457bee685fdb8e50(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4322a8f25dcf88470b5c03cb527196483b807b7a1c049ea899976fb479767c76(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1085e6ee9700adda28fd5c13272db6d539268005ce9f12fd4f30284a8bff8f58(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64252d35724fccebef5d0be0b902f3599e76be6ee7e2e75ef120642ff2b413dc(
    *,
    metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[builtins.str, typing.Any]],
    stat: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6e7d5b86df66fb145e73d88bd25f306739625353bc45c56d903cebb16548b9(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__103b2057d6ffc6484d5c4be3fdb2bb805c2ec4033580375e7ab9867148bdfe6c(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a414302a77facc3b59b981872ec9f113b78cff23fc61c7adcd342c74568b358(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d52eb8dc7f987eaac87529cede5ba423ac19c23a4e34b0d6799df097e2778f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa20e7415d57744fa01d6c718cbe057fe239683943ed9f7fcbfdca02d9ca0e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7aa990342f424cc5f04bf5eb744634c0eadd9bc8679c1b11c96768e0ccd393f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59366954adafb48d5ef89d16d1b6ebb427a8c6a736f96ee884e53360bf2cb097(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4bfcf681d6d5cab9613b28cb891db01f8ffe60bc8d9ebf257fc4e711da6dd9c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3d36dcd5f8308a7e048a45b28fd7ab35fc59cd966fa020cd415277ed4cd77d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b021eafbab75eb3cf74e5f8a09602654edf7dcba955c58d397c3613658d7993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a5c2ff9c199d5ec2ba6dccab9f685165056d4d87bc7460c6c88802ac19ee22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09972a44b39bd616c2da74cfc9e76f57edb9013806ab6730755cc897f34c17cb(
    value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babf6bf130e939a7209ca880c1bbd8626836bee504621fb94ed6f4e28ac34232(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136b62b741544241dd54e2984a72fd451b995b9267b51ab1fa5b7c324314a6d1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d56949429844362eb41fbb80c429ebb94244fb8331ea11fe742e5d6a77781fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d965d1477be91c80d8d0a73f946b87431af34f020a35be597e4d1b689ec4c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf3269a0cc5838f4347a3dbf92fe0e0d404dbd76983000a5828506d34f54a76(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStatMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7378b7aeb6d225145209e2e3d4e20851753713a4920889348197fdb4e873f40b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7280ff3f1711e7cfd3c915b026549ec7b90c9224f4c7e1d3666812f559e0b29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d45e077afddf2a160ce01bcce8659df757081477c10b6267e5d762c38af666d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785f0cf452a63c07a38fcd5c5fe15ad3c081dacc8ffa8ad383c39cabf6c1eaa7(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueriesMetricStat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc60fe2bd9fb5c15d1c1b748475eb50dfdec4d1f72737d5aef27615587400cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232c1b07d1bb5a8db94a4d0eac200db8b05327523bda171a51fc87f96235779f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9f73ec7a7701c9b69ab11d19447023223a167883a8461f8feaba884ede2dea7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043ff655469d6a7e75e24ecb18ff9b404bb20690172df654fc1bd48bdb415d3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d860073aa5e22a705a44ff5eafc186e996873544ca7265935fc16293872bd4c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63563319ec3caddfb5657c16986b15dc733e4ee84e8a7ffec28a82414226bbd(
    value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba65297025445104042bde1deeb1a968685e198acb7691c392f8b391543d175(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796675a624900954836ff5a5b51a444b914b5aaf48ed050d6196d8422e6fa3c7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd795f40e97623d2e8c0658bff3d64172719d536a205eb0945cfcd75058302c5(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff80ceea99e2b2debea6ec4323d58c43b810ec00b50f1326dab0e7a151a039d(
    *,
    metric_data_queries: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d0729194123ceb7c836afcc32056e66f34907ec93c15e7abacd14f03f2f041(
    *,
    id: builtins.str,
    expression: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat, typing.Dict[builtins.str, typing.Any]]] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00db678cd1f25a9479e281b3a8783eb9739678584f54219faf2b3d3cfae1237(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c03ccd0e569311b0f0f58eb2e61799efa23ce92334e2dfb961a86a91a1c2c9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e4c26449383f65f56938c0d634ff388c080e763b98e5035fbb1de97206ba51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07d40ce2a614308e1e74e68d40692296606166da4c4bf58c87ddd96b2ada84fc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f882fa72886216cec45d64ae7a5145a499ebb2dbb993972c7bdee040875e94ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca509078559bc12be927aa431062d1bd4f0a4abd100e698f48d1faa76f80b912(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2353053dadad55b11db1326eba9b272ad0f141ce1cf8583604e1d81a3ad353d2(
    *,
    metric: typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric, typing.Dict[builtins.str, typing.Any]],
    stat: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a3fbb35361bf60541f6e71168f1b8f178519ac98c8c6d4f9f0fe66b7abaec9f(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966b9fdc10d764d3ff2a27acf786eeb27a682e1bbf4076e61b0d9f07c3b3dd62(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3cdd1355ca9f3c289db8574bab1b51ea606931675f30a83113c8d43047f292(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076c368efdf770d506d9f90c70caa19e9888b7535eba05cf4fbee8acd3a1eb9b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11b1473dfa78280bbcbc7e6e52860669ac8ce7d5f540dbfb277a7775835fc28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e22d3182604821442d1c9c4f98149b9eedd5443f41f7bc5419ea648d113791(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__343e17a8cddca7103a3853638e92661d7f499a05bfe6385b84ad318009f1490c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5913288f81228fbbaea25878b13ec7db46bd224546608d573bdff369286b8d17(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94852910c493c35b9f0a5cd9ddbdc24c99e17213dd273d31faf32fa2459a6c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea7352f1c1c0979dd2b2f426d74fe4c8c9146ceebf03b6deaaaa134568beb356(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d40c595d8820cfa246e4a3eab665c453e4505a778e8d32ccf8617aeac3f0d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129cc1cf25c356765b51d6e4b8dbde852a42606eabf0df8fc6228d06bb89d31d(
    value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc083196cb668b93b0d8d418dc5c1f2a9453578f8fe84695e95c6498bc586c0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910fb863721d34993c1b320474a24e2d83b3472fed9b925a8886cace1e11b469(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetricDimensions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8f84f8b2b5cfbce1b9b67f096458feab9a9fe5a931b2e231f56c3e1e5f063c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3c2bc6b438be6ad42b2e929d037340d68154e9eaca7103701732de209f8b79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38275b0e1cf5624a69e2ff80937ec099f6f127b5c81598bf4f897daef913a236(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStatMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9620f3f5e9c7a3c4124ff2ed23f5dec622612f437dece262effd21bcdd2e728a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029a410326e09b10c537b032b2ac00319eec5af474f8e7a0fff945b92da3f776(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d00ded0096a230f917895fb2aa2cf6e440b683cdf48cb444658c5c1cd39639ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__512ebeec4f07baf4e381884fbfd3cd20ce9b79d19385af0750a61804517254b1(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueriesMetricStat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399aa130ce3f06612d033f703c5b9c0cf8a433b7009ac85c58d9e0c8115e49ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab32315e44d946fb0f0d2fc2b49e3184b1ecc51175f60165c70960dcb21cbdaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b777e61c8756eb55a8af5e1273eafd986446a18c34c213406329157acdbb889(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19959b3e6d888fd1170b39953ae3b75f0f08b3b3cedeb6f15487bc81cd0914b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f62cddfb2178c15d1cf803a924f402a4ceb7a49d14595dc73455beefaacc12(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525ce3b4032dac8eba4cd4241edebe1b8e8c5b02053bb3eee643d2810a1282b7(
    value: typing.Optional[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf2f6a8b11696251ebd9ea75d0505c504e37c450ce3142c31a6516810b6aa97(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf5dba7fad0cb1af8bd90d347c6c0372c468de7da3b56569fae37d1c208b0361(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueries, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc53e86f9f12277932936912fc32ba15ef479ee078c7e92eb5533b3806a59a1(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5ee72804c747f41ed5c543ea19d91720bd94149e66d792c02de9c6e4bb45d7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576fe0387a7d089a02db91edd4123e776655bd7360dd52fcd9d6ec8d2ee5bd19(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c285851edacf0ad2ea3f1856063c2bf24fce7820b5d642949e9298e4264ed9fb(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67567f772d46122a62d7e3bddc67ac64df67d2e4315504435828a3b4b34bcb37(
    *,
    predefined_metric_type: builtins.str,
    resource_label: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e50ea1b2b6ce22f094388a5c11ef51b55378f6f966627bb1bf24ebf6b28b39(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf7c00be787f140d0724e89ffe0348dced00ff626faf8fe2b961e7396a4bee6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e41b6ec1c8522de84d64dfb7424a0cbb51fb51f3e1a3405e74b98d11f63b1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f07d2393ef334b24f1d86474b23c20341ce6835a19ccd101e1c17fe6dd7d6315(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad52c84b24e6745994b2af46209470ae75551a185d81b58ae95a12f396ddbe7(
    *,
    predefined_metric_type: builtins.str,
    resource_label: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124eb5b26383ba72dbeff26a4e556bbcd618aeaa307c53158a4e0671a2e8bd17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f59a3343df82f4ca368abf3da2b98acd52cc24e067a467674c3ff47006eb3a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba219afa34c9f0664f722fcd35e58751119404462f67cc6b69f48f8b43b9585d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b6d515923cec8f2ee508d738b9db2fc1b2bedd39f2d20f80fa33aad5e3c689f(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d62fdb15420670189d4ed5661c7e76fc31e13dd17198dba2c77f22453c29b617(
    *,
    predefined_metric_type: builtins.str,
    resource_label: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a79bd1efe1eff92993d4fa9cd3fb4da8d49625ddfadea36b3eda2cf29a3102(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1912d828e0a69f31f586db14fb1a5fc82847440684afaf4329fd025139afe4d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe68a8097bb2d9717aa39c5915de84d60ba61149dc1f930b824d4c4d34efe52c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77601bfd63c07d45c48d943b07254077b27b0fcd517def23b408a978f3201bce(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c49cb47169cae9d8910ee2315e0b0c2e581d1fcf9435b4f44576aa4fd03103e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619d8aba354f832ab96b0e87cc23e57ad94ee3a67f0364a0c79d69ad8f4166c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f5596c914b34bb1dd74019e06011fa844f45af4285186b2a712b7533fde19e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff1e691b2166594e714befc2f16350cf47948f91fdf4aebbd48c6b9e22d79f9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4dbdf253a944dc5dc108c42169b6ca4e48ac51f5d2b70a15081c77d0b8b68b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001cc877b07f995a37b551c4114bd9325f1a64bb7f63d2bcb1ed6db2f1cad085(
    value: typing.Optional[AutoscalingPolicyPredictiveScalingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d20c74f4eb215c6f01a2400ea2841dca0156afece4399d39866d7b19315e8e(
    *,
    scaling_adjustment: jsii.Number,
    metric_interval_lower_bound: typing.Optional[builtins.str] = None,
    metric_interval_upper_bound: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74406d5ae07289b5b74ad161309c2cbb2042a38ee0081b39eac6218b807dbe9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__021253259577d227d189715b41fe29f7276c1735003923da60aa513c299454dc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc339413b9b01774a0f712030b95522f007c1dbecefbb48599f5d6137b833846(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a153405823b0516b6b32b5ae5fdb5e766159b4850ea958401a81e76b30d9a9af(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef4f404aaee3ecdfb8902359af48b1a1c2e355921800699ea7de43cc3420370(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f039e9d73f242a1fc94ec058be6b44c2f21ebd669afc6290b6df7928c70f98f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyStepAdjustment]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c841575dcea72b08123eabd2eae79b8e497bb922b2b4e04e830e661aeb45e34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9a53dc3db6c00e455ebd3320cfc26ae22eebf6d4b896a206e8c4cf9de6e68e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb23079e4e942471a6fc0ad6b14d116388f8ade7a051e896587462f5ec18eb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f0935397699c628480c3e52d41ea838ccdad10921cbbee6d90dc170235a050(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f3090252ac83359d06a157465cae2f7b5c21761c1f424a8f993eff414dd88e(
    value: typing.Optional[typing.Union[AutoscalingPolicyStepAdjustment, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f37c7cfac5681455295d06bf101533dd5b2ab8265175f9aa160c55cfc0a892(
    *,
    target_value: jsii.Number,
    customized_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    predefined_metric_specification: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deacc0f616370662ba319b9d4fd9504d7598e955230c011722246e721262a17c(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    statistic: builtins.str,
    metric_dimension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, typing.Dict[builtins.str, typing.Any]]]]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0251fa0824af46b744ae739dc0bf2a2342a2e0416962a6bd1304227b823d0c(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e95b8b4d0934432604ab87bbb7ede35e3b7f6f269ae8811a17ce95cdf400d624(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee6bc00a25e93f1b5247ca616c15cf1a77a4f15231e0cd1c0d3d12b3f01de83(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efdb36ecb2103899553befe5231b2b7b1c85ba1bf377d3e6fc323b237036202c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe64aac80ee1375832abad82867ee34e0ae8d80027911bf1c4d20cbf92012f67(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026fbe3ba58ce1bc1c7d9ac0220c24b7b47e7d2073ed642901045eb7a33297b4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf3276173a06f261356d07bc21d57c270eeee1f712c972e00a6f0ef7e079efa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5677f20107d717afa06b32e355194f952c3648d5994fbc1a86f9d8771450ac5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf773b123bbe2b23b466d2fd50460f6c9f38cdacd210f84d16c65c4c84f177bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfdaac1f4a4178345f3c18d46c4e616e747acc687263ec51be49429408779c8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0b33715c9b8e6c6505f0830721f168658736bc3204bdc9eb7fedf389e11c5a(
    value: typing.Optional[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__153ad1bb1dca22ffb12209a67b7a5193ad3903bc207902b81e8168a01ea078c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a0ddcdecfd6db623913254646a9f7e055ccff5af02c5bb1da47deb47ff47bc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a0403c46bfa9e8f1af546b8dbed7ec1cb472f70482578cdb9282ba5e33ee41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcaae2ca45199c949a5d93e8debd83bb74d50447063a81002bd6709eaf79e858(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790f696f642d2fd819ad70c0eb80ea023b22937be41ff758635e25f2d6ee8fa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__873b0ff74e6e2ee63a0fda1c4677654f6cde08e7b539c43ee81b9a21f88086b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eadc5b2cba0f39df32fc10383acb82b82ba722fd62ddc0c1669f949cd5c61b6(
    value: typing.Optional[AutoscalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7292e6e1514eb1bc5bd40d56a3b3a43c83fd4130d61c1feaa620a0844cb9b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d8caa1841f7ca62e69f6b97a697b7050afc869ab8b28a310a8ca1cdb677f8c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf22f63014257f00fdb474296dcc2d45325d8ab38ab868adad8c288b11c702b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d908c73ce9d857e1c1da679dd2d78944ed783e9aa7da697774d1c5ed33b650c(
    value: typing.Optional[AutoscalingPolicyTargetTrackingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ce1a4cc681260cac9db21cdc8f492175491c498e499aa8515a8503d316dd33(
    *,
    predefined_metric_type: builtins.str,
    resource_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde52df456711af3450e22262d8d8143a5a2304115442f9077f978f279caafb3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844009a943f21cb6e7ffcfa4fd4b1642aa16b8cf5007a58fe005e69623816029(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef763118357149238001e674a8e56c97530470c440860569be6614f3dbf3b39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c0218df9ce67def3892479a4dd727d35d3fbe56466ef1b2e8f5dc9e4754dbd(
    value: typing.Optional[AutoscalingPolicyTargetTrackingConfigurationPredefinedMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass
