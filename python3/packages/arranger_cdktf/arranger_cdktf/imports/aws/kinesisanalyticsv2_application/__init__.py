'''
# `aws_kinesisanalyticsv2_application`

Refer to the Terraform Registory for docs: [`aws_kinesisanalyticsv2_application`](https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application).
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


class Kinesisanalyticsv2Application(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2Application",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application aws_kinesisanalyticsv2_application}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        runtime_environment: builtins.str,
        service_execution_role: builtins.str,
        application_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        force_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application aws_kinesisanalyticsv2_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.
        :param runtime_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#runtime_environment Kinesisanalyticsv2Application#runtime_environment}.
        :param service_execution_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#service_execution_role Kinesisanalyticsv2Application#service_execution_role}.
        :param application_configuration: application_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_configuration Kinesisanalyticsv2Application#application_configuration}
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#cloudwatch_logging_options Kinesisanalyticsv2Application#cloudwatch_logging_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#description Kinesisanalyticsv2Application#description}.
        :param force_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#force_stop Kinesisanalyticsv2Application#force_stop}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#id Kinesisanalyticsv2Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#start_application Kinesisanalyticsv2Application#start_application}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#tags Kinesisanalyticsv2Application#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#tags_all Kinesisanalyticsv2Application#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#timeouts Kinesisanalyticsv2Application#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0870f192d7cef34dc96461fd8ff0c67267418d1e0a33296a2f88c93ab7d52ee)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Kinesisanalyticsv2ApplicationConfig(
            name=name,
            runtime_environment=runtime_environment,
            service_execution_role=service_execution_role,
            application_configuration=application_configuration,
            cloudwatch_logging_options=cloudwatch_logging_options,
            description=description,
            force_stop=force_stop,
            id=id,
            start_application=start_application,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApplicationConfiguration")
    def put_application_configuration(
        self,
        *,
        application_code_configuration: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration", typing.Dict[builtins.str, typing.Any]],
        application_snapshot_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        environment_properties: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        flink_application_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        run_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        sql_application_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_code_configuration: application_code_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_code_configuration Kinesisanalyticsv2Application#application_code_configuration}
        :param application_snapshot_configuration: application_snapshot_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_snapshot_configuration Kinesisanalyticsv2Application#application_snapshot_configuration}
        :param environment_properties: environment_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#environment_properties Kinesisanalyticsv2Application#environment_properties}
        :param flink_application_configuration: flink_application_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#flink_application_configuration Kinesisanalyticsv2Application#flink_application_configuration}
        :param run_configuration: run_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#run_configuration Kinesisanalyticsv2Application#run_configuration}
        :param sql_application_configuration: sql_application_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_application_configuration Kinesisanalyticsv2Application#sql_application_configuration}
        :param vpc_configuration: vpc_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#vpc_configuration Kinesisanalyticsv2Application#vpc_configuration}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfiguration(
            application_code_configuration=application_code_configuration,
            application_snapshot_configuration=application_snapshot_configuration,
            environment_properties=environment_properties,
            flink_application_configuration=flink_application_configuration,
            run_configuration=run_configuration,
            sql_application_configuration=sql_application_configuration,
            vpc_configuration=vpc_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationConfiguration", [value]))

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(self, *, log_stream_arn: builtins.str) -> None:
        '''
        :param log_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#log_stream_arn Kinesisanalyticsv2Application#log_stream_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions(
            log_stream_arn=log_stream_arn
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#create Kinesisanalyticsv2Application#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#delete Kinesisanalyticsv2Application#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#update Kinesisanalyticsv2Application#update}.
        '''
        value = Kinesisanalyticsv2ApplicationTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplicationConfiguration")
    def reset_application_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationConfiguration", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetForceStop")
    def reset_force_stop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceStop", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStartApplication")
    def reset_start_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartApplication", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="applicationConfiguration")
    def application_configuration(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationOutputReference", jsii.get(self, "applicationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> "Kinesisanalyticsv2ApplicationCloudwatchLoggingOptionsOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationCloudwatchLoggingOptionsOutputReference", jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="createTimestamp")
    def create_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdateTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "Kinesisanalyticsv2ApplicationTimeoutsOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "versionId"))

    @builtins.property
    @jsii.member(jsii_name="applicationConfigurationInput")
    def application_configuration_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfiguration"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfiguration"], jsii.get(self, "applicationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions"], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="forceStopInput")
    def force_stop_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceStopInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEnvironmentInput")
    def runtime_environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRoleInput")
    def service_execution_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceExecutionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="startApplicationInput")
    def start_application_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "startApplicationInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c45eddcd34c06cb9e721d6b0a10a15f82257adba6b726db20aadeaccdfe8667)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="forceStop")
    def force_stop(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceStop"))

    @force_stop.setter
    def force_stop(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ddaa350f906d65c0c5cc8c42afa9825f554219d1fe74af63f4de0f2fcc506bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceStop", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__643e4bf26f1302814c1d6b166efb36c0260d49232375fd99790c0415e6052aa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f6fc32afd0a65d06749f3fe2e4e376ca77ff51a0ca913dfa25ba14dc11d65f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeEnvironment")
    def runtime_environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeEnvironment"))

    @runtime_environment.setter
    def runtime_environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b17dc1ac59f1d027019fd7ea25f5a120473745997f75a42f6802d217aad061b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRole")
    def service_execution_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRole"))

    @service_execution_role.setter
    def service_execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ac653204b6a9609442086beeaaf4b53908e85d319efb0cb51a4eeb4899cfcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRole", value)

    @builtins.property
    @jsii.member(jsii_name="startApplication")
    def start_application(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "startApplication"))

    @start_application.setter
    def start_application(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81cf65fd961c9ebb0f23db4841d709e53bac2e0e8a8ecc934a0bf0f47754ed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startApplication", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc874a51e319affbcc09dcb8778ceb7d169fff3dfc864f9337511296811183f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22829825060fad7a5fe36f07b933b6064b342234b2d26c8b9c2c9c69dac9b39e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "application_code_configuration": "applicationCodeConfiguration",
        "application_snapshot_configuration": "applicationSnapshotConfiguration",
        "environment_properties": "environmentProperties",
        "flink_application_configuration": "flinkApplicationConfiguration",
        "run_configuration": "runConfiguration",
        "sql_application_configuration": "sqlApplicationConfiguration",
        "vpc_configuration": "vpcConfiguration",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfiguration:
    def __init__(
        self,
        *,
        application_code_configuration: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration", typing.Dict[builtins.str, typing.Any]],
        application_snapshot_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        environment_properties: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        flink_application_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        run_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        sql_application_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_code_configuration: application_code_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_code_configuration Kinesisanalyticsv2Application#application_code_configuration}
        :param application_snapshot_configuration: application_snapshot_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_snapshot_configuration Kinesisanalyticsv2Application#application_snapshot_configuration}
        :param environment_properties: environment_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#environment_properties Kinesisanalyticsv2Application#environment_properties}
        :param flink_application_configuration: flink_application_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#flink_application_configuration Kinesisanalyticsv2Application#flink_application_configuration}
        :param run_configuration: run_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#run_configuration Kinesisanalyticsv2Application#run_configuration}
        :param sql_application_configuration: sql_application_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_application_configuration Kinesisanalyticsv2Application#sql_application_configuration}
        :param vpc_configuration: vpc_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#vpc_configuration Kinesisanalyticsv2Application#vpc_configuration}
        '''
        if isinstance(application_code_configuration, dict):
            application_code_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration(**application_code_configuration)
        if isinstance(application_snapshot_configuration, dict):
            application_snapshot_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration(**application_snapshot_configuration)
        if isinstance(environment_properties, dict):
            environment_properties = Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties(**environment_properties)
        if isinstance(flink_application_configuration, dict):
            flink_application_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration(**flink_application_configuration)
        if isinstance(run_configuration, dict):
            run_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration(**run_configuration)
        if isinstance(sql_application_configuration, dict):
            sql_application_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration(**sql_application_configuration)
        if isinstance(vpc_configuration, dict):
            vpc_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration(**vpc_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1244ae7dc7cafa8442553419fe54fe8e2c7f35c192358c1b4e80ce29cd5e10a)
            check_type(argname="argument application_code_configuration", value=application_code_configuration, expected_type=type_hints["application_code_configuration"])
            check_type(argname="argument application_snapshot_configuration", value=application_snapshot_configuration, expected_type=type_hints["application_snapshot_configuration"])
            check_type(argname="argument environment_properties", value=environment_properties, expected_type=type_hints["environment_properties"])
            check_type(argname="argument flink_application_configuration", value=flink_application_configuration, expected_type=type_hints["flink_application_configuration"])
            check_type(argname="argument run_configuration", value=run_configuration, expected_type=type_hints["run_configuration"])
            check_type(argname="argument sql_application_configuration", value=sql_application_configuration, expected_type=type_hints["sql_application_configuration"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_code_configuration": application_code_configuration,
        }
        if application_snapshot_configuration is not None:
            self._values["application_snapshot_configuration"] = application_snapshot_configuration
        if environment_properties is not None:
            self._values["environment_properties"] = environment_properties
        if flink_application_configuration is not None:
            self._values["flink_application_configuration"] = flink_application_configuration
        if run_configuration is not None:
            self._values["run_configuration"] = run_configuration
        if sql_application_configuration is not None:
            self._values["sql_application_configuration"] = sql_application_configuration
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

    @builtins.property
    def application_code_configuration(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration":
        '''application_code_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_code_configuration Kinesisanalyticsv2Application#application_code_configuration}
        '''
        result = self._values.get("application_code_configuration")
        assert result is not None, "Required property 'application_code_configuration' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration", result)

    @builtins.property
    def application_snapshot_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration"]:
        '''application_snapshot_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_snapshot_configuration Kinesisanalyticsv2Application#application_snapshot_configuration}
        '''
        result = self._values.get("application_snapshot_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration"], result)

    @builtins.property
    def environment_properties(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties"]:
        '''environment_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#environment_properties Kinesisanalyticsv2Application#environment_properties}
        '''
        result = self._values.get("environment_properties")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties"], result)

    @builtins.property
    def flink_application_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration"]:
        '''flink_application_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#flink_application_configuration Kinesisanalyticsv2Application#flink_application_configuration}
        '''
        result = self._values.get("flink_application_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration"], result)

    @builtins.property
    def run_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration"]:
        '''run_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#run_configuration Kinesisanalyticsv2Application#run_configuration}
        '''
        result = self._values.get("run_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration"], result)

    @builtins.property
    def sql_application_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration"]:
        '''sql_application_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_application_configuration Kinesisanalyticsv2Application#sql_application_configuration}
        '''
        result = self._values.get("sql_application_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration"], result)

    @builtins.property
    def vpc_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration"]:
        '''vpc_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#vpc_configuration Kinesisanalyticsv2Application#vpc_configuration}
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "code_content_type": "codeContentType",
        "code_content": "codeContent",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration:
    def __init__(
        self,
        *,
        code_content_type: builtins.str,
        code_content: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param code_content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#code_content_type Kinesisanalyticsv2Application#code_content_type}.
        :param code_content: code_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#code_content Kinesisanalyticsv2Application#code_content}
        '''
        if isinstance(code_content, dict):
            code_content = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent(**code_content)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856dbbe332623ea922d11629d9cdda202a470d126ebfab62b749eebec46fcd15)
            check_type(argname="argument code_content_type", value=code_content_type, expected_type=type_hints["code_content_type"])
            check_type(argname="argument code_content", value=code_content, expected_type=type_hints["code_content"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_content_type": code_content_type,
        }
        if code_content is not None:
            self._values["code_content"] = code_content

    @builtins.property
    def code_content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#code_content_type Kinesisanalyticsv2Application#code_content_type}.'''
        result = self._values.get("code_content_type")
        assert result is not None, "Required property 'code_content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_content(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent"]:
        '''code_content block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#code_content Kinesisanalyticsv2Application#code_content}
        '''
        result = self._values.get("code_content")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent",
    jsii_struct_bases=[],
    name_mapping={
        "s3_content_location": "s3ContentLocation",
        "text_content": "textContent",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent:
    def __init__(
        self,
        *,
        s3_content_location: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation", typing.Dict[builtins.str, typing.Any]]] = None,
        text_content: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_content_location: s3_content_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#s3_content_location Kinesisanalyticsv2Application#s3_content_location}
        :param text_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#text_content Kinesisanalyticsv2Application#text_content}.
        '''
        if isinstance(s3_content_location, dict):
            s3_content_location = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation(**s3_content_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d72dc6cab15c6ac2b666f1a93a8a8ca157741f9dfa67cac2b640cdebc8f281)
            check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
            check_type(argname="argument text_content", value=text_content, expected_type=type_hints["text_content"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_content_location is not None:
            self._values["s3_content_location"] = s3_content_location
        if text_content is not None:
            self._values["text_content"] = text_content

    @builtins.property
    def s3_content_location(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation"]:
        '''s3_content_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#s3_content_location Kinesisanalyticsv2Application#s3_content_location}
        '''
        result = self._values.get("s3_content_location")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation"], result)

    @builtins.property
    def text_content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#text_content Kinesisanalyticsv2Application#text_content}.'''
        result = self._values.get("text_content")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99665185775e7ec78eabe3c406f72a940666a85b9db840407e9a7c10a3009549)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3ContentLocation")
    def put_s3_content_location(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#bucket_arn Kinesisanalyticsv2Application#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#file_key Kinesisanalyticsv2Application#file_key}.
        :param object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#object_version Kinesisanalyticsv2Application#object_version}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation(
            bucket_arn=bucket_arn, file_key=file_key, object_version=object_version
        )

        return typing.cast(None, jsii.invoke(self, "putS3ContentLocation", [value]))

    @jsii.member(jsii_name="resetS3ContentLocation")
    def reset_s3_content_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3ContentLocation", []))

    @jsii.member(jsii_name="resetTextContent")
    def reset_text_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTextContent", []))

    @builtins.property
    @jsii.member(jsii_name="s3ContentLocation")
    def s3_content_location(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationOutputReference", jsii.get(self, "s3ContentLocation"))

    @builtins.property
    @jsii.member(jsii_name="s3ContentLocationInput")
    def s3_content_location_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation"], jsii.get(self, "s3ContentLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="textContentInput")
    def text_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textContentInput"))

    @builtins.property
    @jsii.member(jsii_name="textContent")
    def text_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textContent"))

    @text_content.setter
    def text_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b352266c694105cf51a0d2e6d8ea16200e5f8a4a62ade2ac3fc3edb2920dbad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textContent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4b964dea0243efc8701198b19ad25cabaf57eb0c0c02e4dcbe68e9ff6cb5ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "file_key": "fileKey",
        "object_version": "objectVersion",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#bucket_arn Kinesisanalyticsv2Application#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#file_key Kinesisanalyticsv2Application#file_key}.
        :param object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#object_version Kinesisanalyticsv2Application#object_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c15b86ffde5f13ac2e4138e9fbb33bcb88fbcd0a48e6525696e64da5b77f96f)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "file_key": file_key,
        }
        if object_version is not None:
            self._values["object_version"] = object_version

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#bucket_arn Kinesisanalyticsv2Application#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#file_key Kinesisanalyticsv2Application#file_key}.'''
        result = self._values.get("file_key")
        assert result is not None, "Required property 'file_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#object_version Kinesisanalyticsv2Application#object_version}.'''
        result = self._values.get("object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d89f999e0cee37ce2fe5d8b01e37b0730d916edc62807b624adcd4af4a9c568d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetObjectVersion")
    def reset_object_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectVersion", []))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="fileKeyInput")
    def file_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="objectVersionInput")
    def object_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d930528cae1d78837dc8bf522766987192a4b42d1de69ca3071a966904914c05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="fileKey")
    def file_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileKey"))

    @file_key.setter
    def file_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db6f8d4070794ab051a68395b923b5fcea7cfa524e1ae1bc6b8386cb6c3df35c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileKey", value)

    @builtins.property
    @jsii.member(jsii_name="objectVersion")
    def object_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectVersion"))

    @object_version.setter
    def object_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43dceab61353d7767863bd0516f290f003e2b450a91c36cd0f3401d533980b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df634c70a6d8cf476b42c54c606531060348b55a4f8ac86d47cd909c17c4b1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__747969dccec9bf3a0b70d09d5c2a5c1749b0713690b1c1f163cbefdcc627762c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeContent")
    def put_code_content(
        self,
        *,
        s3_content_location: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        text_content: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_content_location: s3_content_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#s3_content_location Kinesisanalyticsv2Application#s3_content_location}
        :param text_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#text_content Kinesisanalyticsv2Application#text_content}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent(
            s3_content_location=s3_content_location, text_content=text_content
        )

        return typing.cast(None, jsii.invoke(self, "putCodeContent", [value]))

    @jsii.member(jsii_name="resetCodeContent")
    def reset_code_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeContent", []))

    @builtins.property
    @jsii.member(jsii_name="codeContent")
    def code_content(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentOutputReference, jsii.get(self, "codeContent"))

    @builtins.property
    @jsii.member(jsii_name="codeContentInput")
    def code_content_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent], jsii.get(self, "codeContentInput"))

    @builtins.property
    @jsii.member(jsii_name="codeContentTypeInput")
    def code_content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeContentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="codeContentType")
    def code_content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codeContentType"))

    @code_content_type.setter
    def code_content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05512ababfb27f8cbe5c15e6ff2489f8efc3db4df68b976ad25b52d330bf43e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeContentType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd0fc8794af3b1f41dab141fb4e46e0c6cdd1d9d590c934a10e207d4f95ccb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration",
    jsii_struct_bases=[],
    name_mapping={"snapshots_enabled": "snapshotsEnabled"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration:
    def __init__(
        self,
        *,
        snapshots_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param snapshots_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#snapshots_enabled Kinesisanalyticsv2Application#snapshots_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915df0e2c75a07fc98e5c325b5a423c294a86d8119e6cc23d4fffab7747dd3d3)
            check_type(argname="argument snapshots_enabled", value=snapshots_enabled, expected_type=type_hints["snapshots_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "snapshots_enabled": snapshots_enabled,
        }

    @builtins.property
    def snapshots_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#snapshots_enabled Kinesisanalyticsv2Application#snapshots_enabled}.'''
        result = self._values.get("snapshots_enabled")
        assert result is not None, "Required property 'snapshots_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c374f0f7ebeb915ecb61b1163928a3b037ca792b41fdb835329fd1e6a802dd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="snapshotsEnabledInput")
    def snapshots_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "snapshotsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotsEnabled")
    def snapshots_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "snapshotsEnabled"))

    @snapshots_enabled.setter
    def snapshots_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a83b8c0a2c2e845f15d75952a8f5a22a26a94e994da4b1151c50a52ed7218d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50cd77439c3561fa2fda8ad5bc06fa1ff3794caa16471942f3e6664c3867b478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties",
    jsii_struct_bases=[],
    name_mapping={"property_group": "propertyGroup"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties:
    def __init__(
        self,
        *,
        property_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param property_group: property_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_group Kinesisanalyticsv2Application#property_group}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd333262a72dca0196a1a34094cfb67d8eb7ab10c242e4f131515b78736f860)
            check_type(argname="argument property_group", value=property_group, expected_type=type_hints["property_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "property_group": property_group,
        }

    @builtins.property
    def property_group(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup"]]:
        '''property_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_group Kinesisanalyticsv2Application#property_group}
        '''
        result = self._values.get("property_group")
        assert result is not None, "Required property 'property_group' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__703a367a8588136beac97633d449724a9e35a277b31eea17cee33976c0a95a5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPropertyGroup")
    def put_property_group(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdc37901fc8022f51a71e77ed754cd32019a863543e3df5a471724f2f0a89acc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPropertyGroup", [value]))

    @builtins.property
    @jsii.member(jsii_name="propertyGroup")
    def property_group(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupList":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupList", jsii.get(self, "propertyGroup"))

    @builtins.property
    @jsii.member(jsii_name="propertyGroupInput")
    def property_group_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup"]]], jsii.get(self, "propertyGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af1bc20f6d4a4c12daa6ce56584310b0ddce2af930d89447540e5083fd9346e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup",
    jsii_struct_bases=[],
    name_mapping={
        "property_group_id": "propertyGroupId",
        "property_map": "propertyMap",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup:
    def __init__(
        self,
        *,
        property_group_id: builtins.str,
        property_map: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param property_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_group_id Kinesisanalyticsv2Application#property_group_id}.
        :param property_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_map Kinesisanalyticsv2Application#property_map}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702fc9d67a06a9505f20d25c85d393c1846b114dab7265a886edf3046bf945db)
            check_type(argname="argument property_group_id", value=property_group_id, expected_type=type_hints["property_group_id"])
            check_type(argname="argument property_map", value=property_map, expected_type=type_hints["property_map"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "property_group_id": property_group_id,
            "property_map": property_map,
        }

    @builtins.property
    def property_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_group_id Kinesisanalyticsv2Application#property_group_id}.'''
        result = self._values.get("property_group_id")
        assert result is not None, "Required property 'property_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def property_map(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_map Kinesisanalyticsv2Application#property_map}.'''
        result = self._values.get("property_map")
        assert result is not None, "Required property 'property_map' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64e4f98675f510f13d7241a85c472c7ed301a54d01cb294e634ad7ce17609300)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__672060e1158aca1f8175149fa4f2e376021ae28e96a70f9e9012a4c7a9b4f028)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6ea35506896b0dd9332808df6c30ce60bbb092b78942fcef2bf94ae2d9aa238)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42a09fbd84252d94d38c61f0aef1a9f90b58af11492cbfee8b04dadb35250c1f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6f929cf681781857e899e394da88eaf85539e70140e9736a15e545fec4640da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb28d72aa0560bb1f1759c11f221789df0a7ac6c90d169661eeecf6c37b0670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b0f23bed97c879dc485fcd77aeef094250cde174ec90527c881e271ad29409a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="propertyGroupIdInput")
    def property_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyMapInput")
    def property_map_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertyMapInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyGroupId")
    def property_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propertyGroupId"))

    @property_group_id.setter
    def property_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb32dbffa589317101a00af72d66b63b539504a25ecf5f5485f6f6c053cd4d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="propertyMap")
    def property_map(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "propertyMap"))

    @property_map.setter
    def property_map(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceed5b8201cc1d6a778e521490f3fce59adf6e2adf41a38155a0174365bbb5cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyMap", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3c4aa97730b67da2d88c8e27f57543925eaf0bb6a5f3195f98729336eb5f74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "checkpoint_configuration": "checkpointConfiguration",
        "monitoring_configuration": "monitoringConfiguration",
        "parallelism_configuration": "parallelismConfiguration",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration:
    def __init__(
        self,
        *,
        checkpoint_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        parallelism_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param checkpoint_configuration: checkpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpoint_configuration Kinesisanalyticsv2Application#checkpoint_configuration}
        :param monitoring_configuration: monitoring_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#monitoring_configuration Kinesisanalyticsv2Application#monitoring_configuration}
        :param parallelism_configuration: parallelism_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism_configuration Kinesisanalyticsv2Application#parallelism_configuration}
        '''
        if isinstance(checkpoint_configuration, dict):
            checkpoint_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration(**checkpoint_configuration)
        if isinstance(monitoring_configuration, dict):
            monitoring_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration(**monitoring_configuration)
        if isinstance(parallelism_configuration, dict):
            parallelism_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration(**parallelism_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbc5d5ca6841984b6e7adc225495bb75da811adb7f8db81506e42ff85705d83e)
            check_type(argname="argument checkpoint_configuration", value=checkpoint_configuration, expected_type=type_hints["checkpoint_configuration"])
            check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            check_type(argname="argument parallelism_configuration", value=parallelism_configuration, expected_type=type_hints["parallelism_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if checkpoint_configuration is not None:
            self._values["checkpoint_configuration"] = checkpoint_configuration
        if monitoring_configuration is not None:
            self._values["monitoring_configuration"] = monitoring_configuration
        if parallelism_configuration is not None:
            self._values["parallelism_configuration"] = parallelism_configuration

    @builtins.property
    def checkpoint_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration"]:
        '''checkpoint_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpoint_configuration Kinesisanalyticsv2Application#checkpoint_configuration}
        '''
        result = self._values.get("checkpoint_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration"], result)

    @builtins.property
    def monitoring_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration"]:
        '''monitoring_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#monitoring_configuration Kinesisanalyticsv2Application#monitoring_configuration}
        '''
        result = self._values.get("monitoring_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration"], result)

    @builtins.property
    def parallelism_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration"]:
        '''parallelism_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism_configuration Kinesisanalyticsv2Application#parallelism_configuration}
        '''
        result = self._values.get("parallelism_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_type": "configurationType",
        "checkpointing_enabled": "checkpointingEnabled",
        "checkpoint_interval": "checkpointInterval",
        "min_pause_between_checkpoints": "minPauseBetweenCheckpoints",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration:
    def __init__(
        self,
        *,
        configuration_type: builtins.str,
        checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        checkpoint_interval: typing.Optional[jsii.Number] = None,
        min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.
        :param checkpointing_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpointing_enabled Kinesisanalyticsv2Application#checkpointing_enabled}.
        :param checkpoint_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpoint_interval Kinesisanalyticsv2Application#checkpoint_interval}.
        :param min_pause_between_checkpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#min_pause_between_checkpoints Kinesisanalyticsv2Application#min_pause_between_checkpoints}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8166e95c99614c7212dba6d08bd124a6d48706910901563c08f460a1217f7ac)
            check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
            check_type(argname="argument checkpointing_enabled", value=checkpointing_enabled, expected_type=type_hints["checkpointing_enabled"])
            check_type(argname="argument checkpoint_interval", value=checkpoint_interval, expected_type=type_hints["checkpoint_interval"])
            check_type(argname="argument min_pause_between_checkpoints", value=min_pause_between_checkpoints, expected_type=type_hints["min_pause_between_checkpoints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_type": configuration_type,
        }
        if checkpointing_enabled is not None:
            self._values["checkpointing_enabled"] = checkpointing_enabled
        if checkpoint_interval is not None:
            self._values["checkpoint_interval"] = checkpoint_interval
        if min_pause_between_checkpoints is not None:
            self._values["min_pause_between_checkpoints"] = min_pause_between_checkpoints

    @builtins.property
    def configuration_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.'''
        result = self._values.get("configuration_type")
        assert result is not None, "Required property 'configuration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def checkpointing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpointing_enabled Kinesisanalyticsv2Application#checkpointing_enabled}.'''
        result = self._values.get("checkpointing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def checkpoint_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpoint_interval Kinesisanalyticsv2Application#checkpoint_interval}.'''
        result = self._values.get("checkpoint_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_pause_between_checkpoints(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#min_pause_between_checkpoints Kinesisanalyticsv2Application#min_pause_between_checkpoints}.'''
        result = self._values.get("min_pause_between_checkpoints")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b037192718f0be908925302082edc74892044dedfabb2de8ddc7db81f587c63f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckpointingEnabled")
    def reset_checkpointing_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointingEnabled", []))

    @jsii.member(jsii_name="resetCheckpointInterval")
    def reset_checkpoint_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointInterval", []))

    @jsii.member(jsii_name="resetMinPauseBetweenCheckpoints")
    def reset_min_pause_between_checkpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinPauseBetweenCheckpoints", []))

    @builtins.property
    @jsii.member(jsii_name="checkpointingEnabledInput")
    def checkpointing_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "checkpointingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="checkpointIntervalInput")
    def checkpoint_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "checkpointIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationTypeInput")
    def configuration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minPauseBetweenCheckpointsInput")
    def min_pause_between_checkpoints_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minPauseBetweenCheckpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="checkpointingEnabled")
    def checkpointing_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "checkpointingEnabled"))

    @checkpointing_enabled.setter
    def checkpointing_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c5f79b0e7e018399cbca9f59ec4173f4377fa831732b1c3f3dca0cf4e3aa612)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="checkpointInterval")
    def checkpoint_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "checkpointInterval"))

    @checkpoint_interval.setter
    def checkpoint_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c165704181397ed5da5101a1f716d0ad2d76a48bf04340f4987de296598616)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointInterval", value)

    @builtins.property
    @jsii.member(jsii_name="configurationType")
    def configuration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationType"))

    @configuration_type.setter
    def configuration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__247a43965d90669c98a026ec69de021d682773b378d41694472a7476ee9b036e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationType", value)

    @builtins.property
    @jsii.member(jsii_name="minPauseBetweenCheckpoints")
    def min_pause_between_checkpoints(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minPauseBetweenCheckpoints"))

    @min_pause_between_checkpoints.setter
    def min_pause_between_checkpoints(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07313dd85af569c797e2919cc82e950a2097f30391955fd40e9f0a1157e456f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minPauseBetweenCheckpoints", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e271760dd1f828e54bc6c0939a768dc75dc3a7c23a77804b5b882d5dbbdd26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_type": "configurationType",
        "log_level": "logLevel",
        "metrics_level": "metricsLevel",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration:
    def __init__(
        self,
        *,
        configuration_type: builtins.str,
        log_level: typing.Optional[builtins.str] = None,
        metrics_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#log_level Kinesisanalyticsv2Application#log_level}.
        :param metrics_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#metrics_level Kinesisanalyticsv2Application#metrics_level}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b20132283c684756f5a66533885dc185b9d68c3b5f4b30070eec145667c639)
            check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument metrics_level", value=metrics_level, expected_type=type_hints["metrics_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_type": configuration_type,
        }
        if log_level is not None:
            self._values["log_level"] = log_level
        if metrics_level is not None:
            self._values["metrics_level"] = metrics_level

    @builtins.property
    def configuration_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.'''
        result = self._values.get("configuration_type")
        assert result is not None, "Required property 'configuration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#log_level Kinesisanalyticsv2Application#log_level}.'''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#metrics_level Kinesisanalyticsv2Application#metrics_level}.'''
        result = self._values.get("metrics_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed9dc31e0fd04b9f95661b470a1964b0189ddd303b7b2c9665fc0b06cc75849f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLogLevel")
    def reset_log_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevel", []))

    @jsii.member(jsii_name="resetMetricsLevel")
    def reset_metrics_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsLevel", []))

    @builtins.property
    @jsii.member(jsii_name="configurationTypeInput")
    def configuration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelInput")
    def log_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsLevelInput")
    def metrics_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricsLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationType")
    def configuration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationType"))

    @configuration_type.setter
    def configuration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a05e5aae223361eca1bb2aeb282c80695173cef4dacbf1ee8f758c5d982f2dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationType", value)

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19add5df3d4d8bf36c2e656602d7062bda9bf2a58f0bd86fcf976140669273d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="metricsLevel")
    def metrics_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricsLevel"))

    @metrics_level.setter
    def metrics_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665f3ceeedb7d954f0113d26fa888c11e4fa197ef99790c08210d34a8262b3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eecee5ce4715178b1493aaa7278e5c6ce7f866f01fd84cdabdbbb8cfc9de89e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2023925952fe73f537f44f40be44f7372f06d10e65952829cf85b122a27f86ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCheckpointConfiguration")
    def put_checkpoint_configuration(
        self,
        *,
        configuration_type: builtins.str,
        checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        checkpoint_interval: typing.Optional[jsii.Number] = None,
        min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.
        :param checkpointing_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpointing_enabled Kinesisanalyticsv2Application#checkpointing_enabled}.
        :param checkpoint_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpoint_interval Kinesisanalyticsv2Application#checkpoint_interval}.
        :param min_pause_between_checkpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#min_pause_between_checkpoints Kinesisanalyticsv2Application#min_pause_between_checkpoints}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration(
            configuration_type=configuration_type,
            checkpointing_enabled=checkpointing_enabled,
            checkpoint_interval=checkpoint_interval,
            min_pause_between_checkpoints=min_pause_between_checkpoints,
        )

        return typing.cast(None, jsii.invoke(self, "putCheckpointConfiguration", [value]))

    @jsii.member(jsii_name="putMonitoringConfiguration")
    def put_monitoring_configuration(
        self,
        *,
        configuration_type: builtins.str,
        log_level: typing.Optional[builtins.str] = None,
        metrics_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.
        :param log_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#log_level Kinesisanalyticsv2Application#log_level}.
        :param metrics_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#metrics_level Kinesisanalyticsv2Application#metrics_level}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration(
            configuration_type=configuration_type,
            log_level=log_level,
            metrics_level=metrics_level,
        )

        return typing.cast(None, jsii.invoke(self, "putMonitoringConfiguration", [value]))

    @jsii.member(jsii_name="putParallelismConfiguration")
    def put_parallelism_configuration(
        self,
        *,
        configuration_type: builtins.str,
        auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parallelism: typing.Optional[jsii.Number] = None,
        parallelism_per_kpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.
        :param auto_scaling_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#auto_scaling_enabled Kinesisanalyticsv2Application#auto_scaling_enabled}.
        :param parallelism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism Kinesisanalyticsv2Application#parallelism}.
        :param parallelism_per_kpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism_per_kpu Kinesisanalyticsv2Application#parallelism_per_kpu}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration(
            configuration_type=configuration_type,
            auto_scaling_enabled=auto_scaling_enabled,
            parallelism=parallelism,
            parallelism_per_kpu=parallelism_per_kpu,
        )

        return typing.cast(None, jsii.invoke(self, "putParallelismConfiguration", [value]))

    @jsii.member(jsii_name="resetCheckpointConfiguration")
    def reset_checkpoint_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointConfiguration", []))

    @jsii.member(jsii_name="resetMonitoringConfiguration")
    def reset_monitoring_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringConfiguration", []))

    @jsii.member(jsii_name="resetParallelismConfiguration")
    def reset_parallelism_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelismConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="checkpointConfiguration")
    def checkpoint_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationOutputReference, jsii.get(self, "checkpointConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationOutputReference, jsii.get(self, "monitoringConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="parallelismConfiguration")
    def parallelism_configuration(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationOutputReference", jsii.get(self, "parallelismConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="checkpointConfigurationInput")
    def checkpoint_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration], jsii.get(self, "checkpointConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringConfigurationInput")
    def monitoring_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration], jsii.get(self, "monitoringConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismConfigurationInput")
    def parallelism_configuration_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration"], jsii.get(self, "parallelismConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c3d7b66352e9e5199549e07b26c22ea221d9049cd02f0dd437353895355aa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_type": "configurationType",
        "auto_scaling_enabled": "autoScalingEnabled",
        "parallelism": "parallelism",
        "parallelism_per_kpu": "parallelismPerKpu",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration:
    def __init__(
        self,
        *,
        configuration_type: builtins.str,
        auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parallelism: typing.Optional[jsii.Number] = None,
        parallelism_per_kpu: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.
        :param auto_scaling_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#auto_scaling_enabled Kinesisanalyticsv2Application#auto_scaling_enabled}.
        :param parallelism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism Kinesisanalyticsv2Application#parallelism}.
        :param parallelism_per_kpu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism_per_kpu Kinesisanalyticsv2Application#parallelism_per_kpu}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a79e76e324a9efba2e9f3f41f6a15f6c7a0e3c0e90dbb2b99f651a99b9ab35d)
            check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
            check_type(argname="argument auto_scaling_enabled", value=auto_scaling_enabled, expected_type=type_hints["auto_scaling_enabled"])
            check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
            check_type(argname="argument parallelism_per_kpu", value=parallelism_per_kpu, expected_type=type_hints["parallelism_per_kpu"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_type": configuration_type,
        }
        if auto_scaling_enabled is not None:
            self._values["auto_scaling_enabled"] = auto_scaling_enabled
        if parallelism is not None:
            self._values["parallelism"] = parallelism
        if parallelism_per_kpu is not None:
            self._values["parallelism_per_kpu"] = parallelism_per_kpu

    @builtins.property
    def configuration_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#configuration_type Kinesisanalyticsv2Application#configuration_type}.'''
        result = self._values.get("configuration_type")
        assert result is not None, "Required property 'configuration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scaling_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#auto_scaling_enabled Kinesisanalyticsv2Application#auto_scaling_enabled}.'''
        result = self._values.get("auto_scaling_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def parallelism(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism Kinesisanalyticsv2Application#parallelism}.'''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parallelism_per_kpu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism_per_kpu Kinesisanalyticsv2Application#parallelism_per_kpu}.'''
        result = self._values.get("parallelism_per_kpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0da26c2884c01d34feccf66afb99c87a37fa65470468101686a552933e2f7b7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoScalingEnabled")
    def reset_auto_scaling_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScalingEnabled", []))

    @jsii.member(jsii_name="resetParallelism")
    def reset_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelism", []))

    @jsii.member(jsii_name="resetParallelismPerKpu")
    def reset_parallelism_per_kpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelismPerKpu", []))

    @builtins.property
    @jsii.member(jsii_name="autoScalingEnabledInput")
    def auto_scaling_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoScalingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationTypeInput")
    def configuration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismInput")
    def parallelism_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismPerKpuInput")
    def parallelism_per_kpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parallelismPerKpuInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingEnabled")
    def auto_scaling_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoScalingEnabled"))

    @auto_scaling_enabled.setter
    def auto_scaling_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3905231735dad3b72816908260070eafbee381cb8af6c990089470aac724668e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="configurationType")
    def configuration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationType"))

    @configuration_type.setter
    def configuration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__589e2ddcea7376a84f46c98ccefd34d6f1bec5230b390ff43f260b23e578f64a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationType", value)

    @builtins.property
    @jsii.member(jsii_name="parallelism")
    def parallelism(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parallelism"))

    @parallelism.setter
    def parallelism(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42cf774bcd7f89fe65f24244380991bc228aa6a4da6f831a9a66e60698a428fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parallelism", value)

    @builtins.property
    @jsii.member(jsii_name="parallelismPerKpu")
    def parallelism_per_kpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parallelismPerKpu"))

    @parallelism_per_kpu.setter
    def parallelism_per_kpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0393a44b25c1bf53c26ea075f55a4c5d417852db1434bcd5d67cb9f8fbf7b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parallelismPerKpu", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8d3da2b25521df6af33267cf68e4a2ba0d6a4062ce8978f68ba0ccd1a12d4f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2bfeacddbc525fe998fd486ee0da4b974bbc851fed527c0a3ad34d562f648d62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationCodeConfiguration")
    def put_application_code_configuration(
        self,
        *,
        code_content_type: builtins.str,
        code_content: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param code_content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#code_content_type Kinesisanalyticsv2Application#code_content_type}.
        :param code_content: code_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#code_content Kinesisanalyticsv2Application#code_content}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration(
            code_content_type=code_content_type, code_content=code_content
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationCodeConfiguration", [value]))

    @jsii.member(jsii_name="putApplicationSnapshotConfiguration")
    def put_application_snapshot_configuration(
        self,
        *,
        snapshots_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param snapshots_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#snapshots_enabled Kinesisanalyticsv2Application#snapshots_enabled}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration(
            snapshots_enabled=snapshots_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationSnapshotConfiguration", [value]))

    @jsii.member(jsii_name="putEnvironmentProperties")
    def put_environment_properties(
        self,
        *,
        property_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param property_group: property_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#property_group Kinesisanalyticsv2Application#property_group}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties(
            property_group=property_group
        )

        return typing.cast(None, jsii.invoke(self, "putEnvironmentProperties", [value]))

    @jsii.member(jsii_name="putFlinkApplicationConfiguration")
    def put_flink_application_configuration(
        self,
        *,
        checkpoint_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        monitoring_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        parallelism_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param checkpoint_configuration: checkpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#checkpoint_configuration Kinesisanalyticsv2Application#checkpoint_configuration}
        :param monitoring_configuration: monitoring_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#monitoring_configuration Kinesisanalyticsv2Application#monitoring_configuration}
        :param parallelism_configuration: parallelism_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#parallelism_configuration Kinesisanalyticsv2Application#parallelism_configuration}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration(
            checkpoint_configuration=checkpoint_configuration,
            monitoring_configuration=monitoring_configuration,
            parallelism_configuration=parallelism_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putFlinkApplicationConfiguration", [value]))

    @jsii.member(jsii_name="putRunConfiguration")
    def put_run_configuration(
        self,
        *,
        application_restore_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        flink_run_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_restore_configuration: application_restore_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_restore_configuration Kinesisanalyticsv2Application#application_restore_configuration}
        :param flink_run_configuration: flink_run_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#flink_run_configuration Kinesisanalyticsv2Application#flink_run_configuration}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration(
            application_restore_configuration=application_restore_configuration,
            flink_run_configuration=flink_run_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putRunConfiguration", [value]))

    @jsii.member(jsii_name="putSqlApplicationConfiguration")
    def put_sql_application_configuration(
        self,
        *,
        input: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput", typing.Dict[builtins.str, typing.Any]]] = None,
        output: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput", typing.Dict[builtins.str, typing.Any]]]]] = None,
        reference_data_source: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input Kinesisanalyticsv2Application#input}
        :param output: output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#output Kinesisanalyticsv2Application#output}
        :param reference_data_source: reference_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#reference_data_source Kinesisanalyticsv2Application#reference_data_source}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration(
            input=input, output=output, reference_data_source=reference_data_source
        )

        return typing.cast(None, jsii.invoke(self, "putSqlApplicationConfiguration", [value]))

    @jsii.member(jsii_name="putVpcConfiguration")
    def put_vpc_configuration(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#security_group_ids Kinesisanalyticsv2Application#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#subnet_ids Kinesisanalyticsv2Application#subnet_ids}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfiguration", [value]))

    @jsii.member(jsii_name="resetApplicationSnapshotConfiguration")
    def reset_application_snapshot_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationSnapshotConfiguration", []))

    @jsii.member(jsii_name="resetEnvironmentProperties")
    def reset_environment_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentProperties", []))

    @jsii.member(jsii_name="resetFlinkApplicationConfiguration")
    def reset_flink_application_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlinkApplicationConfiguration", []))

    @jsii.member(jsii_name="resetRunConfiguration")
    def reset_run_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunConfiguration", []))

    @jsii.member(jsii_name="resetSqlApplicationConfiguration")
    def reset_sql_application_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlApplicationConfiguration", []))

    @jsii.member(jsii_name="resetVpcConfiguration")
    def reset_vpc_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="applicationCodeConfiguration")
    def application_code_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationOutputReference, jsii.get(self, "applicationCodeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="applicationSnapshotConfiguration")
    def application_snapshot_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfigurationOutputReference, jsii.get(self, "applicationSnapshotConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="environmentProperties")
    def environment_properties(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesOutputReference, jsii.get(self, "environmentProperties"))

    @builtins.property
    @jsii.member(jsii_name="flinkApplicationConfiguration")
    def flink_application_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationOutputReference, jsii.get(self, "flinkApplicationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="runConfiguration")
    def run_configuration(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationOutputReference", jsii.get(self, "runConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="sqlApplicationConfiguration")
    def sql_application_configuration(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputReference", jsii.get(self, "sqlApplicationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfigurationOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfigurationOutputReference", jsii.get(self, "vpcConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="applicationCodeConfigurationInput")
    def application_code_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration], jsii.get(self, "applicationCodeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationSnapshotConfigurationInput")
    def application_snapshot_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration], jsii.get(self, "applicationSnapshotConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentPropertiesInput")
    def environment_properties_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties], jsii.get(self, "environmentPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="flinkApplicationConfigurationInput")
    def flink_application_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration], jsii.get(self, "flinkApplicationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="runConfigurationInput")
    def run_configuration_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration"], jsii.get(self, "runConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlApplicationConfigurationInput")
    def sql_application_configuration_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration"], jsii.get(self, "sqlApplicationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigurationInput")
    def vpc_configuration_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration"], jsii.get(self, "vpcConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5fed13a1e4bb9f375c129069e6f5473c17c748f7798dca65b2a42c5dad8bb38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "application_restore_configuration": "applicationRestoreConfiguration",
        "flink_run_configuration": "flinkRunConfiguration",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration:
    def __init__(
        self,
        *,
        application_restore_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        flink_run_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_restore_configuration: application_restore_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_restore_configuration Kinesisanalyticsv2Application#application_restore_configuration}
        :param flink_run_configuration: flink_run_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#flink_run_configuration Kinesisanalyticsv2Application#flink_run_configuration}
        '''
        if isinstance(application_restore_configuration, dict):
            application_restore_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration(**application_restore_configuration)
        if isinstance(flink_run_configuration, dict):
            flink_run_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration(**flink_run_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__719852cc4d7e5048b5a908827847f01a08639b592424cbbd91b08a8f589294b0)
            check_type(argname="argument application_restore_configuration", value=application_restore_configuration, expected_type=type_hints["application_restore_configuration"])
            check_type(argname="argument flink_run_configuration", value=flink_run_configuration, expected_type=type_hints["flink_run_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_restore_configuration is not None:
            self._values["application_restore_configuration"] = application_restore_configuration
        if flink_run_configuration is not None:
            self._values["flink_run_configuration"] = flink_run_configuration

    @builtins.property
    def application_restore_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration"]:
        '''application_restore_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_restore_configuration Kinesisanalyticsv2Application#application_restore_configuration}
        '''
        result = self._values.get("application_restore_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration"], result)

    @builtins.property
    def flink_run_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration"]:
        '''flink_run_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#flink_run_configuration Kinesisanalyticsv2Application#flink_run_configuration}
        '''
        result = self._values.get("flink_run_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "application_restore_type": "applicationRestoreType",
        "snapshot_name": "snapshotName",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration:
    def __init__(
        self,
        *,
        application_restore_type: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_restore_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_restore_type Kinesisanalyticsv2Application#application_restore_type}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#snapshot_name Kinesisanalyticsv2Application#snapshot_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5349584eb117c417baf3676c660a66ea9a99cbad3bd99dfddd4b8f94067e6b00)
            check_type(argname="argument application_restore_type", value=application_restore_type, expected_type=type_hints["application_restore_type"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_restore_type is not None:
            self._values["application_restore_type"] = application_restore_type
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name

    @builtins.property
    def application_restore_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_restore_type Kinesisanalyticsv2Application#application_restore_type}.'''
        result = self._values.get("application_restore_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#snapshot_name Kinesisanalyticsv2Application#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45d751201480ccf95acf1aaf2cb353d6cd4acd10d463eb9480a3d477ecb271ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApplicationRestoreType")
    def reset_application_restore_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationRestoreType", []))

    @jsii.member(jsii_name="resetSnapshotName")
    def reset_snapshot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotName", []))

    @builtins.property
    @jsii.member(jsii_name="applicationRestoreTypeInput")
    def application_restore_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationRestoreTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationRestoreType")
    def application_restore_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationRestoreType"))

    @application_restore_type.setter
    def application_restore_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b72b665a73e5a1bdecbf0fd8d565c18549337e5d7337e376632e9c9315bce4af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationRestoreType", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e12e14fbd6e9e377d16ca2eee70aeadb7d120ecc6b14a060596741576acb48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6431beba99b89d4f1b8bade38b75397e8aec0844d6c0f299beaff279556ff058)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration",
    jsii_struct_bases=[],
    name_mapping={"allow_non_restored_state": "allowNonRestoredState"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration:
    def __init__(
        self,
        *,
        allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_non_restored_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#allow_non_restored_state Kinesisanalyticsv2Application#allow_non_restored_state}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47836cca49a2d0d472d6dc5948c16a240e17fe3058d9f26eb50860b950744af5)
            check_type(argname="argument allow_non_restored_state", value=allow_non_restored_state, expected_type=type_hints["allow_non_restored_state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_non_restored_state is not None:
            self._values["allow_non_restored_state"] = allow_non_restored_state

    @builtins.property
    def allow_non_restored_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#allow_non_restored_state Kinesisanalyticsv2Application#allow_non_restored_state}.'''
        result = self._values.get("allow_non_restored_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a1ee689559590cff1a7076d52a1fdbf8e7f590cf8ce646b16c6a9e7a5074e43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowNonRestoredState")
    def reset_allow_non_restored_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowNonRestoredState", []))

    @builtins.property
    @jsii.member(jsii_name="allowNonRestoredStateInput")
    def allow_non_restored_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowNonRestoredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowNonRestoredState")
    def allow_non_restored_state(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowNonRestoredState"))

    @allow_non_restored_state.setter
    def allow_non_restored_state(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17bd967440038fd656299b401db52fd72c740d804c47ea48b5857d4861bca709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowNonRestoredState", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22c91f7d6834ebe1fec46b79262061d18de3a6081db213a6eb9f1fe082c8998a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef0c232e512d892172479dae5370838ca3efa4b2fd6a9e2db936e829575af700)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationRestoreConfiguration")
    def put_application_restore_configuration(
        self,
        *,
        application_restore_type: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_restore_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_restore_type Kinesisanalyticsv2Application#application_restore_type}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#snapshot_name Kinesisanalyticsv2Application#snapshot_name}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration(
            application_restore_type=application_restore_type,
            snapshot_name=snapshot_name,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationRestoreConfiguration", [value]))

    @jsii.member(jsii_name="putFlinkRunConfiguration")
    def put_flink_run_configuration(
        self,
        *,
        allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_non_restored_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#allow_non_restored_state Kinesisanalyticsv2Application#allow_non_restored_state}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration(
            allow_non_restored_state=allow_non_restored_state
        )

        return typing.cast(None, jsii.invoke(self, "putFlinkRunConfiguration", [value]))

    @jsii.member(jsii_name="resetApplicationRestoreConfiguration")
    def reset_application_restore_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationRestoreConfiguration", []))

    @jsii.member(jsii_name="resetFlinkRunConfiguration")
    def reset_flink_run_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlinkRunConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="applicationRestoreConfiguration")
    def application_restore_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationOutputReference, jsii.get(self, "applicationRestoreConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="flinkRunConfiguration")
    def flink_run_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationOutputReference, jsii.get(self, "flinkRunConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="applicationRestoreConfigurationInput")
    def application_restore_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration], jsii.get(self, "applicationRestoreConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="flinkRunConfigurationInput")
    def flink_run_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration], jsii.get(self, "flinkRunConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee3af73a7df9b6f2305740de8c50801871ac0b1b8d7a4f5f74c3358e06bf1eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "input": "input",
        "output": "output",
        "reference_data_source": "referenceDataSource",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration:
    def __init__(
        self,
        *,
        input: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput", typing.Dict[builtins.str, typing.Any]]] = None,
        output: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput", typing.Dict[builtins.str, typing.Any]]]]] = None,
        reference_data_source: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input Kinesisanalyticsv2Application#input}
        :param output: output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#output Kinesisanalyticsv2Application#output}
        :param reference_data_source: reference_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#reference_data_source Kinesisanalyticsv2Application#reference_data_source}
        '''
        if isinstance(input, dict):
            input = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput(**input)
        if isinstance(reference_data_source, dict):
            reference_data_source = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource(**reference_data_source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cecd57323f898bf8925ff40596630ed85378bd9bbc5b86c5125eb0c3a09f18)
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument reference_data_source", value=reference_data_source, expected_type=type_hints["reference_data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if input is not None:
            self._values["input"] = input
        if output is not None:
            self._values["output"] = output
        if reference_data_source is not None:
            self._values["reference_data_source"] = reference_data_source

    @builtins.property
    def input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput"]:
        '''input block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input Kinesisanalyticsv2Application#input}
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput"], result)

    @builtins.property
    def output(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput"]]]:
        '''output block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#output Kinesisanalyticsv2Application#output}
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput"]]], result)

    @builtins.property
    def reference_data_source(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource"]:
        '''reference_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#reference_data_source Kinesisanalyticsv2Application#reference_data_source}
        '''
        result = self._values.get("reference_data_source")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput",
    jsii_struct_bases=[],
    name_mapping={
        "input_schema": "inputSchema",
        "name_prefix": "namePrefix",
        "input_parallelism": "inputParallelism",
        "input_processing_configuration": "inputProcessingConfiguration",
        "input_starting_position_configuration": "inputStartingPositionConfiguration",
        "kinesis_firehose_input": "kinesisFirehoseInput",
        "kinesis_streams_input": "kinesisStreamsInput",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput:
    def __init__(
        self,
        *,
        input_schema: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema", typing.Dict[builtins.str, typing.Any]],
        name_prefix: builtins.str,
        input_parallelism: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism", typing.Dict[builtins.str, typing.Any]]] = None,
        input_processing_configuration: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        input_starting_position_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        kinesis_firehose_input: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_streams_input: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param input_schema: input_schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_schema Kinesisanalyticsv2Application#input_schema}
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name_prefix Kinesisanalyticsv2Application#name_prefix}.
        :param input_parallelism: input_parallelism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_parallelism Kinesisanalyticsv2Application#input_parallelism}
        :param input_processing_configuration: input_processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_processing_configuration Kinesisanalyticsv2Application#input_processing_configuration}
        :param input_starting_position_configuration: input_starting_position_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_starting_position_configuration Kinesisanalyticsv2Application#input_starting_position_configuration}
        :param kinesis_firehose_input: kinesis_firehose_input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_firehose_input Kinesisanalyticsv2Application#kinesis_firehose_input}
        :param kinesis_streams_input: kinesis_streams_input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_streams_input Kinesisanalyticsv2Application#kinesis_streams_input}
        '''
        if isinstance(input_schema, dict):
            input_schema = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema(**input_schema)
        if isinstance(input_parallelism, dict):
            input_parallelism = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism(**input_parallelism)
        if isinstance(input_processing_configuration, dict):
            input_processing_configuration = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration(**input_processing_configuration)
        if isinstance(kinesis_firehose_input, dict):
            kinesis_firehose_input = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput(**kinesis_firehose_input)
        if isinstance(kinesis_streams_input, dict):
            kinesis_streams_input = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput(**kinesis_streams_input)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f80f578df5c9c2be7ebdf29672a020f1bc69d9c3db28c61a2f46cdbfa218f1e)
            check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument input_parallelism", value=input_parallelism, expected_type=type_hints["input_parallelism"])
            check_type(argname="argument input_processing_configuration", value=input_processing_configuration, expected_type=type_hints["input_processing_configuration"])
            check_type(argname="argument input_starting_position_configuration", value=input_starting_position_configuration, expected_type=type_hints["input_starting_position_configuration"])
            check_type(argname="argument kinesis_firehose_input", value=kinesis_firehose_input, expected_type=type_hints["kinesis_firehose_input"])
            check_type(argname="argument kinesis_streams_input", value=kinesis_streams_input, expected_type=type_hints["kinesis_streams_input"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_schema": input_schema,
            "name_prefix": name_prefix,
        }
        if input_parallelism is not None:
            self._values["input_parallelism"] = input_parallelism
        if input_processing_configuration is not None:
            self._values["input_processing_configuration"] = input_processing_configuration
        if input_starting_position_configuration is not None:
            self._values["input_starting_position_configuration"] = input_starting_position_configuration
        if kinesis_firehose_input is not None:
            self._values["kinesis_firehose_input"] = kinesis_firehose_input
        if kinesis_streams_input is not None:
            self._values["kinesis_streams_input"] = kinesis_streams_input

    @builtins.property
    def input_schema(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema":
        '''input_schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_schema Kinesisanalyticsv2Application#input_schema}
        '''
        result = self._values.get("input_schema")
        assert result is not None, "Required property 'input_schema' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema", result)

    @builtins.property
    def name_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name_prefix Kinesisanalyticsv2Application#name_prefix}.'''
        result = self._values.get("name_prefix")
        assert result is not None, "Required property 'name_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_parallelism(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism"]:
        '''input_parallelism block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_parallelism Kinesisanalyticsv2Application#input_parallelism}
        '''
        result = self._values.get("input_parallelism")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism"], result)

    @builtins.property
    def input_processing_configuration(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration"]:
        '''input_processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_processing_configuration Kinesisanalyticsv2Application#input_processing_configuration}
        '''
        result = self._values.get("input_processing_configuration")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration"], result)

    @builtins.property
    def input_starting_position_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration"]]]:
        '''input_starting_position_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_starting_position_configuration Kinesisanalyticsv2Application#input_starting_position_configuration}
        '''
        result = self._values.get("input_starting_position_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration"]]], result)

    @builtins.property
    def kinesis_firehose_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput"]:
        '''kinesis_firehose_input block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_firehose_input Kinesisanalyticsv2Application#kinesis_firehose_input}
        '''
        result = self._values.get("kinesis_firehose_input")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput"], result)

    @builtins.property
    def kinesis_streams_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput"]:
        '''kinesis_streams_input block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_streams_input Kinesisanalyticsv2Application#kinesis_streams_input}
        '''
        result = self._values.get("kinesis_streams_input")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism",
    jsii_struct_bases=[],
    name_mapping={"count": "count"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism:
    def __init__(self, *, count: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#count Kinesisanalyticsv2Application#count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82c9d36ea3768684254efbe12580ce0e62e0f7f374acfbea3bd5d3be281a429b)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#count Kinesisanalyticsv2Application#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a7acab5ff47f48da384e3df2e99e593dbf759109eacd97f1398993c583a5898)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b1872426891bf23838564eb779a36e0df02aa4906b6a33a91ff4a5edacd610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c36de2f36079a1ed847d9e8776aee4a742f7ea2e6e18861b45ff2c680f266122)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"input_lambda_processor": "inputLambdaProcessor"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration:
    def __init__(
        self,
        *,
        input_lambda_processor: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param input_lambda_processor: input_lambda_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_lambda_processor Kinesisanalyticsv2Application#input_lambda_processor}
        '''
        if isinstance(input_lambda_processor, dict):
            input_lambda_processor = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor(**input_lambda_processor)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa0c3b80958f98e51e24898dca49266d2347e4fd8d1d1ecd5f981c8d94cbaea)
            check_type(argname="argument input_lambda_processor", value=input_lambda_processor, expected_type=type_hints["input_lambda_processor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_lambda_processor": input_lambda_processor,
        }

    @builtins.property
    def input_lambda_processor(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor":
        '''input_lambda_processor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_lambda_processor Kinesisanalyticsv2Application#input_lambda_processor}
        '''
        result = self._values.get("input_lambda_processor")
        assert result is not None, "Required property 'input_lambda_processor' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__197cfdfbb99c8db2f77d185c92b2e2e3143c3b29d12b877fdc2396eaaa5364c7)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__097fe161792da064990bf7ae9890cc2a3391684458fada7b542a38709d613fa9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83dac9e0059c954e895fbfcf04a1f17bfb336fc9e922df0c56076571d39138e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f67136e023d888ea30b4d3e4d25372a03a2c32bd911031853fc5403bd0dcf521)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3adba17746a8b3719c4b6002c40e32f5ca515da69aa5cefade00f7fd2e67ea1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInputLambdaProcessor")
    def put_input_lambda_processor(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor(
            resource_arn=resource_arn
        )

        return typing.cast(None, jsii.invoke(self, "putInputLambdaProcessor", [value]))

    @builtins.property
    @jsii.member(jsii_name="inputLambdaProcessor")
    def input_lambda_processor(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorOutputReference, jsii.get(self, "inputLambdaProcessor"))

    @builtins.property
    @jsii.member(jsii_name="inputLambdaProcessorInput")
    def input_lambda_processor_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor], jsii.get(self, "inputLambdaProcessorInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f95b37339b92d3b822a6fea5b634f0b726141638a30aa1abfa85056a3ffeeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema",
    jsii_struct_bases=[],
    name_mapping={
        "record_column": "recordColumn",
        "record_format": "recordFormat",
        "record_encoding": "recordEncoding",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema:
    def __init__(
        self,
        *,
        record_column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_column: record_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column Kinesisanalyticsv2Application#record_column}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format Kinesisanalyticsv2Application#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_encoding Kinesisanalyticsv2Application#record_encoding}.
        '''
        if isinstance(record_format, dict):
            record_format = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat(**record_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c982d2bb6ef3892d100a7e0496c66ac279e32477433f53acecbeb8c0d3603eb0)
            check_type(argname="argument record_column", value=record_column, expected_type=type_hints["record_column"])
            check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
            check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_column": record_column,
            "record_format": record_format,
        }
        if record_encoding is not None:
            self._values["record_encoding"] = record_encoding

    @builtins.property
    def record_column(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn"]]:
        '''record_column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column Kinesisanalyticsv2Application#record_column}
        '''
        result = self._values.get("record_column")
        assert result is not None, "Required property 'record_column' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn"]], result)

    @builtins.property
    def record_format(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat":
        '''record_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format Kinesisanalyticsv2Application#record_format}
        '''
        result = self._values.get("record_format")
        assert result is not None, "Required property 'record_format' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat", result)

    @builtins.property
    def record_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_encoding Kinesisanalyticsv2Application#record_encoding}.'''
        result = self._values.get("record_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdcb2bc5181c431330f3e3b0fd7b7aa0314a57af5c2bbdca28df214cfeacdd10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRecordColumn")
    def put_record_column(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e754b823676f2a517638ea385334f835e61c4e38d1fe75763f4853877fd607c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordColumn", [value]))

    @jsii.member(jsii_name="putRecordFormat")
    def put_record_format(
        self,
        *,
        mapping_parameters: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]],
        record_format_type: builtins.str,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping_parameters Kinesisanalyticsv2Application#mapping_parameters}
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat(
            mapping_parameters=mapping_parameters,
            record_format_type=record_format_type,
        )

        return typing.cast(None, jsii.invoke(self, "putRecordFormat", [value]))

    @jsii.member(jsii_name="resetRecordEncoding")
    def reset_record_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="recordColumn")
    def record_column(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnList":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnList", jsii.get(self, "recordColumn"))

    @builtins.property
    @jsii.member(jsii_name="recordFormat")
    def record_format(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatOutputReference", jsii.get(self, "recordFormat"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnInput")
    def record_column_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn"]]], jsii.get(self, "recordColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncodingInput")
    def record_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatInput")
    def record_format_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat"], jsii.get(self, "recordFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncoding")
    def record_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordEncoding"))

    @record_encoding.setter
    def record_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa95b419397c637412c52306cbf95cdd6ba63c82173e91b4a400c552c8d9099b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44cabe0542504722cb7e109c071a847bfb22eee32b8fc668c690e74756777abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_type: builtins.str,
        mapping: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.
        :param sql_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_type Kinesisanalyticsv2Application#sql_type}.
        :param mapping: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping Kinesisanalyticsv2Application#mapping}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcb20fcbd17b8bc92692a6122cb46967ab2a311fc4909c0bf8c4cb0d31f8eb37)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
            check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "sql_type": sql_type,
        }
        if mapping is not None:
            self._values["mapping"] = mapping

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_type Kinesisanalyticsv2Application#sql_type}.'''
        result = self._values.get("sql_type")
        assert result is not None, "Required property 'sql_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping Kinesisanalyticsv2Application#mapping}.'''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c00b9fec3d62a76c267f1381302431c6bb182fd22102ff68a7abe117d5327d89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e36c21444eed123390334bc87e6ee023ab98cee7008548f8f7c9a083b64af39)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e5b5c9cfe3bc5463b74b2c72ba7c9ce5e67da1e70528f5d321e54ffbfd6e1ef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__184b77fa82e754f77c38eb797bc28b4b6a7df00de56ea0a32fb53d0b169e66ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d73d165c02f739ae31badbe61edbcbd48f0a2111fdde6634c1ebb685c7dde74a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d5bc4b679c97c95710ced577fd6372e3d6b960d07874d1f68567857078b8737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e150c74cf8551bb04dda521256ada4eafce269574244c68271921454f2c4856)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMapping")
    def reset_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapping", []))

    @builtins.property
    @jsii.member(jsii_name="mappingInput")
    def mapping_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mappingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlTypeInput")
    def sql_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapping"))

    @mapping.setter
    def mapping(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b21d89cc1804e47f20fc163d54eb28a06f30069d79f333daca15235bf939211)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bbef5b916a656f8a93058b2517602c75142cf45017ac704f000921072dafeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sqlType")
    def sql_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlType"))

    @sql_type.setter
    def sql_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__866cab9939af722c8bb39329952f82b9e52579ab90f29b8981bb3aab776b67e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b62f681342e62a7c0e96fd628109b1aca137f192f295997746fe381bbc77fde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat",
    jsii_struct_bases=[],
    name_mapping={
        "mapping_parameters": "mappingParameters",
        "record_format_type": "recordFormatType",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat:
    def __init__(
        self,
        *,
        mapping_parameters: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]],
        record_format_type: builtins.str,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping_parameters Kinesisanalyticsv2Application#mapping_parameters}
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.
        '''
        if isinstance(mapping_parameters, dict):
            mapping_parameters = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters(**mapping_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4a3a0b5baa59bf5ebf0d8401ee3efbfe803e2ca0479264f8cb90a3a910a69d)
            check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mapping_parameters": mapping_parameters,
            "record_format_type": record_format_type,
        }

    @builtins.property
    def mapping_parameters(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters":
        '''mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping_parameters Kinesisanalyticsv2Application#mapping_parameters}
        '''
        result = self._values.get("mapping_parameters")
        assert result is not None, "Required property 'mapping_parameters' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters", result)

    @builtins.property
    def record_format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.'''
        result = self._values.get("record_format_type")
        assert result is not None, "Required property 'record_format_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters",
    jsii_struct_bases=[],
    name_mapping={
        "csv_mapping_parameters": "csvMappingParameters",
        "json_mapping_parameters": "jsonMappingParameters",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters:
    def __init__(
        self,
        *,
        csv_mapping_parameters: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        json_mapping_parameters: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv_mapping_parameters: csv_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#csv_mapping_parameters Kinesisanalyticsv2Application#csv_mapping_parameters}
        :param json_mapping_parameters: json_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#json_mapping_parameters Kinesisanalyticsv2Application#json_mapping_parameters}
        '''
        if isinstance(csv_mapping_parameters, dict):
            csv_mapping_parameters = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters(**csv_mapping_parameters)
        if isinstance(json_mapping_parameters, dict):
            json_mapping_parameters = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters(**json_mapping_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ecef25810511585f325126a2ce7d976f8ce263ec3693cb57ae807edeadade3e)
            check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
            check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if csv_mapping_parameters is not None:
            self._values["csv_mapping_parameters"] = csv_mapping_parameters
        if json_mapping_parameters is not None:
            self._values["json_mapping_parameters"] = json_mapping_parameters

    @builtins.property
    def csv_mapping_parameters(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters"]:
        '''csv_mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#csv_mapping_parameters Kinesisanalyticsv2Application#csv_mapping_parameters}
        '''
        result = self._values.get("csv_mapping_parameters")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters"], result)

    @builtins.property
    def json_mapping_parameters(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters"]:
        '''json_mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#json_mapping_parameters Kinesisanalyticsv2Application#json_mapping_parameters}
        '''
        result = self._values.get("json_mapping_parameters")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters",
    jsii_struct_bases=[],
    name_mapping={
        "record_column_delimiter": "recordColumnDelimiter",
        "record_row_delimiter": "recordRowDelimiter",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters:
    def __init__(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column_delimiter Kinesisanalyticsv2Application#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_delimiter Kinesisanalyticsv2Application#record_row_delimiter}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfc6d209b8d7aee41a215db6f2b68a64bda6d63103a5801af5591628fbc302aa)
            check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
            check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_column_delimiter": record_column_delimiter,
            "record_row_delimiter": record_row_delimiter,
        }

    @builtins.property
    def record_column_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column_delimiter Kinesisanalyticsv2Application#record_column_delimiter}.'''
        result = self._values.get("record_column_delimiter")
        assert result is not None, "Required property 'record_column_delimiter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_row_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_delimiter Kinesisanalyticsv2Application#record_row_delimiter}.'''
        result = self._values.get("record_row_delimiter")
        assert result is not None, "Required property 'record_row_delimiter' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dbf03d4d19faca062397b2e1f4c7671713ef27657ffbb913024bb81c9b102850)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="recordColumnDelimiterInput")
    def record_column_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordColumnDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiterInput")
    def record_row_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnDelimiter")
    def record_column_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordColumnDelimiter"))

    @record_column_delimiter.setter
    def record_column_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70bce5a249d2313df669ec0994e83b26cedee74bc22c766ae6c2011c31ea266a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordColumnDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiter")
    def record_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowDelimiter"))

    @record_row_delimiter.setter
    def record_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d088639fd01ed9259c54da4d671bd66c510e3ceba54977c890341471bff2ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b49e163bc9b05722f4f181fc12436722a59e9c7a7001b31f546dc4067b1f955)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters",
    jsii_struct_bases=[],
    name_mapping={"record_row_path": "recordRowPath"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters:
    def __init__(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_path Kinesisanalyticsv2Application#record_row_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af59f43165b148519b784b9227c112b4921371c4aa47190cb641d97a5e4e59e8)
            check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_row_path": record_row_path,
        }

    @builtins.property
    def record_row_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_path Kinesisanalyticsv2Application#record_row_path}.'''
        result = self._values.get("record_row_path")
        assert result is not None, "Required property 'record_row_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c7dbd547f4d561fa66da73c6219fc826f9c9fd43cde02d51b48676111238ad8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="recordRowPathInput")
    def record_row_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowPathInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowPath")
    def record_row_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowPath"))

    @record_row_path.setter
    def record_row_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928b30788750684d7c4a78b81cca79f5290b334c66fbd1adc34cbbfde53801ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55bc0e49c1e6a0de10abf17a92a4ffed6f1452ec89ec9ad5bda973fcb78ad690)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__feddb4b6e96ee0693f8d1f49f99af53bd0844d961f9969ed10fea50448db3c4a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCsvMappingParameters")
    def put_csv_mapping_parameters(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column_delimiter Kinesisanalyticsv2Application#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_delimiter Kinesisanalyticsv2Application#record_row_delimiter}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters(
            record_column_delimiter=record_column_delimiter,
            record_row_delimiter=record_row_delimiter,
        )

        return typing.cast(None, jsii.invoke(self, "putCsvMappingParameters", [value]))

    @jsii.member(jsii_name="putJsonMappingParameters")
    def put_json_mapping_parameters(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_path Kinesisanalyticsv2Application#record_row_path}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters(
            record_row_path=record_row_path
        )

        return typing.cast(None, jsii.invoke(self, "putJsonMappingParameters", [value]))

    @jsii.member(jsii_name="resetCsvMappingParameters")
    def reset_csv_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvMappingParameters", []))

    @jsii.member(jsii_name="resetJsonMappingParameters")
    def reset_json_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonMappingParameters", []))

    @builtins.property
    @jsii.member(jsii_name="csvMappingParameters")
    def csv_mapping_parameters(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference, jsii.get(self, "csvMappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="jsonMappingParameters")
    def json_mapping_parameters(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference, jsii.get(self, "jsonMappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="csvMappingParametersInput")
    def csv_mapping_parameters_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters], jsii.get(self, "csvMappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonMappingParametersInput")
    def json_mapping_parameters_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters], jsii.get(self, "jsonMappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86354b28d10bb954f5512a36235682d2bce82a3d386a81e7b602310611188000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc4e6118ea1541edade3cb1aa617bb5b7ea53397d8aaf98f6c91ee48c95d2d82)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMappingParameters")
    def put_mapping_parameters(
        self,
        *,
        csv_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
        json_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv_mapping_parameters: csv_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#csv_mapping_parameters Kinesisanalyticsv2Application#csv_mapping_parameters}
        :param json_mapping_parameters: json_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#json_mapping_parameters Kinesisanalyticsv2Application#json_mapping_parameters}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters(
            csv_mapping_parameters=csv_mapping_parameters,
            json_mapping_parameters=json_mapping_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putMappingParameters", [value]))

    @builtins.property
    @jsii.member(jsii_name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersOutputReference, jsii.get(self, "mappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="mappingParametersInput")
    def mapping_parameters_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters], jsii.get(self, "mappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatTypeInput")
    def record_format_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordFormatTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @record_format_type.setter
    def record_format_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8029513dc5c15128885125c948ac2ac1cbf484b507a92d15ba361f64db4f5189)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordFormatType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb157d3ef21a96833b0997119d6558603593e8d4be568b2f48606ac9e100d4aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"input_starting_position": "inputStartingPosition"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration:
    def __init__(
        self,
        *,
        input_starting_position: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input_starting_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_starting_position Kinesisanalyticsv2Application#input_starting_position}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15422c5702a970622cf31f2e1ff82be99e35729b79d4ed05d5baa3a44cc66aa5)
            check_type(argname="argument input_starting_position", value=input_starting_position, expected_type=type_hints["input_starting_position"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if input_starting_position is not None:
            self._values["input_starting_position"] = input_starting_position

    @builtins.property
    def input_starting_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_starting_position Kinesisanalyticsv2Application#input_starting_position}.'''
        result = self._values.get("input_starting_position")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00fcff032d35f00cb2006b8705287c9d8eb8896793049b5aecf72fcbb152180d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77001cb8cee83d6cea7d0d3dacdfdccb615fac722349bcdd31f60eac912af1de)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12dd12b67a00ee460f49b31c693455be263fbbb4929b755f61fb667305aa8d12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7bd1c9f426528694204da790430f07aa628d0bdf0511cafd912620171574e80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f18e05f3d82fe215a71fc6daa547da6dbb403ef0ce88de35aa30febed6f87e4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb7fe4591b88d50632e51ffee765fdeeed504e13e41fd2f8104c375e82bc06f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86cb19d7a5eff26c72e68389ffb73b0be4668cf456338843ba7213cdc97cfb5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetInputStartingPosition")
    def reset_input_starting_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputStartingPosition", []))

    @builtins.property
    @jsii.member(jsii_name="inputStartingPositionInput")
    def input_starting_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputStartingPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="inputStartingPosition")
    def input_starting_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputStartingPosition"))

    @input_starting_position.setter
    def input_starting_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5612ff68b5fabfca310702233c28d2c960d243d485e8f7e32629c742f3b954bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputStartingPosition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6373dbaf70a7dbddaddf4c7a0c783f53affb6a43fc7bcc1b266772a647d32084)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1742dbe1a289b0e094c8c88063d72dc9dd8a9f3d67cbd65f1dd98d80de6c5dce)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a50d08f71abd80537fa2977841c89dead99ee7467b53a7fc13b308634c2354d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af400bade83b740b6fc1bd028485969e747fd611da09f970f864ff8e6a75091d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f6a03d03580794e170c7de3a96712dc933e40007d01012c7f6d81e8200c7d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c929e6d35a2c9638dcc5af7c0ec6b56364e61cce43fc65514621feb470f57ed)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0746241dd6bbc4e7c37c583ea917ca13134b6980bcec8840d8cd16ee45b089b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec5783102f58aca8f361f77072b70120f5571fa25637906a440f5971f614ed0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f995b65c8e339e555284b00db7bcce6b3c3a6ad6dd7180fef95d3db3a930be77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fa232a259895087a6e7d78b44852a3a46330f46e59473a880220aab9f1b654e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInputParallelism")
    def put_input_parallelism(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#count Kinesisanalyticsv2Application#count}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism(
            count=count
        )

        return typing.cast(None, jsii.invoke(self, "putInputParallelism", [value]))

    @jsii.member(jsii_name="putInputProcessingConfiguration")
    def put_input_processing_configuration(
        self,
        *,
        input_lambda_processor: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param input_lambda_processor: input_lambda_processor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_lambda_processor Kinesisanalyticsv2Application#input_lambda_processor}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration(
            input_lambda_processor=input_lambda_processor
        )

        return typing.cast(None, jsii.invoke(self, "putInputProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putInputSchema")
    def put_input_schema(
        self,
        *,
        record_column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat, typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_column: record_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column Kinesisanalyticsv2Application#record_column}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format Kinesisanalyticsv2Application#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_encoding Kinesisanalyticsv2Application#record_encoding}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema(
            record_column=record_column,
            record_format=record_format,
            record_encoding=record_encoding,
        )

        return typing.cast(None, jsii.invoke(self, "putInputSchema", [value]))

    @jsii.member(jsii_name="putInputStartingPositionConfiguration")
    def put_input_starting_position_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94bb534d9f38523a35b5b5ebf06f7866523855d93f6d42ca75b5b6122f431c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInputStartingPositionConfiguration", [value]))

    @jsii.member(jsii_name="putKinesisFirehoseInput")
    def put_kinesis_firehose_input(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput(
            resource_arn=resource_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehoseInput", [value]))

    @jsii.member(jsii_name="putKinesisStreamsInput")
    def put_kinesis_streams_input(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput(
            resource_arn=resource_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStreamsInput", [value]))

    @jsii.member(jsii_name="resetInputParallelism")
    def reset_input_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputParallelism", []))

    @jsii.member(jsii_name="resetInputProcessingConfiguration")
    def reset_input_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputProcessingConfiguration", []))

    @jsii.member(jsii_name="resetInputStartingPositionConfiguration")
    def reset_input_starting_position_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputStartingPositionConfiguration", []))

    @jsii.member(jsii_name="resetKinesisFirehoseInput")
    def reset_kinesis_firehose_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehoseInput", []))

    @jsii.member(jsii_name="resetKinesisStreamsInput")
    def reset_kinesis_streams_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStreamsInput", []))

    @builtins.property
    @jsii.member(jsii_name="inAppStreamNames")
    def in_app_stream_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inAppStreamNames"))

    @builtins.property
    @jsii.member(jsii_name="inputId")
    def input_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputId"))

    @builtins.property
    @jsii.member(jsii_name="inputParallelism")
    def input_parallelism(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismOutputReference, jsii.get(self, "inputParallelism"))

    @builtins.property
    @jsii.member(jsii_name="inputProcessingConfiguration")
    def input_processing_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationOutputReference, jsii.get(self, "inputProcessingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="inputSchema")
    def input_schema(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaOutputReference, jsii.get(self, "inputSchema"))

    @builtins.property
    @jsii.member(jsii_name="inputStartingPositionConfiguration")
    def input_starting_position_configuration(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationList:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationList, jsii.get(self, "inputStartingPositionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseInput")
    def kinesis_firehose_input(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputOutputReference, jsii.get(self, "kinesisFirehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamsInput")
    def kinesis_streams_input(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputOutputReference, jsii.get(self, "kinesisStreamsInput"))

    @builtins.property
    @jsii.member(jsii_name="inputParallelismInput")
    def input_parallelism_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism], jsii.get(self, "inputParallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="inputProcessingConfigurationInput")
    def input_processing_configuration_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration], jsii.get(self, "inputProcessingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="inputSchemaInput")
    def input_schema_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema], jsii.get(self, "inputSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="inputStartingPositionConfigurationInput")
    def input_starting_position_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration]]], jsii.get(self, "inputStartingPositionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseInputInput")
    def kinesis_firehose_input_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput], jsii.get(self, "kinesisFirehoseInputInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamsInputInput")
    def kinesis_streams_input_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput], jsii.get(self, "kinesisStreamsInputInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9aac53550f8bea35a0e5e282fb225008886c6199a55fc0cdad2b9bfe2b81be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cca5de6a383e476182a2c5c520a468bc6aafe6296e56724ee11218f08fa0c5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput",
    jsii_struct_bases=[],
    name_mapping={
        "destination_schema": "destinationSchema",
        "name": "name",
        "kinesis_firehose_output": "kinesisFirehoseOutput",
        "kinesis_streams_output": "kinesisStreamsOutput",
        "lambda_output": "lambdaOutput",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput:
    def __init__(
        self,
        *,
        destination_schema: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        kinesis_firehose_output: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_streams_output: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_output: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param destination_schema: destination_schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#destination_schema Kinesisanalyticsv2Application#destination_schema}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.
        :param kinesis_firehose_output: kinesis_firehose_output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_firehose_output Kinesisanalyticsv2Application#kinesis_firehose_output}
        :param kinesis_streams_output: kinesis_streams_output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_streams_output Kinesisanalyticsv2Application#kinesis_streams_output}
        :param lambda_output: lambda_output block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#lambda_output Kinesisanalyticsv2Application#lambda_output}
        '''
        if isinstance(destination_schema, dict):
            destination_schema = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema(**destination_schema)
        if isinstance(kinesis_firehose_output, dict):
            kinesis_firehose_output = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput(**kinesis_firehose_output)
        if isinstance(kinesis_streams_output, dict):
            kinesis_streams_output = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput(**kinesis_streams_output)
        if isinstance(lambda_output, dict):
            lambda_output = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput(**lambda_output)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56589e745c082b9d1234375257c9119a62742a669aa0849d7e720eb12b0ec08a)
            check_type(argname="argument destination_schema", value=destination_schema, expected_type=type_hints["destination_schema"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument kinesis_firehose_output", value=kinesis_firehose_output, expected_type=type_hints["kinesis_firehose_output"])
            check_type(argname="argument kinesis_streams_output", value=kinesis_streams_output, expected_type=type_hints["kinesis_streams_output"])
            check_type(argname="argument lambda_output", value=lambda_output, expected_type=type_hints["lambda_output"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_schema": destination_schema,
            "name": name,
        }
        if kinesis_firehose_output is not None:
            self._values["kinesis_firehose_output"] = kinesis_firehose_output
        if kinesis_streams_output is not None:
            self._values["kinesis_streams_output"] = kinesis_streams_output
        if lambda_output is not None:
            self._values["lambda_output"] = lambda_output

    @builtins.property
    def destination_schema(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema":
        '''destination_schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#destination_schema Kinesisanalyticsv2Application#destination_schema}
        '''
        result = self._values.get("destination_schema")
        assert result is not None, "Required property 'destination_schema' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kinesis_firehose_output(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput"]:
        '''kinesis_firehose_output block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_firehose_output Kinesisanalyticsv2Application#kinesis_firehose_output}
        '''
        result = self._values.get("kinesis_firehose_output")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput"], result)

    @builtins.property
    def kinesis_streams_output(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput"]:
        '''kinesis_streams_output block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_streams_output Kinesisanalyticsv2Application#kinesis_streams_output}
        '''
        result = self._values.get("kinesis_streams_output")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput"], result)

    @builtins.property
    def lambda_output(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput"]:
        '''lambda_output block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#lambda_output Kinesisanalyticsv2Application#lambda_output}
        '''
        result = self._values.get("lambda_output")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema",
    jsii_struct_bases=[],
    name_mapping={"record_format_type": "recordFormatType"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema:
    def __init__(self, *, record_format_type: builtins.str) -> None:
        '''
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504968930b1ff55ec17a7142b122072c643ac30745fc00b180fc9da15e01d848)
            check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_format_type": record_format_type,
        }

    @builtins.property
    def record_format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.'''
        result = self._values.get("record_format_type")
        assert result is not None, "Required property 'record_format_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0163c7653e787b159d118695e4168d5b0c3f99271bbdb516a1b7fdbca43a7ae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="recordFormatTypeInput")
    def record_format_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordFormatTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @record_format_type.setter
    def record_format_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3e0bb159fb290156b10a1a355bc0edc356a5d740d28582d5318404d1c19e7d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordFormatType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60dd700daa80113e4202c447c86e46c234fe70082b04c7c7289b3064272d6919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23c338d489dc9a79d1fcfb011c179da83a3dca8cbc194cf1db01b9e393af9da)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4afc51bebcdc0c50e7eb155d74436363f7f72671b35fb0866e80fa393905a24)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42957d7f2f99692f7f941712fe074cf9118412f21665822bada8972262c3bcde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c9d9fd3927f9abe4b346f07a9fd30eed383122219842cede7cf425f56de840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c467999e3b3d39e383228caf490a68d8731ffd95ffcfe4b4542f9b02452379)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2eea63d079e080ed3a0fc0e62d31c509563cda3892d21c4ea3029eeceda34e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be8306cfde4b0dab2a432cac7b6ae21e7b00d2b4a27c9281ca027b4dfd33038)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6366ba2be9b1b203d652121b1c31f58d78b86fd659f50b0410aee00722cd5c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14390f607f7b5ac3706fbf470a118b087954258b5ec97b238feee0482cbe8282)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7360a9efed79fda760f2273ecb75cfce6f7154d3ca7e188c0dd05d6820661412)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aa48bdb47fbdb5346f92b9763e4ba96f37f8485bef026268973f40b5ee26ea4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aabb7c62846c2225c1fb30ccef5b49fb9c795396ba5a490a7130ea3abf1f54d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1a5afeb905daaf6620bced1faf3cf40bac82fdd311ba0eca973bffd391aad35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e438533cbf7e08d161ea1012dc3f1bc1b93a59169fdf4c1b64bc24272dd99a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320fc79095549f0d4f0cfcf0b6da113660a9ca6c0e1cf2fb00fdc918a68d6a38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b20e05ed8aae13649093ad43835d2359608dd88e83d632702d9def9b066d84c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__404b8dd10e050089fbb4fc869f15f9b348b0ceeda446967e501e592588932045)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106e67d188a1102a324f7de90e1eb625a6c7c6eb5d9a36433ca96e0ce971dd06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__813d3e0bbcf134210d8c3589170e9af3aa60f8c5d5ae7205ca583386850b1d9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDestinationSchema")
    def put_destination_schema(self, *, record_format_type: builtins.str) -> None:
        '''
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema(
            record_format_type=record_format_type
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationSchema", [value]))

    @jsii.member(jsii_name="putKinesisFirehoseOutput")
    def put_kinesis_firehose_output(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput(
            resource_arn=resource_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehoseOutput", [value]))

    @jsii.member(jsii_name="putKinesisStreamsOutput")
    def put_kinesis_streams_output(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput(
            resource_arn=resource_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStreamsOutput", [value]))

    @jsii.member(jsii_name="putLambdaOutput")
    def put_lambda_output(self, *, resource_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#resource_arn Kinesisanalyticsv2Application#resource_arn}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput(
            resource_arn=resource_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaOutput", [value]))

    @jsii.member(jsii_name="resetKinesisFirehoseOutput")
    def reset_kinesis_firehose_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehoseOutput", []))

    @jsii.member(jsii_name="resetKinesisStreamsOutput")
    def reset_kinesis_streams_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStreamsOutput", []))

    @jsii.member(jsii_name="resetLambdaOutput")
    def reset_lambda_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaOutput", []))

    @builtins.property
    @jsii.member(jsii_name="destinationSchema")
    def destination_schema(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaOutputReference, jsii.get(self, "destinationSchema"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseOutput")
    def kinesis_firehose_output(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputOutputReference, jsii.get(self, "kinesisFirehoseOutput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamsOutput")
    def kinesis_streams_output(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputOutputReference, jsii.get(self, "kinesisStreamsOutput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaOutput")
    def lambda_output(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputOutputReference, jsii.get(self, "lambdaOutput"))

    @builtins.property
    @jsii.member(jsii_name="outputId")
    def output_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputId"))

    @builtins.property
    @jsii.member(jsii_name="destinationSchemaInput")
    def destination_schema_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema], jsii.get(self, "destinationSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseOutputInput")
    def kinesis_firehose_output_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput], jsii.get(self, "kinesisFirehoseOutputInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamsOutputInput")
    def kinesis_streams_output_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput], jsii.get(self, "kinesisStreamsOutputInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaOutputInput")
    def lambda_output_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput], jsii.get(self, "lambdaOutputInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d8af56bd3c8cafb44103b418f144144ffaf71934a13386ed50e91598153349d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee720bb5f7ea6a934971264c19d0eba896736c100e2e63bea6a530636eda39fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f64d0990ed211b4663a6adb82918f8bdb0e6a2354d61becba2e4a9fe288a6eb7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInput")
    def put_input(
        self,
        *,
        input_schema: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema, typing.Dict[builtins.str, typing.Any]],
        name_prefix: builtins.str,
        input_parallelism: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism, typing.Dict[builtins.str, typing.Any]]] = None,
        input_processing_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        input_starting_position_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
        kinesis_firehose_input: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput, typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_streams_input: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param input_schema: input_schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_schema Kinesisanalyticsv2Application#input_schema}
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name_prefix Kinesisanalyticsv2Application#name_prefix}.
        :param input_parallelism: input_parallelism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_parallelism Kinesisanalyticsv2Application#input_parallelism}
        :param input_processing_configuration: input_processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_processing_configuration Kinesisanalyticsv2Application#input_processing_configuration}
        :param input_starting_position_configuration: input_starting_position_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#input_starting_position_configuration Kinesisanalyticsv2Application#input_starting_position_configuration}
        :param kinesis_firehose_input: kinesis_firehose_input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_firehose_input Kinesisanalyticsv2Application#kinesis_firehose_input}
        :param kinesis_streams_input: kinesis_streams_input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#kinesis_streams_input Kinesisanalyticsv2Application#kinesis_streams_input}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput(
            input_schema=input_schema,
            name_prefix=name_prefix,
            input_parallelism=input_parallelism,
            input_processing_configuration=input_processing_configuration,
            input_starting_position_configuration=input_starting_position_configuration,
            kinesis_firehose_input=kinesis_firehose_input,
            kinesis_streams_input=kinesis_streams_input,
        )

        return typing.cast(None, jsii.invoke(self, "putInput", [value]))

    @jsii.member(jsii_name="putOutput")
    def put_output(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b8c2599434ca3a62fff6ef6fa4adb4344baa36bb317e82d5a9e96593da436d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOutput", [value]))

    @jsii.member(jsii_name="putReferenceDataSource")
    def put_reference_data_source(
        self,
        *,
        reference_schema: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema", typing.Dict[builtins.str, typing.Any]],
        s3_reference_data_source: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource", typing.Dict[builtins.str, typing.Any]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param reference_schema: reference_schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#reference_schema Kinesisanalyticsv2Application#reference_schema}
        :param s3_reference_data_source: s3_reference_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#s3_reference_data_source Kinesisanalyticsv2Application#s3_reference_data_source}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#table_name Kinesisanalyticsv2Application#table_name}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource(
            reference_schema=reference_schema,
            s3_reference_data_source=s3_reference_data_source,
            table_name=table_name,
        )

        return typing.cast(None, jsii.invoke(self, "putReferenceDataSource", [value]))

    @jsii.member(jsii_name="resetInput")
    def reset_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInput", []))

    @jsii.member(jsii_name="resetOutput")
    def reset_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutput", []))

    @jsii.member(jsii_name="resetReferenceDataSource")
    def reset_reference_data_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReferenceDataSource", []))

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputOutputReference, jsii.get(self, "input"))

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputList:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputList, jsii.get(self, "output"))

    @builtins.property
    @jsii.member(jsii_name="referenceDataSource")
    def reference_data_source(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceOutputReference", jsii.get(self, "referenceDataSource"))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="outputInput")
    def output_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput]]], jsii.get(self, "outputInput"))

    @builtins.property
    @jsii.member(jsii_name="referenceDataSourceInput")
    def reference_data_source_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource"], jsii.get(self, "referenceDataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5631fd3a105932ca578f3a569266d75db9c926543dc65b5cc1937e3895136d4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource",
    jsii_struct_bases=[],
    name_mapping={
        "reference_schema": "referenceSchema",
        "s3_reference_data_source": "s3ReferenceDataSource",
        "table_name": "tableName",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource:
    def __init__(
        self,
        *,
        reference_schema: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema", typing.Dict[builtins.str, typing.Any]],
        s3_reference_data_source: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource", typing.Dict[builtins.str, typing.Any]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param reference_schema: reference_schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#reference_schema Kinesisanalyticsv2Application#reference_schema}
        :param s3_reference_data_source: s3_reference_data_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#s3_reference_data_source Kinesisanalyticsv2Application#s3_reference_data_source}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#table_name Kinesisanalyticsv2Application#table_name}.
        '''
        if isinstance(reference_schema, dict):
            reference_schema = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema(**reference_schema)
        if isinstance(s3_reference_data_source, dict):
            s3_reference_data_source = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource(**s3_reference_data_source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ffff9c3b1bb3cf45c38f3325c4181bd58cb81018ad3b4e7013e7d62941fac6)
            check_type(argname="argument reference_schema", value=reference_schema, expected_type=type_hints["reference_schema"])
            check_type(argname="argument s3_reference_data_source", value=s3_reference_data_source, expected_type=type_hints["s3_reference_data_source"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "reference_schema": reference_schema,
            "s3_reference_data_source": s3_reference_data_source,
            "table_name": table_name,
        }

    @builtins.property
    def reference_schema(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema":
        '''reference_schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#reference_schema Kinesisanalyticsv2Application#reference_schema}
        '''
        result = self._values.get("reference_schema")
        assert result is not None, "Required property 'reference_schema' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema", result)

    @builtins.property
    def s3_reference_data_source(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource":
        '''s3_reference_data_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#s3_reference_data_source Kinesisanalyticsv2Application#s3_reference_data_source}
        '''
        result = self._values.get("s3_reference_data_source")
        assert result is not None, "Required property 's3_reference_data_source' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource", result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#table_name Kinesisanalyticsv2Application#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c5d4fa0b7289b66ba1562b63a47f583b333761f941bc82d5a2e62e8dc27bf73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putReferenceSchema")
    def put_reference_schema(
        self,
        *,
        record_column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_column: record_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column Kinesisanalyticsv2Application#record_column}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format Kinesisanalyticsv2Application#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_encoding Kinesisanalyticsv2Application#record_encoding}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema(
            record_column=record_column,
            record_format=record_format,
            record_encoding=record_encoding,
        )

        return typing.cast(None, jsii.invoke(self, "putReferenceSchema", [value]))

    @jsii.member(jsii_name="putS3ReferenceDataSource")
    def put_s3_reference_data_source(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#bucket_arn Kinesisanalyticsv2Application#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#file_key Kinesisanalyticsv2Application#file_key}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource(
            bucket_arn=bucket_arn, file_key=file_key
        )

        return typing.cast(None, jsii.invoke(self, "putS3ReferenceDataSource", [value]))

    @builtins.property
    @jsii.member(jsii_name="referenceId")
    def reference_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "referenceId"))

    @builtins.property
    @jsii.member(jsii_name="referenceSchema")
    def reference_schema(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaOutputReference", jsii.get(self, "referenceSchema"))

    @builtins.property
    @jsii.member(jsii_name="s3ReferenceDataSource")
    def s3_reference_data_source(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceOutputReference", jsii.get(self, "s3ReferenceDataSource"))

    @builtins.property
    @jsii.member(jsii_name="referenceSchemaInput")
    def reference_schema_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema"], jsii.get(self, "referenceSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ReferenceDataSourceInput")
    def s3_reference_data_source_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource"], jsii.get(self, "s3ReferenceDataSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c496970f276f3b0719eb6b7970d5c856d816a204ba88bcbc2ff45d6dc32a31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd2d4b58a19380df96af183b93145cc722b251feff78993047d898f064acf82f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema",
    jsii_struct_bases=[],
    name_mapping={
        "record_column": "recordColumn",
        "record_format": "recordFormat",
        "record_encoding": "recordEncoding",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema:
    def __init__(
        self,
        *,
        record_column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_column: record_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column Kinesisanalyticsv2Application#record_column}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format Kinesisanalyticsv2Application#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_encoding Kinesisanalyticsv2Application#record_encoding}.
        '''
        if isinstance(record_format, dict):
            record_format = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat(**record_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c525d2b462efe1c4d6d8c21f117dbd8553c4cf134e4f4edd25bec667481cfb)
            check_type(argname="argument record_column", value=record_column, expected_type=type_hints["record_column"])
            check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
            check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_column": record_column,
            "record_format": record_format,
        }
        if record_encoding is not None:
            self._values["record_encoding"] = record_encoding

    @builtins.property
    def record_column(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn"]]:
        '''record_column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column Kinesisanalyticsv2Application#record_column}
        '''
        result = self._values.get("record_column")
        assert result is not None, "Required property 'record_column' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn"]], result)

    @builtins.property
    def record_format(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat":
        '''record_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format Kinesisanalyticsv2Application#record_format}
        '''
        result = self._values.get("record_format")
        assert result is not None, "Required property 'record_format' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat", result)

    @builtins.property
    def record_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_encoding Kinesisanalyticsv2Application#record_encoding}.'''
        result = self._values.get("record_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29281b993dc5c7fb9d3585b9a64ac9dd15d3dafc717154dbcab80da935ca6cab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRecordColumn")
    def put_record_column(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd704d573aba9b05475b7ee2a086f3c88eec0a86fb4de7682c9ddcdbebd2b633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordColumn", [value]))

    @jsii.member(jsii_name="putRecordFormat")
    def put_record_format(
        self,
        *,
        mapping_parameters: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]],
        record_format_type: builtins.str,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping_parameters Kinesisanalyticsv2Application#mapping_parameters}
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat(
            mapping_parameters=mapping_parameters,
            record_format_type=record_format_type,
        )

        return typing.cast(None, jsii.invoke(self, "putRecordFormat", [value]))

    @jsii.member(jsii_name="resetRecordEncoding")
    def reset_record_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="recordColumn")
    def record_column(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnList":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnList", jsii.get(self, "recordColumn"))

    @builtins.property
    @jsii.member(jsii_name="recordFormat")
    def record_format(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatOutputReference":
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatOutputReference", jsii.get(self, "recordFormat"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnInput")
    def record_column_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn"]]], jsii.get(self, "recordColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncodingInput")
    def record_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatInput")
    def record_format_input(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat"]:
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat"], jsii.get(self, "recordFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncoding")
    def record_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordEncoding"))

    @record_encoding.setter
    def record_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42dbb7fe7aab1dc109718ec586c16fe201e240c472b172a8275629f75416894e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a4e04d97dab97249e150d878d87bae96cb3614fe9e32d41d1307a09327c6d99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_type: builtins.str,
        mapping: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.
        :param sql_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_type Kinesisanalyticsv2Application#sql_type}.
        :param mapping: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping Kinesisanalyticsv2Application#mapping}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bddcf7aa72a1e793d05829a4aac2dffe29dc0851293fdca33d0dd40086df9bc2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
            check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "sql_type": sql_type,
        }
        if mapping is not None:
            self._values["mapping"] = mapping

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#sql_type Kinesisanalyticsv2Application#sql_type}.'''
        result = self._values.get("sql_type")
        assert result is not None, "Required property 'sql_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping Kinesisanalyticsv2Application#mapping}.'''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47c5f8cf357c52e984f34fa10eb40047e39ecf7d796074dd1b3c251cde4180e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe47e4e6812d9f89d6e334b6e800556f067e990a8e94eb757bd06cbafce65db)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c181383f214b96f62fc1376942eb99f491d5d8c407034c86f130e325118c13d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91f5f851d68c838732583e9056c3855399dcbd3712eda14f59a45cc14e030d3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4b9d837017e0d4a60db73cb686c061a4c96466972b066a76769fa5ebb7abd9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846819791b231cd564ac0480d88c12e64795d7943dd2ab0505cd68e50aeaa9de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d88319626bc96c544dce3eff79f5a6fed9dd7267d6471a448cf492602034fe2c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMapping")
    def reset_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapping", []))

    @builtins.property
    @jsii.member(jsii_name="mappingInput")
    def mapping_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mappingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlTypeInput")
    def sql_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapping"))

    @mapping.setter
    def mapping(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9777c6d049da5c5e9373071625bdb1589c291348a3962e6f025696f5a0cae867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913c9811d5c1730101e96c85c7c45cdaefcc06ee8c3891be5fa8f3a648c15952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sqlType")
    def sql_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlType"))

    @sql_type.setter
    def sql_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f9853a7d324a5e998fe8459d345a34db4d39701797ac0bc5b86eb53979474bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40456da42a1dcd5990acf0baee2f17b94a7a0a6332530e6b01decf40305ca999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat",
    jsii_struct_bases=[],
    name_mapping={
        "mapping_parameters": "mappingParameters",
        "record_format_type": "recordFormatType",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat:
    def __init__(
        self,
        *,
        mapping_parameters: typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]],
        record_format_type: builtins.str,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping_parameters Kinesisanalyticsv2Application#mapping_parameters}
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.
        '''
        if isinstance(mapping_parameters, dict):
            mapping_parameters = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters(**mapping_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f25eecdb46764a4b647c52af136be47b1e469eccaade3c45d4fda2edd254971)
            check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mapping_parameters": mapping_parameters,
            "record_format_type": record_format_type,
        }

    @builtins.property
    def mapping_parameters(
        self,
    ) -> "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters":
        '''mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#mapping_parameters Kinesisanalyticsv2Application#mapping_parameters}
        '''
        result = self._values.get("mapping_parameters")
        assert result is not None, "Required property 'mapping_parameters' is missing"
        return typing.cast("Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters", result)

    @builtins.property
    def record_format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_format_type Kinesisanalyticsv2Application#record_format_type}.'''
        result = self._values.get("record_format_type")
        assert result is not None, "Required property 'record_format_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters",
    jsii_struct_bases=[],
    name_mapping={
        "csv_mapping_parameters": "csvMappingParameters",
        "json_mapping_parameters": "jsonMappingParameters",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters:
    def __init__(
        self,
        *,
        csv_mapping_parameters: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        json_mapping_parameters: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv_mapping_parameters: csv_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#csv_mapping_parameters Kinesisanalyticsv2Application#csv_mapping_parameters}
        :param json_mapping_parameters: json_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#json_mapping_parameters Kinesisanalyticsv2Application#json_mapping_parameters}
        '''
        if isinstance(csv_mapping_parameters, dict):
            csv_mapping_parameters = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters(**csv_mapping_parameters)
        if isinstance(json_mapping_parameters, dict):
            json_mapping_parameters = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters(**json_mapping_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a2d737b9d09fc05c90ae6467a5c733b79702ce3864e7ef8385605582f8914a)
            check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
            check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if csv_mapping_parameters is not None:
            self._values["csv_mapping_parameters"] = csv_mapping_parameters
        if json_mapping_parameters is not None:
            self._values["json_mapping_parameters"] = json_mapping_parameters

    @builtins.property
    def csv_mapping_parameters(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters"]:
        '''csv_mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#csv_mapping_parameters Kinesisanalyticsv2Application#csv_mapping_parameters}
        '''
        result = self._values.get("csv_mapping_parameters")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters"], result)

    @builtins.property
    def json_mapping_parameters(
        self,
    ) -> typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters"]:
        '''json_mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#json_mapping_parameters Kinesisanalyticsv2Application#json_mapping_parameters}
        '''
        result = self._values.get("json_mapping_parameters")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters",
    jsii_struct_bases=[],
    name_mapping={
        "record_column_delimiter": "recordColumnDelimiter",
        "record_row_delimiter": "recordRowDelimiter",
    },
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters:
    def __init__(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column_delimiter Kinesisanalyticsv2Application#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_delimiter Kinesisanalyticsv2Application#record_row_delimiter}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4eef6591ab2e9de801dbcf7c1e6d6de65d3f9ce203f5979badcfcd09fbed47a)
            check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
            check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_column_delimiter": record_column_delimiter,
            "record_row_delimiter": record_row_delimiter,
        }

    @builtins.property
    def record_column_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column_delimiter Kinesisanalyticsv2Application#record_column_delimiter}.'''
        result = self._values.get("record_column_delimiter")
        assert result is not None, "Required property 'record_column_delimiter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_row_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_delimiter Kinesisanalyticsv2Application#record_row_delimiter}.'''
        result = self._values.get("record_row_delimiter")
        assert result is not None, "Required property 'record_row_delimiter' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a06849414bb953268fddfcde0269bdc146f633835169c6f38f25734a722896cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="recordColumnDelimiterInput")
    def record_column_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordColumnDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiterInput")
    def record_row_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnDelimiter")
    def record_column_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordColumnDelimiter"))

    @record_column_delimiter.setter
    def record_column_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62e5151c2ec1f3d9957ab3ded090380d3731f554c7145022fd783b21ac940f56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordColumnDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiter")
    def record_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowDelimiter"))

    @record_row_delimiter.setter
    def record_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb66465a0b3d142d9e1d4f0a0d2f63023640fc129ef5637f39de76baabf6011)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ba65990d84aff4aa1fa23082876e55dd1f42af629dcba5c0333a9979ebe8ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters",
    jsii_struct_bases=[],
    name_mapping={"record_row_path": "recordRowPath"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters:
    def __init__(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_path Kinesisanalyticsv2Application#record_row_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a01f217f48bdf023f4eb607124819a4725cee1092c57409038a04c17b67a60e)
            check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_row_path": record_row_path,
        }

    @builtins.property
    def record_row_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_path Kinesisanalyticsv2Application#record_row_path}.'''
        result = self._values.get("record_row_path")
        assert result is not None, "Required property 'record_row_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70a0aca83b2b32c89904119aeca6802e59170a37b06f08f2f21b804b628853f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="recordRowPathInput")
    def record_row_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowPathInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowPath")
    def record_row_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowPath"))

    @record_row_path.setter
    def record_row_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286c497e4f28a2e6926d83a0c51e03cc99d9e22535bd0e497b594670dd1f198e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d758c80e2a1a423dc564ec119fb4d74b9b93b63e8bcb747816e075fc295b6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aad966332960c222d00cf18448818408b07d105aab8a1183578b4a83332291a2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCsvMappingParameters")
    def put_csv_mapping_parameters(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_column_delimiter Kinesisanalyticsv2Application#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_delimiter Kinesisanalyticsv2Application#record_row_delimiter}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters(
            record_column_delimiter=record_column_delimiter,
            record_row_delimiter=record_row_delimiter,
        )

        return typing.cast(None, jsii.invoke(self, "putCsvMappingParameters", [value]))

    @jsii.member(jsii_name="putJsonMappingParameters")
    def put_json_mapping_parameters(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#record_row_path Kinesisanalyticsv2Application#record_row_path}.
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters(
            record_row_path=record_row_path
        )

        return typing.cast(None, jsii.invoke(self, "putJsonMappingParameters", [value]))

    @jsii.member(jsii_name="resetCsvMappingParameters")
    def reset_csv_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvMappingParameters", []))

    @jsii.member(jsii_name="resetJsonMappingParameters")
    def reset_json_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonMappingParameters", []))

    @builtins.property
    @jsii.member(jsii_name="csvMappingParameters")
    def csv_mapping_parameters(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference, jsii.get(self, "csvMappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="jsonMappingParameters")
    def json_mapping_parameters(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference, jsii.get(self, "jsonMappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="csvMappingParametersInput")
    def csv_mapping_parameters_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters], jsii.get(self, "csvMappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonMappingParametersInput")
    def json_mapping_parameters_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters], jsii.get(self, "jsonMappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__028d5efb3d70bbdeaec4b0694088f3fe4822b9eb9807123d71126007992c4efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__299c0600dc21176563658891a60192161079669dbcfa483de1440683093f1e9d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMappingParameters")
    def put_mapping_parameters(
        self,
        *,
        csv_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
        json_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv_mapping_parameters: csv_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#csv_mapping_parameters Kinesisanalyticsv2Application#csv_mapping_parameters}
        :param json_mapping_parameters: json_mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#json_mapping_parameters Kinesisanalyticsv2Application#json_mapping_parameters}
        '''
        value = Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters(
            csv_mapping_parameters=csv_mapping_parameters,
            json_mapping_parameters=json_mapping_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putMappingParameters", [value]))

    @builtins.property
    @jsii.member(jsii_name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersOutputReference:
        return typing.cast(Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersOutputReference, jsii.get(self, "mappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="mappingParametersInput")
    def mapping_parameters_input(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters], jsii.get(self, "mappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatTypeInput")
    def record_format_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordFormatTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @record_format_type.setter
    def record_format_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b6eaef2e5ecdfde45947bf115061af00cbdc81bf37e95a9b904c30257207ad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordFormatType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__226c3cb6b471dba4dc45d1077e0a2daf794dd4b494d6e1b770f13f2cc868642e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource",
    jsii_struct_bases=[],
    name_mapping={"bucket_arn": "bucketArn", "file_key": "fileKey"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource:
    def __init__(self, *, bucket_arn: builtins.str, file_key: builtins.str) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#bucket_arn Kinesisanalyticsv2Application#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#file_key Kinesisanalyticsv2Application#file_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7515b6be834f68ac0fd18082f6080a79913d27299d20c1f31c031f9ee289ed48)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "file_key": file_key,
        }

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#bucket_arn Kinesisanalyticsv2Application#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#file_key Kinesisanalyticsv2Application#file_key}.'''
        result = self._values.get("file_key")
        assert result is not None, "Required property 'file_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0262afb2a3dad76c94223c14254b930d6c7572a6b7d6e8e30f4ac17cc78df892)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="fileKeyInput")
    def file_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__111f3fa1f72d9cebc716020d550c8eee6781695bb4d7b985b415881896ceacbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="fileKey")
    def file_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileKey"))

    @file_key.setter
    def file_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea20afbf4f3addbc75bb767472d61b9825af4ab0585774636dae44a3d2a437c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212dbb74ef1d2308e14ffa1c290e7b49d1950099172e468fe318e5fdd95d45fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#security_group_ids Kinesisanalyticsv2Application#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#subnet_ids Kinesisanalyticsv2Application#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5419cf8341c64e1ae7ea747c11df905b55c3f36edabc9965ef469d10b2b251)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#security_group_ids Kinesisanalyticsv2Application#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#subnet_ids Kinesisanalyticsv2Application#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aeb018050565d0d0d58c7ab721630da3b224eb244014d8288577aa1cf4faf0a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="vpcConfigurationId")
    def vpc_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c9f187bc9aac7fb5c412495d8635f5b8dadd1c858b9dc11fb1c73e83eafa5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae3ff6ec1ae51f19900430d5e8885052f7a0b468472a3f02e23e1918df244f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02394d3179c36fefa53845f03fa46590eb7cf093291cf98daa8c01e77cb1b2db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={"log_stream_arn": "logStreamArn"},
)
class Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions:
    def __init__(self, *, log_stream_arn: builtins.str) -> None:
        '''
        :param log_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#log_stream_arn Kinesisanalyticsv2Application#log_stream_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b00a1553756067e6fdde45c969c2db309a309ab281526b927080ebe09469ce68)
            check_type(argname="argument log_stream_arn", value=log_stream_arn, expected_type=type_hints["log_stream_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_stream_arn": log_stream_arn,
        }

    @builtins.property
    def log_stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#log_stream_arn Kinesisanalyticsv2Application#log_stream_arn}.'''
        result = self._values.get("log_stream_arn")
        assert result is not None, "Required property 'log_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__087ac8575709c0815af11aa2bc57c9369a68ff71794ed1b8ce3a46bc5d13934f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionId")
    def cloudwatch_logging_option_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLoggingOptionId"))

    @builtins.property
    @jsii.member(jsii_name="logStreamArnInput")
    def log_stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamArn")
    def log_stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamArn"))

    @log_stream_arn.setter
    def log_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfe8e40d085f6ba8318363d2627597d621001ea68e7e402951e40d54a3a4cc5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e3228021e2f459ba9d348853ab7048019c1791deaa0e25e332719f422bc1593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationConfig",
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
        "runtime_environment": "runtimeEnvironment",
        "service_execution_role": "serviceExecutionRole",
        "application_configuration": "applicationConfiguration",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "description": "description",
        "force_stop": "forceStop",
        "id": "id",
        "start_application": "startApplication",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class Kinesisanalyticsv2ApplicationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        runtime_environment: builtins.str,
        service_execution_role: builtins.str,
        application_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        force_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["Kinesisanalyticsv2ApplicationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.
        :param runtime_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#runtime_environment Kinesisanalyticsv2Application#runtime_environment}.
        :param service_execution_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#service_execution_role Kinesisanalyticsv2Application#service_execution_role}.
        :param application_configuration: application_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_configuration Kinesisanalyticsv2Application#application_configuration}
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#cloudwatch_logging_options Kinesisanalyticsv2Application#cloudwatch_logging_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#description Kinesisanalyticsv2Application#description}.
        :param force_stop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#force_stop Kinesisanalyticsv2Application#force_stop}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#id Kinesisanalyticsv2Application#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#start_application Kinesisanalyticsv2Application#start_application}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#tags Kinesisanalyticsv2Application#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#tags_all Kinesisanalyticsv2Application#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#timeouts Kinesisanalyticsv2Application#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(application_configuration, dict):
            application_configuration = Kinesisanalyticsv2ApplicationApplicationConfiguration(**application_configuration)
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(timeouts, dict):
            timeouts = Kinesisanalyticsv2ApplicationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c17f89ceb8e18cd88d9067549ce193d9e411c5330f72a9359fa20c993b30f9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_environment", value=runtime_environment, expected_type=type_hints["runtime_environment"])
            check_type(argname="argument service_execution_role", value=service_execution_role, expected_type=type_hints["service_execution_role"])
            check_type(argname="argument application_configuration", value=application_configuration, expected_type=type_hints["application_configuration"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument force_stop", value=force_stop, expected_type=type_hints["force_stop"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument start_application", value=start_application, expected_type=type_hints["start_application"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "runtime_environment": runtime_environment,
            "service_execution_role": service_execution_role,
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
        if application_configuration is not None:
            self._values["application_configuration"] = application_configuration
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if description is not None:
            self._values["description"] = description
        if force_stop is not None:
            self._values["force_stop"] = force_stop
        if id is not None:
            self._values["id"] = id
        if start_application is not None:
            self._values["start_application"] = start_application
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#name Kinesisanalyticsv2Application#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_environment(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#runtime_environment Kinesisanalyticsv2Application#runtime_environment}.'''
        result = self._values.get("runtime_environment")
        assert result is not None, "Required property 'runtime_environment' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_execution_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#service_execution_role Kinesisanalyticsv2Application#service_execution_role}.'''
        result = self._values.get("service_execution_role")
        assert result is not None, "Required property 'service_execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_configuration(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfiguration]:
        '''application_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#application_configuration Kinesisanalyticsv2Application#application_configuration}
        '''
        result = self._values.get("application_configuration")
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfiguration], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#cloudwatch_logging_options Kinesisanalyticsv2Application#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#description Kinesisanalyticsv2Application#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_stop(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#force_stop Kinesisanalyticsv2Application#force_stop}.'''
        result = self._values.get("force_stop")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#id Kinesisanalyticsv2Application#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_application(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#start_application Kinesisanalyticsv2Application#start_application}.'''
        result = self._values.get("start_application")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#tags Kinesisanalyticsv2Application#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#tags_all Kinesisanalyticsv2Application#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["Kinesisanalyticsv2ApplicationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#timeouts Kinesisanalyticsv2Application#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["Kinesisanalyticsv2ApplicationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class Kinesisanalyticsv2ApplicationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#create Kinesisanalyticsv2Application#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#delete Kinesisanalyticsv2Application#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#update Kinesisanalyticsv2Application#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9422d33541edc2e5fea837d28dcc778874a8a28d75f60a679db0942d2fad267d)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#create Kinesisanalyticsv2Application#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#delete Kinesisanalyticsv2Application#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesisanalyticsv2_application#update Kinesisanalyticsv2Application#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Kinesisanalyticsv2ApplicationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Kinesisanalyticsv2ApplicationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisanalyticsv2Application.Kinesisanalyticsv2ApplicationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b994af8121199e20d3c512cf3439be8752ab117078d02ef6d7bef59d1827200c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b125ed218558a7c69282f8a96e17b4b07f030829f51559506471d53132fe0923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24e0051e76f336b9cf88a8eb02620b4d411c176b30bb8dbca3c14881c0bbad84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ced18b344518d258c357e20d7881e53def20b92ebcf74da18e998a9066c8426)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__407df4353ca7dddb9c8acb76354962c8c45c4042078a03f3c053c46ad5dfb9f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Kinesisanalyticsv2Application",
    "Kinesisanalyticsv2ApplicationApplicationConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupList",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnList",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationList",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputList",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnList",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceOutputReference",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration",
    "Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfigurationOutputReference",
    "Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions",
    "Kinesisanalyticsv2ApplicationCloudwatchLoggingOptionsOutputReference",
    "Kinesisanalyticsv2ApplicationConfig",
    "Kinesisanalyticsv2ApplicationTimeouts",
    "Kinesisanalyticsv2ApplicationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__d0870f192d7cef34dc96461fd8ff0c67267418d1e0a33296a2f88c93ab7d52ee(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    runtime_environment: builtins.str,
    service_execution_role: builtins.str,
    application_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    force_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7c45eddcd34c06cb9e721d6b0a10a15f82257adba6b726db20aadeaccdfe8667(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ddaa350f906d65c0c5cc8c42afa9825f554219d1fe74af63f4de0f2fcc506bb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643e4bf26f1302814c1d6b166efb36c0260d49232375fd99790c0415e6052aa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f6fc32afd0a65d06749f3fe2e4e376ca77ff51a0ca913dfa25ba14dc11d65f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b17dc1ac59f1d027019fd7ea25f5a120473745997f75a42f6802d217aad061b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ac653204b6a9609442086beeaaf4b53908e85d319efb0cb51a4eeb4899cfcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81cf65fd961c9ebb0f23db4841d709e53bac2e0e8a8ecc934a0bf0f47754ed2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc874a51e319affbcc09dcb8778ceb7d169fff3dfc864f9337511296811183f2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22829825060fad7a5fe36f07b933b6064b342234b2d26c8b9c2c9c69dac9b39e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1244ae7dc7cafa8442553419fe54fe8e2c7f35c192358c1b4e80ce29cd5e10a(
    *,
    application_code_configuration: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration, typing.Dict[builtins.str, typing.Any]],
    application_snapshot_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    environment_properties: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    flink_application_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    run_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    sql_application_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856dbbe332623ea922d11629d9cdda202a470d126ebfab62b749eebec46fcd15(
    *,
    code_content_type: builtins.str,
    code_content: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d72dc6cab15c6ac2b666f1a93a8a8ca157741f9dfa67cac2b640cdebc8f281(
    *,
    s3_content_location: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    text_content: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99665185775e7ec78eabe3c406f72a940666a85b9db840407e9a7c10a3009549(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b352266c694105cf51a0d2e6d8ea16200e5f8a4a62ade2ac3fc3edb2920dbad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4b964dea0243efc8701198b19ad25cabaf57eb0c0c02e4dcbe68e9ff6cb5ee(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContent],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c15b86ffde5f13ac2e4138e9fbb33bcb88fbcd0a48e6525696e64da5b77f96f(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d89f999e0cee37ce2fe5d8b01e37b0730d916edc62807b624adcd4af4a9c568d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d930528cae1d78837dc8bf522766987192a4b42d1de69ca3071a966904914c05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db6f8d4070794ab051a68395b923b5fcea7cfa524e1ae1bc6b8386cb6c3df35c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43dceab61353d7767863bd0516f290f003e2b450a91c36cd0f3401d533980b22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df634c70a6d8cf476b42c54c606531060348b55a4f8ac86d47cd909c17c4b1c2(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__747969dccec9bf3a0b70d09d5c2a5c1749b0713690b1c1f163cbefdcc627762c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05512ababfb27f8cbe5c15e6ff2489f8efc3db4df68b976ad25b52d330bf43e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd0fc8794af3b1f41dab141fb4e46e0c6cdd1d9d590c934a10e207d4f95ccb2(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationCodeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915df0e2c75a07fc98e5c325b5a423c294a86d8119e6cc23d4fffab7747dd3d3(
    *,
    snapshots_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c374f0f7ebeb915ecb61b1163928a3b037ca792b41fdb835329fd1e6a802dd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a83b8c0a2c2e845f15d75952a8f5a22a26a94e994da4b1151c50a52ed7218d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50cd77439c3561fa2fda8ad5bc06fa1ff3794caa16471942f3e6664c3867b478(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationApplicationSnapshotConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd333262a72dca0196a1a34094cfb67d8eb7ab10c242e4f131515b78736f860(
    *,
    property_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703a367a8588136beac97633d449724a9e35a277b31eea17cee33976c0a95a5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdc37901fc8022f51a71e77ed754cd32019a863543e3df5a471724f2f0a89acc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af1bc20f6d4a4c12daa6ce56584310b0ddce2af930d89447540e5083fd9346e2(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702fc9d67a06a9505f20d25c85d393c1846b114dab7265a886edf3046bf945db(
    *,
    property_group_id: builtins.str,
    property_map: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e4f98675f510f13d7241a85c472c7ed301a54d01cb294e634ad7ce17609300(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__672060e1158aca1f8175149fa4f2e376021ae28e96a70f9e9012a4c7a9b4f028(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6ea35506896b0dd9332808df6c30ce60bbb092b78942fcef2bf94ae2d9aa238(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a09fbd84252d94d38c61f0aef1a9f90b58af11492cbfee8b04dadb35250c1f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f929cf681781857e899e394da88eaf85539e70140e9736a15e545fec4640da(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb28d72aa0560bb1f1759c11f221789df0a7ac6c90d169661eeecf6c37b0670(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0f23bed97c879dc485fcd77aeef094250cde174ec90527c881e271ad29409a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb32dbffa589317101a00af72d66b63b539504a25ecf5f5485f6f6c053cd4d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceed5b8201cc1d6a778e521490f3fce59adf6e2adf41a38155a0174365bbb5cf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3c4aa97730b67da2d88c8e27f57543925eaf0bb6a5f3195f98729336eb5f74(
    value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroup, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc5d5ca6841984b6e7adc225495bb75da811adb7f8db81506e42ff85705d83e(
    *,
    checkpoint_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    parallelism_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8166e95c99614c7212dba6d08bd124a6d48706910901563c08f460a1217f7ac(
    *,
    configuration_type: builtins.str,
    checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    checkpoint_interval: typing.Optional[jsii.Number] = None,
    min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b037192718f0be908925302082edc74892044dedfabb2de8ddc7db81f587c63f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5f79b0e7e018399cbca9f59ec4173f4377fa831732b1c3f3dca0cf4e3aa612(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c165704181397ed5da5101a1f716d0ad2d76a48bf04340f4987de296598616(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__247a43965d90669c98a026ec69de021d682773b378d41694472a7476ee9b036e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07313dd85af569c797e2919cc82e950a2097f30391955fd40e9f0a1157e456f4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e271760dd1f828e54bc6c0939a768dc75dc3a7c23a77804b5b882d5dbbdd26(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b20132283c684756f5a66533885dc185b9d68c3b5f4b30070eec145667c639(
    *,
    configuration_type: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
    metrics_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9dc31e0fd04b9f95661b470a1964b0189ddd303b7b2c9665fc0b06cc75849f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a05e5aae223361eca1bb2aeb282c80695173cef4dacbf1ee8f758c5d982f2dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19add5df3d4d8bf36c2e656602d7062bda9bf2a58f0bd86fcf976140669273d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665f3ceeedb7d954f0113d26fa888c11e4fa197ef99790c08210d34a8262b3e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eecee5ce4715178b1493aaa7278e5c6ce7f866f01fd84cdabdbbb8cfc9de89e7(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2023925952fe73f537f44f40be44f7372f06d10e65952829cf85b122a27f86ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8c3d7b66352e9e5199549e07b26c22ea221d9049cd02f0dd437353895355aa9(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a79e76e324a9efba2e9f3f41f6a15f6c7a0e3c0e90dbb2b99f651a99b9ab35d(
    *,
    configuration_type: builtins.str,
    auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parallelism: typing.Optional[jsii.Number] = None,
    parallelism_per_kpu: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da26c2884c01d34feccf66afb99c87a37fa65470468101686a552933e2f7b7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3905231735dad3b72816908260070eafbee381cb8af6c990089470aac724668e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589e2ddcea7376a84f46c98ccefd34d6f1bec5230b390ff43f260b23e578f64a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42cf774bcd7f89fe65f24244380991bc228aa6a4da6f831a9a66e60698a428fb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0393a44b25c1bf53c26ea075f55a4c5d417852db1434bcd5d67cb9f8fbf7b7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d3da2b25521df6af33267cf68e4a2ba0d6a4062ce8978f68ba0ccd1a12d4f9(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bfeacddbc525fe998fd486ee0da4b974bbc851fed527c0a3ad34d562f648d62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fed13a1e4bb9f375c129069e6f5473c17c748f7798dca65b2a42c5dad8bb38(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__719852cc4d7e5048b5a908827847f01a08639b592424cbbd91b08a8f589294b0(
    *,
    application_restore_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    flink_run_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5349584eb117c417baf3676c660a66ea9a99cbad3bd99dfddd4b8f94067e6b00(
    *,
    application_restore_type: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d751201480ccf95acf1aaf2cb353d6cd4acd10d463eb9480a3d477ecb271ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72b665a73e5a1bdecbf0fd8d565c18549337e5d7337e376632e9c9315bce4af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e12e14fbd6e9e377d16ca2eee70aeadb7d120ecc6b14a060596741576acb48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6431beba99b89d4f1b8bade38b75397e8aec0844d6c0f299beaff279556ff058(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47836cca49a2d0d472d6dc5948c16a240e17fe3058d9f26eb50860b950744af5(
    *,
    allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1ee689559590cff1a7076d52a1fdbf8e7f590cf8ce646b16c6a9e7a5074e43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17bd967440038fd656299b401db52fd72c740d804c47ea48b5857d4861bca709(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c91f7d6834ebe1fec46b79262061d18de3a6081db213a6eb9f1fe082c8998a(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfigurationFlinkRunConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef0c232e512d892172479dae5370838ca3efa4b2fd6a9e2db936e829575af700(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee3af73a7df9b6f2305740de8c50801871ac0b1b8d7a4f5f74c3358e06bf1eab(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationRunConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5cecd57323f898bf8925ff40596630ed85378bd9bbc5b86c5125eb0c3a09f18(
    *,
    input: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput, typing.Dict[builtins.str, typing.Any]]] = None,
    output: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, typing.Dict[builtins.str, typing.Any]]]]] = None,
    reference_data_source: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f80f578df5c9c2be7ebdf29672a020f1bc69d9c3db28c61a2f46cdbfa218f1e(
    *,
    input_schema: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema, typing.Dict[builtins.str, typing.Any]],
    name_prefix: builtins.str,
    input_parallelism: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism, typing.Dict[builtins.str, typing.Any]]] = None,
    input_processing_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    input_starting_position_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kinesis_firehose_input: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_streams_input: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c9d36ea3768684254efbe12580ce0e62e0f7f374acfbea3bd5d3be281a429b(
    *,
    count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7acab5ff47f48da384e3df2e99e593dbf759109eacd97f1398993c583a5898(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b1872426891bf23838564eb779a36e0df02aa4906b6a33a91ff4a5edacd610(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c36de2f36079a1ed847d9e8776aee4a742f7ea2e6e18861b45ff2c680f266122(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelism],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa0c3b80958f98e51e24898dca49266d2347e4fd8d1d1ecd5f981c8d94cbaea(
    *,
    input_lambda_processor: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197cfdfbb99c8db2f77d185c92b2e2e3143c3b29d12b877fdc2396eaaa5364c7(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097fe161792da064990bf7ae9890cc2a3391684458fada7b542a38709d613fa9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83dac9e0059c954e895fbfcf04a1f17bfb336fc9e922df0c56076571d39138e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f67136e023d888ea30b4d3e4d25372a03a2c32bd911031853fc5403bd0dcf521(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessor],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3adba17746a8b3719c4b6002c40e32f5ca515da69aa5cefade00f7fd2e67ea1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f95b37339b92d3b822a6fea5b634f0b726141638a30aa1abfa85056a3ffeeb(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c982d2bb6ef3892d100a7e0496c66ac279e32477433f53acecbeb8c0d3603eb0(
    *,
    record_column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, typing.Dict[builtins.str, typing.Any]]]],
    record_format: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat, typing.Dict[builtins.str, typing.Any]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdcb2bc5181c431330f3e3b0fd7b7aa0314a57af5c2bbdca28df214cfeacdd10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e754b823676f2a517638ea385334f835e61c4e38d1fe75763f4853877fd607c8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa95b419397c637412c52306cbf95cdd6ba63c82173e91b4a400c552c8d9099b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44cabe0542504722cb7e109c071a847bfb22eee32b8fc668c690e74756777abd(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb20fcbd17b8bc92692a6122cb46967ab2a311fc4909c0bf8c4cb0d31f8eb37(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00b9fec3d62a76c267f1381302431c6bb182fd22102ff68a7abe117d5327d89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e36c21444eed123390334bc87e6ee023ab98cee7008548f8f7c9a083b64af39(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5b5c9cfe3bc5463b74b2c72ba7c9ce5e67da1e70528f5d321e54ffbfd6e1ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__184b77fa82e754f77c38eb797bc28b4b6a7df00de56ea0a32fb53d0b169e66ff(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73d165c02f739ae31badbe61edbcbd48f0a2111fdde6634c1ebb685c7dde74a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5bc4b679c97c95710ced577fd6372e3d6b960d07874d1f68567857078b8737(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e150c74cf8551bb04dda521256ada4eafce269574244c68271921454f2c4856(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b21d89cc1804e47f20fc163d54eb28a06f30069d79f333daca15235bf939211(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bbef5b916a656f8a93058b2517602c75142cf45017ac704f000921072dafeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__866cab9939af722c8bb39329952f82b9e52579ab90f29b8981bb3aab776b67e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b62f681342e62a7c0e96fd628109b1aca137f192f295997746fe381bbc77fde(
    value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c4a3a0b5baa59bf5ebf0d8401ee3efbfe803e2ca0479264f8cb90a3a910a69d(
    *,
    mapping_parameters: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters, typing.Dict[builtins.str, typing.Any]],
    record_format_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ecef25810511585f325126a2ce7d976f8ce263ec3693cb57ae807edeadade3e(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfc6d209b8d7aee41a215db6f2b68a64bda6d63103a5801af5591628fbc302aa(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbf03d4d19faca062397b2e1f4c7671713ef27657ffbb913024bb81c9b102850(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70bce5a249d2313df669ec0994e83b26cedee74bc22c766ae6c2011c31ea266a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d088639fd01ed9259c54da4d671bd66c510e3ceba54977c890341471bff2ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b49e163bc9b05722f4f181fc12436722a59e9c7a7001b31f546dc4067b1f955(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af59f43165b148519b784b9227c112b4921371c4aa47190cb641d97a5e4e59e8(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c7dbd547f4d561fa66da73c6219fc826f9c9fd43cde02d51b48676111238ad8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928b30788750684d7c4a78b81cca79f5290b334c66fbd1adc34cbbfde53801ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55bc0e49c1e6a0de10abf17a92a4ffed6f1452ec89ec9ad5bda973fcb78ad690(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feddb4b6e96ee0693f8d1f49f99af53bd0844d961f9969ed10fea50448db3c4a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86354b28d10bb954f5512a36235682d2bce82a3d386a81e7b602310611188000(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4e6118ea1541edade3cb1aa617bb5b7ea53397d8aaf98f6c91ee48c95d2d82(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8029513dc5c15128885125c948ac2ac1cbf484b507a92d15ba361f64db4f5189(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb157d3ef21a96833b0997119d6558603593e8d4be568b2f48606ac9e100d4aa(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15422c5702a970622cf31f2e1ff82be99e35729b79d4ed05d5baa3a44cc66aa5(
    *,
    input_starting_position: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00fcff032d35f00cb2006b8705287c9d8eb8896793049b5aecf72fcbb152180d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77001cb8cee83d6cea7d0d3dacdfdccb615fac722349bcdd31f60eac912af1de(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12dd12b67a00ee460f49b31c693455be263fbbb4929b755f61fb667305aa8d12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7bd1c9f426528694204da790430f07aa628d0bdf0511cafd912620171574e80(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f18e05f3d82fe215a71fc6daa547da6dbb403ef0ce88de35aa30febed6f87e4d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb7fe4591b88d50632e51ffee765fdeeed504e13e41fd2f8104c375e82bc06f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86cb19d7a5eff26c72e68389ffb73b0be4668cf456338843ba7213cdc97cfb5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5612ff68b5fabfca310702233c28d2c960d243d485e8f7e32629c742f3b954bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6373dbaf70a7dbddaddf4c7a0c783f53affb6a43fc7bcc1b266772a647d32084(
    value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1742dbe1a289b0e094c8c88063d72dc9dd8a9f3d67cbd65f1dd98d80de6c5dce(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a50d08f71abd80537fa2977841c89dead99ee7467b53a7fc13b308634c2354d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af400bade83b740b6fc1bd028485969e747fd611da09f970f864ff8e6a75091d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f6a03d03580794e170c7de3a96712dc933e40007d01012c7f6d81e8200c7d8(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c929e6d35a2c9638dcc5af7c0ec6b56364e61cce43fc65514621feb470f57ed(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0746241dd6bbc4e7c37c583ea917ca13134b6980bcec8840d8cd16ee45b089b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec5783102f58aca8f361f77072b70120f5571fa25637906a440f5971f614ed0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f995b65c8e339e555284b00db7bcce6b3c3a6ad6dd7180fef95d3db3a930be77(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fa232a259895087a6e7d78b44852a3a46330f46e59473a880220aab9f1b654e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bb534d9f38523a35b5b5ebf06f7866523855d93f6d42ca75b5b6122f431c8a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c9aac53550f8bea35a0e5e282fb225008886c6199a55fc0cdad2b9bfe2b81be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cca5de6a383e476182a2c5c520a468bc6aafe6296e56724ee11218f08fa0c5c(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationInput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56589e745c082b9d1234375257c9119a62742a669aa0849d7e720eb12b0ec08a(
    *,
    destination_schema: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    kinesis_firehose_output: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_streams_output: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_output: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504968930b1ff55ec17a7142b122072c643ac30745fc00b180fc9da15e01d848(
    *,
    record_format_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0163c7653e787b159d118695e4168d5b0c3f99271bbdb516a1b7fdbca43a7ae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3e0bb159fb290156b10a1a355bc0edc356a5d740d28582d5318404d1c19e7d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60dd700daa80113e4202c447c86e46c234fe70082b04c7c7289b3064272d6919(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23c338d489dc9a79d1fcfb011c179da83a3dca8cbc194cf1db01b9e393af9da(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4afc51bebcdc0c50e7eb155d74436363f7f72671b35fb0866e80fa393905a24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42957d7f2f99692f7f941712fe074cf9118412f21665822bada8972262c3bcde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c9d9fd3927f9abe4b346f07a9fd30eed383122219842cede7cf425f56de840(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c467999e3b3d39e383228caf490a68d8731ffd95ffcfe4b4542f9b02452379(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2eea63d079e080ed3a0fc0e62d31c509563cda3892d21c4ea3029eeceda34e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be8306cfde4b0dab2a432cac7b6ae21e7b00d2b4a27c9281ca027b4dfd33038(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6366ba2be9b1b203d652121b1c31f58d78b86fd659f50b0410aee00722cd5c5(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14390f607f7b5ac3706fbf470a118b087954258b5ec97b238feee0482cbe8282(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7360a9efed79fda760f2273ecb75cfce6f7154d3ca7e188c0dd05d6820661412(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aa48bdb47fbdb5346f92b9763e4ba96f37f8485bef026268973f40b5ee26ea4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aabb7c62846c2225c1fb30ccef5b49fb9c795396ba5a490a7130ea3abf1f54d(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a5afeb905daaf6620bced1faf3cf40bac82fdd311ba0eca973bffd391aad35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e438533cbf7e08d161ea1012dc3f1bc1b93a59169fdf4c1b64bc24272dd99a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320fc79095549f0d4f0cfcf0b6da113660a9ca6c0e1cf2fb00fdc918a68d6a38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b20e05ed8aae13649093ad43835d2359608dd88e83d632702d9def9b066d84c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404b8dd10e050089fbb4fc869f15f9b348b0ceeda446967e501e592588932045(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106e67d188a1102a324f7de90e1eb625a6c7c6eb5d9a36433ca96e0ce971dd06(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813d3e0bbcf134210d8c3589170e9af3aa60f8c5d5ae7205ca583386850b1d9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8af56bd3c8cafb44103b418f144144ffaf71934a13386ed50e91598153349d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee720bb5f7ea6a934971264c19d0eba896736c100e2e63bea6a530636eda39fe(
    value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64d0990ed211b4663a6adb82918f8bdb0e6a2354d61becba2e4a9fe288a6eb7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b8c2599434ca3a62fff6ef6fa4adb4344baa36bb317e82d5a9e96593da436d5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationOutput, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5631fd3a105932ca578f3a569266d75db9c926543dc65b5cc1937e3895136d4b(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ffff9c3b1bb3cf45c38f3325c4181bd58cb81018ad3b4e7013e7d62941fac6(
    *,
    reference_schema: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema, typing.Dict[builtins.str, typing.Any]],
    s3_reference_data_source: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource, typing.Dict[builtins.str, typing.Any]],
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5d4fa0b7289b66ba1562b63a47f583b333761f941bc82d5a2e62e8dc27bf73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c496970f276f3b0719eb6b7970d5c856d816a204ba88bcbc2ff45d6dc32a31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd2d4b58a19380df96af183b93145cc722b251feff78993047d898f064acf82f(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c525d2b462efe1c4d6d8c21f117dbd8553c4cf134e4f4edd25bec667481cfb(
    *,
    record_column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn, typing.Dict[builtins.str, typing.Any]]]],
    record_format: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat, typing.Dict[builtins.str, typing.Any]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29281b993dc5c7fb9d3585b9a64ac9dd15d3dafc717154dbcab80da935ca6cab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd704d573aba9b05475b7ee2a086f3c88eec0a86fb4de7682c9ddcdbebd2b633(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42dbb7fe7aab1dc109718ec586c16fe201e240c472b172a8275629f75416894e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a4e04d97dab97249e150d878d87bae96cb3614fe9e32d41d1307a09327c6d99(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bddcf7aa72a1e793d05829a4aac2dffe29dc0851293fdca33d0dd40086df9bc2(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47c5f8cf357c52e984f34fa10eb40047e39ecf7d796074dd1b3c251cde4180e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe47e4e6812d9f89d6e334b6e800556f067e990a8e94eb757bd06cbafce65db(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c181383f214b96f62fc1376942eb99f491d5d8c407034c86f130e325118c13d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f5f851d68c838732583e9056c3855399dcbd3712eda14f59a45cc14e030d3b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b9d837017e0d4a60db73cb686c061a4c96466972b066a76769fa5ebb7abd9c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846819791b231cd564ac0480d88c12e64795d7943dd2ab0505cd68e50aeaa9de(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88319626bc96c544dce3eff79f5a6fed9dd7267d6471a448cf492602034fe2c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9777c6d049da5c5e9373071625bdb1589c291348a3962e6f025696f5a0cae867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913c9811d5c1730101e96c85c7c45cdaefcc06ee8c3891be5fa8f3a648c15952(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f9853a7d324a5e998fe8459d345a34db4d39701797ac0bc5b86eb53979474bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40456da42a1dcd5990acf0baee2f17b94a7a0a6332530e6b01decf40305ca999(
    value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumn, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f25eecdb46764a4b647c52af136be47b1e469eccaade3c45d4fda2edd254971(
    *,
    mapping_parameters: typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters, typing.Dict[builtins.str, typing.Any]],
    record_format_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a2d737b9d09fc05c90ae6467a5c733b79702ce3864e7ef8385605582f8914a(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4eef6591ab2e9de801dbcf7c1e6d6de65d3f9ce203f5979badcfcd09fbed47a(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06849414bb953268fddfcde0269bdc146f633835169c6f38f25734a722896cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62e5151c2ec1f3d9957ab3ded090380d3731f554c7145022fd783b21ac940f56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb66465a0b3d142d9e1d4f0a0d2f63023640fc129ef5637f39de76baabf6011(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ba65990d84aff4aa1fa23082876e55dd1f42af629dcba5c0333a9979ebe8ab(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a01f217f48bdf023f4eb607124819a4725cee1092c57409038a04c17b67a60e(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a0aca83b2b32c89904119aeca6802e59170a37b06f08f2f21b804b628853f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286c497e4f28a2e6926d83a0c51e03cc99d9e22535bd0e497b594670dd1f198e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d758c80e2a1a423dc564ec119fb4d74b9b93b63e8bcb747816e075fc295b6b(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad966332960c222d00cf18448818408b07d105aab8a1183578b4a83332291a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028d5efb3d70bbdeaec4b0694088f3fe4822b9eb9807123d71126007992c4efb(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299c0600dc21176563658891a60192161079669dbcfa483de1440683093f1e9d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b6eaef2e5ecdfde45947bf115061af00cbdc81bf37e95a9b904c30257207ad7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226c3cb6b471dba4dc45d1077e0a2daf794dd4b494d6e1b770f13f2cc868642e(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7515b6be834f68ac0fd18082f6080a79913d27299d20c1f31c031f9ee289ed48(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0262afb2a3dad76c94223c14254b930d6c7572a6b7d6e8e30f4ac17cc78df892(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111f3fa1f72d9cebc716020d550c8eee6781695bb4d7b985b415881896ceacbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea20afbf4f3addbc75bb767472d61b9825af4ab0585774636dae44a3d2a437c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212dbb74ef1d2308e14ffa1c290e7b49d1950099172e468fe318e5fdd95d45fa(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5419cf8341c64e1ae7ea747c11df905b55c3f36edabc9965ef469d10b2b251(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb018050565d0d0d58c7ab721630da3b224eb244014d8288577aa1cf4faf0a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c9f187bc9aac7fb5c412495d8635f5b8dadd1c858b9dc11fb1c73e83eafa5f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae3ff6ec1ae51f19900430d5e8885052f7a0b468472a3f02e23e1918df244f3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02394d3179c36fefa53845f03fa46590eb7cf093291cf98daa8c01e77cb1b2db(
    value: typing.Optional[Kinesisanalyticsv2ApplicationApplicationConfigurationVpcConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b00a1553756067e6fdde45c969c2db309a309ab281526b927080ebe09469ce68(
    *,
    log_stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087ac8575709c0815af11aa2bc57c9369a68ff71794ed1b8ce3a46bc5d13934f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfe8e40d085f6ba8318363d2627597d621001ea68e7e402951e40d54a3a4cc5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e3228021e2f459ba9d348853ab7048019c1791deaa0e25e332719f422bc1593(
    value: typing.Optional[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c17f89ceb8e18cd88d9067549ce193d9e411c5330f72a9359fa20c993b30f9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    runtime_environment: builtins.str,
    service_execution_role: builtins.str,
    application_configuration: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationApplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    force_stop: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9422d33541edc2e5fea837d28dcc778874a8a28d75f60a679db0942d2fad267d(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b994af8121199e20d3c512cf3439be8752ab117078d02ef6d7bef59d1827200c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b125ed218558a7c69282f8a96e17b4b07f030829f51559506471d53132fe0923(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e0051e76f336b9cf88a8eb02620b4d411c176b30bb8dbca3c14881c0bbad84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ced18b344518d258c357e20d7881e53def20b92ebcf74da18e998a9066c8426(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407df4353ca7dddb9c8acb76354962c8c45c4042078a03f3c053c46ad5dfb9f3(
    value: typing.Optional[typing.Union[Kinesisanalyticsv2ApplicationTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
