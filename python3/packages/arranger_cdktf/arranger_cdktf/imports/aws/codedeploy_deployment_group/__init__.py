'''
# `aws_codedeploy_deployment_group`

Refer to the Terraform Registory for docs: [`aws_codedeploy_deployment_group`](https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group).
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


class CodedeployDeploymentGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group aws_codedeploy_deployment_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        app_name: builtins.str,
        deployment_group_name: builtins.str,
        service_role_arn: builtins.str,
        alarm_configuration: typing.Optional[typing.Union["CodedeployDeploymentGroupAlarmConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_rollback_configuration: typing.Optional[typing.Union["CodedeployDeploymentGroupAutoRollbackConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        blue_green_deployment_config: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        deployment_style: typing.Optional[typing.Union["CodedeployDeploymentGroupDeploymentStyle", typing.Dict[builtins.str, typing.Any]]] = None,
        ec2_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ec2_tag_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSet", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ecs_service: typing.Optional[typing.Union["CodedeployDeploymentGroupEcsService", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        on_premises_instance_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupOnPremisesInstanceTagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trigger_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupTriggerConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group aws_codedeploy_deployment_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param app_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#app_name CodedeployDeploymentGroup#app_name}.
        :param deployment_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_group_name CodedeployDeploymentGroup#deployment_group_name}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_role_arn CodedeployDeploymentGroup#service_role_arn}.
        :param alarm_configuration: alarm_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarm_configuration CodedeployDeploymentGroup#alarm_configuration}
        :param auto_rollback_configuration: auto_rollback_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#auto_rollback_configuration CodedeployDeploymentGroup#auto_rollback_configuration}
        :param autoscaling_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#autoscaling_groups CodedeployDeploymentGroup#autoscaling_groups}.
        :param blue_green_deployment_config: blue_green_deployment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#blue_green_deployment_config CodedeployDeploymentGroup#blue_green_deployment_config}
        :param deployment_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_config_name CodedeployDeploymentGroup#deployment_config_name}.
        :param deployment_style: deployment_style block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_style CodedeployDeploymentGroup#deployment_style}
        :param ec2_tag_filter: ec2_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        :param ec2_tag_set: ec2_tag_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_set CodedeployDeploymentGroup#ec2_tag_set}
        :param ecs_service: ecs_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ecs_service CodedeployDeploymentGroup#ecs_service}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#id CodedeployDeploymentGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_info: load_balancer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#load_balancer_info CodedeployDeploymentGroup#load_balancer_info}
        :param on_premises_instance_tag_filter: on_premises_instance_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#on_premises_instance_tag_filter CodedeployDeploymentGroup#on_premises_instance_tag_filter}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags CodedeployDeploymentGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags_all CodedeployDeploymentGroup#tags_all}.
        :param trigger_configuration: trigger_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_configuration CodedeployDeploymentGroup#trigger_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a51cdfc03044b15048acd5fc253ab5adebe12adc94a1279db346580da69b08d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CodedeployDeploymentGroupConfig(
            app_name=app_name,
            deployment_group_name=deployment_group_name,
            service_role_arn=service_role_arn,
            alarm_configuration=alarm_configuration,
            auto_rollback_configuration=auto_rollback_configuration,
            autoscaling_groups=autoscaling_groups,
            blue_green_deployment_config=blue_green_deployment_config,
            deployment_config_name=deployment_config_name,
            deployment_style=deployment_style,
            ec2_tag_filter=ec2_tag_filter,
            ec2_tag_set=ec2_tag_set,
            ecs_service=ecs_service,
            id=id,
            load_balancer_info=load_balancer_info,
            on_premises_instance_tag_filter=on_premises_instance_tag_filter,
            tags=tags,
            tags_all=tags_all,
            trigger_configuration=trigger_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlarmConfiguration")
    def put_alarm_configuration(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarms CodedeployDeploymentGroup#alarms}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param ignore_poll_alarm_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ignore_poll_alarm_failure CodedeployDeploymentGroup#ignore_poll_alarm_failure}.
        '''
        value = CodedeployDeploymentGroupAlarmConfiguration(
            alarms=alarms,
            enabled=enabled,
            ignore_poll_alarm_failure=ignore_poll_alarm_failure,
        )

        return typing.cast(None, jsii.invoke(self, "putAlarmConfiguration", [value]))

    @jsii.member(jsii_name="putAutoRollbackConfiguration")
    def put_auto_rollback_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#events CodedeployDeploymentGroup#events}.
        '''
        value = CodedeployDeploymentGroupAutoRollbackConfiguration(
            enabled=enabled, events=events
        )

        return typing.cast(None, jsii.invoke(self, "putAutoRollbackConfiguration", [value]))

    @jsii.member(jsii_name="putBlueGreenDeploymentConfig")
    def put_blue_green_deployment_config(
        self,
        *,
        deployment_ready_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption", typing.Dict[builtins.str, typing.Any]]] = None,
        green_fleet_provisioning_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption", typing.Dict[builtins.str, typing.Any]]] = None,
        terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param deployment_ready_option: deployment_ready_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_ready_option CodedeployDeploymentGroup#deployment_ready_option}
        :param green_fleet_provisioning_option: green_fleet_provisioning_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#green_fleet_provisioning_option CodedeployDeploymentGroup#green_fleet_provisioning_option}
        :param terminate_blue_instances_on_deployment_success: terminate_blue_instances_on_deployment_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#terminate_blue_instances_on_deployment_success CodedeployDeploymentGroup#terminate_blue_instances_on_deployment_success}
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfig(
            deployment_ready_option=deployment_ready_option,
            green_fleet_provisioning_option=green_fleet_provisioning_option,
            terminate_blue_instances_on_deployment_success=terminate_blue_instances_on_deployment_success,
        )

        return typing.cast(None, jsii.invoke(self, "putBlueGreenDeploymentConfig", [value]))

    @jsii.member(jsii_name="putDeploymentStyle")
    def put_deployment_style(
        self,
        *,
        deployment_option: typing.Optional[builtins.str] = None,
        deployment_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_option CodedeployDeploymentGroup#deployment_option}.
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_type CodedeployDeploymentGroup#deployment_type}.
        '''
        value = CodedeployDeploymentGroupDeploymentStyle(
            deployment_option=deployment_option, deployment_type=deployment_type
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentStyle", [value]))

    @jsii.member(jsii_name="putEc2TagFilter")
    def put_ec2_tag_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be139ef89e27305ef54753085c08f5b09accd2a0fe432f81c313967a07becbcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2TagFilter", [value]))

    @jsii.member(jsii_name="putEc2TagSet")
    def put_ec2_tag_set(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSet", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b62d1e1f4d5ff829dbf571dc56ae0d412882d8566ec064d53438beb2ba04206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2TagSet", [value]))

    @jsii.member(jsii_name="putEcsService")
    def put_ecs_service(
        self,
        *,
        cluster_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#cluster_name CodedeployDeploymentGroup#cluster_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_name CodedeployDeploymentGroup#service_name}.
        '''
        value = CodedeployDeploymentGroupEcsService(
            cluster_name=cluster_name, service_name=service_name
        )

        return typing.cast(None, jsii.invoke(self, "putEcsService", [value]))

    @jsii.member(jsii_name="putLoadBalancerInfo")
    def put_load_balancer_info(
        self,
        *,
        elb_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoElbInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_group_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_group_pair_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_info: elb_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#elb_info CodedeployDeploymentGroup#elb_info}
        :param target_group_info: target_group_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_info CodedeployDeploymentGroup#target_group_info}
        :param target_group_pair_info: target_group_pair_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_pair_info CodedeployDeploymentGroup#target_group_pair_info}
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfo(
            elb_info=elb_info,
            target_group_info=target_group_info,
            target_group_pair_info=target_group_pair_info,
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancerInfo", [value]))

    @jsii.member(jsii_name="putOnPremisesInstanceTagFilter")
    def put_on_premises_instance_tag_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupOnPremisesInstanceTagFilter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd496324cab5fa2bc61e748e22d74a859718bca9fb54616c12a40cf0b5c20c0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnPremisesInstanceTagFilter", [value]))

    @jsii.member(jsii_name="putTriggerConfiguration")
    def put_trigger_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupTriggerConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd9a054425ae54971157fe66ed06e4a2b90e3c6a93ade7e6422c4af90b38f60d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTriggerConfiguration", [value]))

    @jsii.member(jsii_name="resetAlarmConfiguration")
    def reset_alarm_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarmConfiguration", []))

    @jsii.member(jsii_name="resetAutoRollbackConfiguration")
    def reset_auto_rollback_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRollbackConfiguration", []))

    @jsii.member(jsii_name="resetAutoscalingGroups")
    def reset_autoscaling_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingGroups", []))

    @jsii.member(jsii_name="resetBlueGreenDeploymentConfig")
    def reset_blue_green_deployment_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlueGreenDeploymentConfig", []))

    @jsii.member(jsii_name="resetDeploymentConfigName")
    def reset_deployment_config_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentConfigName", []))

    @jsii.member(jsii_name="resetDeploymentStyle")
    def reset_deployment_style(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentStyle", []))

    @jsii.member(jsii_name="resetEc2TagFilter")
    def reset_ec2_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2TagFilter", []))

    @jsii.member(jsii_name="resetEc2TagSet")
    def reset_ec2_tag_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2TagSet", []))

    @jsii.member(jsii_name="resetEcsService")
    def reset_ecs_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEcsService", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadBalancerInfo")
    def reset_load_balancer_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerInfo", []))

    @jsii.member(jsii_name="resetOnPremisesInstanceTagFilter")
    def reset_on_premises_instance_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnPremisesInstanceTagFilter", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTriggerConfiguration")
    def reset_trigger_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alarmConfiguration")
    def alarm_configuration(
        self,
    ) -> "CodedeployDeploymentGroupAlarmConfigurationOutputReference":
        return typing.cast("CodedeployDeploymentGroupAlarmConfigurationOutputReference", jsii.get(self, "alarmConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfiguration")
    def auto_rollback_configuration(
        self,
    ) -> "CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference":
        return typing.cast("CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference", jsii.get(self, "autoRollbackConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenDeploymentConfig")
    def blue_green_deployment_config(
        self,
    ) -> "CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference":
        return typing.cast("CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference", jsii.get(self, "blueGreenDeploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computePlatform"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupId")
    def deployment_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStyle")
    def deployment_style(
        self,
    ) -> "CodedeployDeploymentGroupDeploymentStyleOutputReference":
        return typing.cast("CodedeployDeploymentGroupDeploymentStyleOutputReference", jsii.get(self, "deploymentStyle"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilter")
    def ec2_tag_filter(self) -> "CodedeployDeploymentGroupEc2TagFilterList":
        return typing.cast("CodedeployDeploymentGroupEc2TagFilterList", jsii.get(self, "ec2TagFilter"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagSet")
    def ec2_tag_set(self) -> "CodedeployDeploymentGroupEc2TagSetList":
        return typing.cast("CodedeployDeploymentGroupEc2TagSetList", jsii.get(self, "ec2TagSet"))

    @builtins.property
    @jsii.member(jsii_name="ecsService")
    def ecs_service(self) -> "CodedeployDeploymentGroupEcsServiceOutputReference":
        return typing.cast("CodedeployDeploymentGroupEcsServiceOutputReference", jsii.get(self, "ecsService"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInfo")
    def load_balancer_info(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoOutputReference", jsii.get(self, "loadBalancerInfo"))

    @builtins.property
    @jsii.member(jsii_name="onPremisesInstanceTagFilter")
    def on_premises_instance_tag_filter(
        self,
    ) -> "CodedeployDeploymentGroupOnPremisesInstanceTagFilterList":
        return typing.cast("CodedeployDeploymentGroupOnPremisesInstanceTagFilterList", jsii.get(self, "onPremisesInstanceTagFilter"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfiguration")
    def trigger_configuration(
        self,
    ) -> "CodedeployDeploymentGroupTriggerConfigurationList":
        return typing.cast("CodedeployDeploymentGroupTriggerConfigurationList", jsii.get(self, "triggerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="alarmConfigurationInput")
    def alarm_configuration_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupAlarmConfiguration"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupAlarmConfiguration"], jsii.get(self, "alarmConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="appNameInput")
    def app_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfigurationInput")
    def auto_rollback_configuration_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupAutoRollbackConfiguration"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupAutoRollbackConfiguration"], jsii.get(self, "autoRollbackConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupsInput")
    def autoscaling_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoscalingGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenDeploymentConfigInput")
    def blue_green_deployment_config_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfig"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfig"], jsii.get(self, "blueGreenDeploymentConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigNameInput")
    def deployment_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupNameInput")
    def deployment_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStyleInput")
    def deployment_style_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupDeploymentStyle"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupDeploymentStyle"], jsii.get(self, "deploymentStyleInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilterInput")
    def ec2_tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]], jsii.get(self, "ec2TagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagSetInput")
    def ec2_tag_set_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]], jsii.get(self, "ec2TagSetInput"))

    @builtins.property
    @jsii.member(jsii_name="ecsServiceInput")
    def ecs_service_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupEcsService"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupEcsService"], jsii.get(self, "ecsServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInfoInput")
    def load_balancer_info_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"], jsii.get(self, "loadBalancerInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="onPremisesInstanceTagFilterInput")
    def on_premises_instance_tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]], jsii.get(self, "onPremisesInstanceTagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

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
    @jsii.member(jsii_name="triggerConfigurationInput")
    def trigger_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]], jsii.get(self, "triggerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="appName")
    def app_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appName"))

    @app_name.setter
    def app_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a9a97dd0daca96a62852f6a4f529f8a497bda322a33f2ffb1253a1dce1f777f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appName", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroups")
    def autoscaling_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "autoscalingGroups"))

    @autoscaling_groups.setter
    def autoscaling_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edd51dc82dfecf8fb35205e2a419528fc3d63c06b35519ca199b67f17000012d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroups", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))

    @deployment_config_name.setter
    def deployment_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6492f80886aa77494b45ed1b1287b6158806156145911aad6475b3d26283f50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @deployment_group_name.setter
    def deployment_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__588d1fc5c0f4b044af3bc6519f0145b4bf1da7471eaac357826dacc44bcfee85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738f8d0469938a18c774b4adf6778013cab39ac7aa467d304e52698443228220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355348322428cd976957ff055f1a275b0ce785776fa8e1779d5e8f1f7c0af026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea97f2d9af84cf70bd3ca15f1ca271b40559689114bc0353cbef8a9235fa985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61be878e4b78f740a1b2845d1c9c30598a8fa67a322a002fe879afa4f0c994d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAlarmConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "enabled": "enabled",
        "ignore_poll_alarm_failure": "ignorePollAlarmFailure",
    },
)
class CodedeployDeploymentGroupAlarmConfiguration:
    def __init__(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarms CodedeployDeploymentGroup#alarms}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param ignore_poll_alarm_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ignore_poll_alarm_failure CodedeployDeploymentGroup#ignore_poll_alarm_failure}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ecf6c6a3f93f00463abab8ca180aa51b7cafe98722ac1c183bfa90372bd5e2)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument ignore_poll_alarm_failure", value=ignore_poll_alarm_failure, expected_type=type_hints["ignore_poll_alarm_failure"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alarms is not None:
            self._values["alarms"] = alarms
        if enabled is not None:
            self._values["enabled"] = enabled
        if ignore_poll_alarm_failure is not None:
            self._values["ignore_poll_alarm_failure"] = ignore_poll_alarm_failure

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarms CodedeployDeploymentGroup#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ignore_poll_alarm_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ignore_poll_alarm_failure CodedeployDeploymentGroup#ignore_poll_alarm_failure}.'''
        result = self._values.get("ignore_poll_alarm_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupAlarmConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupAlarmConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAlarmConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfe81920254ba7a3ef4d61181f5df448e3e842e1c0e3e63605035d14501a6947)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAlarms")
    def reset_alarms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarms", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetIgnorePollAlarmFailure")
    def reset_ignore_poll_alarm_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnorePollAlarmFailure", []))

    @builtins.property
    @jsii.member(jsii_name="alarmsInput")
    def alarms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ignorePollAlarmFailureInput")
    def ignore_poll_alarm_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ignorePollAlarmFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarms"))

    @alarms.setter
    def alarms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc603ee27ce18eb6576851b12d9abcbc74d201bacb8fd46d81f386fe938a554e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__e2156143618edafaf38fd463fee59f012a86d21895a5ef1d1da5c14164255b27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="ignorePollAlarmFailure")
    def ignore_poll_alarm_failure(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ignorePollAlarmFailure"))

    @ignore_poll_alarm_failure.setter
    def ignore_poll_alarm_failure(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c10476108591e14fd58777f4390aa39d5859e06fc4a73908e127c1b4dddcfd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignorePollAlarmFailure", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAlarmConfiguration]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAlarmConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupAlarmConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf8fdd29ca7a513eee6b6b90a73c28a0104b7f713bf74222e69f41d90aae9410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAutoRollbackConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "events": "events"},
)
class CodedeployDeploymentGroupAutoRollbackConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#events CodedeployDeploymentGroup#events}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ecae8b42597023d25f3486f36bb962a73b40c37564208af454fa09631b5583)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if events is not None:
            self._values["events"] = events

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#events CodedeployDeploymentGroup#events}.'''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupAutoRollbackConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a038ca8a7c2800009a7e96b6a1d9bca48584c19f7c1fba6556f7adfe29f6b35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEvents")
    def reset_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvents", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7fb153baf84574ae987797ad78cf4af8cf8a57de9bc96fd225e8caafc05c4eba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d593702e0f1d1d417867afb43d2b353af1044907eb22c6f37ba6804985c4ce88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699608825ba0eb3423625611c83ed065a6b66afaccdffd2cb973e788ba340412)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfig",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_ready_option": "deploymentReadyOption",
        "green_fleet_provisioning_option": "greenFleetProvisioningOption",
        "terminate_blue_instances_on_deployment_success": "terminateBlueInstancesOnDeploymentSuccess",
    },
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfig:
    def __init__(
        self,
        *,
        deployment_ready_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption", typing.Dict[builtins.str, typing.Any]]] = None,
        green_fleet_provisioning_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption", typing.Dict[builtins.str, typing.Any]]] = None,
        terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param deployment_ready_option: deployment_ready_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_ready_option CodedeployDeploymentGroup#deployment_ready_option}
        :param green_fleet_provisioning_option: green_fleet_provisioning_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#green_fleet_provisioning_option CodedeployDeploymentGroup#green_fleet_provisioning_option}
        :param terminate_blue_instances_on_deployment_success: terminate_blue_instances_on_deployment_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#terminate_blue_instances_on_deployment_success CodedeployDeploymentGroup#terminate_blue_instances_on_deployment_success}
        '''
        if isinstance(deployment_ready_option, dict):
            deployment_ready_option = CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(**deployment_ready_option)
        if isinstance(green_fleet_provisioning_option, dict):
            green_fleet_provisioning_option = CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(**green_fleet_provisioning_option)
        if isinstance(terminate_blue_instances_on_deployment_success, dict):
            terminate_blue_instances_on_deployment_success = CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(**terminate_blue_instances_on_deployment_success)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cfae2ebbaf85ea96608d68589b2a8a6c94be88d8eb45093f2d1e69be4e7d021)
            check_type(argname="argument deployment_ready_option", value=deployment_ready_option, expected_type=type_hints["deployment_ready_option"])
            check_type(argname="argument green_fleet_provisioning_option", value=green_fleet_provisioning_option, expected_type=type_hints["green_fleet_provisioning_option"])
            check_type(argname="argument terminate_blue_instances_on_deployment_success", value=terminate_blue_instances_on_deployment_success, expected_type=type_hints["terminate_blue_instances_on_deployment_success"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_ready_option is not None:
            self._values["deployment_ready_option"] = deployment_ready_option
        if green_fleet_provisioning_option is not None:
            self._values["green_fleet_provisioning_option"] = green_fleet_provisioning_option
        if terminate_blue_instances_on_deployment_success is not None:
            self._values["terminate_blue_instances_on_deployment_success"] = terminate_blue_instances_on_deployment_success

    @builtins.property
    def deployment_ready_option(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption"]:
        '''deployment_ready_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_ready_option CodedeployDeploymentGroup#deployment_ready_option}
        '''
        result = self._values.get("deployment_ready_option")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption"], result)

    @builtins.property
    def green_fleet_provisioning_option(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption"]:
        '''green_fleet_provisioning_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#green_fleet_provisioning_option CodedeployDeploymentGroup#green_fleet_provisioning_option}
        '''
        result = self._values.get("green_fleet_provisioning_option")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption"], result)

    @builtins.property
    def terminate_blue_instances_on_deployment_success(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"]:
        '''terminate_blue_instances_on_deployment_success block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#terminate_blue_instances_on_deployment_success CodedeployDeploymentGroup#terminate_blue_instances_on_deployment_success}
        '''
        result = self._values.get("terminate_blue_instances_on_deployment_success")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption",
    jsii_struct_bases=[],
    name_mapping={
        "action_on_timeout": "actionOnTimeout",
        "wait_time_in_minutes": "waitTimeInMinutes",
    },
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption:
    def __init__(
        self,
        *,
        action_on_timeout: typing.Optional[builtins.str] = None,
        wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action_on_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action_on_timeout CodedeployDeploymentGroup#action_on_timeout}.
        :param wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#wait_time_in_minutes CodedeployDeploymentGroup#wait_time_in_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d745b8f19e9b07194abcdaa553c7801f9720e380b7f08f79a4292528bd98271)
            check_type(argname="argument action_on_timeout", value=action_on_timeout, expected_type=type_hints["action_on_timeout"])
            check_type(argname="argument wait_time_in_minutes", value=wait_time_in_minutes, expected_type=type_hints["wait_time_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action_on_timeout is not None:
            self._values["action_on_timeout"] = action_on_timeout
        if wait_time_in_minutes is not None:
            self._values["wait_time_in_minutes"] = wait_time_in_minutes

    @builtins.property
    def action_on_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action_on_timeout CodedeployDeploymentGroup#action_on_timeout}.'''
        result = self._values.get("action_on_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#wait_time_in_minutes CodedeployDeploymentGroup#wait_time_in_minutes}.'''
        result = self._values.get("wait_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__246249807389f65d4a1203886ef6612cbf6aec13c2e1360b8dc3145cd761fc2b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActionOnTimeout")
    def reset_action_on_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionOnTimeout", []))

    @jsii.member(jsii_name="resetWaitTimeInMinutes")
    def reset_wait_time_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitTimeInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="actionOnTimeoutInput")
    def action_on_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionOnTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="waitTimeInMinutesInput")
    def wait_time_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitTimeInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="actionOnTimeout")
    def action_on_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionOnTimeout"))

    @action_on_timeout.setter
    def action_on_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2fabdf03892ba27256fb30f1bd07e24b4af7501a2bba54d215e18194a77e18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionOnTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="waitTimeInMinutes")
    def wait_time_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitTimeInMinutes"))

    @wait_time_in_minutes.setter
    def wait_time_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff4d617ece90dd18259d92de642e7e84994d64c58c2ecf5af76bcc2990a2e944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitTimeInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee5060141e0d4daa3e168dbcc233431debeb2f6fd566ade24636f03ef88473ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption",
    jsii_struct_bases=[],
    name_mapping={"action": "action"},
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption:
    def __init__(self, *, action: typing.Optional[builtins.str] = None) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9123b656f15fcd4d6eb00f9b5ff9412650b8aed94d868592264600e351f6270)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f5e1c153826f9b0f8d07cf3cd1345fb6bb223d96ec03bb49310c5295c3c1215)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee7a5009c74f220a9456b9bfc609f15e51a7a1e4a521eff0616bc3d02857ebff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4f6157f4e3b1c07a65658bfafa17816d6cfff0319bcd23a9b2af32d602c4f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec006e660114f4e22eaf9cf73eb4a79ea594aa15e2722f2ac1c04c9a7311078d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeploymentReadyOption")
    def put_deployment_ready_option(
        self,
        *,
        action_on_timeout: typing.Optional[builtins.str] = None,
        wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action_on_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action_on_timeout CodedeployDeploymentGroup#action_on_timeout}.
        :param wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#wait_time_in_minutes CodedeployDeploymentGroup#wait_time_in_minutes}.
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(
            action_on_timeout=action_on_timeout,
            wait_time_in_minutes=wait_time_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentReadyOption", [value]))

    @jsii.member(jsii_name="putGreenFleetProvisioningOption")
    def put_green_fleet_provisioning_option(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(
            action=action
        )

        return typing.cast(None, jsii.invoke(self, "putGreenFleetProvisioningOption", [value]))

    @jsii.member(jsii_name="putTerminateBlueInstancesOnDeploymentSuccess")
    def put_terminate_blue_instances_on_deployment_success(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        :param termination_wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#termination_wait_time_in_minutes CodedeployDeploymentGroup#termination_wait_time_in_minutes}.
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(
            action=action,
            termination_wait_time_in_minutes=termination_wait_time_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putTerminateBlueInstancesOnDeploymentSuccess", [value]))

    @jsii.member(jsii_name="resetDeploymentReadyOption")
    def reset_deployment_ready_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentReadyOption", []))

    @jsii.member(jsii_name="resetGreenFleetProvisioningOption")
    def reset_green_fleet_provisioning_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGreenFleetProvisioningOption", []))

    @jsii.member(jsii_name="resetTerminateBlueInstancesOnDeploymentSuccess")
    def reset_terminate_blue_instances_on_deployment_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateBlueInstancesOnDeploymentSuccess", []))

    @builtins.property
    @jsii.member(jsii_name="deploymentReadyOption")
    def deployment_ready_option(
        self,
    ) -> CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference:
        return typing.cast(CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference, jsii.get(self, "deploymentReadyOption"))

    @builtins.property
    @jsii.member(jsii_name="greenFleetProvisioningOption")
    def green_fleet_provisioning_option(
        self,
    ) -> CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference:
        return typing.cast(CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference, jsii.get(self, "greenFleetProvisioningOption"))

    @builtins.property
    @jsii.member(jsii_name="terminateBlueInstancesOnDeploymentSuccess")
    def terminate_blue_instances_on_deployment_success(
        self,
    ) -> "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference":
        return typing.cast("CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference", jsii.get(self, "terminateBlueInstancesOnDeploymentSuccess"))

    @builtins.property
    @jsii.member(jsii_name="deploymentReadyOptionInput")
    def deployment_ready_option_input(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption], jsii.get(self, "deploymentReadyOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="greenFleetProvisioningOptionInput")
    def green_fleet_provisioning_option_input(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption], jsii.get(self, "greenFleetProvisioningOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateBlueInstancesOnDeploymentSuccessInput")
    def terminate_blue_instances_on_deployment_success_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"], jsii.get(self, "terminateBlueInstancesOnDeploymentSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262019f5f73bbe2e02e88d5080686abd88a9ee25ace7357a3038a175e6f9619d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "termination_wait_time_in_minutes": "terminationWaitTimeInMinutes",
    },
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        :param termination_wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#termination_wait_time_in_minutes CodedeployDeploymentGroup#termination_wait_time_in_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813fb4b5d0d11c08648e14e21aa489eb1f52f35887bf6c2f3276eb9769bdd084)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument termination_wait_time_in_minutes", value=termination_wait_time_in_minutes, expected_type=type_hints["termination_wait_time_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if termination_wait_time_in_minutes is not None:
            self._values["termination_wait_time_in_minutes"] = termination_wait_time_in_minutes

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def termination_wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#termination_wait_time_in_minutes CodedeployDeploymentGroup#termination_wait_time_in_minutes}.'''
        result = self._values.get("termination_wait_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03b895445cf0d437c0dfbb844f6e4355f29cbce6c1b05e272cf9dda91e52c24c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetTerminationWaitTimeInMinutes")
    def reset_termination_wait_time_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationWaitTimeInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationWaitTimeInMinutesInput")
    def termination_wait_time_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "terminationWaitTimeInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64fa818deda9f777a77a3e78f3fc520a388d209748f0d09bb59ea89ef460003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="terminationWaitTimeInMinutes")
    def termination_wait_time_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "terminationWaitTimeInMinutes"))

    @termination_wait_time_in_minutes.setter
    def termination_wait_time_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e379e865f137eb26f9a805a798fbe58f06c20f3f6d6e79ab240521cfa3a288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationWaitTimeInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__103dd36b285947a02cfd35c23534cbf2165196b7461ec6186c724f7bb3decf0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "app_name": "appName",
        "deployment_group_name": "deploymentGroupName",
        "service_role_arn": "serviceRoleArn",
        "alarm_configuration": "alarmConfiguration",
        "auto_rollback_configuration": "autoRollbackConfiguration",
        "autoscaling_groups": "autoscalingGroups",
        "blue_green_deployment_config": "blueGreenDeploymentConfig",
        "deployment_config_name": "deploymentConfigName",
        "deployment_style": "deploymentStyle",
        "ec2_tag_filter": "ec2TagFilter",
        "ec2_tag_set": "ec2TagSet",
        "ecs_service": "ecsService",
        "id": "id",
        "load_balancer_info": "loadBalancerInfo",
        "on_premises_instance_tag_filter": "onPremisesInstanceTagFilter",
        "tags": "tags",
        "tags_all": "tagsAll",
        "trigger_configuration": "triggerConfiguration",
    },
)
class CodedeployDeploymentGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        app_name: builtins.str,
        deployment_group_name: builtins.str,
        service_role_arn: builtins.str,
        alarm_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAlarmConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_rollback_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAutoRollbackConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        blue_green_deployment_config: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        deployment_style: typing.Optional[typing.Union["CodedeployDeploymentGroupDeploymentStyle", typing.Dict[builtins.str, typing.Any]]] = None,
        ec2_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ec2_tag_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSet", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ecs_service: typing.Optional[typing.Union["CodedeployDeploymentGroupEcsService", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        on_premises_instance_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupOnPremisesInstanceTagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trigger_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupTriggerConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param app_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#app_name CodedeployDeploymentGroup#app_name}.
        :param deployment_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_group_name CodedeployDeploymentGroup#deployment_group_name}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_role_arn CodedeployDeploymentGroup#service_role_arn}.
        :param alarm_configuration: alarm_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarm_configuration CodedeployDeploymentGroup#alarm_configuration}
        :param auto_rollback_configuration: auto_rollback_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#auto_rollback_configuration CodedeployDeploymentGroup#auto_rollback_configuration}
        :param autoscaling_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#autoscaling_groups CodedeployDeploymentGroup#autoscaling_groups}.
        :param blue_green_deployment_config: blue_green_deployment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#blue_green_deployment_config CodedeployDeploymentGroup#blue_green_deployment_config}
        :param deployment_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_config_name CodedeployDeploymentGroup#deployment_config_name}.
        :param deployment_style: deployment_style block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_style CodedeployDeploymentGroup#deployment_style}
        :param ec2_tag_filter: ec2_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        :param ec2_tag_set: ec2_tag_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_set CodedeployDeploymentGroup#ec2_tag_set}
        :param ecs_service: ecs_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ecs_service CodedeployDeploymentGroup#ecs_service}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#id CodedeployDeploymentGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_info: load_balancer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#load_balancer_info CodedeployDeploymentGroup#load_balancer_info}
        :param on_premises_instance_tag_filter: on_premises_instance_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#on_premises_instance_tag_filter CodedeployDeploymentGroup#on_premises_instance_tag_filter}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags CodedeployDeploymentGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags_all CodedeployDeploymentGroup#tags_all}.
        :param trigger_configuration: trigger_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_configuration CodedeployDeploymentGroup#trigger_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alarm_configuration, dict):
            alarm_configuration = CodedeployDeploymentGroupAlarmConfiguration(**alarm_configuration)
        if isinstance(auto_rollback_configuration, dict):
            auto_rollback_configuration = CodedeployDeploymentGroupAutoRollbackConfiguration(**auto_rollback_configuration)
        if isinstance(blue_green_deployment_config, dict):
            blue_green_deployment_config = CodedeployDeploymentGroupBlueGreenDeploymentConfig(**blue_green_deployment_config)
        if isinstance(deployment_style, dict):
            deployment_style = CodedeployDeploymentGroupDeploymentStyle(**deployment_style)
        if isinstance(ecs_service, dict):
            ecs_service = CodedeployDeploymentGroupEcsService(**ecs_service)
        if isinstance(load_balancer_info, dict):
            load_balancer_info = CodedeployDeploymentGroupLoadBalancerInfo(**load_balancer_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93088c6e0ca80958f5ad1a88d417be5c9481dd4a7ce9fd28824bd92690947400)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument app_name", value=app_name, expected_type=type_hints["app_name"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument alarm_configuration", value=alarm_configuration, expected_type=type_hints["alarm_configuration"])
            check_type(argname="argument auto_rollback_configuration", value=auto_rollback_configuration, expected_type=type_hints["auto_rollback_configuration"])
            check_type(argname="argument autoscaling_groups", value=autoscaling_groups, expected_type=type_hints["autoscaling_groups"])
            check_type(argname="argument blue_green_deployment_config", value=blue_green_deployment_config, expected_type=type_hints["blue_green_deployment_config"])
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument deployment_style", value=deployment_style, expected_type=type_hints["deployment_style"])
            check_type(argname="argument ec2_tag_filter", value=ec2_tag_filter, expected_type=type_hints["ec2_tag_filter"])
            check_type(argname="argument ec2_tag_set", value=ec2_tag_set, expected_type=type_hints["ec2_tag_set"])
            check_type(argname="argument ecs_service", value=ecs_service, expected_type=type_hints["ecs_service"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_balancer_info", value=load_balancer_info, expected_type=type_hints["load_balancer_info"])
            check_type(argname="argument on_premises_instance_tag_filter", value=on_premises_instance_tag_filter, expected_type=type_hints["on_premises_instance_tag_filter"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument trigger_configuration", value=trigger_configuration, expected_type=type_hints["trigger_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_name": app_name,
            "deployment_group_name": deployment_group_name,
            "service_role_arn": service_role_arn,
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
        if alarm_configuration is not None:
            self._values["alarm_configuration"] = alarm_configuration
        if auto_rollback_configuration is not None:
            self._values["auto_rollback_configuration"] = auto_rollback_configuration
        if autoscaling_groups is not None:
            self._values["autoscaling_groups"] = autoscaling_groups
        if blue_green_deployment_config is not None:
            self._values["blue_green_deployment_config"] = blue_green_deployment_config
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if deployment_style is not None:
            self._values["deployment_style"] = deployment_style
        if ec2_tag_filter is not None:
            self._values["ec2_tag_filter"] = ec2_tag_filter
        if ec2_tag_set is not None:
            self._values["ec2_tag_set"] = ec2_tag_set
        if ecs_service is not None:
            self._values["ecs_service"] = ecs_service
        if id is not None:
            self._values["id"] = id
        if load_balancer_info is not None:
            self._values["load_balancer_info"] = load_balancer_info
        if on_premises_instance_tag_filter is not None:
            self._values["on_premises_instance_tag_filter"] = on_premises_instance_tag_filter
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if trigger_configuration is not None:
            self._values["trigger_configuration"] = trigger_configuration

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
    def app_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#app_name CodedeployDeploymentGroup#app_name}.'''
        result = self._values.get("app_name")
        assert result is not None, "Required property 'app_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_group_name CodedeployDeploymentGroup#deployment_group_name}.'''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_role_arn CodedeployDeploymentGroup#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_configuration(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAlarmConfiguration]:
        '''alarm_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarm_configuration CodedeployDeploymentGroup#alarm_configuration}
        '''
        result = self._values.get("alarm_configuration")
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAlarmConfiguration], result)

    @builtins.property
    def auto_rollback_configuration(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration]:
        '''auto_rollback_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#auto_rollback_configuration CodedeployDeploymentGroup#auto_rollback_configuration}
        '''
        result = self._values.get("auto_rollback_configuration")
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration], result)

    @builtins.property
    def autoscaling_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#autoscaling_groups CodedeployDeploymentGroup#autoscaling_groups}.'''
        result = self._values.get("autoscaling_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def blue_green_deployment_config(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig]:
        '''blue_green_deployment_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#blue_green_deployment_config CodedeployDeploymentGroup#blue_green_deployment_config}
        '''
        result = self._values.get("blue_green_deployment_config")
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig], result)

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_config_name CodedeployDeploymentGroup#deployment_config_name}.'''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_style(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupDeploymentStyle"]:
        '''deployment_style block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_style CodedeployDeploymentGroup#deployment_style}
        '''
        result = self._values.get("deployment_style")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupDeploymentStyle"], result)

    @builtins.property
    def ec2_tag_filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]]:
        '''ec2_tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        '''
        result = self._values.get("ec2_tag_filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]], result)

    @builtins.property
    def ec2_tag_set(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]]:
        '''ec2_tag_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_set CodedeployDeploymentGroup#ec2_tag_set}
        '''
        result = self._values.get("ec2_tag_set")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]], result)

    @builtins.property
    def ecs_service(self) -> typing.Optional["CodedeployDeploymentGroupEcsService"]:
        '''ecs_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ecs_service CodedeployDeploymentGroup#ecs_service}
        '''
        result = self._values.get("ecs_service")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupEcsService"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#id CodedeployDeploymentGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_info(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"]:
        '''load_balancer_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#load_balancer_info CodedeployDeploymentGroup#load_balancer_info}
        '''
        result = self._values.get("load_balancer_info")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"], result)

    @builtins.property
    def on_premises_instance_tag_filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]]:
        '''on_premises_instance_tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#on_premises_instance_tag_filter CodedeployDeploymentGroup#on_premises_instance_tag_filter}
        '''
        result = self._values.get("on_premises_instance_tag_filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags CodedeployDeploymentGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags_all CodedeployDeploymentGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def trigger_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]]:
        '''trigger_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_configuration CodedeployDeploymentGroup#trigger_configuration}
        '''
        result = self._values.get("trigger_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupDeploymentStyle",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_option": "deploymentOption",
        "deployment_type": "deploymentType",
    },
)
class CodedeployDeploymentGroupDeploymentStyle:
    def __init__(
        self,
        *,
        deployment_option: typing.Optional[builtins.str] = None,
        deployment_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_option CodedeployDeploymentGroup#deployment_option}.
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_type CodedeployDeploymentGroup#deployment_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e98b44fcff11257a6950cb457f863b133073ed55b2dbcd953fdf2be006dff9f)
            check_type(argname="argument deployment_option", value=deployment_option, expected_type=type_hints["deployment_option"])
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_option is not None:
            self._values["deployment_option"] = deployment_option
        if deployment_type is not None:
            self._values["deployment_type"] = deployment_type

    @builtins.property
    def deployment_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_option CodedeployDeploymentGroup#deployment_option}.'''
        result = self._values.get("deployment_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_type CodedeployDeploymentGroup#deployment_type}.'''
        result = self._values.get("deployment_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupDeploymentStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupDeploymentStyleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupDeploymentStyleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c5171d672aafcefa4d49e46f052e2d1745842339dada465f7616b1ff18382d5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeploymentOption")
    def reset_deployment_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentOption", []))

    @jsii.member(jsii_name="resetDeploymentType")
    def reset_deployment_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentType", []))

    @builtins.property
    @jsii.member(jsii_name="deploymentOptionInput")
    def deployment_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentOption")
    def deployment_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentOption"))

    @deployment_option.setter
    def deployment_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c6c138cbbd3d51cfba1a669e381d4b0bc126e3f3984b310bc9b96b618a26ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentOption", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76c3572fcc99b2087a43208b6adf0aede0779e98adc0547462e353d589632756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupDeploymentStyle]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupDeploymentStyle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupDeploymentStyle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34a5b6cbc13a18bb73ac27a44fb15ffa2bba36777daa28a2b94c2b4dfaff0f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CodedeployDeploymentGroupEc2TagFilter:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c292b2bbe2497a3901bd7af6bc14c9ac0965b2d160381d198ac2d9417d53336a)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEc2TagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupEc2TagFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b36b5443a51c3f8aa611d51b6349d549b3483e46d3b64f90891cc29ab3a51f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupEc2TagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7f6de7bae10dd491bc6f23e81ff5145707db60a2640bf2838d44cd6083a8a98)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupEc2TagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765e9fc84be1513d1d3e04d36623c143d6708b1265473772a3dba6ca8809bcef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90a1c57fd06bfd379cd2a24dae1b457f3497400292cf244d7032b176223b2c9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3441fceed5d6b558b5f049ff77428810a11b0585275002d042dde9653924842e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069c3971ca97cf0e220712cfac84b8e81b92232c5f58317847bb4f36be1fe4b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__10c53fcb9bdc8ec7a5823b7c412bd15b29919fbbaa8b741f79c71b79bd8c9482)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b238855826892db5ceb893c1b62133e37e68fdf16c11dc207b10df80602ebaa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0ebc6ec99ea132618954526f2acb3be835aad3473877e17b23e43d716d766af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca0cb1291f68300cc6e42c16a566d72dde49fd946af23dc95d7b45b618860b86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6188cd60accbffcb94b4954b2ce67231e1acd01b4effed6a16a5d5c5e076da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSet",
    jsii_struct_bases=[],
    name_mapping={"ec2_tag_filter": "ec2TagFilter"},
)
class CodedeployDeploymentGroupEc2TagSet:
    def __init__(
        self,
        *,
        ec2_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSetEc2TagFilter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ec2_tag_filter: ec2_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318b05de0d2ec5a79b50571dc034c0c41cbeab7f241bacdb4f5b5cfc424dc3ba)
            check_type(argname="argument ec2_tag_filter", value=ec2_tag_filter, expected_type=type_hints["ec2_tag_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ec2_tag_filter is not None:
            self._values["ec2_tag_filter"] = ec2_tag_filter

    @builtins.property
    def ec2_tag_filter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSetEc2TagFilter"]]]:
        '''ec2_tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        '''
        result = self._values.get("ec2_tag_filter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSetEc2TagFilter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEc2TagSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetEc2TagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CodedeployDeploymentGroupEc2TagSetEc2TagFilter:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d30c1905187a12773653d48f4d17c659d52005e5fc347e5ee3115dde06b59b6)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEc2TagSetEc2TagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupEc2TagSetEc2TagFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetEc2TagFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6941bdb8c77a7cb28c7fd411a5326eb205faf1e5e0a86e9535f181c2c2bac5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da38943f078ffc1b41abafc98ce369d95d4f26162e02273089375d009c9fc420)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff301c4d8112412514b185cbcd384d1e200d47099415f1f0694f248a3fbf4d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__83e95bf5a25bc11ff4b315c399cce76ba52f7065399c7d93ddf653c4c7eafece)
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
            type_hints = typing.get_type_hints(_typecheckingstub__179388225f68319c07fef29cf5385de7f9ea2ef8e2ab7ffae6fd64d521526cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5366975b81a94977494ef35e32d9810cea8d4a2007b4263863044f84e5fa1082)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29da1a20ce680a29ba6802fc614b62f0e560aba06997f65fa5eb426e00ff6679)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d58f16a55573825c032203ed02e5b39318b8a09fd65b90492789fb1006eb42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b153ae40f692ee4b12ad5f72297ffb0901958d135a1757e91853795709508bc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e322e098c9a612a15bcc5d60fef03a01833d65d08710880fdc13c0e17ed3941c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8077c5667693c1980650cc8e2d238fc075d6396a41c239ba2afe4cc73db7b71d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagSetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66dc1180103ec102ce24a4fe3dc028149929004fc5a1f1733cf241d739d417a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupEc2TagSetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ade9e16837d6002497ea768308af93d90836c6e42505a6d9026f798d137211)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupEc2TagSetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93864ab3bc2177d9eb8da2b29142c672213b3fca4d7af04488db39f9bb82e79)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cf7ab83e3a4bf4af57953126e1ab903c3b3e11d8f20de415c3d48c39b6eb397)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05d66daaaa79fb13d75f40d40ac183c1c9edfa7929321036f435cb1b3fadc654)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e1a4a258ad815fd91aa6d8546342b3c9602eef45a43ba62208db2e87f6b51a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagSetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a671dda3624c262a7a72b20d7e0e6fc72c5a9640a576062a6dab50091df5945)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEc2TagFilter")
    def put_ec2_tag_filter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b48ee2a88ccd2f0bc18791ebd27c6d3a6e976df94958903690129d65dfba192e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2TagFilter", [value]))

    @jsii.member(jsii_name="resetEc2TagFilter")
    def reset_ec2_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2TagFilter", []))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilter")
    def ec2_tag_filter(self) -> CodedeployDeploymentGroupEc2TagSetEc2TagFilterList:
        return typing.cast(CodedeployDeploymentGroupEc2TagSetEc2TagFilterList, jsii.get(self, "ec2TagFilter"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilterInput")
    def ec2_tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]], jsii.get(self, "ec2TagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f65bdfcbcd7a34a4af1e7d00b0f922c15106daab76a5f1d1339ca8b5f1adb6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEcsService",
    jsii_struct_bases=[],
    name_mapping={"cluster_name": "clusterName", "service_name": "serviceName"},
)
class CodedeployDeploymentGroupEcsService:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#cluster_name CodedeployDeploymentGroup#cluster_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_name CodedeployDeploymentGroup#service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2b47eedea7ba1203c95fefe93096a8810ae2c4fcd14211ccf9b7501883dcdd2)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "service_name": service_name,
        }

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#cluster_name CodedeployDeploymentGroup#cluster_name}.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_name CodedeployDeploymentGroup#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEcsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupEcsServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEcsServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55617947dac33a1ad0b633a7802b02e5c84d64ea172195a402c5842a9f561fb8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c241df8be82798277c91bb2aca24b09b6db119a8d1beea969c934d31f0a39f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b2190f15ade6435d2bcfa1e315eb09af4fc4d2175631a856cdbe24296b9174)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodedeployDeploymentGroupEcsService]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupEcsService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupEcsService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9fa178e612c9dedaf25278c4b6e4f5bd2e272c5fe903e62cbffc0f23001f5e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfo",
    jsii_struct_bases=[],
    name_mapping={
        "elb_info": "elbInfo",
        "target_group_info": "targetGroupInfo",
        "target_group_pair_info": "targetGroupPairInfo",
    },
)
class CodedeployDeploymentGroupLoadBalancerInfo:
    def __init__(
        self,
        *,
        elb_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoElbInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_group_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_group_pair_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_info: elb_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#elb_info CodedeployDeploymentGroup#elb_info}
        :param target_group_info: target_group_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_info CodedeployDeploymentGroup#target_group_info}
        :param target_group_pair_info: target_group_pair_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_pair_info CodedeployDeploymentGroup#target_group_pair_info}
        '''
        if isinstance(target_group_pair_info, dict):
            target_group_pair_info = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo(**target_group_pair_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__addbad8f4bce35632020654f28a52fbff3d9b18866c2c9f9fcbd6ded02bd9543)
            check_type(argname="argument elb_info", value=elb_info, expected_type=type_hints["elb_info"])
            check_type(argname="argument target_group_info", value=target_group_info, expected_type=type_hints["target_group_info"])
            check_type(argname="argument target_group_pair_info", value=target_group_pair_info, expected_type=type_hints["target_group_pair_info"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_info is not None:
            self._values["elb_info"] = elb_info
        if target_group_info is not None:
            self._values["target_group_info"] = target_group_info
        if target_group_pair_info is not None:
            self._values["target_group_pair_info"] = target_group_pair_info

    @builtins.property
    def elb_info(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoElbInfo"]]]:
        '''elb_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#elb_info CodedeployDeploymentGroup#elb_info}
        '''
        result = self._values.get("elb_info")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoElbInfo"]]], result)

    @builtins.property
    def target_group_info(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]]:
        '''target_group_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_info CodedeployDeploymentGroup#target_group_info}
        '''
        result = self._values.get("target_group_info")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]], result)

    @builtins.property
    def target_group_pair_info(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"]:
        '''target_group_pair_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_pair_info CodedeployDeploymentGroup#target_group_pair_info}
        '''
        result = self._values.get("target_group_pair_info")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoElbInfo",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CodedeployDeploymentGroupLoadBalancerInfoElbInfo:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d4b06bd0791df4e9532afc8b89151f0f5ecbfe7f54b044f2d0c1221f7dd722)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoElbInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoElbInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoElbInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11615ebc884024a225565d37c94ecbd125e089a32f72073323a823c983c659a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1565609473358180ab7ca4d3caa2751305561a1993d48062ebf5cfcfc691e276)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a0853d181ed2c854fd9be877343a8e05439db14aa6f6c88afc841a8a4932e01)
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
            type_hints = typing.get_type_hints(_typecheckingstub__700d6d8a5200e08c6fead0f79b53f72b2a50d4d7c76e60416fd065bdd82e4529)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddaa57403fdb4dacb5a86312c873ff5f8f282c02a3f78f7399fd61f7fba0342d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351d61ce7b15f47c2ff617a213cb549a29c65292926a0d46b550adab5a8e05a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__863e8de0e055795e3f4f9ddbfe075de9df6bf51220c28effc33a7ca3216ceaf2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f56d34cef77bc7ac9e4af5cc45754ec2a6a0827100b338e58ef8ef9e303fa8f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f9b95cf899f5801ce7a6008b8451c7b405ebca9a70d5896c8d386c1d95ee2ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e5fdb6d69e54f49313ff5e1ff6226f7cde8e78b6923c5e22a3622e88e5c2d76)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putElbInfo")
    def put_elb_info(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe5a5dfa36dd17613ca7369fd61d3a9c2cffb877eda213b6cd08a8e3658d6e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putElbInfo", [value]))

    @jsii.member(jsii_name="putTargetGroupInfo")
    def put_target_group_info(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888122afae2c987fcdf3e1da784c62a548aa9d575ad1189b944b41cbd4de49ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGroupInfo", [value]))

    @jsii.member(jsii_name="putTargetGroupPairInfo")
    def put_target_group_pair_info(
        self,
        *,
        prod_traffic_route: typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute", typing.Dict[builtins.str, typing.Any]],
        target_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup", typing.Dict[builtins.str, typing.Any]]]],
        test_traffic_route: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param prod_traffic_route: prod_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#prod_traffic_route CodedeployDeploymentGroup#prod_traffic_route}
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group CodedeployDeploymentGroup#target_group}
        :param test_traffic_route: test_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#test_traffic_route CodedeployDeploymentGroup#test_traffic_route}
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo(
            prod_traffic_route=prod_traffic_route,
            target_group=target_group,
            test_traffic_route=test_traffic_route,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetGroupPairInfo", [value]))

    @jsii.member(jsii_name="resetElbInfo")
    def reset_elb_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElbInfo", []))

    @jsii.member(jsii_name="resetTargetGroupInfo")
    def reset_target_group_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupInfo", []))

    @jsii.member(jsii_name="resetTargetGroupPairInfo")
    def reset_target_group_pair_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupPairInfo", []))

    @builtins.property
    @jsii.member(jsii_name="elbInfo")
    def elb_info(self) -> CodedeployDeploymentGroupLoadBalancerInfoElbInfoList:
        return typing.cast(CodedeployDeploymentGroupLoadBalancerInfoElbInfoList, jsii.get(self, "elbInfo"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInfo")
    def target_group_info(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList", jsii.get(self, "targetGroupInfo"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupPairInfo")
    def target_group_pair_info(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference", jsii.get(self, "targetGroupPairInfo"))

    @builtins.property
    @jsii.member(jsii_name="elbInfoInput")
    def elb_info_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]], jsii.get(self, "elbInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInfoInput")
    def target_group_info_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]], jsii.get(self, "targetGroupInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupPairInfoInput")
    def target_group_pair_info_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"], jsii.get(self, "targetGroupPairInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c2418ab7594c023c6d42c128337f9b828d64c7d54279b7b4b1469d1780c1ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16355d417d0efb4c8e672324e7671d80401a84f0d2e72a4331189d272d4c7eeb)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c686557bbf35b73d63315d9437b687589521979c52bdc5da490877cffc3bf3f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2541a67b9ea3585c211fa29ad9633f749e0e5d10db50e011b9d3a84b11ad99)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45dcdcef547e0658964151760b87b55653493b91867ada14865a5e2814f7c38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3161d7409c8a1abdd425cf92156d53e5a34dee85e24aeb1b330ac88576aa4b8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d4a67f18f360f17e8e26d3fad7e97c6eae181c80906ea14bf6df3ddcd38aaa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c7efab2c25a91d7e2618bd5027f5c4b26ed6eb5857b0dc070df03c5f3116c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a21c57ec38d3271fb2fcc63b7ce6e88ab901b47269032dda0bda50f3d5d15d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9b3fb8c200bd122d3de6b9c754f1c8718408d4e1b1a33e49f798f75377e7a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e44e6b81598fc272fdfcc9a3bab270b24f0a39ba889c92661293a2363a8d18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo",
    jsii_struct_bases=[],
    name_mapping={
        "prod_traffic_route": "prodTrafficRoute",
        "target_group": "targetGroup",
        "test_traffic_route": "testTrafficRoute",
    },
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo:
    def __init__(
        self,
        *,
        prod_traffic_route: typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute", typing.Dict[builtins.str, typing.Any]],
        target_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup", typing.Dict[builtins.str, typing.Any]]]],
        test_traffic_route: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param prod_traffic_route: prod_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#prod_traffic_route CodedeployDeploymentGroup#prod_traffic_route}
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group CodedeployDeploymentGroup#target_group}
        :param test_traffic_route: test_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#test_traffic_route CodedeployDeploymentGroup#test_traffic_route}
        '''
        if isinstance(prod_traffic_route, dict):
            prod_traffic_route = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(**prod_traffic_route)
        if isinstance(test_traffic_route, dict):
            test_traffic_route = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(**test_traffic_route)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6abf8fe43a067295bb66b87ba4687b5969f9fa1d0d31e015e997bafbafe26302)
            check_type(argname="argument prod_traffic_route", value=prod_traffic_route, expected_type=type_hints["prod_traffic_route"])
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
            check_type(argname="argument test_traffic_route", value=test_traffic_route, expected_type=type_hints["test_traffic_route"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prod_traffic_route": prod_traffic_route,
            "target_group": target_group,
        }
        if test_traffic_route is not None:
            self._values["test_traffic_route"] = test_traffic_route

    @builtins.property
    def prod_traffic_route(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute":
        '''prod_traffic_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#prod_traffic_route CodedeployDeploymentGroup#prod_traffic_route}
        '''
        result = self._values.get("prod_traffic_route")
        assert result is not None, "Required property 'prod_traffic_route' is missing"
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute", result)

    @builtins.property
    def target_group(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]]:
        '''target_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group CodedeployDeploymentGroup#target_group}
        '''
        result = self._values.get("target_group")
        assert result is not None, "Required property 'target_group' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]], result)

    @builtins.property
    def test_traffic_route(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"]:
        '''test_traffic_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#test_traffic_route CodedeployDeploymentGroup#test_traffic_route}
        '''
        result = self._values.get("test_traffic_route")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__780b7375f976dc390c218422a84c4d9ae06cda782462dc733c196b95d0c3aedc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProdTrafficRoute")
    def put_prod_traffic_route(
        self,
        *,
        listener_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(
            listener_arns=listener_arns
        )

        return typing.cast(None, jsii.invoke(self, "putProdTrafficRoute", [value]))

    @jsii.member(jsii_name="putTargetGroup")
    def put_target_group(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2c65a7d48459abae63e1b8185f72206a4a2764d728262aff6409c83c9d8c60e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGroup", [value]))

    @jsii.member(jsii_name="putTestTrafficRoute")
    def put_test_traffic_route(
        self,
        *,
        listener_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(
            listener_arns=listener_arns
        )

        return typing.cast(None, jsii.invoke(self, "putTestTrafficRoute", [value]))

    @jsii.member(jsii_name="resetTestTrafficRoute")
    def reset_test_traffic_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestTrafficRoute", []))

    @builtins.property
    @jsii.member(jsii_name="prodTrafficRoute")
    def prod_traffic_route(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference", jsii.get(self, "prodTrafficRoute"))

    @builtins.property
    @jsii.member(jsii_name="targetGroup")
    def target_group(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList", jsii.get(self, "targetGroup"))

    @builtins.property
    @jsii.member(jsii_name="testTrafficRoute")
    def test_traffic_route(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference", jsii.get(self, "testTrafficRoute"))

    @builtins.property
    @jsii.member(jsii_name="prodTrafficRouteInput")
    def prod_traffic_route_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute"], jsii.get(self, "prodTrafficRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInput")
    def target_group_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]]], jsii.get(self, "targetGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="testTrafficRouteInput")
    def test_traffic_route_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"], jsii.get(self, "testTrafficRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3011d9dfdd88c94113524a02963688f3f45065aab65f09b15f511bcfda5787a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute",
    jsii_struct_bases=[],
    name_mapping={"listener_arns": "listenerArns"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute:
    def __init__(self, *, listener_arns: typing.Sequence[builtins.str]) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbaf64627f97417ef4e23b77984eeef220c6af702bd1b3c5e01138bafd2f111)
            check_type(argname="argument listener_arns", value=listener_arns, expected_type=type_hints["listener_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_arns": listener_arns,
        }

    @builtins.property
    def listener_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.'''
        result = self._values.get("listener_arns")
        assert result is not None, "Required property 'listener_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9eca6f6a2b8c8fb5472df0add3248946737d2795585baf837fbd357d0d4b816d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="listenerArnsInput")
    def listener_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listenerArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerArns")
    def listener_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listenerArns"))

    @listener_arns.setter
    def listener_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8e7b8c5da188a0a566cbabb55b4939a636118c13ea311f165795b7d3acb7cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445aa1dc0d79d04e7a489c134c80b202d0b4df28f340dce77a047c786c213aef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d32f786e91314e656b86169be4fc2dc244acad531705ac7a27faeed4feaa0c38)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0455c50194e0ad05571157e87db7a80616c501475010ee08840256059346e9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69634c045bf4333e320f9d27e51f93fc4cfedfe7c03e3c71387ff6de0b4d641)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__492cfaf5a2ff3b85b1c6f9bb1b117df107d70faff4d6a1b0998236942979a5f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9df330bc4a027dfb8bc18bae020911fb2d6c696ad66f7f3a86f2226efdd8e699)
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
            type_hints = typing.get_type_hints(_typecheckingstub__619e641b69955f10219da1b971eaff29a9e2fbd15be465cfa47db8d154f934ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b1e27c3d2e8b7c0f519704b0b1565667169ed7e0afac30efc826e8404bc92d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__616309e9f855fe4568fb398b8e6d41c4e090966b98cd9cd10f2c4ca93311a595)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea9b1fa6d5165aeadc2169f172e6498e17c90a17e6658a5f239898bb70d1bbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355e58639a591d49e52156f2b0cd6c3f21506c86f0ce1389fce7d906ff359344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute",
    jsii_struct_bases=[],
    name_mapping={"listener_arns": "listenerArns"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute:
    def __init__(self, *, listener_arns: typing.Sequence[builtins.str]) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50d234d3c8770920390ad204809fab7826881ad09e651e20ce172270854e5b62)
            check_type(argname="argument listener_arns", value=listener_arns, expected_type=type_hints["listener_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_arns": listener_arns,
        }

    @builtins.property
    def listener_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.'''
        result = self._values.get("listener_arns")
        assert result is not None, "Required property 'listener_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b93bd4f9a03790bfe1a5d28935644515d737cede1cbbdbaba0bfb7edfa692881)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="listenerArnsInput")
    def listener_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listenerArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerArns")
    def listener_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listenerArns"))

    @listener_arns.setter
    def listener_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14432fcd289b698ae7f19f461f3cf20a2ba53b2e754ec699df4e26d89c49eaf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd80215bc68069d28f8b213646741121cf6cd9db883b9e9176dd600c33568f81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupOnPremisesInstanceTagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CodedeployDeploymentGroupOnPremisesInstanceTagFilter:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd65d61875003d8a7efa7335bcca0d091cea8c18696935390f183dac98113ad)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupOnPremisesInstanceTagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupOnPremisesInstanceTagFilterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupOnPremisesInstanceTagFilterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__81aaab63d50c8d6eedee09cfa3f20a785639a67afb618dd98bdab58255f13925)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ebfa28bf660885644bcc1a5cb3fc3431aa0281d05dcd06fa7f4ea9cf9370f5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f1d7efc632e6c8a4d3c863eae7143a4c2a2b30351ec8993af38e6153e7abb5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__62719c1a6753d725bb4cb774217449ddd0c792f087e30b3182085a67507bba85)
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
            type_hints = typing.get_type_hints(_typecheckingstub__79f2d72e3a25c37fc6b36943e394d6e27d138a888013fcb60268d399cf32a3ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e86bce0266a5bca4a9819c8f2573aa974ff9864ea495de576baa6069d558e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a5a7280cdebb6d59c0a4c05a46643dd239b33018e88232c07f1fb92188ba9a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5593c79f2463a024be89b03b417763713f2fa4bb4ae2d27a17425456467292d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44ed21b0a157e07016fc6d2ba8482f8434bdef04d1d2dd56b8225204f6c4e095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d619152d694269a572ebfa3ff331479bb704491f332ff5aa49227fe0fece9b95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e9ae9ae722d17d6d3eb1ef11434dc5b7bdfba048c160c4ad0652ce13202aa6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupTriggerConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "trigger_events": "triggerEvents",
        "trigger_name": "triggerName",
        "trigger_target_arn": "triggerTargetArn",
    },
)
class CodedeployDeploymentGroupTriggerConfiguration:
    def __init__(
        self,
        *,
        trigger_events: typing.Sequence[builtins.str],
        trigger_name: builtins.str,
        trigger_target_arn: builtins.str,
    ) -> None:
        '''
        :param trigger_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_events CodedeployDeploymentGroup#trigger_events}.
        :param trigger_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_name CodedeployDeploymentGroup#trigger_name}.
        :param trigger_target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_target_arn CodedeployDeploymentGroup#trigger_target_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8ddd661e6b0d86970c3a52bc4aa7a4cc90a51cfd4568f2aeb6866c46167468)
            check_type(argname="argument trigger_events", value=trigger_events, expected_type=type_hints["trigger_events"])
            check_type(argname="argument trigger_name", value=trigger_name, expected_type=type_hints["trigger_name"])
            check_type(argname="argument trigger_target_arn", value=trigger_target_arn, expected_type=type_hints["trigger_target_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trigger_events": trigger_events,
            "trigger_name": trigger_name,
            "trigger_target_arn": trigger_target_arn,
        }

    @builtins.property
    def trigger_events(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_events CodedeployDeploymentGroup#trigger_events}.'''
        result = self._values.get("trigger_events")
        assert result is not None, "Required property 'trigger_events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def trigger_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_name CodedeployDeploymentGroup#trigger_name}.'''
        result = self._values.get("trigger_name")
        assert result is not None, "Required property 'trigger_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_target_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_target_arn CodedeployDeploymentGroup#trigger_target_arn}.'''
        result = self._values.get("trigger_target_arn")
        assert result is not None, "Required property 'trigger_target_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupTriggerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupTriggerConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupTriggerConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cff884cb2bdb00fe8ebf3b6f7ebd7982932b31f5df3b24c828f11088f13ee1d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupTriggerConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f24ad72af78750c912c10ab61d5e2781e30d6c85751b45798c6f072806e9b55)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupTriggerConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ecba6d87d06c6a6abf72fe3bd063b208a1b512ded9c857578c124bf7c5b2d08)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38941b5557e29b3f75250226e9285b02f6012e27709fce8063cf2887676559b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__927461a001667ec257be0a1b6ddc3cb2d636e05b214d91f29c45f89592acaadf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0d2a003165135ed9bb0fe04e84954b7306969c313a30335901ce1c821fe69c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupTriggerConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.codedeployDeploymentGroup.CodedeployDeploymentGroupTriggerConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f26d64c2fd52967ca9d6f89ac3cf6b3bec6d23f38989a61fd6803ef02a8f800)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="triggerEventsInput")
    def trigger_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "triggerEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerNameInput")
    def trigger_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerTargetArnInput")
    def trigger_target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerTargetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerEvents")
    def trigger_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "triggerEvents"))

    @trigger_events.setter
    def trigger_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e122aef0ce192ffa3653771b13a62a8a8dfcadc725224604cb1d526944e874e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerEvents", value)

    @builtins.property
    @jsii.member(jsii_name="triggerName")
    def trigger_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerName"))

    @trigger_name.setter
    def trigger_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cb6fd8b1d05e1a20a1c4e677c3df4e73e961962f5fea2623cc1297f384fbd85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerName", value)

    @builtins.property
    @jsii.member(jsii_name="triggerTargetArn")
    def trigger_target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerTargetArn"))

    @trigger_target_arn.setter
    def trigger_target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8afbdcbedd2bc55171f28e1d998a7c968c5ad276731017802a41f1fe1fe1500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8d50aa107526c01f596277be956bf2dd552155cc925c7dfa3b9dddad885a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodedeployDeploymentGroup",
    "CodedeployDeploymentGroupAlarmConfiguration",
    "CodedeployDeploymentGroupAlarmConfigurationOutputReference",
    "CodedeployDeploymentGroupAutoRollbackConfiguration",
    "CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfig",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference",
    "CodedeployDeploymentGroupConfig",
    "CodedeployDeploymentGroupDeploymentStyle",
    "CodedeployDeploymentGroupDeploymentStyleOutputReference",
    "CodedeployDeploymentGroupEc2TagFilter",
    "CodedeployDeploymentGroupEc2TagFilterList",
    "CodedeployDeploymentGroupEc2TagFilterOutputReference",
    "CodedeployDeploymentGroupEc2TagSet",
    "CodedeployDeploymentGroupEc2TagSetEc2TagFilter",
    "CodedeployDeploymentGroupEc2TagSetEc2TagFilterList",
    "CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference",
    "CodedeployDeploymentGroupEc2TagSetList",
    "CodedeployDeploymentGroupEc2TagSetOutputReference",
    "CodedeployDeploymentGroupEcsService",
    "CodedeployDeploymentGroupEcsServiceOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoElbInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoElbInfoList",
    "CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference",
    "CodedeployDeploymentGroupOnPremisesInstanceTagFilter",
    "CodedeployDeploymentGroupOnPremisesInstanceTagFilterList",
    "CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference",
    "CodedeployDeploymentGroupTriggerConfiguration",
    "CodedeployDeploymentGroupTriggerConfigurationList",
    "CodedeployDeploymentGroupTriggerConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__6a51cdfc03044b15048acd5fc253ab5adebe12adc94a1279db346580da69b08d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    app_name: builtins.str,
    deployment_group_name: builtins.str,
    service_role_arn: builtins.str,
    alarm_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAlarmConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_rollback_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAutoRollbackConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    blue_green_deployment_config: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
    deployment_style: typing.Optional[typing.Union[CodedeployDeploymentGroupDeploymentStyle, typing.Dict[builtins.str, typing.Any]]] = None,
    ec2_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ec2_tag_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSet, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ecs_service: typing.Optional[typing.Union[CodedeployDeploymentGroupEcsService, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    load_balancer_info: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    on_premises_instance_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    trigger_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__be139ef89e27305ef54753085c08f5b09accd2a0fe432f81c313967a07becbcb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b62d1e1f4d5ff829dbf571dc56ae0d412882d8566ec064d53438beb2ba04206(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSet, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd496324cab5fa2bc61e748e22d74a859718bca9fb54616c12a40cf0b5c20c0a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd9a054425ae54971157fe66ed06e4a2b90e3c6a93ade7e6422c4af90b38f60d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a9a97dd0daca96a62852f6a4f529f8a497bda322a33f2ffb1253a1dce1f777f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edd51dc82dfecf8fb35205e2a419528fc3d63c06b35519ca199b67f17000012d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6492f80886aa77494b45ed1b1287b6158806156145911aad6475b3d26283f50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588d1fc5c0f4b044af3bc6519f0145b4bf1da7471eaac357826dacc44bcfee85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738f8d0469938a18c774b4adf6778013cab39ac7aa467d304e52698443228220(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355348322428cd976957ff055f1a275b0ce785776fa8e1779d5e8f1f7c0af026(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea97f2d9af84cf70bd3ca15f1ca271b40559689114bc0353cbef8a9235fa985(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61be878e4b78f740a1b2845d1c9c30598a8fa67a322a002fe879afa4f0c994d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ecf6c6a3f93f00463abab8ca180aa51b7cafe98722ac1c183bfa90372bd5e2(
    *,
    alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfe81920254ba7a3ef4d61181f5df448e3e842e1c0e3e63605035d14501a6947(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc603ee27ce18eb6576851b12d9abcbc74d201bacb8fd46d81f386fe938a554e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2156143618edafaf38fd463fee59f012a86d21895a5ef1d1da5c14164255b27(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c10476108591e14fd58777f4390aa39d5859e06fc4a73908e127c1b4dddcfd5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf8fdd29ca7a513eee6b6b90a73c28a0104b7f713bf74222e69f41d90aae9410(
    value: typing.Optional[CodedeployDeploymentGroupAlarmConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ecae8b42597023d25f3486f36bb962a73b40c37564208af454fa09631b5583(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a038ca8a7c2800009a7e96b6a1d9bca48584c19f7c1fba6556f7adfe29f6b35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fb153baf84574ae987797ad78cf4af8cf8a57de9bc96fd225e8caafc05c4eba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d593702e0f1d1d417867afb43d2b353af1044907eb22c6f37ba6804985c4ce88(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699608825ba0eb3423625611c83ed065a6b66afaccdffd2cb973e788ba340412(
    value: typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cfae2ebbaf85ea96608d68589b2a8a6c94be88d8eb45093f2d1e69be4e7d021(
    *,
    deployment_ready_option: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption, typing.Dict[builtins.str, typing.Any]]] = None,
    green_fleet_provisioning_option: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption, typing.Dict[builtins.str, typing.Any]]] = None,
    terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d745b8f19e9b07194abcdaa553c7801f9720e380b7f08f79a4292528bd98271(
    *,
    action_on_timeout: typing.Optional[builtins.str] = None,
    wait_time_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__246249807389f65d4a1203886ef6612cbf6aec13c2e1360b8dc3145cd761fc2b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2fabdf03892ba27256fb30f1bd07e24b4af7501a2bba54d215e18194a77e18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff4d617ece90dd18259d92de642e7e84994d64c58c2ecf5af76bcc2990a2e944(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee5060141e0d4daa3e168dbcc233431debeb2f6fd566ade24636f03ef88473ef(
    value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9123b656f15fcd4d6eb00f9b5ff9412650b8aed94d868592264600e351f6270(
    *,
    action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f5e1c153826f9b0f8d07cf3cd1345fb6bb223d96ec03bb49310c5295c3c1215(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7a5009c74f220a9456b9bfc609f15e51a7a1e4a521eff0616bc3d02857ebff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f6157f4e3b1c07a65658bfafa17816d6cfff0319bcd23a9b2af32d602c4f5d(
    value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec006e660114f4e22eaf9cf73eb4a79ea594aa15e2722f2ac1c04c9a7311078d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262019f5f73bbe2e02e88d5080686abd88a9ee25ace7357a3038a175e6f9619d(
    value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813fb4b5d0d11c08648e14e21aa489eb1f52f35887bf6c2f3276eb9769bdd084(
    *,
    action: typing.Optional[builtins.str] = None,
    termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b895445cf0d437c0dfbb844f6e4355f29cbce6c1b05e272cf9dda91e52c24c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64fa818deda9f777a77a3e78f3fc520a388d209748f0d09bb59ea89ef460003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e379e865f137eb26f9a805a798fbe58f06c20f3f6d6e79ab240521cfa3a288(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__103dd36b285947a02cfd35c23534cbf2165196b7461ec6186c724f7bb3decf0e(
    value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93088c6e0ca80958f5ad1a88d417be5c9481dd4a7ce9fd28824bd92690947400(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    app_name: builtins.str,
    deployment_group_name: builtins.str,
    service_role_arn: builtins.str,
    alarm_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAlarmConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_rollback_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAutoRollbackConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    blue_green_deployment_config: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
    deployment_style: typing.Optional[typing.Union[CodedeployDeploymentGroupDeploymentStyle, typing.Dict[builtins.str, typing.Any]]] = None,
    ec2_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ec2_tag_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSet, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ecs_service: typing.Optional[typing.Union[CodedeployDeploymentGroupEcsService, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    load_balancer_info: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    on_premises_instance_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    trigger_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e98b44fcff11257a6950cb457f863b133073ed55b2dbcd953fdf2be006dff9f(
    *,
    deployment_option: typing.Optional[builtins.str] = None,
    deployment_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5171d672aafcefa4d49e46f052e2d1745842339dada465f7616b1ff18382d5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c6c138cbbd3d51cfba1a669e381d4b0bc126e3f3984b310bc9b96b618a26ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76c3572fcc99b2087a43208b6adf0aede0779e98adc0547462e353d589632756(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34a5b6cbc13a18bb73ac27a44fb15ffa2bba36777daa28a2b94c2b4dfaff0f3(
    value: typing.Optional[CodedeployDeploymentGroupDeploymentStyle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c292b2bbe2497a3901bd7af6bc14c9ac0965b2d160381d198ac2d9417d53336a(
    *,
    key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b36b5443a51c3f8aa611d51b6349d549b3483e46d3b64f90891cc29ab3a51f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f6de7bae10dd491bc6f23e81ff5145707db60a2640bf2838d44cd6083a8a98(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765e9fc84be1513d1d3e04d36623c143d6708b1265473772a3dba6ca8809bcef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a1c57fd06bfd379cd2a24dae1b457f3497400292cf244d7032b176223b2c9f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3441fceed5d6b558b5f049ff77428810a11b0585275002d042dde9653924842e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069c3971ca97cf0e220712cfac84b8e81b92232c5f58317847bb4f36be1fe4b1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c53fcb9bdc8ec7a5823b7c412bd15b29919fbbaa8b741f79c71b79bd8c9482(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b238855826892db5ceb893c1b62133e37e68fdf16c11dc207b10df80602ebaa4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ebc6ec99ea132618954526f2acb3be835aad3473877e17b23e43d716d766af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca0cb1291f68300cc6e42c16a566d72dde49fd946af23dc95d7b45b618860b86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6188cd60accbffcb94b4954b2ce67231e1acd01b4effed6a16a5d5c5e076da(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318b05de0d2ec5a79b50571dc034c0c41cbeab7f241bacdb4f5b5cfc424dc3ba(
    *,
    ec2_tag_filter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d30c1905187a12773653d48f4d17c659d52005e5fc347e5ee3115dde06b59b6(
    *,
    key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6941bdb8c77a7cb28c7fd411a5326eb205faf1e5e0a86e9535f181c2c2bac5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da38943f078ffc1b41abafc98ce369d95d4f26162e02273089375d009c9fc420(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff301c4d8112412514b185cbcd384d1e200d47099415f1f0694f248a3fbf4d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e95bf5a25bc11ff4b315c399cce76ba52f7065399c7d93ddf653c4c7eafece(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__179388225f68319c07fef29cf5385de7f9ea2ef8e2ab7ffae6fd64d521526cf8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5366975b81a94977494ef35e32d9810cea8d4a2007b4263863044f84e5fa1082(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29da1a20ce680a29ba6802fc614b62f0e560aba06997f65fa5eb426e00ff6679(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d58f16a55573825c032203ed02e5b39318b8a09fd65b90492789fb1006eb42e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b153ae40f692ee4b12ad5f72297ffb0901958d135a1757e91853795709508bc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e322e098c9a612a15bcc5d60fef03a01833d65d08710880fdc13c0e17ed3941c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8077c5667693c1980650cc8e2d238fc075d6396a41c239ba2afe4cc73db7b71d(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dc1180103ec102ce24a4fe3dc028149929004fc5a1f1733cf241d739d417a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ade9e16837d6002497ea768308af93d90836c6e42505a6d9026f798d137211(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93864ab3bc2177d9eb8da2b29142c672213b3fca4d7af04488db39f9bb82e79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf7ab83e3a4bf4af57953126e1ab903c3b3e11d8f20de415c3d48c39b6eb397(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d66daaaa79fb13d75f40d40ac183c1c9edfa7929321036f435cb1b3fadc654(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e1a4a258ad815fd91aa6d8546342b3c9602eef45a43ba62208db2e87f6b51a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a671dda3624c262a7a72b20d7e0e6fc72c5a9640a576062a6dab50091df5945(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48ee2a88ccd2f0bc18791ebd27c6d3a6e976df94958903690129d65dfba192e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f65bdfcbcd7a34a4af1e7d00b0f922c15106daab76a5f1d1339ca8b5f1adb6a(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2b47eedea7ba1203c95fefe93096a8810ae2c4fcd14211ccf9b7501883dcdd2(
    *,
    cluster_name: builtins.str,
    service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55617947dac33a1ad0b633a7802b02e5c84d64ea172195a402c5842a9f561fb8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c241df8be82798277c91bb2aca24b09b6db119a8d1beea969c934d31f0a39f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b2190f15ade6435d2bcfa1e315eb09af4fc4d2175631a856cdbe24296b9174(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9fa178e612c9dedaf25278c4b6e4f5bd2e272c5fe903e62cbffc0f23001f5e7(
    value: typing.Optional[CodedeployDeploymentGroupEcsService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__addbad8f4bce35632020654f28a52fbff3d9b18866c2c9f9fcbd6ded02bd9543(
    *,
    elb_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_group_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_group_pair_info: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d4b06bd0791df4e9532afc8b89151f0f5ecbfe7f54b044f2d0c1221f7dd722(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11615ebc884024a225565d37c94ecbd125e089a32f72073323a823c983c659a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1565609473358180ab7ca4d3caa2751305561a1993d48062ebf5cfcfc691e276(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a0853d181ed2c854fd9be877343a8e05439db14aa6f6c88afc841a8a4932e01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__700d6d8a5200e08c6fead0f79b53f72b2a50d4d7c76e60416fd065bdd82e4529(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddaa57403fdb4dacb5a86312c873ff5f8f282c02a3f78f7399fd61f7fba0342d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351d61ce7b15f47c2ff617a213cb549a29c65292926a0d46b550adab5a8e05a8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863e8de0e055795e3f4f9ddbfe075de9df6bf51220c28effc33a7ca3216ceaf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f56d34cef77bc7ac9e4af5cc45754ec2a6a0827100b338e58ef8ef9e303fa8f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f9b95cf899f5801ce7a6008b8451c7b405ebca9a70d5896c8d386c1d95ee2ac(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5fdb6d69e54f49313ff5e1ff6226f7cde8e78b6923c5e22a3622e88e5c2d76(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe5a5dfa36dd17613ca7369fd61d3a9c2cffb877eda213b6cd08a8e3658d6e0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888122afae2c987fcdf3e1da784c62a548aa9d575ad1189b944b41cbd4de49ee(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2418ab7594c023c6d42c128337f9b828d64c7d54279b7b4b1469d1780c1ce7(
    value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16355d417d0efb4c8e672324e7671d80401a84f0d2e72a4331189d272d4c7eeb(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c686557bbf35b73d63315d9437b687589521979c52bdc5da490877cffc3bf3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2541a67b9ea3585c211fa29ad9633f749e0e5d10db50e011b9d3a84b11ad99(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45dcdcef547e0658964151760b87b55653493b91867ada14865a5e2814f7c38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3161d7409c8a1abdd425cf92156d53e5a34dee85e24aeb1b330ac88576aa4b8f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d4a67f18f360f17e8e26d3fad7e97c6eae181c80906ea14bf6df3ddcd38aaa1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c7efab2c25a91d7e2618bd5027f5c4b26ed6eb5857b0dc070df03c5f3116c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a21c57ec38d3271fb2fcc63b7ce6e88ab901b47269032dda0bda50f3d5d15d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9b3fb8c200bd122d3de6b9c754f1c8718408d4e1b1a33e49f798f75377e7a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e44e6b81598fc272fdfcc9a3bab270b24f0a39ba889c92661293a2363a8d18(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6abf8fe43a067295bb66b87ba4687b5969f9fa1d0d31e015e997bafbafe26302(
    *,
    prod_traffic_route: typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute, typing.Dict[builtins.str, typing.Any]],
    target_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, typing.Dict[builtins.str, typing.Any]]]],
    test_traffic_route: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__780b7375f976dc390c218422a84c4d9ae06cda782462dc733c196b95d0c3aedc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2c65a7d48459abae63e1b8185f72206a4a2764d728262aff6409c83c9d8c60e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3011d9dfdd88c94113524a02963688f3f45065aab65f09b15f511bcfda5787a7(
    value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbaf64627f97417ef4e23b77984eeef220c6af702bd1b3c5e01138bafd2f111(
    *,
    listener_arns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eca6f6a2b8c8fb5472df0add3248946737d2795585baf837fbd357d0d4b816d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8e7b8c5da188a0a566cbabb55b4939a636118c13ea311f165795b7d3acb7cba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445aa1dc0d79d04e7a489c134c80b202d0b4df28f340dce77a047c786c213aef(
    value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32f786e91314e656b86169be4fc2dc244acad531705ac7a27faeed4feaa0c38(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0455c50194e0ad05571157e87db7a80616c501475010ee08840256059346e9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69634c045bf4333e320f9d27e51f93fc4cfedfe7c03e3c71387ff6de0b4d641(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__492cfaf5a2ff3b85b1c6f9bb1b117df107d70faff4d6a1b0998236942979a5f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9df330bc4a027dfb8bc18bae020911fb2d6c696ad66f7f3a86f2226efdd8e699(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619e641b69955f10219da1b971eaff29a9e2fbd15be465cfa47db8d154f934ee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1e27c3d2e8b7c0f519704b0b1565667169ed7e0afac30efc826e8404bc92d7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__616309e9f855fe4568fb398b8e6d41c4e090966b98cd9cd10f2c4ca93311a595(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea9b1fa6d5165aeadc2169f172e6498e17c90a17e6658a5f239898bb70d1bbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355e58639a591d49e52156f2b0cd6c3f21506c86f0ce1389fce7d906ff359344(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50d234d3c8770920390ad204809fab7826881ad09e651e20ce172270854e5b62(
    *,
    listener_arns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b93bd4f9a03790bfe1a5d28935644515d737cede1cbbdbaba0bfb7edfa692881(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14432fcd289b698ae7f19f461f3cf20a2ba53b2e754ec699df4e26d89c49eaf9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd80215bc68069d28f8b213646741121cf6cd9db883b9e9176dd600c33568f81(
    value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd65d61875003d8a7efa7335bcca0d091cea8c18696935390f183dac98113ad(
    *,
    key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81aaab63d50c8d6eedee09cfa3f20a785639a67afb618dd98bdab58255f13925(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ebfa28bf660885644bcc1a5cb3fc3431aa0281d05dcd06fa7f4ea9cf9370f5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f1d7efc632e6c8a4d3c863eae7143a4c2a2b30351ec8993af38e6153e7abb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62719c1a6753d725bb4cb774217449ddd0c792f087e30b3182085a67507bba85(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f2d72e3a25c37fc6b36943e394d6e27d138a888013fcb60268d399cf32a3ea(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e86bce0266a5bca4a9819c8f2573aa974ff9864ea495de576baa6069d558e5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5a7280cdebb6d59c0a4c05a46643dd239b33018e88232c07f1fb92188ba9a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5593c79f2463a024be89b03b417763713f2fa4bb4ae2d27a17425456467292d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ed21b0a157e07016fc6d2ba8482f8434bdef04d1d2dd56b8225204f6c4e095(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d619152d694269a572ebfa3ff331479bb704491f332ff5aa49227fe0fece9b95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9ae9ae722d17d6d3eb1ef11434dc5b7bdfba048c160c4ad0652ce13202aa6a(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8ddd661e6b0d86970c3a52bc4aa7a4cc90a51cfd4568f2aeb6866c46167468(
    *,
    trigger_events: typing.Sequence[builtins.str],
    trigger_name: builtins.str,
    trigger_target_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff884cb2bdb00fe8ebf3b6f7ebd7982932b31f5df3b24c828f11088f13ee1d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f24ad72af78750c912c10ab61d5e2781e30d6c85751b45798c6f072806e9b55(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecba6d87d06c6a6abf72fe3bd063b208a1b512ded9c857578c124bf7c5b2d08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38941b5557e29b3f75250226e9285b02f6012e27709fce8063cf2887676559b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__927461a001667ec257be0a1b6ddc3cb2d636e05b214d91f29c45f89592acaadf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0d2a003165135ed9bb0fe04e84954b7306969c313a30335901ce1c821fe69c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f26d64c2fd52967ca9d6f89ac3cf6b3bec6d23f38989a61fd6803ef02a8f800(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e122aef0ce192ffa3653771b13a62a8a8dfcadc725224604cb1d526944e874e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb6fd8b1d05e1a20a1c4e677c3df4e73e961962f5fea2623cc1297f384fbd85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8afbdcbedd2bc55171f28e1d998a7c968c5ad276731017802a41f1fe1fe1500(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8d50aa107526c01f596277be956bf2dd552155cc925c7dfa3b9dddad885a60(
    value: typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
