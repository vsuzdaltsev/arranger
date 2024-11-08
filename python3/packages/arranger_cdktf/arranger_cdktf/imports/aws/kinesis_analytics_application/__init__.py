'''
# `aws_kinesis_analytics_application`

Refer to the Terraform Registory for docs: [`aws_kinesis_analytics_application`](https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application).
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


class KinesisAnalyticsApplication(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application aws_kinesis_analytics_application}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisAnalyticsApplicationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inputs: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputs", typing.Dict[builtins.str, typing.Any]]] = None,
        outputs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationOutputs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        reference_data_sources: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSources", typing.Dict[builtins.str, typing.Any]]] = None,
        start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application aws_kinesis_analytics_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#cloudwatch_logging_options KinesisAnalyticsApplication#cloudwatch_logging_options}
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#code KinesisAnalyticsApplication#code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#description KinesisAnalyticsApplication#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#id KinesisAnalyticsApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inputs: inputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#inputs KinesisAnalyticsApplication#inputs}
        :param outputs: outputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#outputs KinesisAnalyticsApplication#outputs}
        :param reference_data_sources: reference_data_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#reference_data_sources KinesisAnalyticsApplication#reference_data_sources}
        :param start_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#start_application KinesisAnalyticsApplication#start_application}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags KinesisAnalyticsApplication#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags_all KinesisAnalyticsApplication#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c4d169f90215ee16e423364bd59bf0ca6d860488279543f7875ecf8dd1350e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KinesisAnalyticsApplicationConfig(
            name=name,
            cloudwatch_logging_options=cloudwatch_logging_options,
            code=code,
            description=description,
            id=id,
            inputs=inputs,
            outputs=outputs,
            reference_data_sources=reference_data_sources,
            start_application=start_application,
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        log_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param log_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#log_stream_arn KinesisAnalyticsApplication#log_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationCloudwatchLoggingOptions(
            log_stream_arn=log_stream_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putInputs")
    def put_inputs(
        self,
        *,
        name_prefix: builtins.str,
        schema: typing.Union["KinesisAnalyticsApplicationInputsSchema", typing.Dict[builtins.str, typing.Any]],
        kinesis_firehose: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisStream", typing.Dict[builtins.str, typing.Any]]] = None,
        parallelism: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsParallelism", typing.Dict[builtins.str, typing.Any]]] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        starting_position_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsStartingPositionConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name_prefix KinesisAnalyticsApplication#name_prefix}.
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param kinesis_firehose: kinesis_firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        :param kinesis_stream: kinesis_stream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        :param parallelism: parallelism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#parallelism KinesisAnalyticsApplication#parallelism}
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#processing_configuration KinesisAnalyticsApplication#processing_configuration}
        :param starting_position_configuration: starting_position_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position_configuration KinesisAnalyticsApplication#starting_position_configuration}
        '''
        value = KinesisAnalyticsApplicationInputs(
            name_prefix=name_prefix,
            schema=schema,
            kinesis_firehose=kinesis_firehose,
            kinesis_stream=kinesis_stream,
            parallelism=parallelism,
            processing_configuration=processing_configuration,
            starting_position_configuration=starting_position_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putInputs", [value]))

    @jsii.member(jsii_name="putOutputs")
    def put_outputs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationOutputs", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec9dae807a912d52f32a8f034020789a3f57fbfdd1955d0548c44abd05877a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOutputs", [value]))

    @jsii.member(jsii_name="putReferenceDataSources")
    def put_reference_data_sources(
        self,
        *,
        s3: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesS3", typing.Dict[builtins.str, typing.Any]],
        schema: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchema", typing.Dict[builtins.str, typing.Any]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#s3 KinesisAnalyticsApplication#s3}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#table_name KinesisAnalyticsApplication#table_name}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSources(
            s3=s3, schema=schema, table_name=table_name
        )

        return typing.cast(None, jsii.invoke(self, "putReferenceDataSources", [value]))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInputs")
    def reset_inputs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputs", []))

    @jsii.member(jsii_name="resetOutputs")
    def reset_outputs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputs", []))

    @jsii.member(jsii_name="resetReferenceDataSources")
    def reset_reference_data_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReferenceDataSources", []))

    @jsii.member(jsii_name="resetStartApplication")
    def reset_start_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartApplication", []))

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
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> "KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference":
        return typing.cast("KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference", jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="createTimestamp")
    def create_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="inputs")
    def inputs(self) -> "KinesisAnalyticsApplicationInputsOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsOutputReference", jsii.get(self, "inputs"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdateTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(self) -> "KinesisAnalyticsApplicationOutputsList":
        return typing.cast("KinesisAnalyticsApplicationOutputsList", jsii.get(self, "outputs"))

    @builtins.property
    @jsii.member(jsii_name="referenceDataSources")
    def reference_data_sources(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesOutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesOutputReference", jsii.get(self, "referenceDataSources"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationCloudwatchLoggingOptions"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationCloudwatchLoggingOptions"], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputsInput")
    def inputs_input(self) -> typing.Optional["KinesisAnalyticsApplicationInputs"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputs"], jsii.get(self, "inputsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputsInput")
    def outputs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]], jsii.get(self, "outputsInput"))

    @builtins.property
    @jsii.member(jsii_name="referenceDataSourcesInput")
    def reference_data_sources_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"], jsii.get(self, "referenceDataSourcesInput"))

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
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e0ac5da14cce6e9bf99ad440d187cc6c73dca5809a1431dc3bb15a35f272c2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860aaaa40437b9cf5f9f0efbe9c254bd157646d819d81d2ee17d5dee682cf887)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee20b29f1449193b6efe05ac71f73e860b72e11035bf83d3437cacbf81a5adc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dedecac7f8c34b9630128981b6a5793ff69f178a2b72a23f5c42875af2196e74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__5a67dc06e4d47cf5217ab5e300f437a9e5f2c202fe069a5b75d3330d6cd149f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startApplication", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__121d80f39ac432e2364d22609dead0446deecc70c4f3f990562a57a19c040ac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__382801fb942abc3d965912abb41c8a94de093d4e03ae56ed550628761e46610e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={"log_stream_arn": "logStreamArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationCloudwatchLoggingOptions:
    def __init__(self, *, log_stream_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param log_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#log_stream_arn KinesisAnalyticsApplication#log_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__927bdf89054e35be7cec42dd8dcba6f3059ae0aa6ec2e121d6734c66042c2e99)
            check_type(argname="argument log_stream_arn", value=log_stream_arn, expected_type=type_hints["log_stream_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_stream_arn": log_stream_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def log_stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#log_stream_arn KinesisAnalyticsApplication#log_stream_arn}.'''
        result = self._values.get("log_stream_arn")
        assert result is not None, "Required property 'log_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__060bcf32279c66d8d6f4180a44a846f7157e3d1acc37a9e13a88bf2c39beadb2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="logStreamArnInput")
    def log_stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamArn")
    def log_stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamArn"))

    @log_stream_arn.setter
    def log_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c095520965bb3e27cbfecdff0205f576ff7381354a54444c253505e2c29d736)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a80ee488a6cee48e78260268770ac91b645c3ce07846684ec01ac25cda16957)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec60b94ecdb53bbc690ff6780332dfd3890e79c3925441645d1a40c49072dc65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationConfig",
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
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "code": "code",
        "description": "description",
        "id": "id",
        "inputs": "inputs",
        "outputs": "outputs",
        "reference_data_sources": "referenceDataSources",
        "start_application": "startApplication",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class KinesisAnalyticsApplicationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cloudwatch_logging_options: typing.Optional[typing.Union[KinesisAnalyticsApplicationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inputs: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputs", typing.Dict[builtins.str, typing.Any]]] = None,
        outputs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationOutputs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        reference_data_sources: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSources", typing.Dict[builtins.str, typing.Any]]] = None,
        start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#cloudwatch_logging_options KinesisAnalyticsApplication#cloudwatch_logging_options}
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#code KinesisAnalyticsApplication#code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#description KinesisAnalyticsApplication#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#id KinesisAnalyticsApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inputs: inputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#inputs KinesisAnalyticsApplication#inputs}
        :param outputs: outputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#outputs KinesisAnalyticsApplication#outputs}
        :param reference_data_sources: reference_data_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#reference_data_sources KinesisAnalyticsApplication#reference_data_sources}
        :param start_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#start_application KinesisAnalyticsApplication#start_application}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags KinesisAnalyticsApplication#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags_all KinesisAnalyticsApplication#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisAnalyticsApplicationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(inputs, dict):
            inputs = KinesisAnalyticsApplicationInputs(**inputs)
        if isinstance(reference_data_sources, dict):
            reference_data_sources = KinesisAnalyticsApplicationReferenceDataSources(**reference_data_sources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d532ce4dc5faf594a91e1466b7aad5a50eff19540fa1abe37a903a65ac0a0a3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inputs", value=inputs, expected_type=type_hints["inputs"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument reference_data_sources", value=reference_data_sources, expected_type=type_hints["reference_data_sources"])
            check_type(argname="argument start_application", value=start_application, expected_type=type_hints["start_application"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if code is not None:
            self._values["code"] = code
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if inputs is not None:
            self._values["inputs"] = inputs
        if outputs is not None:
            self._values["outputs"] = outputs
        if reference_data_sources is not None:
            self._values["reference_data_sources"] = reference_data_sources
        if start_application is not None:
            self._values["start_application"] = start_application
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#cloudwatch_logging_options KinesisAnalyticsApplication#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions], result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#code KinesisAnalyticsApplication#code}.'''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#description KinesisAnalyticsApplication#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#id KinesisAnalyticsApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inputs(self) -> typing.Optional["KinesisAnalyticsApplicationInputs"]:
        '''inputs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#inputs KinesisAnalyticsApplication#inputs}
        '''
        result = self._values.get("inputs")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputs"], result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]]:
        '''outputs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#outputs KinesisAnalyticsApplication#outputs}
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]], result)

    @builtins.property
    def reference_data_sources(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"]:
        '''reference_data_sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#reference_data_sources KinesisAnalyticsApplication#reference_data_sources}
        '''
        result = self._values.get("reference_data_sources")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"], result)

    @builtins.property
    def start_application(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#start_application KinesisAnalyticsApplication#start_application}.'''
        result = self._values.get("start_application")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags KinesisAnalyticsApplication#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags_all KinesisAnalyticsApplication#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputs",
    jsii_struct_bases=[],
    name_mapping={
        "name_prefix": "namePrefix",
        "schema": "schema",
        "kinesis_firehose": "kinesisFirehose",
        "kinesis_stream": "kinesisStream",
        "parallelism": "parallelism",
        "processing_configuration": "processingConfiguration",
        "starting_position_configuration": "startingPositionConfiguration",
    },
)
class KinesisAnalyticsApplicationInputs:
    def __init__(
        self,
        *,
        name_prefix: builtins.str,
        schema: typing.Union["KinesisAnalyticsApplicationInputsSchema", typing.Dict[builtins.str, typing.Any]],
        kinesis_firehose: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisStream", typing.Dict[builtins.str, typing.Any]]] = None,
        parallelism: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsParallelism", typing.Dict[builtins.str, typing.Any]]] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        starting_position_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsStartingPositionConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name_prefix KinesisAnalyticsApplication#name_prefix}.
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param kinesis_firehose: kinesis_firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        :param kinesis_stream: kinesis_stream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        :param parallelism: parallelism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#parallelism KinesisAnalyticsApplication#parallelism}
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#processing_configuration KinesisAnalyticsApplication#processing_configuration}
        :param starting_position_configuration: starting_position_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position_configuration KinesisAnalyticsApplication#starting_position_configuration}
        '''
        if isinstance(schema, dict):
            schema = KinesisAnalyticsApplicationInputsSchema(**schema)
        if isinstance(kinesis_firehose, dict):
            kinesis_firehose = KinesisAnalyticsApplicationInputsKinesisFirehose(**kinesis_firehose)
        if isinstance(kinesis_stream, dict):
            kinesis_stream = KinesisAnalyticsApplicationInputsKinesisStream(**kinesis_stream)
        if isinstance(parallelism, dict):
            parallelism = KinesisAnalyticsApplicationInputsParallelism(**parallelism)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisAnalyticsApplicationInputsProcessingConfiguration(**processing_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a404a7ed187fae99b53ceb70ed37684b3544347b53e2b5cb7309e698cc9dda1e)
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument kinesis_firehose", value=kinesis_firehose, expected_type=type_hints["kinesis_firehose"])
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument starting_position_configuration", value=starting_position_configuration, expected_type=type_hints["starting_position_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name_prefix": name_prefix,
            "schema": schema,
        }
        if kinesis_firehose is not None:
            self._values["kinesis_firehose"] = kinesis_firehose
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if parallelism is not None:
            self._values["parallelism"] = parallelism
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if starting_position_configuration is not None:
            self._values["starting_position_configuration"] = starting_position_configuration

    @builtins.property
    def name_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name_prefix KinesisAnalyticsApplication#name_prefix}.'''
        result = self._values.get("name_prefix")
        assert result is not None, "Required property 'name_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> "KinesisAnalyticsApplicationInputsSchema":
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("KinesisAnalyticsApplicationInputsSchema", result)

    @builtins.property
    def kinesis_firehose(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsKinesisFirehose"]:
        '''kinesis_firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        '''
        result = self._values.get("kinesis_firehose")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsKinesisFirehose"], result)

    @builtins.property
    def kinesis_stream(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsKinesisStream"]:
        '''kinesis_stream block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsKinesisStream"], result)

    @builtins.property
    def parallelism(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsParallelism"]:
        '''parallelism block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#parallelism KinesisAnalyticsApplication#parallelism}
        '''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsParallelism"], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#processing_configuration KinesisAnalyticsApplication#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"], result)

    @builtins.property
    def starting_position_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]]:
        '''starting_position_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position_configuration KinesisAnalyticsApplication#starting_position_configuration}
        '''
        result = self._values.get("starting_position_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisFirehose",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationInputsKinesisFirehose:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b228af0e114461db543dbb6c9cb975e97317d452e096b6255c3a3e6222390d1d)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsKinesisFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03aa8464d368ee908e78db3a3a45baefe314ac38b4ff5ed201395b91631e9357)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2edd6ae72f3516c7b408d629819f47da4512901f332412f6d2ce056563940598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c567b0845cb8654c83c7d8f3c03f4da960eff65466c8b8c0651cf9522fdc41b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e5ad4f85b7e719de6e3fcd9761dbdf135030ffb16a22626c99b1cc9aa1d52fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationInputsKinesisStream:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90460791b1d636ee064f692d310a202ca69d996971a8cb4d0264d613e038ea13)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsKinesisStreamOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisStreamOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aaccdfa4f4a2f40c17b8b64093e1c73015819c1ace02312d783f7e6d5e6c7622)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3b0c46ddb20129b9cffc547285b203b6abec55fd719a587fc3b8fff1501a1e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1085ab6d886077cae672bf8dd0462efa40a4da6a83cb86b41eefd561e6bcedf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cbd49286544b57bc916e7b16752ce56431249ce292d571361be2107a7963614)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__452ede47079b00344df316b7b12837a99ff5233292dd8e29d9fb82ea1adc015a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKinesisFirehose")
    def put_kinesis_firehose(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationInputsKinesisFirehose(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehose", [value]))

    @jsii.member(jsii_name="putKinesisStream")
    def put_kinesis_stream(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationInputsKinesisStream(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStream", [value]))

    @jsii.member(jsii_name="putParallelism")
    def put_parallelism(self, *, count: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#count KinesisAnalyticsApplication#count}.
        '''
        value = KinesisAnalyticsApplicationInputsParallelism(count=count)

        return typing.cast(None, jsii.invoke(self, "putParallelism", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        lambda_: typing.Union["KinesisAnalyticsApplicationInputsProcessingConfigurationLambda", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        value = KinesisAnalyticsApplicationInputsProcessingConfiguration(
            lambda_=lambda_
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(
        self,
        *,
        record_columns: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordColumns", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        value = KinesisAnalyticsApplicationInputsSchema(
            record_columns=record_columns,
            record_format=record_format,
            record_encoding=record_encoding,
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @jsii.member(jsii_name="putStartingPositionConfiguration")
    def put_starting_position_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsStartingPositionConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b2304a2e34a8cd42471d81663635b506a1473b5c972657e211c85d2390028c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStartingPositionConfiguration", [value]))

    @jsii.member(jsii_name="resetKinesisFirehose")
    def reset_kinesis_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehose", []))

    @jsii.member(jsii_name="resetKinesisStream")
    def reset_kinesis_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStream", []))

    @jsii.member(jsii_name="resetParallelism")
    def reset_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelism", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetStartingPositionConfiguration")
    def reset_starting_position_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartingPositionConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference, jsii.get(self, "kinesisFirehose"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStream")
    def kinesis_stream(
        self,
    ) -> KinesisAnalyticsApplicationInputsKinesisStreamOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsKinesisStreamOutputReference, jsii.get(self, "kinesisStream"))

    @builtins.property
    @jsii.member(jsii_name="parallelism")
    def parallelism(
        self,
    ) -> "KinesisAnalyticsApplicationInputsParallelismOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsParallelismOutputReference", jsii.get(self, "parallelism"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "KinesisAnalyticsApplicationInputsSchemaOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="startingPositionConfiguration")
    def starting_position_configuration(
        self,
    ) -> "KinesisAnalyticsApplicationInputsStartingPositionConfigurationList":
        return typing.cast("KinesisAnalyticsApplicationInputsStartingPositionConfigurationList", jsii.get(self, "startingPositionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="streamNames")
    def stream_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streamNames"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseInput")
    def kinesis_firehose_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose], jsii.get(self, "kinesisFirehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamInput")
    def kinesis_stream_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream], jsii.get(self, "kinesisStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismInput")
    def parallelism_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsParallelism"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsParallelism"], jsii.get(self, "parallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchema"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchema"], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="startingPositionConfigurationInput")
    def starting_position_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]], jsii.get(self, "startingPositionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efff2951628acc1079a6928ab9693c8709f08ead7f47527702b27603a655e3c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KinesisAnalyticsApplicationInputs]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca85d9713583eb1fcd9f20c7be26475e1963a9b3f73cfd8727c5762edb0cef67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsParallelism",
    jsii_struct_bases=[],
    name_mapping={"count": "count"},
)
class KinesisAnalyticsApplicationInputsParallelism:
    def __init__(self, *, count: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#count KinesisAnalyticsApplication#count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187cd930bbd3af383898240bafcbe517611100d6ca7ef839a1436a05ada54f97)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#count KinesisAnalyticsApplication#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsParallelism(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsParallelismOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsParallelismOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56ff654d919984e7010e2574699d15068bb485579c403b30d1b7e6d47b88a39d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88ed9594ef0ef449046b49ee816c59b53118cda59b483f892819539333f24c08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsParallelism]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsParallelism], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsParallelism],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c941217615bb99db792f8c47d85d6f3a9537195b4da5cc64e6d9c08d8ec63a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"lambda_": "lambda"},
)
class KinesisAnalyticsApplicationInputsProcessingConfiguration:
    def __init__(
        self,
        *,
        lambda_: typing.Union["KinesisAnalyticsApplicationInputsProcessingConfigurationLambda", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        if isinstance(lambda_, dict):
            lambda_ = KinesisAnalyticsApplicationInputsProcessingConfigurationLambda(**lambda_)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af06384f651c39a99d0864d07f9f7d8a724fa1237fb39e28f809855ffc6c41ed)
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_": lambda_,
        }

    @builtins.property
    def lambda_(
        self,
    ) -> "KinesisAnalyticsApplicationInputsProcessingConfigurationLambda":
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        result = self._values.get("lambda_")
        assert result is not None, "Required property 'lambda_' is missing"
        return typing.cast("KinesisAnalyticsApplicationInputsProcessingConfigurationLambda", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfigurationLambda",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationInputsProcessingConfigurationLambda:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30cdaaf50691e68d7ad44a4a54f20174584f215837de67da3931442700ce839a)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsProcessingConfigurationLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd640c16c63e5475123333a7acae8c0b1f8e25a95e4b5e8fa7ee87fe5e0b358a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e5eee0ed6823f6926ad19abe255921e81bb0673191a106d3f998162174476d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3eb1eb74671cf2a987a12ff1143975bc78515a587d84ea399bcc7512743313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5342205d08773e4e063ea69c96c9c0968984b2c17408fd705015f3394c6dcacf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__158884a3174236c467e50ec14633a38b2eeb9cfa3519f20c94857eee9288dbab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLambda")
    def put_lambda(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationInputsProcessingConfigurationLambda(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(
        self,
    ) -> KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e371048b2c982ec7154f3e980e042974b8acdaca027f14b20ec991b6a0932d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchema",
    jsii_struct_bases=[],
    name_mapping={
        "record_columns": "recordColumns",
        "record_format": "recordFormat",
        "record_encoding": "recordEncoding",
    },
)
class KinesisAnalyticsApplicationInputsSchema:
    def __init__(
        self,
        *,
        record_columns: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordColumns", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        if isinstance(record_format, dict):
            record_format = KinesisAnalyticsApplicationInputsSchemaRecordFormat(**record_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f27472a12172995ce4426df668df621646cfadd236b0b9a6523f7751c6f4f2a)
            check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
            check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
            check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_columns": record_columns,
            "record_format": record_format,
        }
        if record_encoding is not None:
            self._values["record_encoding"] = record_encoding

    @builtins.property
    def record_columns(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]]:
        '''record_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        '''
        result = self._values.get("record_columns")
        assert result is not None, "Required property 'record_columns' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]], result)

    @builtins.property
    def record_format(self) -> "KinesisAnalyticsApplicationInputsSchemaRecordFormat":
        '''record_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        '''
        result = self._values.get("record_format")
        assert result is not None, "Required property 'record_format' is missing"
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordFormat", result)

    @builtins.property
    def record_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.'''
        result = self._values.get("record_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0a677cb3ae07c83ab0bacee55748617d8f4a1c8fa158561d365768912260736)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRecordColumns")
    def put_record_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02be118cc74d36e30077ca4d268b03f16cdaeda234009aafe7b04c7cd80d465d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordColumns", [value]))

    @jsii.member(jsii_name="putRecordFormat")
    def put_record_format(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormat(
            mapping_parameters=mapping_parameters
        )

        return typing.cast(None, jsii.invoke(self, "putRecordFormat", [value]))

    @jsii.member(jsii_name="resetRecordEncoding")
    def reset_record_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="recordColumns")
    def record_columns(
        self,
    ) -> "KinesisAnalyticsApplicationInputsSchemaRecordColumnsList":
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordColumnsList", jsii.get(self, "recordColumns"))

    @builtins.property
    @jsii.member(jsii_name="recordFormat")
    def record_format(
        self,
    ) -> "KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference", jsii.get(self, "recordFormat"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnsInput")
    def record_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]]], jsii.get(self, "recordColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncodingInput")
    def record_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatInput")
    def record_format_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormat"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormat"], jsii.get(self, "recordFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncoding")
    def record_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordEncoding"))

    @record_encoding.setter
    def record_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f68649f682a1b289b789b3252a8a30347fb1e334a227c205a52291cf34b8ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchema]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff40f7bd108e0acc1cdc134202e5dceb02e713b3dc9d70cfb52bd52f5222700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordColumns",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordColumns:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_type: builtins.str,
        mapping: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param sql_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.
        :param mapping: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77633e1d06abb820c49e9872c409601a9c2cadbd00dbaa40eadf77a41c8cb690)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.'''
        result = self._values.get("sql_type")
        assert result is not None, "Required property 'sql_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.'''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaRecordColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aee70d03047e4b4a2c84fa9af604c21e349083be86814ecfdd105bb3023adc9a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3a90e31e1bb755c097278883c05c7a1f82ac3242665793fc0045c548950886b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d861e975849337f64ba65082a3a5e3282328c221be80758111c473e4e89420c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47b4eee76cb43f2677e922ed04c475dd5ad4f11fbd2095267d158b4bfdad82a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d52b8f3fde12e5dfbec3061097f1dd9da3e9054b0f08b09a4a910d710a9e5fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f3afe264363ef59e59df0a3ad189e12c541c956e99169f6413c2593c7e9723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3327545a3385b59fe65472e62f6154f7de65ad44189381a9771769941ee074ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47a6c6c5e2e4cdd51a1118960c62c2f1dd8c19eb0fd4bfaf76bf286ee5d9f67d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112d66fa507a46ee1d3ba7038500514139dd960373ed89031d4c37405db03a38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sqlType")
    def sql_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlType"))

    @sql_type.setter
    def sql_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6d6a68150a8294ab856a9998fb7cacee62b4aba1771a6da70fbba6b94a0892)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8963b46da112727794a474924b1cc3203544ab5f4b7d69fa5fa2e52c05ad396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormat",
    jsii_struct_bases=[],
    name_mapping={"mapping_parameters": "mappingParameters"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormat:
    def __init__(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        if isinstance(mapping_parameters, dict):
            mapping_parameters = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters(**mapping_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d849d87d91c20626fce9cb40d118c70fe5c6f5111bed02b98ae1657f32337f20)
            check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mapping_parameters is not None:
            self._values["mapping_parameters"] = mapping_parameters

    @builtins.property
    def mapping_parameters(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters"]:
        '''mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        result = self._values.get("mapping_parameters")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters",
    jsii_struct_bases=[],
    name_mapping={"csv": "csv", "json": "json"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters:
    def __init__(
        self,
        *,
        csv: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv", typing.Dict[builtins.str, typing.Any]]] = None,
        json: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        if isinstance(csv, dict):
            csv = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(**csv)
        if isinstance(json, dict):
            json = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(**json)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a4084834412df3a2ad4891a46dddb5d677c2732f1a14dae581223ae884f29c2)
            check_type(argname="argument csv", value=csv, expected_type=type_hints["csv"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if csv is not None:
            self._values["csv"] = csv
        if json is not None:
            self._values["json"] = json

    @builtins.property
    def csv(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv"]:
        '''csv block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        '''
        result = self._values.get("csv")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv"], result)

    @builtins.property
    def json(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson"]:
        '''json block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv",
    jsii_struct_bases=[],
    name_mapping={
        "record_column_delimiter": "recordColumnDelimiter",
        "record_row_delimiter": "recordRowDelimiter",
    },
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv:
    def __init__(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35260e72fede42474f33c1daac0b1c3eb16241c385d1e3ec67366ea92cf5b397)
            check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
            check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_column_delimiter": record_column_delimiter,
            "record_row_delimiter": record_row_delimiter,
        }

    @builtins.property
    def record_column_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.'''
        result = self._values.get("record_column_delimiter")
        assert result is not None, "Required property 'record_column_delimiter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_row_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.'''
        result = self._values.get("record_row_delimiter")
        assert result is not None, "Required property 'record_row_delimiter' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71f48d4246930a78cb0b7f50f6bfb1a1ea5b9f6eb14c97254fbc5d40ed3d89f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b5766e9d52718b2a36eb710b493056cb965928aaa4bcb3d0badac8929c65b51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordColumnDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiter")
    def record_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowDelimiter"))

    @record_row_delimiter.setter
    def record_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c460b2f3c54e7797fcf86f446ef2beb20260422c612b0e54f357fe9fb0fda1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcfd5f1a70107f53916fa012058074f6b42b38cc7c35e225706bab894c8efc75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson",
    jsii_struct_bases=[],
    name_mapping={"record_row_path": "recordRowPath"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson:
    def __init__(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87fd3d38d289bea9a44343dee04011205afe991f9fdd97760f90d14859cef6f2)
            check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_row_path": record_row_path,
        }

    @builtins.property
    def record_row_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.'''
        result = self._values.get("record_row_path")
        assert result is not None, "Required property 'record_row_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__39bc2772e56b395466e01e1cac24b951cda5b2d23079e98b47904859d99c88e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__168311a16664131f4108529ea5308c7271d6a9636c35e4a467688db267f1ea22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a1d80a76e403d17a2701b915b36e107c12cfbcbc1cf85e5c21e6496e7b4a57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__419bff8ef5b1a1ab12be8e405f679247e10ae35c46a1e26a3444e2f7a63858f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCsv")
    def put_csv(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(
            record_column_delimiter=record_column_delimiter,
            record_row_delimiter=record_row_delimiter,
        )

        return typing.cast(None, jsii.invoke(self, "putCsv", [value]))

    @jsii.member(jsii_name="putJson")
    def put_json(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(
            record_row_path=record_row_path
        )

        return typing.cast(None, jsii.invoke(self, "putJson", [value]))

    @jsii.member(jsii_name="resetCsv")
    def reset_csv(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsv", []))

    @jsii.member(jsii_name="resetJson")
    def reset_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJson", []))

    @builtins.property
    @jsii.member(jsii_name="csv")
    def csv(
        self,
    ) -> KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference, jsii.get(self, "csv"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(
        self,
    ) -> KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="csvInput")
    def csv_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv], jsii.get(self, "csvInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f6dad7fbbbbc4512649c3414e8c404fa8327be05ac1966b9982f417a7130de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbf684efc1bc4ac009aac1805d10ff43de03e19ebb0795911a78732290848a21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMappingParameters")
    def put_mapping_parameters(
        self,
        *,
        csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv, typing.Dict[builtins.str, typing.Any]]] = None,
        json: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters(
            csv=csv, json=json
        )

        return typing.cast(None, jsii.invoke(self, "putMappingParameters", [value]))

    @jsii.member(jsii_name="resetMappingParameters")
    def reset_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappingParameters", []))

    @builtins.property
    @jsii.member(jsii_name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference, jsii.get(self, "mappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @builtins.property
    @jsii.member(jsii_name="mappingParametersInput")
    def mapping_parameters_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters], jsii.get(self, "mappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d5994c821aea74f48860298582084ae0478efccc8f5661b87fb7b02de4b0f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsStartingPositionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"starting_position": "startingPosition"},
)
class KinesisAnalyticsApplicationInputsStartingPositionConfiguration:
    def __init__(
        self,
        *,
        starting_position: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param starting_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position KinesisAnalyticsApplication#starting_position}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a731c8a9a246e8b85ee7f78891edeedca75a44127f40fe4f87157699b797838)
            check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if starting_position is not None:
            self._values["starting_position"] = starting_position

    @builtins.property
    def starting_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position KinesisAnalyticsApplication#starting_position}.'''
        result = self._values.get("starting_position")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsStartingPositionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsStartingPositionConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsStartingPositionConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44232b7f166e309955ed6c601151c5a6715dae8b064c52a64726b75c937acd5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234c8c3ec259dba3cfa09aacd5545b674cabea356a5858d90c3f73dd8219bb71)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80bc073f0b1c97c406b3627667c51de5b3e7b7c8dd218cfcbf60ea70c7a6685a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed4dadd5788af90eea422eefcf7c0f2cb9b66b0a8bd99d99c7ae7d2dfc28cd2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a364699be83687081fd8219f786ee9cea40eae6fb3c09927ddae5da77e6ae0b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01416a0124357132a1e826fa69f4676bf605b64c209ada3f79ede52859060442)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__901857592e161700e62c2c355ff1ef0de9d38de4908023952f828d9234fa4073)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStartingPosition")
    def reset_starting_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartingPosition", []))

    @builtins.property
    @jsii.member(jsii_name="startingPositionInput")
    def starting_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startingPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="startingPosition")
    def starting_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startingPosition"))

    @starting_position.setter
    def starting_position(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__486d9d468679b96bb61421159297bf486afdab65b84433a2a2f14cef276e063e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingPosition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b64323f444c7da870f1b99c8db16ffdc1d67c0be4c374ae506d6c528af0ab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputs",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schema": "schema",
        "kinesis_firehose": "kinesisFirehose",
        "kinesis_stream": "kinesisStream",
        "lambda_": "lambda",
    },
)
class KinesisAnalyticsApplicationOutputs:
    def __init__(
        self,
        *,
        name: builtins.str,
        schema: typing.Union["KinesisAnalyticsApplicationOutputsSchema", typing.Dict[builtins.str, typing.Any]],
        kinesis_firehose: typing.Optional[typing.Union["KinesisAnalyticsApplicationOutputsKinesisFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream: typing.Optional[typing.Union["KinesisAnalyticsApplicationOutputsKinesisStream", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_: typing.Optional[typing.Union["KinesisAnalyticsApplicationOutputsLambda", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param kinesis_firehose: kinesis_firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        :param kinesis_stream: kinesis_stream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        if isinstance(schema, dict):
            schema = KinesisAnalyticsApplicationOutputsSchema(**schema)
        if isinstance(kinesis_firehose, dict):
            kinesis_firehose = KinesisAnalyticsApplicationOutputsKinesisFirehose(**kinesis_firehose)
        if isinstance(kinesis_stream, dict):
            kinesis_stream = KinesisAnalyticsApplicationOutputsKinesisStream(**kinesis_stream)
        if isinstance(lambda_, dict):
            lambda_ = KinesisAnalyticsApplicationOutputsLambda(**lambda_)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4fef4104aa07e58b0fa4d03b0dac33d4b4bb6c7b6141583f4109bbce457228)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument kinesis_firehose", value=kinesis_firehose, expected_type=type_hints["kinesis_firehose"])
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "schema": schema,
        }
        if kinesis_firehose is not None:
            self._values["kinesis_firehose"] = kinesis_firehose
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if lambda_ is not None:
            self._values["lambda_"] = lambda_

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> "KinesisAnalyticsApplicationOutputsSchema":
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("KinesisAnalyticsApplicationOutputsSchema", result)

    @builtins.property
    def kinesis_firehose(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationOutputsKinesisFirehose"]:
        '''kinesis_firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        '''
        result = self._values.get("kinesis_firehose")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsKinesisFirehose"], result)

    @builtins.property
    def kinesis_stream(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationOutputsKinesisStream"]:
        '''kinesis_stream block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsKinesisStream"], result)

    @builtins.property
    def lambda_(self) -> typing.Optional["KinesisAnalyticsApplicationOutputsLambda"]:
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsLambda"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisFirehose",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationOutputsKinesisFirehose:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc1f4f165c3d742f1a169190df18dac4ba398acc800ce8716d1ab3e1527fb369)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsKinesisFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0df9b536fc50d4e0e5ba7423f2603ddb29e84e709cab597820c7555f457c2bbb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5450e08908a3473160ba0e940b5646c5c315efc6abf9c463bf3da180bc6a10e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bec8c8b60fd218a94cec8447ce8ba16c75c8d644426dffbde6d923bd1009bec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ef4a0899f3fe8823b2688373638b9476aacc7e3dec4ef08fc55dd9b19857e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationOutputsKinesisStream:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17099a7a1475dbe5ec5f2a239fd4506c4a4eb609b54c47809c4742d9117243ff)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__633a1de3df8407818af92d94a6e1e2e65f2e40e1185b80afa33a69df954fbf7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7845e37e5c015a001ea094426cee83de71a484726c31807aa04645cadb56a91e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b16f1d4e4e34c311df932b46f3a2ab60f9357476422e25d53927c78f268070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f97ca449b4ed6b5571b7cef9469c7d704c21888a96d781f6df11193cc0e4e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsLambda",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationOutputsLambda:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__676987df2c4ed32fc860bd1fbee1e33f3400f31192f308f5c811f6f5c50ed386)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsLambdaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsLambdaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__572eb5a7b4522576eb5432c89fcc110619d066b6b8c753563d1205bea5c482b8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef5858b4294822e1ebac3653fee4c6441c14b70b740eab19879dfceb8378eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fed9da1702fe7e53077e296cbaad30105024576c7ffd3b7aedb9f4a29eda170)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsLambda],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab109c9dbfc4610742f2621dd6100e9befdea2ee94da613685d45ebcbd13c3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationOutputsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6a97f2a4dc27117431053441ac60c68f20b348eb064ffb847abf586c33d369d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisAnalyticsApplicationOutputsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4f930a8e2521c750e209cb7ac92d11da026afa4e11966f938ee0328fea96de)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationOutputsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__969399ffabd63e35752d00872bfc3b25fa4a6a019e17c55465f2431f2b1f0269)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e38870a0f4638744a40a4eafaf66103d858440d6d583779c16b7ca812712c80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2182e7fdaefa37cde440fda5d111c348108c238adb64db566652cbeb2adc20b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21e661a8add121a9a3c2ef0764ec7db45c1e6d31934f2fb4e1fea00e94c225b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationOutputsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__793c48887a1d9067b1e8c0347386ccb341f78290851a8f2f4b6dc90f9cddce4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putKinesisFirehose")
    def put_kinesis_firehose(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationOutputsKinesisFirehose(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehose", [value]))

    @jsii.member(jsii_name="putKinesisStream")
    def put_kinesis_stream(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationOutputsKinesisStream(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStream", [value]))

    @jsii.member(jsii_name="putLambda")
    def put_lambda(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationOutputsLambda(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(self, *, record_format_type: builtins.str) -> None:
        '''
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format_type KinesisAnalyticsApplication#record_format_type}.
        '''
        value = KinesisAnalyticsApplicationOutputsSchema(
            record_format_type=record_format_type
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @jsii.member(jsii_name="resetKinesisFirehose")
    def reset_kinesis_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehose", []))

    @jsii.member(jsii_name="resetKinesisStream")
    def reset_kinesis_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStream", []))

    @jsii.member(jsii_name="resetLambda")
    def reset_lambda(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambda", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference:
        return typing.cast(KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference, jsii.get(self, "kinesisFirehose"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStream")
    def kinesis_stream(
        self,
    ) -> KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference:
        return typing.cast(KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference, jsii.get(self, "kinesisStream"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> KinesisAnalyticsApplicationOutputsLambdaOutputReference:
        return typing.cast(KinesisAnalyticsApplicationOutputsLambdaOutputReference, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "KinesisAnalyticsApplicationOutputsSchemaOutputReference":
        return typing.cast("KinesisAnalyticsApplicationOutputsSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseInput")
    def kinesis_firehose_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose], jsii.get(self, "kinesisFirehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamInput")
    def kinesis_stream_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream], jsii.get(self, "kinesisStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(self) -> typing.Optional[KinesisAnalyticsApplicationOutputsLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsLambda], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationOutputsSchema"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsSchema"], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ae9abcedc0021e4e4e0b0aa210d23578b77897d834782d712b8f88d57022df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7862e8edbba7fc2a007fbe545f3fb19e3ad207a0eee6bbbfc5080d57b291ca42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsSchema",
    jsii_struct_bases=[],
    name_mapping={"record_format_type": "recordFormatType"},
)
class KinesisAnalyticsApplicationOutputsSchema:
    def __init__(self, *, record_format_type: builtins.str) -> None:
        '''
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format_type KinesisAnalyticsApplication#record_format_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdfdade2205d1cfe0baded13c4cbd9320621b4a87e770f2114574c00435cc62f)
            check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_format_type": record_format_type,
        }

    @builtins.property
    def record_format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format_type KinesisAnalyticsApplication#record_format_type}.'''
        result = self._values.get("record_format_type")
        assert result is not None, "Required property 'record_format_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60af91b7b492c29d2dff05dcba9fc0dd0afacfaadfff4b402490b11f964f12e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d98139dc162d6d599d999b3c98d167983516c9b02995905b0a6ff7822e368f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordFormatType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsSchema]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac01c0a7e839d655016de601e4849d0af69c57afc2e43b3d9e586a3fe84facd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSources",
    jsii_struct_bases=[],
    name_mapping={"s3": "s3", "schema": "schema", "table_name": "tableName"},
)
class KinesisAnalyticsApplicationReferenceDataSources:
    def __init__(
        self,
        *,
        s3: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesS3", typing.Dict[builtins.str, typing.Any]],
        schema: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchema", typing.Dict[builtins.str, typing.Any]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#s3 KinesisAnalyticsApplication#s3}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#table_name KinesisAnalyticsApplication#table_name}.
        '''
        if isinstance(s3, dict):
            s3 = KinesisAnalyticsApplicationReferenceDataSourcesS3(**s3)
        if isinstance(schema, dict):
            schema = KinesisAnalyticsApplicationReferenceDataSourcesSchema(**schema)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43d6702b7210d26596762bb4d81c503ecee757538869efa2a46f18e4693d03f9)
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3": s3,
            "schema": schema,
            "table_name": table_name,
        }

    @builtins.property
    def s3(self) -> "KinesisAnalyticsApplicationReferenceDataSourcesS3":
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#s3 KinesisAnalyticsApplication#s3}
        '''
        result = self._values.get("s3")
        assert result is not None, "Required property 's3' is missing"
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesS3", result)

    @builtins.property
    def schema(self) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchema":
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchema", result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#table_name KinesisAnalyticsApplication#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a50c5a7698f28533229ae83d7ba0f11c0f7982671ad3948925a306c5ce84db6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#bucket_arn KinesisAnalyticsApplication#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#file_key KinesisAnalyticsApplication#file_key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesS3(
            bucket_arn=bucket_arn, file_key=file_key, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(
        self,
        *,
        record_columns: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchema(
            record_columns=record_columns,
            record_format=record_format,
            record_encoding=record_encoding,
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesS3"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchema"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchema"], jsii.get(self, "schemaInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b491d3e7dfc18265a3b57cc7f17389bbf3676539918b1ed562a4cada86c046df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSources]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77bf610773fbd72d0b4fdd3acc13ed8636f9230d121d34787d666c40c840e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "file_key": "fileKey",
        "role_arn": "roleArn",
    },
)
class KinesisAnalyticsApplicationReferenceDataSourcesS3:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#bucket_arn KinesisAnalyticsApplication#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#file_key KinesisAnalyticsApplication#file_key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a188f1e276646c91f16b99a2dd0bc50357a4aa7e88ad6b326e314f210d1f0fb)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "file_key": file_key,
            "role_arn": role_arn,
        }

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#bucket_arn KinesisAnalyticsApplication#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#file_key KinesisAnalyticsApplication#file_key}.'''
        result = self._values.get("file_key")
        assert result is not None, "Required property 'file_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcd2ab0118a1725a6a588f0f2bc4214c9981c783eec07b4cacd46b6841acdf86)
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
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d11c47b83a36c3e5a1427620e6cb077171ee38cef164e46f83f660e594a7e0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="fileKey")
    def file_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileKey"))

    @file_key.setter
    def file_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bcd0a43f24549bc1e61f0542c601957f30d74190a6253084bc89bba03a9cca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileKey", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a6a04e2cbb1ed88a2d3e8e035913dc8b20122f4e1f6954ec7a0226cad8236aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d6d45f1eb9d1576426ad3f9a7e18112580ddbfb8ddd24327bd8e342543d0fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchema",
    jsii_struct_bases=[],
    name_mapping={
        "record_columns": "recordColumns",
        "record_format": "recordFormat",
        "record_encoding": "recordEncoding",
    },
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchema:
    def __init__(
        self,
        *,
        record_columns: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns", typing.Dict[builtins.str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat", typing.Dict[builtins.str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        if isinstance(record_format, dict):
            record_format = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(**record_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91042393769f603f2c7e23c974ae7daade0069243462dcbf1ee136baf007e28)
            check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
            check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
            check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_columns": record_columns,
            "record_format": record_format,
        }
        if record_encoding is not None:
            self._values["record_encoding"] = record_encoding

    @builtins.property
    def record_columns(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]]:
        '''record_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        '''
        result = self._values.get("record_columns")
        assert result is not None, "Required property 'record_columns' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]], result)

    @builtins.property
    def record_format(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat":
        '''record_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        '''
        result = self._values.get("record_format")
        assert result is not None, "Required property 'record_format' is missing"
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat", result)

    @builtins.property
    def record_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.'''
        result = self._values.get("record_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28364fa793cdf8213471898968d561085e73b6e2993302bc1bf0f24c7dca25f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRecordColumns")
    def put_record_columns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dbe33566466f42bcd7a22e65096ddb8d50fa35797f27d6775af47533e0b1d5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordColumns", [value]))

    @jsii.member(jsii_name="putRecordFormat")
    def put_record_format(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(
            mapping_parameters=mapping_parameters
        )

        return typing.cast(None, jsii.invoke(self, "putRecordFormat", [value]))

    @jsii.member(jsii_name="resetRecordEncoding")
    def reset_record_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="recordColumns")
    def record_columns(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList", jsii.get(self, "recordColumns"))

    @builtins.property
    @jsii.member(jsii_name="recordFormat")
    def record_format(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference", jsii.get(self, "recordFormat"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnsInput")
    def record_columns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]]], jsii.get(self, "recordColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncodingInput")
    def record_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatInput")
    def record_format_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat"], jsii.get(self, "recordFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncoding")
    def record_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordEncoding"))

    @record_encoding.setter
    def record_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__641dcba00e75194580c9d03af30dd883794d313f56ceb10babd8320fa8435ef8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfdcead481d381d952852bc2907e04e4e4e0e28098522239ecb66ba2327b35f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_type: builtins.str,
        mapping: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param sql_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.
        :param mapping: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f61776fbed6f784c456d5d0885d14140a4008f1d30c953a2b45842cad261a42)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.'''
        result = self._values.get("sql_type")
        assert result is not None, "Required property 'sql_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.'''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4a2e15e81f71cf5cd329fdbe3c71f729a12c726e673eb59f8a7d81240e6d348)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043893725b2e487c8a6da14ebee338aec760e854eeee8210116139423eb56c0a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b70b86e0ce82930adfa5693bbc1a7b036f6ab6526edc1d88e1ed33b65dd9bfd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c075254c325ba95984a35f018c833b004ba3aba2c83368580e7fa6656d27a71c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ef1f33dad5fe025388af2c2e6d007f0b3e554d55334f80c7b9b9790ca2bf75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf489067c727da43ce8c890546d188826adc4fe1eba213422c2d24d973caf0a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a94793bf0f393194a4ab032c8d1dec253a804c9615264f0935bf3b390847384)
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
            type_hints = typing.get_type_hints(_typecheckingstub__689cd48874f6703f13b1beaaaee6a3acde6549cc49cf31500f520b9a185bf66d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f4e16b26ba6193d64de89527939376a0979ab40e6bff40ef7a9ae058d61b62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sqlType")
    def sql_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlType"))

    @sql_type.setter
    def sql_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922628cf4629b0ea6c319352cf99703dae868e7e8384bede44dc4ee77a0fb850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85fec2cf6efd097128cf7b7cabffc71013386d2279b69aa72e8343916f4eaea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat",
    jsii_struct_bases=[],
    name_mapping={"mapping_parameters": "mappingParameters"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat:
    def __init__(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        if isinstance(mapping_parameters, dict):
            mapping_parameters = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(**mapping_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9b999ea904a6d617d283ee366730b41881b2321bfb7e807cd7fe0dfbc67fb8)
            check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mapping_parameters is not None:
            self._values["mapping_parameters"] = mapping_parameters

    @builtins.property
    def mapping_parameters(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters"]:
        '''mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        result = self._values.get("mapping_parameters")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters",
    jsii_struct_bases=[],
    name_mapping={"csv": "csv", "json": "json"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters:
    def __init__(
        self,
        *,
        csv: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv", typing.Dict[builtins.str, typing.Any]]] = None,
        json: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        if isinstance(csv, dict):
            csv = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(**csv)
        if isinstance(json, dict):
            json = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(**json)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a29350fba3c1e1d03dd496e47f2850a4673ebad29002c1735d9365d757550c)
            check_type(argname="argument csv", value=csv, expected_type=type_hints["csv"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if csv is not None:
            self._values["csv"] = csv
        if json is not None:
            self._values["json"] = json

    @builtins.property
    def csv(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv"]:
        '''csv block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        '''
        result = self._values.get("csv")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv"], result)

    @builtins.property
    def json(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson"]:
        '''json block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv",
    jsii_struct_bases=[],
    name_mapping={
        "record_column_delimiter": "recordColumnDelimiter",
        "record_row_delimiter": "recordRowDelimiter",
    },
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv:
    def __init__(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a5013613de7a4a58a412abc444086f756a9ad926520fbf061ccf5696e50829)
            check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
            check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_column_delimiter": record_column_delimiter,
            "record_row_delimiter": record_row_delimiter,
        }

    @builtins.property
    def record_column_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.'''
        result = self._values.get("record_column_delimiter")
        assert result is not None, "Required property 'record_column_delimiter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_row_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.'''
        result = self._values.get("record_row_delimiter")
        assert result is not None, "Required property 'record_row_delimiter' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__531302b1ec0f049f237726a70d645928a5ab018f64332c004d7e1d17dc3ed3d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9d4127a943f396cbfa57fc0d3f5e8fa07448f9f5032e96d7d15929e4fddfb04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordColumnDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiter")
    def record_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowDelimiter"))

    @record_row_delimiter.setter
    def record_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44dd7b8e0af257784e474a3491984ba900815f86a190781dc3d5407eddbf555)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c15bd159e8cda037194d824c90f87fe00ab39a8a9e6fe1ccfdd4e8c4b5465f2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson",
    jsii_struct_bases=[],
    name_mapping={"record_row_path": "recordRowPath"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson:
    def __init__(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089746a7bce0c9dc00e739ab27cf97874a303d330a478454a4be8d0c35bce918)
            check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_row_path": record_row_path,
        }

    @builtins.property
    def record_row_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.'''
        result = self._values.get("record_row_path")
        assert result is not None, "Required property 'record_row_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c06f03dd0b9dc733750dca4df4f904bbbbc289742f6be71a58c5ee83c0d644df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__519c0ff90c5a99be25d71cb904f09848dc1460e13626a2c10a7ebcc93ac346c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ec214b3a1e11382fa8b39b0cd341e7a7b47817fdd0ece5e78e66d80f37a9f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1d4d6d26bc830752403fde2ac4d733299781ba59b8060d5faeb4fa97ba4246a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCsv")
    def put_csv(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(
            record_column_delimiter=record_column_delimiter,
            record_row_delimiter=record_row_delimiter,
        )

        return typing.cast(None, jsii.invoke(self, "putCsv", [value]))

    @jsii.member(jsii_name="putJson")
    def put_json(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(
            record_row_path=record_row_path
        )

        return typing.cast(None, jsii.invoke(self, "putJson", [value]))

    @jsii.member(jsii_name="resetCsv")
    def reset_csv(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsv", []))

    @jsii.member(jsii_name="resetJson")
    def reset_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJson", []))

    @builtins.property
    @jsii.member(jsii_name="csv")
    def csv(
        self,
    ) -> KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference:
        return typing.cast(KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference, jsii.get(self, "csv"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(
        self,
    ) -> KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference:
        return typing.cast(KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="csvInput")
    def csv_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv], jsii.get(self, "csvInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__989d4508391b38b5543cfddd97acf14c6b2a559f0b3bb68aa6a63bafcb2a4189)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4395cd1b3f8f740766ac869b4e0f4eda624ca7856d2b067ac4dc53c57183600a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMappingParameters")
    def put_mapping_parameters(
        self,
        *,
        csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv, typing.Dict[builtins.str, typing.Any]]] = None,
        json: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(
            csv=csv, json=json
        )

        return typing.cast(None, jsii.invoke(self, "putMappingParameters", [value]))

    @jsii.member(jsii_name="resetMappingParameters")
    def reset_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappingParameters", []))

    @builtins.property
    @jsii.member(jsii_name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference:
        return typing.cast(KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference, jsii.get(self, "mappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @builtins.property
    @jsii.member(jsii_name="mappingParametersInput")
    def mapping_parameters_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters], jsii.get(self, "mappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5017ff7ffa3d18b47a0068c7ad9661923ca599a15593cd4946200344d7926e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KinesisAnalyticsApplication",
    "KinesisAnalyticsApplicationCloudwatchLoggingOptions",
    "KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference",
    "KinesisAnalyticsApplicationConfig",
    "KinesisAnalyticsApplicationInputs",
    "KinesisAnalyticsApplicationInputsKinesisFirehose",
    "KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference",
    "KinesisAnalyticsApplicationInputsKinesisStream",
    "KinesisAnalyticsApplicationInputsKinesisStreamOutputReference",
    "KinesisAnalyticsApplicationInputsOutputReference",
    "KinesisAnalyticsApplicationInputsParallelism",
    "KinesisAnalyticsApplicationInputsParallelismOutputReference",
    "KinesisAnalyticsApplicationInputsProcessingConfiguration",
    "KinesisAnalyticsApplicationInputsProcessingConfigurationLambda",
    "KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference",
    "KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference",
    "KinesisAnalyticsApplicationInputsSchema",
    "KinesisAnalyticsApplicationInputsSchemaOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordColumns",
    "KinesisAnalyticsApplicationInputsSchemaRecordColumnsList",
    "KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormat",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference",
    "KinesisAnalyticsApplicationInputsStartingPositionConfiguration",
    "KinesisAnalyticsApplicationInputsStartingPositionConfigurationList",
    "KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference",
    "KinesisAnalyticsApplicationOutputs",
    "KinesisAnalyticsApplicationOutputsKinesisFirehose",
    "KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference",
    "KinesisAnalyticsApplicationOutputsKinesisStream",
    "KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference",
    "KinesisAnalyticsApplicationOutputsLambda",
    "KinesisAnalyticsApplicationOutputsLambdaOutputReference",
    "KinesisAnalyticsApplicationOutputsList",
    "KinesisAnalyticsApplicationOutputsOutputReference",
    "KinesisAnalyticsApplicationOutputsSchema",
    "KinesisAnalyticsApplicationOutputsSchemaOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSources",
    "KinesisAnalyticsApplicationReferenceDataSourcesOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesS3",
    "KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchema",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference",
]

publication.publish()

def _typecheckingstub__d4c4d169f90215ee16e423364bd59bf0ca6d860488279543f7875ecf8dd1350e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisAnalyticsApplicationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inputs: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputs, typing.Dict[builtins.str, typing.Any]]] = None,
    outputs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationOutputs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    reference_data_sources: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSources, typing.Dict[builtins.str, typing.Any]]] = None,
    start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__6ec9dae807a912d52f32a8f034020789a3f57fbfdd1955d0548c44abd05877a2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationOutputs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e0ac5da14cce6e9bf99ad440d187cc6c73dca5809a1431dc3bb15a35f272c2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860aaaa40437b9cf5f9f0efbe9c254bd157646d819d81d2ee17d5dee682cf887(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee20b29f1449193b6efe05ac71f73e860b72e11035bf83d3437cacbf81a5adc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedecac7f8c34b9630128981b6a5793ff69f178a2b72a23f5c42875af2196e74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a67dc06e4d47cf5217ab5e300f437a9e5f2c202fe069a5b75d3330d6cd149f4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121d80f39ac432e2364d22609dead0446deecc70c4f3f990562a57a19c040ac4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382801fb942abc3d965912abb41c8a94de093d4e03ae56ed550628761e46610e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__927bdf89054e35be7cec42dd8dcba6f3059ae0aa6ec2e121d6734c66042c2e99(
    *,
    log_stream_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060bcf32279c66d8d6f4180a44a846f7157e3d1acc37a9e13a88bf2c39beadb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c095520965bb3e27cbfecdff0205f576ff7381354a54444c253505e2c29d736(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a80ee488a6cee48e78260268770ac91b645c3ce07846684ec01ac25cda16957(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec60b94ecdb53bbc690ff6780332dfd3890e79c3925441645d1a40c49072dc65(
    value: typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d532ce4dc5faf594a91e1466b7aad5a50eff19540fa1abe37a903a65ac0a0a3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisAnalyticsApplicationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    code: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inputs: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputs, typing.Dict[builtins.str, typing.Any]]] = None,
    outputs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationOutputs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    reference_data_sources: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSources, typing.Dict[builtins.str, typing.Any]]] = None,
    start_application: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a404a7ed187fae99b53ceb70ed37684b3544347b53e2b5cb7309e698cc9dda1e(
    *,
    name_prefix: builtins.str,
    schema: typing.Union[KinesisAnalyticsApplicationInputsSchema, typing.Dict[builtins.str, typing.Any]],
    kinesis_firehose: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsKinesisFirehose, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_stream: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsKinesisStream, typing.Dict[builtins.str, typing.Any]]] = None,
    parallelism: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsParallelism, typing.Dict[builtins.str, typing.Any]]] = None,
    processing_configuration: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    starting_position_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b228af0e114461db543dbb6c9cb975e97317d452e096b6255c3a3e6222390d1d(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03aa8464d368ee908e78db3a3a45baefe314ac38b4ff5ed201395b91631e9357(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2edd6ae72f3516c7b408d629819f47da4512901f332412f6d2ce056563940598(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c567b0845cb8654c83c7d8f3c03f4da960eff65466c8b8c0651cf9522fdc41b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e5ad4f85b7e719de6e3fcd9761dbdf135030ffb16a22626c99b1cc9aa1d52fb(
    value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90460791b1d636ee064f692d310a202ca69d996971a8cb4d0264d613e038ea13(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaccdfa4f4a2f40c17b8b64093e1c73015819c1ace02312d783f7e6d5e6c7622(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3b0c46ddb20129b9cffc547285b203b6abec55fd719a587fc3b8fff1501a1e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1085ab6d886077cae672bf8dd0462efa40a4da6a83cb86b41eefd561e6bcedf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cbd49286544b57bc916e7b16752ce56431249ce292d571361be2107a7963614(
    value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452ede47079b00344df316b7b12837a99ff5233292dd8e29d9fb82ea1adc015a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b2304a2e34a8cd42471d81663635b506a1473b5c972657e211c85d2390028c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efff2951628acc1079a6928ab9693c8709f08ead7f47527702b27603a655e3c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca85d9713583eb1fcd9f20c7be26475e1963a9b3f73cfd8727c5762edb0cef67(
    value: typing.Optional[KinesisAnalyticsApplicationInputs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187cd930bbd3af383898240bafcbe517611100d6ca7ef839a1436a05ada54f97(
    *,
    count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ff654d919984e7010e2574699d15068bb485579c403b30d1b7e6d47b88a39d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ed9594ef0ef449046b49ee816c59b53118cda59b483f892819539333f24c08(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c941217615bb99db792f8c47d85d6f3a9537195b4da5cc64e6d9c08d8ec63a4(
    value: typing.Optional[KinesisAnalyticsApplicationInputsParallelism],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af06384f651c39a99d0864d07f9f7d8a724fa1237fb39e28f809855ffc6c41ed(
    *,
    lambda_: typing.Union[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30cdaaf50691e68d7ad44a4a54f20174584f215837de67da3931442700ce839a(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd640c16c63e5475123333a7acae8c0b1f8e25a95e4b5e8fa7ee87fe5e0b358a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e5eee0ed6823f6926ad19abe255921e81bb0673191a106d3f998162174476d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3eb1eb74671cf2a987a12ff1143975bc78515a587d84ea399bcc7512743313(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5342205d08773e4e063ea69c96c9c0968984b2c17408fd705015f3394c6dcacf(
    value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158884a3174236c467e50ec14633a38b2eeb9cfa3519f20c94857eee9288dbab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e371048b2c982ec7154f3e980e042974b8acdaca027f14b20ec991b6a0932d(
    value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f27472a12172995ce4426df668df621646cfadd236b0b9a6523f7751c6f4f2a(
    *,
    record_columns: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, typing.Dict[builtins.str, typing.Any]]]],
    record_format: typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormat, typing.Dict[builtins.str, typing.Any]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a677cb3ae07c83ab0bacee55748617d8f4a1c8fa158561d365768912260736(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02be118cc74d36e30077ca4d268b03f16cdaeda234009aafe7b04c7cd80d465d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f68649f682a1b289b789b3252a8a30347fb1e334a227c205a52291cf34b8ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff40f7bd108e0acc1cdc134202e5dceb02e713b3dc9d70cfb52bd52f5222700(
    value: typing.Optional[KinesisAnalyticsApplicationInputsSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77633e1d06abb820c49e9872c409601a9c2cadbd00dbaa40eadf77a41c8cb690(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee70d03047e4b4a2c84fa9af604c21e349083be86814ecfdd105bb3023adc9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3a90e31e1bb755c097278883c05c7a1f82ac3242665793fc0045c548950886b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d861e975849337f64ba65082a3a5e3282328c221be80758111c473e4e89420c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47b4eee76cb43f2677e922ed04c475dd5ad4f11fbd2095267d158b4bfdad82a5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52b8f3fde12e5dfbec3061097f1dd9da3e9054b0f08b09a4a910d710a9e5fc1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f3afe264363ef59e59df0a3ad189e12c541c956e99169f6413c2593c7e9723(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3327545a3385b59fe65472e62f6154f7de65ad44189381a9771769941ee074ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a6c6c5e2e4cdd51a1118960c62c2f1dd8c19eb0fd4bfaf76bf286ee5d9f67d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112d66fa507a46ee1d3ba7038500514139dd960373ed89031d4c37405db03a38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6d6a68150a8294ab856a9998fb7cacee62b4aba1771a6da70fbba6b94a0892(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8963b46da112727794a474924b1cc3203544ab5f4b7d69fa5fa2e52c05ad396(
    value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d849d87d91c20626fce9cb40d118c70fe5c6f5111bed02b98ae1657f32337f20(
    *,
    mapping_parameters: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a4084834412df3a2ad4891a46dddb5d677c2732f1a14dae581223ae884f29c2(
    *,
    csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv, typing.Dict[builtins.str, typing.Any]]] = None,
    json: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35260e72fede42474f33c1daac0b1c3eb16241c385d1e3ec67366ea92cf5b397(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f48d4246930a78cb0b7f50f6bfb1a1ea5b9f6eb14c97254fbc5d40ed3d89f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b5766e9d52718b2a36eb710b493056cb965928aaa4bcb3d0badac8929c65b51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c460b2f3c54e7797fcf86f446ef2beb20260422c612b0e54f357fe9fb0fda1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcfd5f1a70107f53916fa012058074f6b42b38cc7c35e225706bab894c8efc75(
    value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87fd3d38d289bea9a44343dee04011205afe991f9fdd97760f90d14859cef6f2(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39bc2772e56b395466e01e1cac24b951cda5b2d23079e98b47904859d99c88e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168311a16664131f4108529ea5308c7271d6a9636c35e4a467688db267f1ea22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a1d80a76e403d17a2701b915b36e107c12cfbcbc1cf85e5c21e6496e7b4a57(
    value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419bff8ef5b1a1ab12be8e405f679247e10ae35c46a1e26a3444e2f7a63858f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f6dad7fbbbbc4512649c3414e8c404fa8327be05ac1966b9982f417a7130de(
    value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf684efc1bc4ac009aac1805d10ff43de03e19ebb0795911a78732290848a21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d5994c821aea74f48860298582084ae0478efccc8f5661b87fb7b02de4b0f2(
    value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a731c8a9a246e8b85ee7f78891edeedca75a44127f40fe4f87157699b797838(
    *,
    starting_position: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44232b7f166e309955ed6c601151c5a6715dae8b064c52a64726b75c937acd5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234c8c3ec259dba3cfa09aacd5545b674cabea356a5858d90c3f73dd8219bb71(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bc073f0b1c97c406b3627667c51de5b3e7b7c8dd218cfcbf60ea70c7a6685a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4dadd5788af90eea422eefcf7c0f2cb9b66b0a8bd99d99c7ae7d2dfc28cd2a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a364699be83687081fd8219f786ee9cea40eae6fb3c09927ddae5da77e6ae0b4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01416a0124357132a1e826fa69f4676bf605b64c209ada3f79ede52859060442(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901857592e161700e62c2c355ff1ef0de9d38de4908023952f828d9234fa4073(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__486d9d468679b96bb61421159297bf486afdab65b84433a2a2f14cef276e063e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b64323f444c7da870f1b99c8db16ffdc1d67c0be4c374ae506d6c528af0ab2(
    value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4fef4104aa07e58b0fa4d03b0dac33d4b4bb6c7b6141583f4109bbce457228(
    *,
    name: builtins.str,
    schema: typing.Union[KinesisAnalyticsApplicationOutputsSchema, typing.Dict[builtins.str, typing.Any]],
    kinesis_firehose: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputsKinesisFirehose, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_stream: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputsKinesisStream, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputsLambda, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc1f4f165c3d742f1a169190df18dac4ba398acc800ce8716d1ab3e1527fb369(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df9b536fc50d4e0e5ba7423f2603ddb29e84e709cab597820c7555f457c2bbb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5450e08908a3473160ba0e940b5646c5c315efc6abf9c463bf3da180bc6a10e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec8c8b60fd218a94cec8447ce8ba16c75c8d644426dffbde6d923bd1009bec8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ef4a0899f3fe8823b2688373638b9476aacc7e3dec4ef08fc55dd9b19857e5(
    value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17099a7a1475dbe5ec5f2a239fd4506c4a4eb609b54c47809c4742d9117243ff(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__633a1de3df8407818af92d94a6e1e2e65f2e40e1185b80afa33a69df954fbf7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7845e37e5c015a001ea094426cee83de71a484726c31807aa04645cadb56a91e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b16f1d4e4e34c311df932b46f3a2ab60f9357476422e25d53927c78f268070(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f97ca449b4ed6b5571b7cef9469c7d704c21888a96d781f6df11193cc0e4e77(
    value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676987df2c4ed32fc860bd1fbee1e33f3400f31192f308f5c811f6f5c50ed386(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572eb5a7b4522576eb5432c89fcc110619d066b6b8c753563d1205bea5c482b8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef5858b4294822e1ebac3653fee4c6441c14b70b740eab19879dfceb8378eaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fed9da1702fe7e53077e296cbaad30105024576c7ffd3b7aedb9f4a29eda170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab109c9dbfc4610742f2621dd6100e9befdea2ee94da613685d45ebcbd13c3e(
    value: typing.Optional[KinesisAnalyticsApplicationOutputsLambda],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a97f2a4dc27117431053441ac60c68f20b348eb064ffb847abf586c33d369d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4f930a8e2521c750e209cb7ac92d11da026afa4e11966f938ee0328fea96de(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__969399ffabd63e35752d00872bfc3b25fa4a6a019e17c55465f2431f2b1f0269(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e38870a0f4638744a40a4eafaf66103d858440d6d583779c16b7ca812712c80(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2182e7fdaefa37cde440fda5d111c348108c238adb64db566652cbeb2adc20b1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21e661a8add121a9a3c2ef0764ec7db45c1e6d31934f2fb4e1fea00e94c225b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__793c48887a1d9067b1e8c0347386ccb341f78290851a8f2f4b6dc90f9cddce4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ae9abcedc0021e4e4e0b0aa210d23578b77897d834782d712b8f88d57022df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7862e8edbba7fc2a007fbe545f3fb19e3ad207a0eee6bbbfc5080d57b291ca42(
    value: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdfdade2205d1cfe0baded13c4cbd9320621b4a87e770f2114574c00435cc62f(
    *,
    record_format_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60af91b7b492c29d2dff05dcba9fc0dd0afacfaadfff4b402490b11f964f12e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98139dc162d6d599d999b3c98d167983516c9b02995905b0a6ff7822e368f64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac01c0a7e839d655016de601e4849d0af69c57afc2e43b3d9e586a3fe84facd1(
    value: typing.Optional[KinesisAnalyticsApplicationOutputsSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d6702b7210d26596762bb4d81c503ecee757538869efa2a46f18e4693d03f9(
    *,
    s3: typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesS3, typing.Dict[builtins.str, typing.Any]],
    schema: typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchema, typing.Dict[builtins.str, typing.Any]],
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a50c5a7698f28533229ae83d7ba0f11c0f7982671ad3948925a306c5ce84db6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b491d3e7dfc18265a3b57cc7f17389bbf3676539918b1ed562a4cada86c046df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77bf610773fbd72d0b4fdd3acc13ed8636f9230d121d34787d666c40c840e2e(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a188f1e276646c91f16b99a2dd0bc50357a4aa7e88ad6b326e314f210d1f0fb(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd2ab0118a1725a6a588f0f2bc4214c9981c783eec07b4cacd46b6841acdf86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d11c47b83a36c3e5a1427620e6cb077171ee38cef164e46f83f660e594a7e0f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bcd0a43f24549bc1e61f0542c601957f30d74190a6253084bc89bba03a9cca4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a6a04e2cbb1ed88a2d3e8e035913dc8b20122f4e1f6954ec7a0226cad8236aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d6d45f1eb9d1576426ad3f9a7e18112580ddbfb8ddd24327bd8e342543d0fba(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91042393769f603f2c7e23c974ae7daade0069243462dcbf1ee136baf007e28(
    *,
    record_columns: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, typing.Dict[builtins.str, typing.Any]]]],
    record_format: typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat, typing.Dict[builtins.str, typing.Any]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28364fa793cdf8213471898968d561085e73b6e2993302bc1bf0f24c7dca25f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dbe33566466f42bcd7a22e65096ddb8d50fa35797f27d6775af47533e0b1d5a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__641dcba00e75194580c9d03af30dd883794d313f56ceb10babd8320fa8435ef8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfdcead481d381d952852bc2907e04e4e4e0e28098522239ecb66ba2327b35f(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f61776fbed6f784c456d5d0885d14140a4008f1d30c953a2b45842cad261a42(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a2e15e81f71cf5cd329fdbe3c71f729a12c726e673eb59f8a7d81240e6d348(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043893725b2e487c8a6da14ebee338aec760e854eeee8210116139423eb56c0a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b70b86e0ce82930adfa5693bbc1a7b036f6ab6526edc1d88e1ed33b65dd9bfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c075254c325ba95984a35f018c833b004ba3aba2c83368580e7fa6656d27a71c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ef1f33dad5fe025388af2c2e6d007f0b3e554d55334f80c7b9b9790ca2bf75(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf489067c727da43ce8c890546d188826adc4fe1eba213422c2d24d973caf0a9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a94793bf0f393194a4ab032c8d1dec253a804c9615264f0935bf3b390847384(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__689cd48874f6703f13b1beaaaee6a3acde6549cc49cf31500f520b9a185bf66d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f4e16b26ba6193d64de89527939376a0979ab40e6bff40ef7a9ae058d61b62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922628cf4629b0ea6c319352cf99703dae868e7e8384bede44dc4ee77a0fb850(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85fec2cf6efd097128cf7b7cabffc71013386d2279b69aa72e8343916f4eaea(
    value: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9b999ea904a6d617d283ee366730b41881b2321bfb7e807cd7fe0dfbc67fb8(
    *,
    mapping_parameters: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a29350fba3c1e1d03dd496e47f2850a4673ebad29002c1735d9365d757550c(
    *,
    csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv, typing.Dict[builtins.str, typing.Any]]] = None,
    json: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a5013613de7a4a58a412abc444086f756a9ad926520fbf061ccf5696e50829(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531302b1ec0f049f237726a70d645928a5ab018f64332c004d7e1d17dc3ed3d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d4127a943f396cbfa57fc0d3f5e8fa07448f9f5032e96d7d15929e4fddfb04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44dd7b8e0af257784e474a3491984ba900815f86a190781dc3d5407eddbf555(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c15bd159e8cda037194d824c90f87fe00ab39a8a9e6fe1ccfdd4e8c4b5465f2c(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089746a7bce0c9dc00e739ab27cf97874a303d330a478454a4be8d0c35bce918(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06f03dd0b9dc733750dca4df4f904bbbbc289742f6be71a58c5ee83c0d644df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__519c0ff90c5a99be25d71cb904f09848dc1460e13626a2c10a7ebcc93ac346c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ec214b3a1e11382fa8b39b0cd341e7a7b47817fdd0ece5e78e66d80f37a9f1(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d4d6d26bc830752403fde2ac4d733299781ba59b8060d5faeb4fa97ba4246a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__989d4508391b38b5543cfddd97acf14c6b2a559f0b3bb68aa6a63bafcb2a4189(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4395cd1b3f8f740766ac869b4e0f4eda624ca7856d2b067ac4dc53c57183600a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5017ff7ffa3d18b47a0068c7ad9661923ca599a15593cd4946200344d7926e5(
    value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat],
) -> None:
    """Type checking stubs"""
    pass
