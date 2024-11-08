'''
# `aws_lambda_function`

Refer to the Terraform Registory for docs: [`aws_lambda_function`](https://www.terraform.io/docs/providers/aws/r/lambda_function).
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


class LambdaFunction(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunction",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lambda_function aws_lambda_function}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        function_name: builtins.str,
        role: builtins.str,
        architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
        code_signing_config_arn: typing.Optional[builtins.str] = None,
        dead_letter_config: typing.Optional[typing.Union["LambdaFunctionDeadLetterConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Union["LambdaFunctionEnvironment", typing.Dict[builtins.str, typing.Any]]] = None,
        ephemeral_storage: typing.Optional[typing.Union["LambdaFunctionEphemeralStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        filename: typing.Optional[builtins.str] = None,
        file_system_config: typing.Optional[typing.Union["LambdaFunctionFileSystemConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        handler: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_config: typing.Optional[typing.Union["LambdaFunctionImageConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        layers: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        package_type: typing.Optional[builtins.str] = None,
        publish: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        runtime: typing.Optional[builtins.str] = None,
        s3_bucket: typing.Optional[builtins.str] = None,
        s3_key: typing.Optional[builtins.str] = None,
        s3_object_version: typing.Optional[builtins.str] = None,
        snap_start: typing.Optional[typing.Union["LambdaFunctionSnapStart", typing.Dict[builtins.str, typing.Any]]] = None,
        source_code_hash: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["LambdaFunctionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        tracing_config: typing.Optional[typing.Union["LambdaFunctionTracingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_config: typing.Optional[typing.Union["LambdaFunctionVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lambda_function aws_lambda_function} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#function_name LambdaFunction#function_name}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#role LambdaFunction#role}.
        :param architectures: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#architectures LambdaFunction#architectures}.
        :param code_signing_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#code_signing_config_arn LambdaFunction#code_signing_config_arn}.
        :param dead_letter_config: dead_letter_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#dead_letter_config LambdaFunction#dead_letter_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#description LambdaFunction#description}.
        :param environment: environment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#environment LambdaFunction#environment}
        :param ephemeral_storage: ephemeral_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#ephemeral_storage LambdaFunction#ephemeral_storage}
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#filename LambdaFunction#filename}.
        :param file_system_config: file_system_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#file_system_config LambdaFunction#file_system_config}
        :param handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#handler LambdaFunction#handler}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#id LambdaFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_config: image_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#image_config LambdaFunction#image_config}
        :param image_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#image_uri LambdaFunction#image_uri}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#kms_key_arn LambdaFunction#kms_key_arn}.
        :param layers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#layers LambdaFunction#layers}.
        :param memory_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#memory_size LambdaFunction#memory_size}.
        :param package_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#package_type LambdaFunction#package_type}.
        :param publish: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#publish LambdaFunction#publish}.
        :param reserved_concurrent_executions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#reserved_concurrent_executions LambdaFunction#reserved_concurrent_executions}.
        :param runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#runtime LambdaFunction#runtime}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_bucket LambdaFunction#s3_bucket}.
        :param s3_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_key LambdaFunction#s3_key}.
        :param s3_object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_object_version LambdaFunction#s3_object_version}.
        :param snap_start: snap_start block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#snap_start LambdaFunction#snap_start}
        :param source_code_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#source_code_hash LambdaFunction#source_code_hash}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tags LambdaFunction#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tags_all LambdaFunction#tags_all}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#timeout LambdaFunction#timeout}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#timeouts LambdaFunction#timeouts}
        :param tracing_config: tracing_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tracing_config LambdaFunction#tracing_config}
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#vpc_config LambdaFunction#vpc_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955d0469461df7695e0ddad0f5cbd53ae32a3b40d5fa48a8fb68c3858bdf752f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LambdaFunctionConfig(
            function_name=function_name,
            role=role,
            architectures=architectures,
            code_signing_config_arn=code_signing_config_arn,
            dead_letter_config=dead_letter_config,
            description=description,
            environment=environment,
            ephemeral_storage=ephemeral_storage,
            filename=filename,
            file_system_config=file_system_config,
            handler=handler,
            id=id,
            image_config=image_config,
            image_uri=image_uri,
            kms_key_arn=kms_key_arn,
            layers=layers,
            memory_size=memory_size,
            package_type=package_type,
            publish=publish,
            reserved_concurrent_executions=reserved_concurrent_executions,
            runtime=runtime,
            s3_bucket=s3_bucket,
            s3_key=s3_key,
            s3_object_version=s3_object_version,
            snap_start=snap_start,
            source_code_hash=source_code_hash,
            tags=tags,
            tags_all=tags_all,
            timeout=timeout,
            timeouts=timeouts,
            tracing_config=tracing_config,
            vpc_config=vpc_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDeadLetterConfig")
    def put_dead_letter_config(self, *, target_arn: builtins.str) -> None:
        '''
        :param target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#target_arn LambdaFunction#target_arn}.
        '''
        value = LambdaFunctionDeadLetterConfig(target_arn=target_arn)

        return typing.cast(None, jsii.invoke(self, "putDeadLetterConfig", [value]))

    @jsii.member(jsii_name="putEnvironment")
    def put_environment(
        self,
        *,
        variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#variables LambdaFunction#variables}.
        '''
        value = LambdaFunctionEnvironment(variables=variables)

        return typing.cast(None, jsii.invoke(self, "putEnvironment", [value]))

    @jsii.member(jsii_name="putEphemeralStorage")
    def put_ephemeral_storage(
        self,
        *,
        size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#size LambdaFunction#size}.
        '''
        value = LambdaFunctionEphemeralStorage(size=size)

        return typing.cast(None, jsii.invoke(self, "putEphemeralStorage", [value]))

    @jsii.member(jsii_name="putFileSystemConfig")
    def put_file_system_config(
        self,
        *,
        arn: builtins.str,
        local_mount_path: builtins.str,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#arn LambdaFunction#arn}.
        :param local_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#local_mount_path LambdaFunction#local_mount_path}.
        '''
        value = LambdaFunctionFileSystemConfig(
            arn=arn, local_mount_path=local_mount_path
        )

        return typing.cast(None, jsii.invoke(self, "putFileSystemConfig", [value]))

    @jsii.member(jsii_name="putImageConfig")
    def put_image_config(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#command LambdaFunction#command}.
        :param entry_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#entry_point LambdaFunction#entry_point}.
        :param working_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#working_directory LambdaFunction#working_directory}.
        '''
        value = LambdaFunctionImageConfig(
            command=command,
            entry_point=entry_point,
            working_directory=working_directory,
        )

        return typing.cast(None, jsii.invoke(self, "putImageConfig", [value]))

    @jsii.member(jsii_name="putSnapStart")
    def put_snap_start(self, *, apply_on: builtins.str) -> None:
        '''
        :param apply_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#apply_on LambdaFunction#apply_on}.
        '''
        value = LambdaFunctionSnapStart(apply_on=apply_on)

        return typing.cast(None, jsii.invoke(self, "putSnapStart", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#create LambdaFunction#create}.
        '''
        value = LambdaFunctionTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTracingConfig")
    def put_tracing_config(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#mode LambdaFunction#mode}.
        '''
        value = LambdaFunctionTracingConfig(mode=mode)

        return typing.cast(None, jsii.invoke(self, "putTracingConfig", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#security_group_ids LambdaFunction#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#subnet_ids LambdaFunction#subnet_ids}.
        '''
        value = LambdaFunctionVpcConfig(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetArchitectures")
    def reset_architectures(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchitectures", []))

    @jsii.member(jsii_name="resetCodeSigningConfigArn")
    def reset_code_signing_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeSigningConfigArn", []))

    @jsii.member(jsii_name="resetDeadLetterConfig")
    def reset_dead_letter_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetterConfig", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetEphemeralStorage")
    def reset_ephemeral_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEphemeralStorage", []))

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @jsii.member(jsii_name="resetFileSystemConfig")
    def reset_file_system_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemConfig", []))

    @jsii.member(jsii_name="resetHandler")
    def reset_handler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHandler", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageConfig")
    def reset_image_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageConfig", []))

    @jsii.member(jsii_name="resetImageUri")
    def reset_image_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageUri", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetLayers")
    def reset_layers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLayers", []))

    @jsii.member(jsii_name="resetMemorySize")
    def reset_memory_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemorySize", []))

    @jsii.member(jsii_name="resetPackageType")
    def reset_package_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackageType", []))

    @jsii.member(jsii_name="resetPublish")
    def reset_publish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublish", []))

    @jsii.member(jsii_name="resetReservedConcurrentExecutions")
    def reset_reserved_concurrent_executions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservedConcurrentExecutions", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @jsii.member(jsii_name="resetS3Bucket")
    def reset_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Bucket", []))

    @jsii.member(jsii_name="resetS3Key")
    def reset_s3_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Key", []))

    @jsii.member(jsii_name="resetS3ObjectVersion")
    def reset_s3_object_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3ObjectVersion", []))

    @jsii.member(jsii_name="resetSnapStart")
    def reset_snap_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapStart", []))

    @jsii.member(jsii_name="resetSourceCodeHash")
    def reset_source_code_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceCodeHash", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTracingConfig")
    def reset_tracing_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTracingConfig", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

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
    @jsii.member(jsii_name="deadLetterConfig")
    def dead_letter_config(self) -> "LambdaFunctionDeadLetterConfigOutputReference":
        return typing.cast("LambdaFunctionDeadLetterConfigOutputReference", jsii.get(self, "deadLetterConfig"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> "LambdaFunctionEnvironmentOutputReference":
        return typing.cast("LambdaFunctionEnvironmentOutputReference", jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorage")
    def ephemeral_storage(self) -> "LambdaFunctionEphemeralStorageOutputReference":
        return typing.cast("LambdaFunctionEphemeralStorageOutputReference", jsii.get(self, "ephemeralStorage"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemConfig")
    def file_system_config(self) -> "LambdaFunctionFileSystemConfigOutputReference":
        return typing.cast("LambdaFunctionFileSystemConfigOutputReference", jsii.get(self, "fileSystemConfig"))

    @builtins.property
    @jsii.member(jsii_name="imageConfig")
    def image_config(self) -> "LambdaFunctionImageConfigOutputReference":
        return typing.cast("LambdaFunctionImageConfigOutputReference", jsii.get(self, "imageConfig"))

    @builtins.property
    @jsii.member(jsii_name="invokeArn")
    def invoke_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invokeArn"))

    @builtins.property
    @jsii.member(jsii_name="lastModified")
    def last_modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModified"))

    @builtins.property
    @jsii.member(jsii_name="qualifiedArn")
    def qualified_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifiedArn"))

    @builtins.property
    @jsii.member(jsii_name="qualifiedInvokeArn")
    def qualified_invoke_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifiedInvokeArn"))

    @builtins.property
    @jsii.member(jsii_name="signingJobArn")
    def signing_job_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingJobArn"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingProfileVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="snapStart")
    def snap_start(self) -> "LambdaFunctionSnapStartOutputReference":
        return typing.cast("LambdaFunctionSnapStartOutputReference", jsii.get(self, "snapStart"))

    @builtins.property
    @jsii.member(jsii_name="sourceCodeSize")
    def source_code_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sourceCodeSize"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LambdaFunctionTimeoutsOutputReference":
        return typing.cast("LambdaFunctionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tracingConfig")
    def tracing_config(self) -> "LambdaFunctionTracingConfigOutputReference":
        return typing.cast("LambdaFunctionTracingConfigOutputReference", jsii.get(self, "tracingConfig"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "LambdaFunctionVpcConfigOutputReference":
        return typing.cast("LambdaFunctionVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="architecturesInput")
    def architectures_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "architecturesInput"))

    @builtins.property
    @jsii.member(jsii_name="codeSigningConfigArnInput")
    def code_signing_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeSigningConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterConfigInput")
    def dead_letter_config_input(
        self,
    ) -> typing.Optional["LambdaFunctionDeadLetterConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionDeadLetterConfig"], jsii.get(self, "deadLetterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional["LambdaFunctionEnvironment"]:
        return typing.cast(typing.Optional["LambdaFunctionEnvironment"], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorageInput")
    def ephemeral_storage_input(
        self,
    ) -> typing.Optional["LambdaFunctionEphemeralStorage"]:
        return typing.cast(typing.Optional["LambdaFunctionEphemeralStorage"], jsii.get(self, "ephemeralStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemConfigInput")
    def file_system_config_input(
        self,
    ) -> typing.Optional["LambdaFunctionFileSystemConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionFileSystemConfig"], jsii.get(self, "fileSystemConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="handlerInput")
    def handler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handlerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageConfigInput")
    def image_config_input(self) -> typing.Optional["LambdaFunctionImageConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionImageConfig"], jsii.get(self, "imageConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUriInput")
    def image_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageUriInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="layersInput")
    def layers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "layersInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySizeInput")
    def memory_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="packageTypeInput")
    def package_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="publishInput")
    def publish_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publishInput"))

    @builtins.property
    @jsii.member(jsii_name="reservedConcurrentExecutionsInput")
    def reserved_concurrent_executions_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "reservedConcurrentExecutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInput")
    def s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KeyInput")
    def s3_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ObjectVersionInput")
    def s3_object_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3ObjectVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="snapStartInput")
    def snap_start_input(self) -> typing.Optional["LambdaFunctionSnapStart"]:
        return typing.cast(typing.Optional["LambdaFunctionSnapStart"], jsii.get(self, "snapStartInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceCodeHashInput")
    def source_code_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceCodeHashInput"))

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
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LambdaFunctionTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LambdaFunctionTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tracingConfigInput")
    def tracing_config_input(self) -> typing.Optional["LambdaFunctionTracingConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionTracingConfig"], jsii.get(self, "tracingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(self) -> typing.Optional["LambdaFunctionVpcConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="architectures")
    def architectures(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "architectures"))

    @architectures.setter
    def architectures(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63543529e349979e0963377256b9720891360de43911bce9b517fcc2b07f860a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architectures", value)

    @builtins.property
    @jsii.member(jsii_name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codeSigningConfigArn"))

    @code_signing_config_arn.setter
    def code_signing_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c15b08ae843303ddff2b43e7d467cc7c33b2fb849245a8a86d3931b9133a222)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeSigningConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34fd6e75fc82ab8e4d25cc2bb7a5568e4bb6c053f43dc00094291278e63c1e17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec21eb36af74f92385d306af75b8843eee04e5afc5264dc21cb31ce8a010cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07158e9d2e48dabfd324b552eb3b5d42450f9d0f237f2f55250642bdc5d0ef34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handler"))

    @handler.setter
    def handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee70d7918e4264e7f698fd82be02f25c253406161c89d2c6c4bb4d1a9de1534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handler", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb187e7b44ad1a74ad5b1f9d6071dee114cf08996379e91449aea616888e8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4520060f52def529f95eaeaf407ba22e6934fcab735f50136ae7f359e474a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b258409c89a570828bb9a57fd614a8b78e069a26c8771f97fdf59c24c1e26649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="layers")
    def layers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "layers"))

    @layers.setter
    def layers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a2e30739f8f1f9095ba0ad98b583381f726aeb9128a2cb1e1160dd9fa3b4213)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layers", value)

    @builtins.property
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySize"))

    @memory_size.setter
    def memory_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb95ca4b6ca45cc176f8131a7d7d8b0c6aa55c20f832988b8c7ea7e0bc4ec529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySize", value)

    @builtins.property
    @jsii.member(jsii_name="packageType")
    def package_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packageType"))

    @package_type.setter
    def package_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974e8fb8c773fa729d62d5eb8b3f67faa0f3b86d2272b31f89928dd77027914c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageType", value)

    @builtins.property
    @jsii.member(jsii_name="publish")
    def publish(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publish"))

    @publish.setter
    def publish(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb372e8a09dc97f274d6c9ca345bbd013cd8a077f4da99349fca29e6a707968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publish", value)

    @builtins.property
    @jsii.member(jsii_name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "reservedConcurrentExecutions"))

    @reserved_concurrent_executions.setter
    def reserved_concurrent_executions(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece622038c59ebffb3dc126b4c0e57aa2858881425d5637f10de9ba9614bc86c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reservedConcurrentExecutions", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3b114bcc9528693be137c61cebfa42a7324b4c0abc693ccf1adb3c8bfed63c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e00502e67fc36642b87bc1a05257676108f7dc7aef5f0e36268842f63c09e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c436b059a8824e779c5f9c0f9f87bbfd03f0ea8fa61bf432e1366bbfde73251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="s3Key")
    def s3_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Key"))

    @s3_key.setter
    def s3_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d68624289d7a2b4e43ad9eda01bc01a59e08082cf02aed5257bfd5e2064aa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Key", value)

    @builtins.property
    @jsii.member(jsii_name="s3ObjectVersion")
    def s3_object_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3ObjectVersion"))

    @s3_object_version.setter
    def s3_object_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__755fa40d815b764877830dc70f098dbf02790afc4a9cb614f4a00d1792065900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sourceCodeHash")
    def source_code_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceCodeHash"))

    @source_code_hash.setter
    def source_code_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a913da00dc3ecdee9ed45ec147e6bd0c4fe1ea1eb7ab1057e3e78a96ca7314)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceCodeHash", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfa8455178a4adde2eb849debdd4a590754c78e2f3f5ce8f7b6f02c240eaa111)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4c2c4f3ed0b2e3e02cc9134ec2019ea1ccce93ba5335be8b71bb6ae4d9ab72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__052c6e838524afa8a7db536d8460a838efbe09bc1469cdf0df636315471ea661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "function_name": "functionName",
        "role": "role",
        "architectures": "architectures",
        "code_signing_config_arn": "codeSigningConfigArn",
        "dead_letter_config": "deadLetterConfig",
        "description": "description",
        "environment": "environment",
        "ephemeral_storage": "ephemeralStorage",
        "filename": "filename",
        "file_system_config": "fileSystemConfig",
        "handler": "handler",
        "id": "id",
        "image_config": "imageConfig",
        "image_uri": "imageUri",
        "kms_key_arn": "kmsKeyArn",
        "layers": "layers",
        "memory_size": "memorySize",
        "package_type": "packageType",
        "publish": "publish",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "runtime": "runtime",
        "s3_bucket": "s3Bucket",
        "s3_key": "s3Key",
        "s3_object_version": "s3ObjectVersion",
        "snap_start": "snapStart",
        "source_code_hash": "sourceCodeHash",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeout": "timeout",
        "timeouts": "timeouts",
        "tracing_config": "tracingConfig",
        "vpc_config": "vpcConfig",
    },
)
class LambdaFunctionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        function_name: builtins.str,
        role: builtins.str,
        architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
        code_signing_config_arn: typing.Optional[builtins.str] = None,
        dead_letter_config: typing.Optional[typing.Union["LambdaFunctionDeadLetterConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Union["LambdaFunctionEnvironment", typing.Dict[builtins.str, typing.Any]]] = None,
        ephemeral_storage: typing.Optional[typing.Union["LambdaFunctionEphemeralStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        filename: typing.Optional[builtins.str] = None,
        file_system_config: typing.Optional[typing.Union["LambdaFunctionFileSystemConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        handler: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_config: typing.Optional[typing.Union["LambdaFunctionImageConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        layers: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        package_type: typing.Optional[builtins.str] = None,
        publish: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        runtime: typing.Optional[builtins.str] = None,
        s3_bucket: typing.Optional[builtins.str] = None,
        s3_key: typing.Optional[builtins.str] = None,
        s3_object_version: typing.Optional[builtins.str] = None,
        snap_start: typing.Optional[typing.Union["LambdaFunctionSnapStart", typing.Dict[builtins.str, typing.Any]]] = None,
        source_code_hash: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["LambdaFunctionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        tracing_config: typing.Optional[typing.Union["LambdaFunctionTracingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_config: typing.Optional[typing.Union["LambdaFunctionVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#function_name LambdaFunction#function_name}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#role LambdaFunction#role}.
        :param architectures: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#architectures LambdaFunction#architectures}.
        :param code_signing_config_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#code_signing_config_arn LambdaFunction#code_signing_config_arn}.
        :param dead_letter_config: dead_letter_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#dead_letter_config LambdaFunction#dead_letter_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#description LambdaFunction#description}.
        :param environment: environment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#environment LambdaFunction#environment}
        :param ephemeral_storage: ephemeral_storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#ephemeral_storage LambdaFunction#ephemeral_storage}
        :param filename: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#filename LambdaFunction#filename}.
        :param file_system_config: file_system_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#file_system_config LambdaFunction#file_system_config}
        :param handler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#handler LambdaFunction#handler}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#id LambdaFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_config: image_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#image_config LambdaFunction#image_config}
        :param image_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#image_uri LambdaFunction#image_uri}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#kms_key_arn LambdaFunction#kms_key_arn}.
        :param layers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#layers LambdaFunction#layers}.
        :param memory_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#memory_size LambdaFunction#memory_size}.
        :param package_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#package_type LambdaFunction#package_type}.
        :param publish: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#publish LambdaFunction#publish}.
        :param reserved_concurrent_executions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#reserved_concurrent_executions LambdaFunction#reserved_concurrent_executions}.
        :param runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#runtime LambdaFunction#runtime}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_bucket LambdaFunction#s3_bucket}.
        :param s3_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_key LambdaFunction#s3_key}.
        :param s3_object_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_object_version LambdaFunction#s3_object_version}.
        :param snap_start: snap_start block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#snap_start LambdaFunction#snap_start}
        :param source_code_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#source_code_hash LambdaFunction#source_code_hash}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tags LambdaFunction#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tags_all LambdaFunction#tags_all}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#timeout LambdaFunction#timeout}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#timeouts LambdaFunction#timeouts}
        :param tracing_config: tracing_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tracing_config LambdaFunction#tracing_config}
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#vpc_config LambdaFunction#vpc_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dead_letter_config, dict):
            dead_letter_config = LambdaFunctionDeadLetterConfig(**dead_letter_config)
        if isinstance(environment, dict):
            environment = LambdaFunctionEnvironment(**environment)
        if isinstance(ephemeral_storage, dict):
            ephemeral_storage = LambdaFunctionEphemeralStorage(**ephemeral_storage)
        if isinstance(file_system_config, dict):
            file_system_config = LambdaFunctionFileSystemConfig(**file_system_config)
        if isinstance(image_config, dict):
            image_config = LambdaFunctionImageConfig(**image_config)
        if isinstance(snap_start, dict):
            snap_start = LambdaFunctionSnapStart(**snap_start)
        if isinstance(timeouts, dict):
            timeouts = LambdaFunctionTimeouts(**timeouts)
        if isinstance(tracing_config, dict):
            tracing_config = LambdaFunctionTracingConfig(**tracing_config)
        if isinstance(vpc_config, dict):
            vpc_config = LambdaFunctionVpcConfig(**vpc_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93eeb11a2e95389f34a16ae935b7581a58a44bb9505031aba880658e39dd8f9d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument architectures", value=architectures, expected_type=type_hints["architectures"])
            check_type(argname="argument code_signing_config_arn", value=code_signing_config_arn, expected_type=type_hints["code_signing_config_arn"])
            check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument file_system_config", value=file_system_config, expected_type=type_hints["file_system_config"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_config", value=image_config, expected_type=type_hints["image_config"])
            check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument package_type", value=package_type, expected_type=type_hints["package_type"])
            check_type(argname="argument publish", value=publish, expected_type=type_hints["publish"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
            check_type(argname="argument snap_start", value=snap_start, expected_type=type_hints["snap_start"])
            check_type(argname="argument source_code_hash", value=source_code_hash, expected_type=type_hints["source_code_hash"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument tracing_config", value=tracing_config, expected_type=type_hints["tracing_config"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_name": function_name,
            "role": role,
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
        if architectures is not None:
            self._values["architectures"] = architectures
        if code_signing_config_arn is not None:
            self._values["code_signing_config_arn"] = code_signing_config_arn
        if dead_letter_config is not None:
            self._values["dead_letter_config"] = dead_letter_config
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if ephemeral_storage is not None:
            self._values["ephemeral_storage"] = ephemeral_storage
        if filename is not None:
            self._values["filename"] = filename
        if file_system_config is not None:
            self._values["file_system_config"] = file_system_config
        if handler is not None:
            self._values["handler"] = handler
        if id is not None:
            self._values["id"] = id
        if image_config is not None:
            self._values["image_config"] = image_config
        if image_uri is not None:
            self._values["image_uri"] = image_uri
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if layers is not None:
            self._values["layers"] = layers
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if package_type is not None:
            self._values["package_type"] = package_type
        if publish is not None:
            self._values["publish"] = publish
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if runtime is not None:
            self._values["runtime"] = runtime
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket
        if s3_key is not None:
            self._values["s3_key"] = s3_key
        if s3_object_version is not None:
            self._values["s3_object_version"] = s3_object_version
        if snap_start is not None:
            self._values["snap_start"] = snap_start
        if source_code_hash is not None:
            self._values["source_code_hash"] = source_code_hash
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeout is not None:
            self._values["timeout"] = timeout
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if tracing_config is not None:
            self._values["tracing_config"] = tracing_config
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

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
    def function_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#function_name LambdaFunction#function_name}.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#role LambdaFunction#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architectures(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#architectures LambdaFunction#architectures}.'''
        result = self._values.get("architectures")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def code_signing_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#code_signing_config_arn LambdaFunction#code_signing_config_arn}.'''
        result = self._values.get("code_signing_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dead_letter_config(self) -> typing.Optional["LambdaFunctionDeadLetterConfig"]:
        '''dead_letter_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#dead_letter_config LambdaFunction#dead_letter_config}
        '''
        result = self._values.get("dead_letter_config")
        return typing.cast(typing.Optional["LambdaFunctionDeadLetterConfig"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#description LambdaFunction#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional["LambdaFunctionEnvironment"]:
        '''environment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#environment LambdaFunction#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional["LambdaFunctionEnvironment"], result)

    @builtins.property
    def ephemeral_storage(self) -> typing.Optional["LambdaFunctionEphemeralStorage"]:
        '''ephemeral_storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#ephemeral_storage LambdaFunction#ephemeral_storage}
        '''
        result = self._values.get("ephemeral_storage")
        return typing.cast(typing.Optional["LambdaFunctionEphemeralStorage"], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#filename LambdaFunction#filename}.'''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_config(self) -> typing.Optional["LambdaFunctionFileSystemConfig"]:
        '''file_system_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#file_system_config LambdaFunction#file_system_config}
        '''
        result = self._values.get("file_system_config")
        return typing.cast(typing.Optional["LambdaFunctionFileSystemConfig"], result)

    @builtins.property
    def handler(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#handler LambdaFunction#handler}.'''
        result = self._values.get("handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#id LambdaFunction#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_config(self) -> typing.Optional["LambdaFunctionImageConfig"]:
        '''image_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#image_config LambdaFunction#image_config}
        '''
        result = self._values.get("image_config")
        return typing.cast(typing.Optional["LambdaFunctionImageConfig"], result)

    @builtins.property
    def image_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#image_uri LambdaFunction#image_uri}.'''
        result = self._values.get("image_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#kms_key_arn LambdaFunction#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#layers LambdaFunction#layers}.'''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#memory_size LambdaFunction#memory_size}.'''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def package_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#package_type LambdaFunction#package_type}.'''
        result = self._values.get("package_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#publish LambdaFunction#publish}.'''
        result = self._values.get("publish")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#reserved_concurrent_executions LambdaFunction#reserved_concurrent_executions}.'''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#runtime LambdaFunction#runtime}.'''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_bucket LambdaFunction#s3_bucket}.'''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_key LambdaFunction#s3_key}.'''
        result = self._values.get("s3_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_object_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#s3_object_version LambdaFunction#s3_object_version}.'''
        result = self._values.get("s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snap_start(self) -> typing.Optional["LambdaFunctionSnapStart"]:
        '''snap_start block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#snap_start LambdaFunction#snap_start}
        '''
        result = self._values.get("snap_start")
        return typing.cast(typing.Optional["LambdaFunctionSnapStart"], result)

    @builtins.property
    def source_code_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#source_code_hash LambdaFunction#source_code_hash}.'''
        result = self._values.get("source_code_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tags LambdaFunction#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tags_all LambdaFunction#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#timeout LambdaFunction#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LambdaFunctionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#timeouts LambdaFunction#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LambdaFunctionTimeouts"], result)

    @builtins.property
    def tracing_config(self) -> typing.Optional["LambdaFunctionTracingConfig"]:
        '''tracing_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#tracing_config LambdaFunction#tracing_config}
        '''
        result = self._values.get("tracing_config")
        return typing.cast(typing.Optional["LambdaFunctionTracingConfig"], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["LambdaFunctionVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#vpc_config LambdaFunction#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["LambdaFunctionVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionDeadLetterConfig",
    jsii_struct_bases=[],
    name_mapping={"target_arn": "targetArn"},
)
class LambdaFunctionDeadLetterConfig:
    def __init__(self, *, target_arn: builtins.str) -> None:
        '''
        :param target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#target_arn LambdaFunction#target_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f1fe1fbd2a008b33d9aae0637538fa5a3d69044f851e66e546fa26266837a7)
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_arn": target_arn,
        }

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#target_arn LambdaFunction#target_arn}.'''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionDeadLetterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionDeadLetterConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionDeadLetterConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3436ea7f76719ccdc895c052a400e4de3f59db6727aa9b442e4e658851600be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="targetArnInput")
    def target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd1fc499239ad91741db20423f7a09f8dca6e6f45ed79229c7ce3d1b13068cac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionDeadLetterConfig]:
        return typing.cast(typing.Optional[LambdaFunctionDeadLetterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionDeadLetterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc14eb1149e41945a2260c41b6ae5744209a4f00c8ae1ad937b564089c1aaaad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionEnvironment",
    jsii_struct_bases=[],
    name_mapping={"variables": "variables"},
)
class LambdaFunctionEnvironment:
    def __init__(
        self,
        *,
        variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#variables LambdaFunction#variables}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de64c8c8375a8430afda850071780134cd6ff51324f96055a8c3feb0f2083433)
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def variables(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#variables LambdaFunction#variables}.'''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionEnvironmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionEnvironmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87b334faa48761c92a43822aa0a85ca72f1ae17663faebc3ac5801692ee82a08)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetVariables")
    def reset_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariables", []))

    @builtins.property
    @jsii.member(jsii_name="variablesInput")
    def variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "variablesInput"))

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "variables"))

    @variables.setter
    def variables(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1a6e071bede031cdfe7597efdefe1748f877d577264e9d994fe918e8c5fb2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionEnvironment]:
        return typing.cast(typing.Optional[LambdaFunctionEnvironment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LambdaFunctionEnvironment]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a22c237f7cba7828d08f1af166aed9ff504a3a94dd4f1af27624e846406e118d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionEphemeralStorage",
    jsii_struct_bases=[],
    name_mapping={"size": "size"},
)
class LambdaFunctionEphemeralStorage:
    def __init__(self, *, size: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#size LambdaFunction#size}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0cad70fe7d9ab8d39e583de048b64e5b94f8bb899cf2ee696f0eb460f74d42)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if size is not None:
            self._values["size"] = size

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#size LambdaFunction#size}.'''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEphemeralStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionEphemeralStorageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionEphemeralStorageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__165d9ce1eb20ebd6a01e10b0ce67863d5e6c26668679afd2aa908cae05d6c36c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8af0895615ba98e007206090422795bb40bca4720321726ff550831042868c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionEphemeralStorage]:
        return typing.cast(typing.Optional[LambdaFunctionEphemeralStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEphemeralStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84254bc5972ce7f89eb5132427b0b2c6bf5b711553d0dd132999e811a930a368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionFileSystemConfig",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "local_mount_path": "localMountPath"},
)
class LambdaFunctionFileSystemConfig:
    def __init__(self, *, arn: builtins.str, local_mount_path: builtins.str) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#arn LambdaFunction#arn}.
        :param local_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#local_mount_path LambdaFunction#local_mount_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0694596fca940b2f662812cbf9c1fdd944a0ffac99ad49d533e2bfb23bdc03e3)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument local_mount_path", value=local_mount_path, expected_type=type_hints["local_mount_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "local_mount_path": local_mount_path,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#arn LambdaFunction#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def local_mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#local_mount_path LambdaFunction#local_mount_path}.'''
        result = self._values.get("local_mount_path")
        assert result is not None, "Required property 'local_mount_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionFileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionFileSystemConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionFileSystemConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2387e6c3407ae439e8431d1d6357433419fb458e5b1b6ebb1ef7439075eee27a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="localMountPathInput")
    def local_mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localMountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575df02ed238a33f74520fc977fffaa5ac06173400a79d9833e70a8c8cc054aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="localMountPath")
    def local_mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localMountPath"))

    @local_mount_path.setter
    def local_mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc41b6905d4b0040ede3d8bd572ebc6cdf08d6ababb5728c46cc359ecafebe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localMountPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionFileSystemConfig]:
        return typing.cast(typing.Optional[LambdaFunctionFileSystemConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionFileSystemConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e1c25dcd05c4d99c84f348f9c337946bc9f878ad57b82b88495535ae35622fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionImageConfig",
    jsii_struct_bases=[],
    name_mapping={
        "command": "command",
        "entry_point": "entryPoint",
        "working_directory": "workingDirectory",
    },
)
class LambdaFunctionImageConfig:
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#command LambdaFunction#command}.
        :param entry_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#entry_point LambdaFunction#entry_point}.
        :param working_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#working_directory LambdaFunction#working_directory}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e46b80178bfa0221e3b363dab0f02e65a30e14e2c39c3ea880168835a2364e)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command
        if entry_point is not None:
            self._values["entry_point"] = entry_point
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#command LambdaFunction#command}.'''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entry_point(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#entry_point LambdaFunction#entry_point}.'''
        result = self._values.get("entry_point")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#working_directory LambdaFunction#working_directory}.'''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionImageConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionImageConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d46801b94447d411d151c3d19838cb6029d2cafb22d586a064016c2da9eb01e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetEntryPoint")
    def reset_entry_point(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntryPoint", []))

    @jsii.member(jsii_name="resetWorkingDirectory")
    def reset_working_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkingDirectory", []))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="entryPointInput")
    def entry_point_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entryPointInput"))

    @builtins.property
    @jsii.member(jsii_name="workingDirectoryInput")
    def working_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "command"))

    @command.setter
    def command(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea01bd68c6ca994eece6676b15e5d861db38985010824604a4add80a331021a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value)

    @builtins.property
    @jsii.member(jsii_name="entryPoint")
    def entry_point(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entryPoint"))

    @entry_point.setter
    def entry_point(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd962b3cdc2f4b5d55927fcbdcfd2632b3124dc075ce5f89c1b11d8c6cd32f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entryPoint", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e82468d338c7394295a9f5492fad0d91408ca9984b998e96f0aed79bff414610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionImageConfig]:
        return typing.cast(typing.Optional[LambdaFunctionImageConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LambdaFunctionImageConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16acf5a3c33d866205fbd84f37ad1fa2e9fa8b6b5e0cb5a7f15bae198b513bfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionSnapStart",
    jsii_struct_bases=[],
    name_mapping={"apply_on": "applyOn"},
)
class LambdaFunctionSnapStart:
    def __init__(self, *, apply_on: builtins.str) -> None:
        '''
        :param apply_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#apply_on LambdaFunction#apply_on}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd568372dba3033fd3263e1d7c7dad60da54e52d337500c6f2cd29ba149acb0)
            check_type(argname="argument apply_on", value=apply_on, expected_type=type_hints["apply_on"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apply_on": apply_on,
        }

    @builtins.property
    def apply_on(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#apply_on LambdaFunction#apply_on}.'''
        result = self._values.get("apply_on")
        assert result is not None, "Required property 'apply_on' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionSnapStart(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionSnapStartOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionSnapStartOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22346947b5c07bd9ef702890181396d19a77f45c1ef4e51db0401068e46d0735)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="optimizationStatus")
    def optimization_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optimizationStatus"))

    @builtins.property
    @jsii.member(jsii_name="applyOnInput")
    def apply_on_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applyOnInput"))

    @builtins.property
    @jsii.member(jsii_name="applyOn")
    def apply_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applyOn"))

    @apply_on.setter
    def apply_on(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e25dc60d52369d99e71c36de73091892c2ef2e8f7e33cc8beea0a548a95a017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyOn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionSnapStart]:
        return typing.cast(typing.Optional[LambdaFunctionSnapStart], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LambdaFunctionSnapStart]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82da703098ceabf5d4c29ab473a6c771cf3faca93b525baf0da6cbbe6bf25e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class LambdaFunctionTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#create LambdaFunction#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f416190cfd1b501615d70975c9ec6c740c58846f26454129b47bdf7d375188)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#create LambdaFunction#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f15c094a6e0153f4f37dfa0af81488b56a3fb973f153f0304bbf15a1edaeaa7e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abcd3b2c10de0e5179f064a5e88ac73a012ef8b1ea827ff9bea67577c1bc422b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LambdaFunctionTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LambdaFunctionTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LambdaFunctionTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5bd9a9bb51b57c9cb0e7926eb00297d1003ab6c166257a007be4ee4017f695d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionTracingConfig",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class LambdaFunctionTracingConfig:
    def __init__(self, *, mode: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#mode LambdaFunction#mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9af23125c2609b313d714dfb9a31fc564d6d0e3034a91b98cc63f62b73d786)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mode": mode,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#mode LambdaFunction#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionTracingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionTracingConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionTracingConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f2f6d70d69e46786f1b80caf9efd112003c809daaa9b37a8e4906b842b90464)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f0fbaade9ef673f430ad5d3a8dc73e71d827ca30d11457a7eec1b95a9d8d45b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionTracingConfig]:
        return typing.cast(typing.Optional[LambdaFunctionTracingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionTracingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef36b3bf4d5c32e95f423f1dbb27787ce66e40614c6956b729dc9018a131faf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunction.LambdaFunctionVpcConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class LambdaFunctionVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#security_group_ids LambdaFunction#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#subnet_ids LambdaFunction#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eed62df7426e47832bb6c886a68d8cfdc961d12248ec292375043a55ef39bf3)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#security_group_ids LambdaFunction#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function#subnet_ids LambdaFunction#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionVpcConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunction.LambdaFunctionVpcConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__410a438a993d14da184d07e83202b0716faaeb867ea9a330e4b461140a7c1623)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__7231372fcf880a29c94dfb332452943471554b27ff72d1cc978671b2c54a3ec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f164f355eacce1fa0ff03eabb3165d8b4808f9f3ec46b3ede851455143705446)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LambdaFunctionVpcConfig]:
        return typing.cast(typing.Optional[LambdaFunctionVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LambdaFunctionVpcConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f00f6c32abfa3d9e43eaf99e4ed9018dfa4cacd3e70f4af85be5cea7086362)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LambdaFunction",
    "LambdaFunctionConfig",
    "LambdaFunctionDeadLetterConfig",
    "LambdaFunctionDeadLetterConfigOutputReference",
    "LambdaFunctionEnvironment",
    "LambdaFunctionEnvironmentOutputReference",
    "LambdaFunctionEphemeralStorage",
    "LambdaFunctionEphemeralStorageOutputReference",
    "LambdaFunctionFileSystemConfig",
    "LambdaFunctionFileSystemConfigOutputReference",
    "LambdaFunctionImageConfig",
    "LambdaFunctionImageConfigOutputReference",
    "LambdaFunctionSnapStart",
    "LambdaFunctionSnapStartOutputReference",
    "LambdaFunctionTimeouts",
    "LambdaFunctionTimeoutsOutputReference",
    "LambdaFunctionTracingConfig",
    "LambdaFunctionTracingConfigOutputReference",
    "LambdaFunctionVpcConfig",
    "LambdaFunctionVpcConfigOutputReference",
]

publication.publish()

def _typecheckingstub__955d0469461df7695e0ddad0f5cbd53ae32a3b40d5fa48a8fb68c3858bdf752f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    function_name: builtins.str,
    role: builtins.str,
    architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
    code_signing_config_arn: typing.Optional[builtins.str] = None,
    dead_letter_config: typing.Optional[typing.Union[LambdaFunctionDeadLetterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[LambdaFunctionEnvironment, typing.Dict[builtins.str, typing.Any]]] = None,
    ephemeral_storage: typing.Optional[typing.Union[LambdaFunctionEphemeralStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    filename: typing.Optional[builtins.str] = None,
    file_system_config: typing.Optional[typing.Union[LambdaFunctionFileSystemConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    handler: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    image_config: typing.Optional[typing.Union[LambdaFunctionImageConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    image_uri: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    layers: typing.Optional[typing.Sequence[builtins.str]] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    package_type: typing.Optional[builtins.str] = None,
    publish: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    runtime: typing.Optional[builtins.str] = None,
    s3_bucket: typing.Optional[builtins.str] = None,
    s3_key: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
    snap_start: typing.Optional[typing.Union[LambdaFunctionSnapStart, typing.Dict[builtins.str, typing.Any]]] = None,
    source_code_hash: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout: typing.Optional[jsii.Number] = None,
    timeouts: typing.Optional[typing.Union[LambdaFunctionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    tracing_config: typing.Optional[typing.Union[LambdaFunctionTracingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_config: typing.Optional[typing.Union[LambdaFunctionVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__63543529e349979e0963377256b9720891360de43911bce9b517fcc2b07f860a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c15b08ae843303ddff2b43e7d467cc7c33b2fb849245a8a86d3931b9133a222(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34fd6e75fc82ab8e4d25cc2bb7a5568e4bb6c053f43dc00094291278e63c1e17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec21eb36af74f92385d306af75b8843eee04e5afc5264dc21cb31ce8a010cba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07158e9d2e48dabfd324b552eb3b5d42450f9d0f237f2f55250642bdc5d0ef34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee70d7918e4264e7f698fd82be02f25c253406161c89d2c6c4bb4d1a9de1534(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb187e7b44ad1a74ad5b1f9d6071dee114cf08996379e91449aea616888e8c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4520060f52def529f95eaeaf407ba22e6934fcab735f50136ae7f359e474a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b258409c89a570828bb9a57fd614a8b78e069a26c8771f97fdf59c24c1e26649(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2e30739f8f1f9095ba0ad98b583381f726aeb9128a2cb1e1160dd9fa3b4213(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb95ca4b6ca45cc176f8131a7d7d8b0c6aa55c20f832988b8c7ea7e0bc4ec529(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974e8fb8c773fa729d62d5eb8b3f67faa0f3b86d2272b31f89928dd77027914c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb372e8a09dc97f274d6c9ca345bbd013cd8a077f4da99349fca29e6a707968(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece622038c59ebffb3dc126b4c0e57aa2858881425d5637f10de9ba9614bc86c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c3b114bcc9528693be137c61cebfa42a7324b4c0abc693ccf1adb3c8bfed63c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e00502e67fc36642b87bc1a05257676108f7dc7aef5f0e36268842f63c09e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c436b059a8824e779c5f9c0f9f87bbfd03f0ea8fa61bf432e1366bbfde73251(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d68624289d7a2b4e43ad9eda01bc01a59e08082cf02aed5257bfd5e2064aa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__755fa40d815b764877830dc70f098dbf02790afc4a9cb614f4a00d1792065900(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a913da00dc3ecdee9ed45ec147e6bd0c4fe1ea1eb7ab1057e3e78a96ca7314(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa8455178a4adde2eb849debdd4a590754c78e2f3f5ce8f7b6f02c240eaa111(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4c2c4f3ed0b2e3e02cc9134ec2019ea1ccce93ba5335be8b71bb6ae4d9ab72(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__052c6e838524afa8a7db536d8460a838efbe09bc1469cdf0df636315471ea661(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93eeb11a2e95389f34a16ae935b7581a58a44bb9505031aba880658e39dd8f9d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    function_name: builtins.str,
    role: builtins.str,
    architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
    code_signing_config_arn: typing.Optional[builtins.str] = None,
    dead_letter_config: typing.Optional[typing.Union[LambdaFunctionDeadLetterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[LambdaFunctionEnvironment, typing.Dict[builtins.str, typing.Any]]] = None,
    ephemeral_storage: typing.Optional[typing.Union[LambdaFunctionEphemeralStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    filename: typing.Optional[builtins.str] = None,
    file_system_config: typing.Optional[typing.Union[LambdaFunctionFileSystemConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    handler: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    image_config: typing.Optional[typing.Union[LambdaFunctionImageConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    image_uri: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    layers: typing.Optional[typing.Sequence[builtins.str]] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    package_type: typing.Optional[builtins.str] = None,
    publish: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    runtime: typing.Optional[builtins.str] = None,
    s3_bucket: typing.Optional[builtins.str] = None,
    s3_key: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
    snap_start: typing.Optional[typing.Union[LambdaFunctionSnapStart, typing.Dict[builtins.str, typing.Any]]] = None,
    source_code_hash: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout: typing.Optional[jsii.Number] = None,
    timeouts: typing.Optional[typing.Union[LambdaFunctionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    tracing_config: typing.Optional[typing.Union[LambdaFunctionTracingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_config: typing.Optional[typing.Union[LambdaFunctionVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f1fe1fbd2a008b33d9aae0637538fa5a3d69044f851e66e546fa26266837a7(
    *,
    target_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3436ea7f76719ccdc895c052a400e4de3f59db6727aa9b442e4e658851600be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1fc499239ad91741db20423f7a09f8dca6e6f45ed79229c7ce3d1b13068cac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc14eb1149e41945a2260c41b6ae5744209a4f00c8ae1ad937b564089c1aaaad(
    value: typing.Optional[LambdaFunctionDeadLetterConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de64c8c8375a8430afda850071780134cd6ff51324f96055a8c3feb0f2083433(
    *,
    variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87b334faa48761c92a43822aa0a85ca72f1ae17663faebc3ac5801692ee82a08(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1a6e071bede031cdfe7597efdefe1748f877d577264e9d994fe918e8c5fb2c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a22c237f7cba7828d08f1af166aed9ff504a3a94dd4f1af27624e846406e118d(
    value: typing.Optional[LambdaFunctionEnvironment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0cad70fe7d9ab8d39e583de048b64e5b94f8bb899cf2ee696f0eb460f74d42(
    *,
    size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165d9ce1eb20ebd6a01e10b0ce67863d5e6c26668679afd2aa908cae05d6c36c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8af0895615ba98e007206090422795bb40bca4720321726ff550831042868c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84254bc5972ce7f89eb5132427b0b2c6bf5b711553d0dd132999e811a930a368(
    value: typing.Optional[LambdaFunctionEphemeralStorage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0694596fca940b2f662812cbf9c1fdd944a0ffac99ad49d533e2bfb23bdc03e3(
    *,
    arn: builtins.str,
    local_mount_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2387e6c3407ae439e8431d1d6357433419fb458e5b1b6ebb1ef7439075eee27a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575df02ed238a33f74520fc977fffaa5ac06173400a79d9833e70a8c8cc054aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc41b6905d4b0040ede3d8bd572ebc6cdf08d6ababb5728c46cc359ecafebe9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1c25dcd05c4d99c84f348f9c337946bc9f878ad57b82b88495535ae35622fd(
    value: typing.Optional[LambdaFunctionFileSystemConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e46b80178bfa0221e3b363dab0f02e65a30e14e2c39c3ea880168835a2364e(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d46801b94447d411d151c3d19838cb6029d2cafb22d586a064016c2da9eb01e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea01bd68c6ca994eece6676b15e5d861db38985010824604a4add80a331021a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd962b3cdc2f4b5d55927fcbdcfd2632b3124dc075ce5f89c1b11d8c6cd32f4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e82468d338c7394295a9f5492fad0d91408ca9984b998e96f0aed79bff414610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16acf5a3c33d866205fbd84f37ad1fa2e9fa8b6b5e0cb5a7f15bae198b513bfe(
    value: typing.Optional[LambdaFunctionImageConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd568372dba3033fd3263e1d7c7dad60da54e52d337500c6f2cd29ba149acb0(
    *,
    apply_on: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22346947b5c07bd9ef702890181396d19a77f45c1ef4e51db0401068e46d0735(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e25dc60d52369d99e71c36de73091892c2ef2e8f7e33cc8beea0a548a95a017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82da703098ceabf5d4c29ab473a6c771cf3faca93b525baf0da6cbbe6bf25e67(
    value: typing.Optional[LambdaFunctionSnapStart],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f416190cfd1b501615d70975c9ec6c740c58846f26454129b47bdf7d375188(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f15c094a6e0153f4f37dfa0af81488b56a3fb973f153f0304bbf15a1edaeaa7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcd3b2c10de0e5179f064a5e88ac73a012ef8b1ea827ff9bea67577c1bc422b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5bd9a9bb51b57c9cb0e7926eb00297d1003ab6c166257a007be4ee4017f695d(
    value: typing.Optional[typing.Union[LambdaFunctionTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9af23125c2609b313d714dfb9a31fc564d6d0e3034a91b98cc63f62b73d786(
    *,
    mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f2f6d70d69e46786f1b80caf9efd112003c809daaa9b37a8e4906b842b90464(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0fbaade9ef673f430ad5d3a8dc73e71d827ca30d11457a7eec1b95a9d8d45b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef36b3bf4d5c32e95f423f1dbb27787ce66e40614c6956b729dc9018a131faf8(
    value: typing.Optional[LambdaFunctionTracingConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eed62df7426e47832bb6c886a68d8cfdc961d12248ec292375043a55ef39bf3(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__410a438a993d14da184d07e83202b0716faaeb867ea9a330e4b461140a7c1623(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7231372fcf880a29c94dfb332452943471554b27ff72d1cc978671b2c54a3ec5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f164f355eacce1fa0ff03eabb3165d8b4808f9f3ec46b3ede851455143705446(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f00f6c32abfa3d9e43eaf99e4ed9018dfa4cacd3e70f4af85be5cea7086362(
    value: typing.Optional[LambdaFunctionVpcConfig],
) -> None:
    """Type checking stubs"""
    pass
