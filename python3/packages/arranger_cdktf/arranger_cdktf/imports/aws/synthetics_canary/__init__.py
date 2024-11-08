'''
# `aws_synthetics_canary`

Refer to the Terraform Registory for docs: [`aws_synthetics_canary`](https://www.terraform.io/docs/providers/aws/r/synthetics_canary).
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


class SyntheticsCanary(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanary",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary aws_synthetics_canary}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        artifact_s3_location: builtins.str,
        execution_role_arn: builtins.str,
        handler: builtins.str,
        name: builtins.str,
        runtime_version: builtins.str,
        schedule: typing.Union["SyntheticsCanarySchedule", typing.Dict[builtins.str, typing.Any]],
        artifact_config: typing.Optional[typing.Union["SyntheticsCanaryArtifactConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        delete_lambda: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        failure_retention_period: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        run_config: typing.Optional[typing.Union["SyntheticsCanaryRunConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket: typing.Optional[builtins.str] = None,
        s3_key: typing.Optional[builtins.str] = None,
        s3_version: typing.Optional[builtins.str] = None,
        start_canary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        success_retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["SyntheticsCanaryVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        zip_file: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary aws_synthetics_canary} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param artifact_s3_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#artifact_s3_location SyntheticsCanary#artifact_s3_location}.
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#execution_role_arn SyntheticsCanary#execution_role_arn}.
        :param handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#handler SyntheticsCanary#handler}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#name SyntheticsCanary#name}.
        :param runtime_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#runtime_version SyntheticsCanary#runtime_version}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#schedule SyntheticsCanary#schedule}
        :param artifact_config: artifact_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#artifact_config SyntheticsCanary#artifact_config}
        :param delete_lambda: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#delete_lambda SyntheticsCanary#delete_lambda}.
        :param failure_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#failure_retention_period SyntheticsCanary#failure_retention_period}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#id SyntheticsCanary#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param run_config: run_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#run_config SyntheticsCanary#run_config}
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_bucket SyntheticsCanary#s3_bucket}.
        :param s3_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_key SyntheticsCanary#s3_key}.
        :param s3_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_version SyntheticsCanary#s3_version}.
        :param start_canary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#start_canary SyntheticsCanary#start_canary}.
        :param success_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#success_retention_period SyntheticsCanary#success_retention_period}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#tags SyntheticsCanary#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#tags_all SyntheticsCanary#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#vpc_config SyntheticsCanary#vpc_config}
        :param zip_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#zip_file SyntheticsCanary#zip_file}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae2737e406f92a5fc740604b01a6735c0ff11532c4dc64f6be9f1dd8168ffad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SyntheticsCanaryConfig(
            artifact_s3_location=artifact_s3_location,
            execution_role_arn=execution_role_arn,
            handler=handler,
            name=name,
            runtime_version=runtime_version,
            schedule=schedule,
            artifact_config=artifact_config,
            delete_lambda=delete_lambda,
            failure_retention_period=failure_retention_period,
            id=id,
            run_config=run_config,
            s3_bucket=s3_bucket,
            s3_key=s3_key,
            s3_version=s3_version,
            start_canary=start_canary,
            success_retention_period=success_retention_period,
            tags=tags,
            tags_all=tags_all,
            vpc_config=vpc_config,
            zip_file=zip_file,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putArtifactConfig")
    def put_artifact_config(
        self,
        *,
        s3_encryption: typing.Optional[typing.Union["SyntheticsCanaryArtifactConfigS3Encryption", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_encryption: s3_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_encryption SyntheticsCanary#s3_encryption}
        '''
        value = SyntheticsCanaryArtifactConfig(s3_encryption=s3_encryption)

        return typing.cast(None, jsii.invoke(self, "putArtifactConfig", [value]))

    @jsii.member(jsii_name="putRunConfig")
    def put_run_config(
        self,
        *,
        active_tracing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory_in_mb: typing.Optional[jsii.Number] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param active_tracing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#active_tracing SyntheticsCanary#active_tracing}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#environment_variables SyntheticsCanary#environment_variables}.
        :param memory_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#memory_in_mb SyntheticsCanary#memory_in_mb}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#timeout_in_seconds SyntheticsCanary#timeout_in_seconds}.
        '''
        value = SyntheticsCanaryRunConfig(
            active_tracing=active_tracing,
            environment_variables=environment_variables,
            memory_in_mb=memory_in_mb,
            timeout_in_seconds=timeout_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putRunConfig", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        expression: builtins.str,
        duration_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#expression SyntheticsCanary#expression}.
        :param duration_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#duration_in_seconds SyntheticsCanary#duration_in_seconds}.
        '''
        value = SyntheticsCanarySchedule(
            expression=expression, duration_in_seconds=duration_in_seconds
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#security_group_ids SyntheticsCanary#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#subnet_ids SyntheticsCanary#subnet_ids}.
        '''
        value = SyntheticsCanaryVpcConfig(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetArtifactConfig")
    def reset_artifact_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactConfig", []))

    @jsii.member(jsii_name="resetDeleteLambda")
    def reset_delete_lambda(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteLambda", []))

    @jsii.member(jsii_name="resetFailureRetentionPeriod")
    def reset_failure_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureRetentionPeriod", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRunConfig")
    def reset_run_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunConfig", []))

    @jsii.member(jsii_name="resetS3Bucket")
    def reset_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Bucket", []))

    @jsii.member(jsii_name="resetS3Key")
    def reset_s3_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Key", []))

    @jsii.member(jsii_name="resetS3Version")
    def reset_s3_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Version", []))

    @jsii.member(jsii_name="resetStartCanary")
    def reset_start_canary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartCanary", []))

    @jsii.member(jsii_name="resetSuccessRetentionPeriod")
    def reset_success_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessRetentionPeriod", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

    @jsii.member(jsii_name="resetZipFile")
    def reset_zip_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipFile", []))

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
    @jsii.member(jsii_name="artifactConfig")
    def artifact_config(self) -> "SyntheticsCanaryArtifactConfigOutputReference":
        return typing.cast("SyntheticsCanaryArtifactConfigOutputReference", jsii.get(self, "artifactConfig"))

    @builtins.property
    @jsii.member(jsii_name="engineArn")
    def engine_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineArn"))

    @builtins.property
    @jsii.member(jsii_name="runConfig")
    def run_config(self) -> "SyntheticsCanaryRunConfigOutputReference":
        return typing.cast("SyntheticsCanaryRunConfigOutputReference", jsii.get(self, "runConfig"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "SyntheticsCanaryScheduleOutputReference":
        return typing.cast("SyntheticsCanaryScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="sourceLocationArn")
    def source_location_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeline")
    def timeline(self) -> "SyntheticsCanaryTimelineList":
        return typing.cast("SyntheticsCanaryTimelineList", jsii.get(self, "timeline"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "SyntheticsCanaryVpcConfigOutputReference":
        return typing.cast("SyntheticsCanaryVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="artifactConfigInput")
    def artifact_config_input(
        self,
    ) -> typing.Optional["SyntheticsCanaryArtifactConfig"]:
        return typing.cast(typing.Optional["SyntheticsCanaryArtifactConfig"], jsii.get(self, "artifactConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactS3LocationInput")
    def artifact_s3_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactS3LocationInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteLambdaInput")
    def delete_lambda_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteLambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="failureRetentionPeriodInput")
    def failure_retention_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="handlerInput")
    def handler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handlerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="runConfigInput")
    def run_config_input(self) -> typing.Optional["SyntheticsCanaryRunConfig"]:
        return typing.cast(typing.Optional["SyntheticsCanaryRunConfig"], jsii.get(self, "runConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeVersionInput")
    def runtime_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInput")
    def s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KeyInput")
    def s3_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyInput"))

    @builtins.property
    @jsii.member(jsii_name="s3VersionInput")
    def s3_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3VersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["SyntheticsCanarySchedule"]:
        return typing.cast(typing.Optional["SyntheticsCanarySchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="startCanaryInput")
    def start_canary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "startCanaryInput"))

    @builtins.property
    @jsii.member(jsii_name="successRetentionPeriodInput")
    def success_retention_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successRetentionPeriodInput"))

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
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(self) -> typing.Optional["SyntheticsCanaryVpcConfig"]:
        return typing.cast(typing.Optional["SyntheticsCanaryVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="zipFileInput")
    def zip_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipFileInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactS3Location")
    def artifact_s3_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactS3Location"))

    @artifact_s3_location.setter
    def artifact_s3_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9685600921e7f7ba2f8b0f79d53b009662ed667d36b3e0df795dde4b6af1c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="deleteLambda")
    def delete_lambda(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteLambda"))

    @delete_lambda.setter
    def delete_lambda(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9d70dad191d5e6cb3e9665737c967e42ffad03b419ab397315912c137efb88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteLambda", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4723bb0a15ffc0d4de6dfc2f1ae93bc9169f5ad753cd13f5dadc87eda95feeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="failureRetentionPeriod")
    def failure_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureRetentionPeriod"))

    @failure_retention_period.setter
    def failure_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5acb239a8f78dab5895b1f3043cbfc00b64d668c239e5b24c6c68d73b355d0f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handler"))

    @handler.setter
    def handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68cfe3b415f6a692717f302a21d3e0649f014c52b3e2bffa6a27ea96591cd17b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handler", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d568f5b18c3f4f58c128f8ca4da2bc49b10a6506f48423459de2955395e6197e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6a3faed553c3ea05fd686c8786e21897d05de518641934c84172824288e3ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a50c83f87bed1ab0ba843ad338553699609369a5500969de9caf471857605b2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a8e95efd1a06d64f0b85fc20f5d578aafdf35f2f83b813e656c4e67aca67259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="s3Key")
    def s3_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Key"))

    @s3_key.setter
    def s3_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f1c1141d59a01df9303a656beba8a4fc63efd6812abadf1194d030a35b25570)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Key", value)

    @builtins.property
    @jsii.member(jsii_name="s3Version")
    def s3_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Version"))

    @s3_version.setter
    def s3_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c1a7c7781c8b21230dfc109b28ba6d2b553cbf3000686f24aceebd9d594625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Version", value)

    @builtins.property
    @jsii.member(jsii_name="startCanary")
    def start_canary(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "startCanary"))

    @start_canary.setter
    def start_canary(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d0f57a51a1b4f9343520bbfee2a36dfdc9bcaf3c44c88a2bebf786d67870e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startCanary", value)

    @builtins.property
    @jsii.member(jsii_name="successRetentionPeriod")
    def success_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRetentionPeriod"))

    @success_retention_period.setter
    def success_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6463b7ed7af5206a80212773f3c6074a30828b56bfb1b2251ccd4b1d5686751)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592fa0201260652b3538e6843e6fee25e3ffc59374dd971d2652ac13c6fbe714)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1652b7f61f99f1e6b0204bb0b36461ae2ad897771589766d5e763b2f51e0296)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="zipFile")
    def zip_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipFile"))

    @zip_file.setter
    def zip_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__946adcac7137edb94fc51a20f8e982fb967b8075c134525de795d87e29086c78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipFile", value)


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryArtifactConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_encryption": "s3Encryption"},
)
class SyntheticsCanaryArtifactConfig:
    def __init__(
        self,
        *,
        s3_encryption: typing.Optional[typing.Union["SyntheticsCanaryArtifactConfigS3Encryption", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_encryption: s3_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_encryption SyntheticsCanary#s3_encryption}
        '''
        if isinstance(s3_encryption, dict):
            s3_encryption = SyntheticsCanaryArtifactConfigS3Encryption(**s3_encryption)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22cea6b76bd3c75adc5060c120b5e3ee3d318ffadc5e38ce9efdf40eeac31ce4)
            check_type(argname="argument s3_encryption", value=s3_encryption, expected_type=type_hints["s3_encryption"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_encryption is not None:
            self._values["s3_encryption"] = s3_encryption

    @builtins.property
    def s3_encryption(
        self,
    ) -> typing.Optional["SyntheticsCanaryArtifactConfigS3Encryption"]:
        '''s3_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_encryption SyntheticsCanary#s3_encryption}
        '''
        result = self._values.get("s3_encryption")
        return typing.cast(typing.Optional["SyntheticsCanaryArtifactConfigS3Encryption"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanaryArtifactConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsCanaryArtifactConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryArtifactConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bb6821e22fa647ad84b05120b029ea08295f579f5e7e143d71e8da10514ad6f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3Encryption")
    def put_s3_encryption(
        self,
        *,
        encryption_mode: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#encryption_mode SyntheticsCanary#encryption_mode}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#kms_key_arn SyntheticsCanary#kms_key_arn}.
        '''
        value = SyntheticsCanaryArtifactConfigS3Encryption(
            encryption_mode=encryption_mode, kms_key_arn=kms_key_arn
        )

        return typing.cast(None, jsii.invoke(self, "putS3Encryption", [value]))

    @jsii.member(jsii_name="resetS3Encryption")
    def reset_s3_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Encryption", []))

    @builtins.property
    @jsii.member(jsii_name="s3Encryption")
    def s3_encryption(
        self,
    ) -> "SyntheticsCanaryArtifactConfigS3EncryptionOutputReference":
        return typing.cast("SyntheticsCanaryArtifactConfigS3EncryptionOutputReference", jsii.get(self, "s3Encryption"))

    @builtins.property
    @jsii.member(jsii_name="s3EncryptionInput")
    def s3_encryption_input(
        self,
    ) -> typing.Optional["SyntheticsCanaryArtifactConfigS3Encryption"]:
        return typing.cast(typing.Optional["SyntheticsCanaryArtifactConfigS3Encryption"], jsii.get(self, "s3EncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsCanaryArtifactConfig]:
        return typing.cast(typing.Optional[SyntheticsCanaryArtifactConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsCanaryArtifactConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992b842c592cee19630c4e40b70a11195397be6d43576f11a0cc8f367a416c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryArtifactConfigS3Encryption",
    jsii_struct_bases=[],
    name_mapping={"encryption_mode": "encryptionMode", "kms_key_arn": "kmsKeyArn"},
)
class SyntheticsCanaryArtifactConfigS3Encryption:
    def __init__(
        self,
        *,
        encryption_mode: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#encryption_mode SyntheticsCanary#encryption_mode}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#kms_key_arn SyntheticsCanary#kms_key_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__506630cd7d91326019ee698f6a4bc569da2d0a776f68271f2fdcbe5948f97479)
            check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#encryption_mode SyntheticsCanary#encryption_mode}.'''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#kms_key_arn SyntheticsCanary#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanaryArtifactConfigS3Encryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsCanaryArtifactConfigS3EncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryArtifactConfigS3EncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5483e5906e7e8b2c2d9558dff0494bd3afbe99e280c8dec81b3d86340e9e5bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEncryptionMode")
    def reset_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionMode", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionModeInput")
    def encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6612045a0f8ccdd73f9c7dbc6e9e21d621ac47070adca97e4435130f163e410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0b8c1e0c9aab088a551c200a7d1ddccadd73461c02e7ac3489719d6c97ce6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsCanaryArtifactConfigS3Encryption]:
        return typing.cast(typing.Optional[SyntheticsCanaryArtifactConfigS3Encryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsCanaryArtifactConfigS3Encryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a5762fa077f268bd72d911ba2f72df4542c03326709aebec4db4688b519628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "artifact_s3_location": "artifactS3Location",
        "execution_role_arn": "executionRoleArn",
        "handler": "handler",
        "name": "name",
        "runtime_version": "runtimeVersion",
        "schedule": "schedule",
        "artifact_config": "artifactConfig",
        "delete_lambda": "deleteLambda",
        "failure_retention_period": "failureRetentionPeriod",
        "id": "id",
        "run_config": "runConfig",
        "s3_bucket": "s3Bucket",
        "s3_key": "s3Key",
        "s3_version": "s3Version",
        "start_canary": "startCanary",
        "success_retention_period": "successRetentionPeriod",
        "tags": "tags",
        "tags_all": "tagsAll",
        "vpc_config": "vpcConfig",
        "zip_file": "zipFile",
    },
)
class SyntheticsCanaryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        artifact_s3_location: builtins.str,
        execution_role_arn: builtins.str,
        handler: builtins.str,
        name: builtins.str,
        runtime_version: builtins.str,
        schedule: typing.Union["SyntheticsCanarySchedule", typing.Dict[builtins.str, typing.Any]],
        artifact_config: typing.Optional[typing.Union[SyntheticsCanaryArtifactConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        delete_lambda: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        failure_retention_period: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        run_config: typing.Optional[typing.Union["SyntheticsCanaryRunConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket: typing.Optional[builtins.str] = None,
        s3_key: typing.Optional[builtins.str] = None,
        s3_version: typing.Optional[builtins.str] = None,
        start_canary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        success_retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["SyntheticsCanaryVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        zip_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param artifact_s3_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#artifact_s3_location SyntheticsCanary#artifact_s3_location}.
        :param execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#execution_role_arn SyntheticsCanary#execution_role_arn}.
        :param handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#handler SyntheticsCanary#handler}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#name SyntheticsCanary#name}.
        :param runtime_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#runtime_version SyntheticsCanary#runtime_version}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#schedule SyntheticsCanary#schedule}
        :param artifact_config: artifact_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#artifact_config SyntheticsCanary#artifact_config}
        :param delete_lambda: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#delete_lambda SyntheticsCanary#delete_lambda}.
        :param failure_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#failure_retention_period SyntheticsCanary#failure_retention_period}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#id SyntheticsCanary#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param run_config: run_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#run_config SyntheticsCanary#run_config}
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_bucket SyntheticsCanary#s3_bucket}.
        :param s3_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_key SyntheticsCanary#s3_key}.
        :param s3_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_version SyntheticsCanary#s3_version}.
        :param start_canary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#start_canary SyntheticsCanary#start_canary}.
        :param success_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#success_retention_period SyntheticsCanary#success_retention_period}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#tags SyntheticsCanary#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#tags_all SyntheticsCanary#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#vpc_config SyntheticsCanary#vpc_config}
        :param zip_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#zip_file SyntheticsCanary#zip_file}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schedule, dict):
            schedule = SyntheticsCanarySchedule(**schedule)
        if isinstance(artifact_config, dict):
            artifact_config = SyntheticsCanaryArtifactConfig(**artifact_config)
        if isinstance(run_config, dict):
            run_config = SyntheticsCanaryRunConfig(**run_config)
        if isinstance(vpc_config, dict):
            vpc_config = SyntheticsCanaryVpcConfig(**vpc_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe509ea1a455c79c6e27591b644a812528fa1ebfc97ec803455bdfcaf5942be)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument artifact_s3_location", value=artifact_s3_location, expected_type=type_hints["artifact_s3_location"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument artifact_config", value=artifact_config, expected_type=type_hints["artifact_config"])
            check_type(argname="argument delete_lambda", value=delete_lambda, expected_type=type_hints["delete_lambda"])
            check_type(argname="argument failure_retention_period", value=failure_retention_period, expected_type=type_hints["failure_retention_period"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument run_config", value=run_config, expected_type=type_hints["run_config"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            check_type(argname="argument s3_version", value=s3_version, expected_type=type_hints["s3_version"])
            check_type(argname="argument start_canary", value=start_canary, expected_type=type_hints["start_canary"])
            check_type(argname="argument success_retention_period", value=success_retention_period, expected_type=type_hints["success_retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            check_type(argname="argument zip_file", value=zip_file, expected_type=type_hints["zip_file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifact_s3_location": artifact_s3_location,
            "execution_role_arn": execution_role_arn,
            "handler": handler,
            "name": name,
            "runtime_version": runtime_version,
            "schedule": schedule,
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
        if artifact_config is not None:
            self._values["artifact_config"] = artifact_config
        if delete_lambda is not None:
            self._values["delete_lambda"] = delete_lambda
        if failure_retention_period is not None:
            self._values["failure_retention_period"] = failure_retention_period
        if id is not None:
            self._values["id"] = id
        if run_config is not None:
            self._values["run_config"] = run_config
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket
        if s3_key is not None:
            self._values["s3_key"] = s3_key
        if s3_version is not None:
            self._values["s3_version"] = s3_version
        if start_canary is not None:
            self._values["start_canary"] = start_canary
        if success_retention_period is not None:
            self._values["success_retention_period"] = success_retention_period
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config
        if zip_file is not None:
            self._values["zip_file"] = zip_file

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
    def artifact_s3_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#artifact_s3_location SyntheticsCanary#artifact_s3_location}.'''
        result = self._values.get("artifact_s3_location")
        assert result is not None, "Required property 'artifact_s3_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#execution_role_arn SyntheticsCanary#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def handler(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#handler SyntheticsCanary#handler}.'''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#name SyntheticsCanary#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#runtime_version SyntheticsCanary#runtime_version}.'''
        result = self._values.get("runtime_version")
        assert result is not None, "Required property 'runtime_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "SyntheticsCanarySchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#schedule SyntheticsCanary#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("SyntheticsCanarySchedule", result)

    @builtins.property
    def artifact_config(self) -> typing.Optional[SyntheticsCanaryArtifactConfig]:
        '''artifact_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#artifact_config SyntheticsCanary#artifact_config}
        '''
        result = self._values.get("artifact_config")
        return typing.cast(typing.Optional[SyntheticsCanaryArtifactConfig], result)

    @builtins.property
    def delete_lambda(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#delete_lambda SyntheticsCanary#delete_lambda}.'''
        result = self._values.get("delete_lambda")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def failure_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#failure_retention_period SyntheticsCanary#failure_retention_period}.'''
        result = self._values.get("failure_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#id SyntheticsCanary#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_config(self) -> typing.Optional["SyntheticsCanaryRunConfig"]:
        '''run_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#run_config SyntheticsCanary#run_config}
        '''
        result = self._values.get("run_config")
        return typing.cast(typing.Optional["SyntheticsCanaryRunConfig"], result)

    @builtins.property
    def s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_bucket SyntheticsCanary#s3_bucket}.'''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_key SyntheticsCanary#s3_key}.'''
        result = self._values.get("s3_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#s3_version SyntheticsCanary#s3_version}.'''
        result = self._values.get("s3_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_canary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#start_canary SyntheticsCanary#start_canary}.'''
        result = self._values.get("start_canary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def success_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#success_retention_period SyntheticsCanary#success_retention_period}.'''
        result = self._values.get("success_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#tags SyntheticsCanary#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#tags_all SyntheticsCanary#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["SyntheticsCanaryVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#vpc_config SyntheticsCanary#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["SyntheticsCanaryVpcConfig"], result)

    @builtins.property
    def zip_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#zip_file SyntheticsCanary#zip_file}.'''
        result = self._values.get("zip_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanaryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryRunConfig",
    jsii_struct_bases=[],
    name_mapping={
        "active_tracing": "activeTracing",
        "environment_variables": "environmentVariables",
        "memory_in_mb": "memoryInMb",
        "timeout_in_seconds": "timeoutInSeconds",
    },
)
class SyntheticsCanaryRunConfig:
    def __init__(
        self,
        *,
        active_tracing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory_in_mb: typing.Optional[jsii.Number] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param active_tracing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#active_tracing SyntheticsCanary#active_tracing}.
        :param environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#environment_variables SyntheticsCanary#environment_variables}.
        :param memory_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#memory_in_mb SyntheticsCanary#memory_in_mb}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#timeout_in_seconds SyntheticsCanary#timeout_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2d6c7b1741e2b960fb630eb77ab31e84965548d09374fb50b8c50c724976ac6)
            check_type(argname="argument active_tracing", value=active_tracing, expected_type=type_hints["active_tracing"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument memory_in_mb", value=memory_in_mb, expected_type=type_hints["memory_in_mb"])
            check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if active_tracing is not None:
            self._values["active_tracing"] = active_tracing
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if memory_in_mb is not None:
            self._values["memory_in_mb"] = memory_in_mb
        if timeout_in_seconds is not None:
            self._values["timeout_in_seconds"] = timeout_in_seconds

    @builtins.property
    def active_tracing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#active_tracing SyntheticsCanary#active_tracing}.'''
        result = self._values.get("active_tracing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#environment_variables SyntheticsCanary#environment_variables}.'''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def memory_in_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#memory_in_mb SyntheticsCanary#memory_in_mb}.'''
        result = self._values.get("memory_in_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#timeout_in_seconds SyntheticsCanary#timeout_in_seconds}.'''
        result = self._values.get("timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanaryRunConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsCanaryRunConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryRunConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b5f4eed68437b8f6fc78b7f7ff304c3a7af4a115695a2c9c788c5091fd19e76)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActiveTracing")
    def reset_active_tracing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveTracing", []))

    @jsii.member(jsii_name="resetEnvironmentVariables")
    def reset_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariables", []))

    @jsii.member(jsii_name="resetMemoryInMb")
    def reset_memory_in_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryInMb", []))

    @jsii.member(jsii_name="resetTimeoutInSeconds")
    def reset_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="activeTracingInput")
    def active_tracing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activeTracingInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariablesInput")
    def environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInMbInput")
    def memory_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInSecondsInput")
    def timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="activeTracing")
    def active_tracing(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "activeTracing"))

    @active_tracing.setter
    def active_tracing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e93dec86b4de4b0378d51332a9e78edf767a71535aa473032aab3bc130a75a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeTracing", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e351794e1c587ab8fb80c9e1642549f435c0e6eb1dd0212f02bfc436038a9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="memoryInMb")
    def memory_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryInMb"))

    @memory_in_mb.setter
    def memory_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27eff39148254bf5bb2c9e9d19aaa725ed5aaad69a17ad8cc8fe2f73fd6acd70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryInMb", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutInSeconds"))

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd038b24f32fca52e431f4f14df33e43ce940e52160dd5908aa80b388b53661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsCanaryRunConfig]:
        return typing.cast(typing.Optional[SyntheticsCanaryRunConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SyntheticsCanaryRunConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c673b378ba142b91cad63b9f99fb997807d522f49c1276499d9ad9c0f1cfc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanarySchedule",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "duration_in_seconds": "durationInSeconds",
    },
)
class SyntheticsCanarySchedule:
    def __init__(
        self,
        *,
        expression: builtins.str,
        duration_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#expression SyntheticsCanary#expression}.
        :param duration_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#duration_in_seconds SyntheticsCanary#duration_in_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64ed5e86e4518d5c766a77f825a81a325ad8d1ff21dc76c12f17561f7e51f5e)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
        }
        if duration_in_seconds is not None:
            self._values["duration_in_seconds"] = duration_in_seconds

    @builtins.property
    def expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#expression SyntheticsCanary#expression}.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#duration_in_seconds SyntheticsCanary#duration_in_seconds}.'''
        result = self._values.get("duration_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanarySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsCanaryScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a843345bc765dac138150e0292f434ef1488e8b933b02efd634d61d8861934c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDurationInSeconds")
    def reset_duration_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDurationInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="durationInSecondsInput")
    def duration_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInSeconds")
    def duration_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "durationInSeconds"))

    @duration_in_seconds.setter
    def duration_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__478e4dd34c39932dbbfda1b268fcd78cfbb78fb3f8f29d2a5ae01aadca6c6999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durationInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de2f6c236f7980c3cff7186f8f2a5a7008f1f34ff91ede68058bcefbc1de1d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsCanarySchedule]:
        return typing.cast(typing.Optional[SyntheticsCanarySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SyntheticsCanarySchedule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a10a4a566a4e2637de2ab1cadcdb61a255118c48c370f4e1bcb72dc88563da87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryTimeline",
    jsii_struct_bases=[],
    name_mapping={},
)
class SyntheticsCanaryTimeline:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanaryTimeline(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsCanaryTimelineList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryTimelineList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__63f8554ba46ec1e7e56fe8dcb2abcd90e660d9677b51fe6c54eaa978b4379254)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SyntheticsCanaryTimelineOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__718c636a2500c33a8c9ddf049c36cd7558bc2ca0c4c7abef725a6326247a34ad)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticsCanaryTimelineOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d43c3d9503ff6c07db0cb986562d2c8782ed8ee00e7ba9a48347b1b3554eaf9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc316c339faea947991cc64bb6c86f4509a5040c7100dd62c4a56a9820a85654)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f5f27bc0547f2745ea6996ba36b70f5f03a1ef70e489abdf44db002821a880e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class SyntheticsCanaryTimelineOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryTimelineOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86a4aca1958a593fd597bbff01fa252ffbfa0f717ab64df06cf12fded18b61ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="created")
    def created(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "created"))

    @builtins.property
    @jsii.member(jsii_name="lastModified")
    def last_modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModified"))

    @builtins.property
    @jsii.member(jsii_name="lastStarted")
    def last_started(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastStarted"))

    @builtins.property
    @jsii.member(jsii_name="lastStopped")
    def last_stopped(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastStopped"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsCanaryTimeline]:
        return typing.cast(typing.Optional[SyntheticsCanaryTimeline], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SyntheticsCanaryTimeline]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a39928170728dfedbfefed0da851641895cd73d94717708678a847c08fff15c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryVpcConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class SyntheticsCanaryVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#security_group_ids SyntheticsCanary#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#subnet_ids SyntheticsCanary#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f796c04931f4087b191f9252e9a1c209bd6b87a0195cca195a235260be9792b3)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#security_group_ids SyntheticsCanary#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/synthetics_canary#subnet_ids SyntheticsCanary#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsCanaryVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsCanaryVpcConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.syntheticsCanary.SyntheticsCanaryVpcConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d12a1d584d7f1f8964f698ae0f790d7be37ed5859726e7be050ae4badbaf38cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c296cab670d6f1381d48ea96cf2bfb86a4609f10f2dda26db148b2c623849b3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10cf835d591807ccb435130467f04b240d65caa1d0f49de123812bd884b5efa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticsCanaryVpcConfig]:
        return typing.cast(typing.Optional[SyntheticsCanaryVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SyntheticsCanaryVpcConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fcb3594c7a2d3d666a64294fe574056cd8a1545f02f919b011cfd784d7acd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticsCanary",
    "SyntheticsCanaryArtifactConfig",
    "SyntheticsCanaryArtifactConfigOutputReference",
    "SyntheticsCanaryArtifactConfigS3Encryption",
    "SyntheticsCanaryArtifactConfigS3EncryptionOutputReference",
    "SyntheticsCanaryConfig",
    "SyntheticsCanaryRunConfig",
    "SyntheticsCanaryRunConfigOutputReference",
    "SyntheticsCanarySchedule",
    "SyntheticsCanaryScheduleOutputReference",
    "SyntheticsCanaryTimeline",
    "SyntheticsCanaryTimelineList",
    "SyntheticsCanaryTimelineOutputReference",
    "SyntheticsCanaryVpcConfig",
    "SyntheticsCanaryVpcConfigOutputReference",
]

publication.publish()

def _typecheckingstub__fae2737e406f92a5fc740604b01a6735c0ff11532c4dc64f6be9f1dd8168ffad(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    artifact_s3_location: builtins.str,
    execution_role_arn: builtins.str,
    handler: builtins.str,
    name: builtins.str,
    runtime_version: builtins.str,
    schedule: typing.Union[SyntheticsCanarySchedule, typing.Dict[builtins.str, typing.Any]],
    artifact_config: typing.Optional[typing.Union[SyntheticsCanaryArtifactConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_lambda: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    failure_retention_period: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    run_config: typing.Optional[typing.Union[SyntheticsCanaryRunConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket: typing.Optional[builtins.str] = None,
    s3_key: typing.Optional[builtins.str] = None,
    s3_version: typing.Optional[builtins.str] = None,
    start_canary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    success_retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[SyntheticsCanaryVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    zip_file: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__7d9685600921e7f7ba2f8b0f79d53b009662ed667d36b3e0df795dde4b6af1c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9d70dad191d5e6cb3e9665737c967e42ffad03b419ab397315912c137efb88(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4723bb0a15ffc0d4de6dfc2f1ae93bc9169f5ad753cd13f5dadc87eda95feeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5acb239a8f78dab5895b1f3043cbfc00b64d668c239e5b24c6c68d73b355d0f9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68cfe3b415f6a692717f302a21d3e0649f014c52b3e2bffa6a27ea96591cd17b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d568f5b18c3f4f58c128f8ca4da2bc49b10a6506f48423459de2955395e6197e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a3faed553c3ea05fd686c8786e21897d05de518641934c84172824288e3ef6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50c83f87bed1ab0ba843ad338553699609369a5500969de9caf471857605b2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a8e95efd1a06d64f0b85fc20f5d578aafdf35f2f83b813e656c4e67aca67259(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f1c1141d59a01df9303a656beba8a4fc63efd6812abadf1194d030a35b25570(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c1a7c7781c8b21230dfc109b28ba6d2b553cbf3000686f24aceebd9d594625(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d0f57a51a1b4f9343520bbfee2a36dfdc9bcaf3c44c88a2bebf786d67870e4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6463b7ed7af5206a80212773f3c6074a30828b56bfb1b2251ccd4b1d5686751(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592fa0201260652b3538e6843e6fee25e3ffc59374dd971d2652ac13c6fbe714(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1652b7f61f99f1e6b0204bb0b36461ae2ad897771589766d5e763b2f51e0296(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__946adcac7137edb94fc51a20f8e982fb967b8075c134525de795d87e29086c78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22cea6b76bd3c75adc5060c120b5e3ee3d318ffadc5e38ce9efdf40eeac31ce4(
    *,
    s3_encryption: typing.Optional[typing.Union[SyntheticsCanaryArtifactConfigS3Encryption, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb6821e22fa647ad84b05120b029ea08295f579f5e7e143d71e8da10514ad6f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992b842c592cee19630c4e40b70a11195397be6d43576f11a0cc8f367a416c1b(
    value: typing.Optional[SyntheticsCanaryArtifactConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506630cd7d91326019ee698f6a4bc569da2d0a776f68271f2fdcbe5948f97479(
    *,
    encryption_mode: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5483e5906e7e8b2c2d9558dff0494bd3afbe99e280c8dec81b3d86340e9e5bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6612045a0f8ccdd73f9c7dbc6e9e21d621ac47070adca97e4435130f163e410(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0b8c1e0c9aab088a551c200a7d1ddccadd73461c02e7ac3489719d6c97ce6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a5762fa077f268bd72d911ba2f72df4542c03326709aebec4db4688b519628(
    value: typing.Optional[SyntheticsCanaryArtifactConfigS3Encryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe509ea1a455c79c6e27591b644a812528fa1ebfc97ec803455bdfcaf5942be(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    artifact_s3_location: builtins.str,
    execution_role_arn: builtins.str,
    handler: builtins.str,
    name: builtins.str,
    runtime_version: builtins.str,
    schedule: typing.Union[SyntheticsCanarySchedule, typing.Dict[builtins.str, typing.Any]],
    artifact_config: typing.Optional[typing.Union[SyntheticsCanaryArtifactConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_lambda: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    failure_retention_period: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    run_config: typing.Optional[typing.Union[SyntheticsCanaryRunConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket: typing.Optional[builtins.str] = None,
    s3_key: typing.Optional[builtins.str] = None,
    s3_version: typing.Optional[builtins.str] = None,
    start_canary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    success_retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_config: typing.Optional[typing.Union[SyntheticsCanaryVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    zip_file: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2d6c7b1741e2b960fb630eb77ab31e84965548d09374fb50b8c50c724976ac6(
    *,
    active_tracing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    memory_in_mb: typing.Optional[jsii.Number] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b5f4eed68437b8f6fc78b7f7ff304c3a7af4a115695a2c9c788c5091fd19e76(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e93dec86b4de4b0378d51332a9e78edf767a71535aa473032aab3bc130a75a5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e351794e1c587ab8fb80c9e1642549f435c0e6eb1dd0212f02bfc436038a9f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27eff39148254bf5bb2c9e9d19aaa725ed5aaad69a17ad8cc8fe2f73fd6acd70(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd038b24f32fca52e431f4f14df33e43ce940e52160dd5908aa80b388b53661(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c673b378ba142b91cad63b9f99fb997807d522f49c1276499d9ad9c0f1cfc6(
    value: typing.Optional[SyntheticsCanaryRunConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64ed5e86e4518d5c766a77f825a81a325ad8d1ff21dc76c12f17561f7e51f5e(
    *,
    expression: builtins.str,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a843345bc765dac138150e0292f434ef1488e8b933b02efd634d61d8861934c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__478e4dd34c39932dbbfda1b268fcd78cfbb78fb3f8f29d2a5ae01aadca6c6999(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de2f6c236f7980c3cff7186f8f2a5a7008f1f34ff91ede68058bcefbc1de1d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a10a4a566a4e2637de2ab1cadcdb61a255118c48c370f4e1bcb72dc88563da87(
    value: typing.Optional[SyntheticsCanarySchedule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f8554ba46ec1e7e56fe8dcb2abcd90e660d9677b51fe6c54eaa978b4379254(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__718c636a2500c33a8c9ddf049c36cd7558bc2ca0c4c7abef725a6326247a34ad(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d43c3d9503ff6c07db0cb986562d2c8782ed8ee00e7ba9a48347b1b3554eaf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc316c339faea947991cc64bb6c86f4509a5040c7100dd62c4a56a9820a85654(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5f27bc0547f2745ea6996ba36b70f5f03a1ef70e489abdf44db002821a880e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a4aca1958a593fd597bbff01fa252ffbfa0f717ab64df06cf12fded18b61ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a39928170728dfedbfefed0da851641895cd73d94717708678a847c08fff15c(
    value: typing.Optional[SyntheticsCanaryTimeline],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f796c04931f4087b191f9252e9a1c209bd6b87a0195cca195a235260be9792b3(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12a1d584d7f1f8964f698ae0f790d7be37ed5859726e7be050ae4badbaf38cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c296cab670d6f1381d48ea96cf2bfb86a4609f10f2dda26db148b2c623849b3e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10cf835d591807ccb435130467f04b240d65caa1d0f49de123812bd884b5efa4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fcb3594c7a2d3d666a64294fe574056cd8a1545f02f919b011cfd784d7acd9(
    value: typing.Optional[SyntheticsCanaryVpcConfig],
) -> None:
    """Type checking stubs"""
    pass
