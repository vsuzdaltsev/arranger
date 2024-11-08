'''
# `aws_appautoscaling_policy`

Refer to the Terraform Registory for docs: [`aws_appautoscaling_policy`](https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy).
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


class AppautoscalingPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy aws_appautoscaling_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        id: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyStepScalingPolicyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy aws_appautoscaling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_id AppautoscalingPolicy#resource_id}.
        :param scalable_dimension: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scalable_dimension AppautoscalingPolicy#scalable_dimension}.
        :param service_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#service_namespace AppautoscalingPolicy#service_namespace}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#id AppautoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#policy_type AppautoscalingPolicy#policy_type}.
        :param step_scaling_policy_configuration: step_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_scaling_policy_configuration AppautoscalingPolicy#step_scaling_policy_configuration}
        :param target_tracking_scaling_policy_configuration: target_tracking_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_tracking_scaling_policy_configuration AppautoscalingPolicy#target_tracking_scaling_policy_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35252b6fd94e40b6fb0f46c109870966737072f7ca25b4f3cf543b762f811f5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppautoscalingPolicyConfig(
            name=name,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            id=id,
            policy_type=policy_type,
            step_scaling_policy_configuration=step_scaling_policy_configuration,
            target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putStepScalingPolicyConfiguration")
    def put_step_scaling_policy_configuration(
        self,
        *,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#adjustment_type AppautoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#cooldown AppautoscalingPolicy#cooldown}.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_aggregation_type AppautoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#min_adjustment_magnitude AppautoscalingPolicy#min_adjustment_magnitude}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_adjustment AppautoscalingPolicy#step_adjustment}
        '''
        value = AppautoscalingPolicyStepScalingPolicyConfiguration(
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            step_adjustment=step_adjustment,
        )

        return typing.cast(None, jsii.invoke(self, "putStepScalingPolicyConfiguration", [value]))

    @jsii.member(jsii_name="putTargetTrackingScalingPolicyConfiguration")
    def put_target_tracking_scaling_policy_configuration(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_in_cooldown: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_value AppautoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#customized_metric_specification AppautoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#disable_scale_in AppautoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_specification AppautoscalingPolicy#predefined_metric_specification}
        :param scale_in_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_in_cooldown AppautoscalingPolicy#scale_in_cooldown}.
        :param scale_out_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_out_cooldown AppautoscalingPolicy#scale_out_cooldown}.
        '''
        value = AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration(
            target_value=target_value,
            customized_metric_specification=customized_metric_specification,
            disable_scale_in=disable_scale_in,
            predefined_metric_specification=predefined_metric_specification,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetTrackingScalingPolicyConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @jsii.member(jsii_name="resetStepScalingPolicyConfiguration")
    def reset_step_scaling_policy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepScalingPolicyConfiguration", []))

    @jsii.member(jsii_name="resetTargetTrackingScalingPolicyConfiguration")
    def reset_target_tracking_scaling_policy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTrackingScalingPolicyConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alarmArns")
    def alarm_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarmArns"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> "AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference":
        return typing.cast("AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference", jsii.get(self, "stepScalingPolicyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference":
        return typing.cast("AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference", jsii.get(self, "targetTrackingScalingPolicyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="scalableDimensionInput")
    def scalable_dimension_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalableDimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNamespaceInput")
    def service_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="stepScalingPolicyConfigurationInput")
    def step_scaling_policy_configuration_input(
        self,
    ) -> typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"]:
        return typing.cast(typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"], jsii.get(self, "stepScalingPolicyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfigurationInput")
    def target_tracking_scaling_policy_configuration_input(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"]:
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"], jsii.get(self, "targetTrackingScalingPolicyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa5f64b0d864655f0922b2479ac76440b5c22389598e997e2b3ad3bf60a9984)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d80c039f4e3d9f2b0a72e783ac853cd3c01042f1372f35fd779f9691d1583d4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e951c70dd3076720406e30df433f8d5d1853f3091f2b9b197720f4d3a871f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4701e5eb3948154f148e02ef42a44df9c486a6c85aeea21c6cfc46a5ade6f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae0c2442085147485b75f42376b02e871de881e44693494ce362fadb8817eb81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalableDimension", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2595a0347bcf63363b91b6f7fb8da9e87003f74da00a7cda762b79323628080e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNamespace", value)


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyConfig",
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
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "id": "id",
        "policy_type": "policyType",
        "step_scaling_policy_configuration": "stepScalingPolicyConfiguration",
        "target_tracking_scaling_policy_configuration": "targetTrackingScalingPolicyConfiguration",
    },
)
class AppautoscalingPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        id: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyStepScalingPolicyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_id AppautoscalingPolicy#resource_id}.
        :param scalable_dimension: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scalable_dimension AppautoscalingPolicy#scalable_dimension}.
        :param service_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#service_namespace AppautoscalingPolicy#service_namespace}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#id AppautoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#policy_type AppautoscalingPolicy#policy_type}.
        :param step_scaling_policy_configuration: step_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_scaling_policy_configuration AppautoscalingPolicy#step_scaling_policy_configuration}
        :param target_tracking_scaling_policy_configuration: target_tracking_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_tracking_scaling_policy_configuration AppautoscalingPolicy#target_tracking_scaling_policy_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(step_scaling_policy_configuration, dict):
            step_scaling_policy_configuration = AppautoscalingPolicyStepScalingPolicyConfiguration(**step_scaling_policy_configuration)
        if isinstance(target_tracking_scaling_policy_configuration, dict):
            target_tracking_scaling_policy_configuration = AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration(**target_tracking_scaling_policy_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f558b9c3e85c7a5ba2b5e1022d5eeef88980ae6a88a5e95f03ebeb30d3f41d7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument step_scaling_policy_configuration", value=step_scaling_policy_configuration, expected_type=type_hints["step_scaling_policy_configuration"])
            check_type(argname="argument target_tracking_scaling_policy_configuration", value=target_tracking_scaling_policy_configuration, expected_type=type_hints["target_tracking_scaling_policy_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
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
        if policy_type is not None:
            self._values["policy_type"] = policy_type
        if step_scaling_policy_configuration is not None:
            self._values["step_scaling_policy_configuration"] = step_scaling_policy_configuration
        if target_tracking_scaling_policy_configuration is not None:
            self._values["target_tracking_scaling_policy_configuration"] = target_tracking_scaling_policy_configuration

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_id AppautoscalingPolicy#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scalable_dimension AppautoscalingPolicy#scalable_dimension}.'''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#service_namespace AppautoscalingPolicy#service_namespace}.'''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#id AppautoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#policy_type AppautoscalingPolicy#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"]:
        '''step_scaling_policy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_scaling_policy_configuration AppautoscalingPolicy#step_scaling_policy_configuration}
        '''
        result = self._values.get("step_scaling_policy_configuration")
        return typing.cast(typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"], result)

    @builtins.property
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"]:
        '''target_tracking_scaling_policy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_tracking_scaling_policy_configuration AppautoscalingPolicy#target_tracking_scaling_policy_configuration}
        '''
        result = self._values.get("target_tracking_scaling_policy_configuration")
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "step_adjustment": "stepAdjustment",
    },
)
class AppautoscalingPolicyStepScalingPolicyConfiguration:
    def __init__(
        self,
        *,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#adjustment_type AppautoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#cooldown AppautoscalingPolicy#cooldown}.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_aggregation_type AppautoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#min_adjustment_magnitude AppautoscalingPolicy#min_adjustment_magnitude}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_adjustment AppautoscalingPolicy#step_adjustment}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a86fd12db369c4472616d35e2a2e5d3dc371b50009f3604d917939638e01d14)
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
            check_type(argname="argument step_adjustment", value=step_adjustment, expected_type=type_hints["step_adjustment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if step_adjustment is not None:
            self._values["step_adjustment"] = step_adjustment

    @builtins.property
    def adjustment_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#adjustment_type AppautoscalingPolicy#adjustment_type}.'''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#cooldown AppautoscalingPolicy#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_aggregation_type AppautoscalingPolicy#metric_aggregation_type}.'''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#min_adjustment_magnitude AppautoscalingPolicy#min_adjustment_magnitude}.'''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_adjustment(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]]:
        '''step_adjustment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_adjustment AppautoscalingPolicy#step_adjustment}
        '''
        result = self._values.get("step_adjustment")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyStepScalingPolicyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c55523f7eea14d84a7064f8393ae379cff46ec3ab338a022779f2613476ff373)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStepAdjustment")
    def put_step_adjustment(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72554b41bd4c45c6536b4248e228c4ecb6c856fff037c23121c364924fe5cf84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStepAdjustment", [value]))

    @jsii.member(jsii_name="resetAdjustmentType")
    def reset_adjustment_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustmentType", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetMetricAggregationType")
    def reset_metric_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricAggregationType", []))

    @jsii.member(jsii_name="resetMinAdjustmentMagnitude")
    def reset_min_adjustment_magnitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinAdjustmentMagnitude", []))

    @jsii.member(jsii_name="resetStepAdjustment")
    def reset_step_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepAdjustment", []))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustment")
    def step_adjustment(
        self,
    ) -> "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList":
        return typing.cast("AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList", jsii.get(self, "stepAdjustment"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentTypeInput")
    def adjustment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="metricAggregationTypeInput")
    def metric_aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricAggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitudeInput")
    def min_adjustment_magnitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minAdjustmentMagnitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustmentInput")
    def step_adjustment_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]], jsii.get(self, "stepAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentType")
    def adjustment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustmentType"))

    @adjustment_type.setter
    def adjustment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67184154409cdff007031b6315498cd04de2f5016e802d06cc9ca74bffd5c680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustmentType", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979d125b3d5602ec19487917f82d5b2e3c6decf28734936c131a952956656815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="metricAggregationType")
    def metric_aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricAggregationType"))

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f97bf0ce581b7f984520e7cffc85f703442da0815e355d6db886aa38b03b4e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricAggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minAdjustmentMagnitude"))

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3bdda4167d5eba3af4dd1c327a8c4318b098db50c420b9d5556592c48e49502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minAdjustmentMagnitude", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration]:
        return typing.cast(typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60dac499119a387b0ee091234930fced256af3fa158ea36d0f9469720c880171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_adjustment": "scalingAdjustment",
        "metric_interval_lower_bound": "metricIntervalLowerBound",
        "metric_interval_upper_bound": "metricIntervalUpperBound",
    },
)
class AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment:
    def __init__(
        self,
        *,
        scaling_adjustment: jsii.Number,
        metric_interval_lower_bound: typing.Optional[builtins.str] = None,
        metric_interval_upper_bound: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scaling_adjustment AppautoscalingPolicy#scaling_adjustment}.
        :param metric_interval_lower_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_lower_bound AppautoscalingPolicy#metric_interval_lower_bound}.
        :param metric_interval_upper_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_upper_bound AppautoscalingPolicy#metric_interval_upper_bound}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd8fa30192236ccf00445f725a9c488132dc97d1e0803910333f43017d099f9)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scaling_adjustment AppautoscalingPolicy#scaling_adjustment}.'''
        result = self._values.get("scaling_adjustment")
        assert result is not None, "Required property 'scaling_adjustment' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metric_interval_lower_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_lower_bound AppautoscalingPolicy#metric_interval_lower_bound}.'''
        result = self._values.get("metric_interval_lower_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_interval_upper_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_upper_bound AppautoscalingPolicy#metric_interval_upper_bound}.'''
        result = self._values.get("metric_interval_upper_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dd4026b0bbddb278c87bf06c5175e97cc4d2e7b41a05742837eac3a8ea8507c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f159a2cc84cb815c0f0751b2343d5e8b15016ad4d4746fd0c80e267613263f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7463defd785370b2fb25c6a859c5bbaa45a80b7bf236bdd4a4d0754d5c0ea727)
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
            type_hints = typing.get_type_hints(_typecheckingstub__226f00c9e7cd6cb0780db85892d872ec5a8dbaf1f9fe97265b2c62c13d6241c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aeefcd903bb1c190fae56c5c49dd36aa455564727ef1258a334cac81aff8d17d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c104376d53819b6916d45c67a4343eb7ef4bbb9e36a71f542e0b237ea9b4b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a4153f78e5fc07ced8761e58c0eb1e431ae925f95d1627d9d1d3bf650b8fe0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c84272d070dbebfddac5593fae95cc20d889aa0bc4b278ba39a797d88776ac28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalLowerBound", value)

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalUpperBound"))

    @metric_interval_upper_bound.setter
    def metric_interval_upper_bound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427e524b1b2122b09d474129e1cbf6f7ca727dfc9cab10c206439a524934e31a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalUpperBound", value)

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingAdjustment"))

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07294c0ce9501df409113a50c8064ad1ef6129e205279755ed3921d045f80842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingAdjustment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af02492b34cd08d7904bbf222f219f0553397c62a3f1c97f33c518066fb6b88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_metric_specification": "customizedMetricSpecification",
        "disable_scale_in": "disableScaleIn",
        "predefined_metric_specification": "predefinedMetricSpecification",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
    },
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification", typing.Dict[builtins.str, typing.Any]]] = None,
        scale_in_cooldown: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_value AppautoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#customized_metric_specification AppautoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#disable_scale_in AppautoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_specification AppautoscalingPolicy#predefined_metric_specification}
        :param scale_in_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_in_cooldown AppautoscalingPolicy#scale_in_cooldown}.
        :param scale_out_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_out_cooldown AppautoscalingPolicy#scale_out_cooldown}.
        '''
        if isinstance(customized_metric_specification, dict):
            customized_metric_specification = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(**customized_metric_specification)
        if isinstance(predefined_metric_specification, dict):
            predefined_metric_specification = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(**predefined_metric_specification)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67c972cd1eb90c01cf0e0cffd035f46e639d54c24274e4d49a1e0e0c2114acd2)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_metric_specification", value=customized_metric_specification, expected_type=type_hints["customized_metric_specification"])
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument predefined_metric_specification", value=predefined_metric_specification, expected_type=type_hints["predefined_metric_specification"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_metric_specification is not None:
            self._values["customized_metric_specification"] = customized_metric_specification
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if predefined_metric_specification is not None:
            self._values["predefined_metric_specification"] = predefined_metric_specification
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_value AppautoscalingPolicy#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_metric_specification(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification"]:
        '''customized_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#customized_metric_specification AppautoscalingPolicy#customized_metric_specification}
        '''
        result = self._values.get("customized_metric_specification")
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification"], result)

    @builtins.property
    def disable_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#disable_scale_in AppautoscalingPolicy#disable_scale_in}.'''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def predefined_metric_specification(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"]:
        '''predefined_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_specification AppautoscalingPolicy#predefined_metric_specification}
        '''
        result = self._values.get("predefined_metric_specification")
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_in_cooldown AppautoscalingPolicy#scale_in_cooldown}.'''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_out_cooldown AppautoscalingPolicy#scale_out_cooldown}.'''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "statistic": "statistic",
        "dimensions": "dimensions",
        "unit": "unit",
    },
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_name AppautoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#namespace AppautoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#statistic AppautoscalingPolicy#statistic}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#dimensions AppautoscalingPolicy#dimensions}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#unit AppautoscalingPolicy#unit}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee4ca76ecd9bcd02816465fc2c24b0971d43b993305f4f0416ba3781c38fced)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_name AppautoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#namespace AppautoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#statistic AppautoscalingPolicy#statistic}.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#dimensions AppautoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions"]]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#unit AppautoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#value AppautoscalingPolicy#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449f775649f1427466afc5135a411ae9ab1b5c11dafcc352f416b4e9f0dc30eb)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#value AppautoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__54df3c518cb44e15daa9205ea7cc7635791cb30e1c0086bf6d1abecbcece6114)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e19ced788b2fb62afbd8a79c85d0035fa0b83c37d1d64bdcefdc0533ac7ed2a6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee3e8a0b989de0c936cb54bc6dca9d3b67524539aeb7d3e288363faa76d0ea2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6768687784aedd4564f0492de8f7881bca82489c5f6189738ceb7db17302302)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57c80c73fbc4d2106ca730a9cd0f80533ee2bc4937ce4f50e643e587f7ac3972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34876950d2706ef2faf66665c8100fe08bc8f1c533ea8958f784c675228f5d46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0cd6f36d903338a8b650793e0b4cd646cef9001905b28bf7e50a57e867ec4dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3736f1df5c62f57476e8fedb78bf13e0d33209a8f968b78e69271d4a8a536ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf48d0a69b078b9f10644d05428986ec3fbd18af6a70933105359d977f0faa10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2363a301a2bc87b877b246e4718981ee0f5faeb8eb0ba04f3c9e3306cb6e641e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcffb114b0fe05d5d25921f9877f02d027788a1903e3fded49e7bb1830c9280b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a3f820a78709cd78e1d7c1ded0025b60617343f1b5cb91c913a0370a47df461)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList:
        return typing.cast(AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]], jsii.get(self, "dimensionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__17b60ab5b0e32f46749c16cd62f5c58fc3116235c4c0ea0e49a79b835544247d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662995c82eed6556f4845a5a6d3090c0b371a587a7877d1344810b821bd61ecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd4738fc51fb3f74945cf52f0444766a4d80baae51d35ba1e764ac24f06dd6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae756636c7aaa69bbe83d924a5ae086912dc0bdae865c648541f9b75adee374)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dfbf586d8339afb3124465802189d6d0dbf7831e49e7ee58fca7e7e8d34ecf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__466d976ed23f50f6f33e45c0da421dff701e782575cf1031a9000b26b115c3ec)
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
        dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_name AppautoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#namespace AppautoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#statistic AppautoscalingPolicy#statistic}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#dimensions AppautoscalingPolicy#dimensions}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#unit AppautoscalingPolicy#unit}.
        '''
        value = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            dimensions=dimensions,
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
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_type AppautoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_label AppautoscalingPolicy#resource_label}.
        '''
        value = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(
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

    @jsii.member(jsii_name="resetScaleInCooldown")
    def reset_scale_in_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInCooldown", []))

    @jsii.member(jsii_name="resetScaleOutCooldown")
    def reset_scale_out_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleOutCooldown", []))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference:
        return typing.cast(AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference, jsii.get(self, "customizedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecification")
    def predefined_metric_specification(
        self,
    ) -> "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference":
        return typing.cast("AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference", jsii.get(self, "predefinedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecificationInput")
    def customized_metric_specification_input(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification], jsii.get(self, "customizedMetricSpecificationInput"))

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
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"]:
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"], jsii.get(self, "predefinedMetricSpecificationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7e42c5a0c4c6b770c725e203e303e7d90d0cce45635a5dbe56b93d619e8af2aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="scaleInCooldown")
    def scale_in_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleInCooldown"))

    @scale_in_cooldown.setter
    def scale_in_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81cae6c75e5f129b1fd4d009465ab684a5bcdcda8f5960e6e279d3067b519dcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleInCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="scaleOutCooldown")
    def scale_out_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleOutCooldown"))

    @scale_out_cooldown.setter
    def scale_out_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0496a82c9d9aae332fb5b9b2064b946920d1ce2c58b59a3a0387988cefc5cb21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleOutCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f1b3511c542550e0b7c1a7a72b303f37c8a9d48cf207880c7a6960a3bd4f71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8981935b631355d10a9e2cf4cdb6c53476d25f3703856e34f12c4c51d3580840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_type AppautoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_label AppautoscalingPolicy#resource_label}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92ff6c8e69ef3f5f85ac785b93e76b075414a0290fe3779e49e7c7294baae2ee)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
        }
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_type AppautoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_label AppautoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57b7ece7519b0e4388990e3c106a30e3db59c507737261fb21d1664f50f2cc2f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e83b4da0e5d08877757b5dfb74ab769f2fa786b7a11879fa70b2b6cc69da3b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ef8a280814379e2be52b9585bc62f0956204bc31ba52a12ce82ddd5c9a4b00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8171929894ac6998cfdf9a8d9f7d68a2a8427f44af9a564653a8e221ea1c78bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppautoscalingPolicy",
    "AppautoscalingPolicyConfig",
    "AppautoscalingPolicyStepScalingPolicyConfiguration",
    "AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference",
    "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment",
    "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList",
    "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference",
]

publication.publish()

def _typecheckingstub__35252b6fd94e40b6fb0f46c109870966737072f7ca25b4f3cf543b762f811f5d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: builtins.str,
    id: typing.Optional[builtins.str] = None,
    policy_type: typing.Optional[builtins.str] = None,
    step_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__3fa5f64b0d864655f0922b2479ac76440b5c22389598e997e2b3ad3bf60a9984(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80c039f4e3d9f2b0a72e783ac853cd3c01042f1372f35fd779f9691d1583d4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e951c70dd3076720406e30df433f8d5d1853f3091f2b9b197720f4d3a871f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4701e5eb3948154f148e02ef42a44df9c486a6c85aeea21c6cfc46a5ade6f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae0c2442085147485b75f42376b02e871de881e44693494ce362fadb8817eb81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2595a0347bcf63363b91b6f7fb8da9e87003f74da00a7cda762b79323628080e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f558b9c3e85c7a5ba2b5e1022d5eeef88980ae6a88a5e95f03ebeb30d3f41d7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: builtins.str,
    id: typing.Optional[builtins.str] = None,
    policy_type: typing.Optional[builtins.str] = None,
    step_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a86fd12db369c4472616d35e2a2e5d3dc371b50009f3604d917939638e01d14(
    *,
    adjustment_type: typing.Optional[builtins.str] = None,
    cooldown: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[builtins.str] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    step_adjustment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55523f7eea14d84a7064f8393ae379cff46ec3ab338a022779f2613476ff373(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72554b41bd4c45c6536b4248e228c4ecb6c856fff037c23121c364924fe5cf84(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67184154409cdff007031b6315498cd04de2f5016e802d06cc9ca74bffd5c680(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979d125b3d5602ec19487917f82d5b2e3c6decf28734936c131a952956656815(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97bf0ce581b7f984520e7cffc85f703442da0815e355d6db886aa38b03b4e38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3bdda4167d5eba3af4dd1c327a8c4318b098db50c420b9d5556592c48e49502(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60dac499119a387b0ee091234930fced256af3fa158ea36d0f9469720c880171(
    value: typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd8fa30192236ccf00445f725a9c488132dc97d1e0803910333f43017d099f9(
    *,
    scaling_adjustment: jsii.Number,
    metric_interval_lower_bound: typing.Optional[builtins.str] = None,
    metric_interval_upper_bound: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd4026b0bbddb278c87bf06c5175e97cc4d2e7b41a05742837eac3a8ea8507c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f159a2cc84cb815c0f0751b2343d5e8b15016ad4d4746fd0c80e267613263f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7463defd785370b2fb25c6a859c5bbaa45a80b7bf236bdd4a4d0754d5c0ea727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226f00c9e7cd6cb0780db85892d872ec5a8dbaf1f9fe97265b2c62c13d6241c9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeefcd903bb1c190fae56c5c49dd36aa455564727ef1258a334cac81aff8d17d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c104376d53819b6916d45c67a4343eb7ef4bbb9e36a71f542e0b237ea9b4b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4153f78e5fc07ced8761e58c0eb1e431ae925f95d1627d9d1d3bf650b8fe0d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84272d070dbebfddac5593fae95cc20d889aa0bc4b278ba39a797d88776ac28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427e524b1b2122b09d474129e1cbf6f7ca727dfc9cab10c206439a524934e31a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07294c0ce9501df409113a50c8064ad1ef6129e205279755ed3921d045f80842(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af02492b34cd08d7904bbf222f219f0553397c62a3f1c97f33c518066fb6b88(
    value: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67c972cd1eb90c01cf0e0cffd035f46e639d54c24274e4d49a1e0e0c2114acd2(
    *,
    target_value: jsii.Number,
    customized_metric_specification: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    disable_scale_in: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    predefined_metric_specification: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    scale_in_cooldown: typing.Optional[jsii.Number] = None,
    scale_out_cooldown: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee4ca76ecd9bcd02816465fc2c24b0971d43b993305f4f0416ba3781c38fced(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    statistic: builtins.str,
    dimensions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449f775649f1427466afc5135a411ae9ab1b5c11dafcc352f416b4e9f0dc30eb(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54df3c518cb44e15daa9205ea7cc7635791cb30e1c0086bf6d1abecbcece6114(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e19ced788b2fb62afbd8a79c85d0035fa0b83c37d1d64bdcefdc0533ac7ed2a6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee3e8a0b989de0c936cb54bc6dca9d3b67524539aeb7d3e288363faa76d0ea2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6768687784aedd4564f0492de8f7881bca82489c5f6189738ceb7db17302302(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c80c73fbc4d2106ca730a9cd0f80533ee2bc4937ce4f50e643e587f7ac3972(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34876950d2706ef2faf66665c8100fe08bc8f1c533ea8958f784c675228f5d46(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0cd6f36d903338a8b650793e0b4cd646cef9001905b28bf7e50a57e867ec4dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3736f1df5c62f57476e8fedb78bf13e0d33209a8f968b78e69271d4a8a536ee2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf48d0a69b078b9f10644d05428986ec3fbd18af6a70933105359d977f0faa10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2363a301a2bc87b877b246e4718981ee0f5faeb8eb0ba04f3c9e3306cb6e641e(
    value: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcffb114b0fe05d5d25921f9877f02d027788a1903e3fded49e7bb1830c9280b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3f820a78709cd78e1d7c1ded0025b60617343f1b5cb91c913a0370a47df461(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b60ab5b0e32f46749c16cd62f5c58fc3116235c4c0ea0e49a79b835544247d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662995c82eed6556f4845a5a6d3090c0b371a587a7877d1344810b821bd61ecf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd4738fc51fb3f74945cf52f0444766a4d80baae51d35ba1e764ac24f06dd6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae756636c7aaa69bbe83d924a5ae086912dc0bdae865c648541f9b75adee374(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dfbf586d8339afb3124465802189d6d0dbf7831e49e7ee58fca7e7e8d34ecf2(
    value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466d976ed23f50f6f33e45c0da421dff701e782575cf1031a9000b26b115c3ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e42c5a0c4c6b770c725e203e303e7d90d0cce45635a5dbe56b93d619e8af2aa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81cae6c75e5f129b1fd4d009465ab684a5bcdcda8f5960e6e279d3067b519dcd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0496a82c9d9aae332fb5b9b2064b946920d1ce2c58b59a3a0387988cefc5cb21(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f1b3511c542550e0b7c1a7a72b303f37c8a9d48cf207880c7a6960a3bd4f71(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8981935b631355d10a9e2cf4cdb6c53476d25f3703856e34f12c4c51d3580840(
    value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92ff6c8e69ef3f5f85ac785b93e76b075414a0290fe3779e49e7c7294baae2ee(
    *,
    predefined_metric_type: builtins.str,
    resource_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b7ece7519b0e4388990e3c106a30e3db59c507737261fb21d1664f50f2cc2f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e83b4da0e5d08877757b5dfb74ab769f2fa786b7a11879fa70b2b6cc69da3b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ef8a280814379e2be52b9585bc62f0956204bc31ba52a12ce82ddd5c9a4b00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8171929894ac6998cfdf9a8d9f7d68a2a8427f44af9a564653a8e221ea1c78bf(
    value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification],
) -> None:
    """Type checking stubs"""
    pass
