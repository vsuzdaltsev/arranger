'''
# `aws_ssm_maintenance_window_task`

Refer to the Terraform Registory for docs: [`aws_ssm_maintenance_window_task`](https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task).
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


class SsmMaintenanceWindowTask(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTask",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task aws_ssm_maintenance_window_task}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTargets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task aws_ssm_maintenance_window_task} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param task_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_arn SsmMaintenanceWindowTask#task_arn}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_type SsmMaintenanceWindowTask#task_type}.
        :param window_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#window_id SsmMaintenanceWindowTask#window_id}.
        :param cutoff_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cutoff_behavior SsmMaintenanceWindowTask#cutoff_behavior}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#description SsmMaintenanceWindowTask#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#id SsmMaintenanceWindowTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_concurrency SsmMaintenanceWindowTask#max_concurrency}.
        :param max_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_errors SsmMaintenanceWindowTask#max_errors}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#priority SsmMaintenanceWindowTask#priority}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#targets SsmMaintenanceWindowTask#targets}
        :param task_invocation_parameters: task_invocation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_invocation_parameters SsmMaintenanceWindowTask#task_invocation_parameters}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c33375b82c96b14e05d47f714c42f91fc3f648ea3af03faaf4cecf7d1bc9a8b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsmMaintenanceWindowTaskConfig(
            task_arn=task_arn,
            task_type=task_type,
            window_id=window_id,
            cutoff_behavior=cutoff_behavior,
            description=description,
            id=id,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            name=name,
            priority=priority,
            service_role_arn=service_role_arn,
            targets=targets,
            task_invocation_parameters=task_invocation_parameters,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTargets")
    def put_targets(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTargets", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b5268983aaa90ae025091363a82cdd9705e3c52bd1417f9a9e8baedeee0b160)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargets", [value]))

    @jsii.member(jsii_name="putTaskInvocationParameters")
    def put_task_invocation_parameters(
        self,
        *,
        automation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        run_command_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        step_functions_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automation_parameters: automation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#automation_parameters SsmMaintenanceWindowTask#automation_parameters}
        :param lambda_parameters: lambda_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#lambda_parameters SsmMaintenanceWindowTask#lambda_parameters}
        :param run_command_parameters: run_command_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#run_command_parameters SsmMaintenanceWindowTask#run_command_parameters}
        :param step_functions_parameters: step_functions_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#step_functions_parameters SsmMaintenanceWindowTask#step_functions_parameters}
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParameters(
            automation_parameters=automation_parameters,
            lambda_parameters=lambda_parameters,
            run_command_parameters=run_command_parameters,
            step_functions_parameters=step_functions_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putTaskInvocationParameters", [value]))

    @jsii.member(jsii_name="resetCutoffBehavior")
    def reset_cutoff_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCutoffBehavior", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxConcurrency")
    def reset_max_concurrency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrency", []))

    @jsii.member(jsii_name="resetMaxErrors")
    def reset_max_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxErrors", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

    @jsii.member(jsii_name="resetTargets")
    def reset_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargets", []))

    @jsii.member(jsii_name="resetTaskInvocationParameters")
    def reset_task_invocation_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskInvocationParameters", []))

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
    @jsii.member(jsii_name="targets")
    def targets(self) -> "SsmMaintenanceWindowTaskTargetsList":
        return typing.cast("SsmMaintenanceWindowTaskTargetsList", jsii.get(self, "targets"))

    @builtins.property
    @jsii.member(jsii_name="taskInvocationParameters")
    def task_invocation_parameters(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference", jsii.get(self, "taskInvocationParameters"))

    @builtins.property
    @jsii.member(jsii_name="windowTaskId")
    def window_task_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowTaskId"))

    @builtins.property
    @jsii.member(jsii_name="cutoffBehaviorInput")
    def cutoff_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cutoffBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxErrorsInput")
    def max_errors_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskArnInput")
    def task_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskArnInput"))

    @builtins.property
    @jsii.member(jsii_name="taskInvocationParametersInput")
    def task_invocation_parameters_input(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"]:
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"], jsii.get(self, "taskInvocationParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="windowIdInput")
    def window_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cutoffBehavior")
    def cutoff_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cutoffBehavior"))

    @cutoff_behavior.setter
    def cutoff_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9340cee7fc04d35b8f325f1aa1a99ac90d3719972c4bdd532f9b8801832a47e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cutoffBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d24d27514b298b9920797283e166e1e0b476f62ae4ac5d6dbba1cda6ad95196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55e59a21cd547d338ba4089072e89392a918e02146e9b9f82a847976067c5de2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d19becb821716a992671cae5f3594f435ae1d801216112bc004a357db15212)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b4cdf122da1fd2333f8ef53013024e93c8ac620370f2f8d810a38723b0bebe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxErrors", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2613511ee3757edab6e75f1837454de3102293dff4c3da6b98ba96c51390b242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa51212dc92c57c065aaf283c3f27c36ed0728d4fcdf772c7bf1b560ff6abeea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e49940537aac5e2b4720ffe66dd26b115e5275b58065dedb026e81a9f9200d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="taskArn")
    def task_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskArn"))

    @task_arn.setter
    def task_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee161fb9cda821d687c442f508a634126e98b8244a7627be24cced7b126472ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskArn", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d7e01558505275d74a8216da6b21f432e8d05714a4fc969d15415dafdac7c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__639497d20c0cda61d5dc925f43d9934528a8bfb326d01c345bd7810980defc21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowId", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "task_arn": "taskArn",
        "task_type": "taskType",
        "window_id": "windowId",
        "cutoff_behavior": "cutoffBehavior",
        "description": "description",
        "id": "id",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "name": "name",
        "priority": "priority",
        "service_role_arn": "serviceRoleArn",
        "targets": "targets",
        "task_invocation_parameters": "taskInvocationParameters",
    },
)
class SsmMaintenanceWindowTaskConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTargets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param task_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_arn SsmMaintenanceWindowTask#task_arn}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_type SsmMaintenanceWindowTask#task_type}.
        :param window_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#window_id SsmMaintenanceWindowTask#window_id}.
        :param cutoff_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cutoff_behavior SsmMaintenanceWindowTask#cutoff_behavior}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#description SsmMaintenanceWindowTask#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#id SsmMaintenanceWindowTask#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_concurrency SsmMaintenanceWindowTask#max_concurrency}.
        :param max_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_errors SsmMaintenanceWindowTask#max_errors}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#priority SsmMaintenanceWindowTask#priority}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#targets SsmMaintenanceWindowTask#targets}
        :param task_invocation_parameters: task_invocation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_invocation_parameters SsmMaintenanceWindowTask#task_invocation_parameters}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(task_invocation_parameters, dict):
            task_invocation_parameters = SsmMaintenanceWindowTaskTaskInvocationParameters(**task_invocation_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1069539fb252ba88963f3e047821523217272d04c38f71677e5caab2e3ce674c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument task_arn", value=task_arn, expected_type=type_hints["task_arn"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument cutoff_behavior", value=cutoff_behavior, expected_type=type_hints["cutoff_behavior"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_errors", value=max_errors, expected_type=type_hints["max_errors"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument task_invocation_parameters", value=task_invocation_parameters, expected_type=type_hints["task_invocation_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_arn": task_arn,
            "task_type": task_type,
            "window_id": window_id,
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
        if cutoff_behavior is not None:
            self._values["cutoff_behavior"] = cutoff_behavior
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if targets is not None:
            self._values["targets"] = targets
        if task_invocation_parameters is not None:
            self._values["task_invocation_parameters"] = task_invocation_parameters

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
    def task_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_arn SsmMaintenanceWindowTask#task_arn}.'''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_type SsmMaintenanceWindowTask#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#window_id SsmMaintenanceWindowTask#window_id}.'''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cutoff_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cutoff_behavior SsmMaintenanceWindowTask#cutoff_behavior}.'''
        result = self._values.get("cutoff_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#description SsmMaintenanceWindowTask#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#id SsmMaintenanceWindowTask#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_concurrency SsmMaintenanceWindowTask#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#max_errors SsmMaintenanceWindowTask#max_errors}.'''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#priority SsmMaintenanceWindowTask#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]]:
        '''targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#targets SsmMaintenanceWindowTask#targets}
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTargets"]]], result)

    @builtins.property
    def task_invocation_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"]:
        '''task_invocation_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#task_invocation_parameters SsmMaintenanceWindowTask#task_invocation_parameters}
        '''
        result = self._values.get("task_invocation_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTargets",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class SsmMaintenanceWindowTaskTargets:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#key SsmMaintenanceWindowTask#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99235a90aa7453f62f006ad3318d3ccde2719a645d500ea7698b837362abf17)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#key SsmMaintenanceWindowTask#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTargetsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTargetsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f23748e5d6cd3ba0822a323f4755d3d4741eea27fcb2969c008c60b54bb90f3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTaskTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84ad635cb1365c3825b96c0da2dc9813ea63ada619a890ca45ecc028e10175c7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTaskTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73785da5689ae14d110b6acdb4fcf9b1b2b251e771b55c736b1a3dfc2c825bfa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a861a541143aa9b14f86cc7f17fb85d25c4aa3463475b220b51fe01fdaaec8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c788aca24ef15b60353a81df79466cea79f8e8325aba6c396cac957273e560ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f207596ecad6efa9a910b41be83b57e432a694a12952288e5e39a34e064079)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTargetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTargetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1ddac78d7c7105c4eed0f929ed69e4947644489a0acd9034e3671388c0b59bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca085d73a67d4f3793f51c722697104ff0497a4a607d1b789fdc78caab6b91e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3ec26ced43a556f363268adbc836a00a346da71e10cb5e4af15c5c21fc0a7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ab1669015f9800f975872b87e5b34d24fcef9604931726a56d7207ae4f37c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParameters",
    jsii_struct_bases=[],
    name_mapping={
        "automation_parameters": "automationParameters",
        "lambda_parameters": "lambdaParameters",
        "run_command_parameters": "runCommandParameters",
        "step_functions_parameters": "stepFunctionsParameters",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParameters:
    def __init__(
        self,
        *,
        automation_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        run_command_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        step_functions_parameters: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param automation_parameters: automation_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#automation_parameters SsmMaintenanceWindowTask#automation_parameters}
        :param lambda_parameters: lambda_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#lambda_parameters SsmMaintenanceWindowTask#lambda_parameters}
        :param run_command_parameters: run_command_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#run_command_parameters SsmMaintenanceWindowTask#run_command_parameters}
        :param step_functions_parameters: step_functions_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#step_functions_parameters SsmMaintenanceWindowTask#step_functions_parameters}
        '''
        if isinstance(automation_parameters, dict):
            automation_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters(**automation_parameters)
        if isinstance(lambda_parameters, dict):
            lambda_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters(**lambda_parameters)
        if isinstance(run_command_parameters, dict):
            run_command_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(**run_command_parameters)
        if isinstance(step_functions_parameters, dict):
            step_functions_parameters = SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(**step_functions_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8898b72621d9522c455438e7ec53b2c04f359beccb1145a8aebf4f932b4eb48d)
            check_type(argname="argument automation_parameters", value=automation_parameters, expected_type=type_hints["automation_parameters"])
            check_type(argname="argument lambda_parameters", value=lambda_parameters, expected_type=type_hints["lambda_parameters"])
            check_type(argname="argument run_command_parameters", value=run_command_parameters, expected_type=type_hints["run_command_parameters"])
            check_type(argname="argument step_functions_parameters", value=step_functions_parameters, expected_type=type_hints["step_functions_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if automation_parameters is not None:
            self._values["automation_parameters"] = automation_parameters
        if lambda_parameters is not None:
            self._values["lambda_parameters"] = lambda_parameters
        if run_command_parameters is not None:
            self._values["run_command_parameters"] = run_command_parameters
        if step_functions_parameters is not None:
            self._values["step_functions_parameters"] = step_functions_parameters

    @builtins.property
    def automation_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters"]:
        '''automation_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#automation_parameters SsmMaintenanceWindowTask#automation_parameters}
        '''
        result = self._values.get("automation_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters"], result)

    @builtins.property
    def lambda_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters"]:
        '''lambda_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#lambda_parameters SsmMaintenanceWindowTask#lambda_parameters}
        '''
        result = self._values.get("lambda_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters"], result)

    @builtins.property
    def run_command_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"]:
        '''run_command_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#run_command_parameters SsmMaintenanceWindowTask#run_command_parameters}
        '''
        result = self._values.get("run_command_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"], result)

    @builtins.property
    def step_functions_parameters(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"]:
        '''step_functions_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#step_functions_parameters SsmMaintenanceWindowTask#step_functions_parameters}
        '''
        result = self._values.get("step_functions_parameters")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters",
    jsii_struct_bases=[],
    name_mapping={"document_version": "documentVersion", "parameter": "parameter"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters:
    def __init__(
        self,
        *,
        document_version: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4072e3d1cebec2402f7f34a36d25d20f198f726dfa6e96e77b43a12cdd8db3c3)
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if document_version is not None:
            self._values["document_version"] = document_version
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.'''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c5719318fa8b2765b43be4e970e77a8e552097860c2598be7da47b4a6d92e7ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef30cdd1245315a67026487cee809652abe0ab9c36a12bd3696e4f4341a5287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetDocumentVersion")
    def reset_document_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentVersion", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="documentVersionInput")
    def document_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9665b4be358f17820db4e8e021668b0572beb1713c49f71c27f7f93616598b65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__425501d1f8abc67fdb45d88a682883c827b2ff1395f8c2d6d53ed93f5937068e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c534baaf48425ea20a606f1e5faa4490541e6ea376e55ae1e355e66544ca95de)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e437d24b8111af8d0eacd17b4c357298f32cf67916908df5478635ecd31b373)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2505b628bfd30cd25eb69f017d0397f0fcfb30eb4e06790465e2a759db53bd7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8a873aa945d6f525d5e355388fbac420220d1967573c723039491d627c03ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0266b3a0ae23f3a4c1bf16915cafbb4f6b39ef85ff07a29d415d3dd7c4fdc32a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b1a16ddbc6f5ef1cdea311153a4844fc431e647bb634c176b3a4ca49e7439cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d3afc0238054ce0429acf915467302dd76bb87de5ebf5f8f848acb9295d1f73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f252e85ea0ecbbaf1e544a2e74c043fcbc3d36f43463f3bc1a0beffa318ad725)
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1851e96d41cc4cb9e56e2691fd5a0473095aafe65016e6ca44dbd260b9102344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87935a5c022aca31522361ee05303b5880f615a000a6cabeaa18661456b19ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd2db73300d5bba1bd5e7379562dff4f72ac265a6011bb60564a8aea2e6f06b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters",
    jsii_struct_bases=[],
    name_mapping={
        "client_context": "clientContext",
        "payload": "payload",
        "qualifier": "qualifier",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters:
    def __init__(
        self,
        *,
        client_context: typing.Optional[builtins.str] = None,
        payload: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#client_context SsmMaintenanceWindowTask#client_context}.
        :param payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#payload SsmMaintenanceWindowTask#payload}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#qualifier SsmMaintenanceWindowTask#qualifier}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7674c988ada0392e6de1e47ca7c28bd598669673868e8cb502d8f33a8f2eba)
            check_type(argname="argument client_context", value=client_context, expected_type=type_hints["client_context"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_context is not None:
            self._values["client_context"] = client_context
        if payload is not None:
            self._values["payload"] = payload
        if qualifier is not None:
            self._values["qualifier"] = qualifier

    @builtins.property
    def client_context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#client_context SsmMaintenanceWindowTask#client_context}.'''
        result = self._values.get("client_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#payload SsmMaintenanceWindowTask#payload}.'''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#qualifier SsmMaintenanceWindowTask#qualifier}.'''
        result = self._values.get("qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__824e90ddb9f0e40b0a203ee733889b1d1323d7a719329fe182bf6a4e5adf65ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientContext")
    def reset_client_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientContext", []))

    @jsii.member(jsii_name="resetPayload")
    def reset_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayload", []))

    @jsii.member(jsii_name="resetQualifier")
    def reset_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQualifier", []))

    @builtins.property
    @jsii.member(jsii_name="clientContextInput")
    def client_context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientContextInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="clientContext")
    def client_context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientContext"))

    @client_context.setter
    def client_context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c069c406d0ef083bc304b10c559be7e49551c1849637055bfe5537519e40a648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientContext", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d46e811573c130c50b489d1232e0484c7be848869734ea3a64ebe710a7dcdf36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__472d7e3ea0d4eae11befacbdc14da2ef4099f4f0ccfd4baea135708ea641f53c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31ad289f0029df5d0c479d1ef77493f9bb566d7d3f4df72f641e74d5ce67534b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62bf203174150f5f7e4905b52c930755765863adde182481172407275dae360c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutomationParameters")
    def put_automation_parameters(
        self,
        *,
        document_version: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters(
            document_version=document_version, parameter=parameter
        )

        return typing.cast(None, jsii.invoke(self, "putAutomationParameters", [value]))

    @jsii.member(jsii_name="putLambdaParameters")
    def put_lambda_parameters(
        self,
        *,
        client_context: typing.Optional[builtins.str] = None,
        payload: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#client_context SsmMaintenanceWindowTask#client_context}.
        :param payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#payload SsmMaintenanceWindowTask#payload}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#qualifier SsmMaintenanceWindowTask#qualifier}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters(
            client_context=client_context, payload=payload, qualifier=qualifier
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaParameters", [value]))

    @jsii.member(jsii_name="putRunCommandParameters")
    def put_run_command_parameters(
        self,
        *,
        cloudwatch_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        comment: typing.Optional[builtins.str] = None,
        document_hash: typing.Optional[builtins.str] = None,
        document_hash_type: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        output_s3_bucket: typing.Optional[builtins.str] = None,
        output_s3_key_prefix: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cloudwatch_config: cloudwatch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_config SsmMaintenanceWindowTask#cloudwatch_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#comment SsmMaintenanceWindowTask#comment}.
        :param document_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash SsmMaintenanceWindowTask#document_hash}.
        :param document_hash_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash_type SsmMaintenanceWindowTask#document_hash_type}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_config SsmMaintenanceWindowTask#notification_config}
        :param output_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_bucket SsmMaintenanceWindowTask#output_s3_bucket}.
        :param output_s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_key_prefix SsmMaintenanceWindowTask#output_s3_key_prefix}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#timeout_seconds SsmMaintenanceWindowTask#timeout_seconds}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(
            cloudwatch_config=cloudwatch_config,
            comment=comment,
            document_hash=document_hash,
            document_hash_type=document_hash_type,
            document_version=document_version,
            notification_config=notification_config,
            output_s3_bucket=output_s3_bucket,
            output_s3_key_prefix=output_s3_key_prefix,
            parameter=parameter,
            service_role_arn=service_role_arn,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putRunCommandParameters", [value]))

    @jsii.member(jsii_name="putStepFunctionsParameters")
    def put_step_functions_parameters(
        self,
        *,
        input: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#input SsmMaintenanceWindowTask#input}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(
            input=input, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putStepFunctionsParameters", [value]))

    @jsii.member(jsii_name="resetAutomationParameters")
    def reset_automation_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomationParameters", []))

    @jsii.member(jsii_name="resetLambdaParameters")
    def reset_lambda_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaParameters", []))

    @jsii.member(jsii_name="resetRunCommandParameters")
    def reset_run_command_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommandParameters", []))

    @jsii.member(jsii_name="resetStepFunctionsParameters")
    def reset_step_functions_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepFunctionsParameters", []))

    @builtins.property
    @jsii.member(jsii_name="automationParameters")
    def automation_parameters(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference, jsii.get(self, "automationParameters"))

    @builtins.property
    @jsii.member(jsii_name="lambdaParameters")
    def lambda_parameters(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference, jsii.get(self, "lambdaParameters"))

    @builtins.property
    @jsii.member(jsii_name="runCommandParameters")
    def run_command_parameters(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference", jsii.get(self, "runCommandParameters"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctionsParameters")
    def step_functions_parameters(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference", jsii.get(self, "stepFunctionsParameters"))

    @builtins.property
    @jsii.member(jsii_name="automationParametersInput")
    def automation_parameters_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters], jsii.get(self, "automationParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaParametersInput")
    def lambda_parameters_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters], jsii.get(self, "lambdaParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandParametersInput")
    def run_command_parameters_input(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"]:
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters"], jsii.get(self, "runCommandParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctionsParametersInput")
    def step_functions_parameters_input(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"]:
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters"], jsii.get(self, "stepFunctionsParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ab7d040ab8f6c371b59426db4b9273c1535bbf689620e19ef9ef4ac90c1faa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_config": "cloudwatchConfig",
        "comment": "comment",
        "document_hash": "documentHash",
        "document_hash_type": "documentHashType",
        "document_version": "documentVersion",
        "notification_config": "notificationConfig",
        "output_s3_bucket": "outputS3Bucket",
        "output_s3_key_prefix": "outputS3KeyPrefix",
        "parameter": "parameter",
        "service_role_arn": "serviceRoleArn",
        "timeout_seconds": "timeoutSeconds",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters:
    def __init__(
        self,
        *,
        cloudwatch_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        comment: typing.Optional[builtins.str] = None,
        document_hash: typing.Optional[builtins.str] = None,
        document_hash_type: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        output_s3_bucket: typing.Optional[builtins.str] = None,
        output_s3_key_prefix: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cloudwatch_config: cloudwatch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_config SsmMaintenanceWindowTask#cloudwatch_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#comment SsmMaintenanceWindowTask#comment}.
        :param document_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash SsmMaintenanceWindowTask#document_hash}.
        :param document_hash_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash_type SsmMaintenanceWindowTask#document_hash_type}.
        :param document_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_config SsmMaintenanceWindowTask#notification_config}
        :param output_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_bucket SsmMaintenanceWindowTask#output_s3_bucket}.
        :param output_s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_key_prefix SsmMaintenanceWindowTask#output_s3_key_prefix}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#timeout_seconds SsmMaintenanceWindowTask#timeout_seconds}.
        '''
        if isinstance(cloudwatch_config, dict):
            cloudwatch_config = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(**cloudwatch_config)
        if isinstance(notification_config, dict):
            notification_config = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(**notification_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f3245d01f86793e655fd1eeb7557a20960ee80faa1d72bd6f9bdaddf48e143)
            check_type(argname="argument cloudwatch_config", value=cloudwatch_config, expected_type=type_hints["cloudwatch_config"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument document_hash", value=document_hash, expected_type=type_hints["document_hash"])
            check_type(argname="argument document_hash_type", value=document_hash_type, expected_type=type_hints["document_hash_type"])
            check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            check_type(argname="argument notification_config", value=notification_config, expected_type=type_hints["notification_config"])
            check_type(argname="argument output_s3_bucket", value=output_s3_bucket, expected_type=type_hints["output_s3_bucket"])
            check_type(argname="argument output_s3_key_prefix", value=output_s3_key_prefix, expected_type=type_hints["output_s3_key_prefix"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_config is not None:
            self._values["cloudwatch_config"] = cloudwatch_config
        if comment is not None:
            self._values["comment"] = comment
        if document_hash is not None:
            self._values["document_hash"] = document_hash
        if document_hash_type is not None:
            self._values["document_hash_type"] = document_hash_type
        if document_version is not None:
            self._values["document_version"] = document_version
        if notification_config is not None:
            self._values["notification_config"] = notification_config
        if output_s3_bucket is not None:
            self._values["output_s3_bucket"] = output_s3_bucket
        if output_s3_key_prefix is not None:
            self._values["output_s3_key_prefix"] = output_s3_key_prefix
        if parameter is not None:
            self._values["parameter"] = parameter
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def cloudwatch_config(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig"]:
        '''cloudwatch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_config SsmMaintenanceWindowTask#cloudwatch_config}
        '''
        result = self._values.get("cloudwatch_config")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig"], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#comment SsmMaintenanceWindowTask#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash SsmMaintenanceWindowTask#document_hash}.'''
        result = self._values.get("document_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_hash_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_hash_type SsmMaintenanceWindowTask#document_hash_type}.'''
        result = self._values.get("document_hash_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#document_version SsmMaintenanceWindowTask#document_version}.'''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_config(
        self,
    ) -> typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig"]:
        '''notification_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_config SsmMaintenanceWindowTask#notification_config}
        '''
        result = self._values.get("notification_config")
        return typing.cast(typing.Optional["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig"], result)

    @builtins.property
    def output_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_bucket SsmMaintenanceWindowTask#output_s3_bucket}.'''
        result = self._values.get("output_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#output_s3_key_prefix SsmMaintenanceWindowTask#output_s3_key_prefix}.'''
        result = self._values.get("output_s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#parameter SsmMaintenanceWindowTask#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#service_role_arn SsmMaintenanceWindowTask#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#timeout_seconds SsmMaintenanceWindowTask#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_log_group_name": "cloudwatchLogGroupName",
        "cloudwatch_output_enabled": "cloudwatchOutputEnabled",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig:
    def __init__(
        self,
        *,
        cloudwatch_log_group_name: typing.Optional[builtins.str] = None,
        cloudwatch_output_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_log_group_name SsmMaintenanceWindowTask#cloudwatch_log_group_name}.
        :param cloudwatch_output_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_output_enabled SsmMaintenanceWindowTask#cloudwatch_output_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb1bc4f38a196cf3dac812c88b1c88aef02cfe8ac1d0b4bea4a7b28ad52de4b)
            check_type(argname="argument cloudwatch_log_group_name", value=cloudwatch_log_group_name, expected_type=type_hints["cloudwatch_log_group_name"])
            check_type(argname="argument cloudwatch_output_enabled", value=cloudwatch_output_enabled, expected_type=type_hints["cloudwatch_output_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_log_group_name is not None:
            self._values["cloudwatch_log_group_name"] = cloudwatch_log_group_name
        if cloudwatch_output_enabled is not None:
            self._values["cloudwatch_output_enabled"] = cloudwatch_output_enabled

    @builtins.property
    def cloudwatch_log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_log_group_name SsmMaintenanceWindowTask#cloudwatch_log_group_name}.'''
        result = self._values.get("cloudwatch_log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloudwatch_output_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_output_enabled SsmMaintenanceWindowTask#cloudwatch_output_enabled}.'''
        result = self._values.get("cloudwatch_output_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aaadf349b96301bdf4508ca2eab2a97ba813895768ee152d6ba5e62dc4bfd9f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudwatchLogGroupName")
    def reset_cloudwatch_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogGroupName", []))

    @jsii.member(jsii_name="resetCloudwatchOutputEnabled")
    def reset_cloudwatch_output_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchOutputEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupNameInput")
    def cloudwatch_log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchOutputEnabledInput")
    def cloudwatch_output_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudwatchOutputEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupName")
    def cloudwatch_log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupName"))

    @cloudwatch_log_group_name.setter
    def cloudwatch_log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6700319fdb13598f79466eb54f97f0ec1f55999b59cc0b38fd8c21029af5f819)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cloudwatchOutputEnabled")
    def cloudwatch_output_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloudwatchOutputEnabled"))

    @cloudwatch_output_enabled.setter
    def cloudwatch_output_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__007615bc3a8c4506e08f57a102bdf186652b26fdbfcecaf1baf835c49c01370f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchOutputEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7596750e5808567002ba7c0c9cf259f3122d80c58cfb10170ffa0f98d28b9d14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arn": "notificationArn",
        "notification_events": "notificationEvents",
        "notification_type": "notificationType",
    },
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig:
    def __init__(
        self,
        *,
        notification_arn: typing.Optional[builtins.str] = None,
        notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_arn SsmMaintenanceWindowTask#notification_arn}.
        :param notification_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_events SsmMaintenanceWindowTask#notification_events}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_type SsmMaintenanceWindowTask#notification_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec81a934bf07d1225df7bb9af2d6baeb63566702ea73f136fc1ef2163d35a5f)
            check_type(argname="argument notification_arn", value=notification_arn, expected_type=type_hints["notification_arn"])
            check_type(argname="argument notification_events", value=notification_events, expected_type=type_hints["notification_events"])
            check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if notification_arn is not None:
            self._values["notification_arn"] = notification_arn
        if notification_events is not None:
            self._values["notification_events"] = notification_events
        if notification_type is not None:
            self._values["notification_type"] = notification_type

    @builtins.property
    def notification_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_arn SsmMaintenanceWindowTask#notification_arn}.'''
        result = self._values.get("notification_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_events SsmMaintenanceWindowTask#notification_events}.'''
        result = self._values.get("notification_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def notification_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_type SsmMaintenanceWindowTask#notification_type}.'''
        result = self._values.get("notification_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b603e031687e56012edbaf8d4c3ac0c2df5decbdc20c3b9ca28721762431beab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotificationArn")
    def reset_notification_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationArn", []))

    @jsii.member(jsii_name="resetNotificationEvents")
    def reset_notification_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEvents", []))

    @jsii.member(jsii_name="resetNotificationType")
    def reset_notification_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationType", []))

    @builtins.property
    @jsii.member(jsii_name="notificationArnInput")
    def notification_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEventsInput")
    def notification_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTypeInput")
    def notification_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationArn")
    def notification_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationArn"))

    @notification_arn.setter
    def notification_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a9c6a8ede9e23abb31bdaf728fb81bcdf37b3e4df082966706a38f4c172f5dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationArn", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEvents")
    def notification_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEvents"))

    @notification_events.setter
    def notification_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f7203fc98d9404cd6517b352a84ab578a77875f0a59d8797cd2f50435f50d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEvents", value)

    @builtins.property
    @jsii.member(jsii_name="notificationType")
    def notification_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationType"))

    @notification_type.setter
    def notification_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a7c8c3284b4a46a5397e1f37e419eb80ae11a2fa106b7325f421302b79dfb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c5ae4bb140e4d1f86e22c3f70c415f0d7ce951d11c41884302deee0fbf9a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9bcfed63b090f13b5c3b5de626d5d8afee5679abd0a88661e8172abdc076144)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchConfig")
    def put_cloudwatch_config(
        self,
        *,
        cloudwatch_log_group_name: typing.Optional[builtins.str] = None,
        cloudwatch_output_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_log_group_name SsmMaintenanceWindowTask#cloudwatch_log_group_name}.
        :param cloudwatch_output_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#cloudwatch_output_enabled SsmMaintenanceWindowTask#cloudwatch_output_enabled}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig(
            cloudwatch_log_group_name=cloudwatch_log_group_name,
            cloudwatch_output_enabled=cloudwatch_output_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchConfig", [value]))

    @jsii.member(jsii_name="putNotificationConfig")
    def put_notification_config(
        self,
        *,
        notification_arn: typing.Optional[builtins.str] = None,
        notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notification_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_arn SsmMaintenanceWindowTask#notification_arn}.
        :param notification_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_events SsmMaintenanceWindowTask#notification_events}.
        :param notification_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#notification_type SsmMaintenanceWindowTask#notification_type}.
        '''
        value = SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(
            notification_arn=notification_arn,
            notification_events=notification_events,
            notification_type=notification_type,
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationConfig", [value]))

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa76b1085157c164408f26e5fad3812274f3d817cd427b8d50c935a01eace77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetCloudwatchConfig")
    def reset_cloudwatch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchConfig", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDocumentHash")
    def reset_document_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentHash", []))

    @jsii.member(jsii_name="resetDocumentHashType")
    def reset_document_hash_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentHashType", []))

    @jsii.member(jsii_name="resetDocumentVersion")
    def reset_document_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentVersion", []))

    @jsii.member(jsii_name="resetNotificationConfig")
    def reset_notification_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfig", []))

    @jsii.member(jsii_name="resetOutputS3Bucket")
    def reset_output_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputS3Bucket", []))

    @jsii.member(jsii_name="resetOutputS3KeyPrefix")
    def reset_output_s3_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputS3KeyPrefix", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchConfig")
    def cloudwatch_config(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference, jsii.get(self, "cloudwatchConfig"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfig")
    def notification_config(
        self,
    ) -> SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference:
        return typing.cast(SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference, jsii.get(self, "notificationConfig"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(
        self,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList":
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchConfigInput")
    def cloudwatch_config_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig], jsii.get(self, "cloudwatchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="documentHashInput")
    def document_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentHashInput"))

    @builtins.property
    @jsii.member(jsii_name="documentHashTypeInput")
    def document_hash_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentHashTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="documentVersionInput")
    def document_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigInput")
    def notification_config_input(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig], jsii.get(self, "notificationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="outputS3BucketInput")
    def output_s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputS3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="outputS3KeyPrefixInput")
    def output_s3_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputS3KeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f735325e845f05182214312e39c9bde047c715b65815bdf54093dee76a3071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="documentHash")
    def document_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentHash"))

    @document_hash.setter
    def document_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8449807ea2a7e778c65eb6c690d02bc809357d277f8d44096f7c37fdf4f9a561)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentHash", value)

    @builtins.property
    @jsii.member(jsii_name="documentHashType")
    def document_hash_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentHashType"))

    @document_hash_type.setter
    def document_hash_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9544b42ec18cae493aae9a36e1fdb4bf90cf1aebe5aea8ec48affbc80066753a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentHashType", value)

    @builtins.property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c9c80993c337625aa1e2317cecac07830a1472feb96d3afd5ab6592bb53880)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="outputS3Bucket")
    def output_s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputS3Bucket"))

    @output_s3_bucket.setter
    def output_s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17649c2908629bbda35a9d166906a5a63a6bb8070356c1df7ac4668c323d23f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="outputS3KeyPrefix")
    def output_s3_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputS3KeyPrefix"))

    @output_s3_key_prefix.setter
    def output_s3_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b258e4c69da3f0f41f8e491a3cdc7e0cb12f12a22adfeb2481c8965e404e478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputS3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802cc4dea2bc2d7205092e1fe08d5fdeb1f9d3e8be19c8bf2fd5c0aba33fd6c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93594594b6f7a5018f6e51d122ecc3136034719c3a5225d0bcf83efc42e60c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c98d43f8765b1108672a4621d79f77c9303d1406078d8071cef2793186190961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "values": "values"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8320a9bd491dceb69a9ba7aea2a89d7132ff189f124e20b1a359778a5eaa0ad)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#values SsmMaintenanceWindowTask#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26b4b9457972017fd4e36254369ffa2c262cdaef5da974036407d5d1c10773fb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cbaf091d85bb66501b8e95a7f088f0f09cdc3c3121da6292f4c05aa6c3537fe)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14058a6d77b39fbabc09f5c578c84af92cef304d6c5f7a1110c50e3084c08e59)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9be061419502d19c1adbb4ce22d48d7972ac78caca27f60ff28b258881b63666)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8182a336e00c7df7427c2014a3c933add7e0b8695d20f88614e6bd1bd5e2af1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff79e05422e9ebf5129f0cb58ebfcaec37dc33b8cfc6a9489407c3bee0186259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30aa206864bed27a3fa224f0b92eec33a6990d466c91f5d3bedcd0650f7411d0)
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2364486e55538671288eb3394158523aa9449ea63aa325affdb080f36a228ad3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4ee8186a83f95656d24dcc2e13f9016fab53331d41452c977862178091658c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4ebde1a882791f261549819bb68b75ce9121935cbd8ff69dc268e11e48224d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters",
    jsii_struct_bases=[],
    name_mapping={"input": "input", "name": "name"},
)
class SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters:
    def __init__(
        self,
        *,
        input: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#input SsmMaintenanceWindowTask#input}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3bb979000232f11aa87855cf0b22bcd39571fe6019d0e9dccd3a4419cd8aaa)
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if input is not None:
            self._values["input"] = input
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def input(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#input SsmMaintenanceWindowTask#input}.'''
        result = self._values.get("input")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task#name SsmMaintenanceWindowTask#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssmMaintenanceWindowTask.SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4975de5b27a1cc5597bc81c714c5b3aee4cef743a8b4acfb690f64176230ca20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInput")
    def reset_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInput", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "input"))

    @input.setter
    def input(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12f5b302031aa3029d976edf18b8143bec4275e5fdfe5aae81bc8a37704219b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "input", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d989320eab8dc9f33a3ba2b3a714aec86698106c3635a834639e3f4e06b8c688)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters]:
        return typing.cast(typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076296bd1b80cd3b6947be1d6a43dfe44b06c5c47506a6252559b4aefc3f277e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SsmMaintenanceWindowTask",
    "SsmMaintenanceWindowTaskConfig",
    "SsmMaintenanceWindowTaskTargets",
    "SsmMaintenanceWindowTaskTargetsList",
    "SsmMaintenanceWindowTaskTargetsOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterList",
    "SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfigOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterList",
    "SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutputReference",
    "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters",
    "SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutputReference",
]

publication.publish()

def _typecheckingstub__8c33375b82c96b14e05d47f714c42f91fc3f648ea3af03faaf4cecf7d1bc9a8b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    task_arn: builtins.str,
    task_type: builtins.str,
    window_id: builtins.str,
    cutoff_behavior: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[builtins.str] = None,
    max_errors: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
    targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTargets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    task_invocation_parameters: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParameters, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__1b5268983aaa90ae025091363a82cdd9705e3c52bd1417f9a9e8baedeee0b160(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTargets, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9340cee7fc04d35b8f325f1aa1a99ac90d3719972c4bdd532f9b8801832a47e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d24d27514b298b9920797283e166e1e0b476f62ae4ac5d6dbba1cda6ad95196(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e59a21cd547d338ba4089072e89392a918e02146e9b9f82a847976067c5de2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d19becb821716a992671cae5f3594f435ae1d801216112bc004a357db15212(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b4cdf122da1fd2333f8ef53013024e93c8ac620370f2f8d810a38723b0bebe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2613511ee3757edab6e75f1837454de3102293dff4c3da6b98ba96c51390b242(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa51212dc92c57c065aaf283c3f27c36ed0728d4fcdf772c7bf1b560ff6abeea(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e49940537aac5e2b4720ffe66dd26b115e5275b58065dedb026e81a9f9200d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee161fb9cda821d687c442f508a634126e98b8244a7627be24cced7b126472ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d7e01558505275d74a8216da6b21f432e8d05714a4fc969d15415dafdac7c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__639497d20c0cda61d5dc925f43d9934528a8bfb326d01c345bd7810980defc21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1069539fb252ba88963f3e047821523217272d04c38f71677e5caab2e3ce674c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    task_arn: builtins.str,
    task_type: builtins.str,
    window_id: builtins.str,
    cutoff_behavior: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[builtins.str] = None,
    max_errors: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
    targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTargets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    task_invocation_parameters: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParameters, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99235a90aa7453f62f006ad3318d3ccde2719a645d500ea7698b837362abf17(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f23748e5d6cd3ba0822a323f4755d3d4741eea27fcb2969c008c60b54bb90f3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ad635cb1365c3825b96c0da2dc9813ea63ada619a890ca45ecc028e10175c7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73785da5689ae14d110b6acdb4fcf9b1b2b251e771b55c736b1a3dfc2c825bfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a861a541143aa9b14f86cc7f17fb85d25c4aa3463475b220b51fe01fdaaec8b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c788aca24ef15b60353a81df79466cea79f8e8325aba6c396cac957273e560ba(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f207596ecad6efa9a910b41be83b57e432a694a12952288e5e39a34e064079(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTargets]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ddac78d7c7105c4eed0f929ed69e4947644489a0acd9034e3671388c0b59bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca085d73a67d4f3793f51c722697104ff0497a4a607d1b789fdc78caab6b91e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3ec26ced43a556f363268adbc836a00a346da71e10cb5e4af15c5c21fc0a7e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ab1669015f9800f975872b87e5b34d24fcef9604931726a56d7207ae4f37c8a(
    value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTargets, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8898b72621d9522c455438e7ec53b2c04f359beccb1145a8aebf4f932b4eb48d(
    *,
    automation_parameters: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_parameters: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    run_command_parameters: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    step_functions_parameters: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4072e3d1cebec2402f7f34a36d25d20f198f726dfa6e96e77b43a12cdd8db3c3(
    *,
    document_version: typing.Optional[builtins.str] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5719318fa8b2765b43be4e970e77a8e552097860c2598be7da47b4a6d92e7ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef30cdd1245315a67026487cee809652abe0ab9c36a12bd3696e4f4341a5287(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9665b4be358f17820db4e8e021668b0572beb1713c49f71c27f7f93616598b65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__425501d1f8abc67fdb45d88a682883c827b2ff1395f8c2d6d53ed93f5937068e(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c534baaf48425ea20a606f1e5faa4490541e6ea376e55ae1e355e66544ca95de(
    *,
    name: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e437d24b8111af8d0eacd17b4c357298f32cf67916908df5478635ecd31b373(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2505b628bfd30cd25eb69f017d0397f0fcfb30eb4e06790465e2a759db53bd7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8a873aa945d6f525d5e355388fbac420220d1967573c723039491d627c03ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0266b3a0ae23f3a4c1bf16915cafbb4f6b39ef85ff07a29d415d3dd7c4fdc32a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1a16ddbc6f5ef1cdea311153a4844fc431e647bb634c176b3a4ca49e7439cb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d3afc0238054ce0429acf915467302dd76bb87de5ebf5f8f848acb9295d1f73(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f252e85ea0ecbbaf1e544a2e74c043fcbc3d36f43463f3bc1a0beffa318ad725(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1851e96d41cc4cb9e56e2691fd5a0473095aafe65016e6ca44dbd260b9102344(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87935a5c022aca31522361ee05303b5880f615a000a6cabeaa18661456b19ef(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd2db73300d5bba1bd5e7379562dff4f72ac265a6011bb60564a8aea2e6f06b(
    value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7674c988ada0392e6de1e47ca7c28bd598669673868e8cb502d8f33a8f2eba(
    *,
    client_context: typing.Optional[builtins.str] = None,
    payload: typing.Optional[builtins.str] = None,
    qualifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824e90ddb9f0e40b0a203ee733889b1d1323d7a719329fe182bf6a4e5adf65ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c069c406d0ef083bc304b10c559be7e49551c1849637055bfe5537519e40a648(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d46e811573c130c50b489d1232e0484c7be848869734ea3a64ebe710a7dcdf36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472d7e3ea0d4eae11befacbdc14da2ef4099f4f0ccfd4baea135708ea641f53c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ad289f0029df5d0c479d1ef77493f9bb566d7d3f4df72f641e74d5ce67534b(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersLambdaParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62bf203174150f5f7e4905b52c930755765863adde182481172407275dae360c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ab7d040ab8f6c371b59426db4b9273c1535bbf689620e19ef9ef4ac90c1faa(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f3245d01f86793e655fd1eeb7557a20960ee80faa1d72bd6f9bdaddf48e143(
    *,
    cloudwatch_config: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    comment: typing.Optional[builtins.str] = None,
    document_hash: typing.Optional[builtins.str] = None,
    document_hash_type: typing.Optional[builtins.str] = None,
    document_version: typing.Optional[builtins.str] = None,
    notification_config: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    output_s3_bucket: typing.Optional[builtins.str] = None,
    output_s3_key_prefix: typing.Optional[builtins.str] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    service_role_arn: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb1bc4f38a196cf3dac812c88b1c88aef02cfe8ac1d0b4bea4a7b28ad52de4b(
    *,
    cloudwatch_log_group_name: typing.Optional[builtins.str] = None,
    cloudwatch_output_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaadf349b96301bdf4508ca2eab2a97ba813895768ee152d6ba5e62dc4bfd9f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6700319fdb13598f79466eb54f97f0ec1f55999b59cc0b38fd8c21029af5f819(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__007615bc3a8c4506e08f57a102bdf186652b26fdbfcecaf1baf835c49c01370f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7596750e5808567002ba7c0c9cf259f3122d80c58cfb10170ffa0f98d28b9d14(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersCloudwatchConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec81a934bf07d1225df7bb9af2d6baeb63566702ea73f136fc1ef2163d35a5f(
    *,
    notification_arn: typing.Optional[builtins.str] = None,
    notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b603e031687e56012edbaf8d4c3ac0c2df5decbdc20c3b9ca28721762431beab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9c6a8ede9e23abb31bdaf728fb81bcdf37b3e4df082966706a38f4c172f5dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7203fc98d9404cd6517b352a84ab578a77875f0a59d8797cd2f50435f50d39(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a7c8c3284b4a46a5397e1f37e419eb80ae11a2fa106b7325f421302b79dfb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c5ae4bb140e4d1f86e22c3f70c415f0d7ce951d11c41884302deee0fbf9a8e(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9bcfed63b090f13b5c3b5de626d5d8afee5679abd0a88661e8172abdc076144(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa76b1085157c164408f26e5fad3812274f3d817cd427b8d50c935a01eace77(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f735325e845f05182214312e39c9bde047c715b65815bdf54093dee76a3071(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8449807ea2a7e778c65eb6c690d02bc809357d277f8d44096f7c37fdf4f9a561(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9544b42ec18cae493aae9a36e1fdb4bf90cf1aebe5aea8ec48affbc80066753a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c9c80993c337625aa1e2317cecac07830a1472feb96d3afd5ab6592bb53880(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17649c2908629bbda35a9d166906a5a63a6bb8070356c1df7ac4668c323d23f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b258e4c69da3f0f41f8e491a3cdc7e0cb12f12a22adfeb2481c8965e404e478(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802cc4dea2bc2d7205092e1fe08d5fdeb1f9d3e8be19c8bf2fd5c0aba33fd6c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93594594b6f7a5018f6e51d122ecc3136034719c3a5225d0bcf83efc42e60c56(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98d43f8765b1108672a4621d79f77c9303d1406078d8071cef2793186190961(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8320a9bd491dceb69a9ba7aea2a89d7132ff189f124e20b1a359778a5eaa0ad(
    *,
    name: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b4b9457972017fd4e36254369ffa2c262cdaef5da974036407d5d1c10773fb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbaf091d85bb66501b8e95a7f088f0f09cdc3c3121da6292f4c05aa6c3537fe(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14058a6d77b39fbabc09f5c578c84af92cef304d6c5f7a1110c50e3084c08e59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be061419502d19c1adbb4ce22d48d7972ac78caca27f60ff28b258881b63666(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8182a336e00c7df7427c2014a3c933add7e0b8695d20f88614e6bd1bd5e2af1c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff79e05422e9ebf5129f0cb58ebfcaec37dc33b8cfc6a9489407c3bee0186259(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30aa206864bed27a3fa224f0b92eec33a6990d466c91f5d3bedcd0650f7411d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2364486e55538671288eb3394158523aa9449ea63aa325affdb080f36a228ad3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ee8186a83f95656d24dcc2e13f9016fab53331d41452c977862178091658c0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4ebde1a882791f261549819bb68b75ce9121935cbd8ff69dc268e11e48224d(
    value: typing.Optional[typing.Union[SsmMaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3bb979000232f11aa87855cf0b22bcd39571fe6019d0e9dccd3a4419cd8aaa(
    *,
    input: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4975de5b27a1cc5597bc81c714c5b3aee4cef743a8b4acfb690f64176230ca20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f5b302031aa3029d976edf18b8143bec4275e5fdfe5aae81bc8a37704219b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d989320eab8dc9f33a3ba2b3a714aec86698106c3635a834639e3f4e06b8c688(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076296bd1b80cd3b6947be1d6a43dfe44b06c5c47506a6252559b4aefc3f277e(
    value: typing.Optional[SsmMaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters],
) -> None:
    """Type checking stubs"""
    pass
