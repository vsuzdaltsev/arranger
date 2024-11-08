'''
# `aws_cloudwatch_event_target`

Refer to the Terraform Registory for docs: [`aws_cloudwatch_event_target`](https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target).
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


class CloudwatchEventTarget(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTarget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target aws_cloudwatch_event_target}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        arn: builtins.str,
        rule: builtins.str,
        batch_target: typing.Optional[typing.Union["CloudwatchEventTargetBatchTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_config: typing.Optional[typing.Union["CloudwatchEventTargetDeadLetterConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        ecs_target: typing.Optional[typing.Union["CloudwatchEventTargetEcsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        http_target: typing.Optional[typing.Union["CloudwatchEventTargetHttpTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        input: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        input_transformer: typing.Optional[typing.Union["CloudwatchEventTargetInputTransformer", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_target: typing.Optional[typing.Union["CloudwatchEventTargetKinesisTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift_target: typing.Optional[typing.Union["CloudwatchEventTargetRedshiftTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["CloudwatchEventTargetRetryPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        run_command_targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetRunCommandTargets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sqs_target: typing.Optional[typing.Union["CloudwatchEventTargetSqsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        target_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target aws_cloudwatch_event_target} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#rule CloudwatchEventTarget#rule}.
        :param batch_target: batch_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#batch_target CloudwatchEventTarget#batch_target}
        :param dead_letter_config: dead_letter_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#dead_letter_config CloudwatchEventTarget#dead_letter_config}
        :param ecs_target: ecs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#ecs_target CloudwatchEventTarget#ecs_target}
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#event_bus_name CloudwatchEventTarget#event_bus_name}.
        :param http_target: http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#http_target CloudwatchEventTarget#http_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#id CloudwatchEventTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input CloudwatchEventTarget#input}.
        :param input_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_path CloudwatchEventTarget#input_path}.
        :param input_transformer: input_transformer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_transformer CloudwatchEventTarget#input_transformer}
        :param kinesis_target: kinesis_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#kinesis_target CloudwatchEventTarget#kinesis_target}
        :param redshift_target: redshift_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#redshift_target CloudwatchEventTarget#redshift_target}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#retry_policy CloudwatchEventTarget#retry_policy}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#role_arn CloudwatchEventTarget#role_arn}.
        :param run_command_targets: run_command_targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#run_command_targets CloudwatchEventTarget#run_command_targets}
        :param sqs_target: sqs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sqs_target CloudwatchEventTarget#sqs_target}
        :param target_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#target_id CloudwatchEventTarget#target_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2841400388f1eb22d9fb517ac6ea298d64c51453775df58fded90a07ff67fdcc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudwatchEventTargetConfig(
            arn=arn,
            rule=rule,
            batch_target=batch_target,
            dead_letter_config=dead_letter_config,
            ecs_target=ecs_target,
            event_bus_name=event_bus_name,
            http_target=http_target,
            id=id,
            input=input,
            input_path=input_path,
            input_transformer=input_transformer,
            kinesis_target=kinesis_target,
            redshift_target=redshift_target,
            retry_policy=retry_policy,
            role_arn=role_arn,
            run_command_targets=run_command_targets,
            sqs_target=sqs_target,
            target_id=target_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBatchTarget")
    def put_batch_target(
        self,
        *,
        job_definition: builtins.str,
        job_name: builtins.str,
        array_size: typing.Optional[jsii.Number] = None,
        job_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param job_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_definition CloudwatchEventTarget#job_definition}.
        :param job_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_name CloudwatchEventTarget#job_name}.
        :param array_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#array_size CloudwatchEventTarget#array_size}.
        :param job_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_attempts CloudwatchEventTarget#job_attempts}.
        '''
        value = CloudwatchEventTargetBatchTarget(
            job_definition=job_definition,
            job_name=job_name,
            array_size=array_size,
            job_attempts=job_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "putBatchTarget", [value]))

    @jsii.member(jsii_name="putDeadLetterConfig")
    def put_dead_letter_config(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        '''
        value = CloudwatchEventTargetDeadLetterConfig(arn=arn)

        return typing.cast(None, jsii.invoke(self, "putDeadLetterConfig", [value]))

    @jsii.member(jsii_name="putEcsTarget")
    def put_ecs_target(
        self,
        *,
        task_definition_arn: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetCapacityProviderStrategy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["CloudwatchEventTargetEcsTargetNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        placement_constraint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetPlacementConstraint", typing.Dict[builtins.str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param task_definition_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_definition_arn CloudwatchEventTarget#task_definition_arn}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#capacity_provider_strategy CloudwatchEventTarget#capacity_provider_strategy}
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_ecs_managed_tags CloudwatchEventTarget#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_execute_command CloudwatchEventTarget#enable_execute_command}.
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#group CloudwatchEventTarget#group}.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#launch_type CloudwatchEventTarget#launch_type}.
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#network_configuration CloudwatchEventTarget#network_configuration}
        :param placement_constraint: placement_constraint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#placement_constraint CloudwatchEventTarget#placement_constraint}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#platform_version CloudwatchEventTarget#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#propagate_tags CloudwatchEventTarget#propagate_tags}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#tags CloudwatchEventTarget#tags}.
        :param task_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_count CloudwatchEventTarget#task_count}.
        '''
        value = CloudwatchEventTargetEcsTarget(
            task_definition_arn=task_definition_arn,
            capacity_provider_strategy=capacity_provider_strategy,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            group=group,
            launch_type=launch_type,
            network_configuration=network_configuration,
            placement_constraint=placement_constraint,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            tags=tags,
            task_count=task_count,
        )

        return typing.cast(None, jsii.invoke(self, "putEcsTarget", [value]))

    @jsii.member(jsii_name="putHttpTarget")
    def put_http_target(
        self,
        *,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param header_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#header_parameters CloudwatchEventTarget#header_parameters}.
        :param path_parameter_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#path_parameter_values CloudwatchEventTarget#path_parameter_values}.
        :param query_string_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#query_string_parameters CloudwatchEventTarget#query_string_parameters}.
        '''
        value = CloudwatchEventTargetHttpTarget(
            header_parameters=header_parameters,
            path_parameter_values=path_parameter_values,
            query_string_parameters=query_string_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpTarget", [value]))

    @jsii.member(jsii_name="putInputTransformer")
    def put_input_transformer(
        self,
        *,
        input_template: builtins.str,
        input_paths: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param input_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_template CloudwatchEventTarget#input_template}.
        :param input_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_paths CloudwatchEventTarget#input_paths}.
        '''
        value = CloudwatchEventTargetInputTransformer(
            input_template=input_template, input_paths=input_paths
        )

        return typing.cast(None, jsii.invoke(self, "putInputTransformer", [value]))

    @jsii.member(jsii_name="putKinesisTarget")
    def put_kinesis_target(
        self,
        *,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param partition_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#partition_key_path CloudwatchEventTarget#partition_key_path}.
        '''
        value = CloudwatchEventTargetKinesisTarget(
            partition_key_path=partition_key_path
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisTarget", [value]))

    @jsii.member(jsii_name="putRedshiftTarget")
    def put_redshift_target(
        self,
        *,
        database: builtins.str,
        db_user: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        sql: typing.Optional[builtins.str] = None,
        statement_name: typing.Optional[builtins.str] = None,
        with_event: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#database CloudwatchEventTarget#database}.
        :param db_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#db_user CloudwatchEventTarget#db_user}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#secrets_manager_arn CloudwatchEventTarget#secrets_manager_arn}.
        :param sql: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sql CloudwatchEventTarget#sql}.
        :param statement_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#statement_name CloudwatchEventTarget#statement_name}.
        :param with_event: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#with_event CloudwatchEventTarget#with_event}.
        '''
        value = CloudwatchEventTargetRedshiftTarget(
            database=database,
            db_user=db_user,
            secrets_manager_arn=secrets_manager_arn,
            sql=sql,
            statement_name=statement_name,
            with_event=with_event,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshiftTarget", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_event_age_in_seconds CloudwatchEventTarget#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_retry_attempts CloudwatchEventTarget#maximum_retry_attempts}.
        '''
        value = CloudwatchEventTargetRetryPolicy(
            maximum_event_age_in_seconds=maximum_event_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putRunCommandTargets")
    def put_run_command_targets(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetRunCommandTargets", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bcdcf7f7c9729212861af003dd83ffabc6c76f331120cf271c24a6363cdb803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRunCommandTargets", [value]))

    @jsii.member(jsii_name="putSqsTarget")
    def put_sqs_target(
        self,
        *,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#message_group_id CloudwatchEventTarget#message_group_id}.
        '''
        value = CloudwatchEventTargetSqsTarget(message_group_id=message_group_id)

        return typing.cast(None, jsii.invoke(self, "putSqsTarget", [value]))

    @jsii.member(jsii_name="resetBatchTarget")
    def reset_batch_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchTarget", []))

    @jsii.member(jsii_name="resetDeadLetterConfig")
    def reset_dead_letter_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetterConfig", []))

    @jsii.member(jsii_name="resetEcsTarget")
    def reset_ecs_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEcsTarget", []))

    @jsii.member(jsii_name="resetEventBusName")
    def reset_event_bus_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBusName", []))

    @jsii.member(jsii_name="resetHttpTarget")
    def reset_http_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTarget", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInput")
    def reset_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInput", []))

    @jsii.member(jsii_name="resetInputPath")
    def reset_input_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputPath", []))

    @jsii.member(jsii_name="resetInputTransformer")
    def reset_input_transformer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputTransformer", []))

    @jsii.member(jsii_name="resetKinesisTarget")
    def reset_kinesis_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisTarget", []))

    @jsii.member(jsii_name="resetRedshiftTarget")
    def reset_redshift_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshiftTarget", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetRunCommandTargets")
    def reset_run_command_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommandTargets", []))

    @jsii.member(jsii_name="resetSqsTarget")
    def reset_sqs_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqsTarget", []))

    @jsii.member(jsii_name="resetTargetId")
    def reset_target_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="batchTarget")
    def batch_target(self) -> "CloudwatchEventTargetBatchTargetOutputReference":
        return typing.cast("CloudwatchEventTargetBatchTargetOutputReference", jsii.get(self, "batchTarget"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterConfig")
    def dead_letter_config(
        self,
    ) -> "CloudwatchEventTargetDeadLetterConfigOutputReference":
        return typing.cast("CloudwatchEventTargetDeadLetterConfigOutputReference", jsii.get(self, "deadLetterConfig"))

    @builtins.property
    @jsii.member(jsii_name="ecsTarget")
    def ecs_target(self) -> "CloudwatchEventTargetEcsTargetOutputReference":
        return typing.cast("CloudwatchEventTargetEcsTargetOutputReference", jsii.get(self, "ecsTarget"))

    @builtins.property
    @jsii.member(jsii_name="httpTarget")
    def http_target(self) -> "CloudwatchEventTargetHttpTargetOutputReference":
        return typing.cast("CloudwatchEventTargetHttpTargetOutputReference", jsii.get(self, "httpTarget"))

    @builtins.property
    @jsii.member(jsii_name="inputTransformer")
    def input_transformer(
        self,
    ) -> "CloudwatchEventTargetInputTransformerOutputReference":
        return typing.cast("CloudwatchEventTargetInputTransformerOutputReference", jsii.get(self, "inputTransformer"))

    @builtins.property
    @jsii.member(jsii_name="kinesisTarget")
    def kinesis_target(self) -> "CloudwatchEventTargetKinesisTargetOutputReference":
        return typing.cast("CloudwatchEventTargetKinesisTargetOutputReference", jsii.get(self, "kinesisTarget"))

    @builtins.property
    @jsii.member(jsii_name="redshiftTarget")
    def redshift_target(self) -> "CloudwatchEventTargetRedshiftTargetOutputReference":
        return typing.cast("CloudwatchEventTargetRedshiftTargetOutputReference", jsii.get(self, "redshiftTarget"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "CloudwatchEventTargetRetryPolicyOutputReference":
        return typing.cast("CloudwatchEventTargetRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="runCommandTargets")
    def run_command_targets(self) -> "CloudwatchEventTargetRunCommandTargetsList":
        return typing.cast("CloudwatchEventTargetRunCommandTargetsList", jsii.get(self, "runCommandTargets"))

    @builtins.property
    @jsii.member(jsii_name="sqsTarget")
    def sqs_target(self) -> "CloudwatchEventTargetSqsTargetOutputReference":
        return typing.cast("CloudwatchEventTargetSqsTargetOutputReference", jsii.get(self, "sqsTarget"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="batchTargetInput")
    def batch_target_input(self) -> typing.Optional["CloudwatchEventTargetBatchTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetBatchTarget"], jsii.get(self, "batchTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterConfigInput")
    def dead_letter_config_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetDeadLetterConfig"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetDeadLetterConfig"], jsii.get(self, "deadLetterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="ecsTargetInput")
    def ecs_target_input(self) -> typing.Optional["CloudwatchEventTargetEcsTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetEcsTarget"], jsii.get(self, "ecsTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBusNameInput")
    def event_bus_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventBusNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTargetInput")
    def http_target_input(self) -> typing.Optional["CloudwatchEventTargetHttpTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetHttpTarget"], jsii.get(self, "httpTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="inputPathInput")
    def input_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="inputTransformerInput")
    def input_transformer_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetInputTransformer"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetInputTransformer"], jsii.get(self, "inputTransformerInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisTargetInput")
    def kinesis_target_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetKinesisTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetKinesisTarget"], jsii.get(self, "kinesisTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftTargetInput")
    def redshift_target_input(
        self,
    ) -> typing.Optional["CloudwatchEventTargetRedshiftTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetRedshiftTarget"], jsii.get(self, "redshiftTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(self) -> typing.Optional["CloudwatchEventTargetRetryPolicy"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandTargetsInput")
    def run_command_targets_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]], jsii.get(self, "runCommandTargetsInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsTargetInput")
    def sqs_target_input(self) -> typing.Optional["CloudwatchEventTargetSqsTarget"]:
        return typing.cast(typing.Optional["CloudwatchEventTargetSqsTarget"], jsii.get(self, "sqsTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIdInput")
    def target_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a94c98d1db20f1b639c681ad0c61bfa8d30113955669d0f26225717db343d75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="eventBusName")
    def event_bus_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventBusName"))

    @event_bus_name.setter
    def event_bus_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82dcff8f16dd736e1c11ddebdf62162c892a51b3fc52ed3fb22ef0872c85f48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723134b38984a55a9fbd59e10a189b902ac81d52b0854d92857141ef46d49d42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "input"))

    @input.setter
    def input(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e24cc0f717d6c47ea0f55b7391065e491442f8ddd0b1039ae28fab867ae54884)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "input", value)

    @builtins.property
    @jsii.member(jsii_name="inputPath")
    def input_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputPath"))

    @input_path.setter
    def input_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__097678e57e039eb7014b41579c2c350d31ae5d45ec735184b819b5bb61790d20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputPath", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2503f1a06a773c0fe5ccc796060202ba11c515a99ef5af9d2c5869744a629e90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a75b370d72a84a06885932c48ee89d09bc2c149b4d55de14656bc49f034ac36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c38fb5fcedbd9b3509e21b3e870ceb800c5a093f7d3d2f0a69f04f1f96b91be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetBatchTarget",
    jsii_struct_bases=[],
    name_mapping={
        "job_definition": "jobDefinition",
        "job_name": "jobName",
        "array_size": "arraySize",
        "job_attempts": "jobAttempts",
    },
)
class CloudwatchEventTargetBatchTarget:
    def __init__(
        self,
        *,
        job_definition: builtins.str,
        job_name: builtins.str,
        array_size: typing.Optional[jsii.Number] = None,
        job_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param job_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_definition CloudwatchEventTarget#job_definition}.
        :param job_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_name CloudwatchEventTarget#job_name}.
        :param array_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#array_size CloudwatchEventTarget#array_size}.
        :param job_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_attempts CloudwatchEventTarget#job_attempts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec5dbce9617af422336001e68cf6423258145551b389ccd12db500dadf91225)
            check_type(argname="argument job_definition", value=job_definition, expected_type=type_hints["job_definition"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument array_size", value=array_size, expected_type=type_hints["array_size"])
            check_type(argname="argument job_attempts", value=job_attempts, expected_type=type_hints["job_attempts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_definition": job_definition,
            "job_name": job_name,
        }
        if array_size is not None:
            self._values["array_size"] = array_size
        if job_attempts is not None:
            self._values["job_attempts"] = job_attempts

    @builtins.property
    def job_definition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_definition CloudwatchEventTarget#job_definition}.'''
        result = self._values.get("job_definition")
        assert result is not None, "Required property 'job_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_name CloudwatchEventTarget#job_name}.'''
        result = self._values.get("job_name")
        assert result is not None, "Required property 'job_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def array_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#array_size CloudwatchEventTarget#array_size}.'''
        result = self._values.get("array_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def job_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#job_attempts CloudwatchEventTarget#job_attempts}.'''
        result = self._values.get("job_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetBatchTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetBatchTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetBatchTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__390b81c13873856dcd23e96cb4b09e7c892eb57f7639c407c6647aef1d6bbe62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArraySize")
    def reset_array_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArraySize", []))

    @jsii.member(jsii_name="resetJobAttempts")
    def reset_job_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobAttempts", []))

    @builtins.property
    @jsii.member(jsii_name="arraySizeInput")
    def array_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "arraySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="jobAttemptsInput")
    def job_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jobAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="jobDefinitionInput")
    def job_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="jobNameInput")
    def job_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobNameInput"))

    @builtins.property
    @jsii.member(jsii_name="arraySize")
    def array_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "arraySize"))

    @array_size.setter
    def array_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6899ef36ef9194747fcc38115f5cef6ab8cd49cbeff9961d137e08e596bd4fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arraySize", value)

    @builtins.property
    @jsii.member(jsii_name="jobAttempts")
    def job_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "jobAttempts"))

    @job_attempts.setter
    def job_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de40a91b9fed57d611b0800a7e8fe19a211d6e3dd47cd225616d898464c47ba2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="jobDefinition")
    def job_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobDefinition"))

    @job_definition.setter
    def job_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3648bc685dea2b7e7430f140d2c959c37227bfaaaef7afc2ed8d76c73f4bd7b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="jobName")
    def job_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobName"))

    @job_name.setter
    def job_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06741ddabd23cfdb1de0ce4fcd7c411e71ce155b8126972bdac2bbcab05dd204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetBatchTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetBatchTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetBatchTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de4693a8f6782eed232b8cf681f7fa1b027995f1ef139996151379fdc781716b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "arn": "arn",
        "rule": "rule",
        "batch_target": "batchTarget",
        "dead_letter_config": "deadLetterConfig",
        "ecs_target": "ecsTarget",
        "event_bus_name": "eventBusName",
        "http_target": "httpTarget",
        "id": "id",
        "input": "input",
        "input_path": "inputPath",
        "input_transformer": "inputTransformer",
        "kinesis_target": "kinesisTarget",
        "redshift_target": "redshiftTarget",
        "retry_policy": "retryPolicy",
        "role_arn": "roleArn",
        "run_command_targets": "runCommandTargets",
        "sqs_target": "sqsTarget",
        "target_id": "targetId",
    },
)
class CloudwatchEventTargetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        arn: builtins.str,
        rule: builtins.str,
        batch_target: typing.Optional[typing.Union[CloudwatchEventTargetBatchTarget, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_config: typing.Optional[typing.Union["CloudwatchEventTargetDeadLetterConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        ecs_target: typing.Optional[typing.Union["CloudwatchEventTargetEcsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        event_bus_name: typing.Optional[builtins.str] = None,
        http_target: typing.Optional[typing.Union["CloudwatchEventTargetHttpTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        input: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        input_transformer: typing.Optional[typing.Union["CloudwatchEventTargetInputTransformer", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_target: typing.Optional[typing.Union["CloudwatchEventTargetKinesisTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift_target: typing.Optional[typing.Union["CloudwatchEventTargetRedshiftTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["CloudwatchEventTargetRetryPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        run_command_targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetRunCommandTargets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sqs_target: typing.Optional[typing.Union["CloudwatchEventTargetSqsTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        target_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#rule CloudwatchEventTarget#rule}.
        :param batch_target: batch_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#batch_target CloudwatchEventTarget#batch_target}
        :param dead_letter_config: dead_letter_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#dead_letter_config CloudwatchEventTarget#dead_letter_config}
        :param ecs_target: ecs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#ecs_target CloudwatchEventTarget#ecs_target}
        :param event_bus_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#event_bus_name CloudwatchEventTarget#event_bus_name}.
        :param http_target: http_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#http_target CloudwatchEventTarget#http_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#id CloudwatchEventTarget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param input: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input CloudwatchEventTarget#input}.
        :param input_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_path CloudwatchEventTarget#input_path}.
        :param input_transformer: input_transformer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_transformer CloudwatchEventTarget#input_transformer}
        :param kinesis_target: kinesis_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#kinesis_target CloudwatchEventTarget#kinesis_target}
        :param redshift_target: redshift_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#redshift_target CloudwatchEventTarget#redshift_target}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#retry_policy CloudwatchEventTarget#retry_policy}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#role_arn CloudwatchEventTarget#role_arn}.
        :param run_command_targets: run_command_targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#run_command_targets CloudwatchEventTarget#run_command_targets}
        :param sqs_target: sqs_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sqs_target CloudwatchEventTarget#sqs_target}
        :param target_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#target_id CloudwatchEventTarget#target_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(batch_target, dict):
            batch_target = CloudwatchEventTargetBatchTarget(**batch_target)
        if isinstance(dead_letter_config, dict):
            dead_letter_config = CloudwatchEventTargetDeadLetterConfig(**dead_letter_config)
        if isinstance(ecs_target, dict):
            ecs_target = CloudwatchEventTargetEcsTarget(**ecs_target)
        if isinstance(http_target, dict):
            http_target = CloudwatchEventTargetHttpTarget(**http_target)
        if isinstance(input_transformer, dict):
            input_transformer = CloudwatchEventTargetInputTransformer(**input_transformer)
        if isinstance(kinesis_target, dict):
            kinesis_target = CloudwatchEventTargetKinesisTarget(**kinesis_target)
        if isinstance(redshift_target, dict):
            redshift_target = CloudwatchEventTargetRedshiftTarget(**redshift_target)
        if isinstance(retry_policy, dict):
            retry_policy = CloudwatchEventTargetRetryPolicy(**retry_policy)
        if isinstance(sqs_target, dict):
            sqs_target = CloudwatchEventTargetSqsTarget(**sqs_target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889f7231a310d057fdf235aec5d0485ce34deb511d8f845980769377b2e6e8d4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument batch_target", value=batch_target, expected_type=type_hints["batch_target"])
            check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
            check_type(argname="argument ecs_target", value=ecs_target, expected_type=type_hints["ecs_target"])
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
            check_type(argname="argument http_target", value=http_target, expected_type=type_hints["http_target"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument input_transformer", value=input_transformer, expected_type=type_hints["input_transformer"])
            check_type(argname="argument kinesis_target", value=kinesis_target, expected_type=type_hints["kinesis_target"])
            check_type(argname="argument redshift_target", value=redshift_target, expected_type=type_hints["redshift_target"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument run_command_targets", value=run_command_targets, expected_type=type_hints["run_command_targets"])
            check_type(argname="argument sqs_target", value=sqs_target, expected_type=type_hints["sqs_target"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "rule": rule,
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
        if batch_target is not None:
            self._values["batch_target"] = batch_target
        if dead_letter_config is not None:
            self._values["dead_letter_config"] = dead_letter_config
        if ecs_target is not None:
            self._values["ecs_target"] = ecs_target
        if event_bus_name is not None:
            self._values["event_bus_name"] = event_bus_name
        if http_target is not None:
            self._values["http_target"] = http_target
        if id is not None:
            self._values["id"] = id
        if input is not None:
            self._values["input"] = input
        if input_path is not None:
            self._values["input_path"] = input_path
        if input_transformer is not None:
            self._values["input_transformer"] = input_transformer
        if kinesis_target is not None:
            self._values["kinesis_target"] = kinesis_target
        if redshift_target is not None:
            self._values["redshift_target"] = redshift_target
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if run_command_targets is not None:
            self._values["run_command_targets"] = run_command_targets
        if sqs_target is not None:
            self._values["sqs_target"] = sqs_target
        if target_id is not None:
            self._values["target_id"] = target_id

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
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#rule CloudwatchEventTarget#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_target(self) -> typing.Optional[CloudwatchEventTargetBatchTarget]:
        '''batch_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#batch_target CloudwatchEventTarget#batch_target}
        '''
        result = self._values.get("batch_target")
        return typing.cast(typing.Optional[CloudwatchEventTargetBatchTarget], result)

    @builtins.property
    def dead_letter_config(
        self,
    ) -> typing.Optional["CloudwatchEventTargetDeadLetterConfig"]:
        '''dead_letter_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#dead_letter_config CloudwatchEventTarget#dead_letter_config}
        '''
        result = self._values.get("dead_letter_config")
        return typing.cast(typing.Optional["CloudwatchEventTargetDeadLetterConfig"], result)

    @builtins.property
    def ecs_target(self) -> typing.Optional["CloudwatchEventTargetEcsTarget"]:
        '''ecs_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#ecs_target CloudwatchEventTarget#ecs_target}
        '''
        result = self._values.get("ecs_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetEcsTarget"], result)

    @builtins.property
    def event_bus_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#event_bus_name CloudwatchEventTarget#event_bus_name}.'''
        result = self._values.get("event_bus_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_target(self) -> typing.Optional["CloudwatchEventTargetHttpTarget"]:
        '''http_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#http_target CloudwatchEventTarget#http_target}
        '''
        result = self._values.get("http_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetHttpTarget"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#id CloudwatchEventTarget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input CloudwatchEventTarget#input}.'''
        result = self._values.get("input")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_path CloudwatchEventTarget#input_path}.'''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_transformer(
        self,
    ) -> typing.Optional["CloudwatchEventTargetInputTransformer"]:
        '''input_transformer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_transformer CloudwatchEventTarget#input_transformer}
        '''
        result = self._values.get("input_transformer")
        return typing.cast(typing.Optional["CloudwatchEventTargetInputTransformer"], result)

    @builtins.property
    def kinesis_target(self) -> typing.Optional["CloudwatchEventTargetKinesisTarget"]:
        '''kinesis_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#kinesis_target CloudwatchEventTarget#kinesis_target}
        '''
        result = self._values.get("kinesis_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetKinesisTarget"], result)

    @builtins.property
    def redshift_target(self) -> typing.Optional["CloudwatchEventTargetRedshiftTarget"]:
        '''redshift_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#redshift_target CloudwatchEventTarget#redshift_target}
        '''
        result = self._values.get("redshift_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetRedshiftTarget"], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["CloudwatchEventTargetRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#retry_policy CloudwatchEventTarget#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["CloudwatchEventTargetRetryPolicy"], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#role_arn CloudwatchEventTarget#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_command_targets(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]]:
        '''run_command_targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#run_command_targets CloudwatchEventTarget#run_command_targets}
        '''
        result = self._values.get("run_command_targets")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetRunCommandTargets"]]], result)

    @builtins.property
    def sqs_target(self) -> typing.Optional["CloudwatchEventTargetSqsTarget"]:
        '''sqs_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sqs_target CloudwatchEventTarget#sqs_target}
        '''
        result = self._values.get("sqs_target")
        return typing.cast(typing.Optional["CloudwatchEventTargetSqsTarget"], result)

    @builtins.property
    def target_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#target_id CloudwatchEventTarget#target_id}.'''
        result = self._values.get("target_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetDeadLetterConfig",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn"},
)
class CloudwatchEventTargetDeadLetterConfig:
    def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4899971860ef5214db6265c377335b5fc07cba6edad9651612a08c783987c09d)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#arn CloudwatchEventTarget#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetDeadLetterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetDeadLetterConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetDeadLetterConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e64bc4b2b46755f20de495d972cec6a8f328854015bc70091ff761ada12e20b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b14cfa3231284f93d41cb1f6d7872a37c5f5d595361a6c515b2e9d72e51902a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetDeadLetterConfig]:
        return typing.cast(typing.Optional[CloudwatchEventTargetDeadLetterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetDeadLetterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aa316b09a2530e564fd928c9afbdc1aa574fa6f344d15961fee0dbe01fddafc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTarget",
    jsii_struct_bases=[],
    name_mapping={
        "task_definition_arn": "taskDefinitionArn",
        "capacity_provider_strategy": "capacityProviderStrategy",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "group": "group",
        "launch_type": "launchType",
        "network_configuration": "networkConfiguration",
        "placement_constraint": "placementConstraint",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "tags": "tags",
        "task_count": "taskCount",
    },
)
class CloudwatchEventTargetEcsTarget:
    def __init__(
        self,
        *,
        task_definition_arn: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetCapacityProviderStrategy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["CloudwatchEventTargetEcsTargetNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        placement_constraint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetPlacementConstraint", typing.Dict[builtins.str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param task_definition_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_definition_arn CloudwatchEventTarget#task_definition_arn}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#capacity_provider_strategy CloudwatchEventTarget#capacity_provider_strategy}
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_ecs_managed_tags CloudwatchEventTarget#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_execute_command CloudwatchEventTarget#enable_execute_command}.
        :param group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#group CloudwatchEventTarget#group}.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#launch_type CloudwatchEventTarget#launch_type}.
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#network_configuration CloudwatchEventTarget#network_configuration}
        :param placement_constraint: placement_constraint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#placement_constraint CloudwatchEventTarget#placement_constraint}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#platform_version CloudwatchEventTarget#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#propagate_tags CloudwatchEventTarget#propagate_tags}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#tags CloudwatchEventTarget#tags}.
        :param task_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_count CloudwatchEventTarget#task_count}.
        '''
        if isinstance(network_configuration, dict):
            network_configuration = CloudwatchEventTargetEcsTargetNetworkConfiguration(**network_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2bf7278615cb8a9d0abeab0e0c0753c6dac56e60dc39dad24a615fd6f206e00)
            check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
            check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument placement_constraint", value=placement_constraint, expected_type=type_hints["placement_constraint"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_definition_arn": task_definition_arn,
        }
        if capacity_provider_strategy is not None:
            self._values["capacity_provider_strategy"] = capacity_provider_strategy
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if group is not None:
            self._values["group"] = group
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if placement_constraint is not None:
            self._values["placement_constraint"] = placement_constraint
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if tags is not None:
            self._values["tags"] = tags
        if task_count is not None:
            self._values["task_count"] = task_count

    @builtins.property
    def task_definition_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_definition_arn CloudwatchEventTarget#task_definition_arn}.'''
        result = self._values.get("task_definition_arn")
        assert result is not None, "Required property 'task_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetEcsTargetCapacityProviderStrategy"]]]:
        '''capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#capacity_provider_strategy CloudwatchEventTarget#capacity_provider_strategy}
        '''
        result = self._values.get("capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetEcsTargetCapacityProviderStrategy"]]], result)

    @builtins.property
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_ecs_managed_tags CloudwatchEventTarget#enable_ecs_managed_tags}.'''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_execute_command(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#enable_execute_command CloudwatchEventTarget#enable_execute_command}.'''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#group CloudwatchEventTarget#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#launch_type CloudwatchEventTarget#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["CloudwatchEventTargetEcsTargetNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#network_configuration CloudwatchEventTarget#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["CloudwatchEventTargetEcsTargetNetworkConfiguration"], result)

    @builtins.property
    def placement_constraint(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]]:
        '''placement_constraint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#placement_constraint CloudwatchEventTarget#placement_constraint}
        '''
        result = self._values.get("placement_constraint")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#platform_version CloudwatchEventTarget#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#propagate_tags CloudwatchEventTarget#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#tags CloudwatchEventTarget#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#task_count CloudwatchEventTarget#task_count}.'''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "base": "base",
        "weight": "weight",
    },
)
class CloudwatchEventTargetEcsTargetCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        base: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#capacity_provider CloudwatchEventTarget#capacity_provider}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#base CloudwatchEventTarget#base}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#weight CloudwatchEventTarget#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16140419bfe12c76de8ff0670374ff44b60596ecb999b436a99489836d53a724)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_provider": capacity_provider,
        }
        if base is not None:
            self._values["base"] = base
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#capacity_provider CloudwatchEventTarget#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#base CloudwatchEventTarget#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#weight CloudwatchEventTarget#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTargetCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetEcsTargetCapacityProviderStrategyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetCapacityProviderStrategyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86660e95075b3337b5ade6bbe48a87b01edb0bf7a124ea7a94464d4d48cc0c68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventTargetEcsTargetCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56302da4d87e28125fabbdf76babaf2fdafcb7aef3d541c4f679357e4ff8605)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventTargetEcsTargetCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93b2ad39932cd75e437a579e0c4ea8ddacb2e970b8318e6a0db91f53b5a45b10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc7b5bf797d8fa1ae3cffa77a8a33a28878a014edbf37838d194a6136e6488a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70675b8fe403d17ea9d44759f1685712b5f0e32003b3995e385eb81c1b9ba25f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1689090076fd6bf6c2dd0c4cf517665bc3bd2f94838300aeaa527c8c89e6f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetEcsTargetCapacityProviderStrategyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetCapacityProviderStrategyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ea353c522969aed96fb84781fbdfaeb35e5f32a4b7f2b2046aca539122c3ba5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab36451f093fbce3b3d0761df20255c7603bc4fda8507d4b43dad688c6d2afcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90953ab01c7a25922025b9014c8dfed4cedd5e9f4fa35f652dcfd8bd2fd3a49c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d2b6a1feaaedb5f8351976a372ed3cfd026cf5eda5767a7b79155ade83a836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeed9074987d070c5c61bf7b419711b2dae8347c1c0d9b86734c5e9ef9017e37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class CloudwatchEventTargetEcsTargetNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#subnets CloudwatchEventTarget#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#assign_public_ip CloudwatchEventTarget#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#security_groups CloudwatchEventTarget#security_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb73837a6b19d13574574d260445482f59953f50c369a5999f55f9be3d7d0b54)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnets": subnets,
        }
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#subnets CloudwatchEventTarget#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#assign_public_ip CloudwatchEventTarget#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#security_groups CloudwatchEventTarget#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTargetNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18d357ca80b36a234f0d88d6c9111053527bf2c8f657592eb0eea596c66fa210)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40d65b0aaf42075d5b66e34a7ba5bf7a9f832e6197e99d3c88f037d780262b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb11135402cd371dedda48722897375791f2520b6737d74d5a10a7fde7a1eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__550e8b601c9562a6fa6a6bcb75b5341eae1217df2608f27dabae0fbebd76536c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration]:
        return typing.cast(typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4726af1d8ef99dcf71e2a0ad3a09e57ea61280f5e9e1629618f1d26385013d9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetEcsTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f424282282302814b5b3b262f2c8162d1c14eef0f5b34e6c0ad71c2d29c8b7e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCapacityProviderStrategy")
    def put_capacity_provider_strategy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87268a8662a74713fe00395043dd854482ce1616ff7b1ca1a8eb52d050b3bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#subnets CloudwatchEventTarget#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#assign_public_ip CloudwatchEventTarget#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#security_groups CloudwatchEventTarget#security_groups}.
        '''
        value = CloudwatchEventTargetEcsTargetNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putPlacementConstraint")
    def put_placement_constraint(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwatchEventTargetEcsTargetPlacementConstraint", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__954bb3919c00dd29c50e04fe4aacf03aedde14987db92a289566b2ec46fb1280)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraint", [value]))

    @jsii.member(jsii_name="resetCapacityProviderStrategy")
    def reset_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetEnableEcsManagedTags")
    def reset_enable_ecs_managed_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEcsManagedTags", []))

    @jsii.member(jsii_name="resetEnableExecuteCommand")
    def reset_enable_execute_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExecuteCommand", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetPlacementConstraint")
    def reset_placement_constraint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraint", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTaskCount")
    def reset_task_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskCount", []))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategy")
    def capacity_provider_strategy(
        self,
    ) -> CloudwatchEventTargetEcsTargetCapacityProviderStrategyList:
        return typing.cast(CloudwatchEventTargetEcsTargetCapacityProviderStrategyList, jsii.get(self, "capacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference:
        return typing.cast(CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference, jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraint")
    def placement_constraint(
        self,
    ) -> "CloudwatchEventTargetEcsTargetPlacementConstraintList":
        return typing.cast("CloudwatchEventTargetEcsTargetPlacementConstraintList", jsii.get(self, "placementConstraint"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategyInput")
    def capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetCapacityProviderStrategy]]], jsii.get(self, "capacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTagsInput")
    def enable_ecs_managed_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEcsManagedTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommandInput")
    def enable_execute_command_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableExecuteCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration]:
        return typing.cast(typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintInput")
    def placement_constraint_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwatchEventTargetEcsTargetPlacementConstraint"]]], jsii.get(self, "placementConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskCountInput")
    def task_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskCountInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArnInput")
    def task_definition_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTags")
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEcsManagedTags"))

    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeaf6a88bae193ec6a9555fb42990f1b2705886fbfa2c27cd2509b5746f64971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEcsManagedTags", value)

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommand")
    def enable_execute_command(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableExecuteCommand"))

    @enable_execute_command.setter
    def enable_execute_command(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7fcd8bd0366ece6a7e0f11374a4b6f7b277419116ca8919e18841e11d1e4ab4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExecuteCommand", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6cba7bce9371707ac23394adad312f335c05c91ec3eabb07dffd5cab7b4a0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca61b1ce0c8ee35b4a078c3fe80c161224b8ae9878204a4055178a8d4c1c6264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value)

    @builtins.property
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d6afe18022156659244dcf0da85abb4d298411fa63315326c300ab1af45344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2297ae23848a0b4b116a60dc7fb81849e8ed1656d1ddf56134b59d1d41577c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be776988133ee6c2c1b090ed725689400f571a699a8b0fc675e43eaedfe69a4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="taskCount")
    def task_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskCount"))

    @task_count.setter
    def task_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8765c30b0360c537ba2e0dbc73a0ca54b2744d8aec27b023efc79e070c6e07dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskCount", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionArn")
    def task_definition_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinitionArn"))

    @task_definition_arn.setter
    def task_definition_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6bd3f762621f3f1008ade557357fbc1e7b7312205af9693ec4a42787de1f7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinitionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetEcsTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetEcsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetEcsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06be6d560cd7c524e20ab439c2bca29680fb92e9d9f00d060304906298f47948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetPlacementConstraint",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class CloudwatchEventTargetEcsTargetPlacementConstraint:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#type CloudwatchEventTarget#type}.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#expression CloudwatchEventTarget#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef764a48f158da0bbb53dd4350de0015435f2e6c202a56da74e53db8131cc2d)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#type CloudwatchEventTarget#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#expression CloudwatchEventTarget#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetEcsTargetPlacementConstraint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetEcsTargetPlacementConstraintList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetPlacementConstraintList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8228f4351c0a5de6dbd21d51e18484b128ccceb977dbc285c909ee84c8f1f864)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04d39826cbd4f76b4e4ebc0734a36d2268b0617847343a63f718bac5d9650e09)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a741ba45a21a48a63bb4779370fd5ff86fe05435b6bb10b49aeeef54b5524a07)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb7cf98ddde4092f626bdba2b1f7a3383cec09bf46de9b00285d0ea97f61c79a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f00654229bca394ee1123e74fa1b870c38d3cd2704b737668f8ed29c2a09e585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d816f1e2af40cc0f6af09db41fc3b9590793a1fec8254a9a206e73efe548648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dc85f94751157ac0f6dcccbc174ef845ec669f72752cab36f6e02142f8c3924)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091cadbfe4c2808673404e87351c5a51f91946aeb69c3b6b30c359d3f4c86b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6416245d67ddf028cd28ea680b59f58a48e2688f40325e97052124da0659929)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f393d725f16e18303ee7248b69ec0bf19d6994bd253bbd14fe4f5bd7bf2b7a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetHttpTarget",
    jsii_struct_bases=[],
    name_mapping={
        "header_parameters": "headerParameters",
        "path_parameter_values": "pathParameterValues",
        "query_string_parameters": "queryStringParameters",
    },
)
class CloudwatchEventTargetHttpTarget:
    def __init__(
        self,
        *,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param header_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#header_parameters CloudwatchEventTarget#header_parameters}.
        :param path_parameter_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#path_parameter_values CloudwatchEventTarget#path_parameter_values}.
        :param query_string_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#query_string_parameters CloudwatchEventTarget#query_string_parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c347a8d1815e4322209d97a4602d9896baf51171c31e2a5d39f9e5041f8534a)
            check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
            check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if header_parameters is not None:
            self._values["header_parameters"] = header_parameters
        if path_parameter_values is not None:
            self._values["path_parameter_values"] = path_parameter_values
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters

    @builtins.property
    def header_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#header_parameters CloudwatchEventTarget#header_parameters}.'''
        result = self._values.get("header_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#path_parameter_values CloudwatchEventTarget#path_parameter_values}.'''
        result = self._values.get("path_parameter_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#query_string_parameters CloudwatchEventTarget#query_string_parameters}.'''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetHttpTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetHttpTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetHttpTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f20eb0b420829d8c3cfb208e0afe4c0ebdd53ccf6e2bcb8c1daac122fd535907)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHeaderParameters")
    def reset_header_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderParameters", []))

    @jsii.member(jsii_name="resetPathParameterValues")
    def reset_path_parameter_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathParameterValues", []))

    @jsii.member(jsii_name="resetQueryStringParameters")
    def reset_query_string_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringParameters", []))

    @builtins.property
    @jsii.member(jsii_name="headerParametersInput")
    def header_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headerParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="pathParameterValuesInput")
    def path_parameter_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathParameterValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringParametersInput")
    def query_string_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "queryStringParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="headerParameters")
    def header_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headerParameters"))

    @header_parameters.setter
    def header_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e876283db6bb360c9eccfc23d7583c993b7e95441e89b5db9277f67482f8dff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerParameters", value)

    @builtins.property
    @jsii.member(jsii_name="pathParameterValues")
    def path_parameter_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathParameterValues"))

    @path_parameter_values.setter
    def path_parameter_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__004c7c9e3b3832a1aebec44ede62b1d34abd2c7fcd27bd6dcfce69c3776dc42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathParameterValues", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringParameters")
    def query_string_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "queryStringParameters"))

    @query_string_parameters.setter
    def query_string_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1129becec409f139f94b3705a3c4fe8a2738d444b55fc79d6103bfc210657a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringParameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetHttpTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetHttpTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetHttpTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3ce9b2d9fb59046214b1326fda0899d02bc911aac4dd0adfa92c45ec75cb0c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetInputTransformer",
    jsii_struct_bases=[],
    name_mapping={"input_template": "inputTemplate", "input_paths": "inputPaths"},
)
class CloudwatchEventTargetInputTransformer:
    def __init__(
        self,
        *,
        input_template: builtins.str,
        input_paths: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param input_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_template CloudwatchEventTarget#input_template}.
        :param input_paths: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_paths CloudwatchEventTarget#input_paths}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37cfe261cd554f34673b83b2cc320898a1a37196a188ac9f32c9d511076d21c1)
            check_type(argname="argument input_template", value=input_template, expected_type=type_hints["input_template"])
            check_type(argname="argument input_paths", value=input_paths, expected_type=type_hints["input_paths"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_template": input_template,
        }
        if input_paths is not None:
            self._values["input_paths"] = input_paths

    @builtins.property
    def input_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_template CloudwatchEventTarget#input_template}.'''
        result = self._values.get("input_template")
        assert result is not None, "Required property 'input_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_paths(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#input_paths CloudwatchEventTarget#input_paths}.'''
        result = self._values.get("input_paths")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetInputTransformer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetInputTransformerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetInputTransformerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0de1b4150e68504bdf5bdcef612b57082c8a7b15c90fb435a27edb62d8921d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInputPaths")
    def reset_input_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputPaths", []))

    @builtins.property
    @jsii.member(jsii_name="inputPathsInput")
    def input_paths_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "inputPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="inputTemplateInput")
    def input_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="inputPaths")
    def input_paths(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "inputPaths"))

    @input_paths.setter
    def input_paths(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7d5920db4b0f441a0231ef610e66d1aacef43aadedb0b08f477eff3a2faa44c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputPaths", value)

    @builtins.property
    @jsii.member(jsii_name="inputTemplate")
    def input_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputTemplate"))

    @input_template.setter
    def input_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e916a0688858a649c9938659ad95ecd906ce4fcfc3ef865524fced18238c50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetInputTransformer]:
        return typing.cast(typing.Optional[CloudwatchEventTargetInputTransformer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetInputTransformer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813c56bd285644483591b4a0348fc59d88df6f24da557f69828fc4144c83e32e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetKinesisTarget",
    jsii_struct_bases=[],
    name_mapping={"partition_key_path": "partitionKeyPath"},
)
class CloudwatchEventTargetKinesisTarget:
    def __init__(
        self,
        *,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param partition_key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#partition_key_path CloudwatchEventTarget#partition_key_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a1910740f9c1ed3b836f73f1595bb3612dbaed532449cfe7bbe6005037b4cf)
            check_type(argname="argument partition_key_path", value=partition_key_path, expected_type=type_hints["partition_key_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if partition_key_path is not None:
            self._values["partition_key_path"] = partition_key_path

    @builtins.property
    def partition_key_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#partition_key_path CloudwatchEventTarget#partition_key_path}.'''
        result = self._values.get("partition_key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetKinesisTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetKinesisTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetKinesisTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d3c13853ac158f60b9f96cd612f65c5061aaf7b74ec5598fef7f82f17d2264b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPartitionKeyPath")
    def reset_partition_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKeyPath", []))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyPathInput")
    def partition_key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyPath")
    def partition_key_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKeyPath"))

    @partition_key_path.setter
    def partition_key_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f3ad2869bed58d22642db8e3e81eb93b2445f17ee99dbe2d58fd5eee5a97c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKeyPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetKinesisTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetKinesisTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetKinesisTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c4d3868c8b17235904aeb3277428212cb45b7639d4ed7525f36240c20d13712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRedshiftTarget",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "db_user": "dbUser",
        "secrets_manager_arn": "secretsManagerArn",
        "sql": "sql",
        "statement_name": "statementName",
        "with_event": "withEvent",
    },
)
class CloudwatchEventTargetRedshiftTarget:
    def __init__(
        self,
        *,
        database: builtins.str,
        db_user: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        sql: typing.Optional[builtins.str] = None,
        statement_name: typing.Optional[builtins.str] = None,
        with_event: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#database CloudwatchEventTarget#database}.
        :param db_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#db_user CloudwatchEventTarget#db_user}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#secrets_manager_arn CloudwatchEventTarget#secrets_manager_arn}.
        :param sql: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sql CloudwatchEventTarget#sql}.
        :param statement_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#statement_name CloudwatchEventTarget#statement_name}.
        :param with_event: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#with_event CloudwatchEventTarget#with_event}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04bdbbdef4527bac046c9d176789863d1df028562f9646790ad9af7d2a2b79d2)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument db_user", value=db_user, expected_type=type_hints["db_user"])
            check_type(argname="argument secrets_manager_arn", value=secrets_manager_arn, expected_type=type_hints["secrets_manager_arn"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument statement_name", value=statement_name, expected_type=type_hints["statement_name"])
            check_type(argname="argument with_event", value=with_event, expected_type=type_hints["with_event"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
        }
        if db_user is not None:
            self._values["db_user"] = db_user
        if secrets_manager_arn is not None:
            self._values["secrets_manager_arn"] = secrets_manager_arn
        if sql is not None:
            self._values["sql"] = sql
        if statement_name is not None:
            self._values["statement_name"] = statement_name
        if with_event is not None:
            self._values["with_event"] = with_event

    @builtins.property
    def database(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#database CloudwatchEventTarget#database}.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#db_user CloudwatchEventTarget#db_user}.'''
        result = self._values.get("db_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_manager_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#secrets_manager_arn CloudwatchEventTarget#secrets_manager_arn}.'''
        result = self._values.get("secrets_manager_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#sql CloudwatchEventTarget#sql}.'''
        result = self._values.get("sql")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#statement_name CloudwatchEventTarget#statement_name}.'''
        result = self._values.get("statement_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def with_event(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#with_event CloudwatchEventTarget#with_event}.'''
        result = self._values.get("with_event")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetRedshiftTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetRedshiftTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRedshiftTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85285ea558b2f2d48efea58b0292602e08998fafde0c4b76def04d121f701794)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDbUser")
    def reset_db_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbUser", []))

    @jsii.member(jsii_name="resetSecretsManagerArn")
    def reset_secrets_manager_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerArn", []))

    @jsii.member(jsii_name="resetSql")
    def reset_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSql", []))

    @jsii.member(jsii_name="resetStatementName")
    def reset_statement_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementName", []))

    @jsii.member(jsii_name="resetWithEvent")
    def reset_with_event(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithEvent", []))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dbUserInput")
    def db_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbUserInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArnInput")
    def secrets_manager_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlInput")
    def sql_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlInput"))

    @builtins.property
    @jsii.member(jsii_name="statementNameInput")
    def statement_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="withEventInput")
    def with_event_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "withEventInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe607f453290f3fc76031bc9062953f6c2c9fd90dd871994381845eefcf0bc51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="dbUser")
    def db_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbUser"))

    @db_user.setter
    def db_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a33969440aa93570b6fdd39bf93423a44f5fab6045ed31b92f394dcc9040fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbUser", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d740786c83f3d2161f68537930e9d5c69261507563032e6b8ff908d6930d20c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerArn", value)

    @builtins.property
    @jsii.member(jsii_name="sql")
    def sql(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sql"))

    @sql.setter
    def sql(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8495c0a6094556f12e2759b7f2dab02d7e21d095b2818362d0399e1a2d462c51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sql", value)

    @builtins.property
    @jsii.member(jsii_name="statementName")
    def statement_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementName"))

    @statement_name.setter
    def statement_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83333c12df477f4a4535e1f1aa8cae0638970b6da01d217537f128c09f7fba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementName", value)

    @builtins.property
    @jsii.member(jsii_name="withEvent")
    def with_event(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "withEvent"))

    @with_event.setter
    def with_event(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__238662c14a9492063729211ac7a56c9ec5fa2d438a38242a69a3e64d03636bb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withEvent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetRedshiftTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetRedshiftTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetRedshiftTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__161297b43d8d5a32ab796ed23ecc00735abe2af0027dc88c81b14e4fdbc3246c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
    },
)
class CloudwatchEventTargetRetryPolicy:
    def __init__(
        self,
        *,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_event_age_in_seconds CloudwatchEventTarget#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_retry_attempts CloudwatchEventTarget#maximum_retry_attempts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__610a4e69be795d8c17b0795c459e3239bc208d2eb5892e6a45f629b6be33cb5c)
            check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
            check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if maximum_event_age_in_seconds is not None:
            self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts

    @builtins.property
    def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_event_age_in_seconds CloudwatchEventTarget#maximum_event_age_in_seconds}.'''
        result = self._values.get("maximum_event_age_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#maximum_retry_attempts CloudwatchEventTarget#maximum_retry_attempts}.'''
        result = self._values.get("maximum_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetRetryPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c29bd3e94c840b6540d89c249a7237238c9b5e1795d37709dc8772b5e910e3a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaximumEventAgeInSeconds")
    def reset_maximum_event_age_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumEventAgeInSeconds", []))

    @jsii.member(jsii_name="resetMaximumRetryAttempts")
    def reset_maximum_retry_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumRetryAttempts", []))

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSecondsInput")
    def maximum_event_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumEventAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttemptsInput")
    def maximum_retry_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumRetryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumEventAgeInSeconds"))

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e21d5695fdedce245a0f32ca3bec183c2ed28544b577a32026a0a185b8b826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumEventAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumRetryAttempts"))

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db398dcdae6864a00569609dc31cb6283574471c4a4b98b707698f6fe01db11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumRetryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetRetryPolicy]:
        return typing.cast(typing.Optional[CloudwatchEventTargetRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9651947df7b9a1fcfa430323fcb86cbe62cba89665092218df94cc7feacd82f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRunCommandTargets",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class CloudwatchEventTargetRunCommandTargets:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#key CloudwatchEventTarget#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#values CloudwatchEventTarget#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1770731e1a000d994ab0c331e3526f9f0b34e1c5f0361633f37f5a8e41acde9d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#key CloudwatchEventTarget#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#values CloudwatchEventTarget#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetRunCommandTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetRunCommandTargetsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRunCommandTargetsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0900de0d6eb09e2eff4b7d5009ed76990bd65cbc97fa6155bd9b58193e76cc90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwatchEventTargetRunCommandTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e785466817b853eff2d15c44cb16459f352f601c23628783ca75a982cd5dbc1b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwatchEventTargetRunCommandTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8ed0149b9b38f9710661eb37abb8ea4320a5f73bda362343e9120fb1e87ce4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ae94e5b67aff5514cebb2f61044f3a7ee767ec18899e994ce96cfaf5ae142f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0689b06f51a7a5679d4130f6147eccab501a623a223f1cb68f8bbd402e9f99e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9828cda576f20880a3fc55f3a5645088bb5b6efd882a3a3e32f8116b5d487b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwatchEventTargetRunCommandTargetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetRunCommandTargetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__152ec6188310e262baa5166883ff2dadcc598a81a6fbe7d9d019d65a40dcc060)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e967ceacd0478a9cd7d467c235397af5b816c0773bf39eee04b8fc5b3b26f47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658fc0ac0af8dd996f539147e64fca546b7a3a662c660e690e3deca685269e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__905f3809917699ea17fd677db30d6840de6e879bf4a1bad5bad4ed508e4cb359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetSqsTarget",
    jsii_struct_bases=[],
    name_mapping={"message_group_id": "messageGroupId"},
)
class CloudwatchEventTargetSqsTarget:
    def __init__(
        self,
        *,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#message_group_id CloudwatchEventTarget#message_group_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913bbb22d9567d596ffb04b714f86e64b0e5a92d1633140e5e9eb047e455ac7b)
            check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if message_group_id is not None:
            self._values["message_group_id"] = message_group_id

    @builtins.property
    def message_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target#message_group_id CloudwatchEventTarget#message_group_id}.'''
        result = self._values.get("message_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwatchEventTargetSqsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwatchEventTargetSqsTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudwatchEventTarget.CloudwatchEventTargetSqsTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2e4bf63e7cc0a20ed5f1f01e80dffd6c7a9ad0cee307b90a8f8fa311114b4c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessageGroupId")
    def reset_message_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="messageGroupIdInput")
    def message_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="messageGroupId")
    def message_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageGroupId"))

    @message_group_id.setter
    def message_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd4f93692425971bef906e73bbdc1e28ed7f13badfb82fc261d1c3ed92a0aace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudwatchEventTargetSqsTarget]:
        return typing.cast(typing.Optional[CloudwatchEventTargetSqsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudwatchEventTargetSqsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8101be0ae955a65fad5c5f13bbedbe0dad5d07f3076e6dbf30b307f7ea3b0cae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudwatchEventTarget",
    "CloudwatchEventTargetBatchTarget",
    "CloudwatchEventTargetBatchTargetOutputReference",
    "CloudwatchEventTargetConfig",
    "CloudwatchEventTargetDeadLetterConfig",
    "CloudwatchEventTargetDeadLetterConfigOutputReference",
    "CloudwatchEventTargetEcsTarget",
    "CloudwatchEventTargetEcsTargetCapacityProviderStrategy",
    "CloudwatchEventTargetEcsTargetCapacityProviderStrategyList",
    "CloudwatchEventTargetEcsTargetCapacityProviderStrategyOutputReference",
    "CloudwatchEventTargetEcsTargetNetworkConfiguration",
    "CloudwatchEventTargetEcsTargetNetworkConfigurationOutputReference",
    "CloudwatchEventTargetEcsTargetOutputReference",
    "CloudwatchEventTargetEcsTargetPlacementConstraint",
    "CloudwatchEventTargetEcsTargetPlacementConstraintList",
    "CloudwatchEventTargetEcsTargetPlacementConstraintOutputReference",
    "CloudwatchEventTargetHttpTarget",
    "CloudwatchEventTargetHttpTargetOutputReference",
    "CloudwatchEventTargetInputTransformer",
    "CloudwatchEventTargetInputTransformerOutputReference",
    "CloudwatchEventTargetKinesisTarget",
    "CloudwatchEventTargetKinesisTargetOutputReference",
    "CloudwatchEventTargetRedshiftTarget",
    "CloudwatchEventTargetRedshiftTargetOutputReference",
    "CloudwatchEventTargetRetryPolicy",
    "CloudwatchEventTargetRetryPolicyOutputReference",
    "CloudwatchEventTargetRunCommandTargets",
    "CloudwatchEventTargetRunCommandTargetsList",
    "CloudwatchEventTargetRunCommandTargetsOutputReference",
    "CloudwatchEventTargetSqsTarget",
    "CloudwatchEventTargetSqsTargetOutputReference",
]

publication.publish()

def _typecheckingstub__2841400388f1eb22d9fb517ac6ea298d64c51453775df58fded90a07ff67fdcc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    arn: builtins.str,
    rule: builtins.str,
    batch_target: typing.Optional[typing.Union[CloudwatchEventTargetBatchTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_config: typing.Optional[typing.Union[CloudwatchEventTargetDeadLetterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ecs_target: typing.Optional[typing.Union[CloudwatchEventTargetEcsTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    event_bus_name: typing.Optional[builtins.str] = None,
    http_target: typing.Optional[typing.Union[CloudwatchEventTargetHttpTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    input: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    input_transformer: typing.Optional[typing.Union[CloudwatchEventTargetInputTransformer, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_target: typing.Optional[typing.Union[CloudwatchEventTargetKinesisTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift_target: typing.Optional[typing.Union[CloudwatchEventTargetRedshiftTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_policy: typing.Optional[typing.Union[CloudwatchEventTargetRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    run_command_targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetRunCommandTargets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sqs_target: typing.Optional[typing.Union[CloudwatchEventTargetSqsTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    target_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4bcdcf7f7c9729212861af003dd83ffabc6c76f331120cf271c24a6363cdb803(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetRunCommandTargets, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a94c98d1db20f1b639c681ad0c61bfa8d30113955669d0f26225717db343d75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82dcff8f16dd736e1c11ddebdf62162c892a51b3fc52ed3fb22ef0872c85f48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723134b38984a55a9fbd59e10a189b902ac81d52b0854d92857141ef46d49d42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e24cc0f717d6c47ea0f55b7391065e491442f8ddd0b1039ae28fab867ae54884(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097678e57e039eb7014b41579c2c350d31ae5d45ec735184b819b5bb61790d20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2503f1a06a773c0fe5ccc796060202ba11c515a99ef5af9d2c5869744a629e90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a75b370d72a84a06885932c48ee89d09bc2c149b4d55de14656bc49f034ac36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c38fb5fcedbd9b3509e21b3e870ceb800c5a093f7d3d2f0a69f04f1f96b91be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec5dbce9617af422336001e68cf6423258145551b389ccd12db500dadf91225(
    *,
    job_definition: builtins.str,
    job_name: builtins.str,
    array_size: typing.Optional[jsii.Number] = None,
    job_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390b81c13873856dcd23e96cb4b09e7c892eb57f7639c407c6647aef1d6bbe62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6899ef36ef9194747fcc38115f5cef6ab8cd49cbeff9961d137e08e596bd4fa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de40a91b9fed57d611b0800a7e8fe19a211d6e3dd47cd225616d898464c47ba2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3648bc685dea2b7e7430f140d2c959c37227bfaaaef7afc2ed8d76c73f4bd7b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06741ddabd23cfdb1de0ce4fcd7c411e71ce155b8126972bdac2bbcab05dd204(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de4693a8f6782eed232b8cf681f7fa1b027995f1ef139996151379fdc781716b(
    value: typing.Optional[CloudwatchEventTargetBatchTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889f7231a310d057fdf235aec5d0485ce34deb511d8f845980769377b2e6e8d4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    arn: builtins.str,
    rule: builtins.str,
    batch_target: typing.Optional[typing.Union[CloudwatchEventTargetBatchTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_config: typing.Optional[typing.Union[CloudwatchEventTargetDeadLetterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ecs_target: typing.Optional[typing.Union[CloudwatchEventTargetEcsTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    event_bus_name: typing.Optional[builtins.str] = None,
    http_target: typing.Optional[typing.Union[CloudwatchEventTargetHttpTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    input: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    input_transformer: typing.Optional[typing.Union[CloudwatchEventTargetInputTransformer, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_target: typing.Optional[typing.Union[CloudwatchEventTargetKinesisTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift_target: typing.Optional[typing.Union[CloudwatchEventTargetRedshiftTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_policy: typing.Optional[typing.Union[CloudwatchEventTargetRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    run_command_targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetRunCommandTargets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sqs_target: typing.Optional[typing.Union[CloudwatchEventTargetSqsTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    target_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4899971860ef5214db6265c377335b5fc07cba6edad9651612a08c783987c09d(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64bc4b2b46755f20de495d972cec6a8f328854015bc70091ff761ada12e20b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b14cfa3231284f93d41cb1f6d7872a37c5f5d595361a6c515b2e9d72e51902a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aa316b09a2530e564fd928c9afbdc1aa574fa6f344d15961fee0dbe01fddafc(
    value: typing.Optional[CloudwatchEventTargetDeadLetterConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2bf7278615cb8a9d0abeab0e0c0753c6dac56e60dc39dad24a615fd6f206e00(
    *,
    task_definition_arn: builtins.str,
    capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    placement_constraint: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, typing.Dict[builtins.str, typing.Any]]]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    task_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16140419bfe12c76de8ff0670374ff44b60596ecb999b436a99489836d53a724(
    *,
    capacity_provider: builtins.str,
    base: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86660e95075b3337b5ade6bbe48a87b01edb0bf7a124ea7a94464d4d48cc0c68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56302da4d87e28125fabbdf76babaf2fdafcb7aef3d541c4f679357e4ff8605(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b2ad39932cd75e437a579e0c4ea8ddacb2e970b8318e6a0db91f53b5a45b10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc7b5bf797d8fa1ae3cffa77a8a33a28878a014edbf37838d194a6136e6488a1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70675b8fe403d17ea9d44759f1685712b5f0e32003b3995e385eb81c1b9ba25f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1689090076fd6bf6c2dd0c4cf517665bc3bd2f94838300aeaa527c8c89e6f59(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetCapacityProviderStrategy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea353c522969aed96fb84781fbdfaeb35e5f32a4b7f2b2046aca539122c3ba5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab36451f093fbce3b3d0761df20255c7603bc4fda8507d4b43dad688c6d2afcd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90953ab01c7a25922025b9014c8dfed4cedd5e9f4fa35f652dcfd8bd2fd3a49c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d2b6a1feaaedb5f8351976a372ed3cfd026cf5eda5767a7b79155ade83a836(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeed9074987d070c5c61bf7b419711b2dae8347c1c0d9b86734c5e9ef9017e37(
    value: typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb73837a6b19d13574574d260445482f59953f50c369a5999f55f9be3d7d0b54(
    *,
    subnets: typing.Sequence[builtins.str],
    assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d357ca80b36a234f0d88d6c9111053527bf2c8f657592eb0eea596c66fa210(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d65b0aaf42075d5b66e34a7ba5bf7a9f832e6197e99d3c88f037d780262b10(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb11135402cd371dedda48722897375791f2520b6737d74d5a10a7fde7a1eb7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550e8b601c9562a6fa6a6bcb75b5341eae1217df2608f27dabae0fbebd76536c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4726af1d8ef99dcf71e2a0ad3a09e57ea61280f5e9e1629618f1d26385013d9f(
    value: typing.Optional[CloudwatchEventTargetEcsTargetNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f424282282302814b5b3b262f2c8162d1c14eef0f5b34e6c0ad71c2d29c8b7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87268a8662a74713fe00395043dd854482ce1616ff7b1ca1a8eb52d050b3bf2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetEcsTargetCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__954bb3919c00dd29c50e04fe4aacf03aedde14987db92a289566b2ec46fb1280(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeaf6a88bae193ec6a9555fb42990f1b2705886fbfa2c27cd2509b5746f64971(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7fcd8bd0366ece6a7e0f11374a4b6f7b277419116ca8919e18841e11d1e4ab4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6cba7bce9371707ac23394adad312f335c05c91ec3eabb07dffd5cab7b4a0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca61b1ce0c8ee35b4a078c3fe80c161224b8ae9878204a4055178a8d4c1c6264(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d6afe18022156659244dcf0da85abb4d298411fa63315326c300ab1af45344(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2297ae23848a0b4b116a60dc7fb81849e8ed1656d1ddf56134b59d1d41577c95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be776988133ee6c2c1b090ed725689400f571a699a8b0fc675e43eaedfe69a4d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8765c30b0360c537ba2e0dbc73a0ca54b2744d8aec27b023efc79e070c6e07dd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6bd3f762621f3f1008ade557357fbc1e7b7312205af9693ec4a42787de1f7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06be6d560cd7c524e20ab439c2bca29680fb92e9d9f00d060304906298f47948(
    value: typing.Optional[CloudwatchEventTargetEcsTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef764a48f158da0bbb53dd4350de0015435f2e6c202a56da74e53db8131cc2d(
    *,
    type: builtins.str,
    expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8228f4351c0a5de6dbd21d51e18484b128ccceb977dbc285c909ee84c8f1f864(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04d39826cbd4f76b4e4ebc0734a36d2268b0617847343a63f718bac5d9650e09(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a741ba45a21a48a63bb4779370fd5ff86fe05435b6bb10b49aeeef54b5524a07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7cf98ddde4092f626bdba2b1f7a3383cec09bf46de9b00285d0ea97f61c79a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00654229bca394ee1123e74fa1b870c38d3cd2704b737668f8ed29c2a09e585(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d816f1e2af40cc0f6af09db41fc3b9590793a1fec8254a9a206e73efe548648(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetEcsTargetPlacementConstraint]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc85f94751157ac0f6dcccbc174ef845ec669f72752cab36f6e02142f8c3924(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091cadbfe4c2808673404e87351c5a51f91946aeb69c3b6b30c359d3f4c86b58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6416245d67ddf028cd28ea680b59f58a48e2688f40325e97052124da0659929(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f393d725f16e18303ee7248b69ec0bf19d6994bd253bbd14fe4f5bd7bf2b7a4(
    value: typing.Optional[typing.Union[CloudwatchEventTargetEcsTargetPlacementConstraint, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c347a8d1815e4322209d97a4602d9896baf51171c31e2a5d39f9e5041f8534a(
    *,
    header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20eb0b420829d8c3cfb208e0afe4c0ebdd53ccf6e2bcb8c1daac122fd535907(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e876283db6bb360c9eccfc23d7583c993b7e95441e89b5db9277f67482f8dff3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004c7c9e3b3832a1aebec44ede62b1d34abd2c7fcd27bd6dcfce69c3776dc42e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1129becec409f139f94b3705a3c4fe8a2738d444b55fc79d6103bfc210657a3c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3ce9b2d9fb59046214b1326fda0899d02bc911aac4dd0adfa92c45ec75cb0c5(
    value: typing.Optional[CloudwatchEventTargetHttpTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37cfe261cd554f34673b83b2cc320898a1a37196a188ac9f32c9d511076d21c1(
    *,
    input_template: builtins.str,
    input_paths: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0de1b4150e68504bdf5bdcef612b57082c8a7b15c90fb435a27edb62d8921d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7d5920db4b0f441a0231ef610e66d1aacef43aadedb0b08f477eff3a2faa44c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e916a0688858a649c9938659ad95ecd906ce4fcfc3ef865524fced18238c50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813c56bd285644483591b4a0348fc59d88df6f24da557f69828fc4144c83e32e(
    value: typing.Optional[CloudwatchEventTargetInputTransformer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a1910740f9c1ed3b836f73f1595bb3612dbaed532449cfe7bbe6005037b4cf(
    *,
    partition_key_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3c13853ac158f60b9f96cd612f65c5061aaf7b74ec5598fef7f82f17d2264b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f3ad2869bed58d22642db8e3e81eb93b2445f17ee99dbe2d58fd5eee5a97c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4d3868c8b17235904aeb3277428212cb45b7639d4ed7525f36240c20d13712(
    value: typing.Optional[CloudwatchEventTargetKinesisTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bdbbdef4527bac046c9d176789863d1df028562f9646790ad9af7d2a2b79d2(
    *,
    database: builtins.str,
    db_user: typing.Optional[builtins.str] = None,
    secrets_manager_arn: typing.Optional[builtins.str] = None,
    sql: typing.Optional[builtins.str] = None,
    statement_name: typing.Optional[builtins.str] = None,
    with_event: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85285ea558b2f2d48efea58b0292602e08998fafde0c4b76def04d121f701794(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe607f453290f3fc76031bc9062953f6c2c9fd90dd871994381845eefcf0bc51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a33969440aa93570b6fdd39bf93423a44f5fab6045ed31b92f394dcc9040fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d740786c83f3d2161f68537930e9d5c69261507563032e6b8ff908d6930d20c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8495c0a6094556f12e2759b7f2dab02d7e21d095b2818362d0399e1a2d462c51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83333c12df477f4a4535e1f1aa8cae0638970b6da01d217537f128c09f7fba8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238662c14a9492063729211ac7a56c9ec5fa2d438a38242a69a3e64d03636bb2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__161297b43d8d5a32ab796ed23ecc00735abe2af0027dc88c81b14e4fdbc3246c(
    value: typing.Optional[CloudwatchEventTargetRedshiftTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610a4e69be795d8c17b0795c459e3239bc208d2eb5892e6a45f629b6be33cb5c(
    *,
    maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c29bd3e94c840b6540d89c249a7237238c9b5e1795d37709dc8772b5e910e3a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e21d5695fdedce245a0f32ca3bec183c2ed28544b577a32026a0a185b8b826(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db398dcdae6864a00569609dc31cb6283574471c4a4b98b707698f6fe01db11(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9651947df7b9a1fcfa430323fcb86cbe62cba89665092218df94cc7feacd82f4(
    value: typing.Optional[CloudwatchEventTargetRetryPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1770731e1a000d994ab0c331e3526f9f0b34e1c5f0361633f37f5a8e41acde9d(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0900de0d6eb09e2eff4b7d5009ed76990bd65cbc97fa6155bd9b58193e76cc90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e785466817b853eff2d15c44cb16459f352f601c23628783ca75a982cd5dbc1b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8ed0149b9b38f9710661eb37abb8ea4320a5f73bda362343e9120fb1e87ce4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ae94e5b67aff5514cebb2f61044f3a7ee767ec18899e994ce96cfaf5ae142f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0689b06f51a7a5679d4130f6147eccab501a623a223f1cb68f8bbd402e9f99e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9828cda576f20880a3fc55f3a5645088bb5b6efd882a3a3e32f8116b5d487b7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwatchEventTargetRunCommandTargets]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152ec6188310e262baa5166883ff2dadcc598a81a6fbe7d9d019d65a40dcc060(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e967ceacd0478a9cd7d467c235397af5b816c0773bf39eee04b8fc5b3b26f47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658fc0ac0af8dd996f539147e64fca546b7a3a662c660e690e3deca685269e77(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905f3809917699ea17fd677db30d6840de6e879bf4a1bad5bad4ed508e4cb359(
    value: typing.Optional[typing.Union[CloudwatchEventTargetRunCommandTargets, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913bbb22d9567d596ffb04b714f86e64b0e5a92d1633140e5e9eb047e455ac7b(
    *,
    message_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e4bf63e7cc0a20ed5f1f01e80dffd6c7a9ad0cee307b90a8f8fa311114b4c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4f93692425971bef906e73bbdc1e28ed7f13badfb82fc261d1c3ed92a0aace(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8101be0ae955a65fad5c5f13bbedbe0dad5d07f3076e6dbf30b307f7ea3b0cae(
    value: typing.Optional[CloudwatchEventTargetSqsTarget],
) -> None:
    """Type checking stubs"""
    pass
