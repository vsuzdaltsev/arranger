'''
# `aws_kinesis_firehose_delivery_stream`

Refer to the Terraform Registory for docs: [`aws_kinesis_firehose_delivery_stream`](https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream).
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


class KinesisFirehoseDeliveryStream(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStream",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream aws_kinesis_firehose_delivery_stream}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        destination: builtins.str,
        name: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        destination_id: typing.Optional[builtins.str] = None,
        elasticsearch_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        extended_s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        http_endpoint_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kinesis_source_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        server_side_encryption: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamServerSideEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        splunk_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        version_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream aws_kinesis_firehose_delivery_stream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination KinesisFirehoseDeliveryStream#destination}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#arn KinesisFirehoseDeliveryStream#arn}.
        :param destination_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination_id KinesisFirehoseDeliveryStream#destination_id}.
        :param elasticsearch_configuration: elasticsearch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#elasticsearch_configuration KinesisFirehoseDeliveryStream#elasticsearch_configuration}
        :param extended_s3_configuration: extended_s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#extended_s3_configuration KinesisFirehoseDeliveryStream#extended_s3_configuration}
        :param http_endpoint_configuration: http_endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#http_endpoint_configuration KinesisFirehoseDeliveryStream#http_endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#id KinesisFirehoseDeliveryStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kinesis_source_configuration: kinesis_source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_source_configuration KinesisFirehoseDeliveryStream#kinesis_source_configuration}
        :param redshift_configuration: redshift_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#redshift_configuration KinesisFirehoseDeliveryStream#redshift_configuration}
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_configuration KinesisFirehoseDeliveryStream#s3_configuration}
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#server_side_encryption KinesisFirehoseDeliveryStream#server_side_encryption}
        :param splunk_configuration: splunk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#splunk_configuration KinesisFirehoseDeliveryStream#splunk_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags KinesisFirehoseDeliveryStream#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags_all KinesisFirehoseDeliveryStream#tags_all}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffdcf760735fbc16c405ea45dbf955fb65ff581a35f23e6b0a8e2477a8b3e315)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KinesisFirehoseDeliveryStreamConfig(
            destination=destination,
            name=name,
            arn=arn,
            destination_id=destination_id,
            elasticsearch_configuration=elasticsearch_configuration,
            extended_s3_configuration=extended_s3_configuration,
            http_endpoint_configuration=http_endpoint_configuration,
            id=id,
            kinesis_source_configuration=kinesis_source_configuration,
            redshift_configuration=redshift_configuration,
            s3_configuration=s3_configuration,
            server_side_encryption=server_side_encryption,
            splunk_configuration=splunk_configuration,
            tags=tags,
            tags_all=tags_all,
            version_id=version_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putElasticsearchConfiguration")
    def put_elasticsearch_configuration(
        self,
        *,
        index_name: builtins.str,
        role_arn: builtins.str,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_endpoint: typing.Optional[builtins.str] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        index_rotation_period: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param index_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_name KinesisFirehoseDeliveryStream#index_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param cluster_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_endpoint KinesisFirehoseDeliveryStream#cluster_endpoint}.
        :param domain_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#domain_arn KinesisFirehoseDeliveryStream#domain_arn}.
        :param index_rotation_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_rotation_period KinesisFirehoseDeliveryStream#index_rotation_period}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type_name KinesisFirehoseDeliveryStream#type_name}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#vpc_config KinesisFirehoseDeliveryStream#vpc_config}
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfiguration(
            index_name=index_name,
            role_arn=role_arn,
            buffering_interval=buffering_interval,
            buffering_size=buffering_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            cluster_endpoint=cluster_endpoint,
            domain_arn=domain_arn,
            index_rotation_period=index_rotation_period,
            processing_configuration=processing_configuration,
            retry_duration=retry_duration,
            s3_backup_mode=s3_backup_mode,
            type_name=type_name,
            vpc_config=vpc_config,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearchConfiguration", [value]))

    @jsii.member(jsii_name="putExtendedS3Configuration")
    def put_extended_s3_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        data_format_conversion_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        dynamic_partitioning_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param data_format_conversion_configuration: data_format_conversion_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_format_conversion_configuration KinesisFirehoseDeliveryStream#data_format_conversion_configuration}
        :param dynamic_partitioning_configuration: dynamic_partitioning_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dynamic_partitioning_configuration KinesisFirehoseDeliveryStream#dynamic_partitioning_configuration}
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3Configuration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            data_format_conversion_configuration=data_format_conversion_configuration,
            dynamic_partitioning_configuration=dynamic_partitioning_configuration,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
            processing_configuration=processing_configuration,
            s3_backup_configuration=s3_backup_configuration,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putExtendedS3Configuration", [value]))

    @jsii.member(jsii_name="putHttpEndpointConfiguration")
    def put_http_endpoint_configuration(
        self,
        *,
        url: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        request_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        role_arn: typing.Optional[builtins.str] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#url KinesisFirehoseDeliveryStream#url}.
        :param access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#access_key KinesisFirehoseDeliveryStream#access_key}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param request_configuration: request_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#request_configuration KinesisFirehoseDeliveryStream#request_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfiguration(
            url=url,
            access_key=access_key,
            buffering_interval=buffering_interval,
            buffering_size=buffering_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            name=name,
            processing_configuration=processing_configuration,
            request_configuration=request_configuration,
            retry_duration=retry_duration,
            role_arn=role_arn,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpEndpointConfiguration", [value]))

    @jsii.member(jsii_name="putKinesisSourceConfiguration")
    def put_kinesis_source_configuration(
        self,
        *,
        kinesis_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param kinesis_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_stream_arn KinesisFirehoseDeliveryStream#kinesis_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        '''
        value = KinesisFirehoseDeliveryStreamKinesisSourceConfiguration(
            kinesis_stream_arn=kinesis_stream_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisSourceConfiguration", [value]))

    @jsii.member(jsii_name="putRedshiftConfiguration")
    def put_redshift_configuration(
        self,
        *,
        cluster_jdbcurl: builtins.str,
        data_table_name: builtins.str,
        password: builtins.str,
        role_arn: builtins.str,
        username: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        copy_options: typing.Optional[builtins.str] = None,
        data_table_columns: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_jdbcurl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_jdbcurl KinesisFirehoseDeliveryStream#cluster_jdbcurl}.
        :param data_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_name KinesisFirehoseDeliveryStream#data_table_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#password KinesisFirehoseDeliveryStream#password}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#username KinesisFirehoseDeliveryStream#username}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param copy_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#copy_options KinesisFirehoseDeliveryStream#copy_options}.
        :param data_table_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_columns KinesisFirehoseDeliveryStream#data_table_columns}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfiguration(
            cluster_jdbcurl=cluster_jdbcurl,
            data_table_name=data_table_name,
            password=password,
            role_arn=role_arn,
            username=username,
            cloudwatch_logging_options=cloudwatch_logging_options,
            copy_options=copy_options,
            data_table_columns=data_table_columns,
            processing_configuration=processing_configuration,
            retry_duration=retry_duration,
            s3_backup_configuration=s3_backup_configuration,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshiftConfiguration", [value]))

    @jsii.member(jsii_name="putS3Configuration")
    def put_s3_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        value = KinesisFirehoseDeliveryStreamS3Configuration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Configuration", [value]))

    @jsii.member(jsii_name="putServerSideEncryption")
    def put_server_side_encryption(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        key_arn: typing.Optional[builtins.str] = None,
        key_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_arn KinesisFirehoseDeliveryStream#key_arn}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_type KinesisFirehoseDeliveryStream#key_type}.
        '''
        value = KinesisFirehoseDeliveryStreamServerSideEncryption(
            enabled=enabled, key_arn=key_arn, key_type=key_type
        )

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryption", [value]))

    @jsii.member(jsii_name="putSplunkConfiguration")
    def put_splunk_configuration(
        self,
        *,
        hec_endpoint: builtins.str,
        hec_token: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        hec_acknowledgment_timeout: typing.Optional[jsii.Number] = None,
        hec_endpoint_type: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hec_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint KinesisFirehoseDeliveryStream#hec_endpoint}.
        :param hec_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_token KinesisFirehoseDeliveryStream#hec_token}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param hec_acknowledgment_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_acknowledgment_timeout KinesisFirehoseDeliveryStream#hec_acknowledgment_timeout}.
        :param hec_endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint_type KinesisFirehoseDeliveryStream#hec_endpoint_type}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamSplunkConfiguration(
            hec_endpoint=hec_endpoint,
            hec_token=hec_token,
            cloudwatch_logging_options=cloudwatch_logging_options,
            hec_acknowledgment_timeout=hec_acknowledgment_timeout,
            hec_endpoint_type=hec_endpoint_type,
            processing_configuration=processing_configuration,
            retry_duration=retry_duration,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putSplunkConfiguration", [value]))

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetDestinationId")
    def reset_destination_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationId", []))

    @jsii.member(jsii_name="resetElasticsearchConfiguration")
    def reset_elasticsearch_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchConfiguration", []))

    @jsii.member(jsii_name="resetExtendedS3Configuration")
    def reset_extended_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedS3Configuration", []))

    @jsii.member(jsii_name="resetHttpEndpointConfiguration")
    def reset_http_endpoint_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpointConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKinesisSourceConfiguration")
    def reset_kinesis_source_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisSourceConfiguration", []))

    @jsii.member(jsii_name="resetRedshiftConfiguration")
    def reset_redshift_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshiftConfiguration", []))

    @jsii.member(jsii_name="resetS3Configuration")
    def reset_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Configuration", []))

    @jsii.member(jsii_name="resetServerSideEncryption")
    def reset_server_side_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryption", []))

    @jsii.member(jsii_name="resetSplunkConfiguration")
    def reset_splunk_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVersionId")
    def reset_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfiguration")
    def elasticsearch_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference", jsii.get(self, "elasticsearchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="extendedS3Configuration")
    def extended_s3_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference", jsii.get(self, "extendedS3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfiguration")
    def http_endpoint_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference", jsii.get(self, "httpEndpointConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSourceConfiguration")
    def kinesis_source_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference", jsii.get(self, "kinesisSourceConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference", jsii.get(self, "redshiftConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3Configuration")
    def s3_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference", jsii.get(self, "s3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> "KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference", jsii.get(self, "serverSideEncryption"))

    @builtins.property
    @jsii.member(jsii_name="splunkConfiguration")
    def splunk_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference", jsii.get(self, "splunkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationIdInput")
    def destination_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfigurationInput")
    def elasticsearch_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"], jsii.get(self, "elasticsearchConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedS3ConfigurationInput")
    def extended_s3_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"], jsii.get(self, "extendedS3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfigurationInput")
    def http_endpoint_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"], jsii.get(self, "httpEndpointConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSourceConfigurationInput")
    def kinesis_source_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"], jsii.get(self, "kinesisSourceConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftConfigurationInput")
    def redshift_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"], jsii.get(self, "redshiftConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigurationInput")
    def s3_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"], jsii.get(self, "s3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionInput")
    def server_side_encryption_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"], jsii.get(self, "serverSideEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkConfigurationInput")
    def splunk_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"], jsii.get(self, "splunkConfigurationInput"))

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
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d717aa472bb0bb697868caf7939bfd9ca574ccdc157f2478624741e3e78a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f897384a56d7ea48978028f45846c95c8189620fc6e97371b847a330da06aaf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="destinationId")
    def destination_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationId"))

    @destination_id.setter
    def destination_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e52a7c098dd6a8b5fd52df2799c43706d52938649f299d5fe9016dc1e74f67a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccdc63a0a7e294e7d2abe9c04b6bb75271725f397ffe122324f4a9e811f6caec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a814f9eb73145eee49a6fa244bbb06a4f7764aaf76c513e5b530764b7d920d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da0de7ed3801416d7c8322565af1305e49cc2b3e23c8a534b12c8656f6863cd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63c2f356f452b0eedc3be2e274bf71f929285a2b03685b370991d386d4d6763)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd9815a47ac27ac5da5d08d6f66275808774c2614402e987d8cee2e2db8b3976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination": "destination",
        "name": "name",
        "arn": "arn",
        "destination_id": "destinationId",
        "elasticsearch_configuration": "elasticsearchConfiguration",
        "extended_s3_configuration": "extendedS3Configuration",
        "http_endpoint_configuration": "httpEndpointConfiguration",
        "id": "id",
        "kinesis_source_configuration": "kinesisSourceConfiguration",
        "redshift_configuration": "redshiftConfiguration",
        "s3_configuration": "s3Configuration",
        "server_side_encryption": "serverSideEncryption",
        "splunk_configuration": "splunkConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "version_id": "versionId",
    },
)
class KinesisFirehoseDeliveryStreamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        destination: builtins.str,
        name: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        destination_id: typing.Optional[builtins.str] = None,
        elasticsearch_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        extended_s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        http_endpoint_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kinesis_source_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3Configuration", typing.Dict[builtins.str, typing.Any]]] = None,
        server_side_encryption: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamServerSideEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        splunk_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination KinesisFirehoseDeliveryStream#destination}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#arn KinesisFirehoseDeliveryStream#arn}.
        :param destination_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination_id KinesisFirehoseDeliveryStream#destination_id}.
        :param elasticsearch_configuration: elasticsearch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#elasticsearch_configuration KinesisFirehoseDeliveryStream#elasticsearch_configuration}
        :param extended_s3_configuration: extended_s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#extended_s3_configuration KinesisFirehoseDeliveryStream#extended_s3_configuration}
        :param http_endpoint_configuration: http_endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#http_endpoint_configuration KinesisFirehoseDeliveryStream#http_endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#id KinesisFirehoseDeliveryStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kinesis_source_configuration: kinesis_source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_source_configuration KinesisFirehoseDeliveryStream#kinesis_source_configuration}
        :param redshift_configuration: redshift_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#redshift_configuration KinesisFirehoseDeliveryStream#redshift_configuration}
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_configuration KinesisFirehoseDeliveryStream#s3_configuration}
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#server_side_encryption KinesisFirehoseDeliveryStream#server_side_encryption}
        :param splunk_configuration: splunk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#splunk_configuration KinesisFirehoseDeliveryStream#splunk_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags KinesisFirehoseDeliveryStream#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags_all KinesisFirehoseDeliveryStream#tags_all}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(elasticsearch_configuration, dict):
            elasticsearch_configuration = KinesisFirehoseDeliveryStreamElasticsearchConfiguration(**elasticsearch_configuration)
        if isinstance(extended_s3_configuration, dict):
            extended_s3_configuration = KinesisFirehoseDeliveryStreamExtendedS3Configuration(**extended_s3_configuration)
        if isinstance(http_endpoint_configuration, dict):
            http_endpoint_configuration = KinesisFirehoseDeliveryStreamHttpEndpointConfiguration(**http_endpoint_configuration)
        if isinstance(kinesis_source_configuration, dict):
            kinesis_source_configuration = KinesisFirehoseDeliveryStreamKinesisSourceConfiguration(**kinesis_source_configuration)
        if isinstance(redshift_configuration, dict):
            redshift_configuration = KinesisFirehoseDeliveryStreamRedshiftConfiguration(**redshift_configuration)
        if isinstance(s3_configuration, dict):
            s3_configuration = KinesisFirehoseDeliveryStreamS3Configuration(**s3_configuration)
        if isinstance(server_side_encryption, dict):
            server_side_encryption = KinesisFirehoseDeliveryStreamServerSideEncryption(**server_side_encryption)
        if isinstance(splunk_configuration, dict):
            splunk_configuration = KinesisFirehoseDeliveryStreamSplunkConfiguration(**splunk_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a736472808234f4035e4a387d31ec5e97cdbcfc656c63f8110cf238cd6a606fd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument destination_id", value=destination_id, expected_type=type_hints["destination_id"])
            check_type(argname="argument elasticsearch_configuration", value=elasticsearch_configuration, expected_type=type_hints["elasticsearch_configuration"])
            check_type(argname="argument extended_s3_configuration", value=extended_s3_configuration, expected_type=type_hints["extended_s3_configuration"])
            check_type(argname="argument http_endpoint_configuration", value=http_endpoint_configuration, expected_type=type_hints["http_endpoint_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kinesis_source_configuration", value=kinesis_source_configuration, expected_type=type_hints["kinesis_source_configuration"])
            check_type(argname="argument redshift_configuration", value=redshift_configuration, expected_type=type_hints["redshift_configuration"])
            check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
            check_type(argname="argument server_side_encryption", value=server_side_encryption, expected_type=type_hints["server_side_encryption"])
            check_type(argname="argument splunk_configuration", value=splunk_configuration, expected_type=type_hints["splunk_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
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
        if arn is not None:
            self._values["arn"] = arn
        if destination_id is not None:
            self._values["destination_id"] = destination_id
        if elasticsearch_configuration is not None:
            self._values["elasticsearch_configuration"] = elasticsearch_configuration
        if extended_s3_configuration is not None:
            self._values["extended_s3_configuration"] = extended_s3_configuration
        if http_endpoint_configuration is not None:
            self._values["http_endpoint_configuration"] = http_endpoint_configuration
        if id is not None:
            self._values["id"] = id
        if kinesis_source_configuration is not None:
            self._values["kinesis_source_configuration"] = kinesis_source_configuration
        if redshift_configuration is not None:
            self._values["redshift_configuration"] = redshift_configuration
        if s3_configuration is not None:
            self._values["s3_configuration"] = s3_configuration
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if splunk_configuration is not None:
            self._values["splunk_configuration"] = splunk_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if version_id is not None:
            self._values["version_id"] = version_id

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
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination KinesisFirehoseDeliveryStream#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#arn KinesisFirehoseDeliveryStream#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination_id KinesisFirehoseDeliveryStream#destination_id}.'''
        result = self._values.get("destination_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"]:
        '''elasticsearch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#elasticsearch_configuration KinesisFirehoseDeliveryStream#elasticsearch_configuration}
        '''
        result = self._values.get("elasticsearch_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"], result)

    @builtins.property
    def extended_s3_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"]:
        '''extended_s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#extended_s3_configuration KinesisFirehoseDeliveryStream#extended_s3_configuration}
        '''
        result = self._values.get("extended_s3_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"], result)

    @builtins.property
    def http_endpoint_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"]:
        '''http_endpoint_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#http_endpoint_configuration KinesisFirehoseDeliveryStream#http_endpoint_configuration}
        '''
        result = self._values.get("http_endpoint_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#id KinesisFirehoseDeliveryStream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesis_source_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"]:
        '''kinesis_source_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_source_configuration KinesisFirehoseDeliveryStream#kinesis_source_configuration}
        '''
        result = self._values.get("kinesis_source_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"], result)

    @builtins.property
    def redshift_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"]:
        '''redshift_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#redshift_configuration KinesisFirehoseDeliveryStream#redshift_configuration}
        '''
        result = self._values.get("redshift_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"], result)

    @builtins.property
    def s3_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"]:
        '''s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_configuration KinesisFirehoseDeliveryStream#s3_configuration}
        '''
        result = self._values.get("s3_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"], result)

    @builtins.property
    def server_side_encryption(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"]:
        '''server_side_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#server_side_encryption KinesisFirehoseDeliveryStream#server_side_encryption}
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"], result)

    @builtins.property
    def splunk_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"]:
        '''splunk_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#splunk_configuration KinesisFirehoseDeliveryStream#splunk_configuration}
        '''
        result = self._values.get("splunk_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags KinesisFirehoseDeliveryStream#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags_all KinesisFirehoseDeliveryStream#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.'''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "index_name": "indexName",
        "role_arn": "roleArn",
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "cluster_endpoint": "clusterEndpoint",
        "domain_arn": "domainArn",
        "index_rotation_period": "indexRotationPeriod",
        "processing_configuration": "processingConfiguration",
        "retry_duration": "retryDuration",
        "s3_backup_mode": "s3BackupMode",
        "type_name": "typeName",
        "vpc_config": "vpcConfig",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfiguration:
    def __init__(
        self,
        *,
        index_name: builtins.str,
        role_arn: builtins.str,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_endpoint: typing.Optional[builtins.str] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        index_rotation_period: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param index_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_name KinesisFirehoseDeliveryStream#index_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param cluster_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_endpoint KinesisFirehoseDeliveryStream#cluster_endpoint}.
        :param domain_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#domain_arn KinesisFirehoseDeliveryStream#domain_arn}.
        :param index_rotation_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_rotation_period KinesisFirehoseDeliveryStream#index_rotation_period}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type_name KinesisFirehoseDeliveryStream#type_name}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#vpc_config KinesisFirehoseDeliveryStream#vpc_config}
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(vpc_config, dict):
            vpc_config = KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(**vpc_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3866b378b6c277628dba5accc5fa2b99cef532a15a985cd61580ea359299ce4)
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument index_rotation_period", value=index_rotation_period, expected_type=type_hints["index_rotation_period"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_name": index_name,
            "role_arn": role_arn,
        }
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if cluster_endpoint is not None:
            self._values["cluster_endpoint"] = cluster_endpoint
        if domain_arn is not None:
            self._values["domain_arn"] = domain_arn
        if index_rotation_period is not None:
            self._values["index_rotation_period"] = index_rotation_period
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode
        if type_name is not None:
            self._values["type_name"] = type_name
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def index_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_name KinesisFirehoseDeliveryStream#index_name}.'''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffering_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.'''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.'''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def cluster_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_endpoint KinesisFirehoseDeliveryStream#cluster_endpoint}.'''
        result = self._values.get("cluster_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#domain_arn KinesisFirehoseDeliveryStream#domain_arn}.'''
        result = self._values.get("domain_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_rotation_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_rotation_period KinesisFirehoseDeliveryStream#index_rotation_period}.'''
        result = self._values.get("index_rotation_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type_name KinesisFirehoseDeliveryStream#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#vpc_config KinesisFirehoseDeliveryStream#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb959c80f91aba184d30429e40a63178ee3d103224ed6ed83bc3a32f4a8ccf98)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__629392c0654a624dbeae5445bb17fe82100c9ea300ecaad14b85d848261263c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__807c5e386f6c0b18e03b02cecf092ebdf2f4581f8c460246127a251ff34cdc15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b860cb123ddf3ca2c30ef4f715ce5fe7cc1896ec961558e65be7e5d0e6d221a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12c1317e693ea0ffcce77c8ff08e374a3ea31ec9238a76a5c3bb07934eac7a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c75c72a973b4aca71d48ce5131132149e594f1a8ac6a0c404542d4b77b6b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f70c891b5414a6758727dbeb952c887a877d60c5916d17a179054002219dead)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#security_group_ids KinesisFirehoseDeliveryStream#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#subnet_ids KinesisFirehoseDeliveryStream#subnet_ids}.
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(
            role_arn=role_arn,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetBufferingInterval")
    def reset_buffering_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingInterval", []))

    @jsii.member(jsii_name="resetBufferingSize")
    def reset_buffering_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetClusterEndpoint")
    def reset_cluster_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterEndpoint", []))

    @jsii.member(jsii_name="resetDomainArn")
    def reset_domain_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainArn", []))

    @jsii.member(jsii_name="resetIndexRotationPeriod")
    def reset_index_rotation_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexRotationPeriod", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="bufferingIntervalInput")
    def buffering_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingSizeInput")
    def buffering_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpointInput")
    def cluster_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="domainArnInput")
    def domain_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainArnInput"))

    @builtins.property
    @jsii.member(jsii_name="indexNameInput")
    def index_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexNameInput"))

    @builtins.property
    @jsii.member(jsii_name="indexRotationPeriodInput")
    def index_rotation_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexRotationPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingInterval")
    def buffering_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingInterval"))

    @buffering_interval.setter
    def buffering_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b544134facdfa9f389b3f9b0a662587188b68cb6389aaed59da1dba9a719821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferingSize")
    def buffering_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingSize"))

    @buffering_size.setter
    def buffering_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec6a4c2dc077ecfa9523b98645c5979674c3fd8036304d19abd112b154e02bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingSize", value)

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @cluster_endpoint.setter
    def cluster_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffd086d5a9c686077cdbcce2ca035a61e2ad217956c7da3c3a1ff5f1df85979b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainArn"))

    @domain_arn.setter
    def domain_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee77a46698e9336d86abcf4371da47dd865ba5436237f157ff7833176dc6dde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainArn", value)

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70661cbcd138c9ceb3862a2ca4241ecb49a26c82627e17f9ab6632244e366d96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="indexRotationPeriod")
    def index_rotation_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexRotationPeriod"))

    @index_rotation_period.setter
    def index_rotation_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae1bc3cf812a73d809239dd275d35d263ca5a68d28790768410ecff8dc44b12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexRotationPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eb5aec3116696eb280d4e907c78bf0579e840563c9032a89043fe92d0057365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41ee4264a27e253952a5e3f73c8b20a3f193245bcbe4b3beddd754aad8a9a6ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6851f333bb1a5d339ce0acd34602eb4a45823350f6abe1b8685bee407444365f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e391bc6098d5ab12f81cfb2cc872c74ddb95a5098f547326cdb66d80e33c635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d7b8ab5d4348ce246c4e2d1359e0d81c7df0d7ed350fd43474c87516102b63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed5c7b6de9610f839d0e67e0db1ab7a0a2e0d8cc3bdb40b21d19135a2d8af22)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2efd0834e37b7fec9d01915bb53980884c0ba57d56fc023b53e78ea2bfee74f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd59e0ed80fb7c9653fc9a92ea22007ef528617aa078928e9f7889c23acc843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__66652a3e164577763cb59585aa6aa3ce15acad14351be6b9e388f6e93356e46d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8007f3e90e42e14f046a890c3f3e0a8bec359300b9bc17c461e778aa02478f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f078dd5c36fb5012c877043086669c1bd275c82e9742c579841db96bbe8d3adc)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc18ad20b86cb4d59faa2d2ee08d1cf83c9a2627c84172119cd64fa5a28e77c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5e382f8c5186853c01f934866079e08b21e3e6aadef02d5b3b8edd488d58c89)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0250f865b040c83ccf187a7b5a515937f03a6d6e4a468b9827d6636bfcae751)
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
            type_hints = typing.get_type_hints(_typecheckingstub__53a3f205bf9e1e13cc45b85e9f1d2076060ab2828d75e86b64343656f030dc5a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1016ff1ab0dd88a7b53a5b1e59100126a520f171f518e82650d984c4dca27685)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172a8c68559d3a68769af101a5b3763d24b8ca10f342af2870b8709ae1ed395d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4f4f97ea0c5c9478b030c5ad1fb09a4344ebfbaa8897afa3926620472576394)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46aa47203522d0f1421fb81265ede36e1f5e52dcc45f9001ed4523ba036646a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7ad40870d157b5aa25ac715fd9ef8c2acafd8e995be4513b0f746b584532e5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31aee646a01d829978d0599eb871416baa8048354f7ae408edec2ffe01f00fee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e49131a9cb6e94fbf2222f11d0554e61819f2bf9a9c8d6149162e9ede2ef5434)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8941d40f0470dea2b39f00672cb5a32e0db232855700340bd36167de46da33ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44b57b8e03755bdc58cc709ac7ab3b2b45c5ebab7eccd4eebd8d80d70a35984)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd8b57727f64c6ee189fa0b5f9bf037bcd28ff4a7c5fb697c150b16087dab8d0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ec75ae2db6be93504c1b88b29ccbca04f434ec66179223cbb9adabc6e346e56)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0dbc29506b0a88cc039007104f566d01c72e112307724e461f96b8bf83e157ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e18777486deb3c9618635ba6d7a3c4d2e4d370b6ac69d1abdf3c686cc7bb3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce5c6480ff526358c67faff32ac0b00ab20d327d48b43b0cd4b07e812ddfef58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93dcd8783e3dac05a76170f880e99545f7b8b8d7dd6be5670bcb1ea785bd413c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31830755bcd37f9c77de4db011cc1e5220942835ee094664bcf6952c4abc266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98a1e6bb79bb584e3506f9c43f25975fa157d7599fd803a7a57750e2a3ef2923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#security_group_ids KinesisFirehoseDeliveryStream#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#subnet_ids KinesisFirehoseDeliveryStream#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5386ff726cfa4cdc91d5027e76e96c1afd27b6d4d4dc1dd0df9f33535212d14e)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#security_group_ids KinesisFirehoseDeliveryStream#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#subnet_ids KinesisFirehoseDeliveryStream#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22213e42917531a1cdae6ec5fe3a5b6d8c330c56d84a37d9146076631d24b2d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d059c162f828932b54fb5329552790bdc2b5b49ac28d87ee3d047db0384c99f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41cb6ebaf054e037c6330c9a347308066355f706cf4d8b8ea6da6afc8970fa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc98331fe1430e0eb44175ad26a1e51b868d09268fdb70a54247ef31e6939b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39d37bba539cdec8d294e9b447cb26cc2a5554481f338f62e02ec858bd2da96e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "data_format_conversion_configuration": "dataFormatConversionConfiguration",
        "dynamic_partitioning_configuration": "dynamicPartitioningConfiguration",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
        "processing_configuration": "processingConfiguration",
        "s3_backup_configuration": "s3BackupConfiguration",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3Configuration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        data_format_conversion_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        dynamic_partitioning_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param data_format_conversion_configuration: data_format_conversion_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_format_conversion_configuration KinesisFirehoseDeliveryStream#data_format_conversion_configuration}
        :param dynamic_partitioning_configuration: dynamic_partitioning_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dynamic_partitioning_configuration KinesisFirehoseDeliveryStream#dynamic_partitioning_configuration}
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(data_format_conversion_configuration, dict):
            data_format_conversion_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(**data_format_conversion_configuration)
        if isinstance(dynamic_partitioning_configuration, dict):
            dynamic_partitioning_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(**dynamic_partitioning_configuration)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(s3_backup_configuration, dict):
            s3_backup_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(**s3_backup_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec2f226a4d4ed0cfc5737aa2a016c0c5a79be8a8e781e4698fb0da22976e817e)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument data_format_conversion_configuration", value=data_format_conversion_configuration, expected_type=type_hints["data_format_conversion_configuration"])
            check_type(argname="argument dynamic_partitioning_configuration", value=dynamic_partitioning_configuration, expected_type=type_hints["dynamic_partitioning_configuration"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if data_format_conversion_configuration is not None:
            self._values["data_format_conversion_configuration"] = data_format_conversion_configuration
        if dynamic_partitioning_configuration is not None:
            self._values["dynamic_partitioning_configuration"] = dynamic_partitioning_configuration
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if s3_backup_configuration is not None:
            self._values["s3_backup_configuration"] = s3_backup_configuration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_format_conversion_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration"]:
        '''data_format_conversion_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_format_conversion_configuration KinesisFirehoseDeliveryStream#data_format_conversion_configuration}
        '''
        result = self._values.get("data_format_conversion_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration"], result)

    @builtins.property
    def dynamic_partitioning_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration"]:
        '''dynamic_partitioning_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dynamic_partitioning_configuration KinesisFirehoseDeliveryStream#dynamic_partitioning_configuration}
        '''
        result = self._values.get("dynamic_partitioning_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration"], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"], result)

    @builtins.property
    def s3_backup_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"]:
        '''s3_backup_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        '''
        result = self._values.get("s3_backup_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c9f5001b839cd714e1a69fde9d901e37703917fbe3dbd91ea56a07a2465916)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3e47753cb92680f79f6535c3e0839e3c415d4c46cd421353cbdf5bb1cd581ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ec9595ddcf30755005f844cd85565770efb67ca9a40b030573f62f29a1850f73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c9e2e1ef05fc1c08ea3a75257bf66b7b64fe88784f703f11e5b7578774c08e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f90b6985cca27614d4d6b01fd688bd50d5d505a6efa2204f9caa4fa9bfca1331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3352969c3cd0d9f470dda1ccb87be540f1042ba43a9bf6df6788b28d53c9f921)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "input_format_configuration": "inputFormatConfiguration",
        "output_format_configuration": "outputFormatConfiguration",
        "schema_configuration": "schemaConfiguration",
        "enabled": "enabled",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration:
    def __init__(
        self,
        *,
        input_format_configuration: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration", typing.Dict[builtins.str, typing.Any]],
        output_format_configuration: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration", typing.Dict[builtins.str, typing.Any]],
        schema_configuration: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param input_format_configuration: input_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#input_format_configuration KinesisFirehoseDeliveryStream#input_format_configuration}
        :param output_format_configuration: output_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#output_format_configuration KinesisFirehoseDeliveryStream#output_format_configuration}
        :param schema_configuration: schema_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#schema_configuration KinesisFirehoseDeliveryStream#schema_configuration}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        '''
        if isinstance(input_format_configuration, dict):
            input_format_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(**input_format_configuration)
        if isinstance(output_format_configuration, dict):
            output_format_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(**output_format_configuration)
        if isinstance(schema_configuration, dict):
            schema_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(**schema_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca95e9a905a5b63cdf325df6dab92904400afea83ee79fc92cb190f168c44fff)
            check_type(argname="argument input_format_configuration", value=input_format_configuration, expected_type=type_hints["input_format_configuration"])
            check_type(argname="argument output_format_configuration", value=output_format_configuration, expected_type=type_hints["output_format_configuration"])
            check_type(argname="argument schema_configuration", value=schema_configuration, expected_type=type_hints["schema_configuration"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_format_configuration": input_format_configuration,
            "output_format_configuration": output_format_configuration,
            "schema_configuration": schema_configuration,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def input_format_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration":
        '''input_format_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#input_format_configuration KinesisFirehoseDeliveryStream#input_format_configuration}
        '''
        result = self._values.get("input_format_configuration")
        assert result is not None, "Required property 'input_format_configuration' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration", result)

    @builtins.property
    def output_format_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration":
        '''output_format_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#output_format_configuration KinesisFirehoseDeliveryStream#output_format_configuration}
        '''
        result = self._values.get("output_format_configuration")
        assert result is not None, "Required property 'output_format_configuration' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration", result)

    @builtins.property
    def schema_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration":
        '''schema_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#schema_configuration KinesisFirehoseDeliveryStream#schema_configuration}
        '''
        result = self._values.get("schema_configuration")
        assert result is not None, "Required property 'schema_configuration' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration", result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration",
    jsii_struct_bases=[],
    name_mapping={"deserializer": "deserializer"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration:
    def __init__(
        self,
        *,
        deserializer: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param deserializer: deserializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#deserializer KinesisFirehoseDeliveryStream#deserializer}
        '''
        if isinstance(deserializer, dict):
            deserializer = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(**deserializer)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a660e6465758728c098958c772cf523a222b6523eeb6d7937a178eac3d844ff)
            check_type(argname="argument deserializer", value=deserializer, expected_type=type_hints["deserializer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deserializer": deserializer,
        }

    @builtins.property
    def deserializer(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer":
        '''deserializer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#deserializer KinesisFirehoseDeliveryStream#deserializer}
        '''
        result = self._values.get("deserializer")
        assert result is not None, "Required property 'deserializer' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer",
    jsii_struct_bases=[],
    name_mapping={
        "hive_json_ser_de": "hiveJsonSerDe",
        "open_x_json_ser_de": "openXJsonSerDe",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer:
    def __init__(
        self,
        *,
        hive_json_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe", typing.Dict[builtins.str, typing.Any]]] = None,
        open_x_json_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hive_json_ser_de: hive_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hive_json_ser_de KinesisFirehoseDeliveryStream#hive_json_ser_de}
        :param open_x_json_ser_de: open_x_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#open_x_json_ser_de KinesisFirehoseDeliveryStream#open_x_json_ser_de}
        '''
        if isinstance(hive_json_ser_de, dict):
            hive_json_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(**hive_json_ser_de)
        if isinstance(open_x_json_ser_de, dict):
            open_x_json_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(**open_x_json_ser_de)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__930cfdb3a41aab46fcbdf9a0f58bfce6823164da0012e696d9c2afb1f322d416)
            check_type(argname="argument hive_json_ser_de", value=hive_json_ser_de, expected_type=type_hints["hive_json_ser_de"])
            check_type(argname="argument open_x_json_ser_de", value=open_x_json_ser_de, expected_type=type_hints["open_x_json_ser_de"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hive_json_ser_de is not None:
            self._values["hive_json_ser_de"] = hive_json_ser_de
        if open_x_json_ser_de is not None:
            self._values["open_x_json_ser_de"] = open_x_json_ser_de

    @builtins.property
    def hive_json_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe"]:
        '''hive_json_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hive_json_ser_de KinesisFirehoseDeliveryStream#hive_json_ser_de}
        '''
        result = self._values.get("hive_json_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe"], result)

    @builtins.property
    def open_x_json_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe"]:
        '''open_x_json_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#open_x_json_ser_de KinesisFirehoseDeliveryStream#open_x_json_ser_de}
        '''
        result = self._values.get("open_x_json_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe",
    jsii_struct_bases=[],
    name_mapping={"timestamp_formats": "timestampFormats"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe:
    def __init__(
        self,
        *,
        timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param timestamp_formats: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#timestamp_formats KinesisFirehoseDeliveryStream#timestamp_formats}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50387e96602d954019d17e39667153420a8ed8c7665670b0e0432c7776320143)
            check_type(argname="argument timestamp_formats", value=timestamp_formats, expected_type=type_hints["timestamp_formats"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if timestamp_formats is not None:
            self._values["timestamp_formats"] = timestamp_formats

    @builtins.property
    def timestamp_formats(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#timestamp_formats KinesisFirehoseDeliveryStream#timestamp_formats}.'''
        result = self._values.get("timestamp_formats")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__409d21892f711f8af586aba4366f9f98a5f3a395e451ce76ea3deaef82efe7f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimestampFormats")
    def reset_timestamp_formats(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestampFormats", []))

    @builtins.property
    @jsii.member(jsii_name="timestampFormatsInput")
    def timestamp_formats_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "timestampFormatsInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampFormats")
    def timestamp_formats(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "timestampFormats"))

    @timestamp_formats.setter
    def timestamp_formats(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8f36d0e1f5252e42bdec9bca7e8df471e3cf4ca4533412e4ae08e7f6aa7900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timestampFormats", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f1c25b3407e383ecb5fb282b52a6400ca04affa73e18f723179efa052f88479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe",
    jsii_struct_bases=[],
    name_mapping={
        "case_insensitive": "caseInsensitive",
        "column_to_json_key_mappings": "columnToJsonKeyMappings",
        "convert_dots_in_json_keys_to_underscores": "convertDotsInJsonKeysToUnderscores",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe:
    def __init__(
        self,
        *,
        case_insensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        column_to_json_key_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param case_insensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#case_insensitive KinesisFirehoseDeliveryStream#case_insensitive}.
        :param column_to_json_key_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#column_to_json_key_mappings KinesisFirehoseDeliveryStream#column_to_json_key_mappings}.
        :param convert_dots_in_json_keys_to_underscores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#convert_dots_in_json_keys_to_underscores KinesisFirehoseDeliveryStream#convert_dots_in_json_keys_to_underscores}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590ada3fbb4229184dd0f4af77d57012dbe743b7404c04df81e5f6301d4da8d4)
            check_type(argname="argument case_insensitive", value=case_insensitive, expected_type=type_hints["case_insensitive"])
            check_type(argname="argument column_to_json_key_mappings", value=column_to_json_key_mappings, expected_type=type_hints["column_to_json_key_mappings"])
            check_type(argname="argument convert_dots_in_json_keys_to_underscores", value=convert_dots_in_json_keys_to_underscores, expected_type=type_hints["convert_dots_in_json_keys_to_underscores"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if case_insensitive is not None:
            self._values["case_insensitive"] = case_insensitive
        if column_to_json_key_mappings is not None:
            self._values["column_to_json_key_mappings"] = column_to_json_key_mappings
        if convert_dots_in_json_keys_to_underscores is not None:
            self._values["convert_dots_in_json_keys_to_underscores"] = convert_dots_in_json_keys_to_underscores

    @builtins.property
    def case_insensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#case_insensitive KinesisFirehoseDeliveryStream#case_insensitive}.'''
        result = self._values.get("case_insensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def column_to_json_key_mappings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#column_to_json_key_mappings KinesisFirehoseDeliveryStream#column_to_json_key_mappings}.'''
        result = self._values.get("column_to_json_key_mappings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def convert_dots_in_json_keys_to_underscores(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#convert_dots_in_json_keys_to_underscores KinesisFirehoseDeliveryStream#convert_dots_in_json_keys_to_underscores}.'''
        result = self._values.get("convert_dots_in_json_keys_to_underscores")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__365025d822af9986bf424aaa3d77ab0e417e4e9dc308d2ab1e211435f547b2c1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaseInsensitive")
    def reset_case_insensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaseInsensitive", []))

    @jsii.member(jsii_name="resetColumnToJsonKeyMappings")
    def reset_column_to_json_key_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumnToJsonKeyMappings", []))

    @jsii.member(jsii_name="resetConvertDotsInJsonKeysToUnderscores")
    def reset_convert_dots_in_json_keys_to_underscores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConvertDotsInJsonKeysToUnderscores", []))

    @builtins.property
    @jsii.member(jsii_name="caseInsensitiveInput")
    def case_insensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "caseInsensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="columnToJsonKeyMappingsInput")
    def column_to_json_key_mappings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "columnToJsonKeyMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="convertDotsInJsonKeysToUnderscoresInput")
    def convert_dots_in_json_keys_to_underscores_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "convertDotsInJsonKeysToUnderscoresInput"))

    @builtins.property
    @jsii.member(jsii_name="caseInsensitive")
    def case_insensitive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "caseInsensitive"))

    @case_insensitive.setter
    def case_insensitive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4b906f4503b7bffa587484f96175fdeda0ad9fc3f796a5de61222401e13fa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseInsensitive", value)

    @builtins.property
    @jsii.member(jsii_name="columnToJsonKeyMappings")
    def column_to_json_key_mappings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "columnToJsonKeyMappings"))

    @column_to_json_key_mappings.setter
    def column_to_json_key_mappings(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0583faaef1b37d0b6a46f6d20312d98ae0a029edaafaf6d382d08872006bc88a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnToJsonKeyMappings", value)

    @builtins.property
    @jsii.member(jsii_name="convertDotsInJsonKeysToUnderscores")
    def convert_dots_in_json_keys_to_underscores(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "convertDotsInJsonKeysToUnderscores"))

    @convert_dots_in_json_keys_to_underscores.setter
    def convert_dots_in_json_keys_to_underscores(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef6972ac56cb589844645be659c43b27741383e0f35fa6b638eaf946dce1a774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "convertDotsInJsonKeysToUnderscores", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1876743364208c9572630dbfc6d0fb399966a597a79a435434bfcdf6b945d811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35a3cda55fec7cbf67eedb318e409b2edf7c63a6c91ddad7cec734f0358fae5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHiveJsonSerDe")
    def put_hive_json_ser_de(
        self,
        *,
        timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param timestamp_formats: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#timestamp_formats KinesisFirehoseDeliveryStream#timestamp_formats}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(
            timestamp_formats=timestamp_formats
        )

        return typing.cast(None, jsii.invoke(self, "putHiveJsonSerDe", [value]))

    @jsii.member(jsii_name="putOpenXJsonSerDe")
    def put_open_x_json_ser_de(
        self,
        *,
        case_insensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        column_to_json_key_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param case_insensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#case_insensitive KinesisFirehoseDeliveryStream#case_insensitive}.
        :param column_to_json_key_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#column_to_json_key_mappings KinesisFirehoseDeliveryStream#column_to_json_key_mappings}.
        :param convert_dots_in_json_keys_to_underscores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#convert_dots_in_json_keys_to_underscores KinesisFirehoseDeliveryStream#convert_dots_in_json_keys_to_underscores}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(
            case_insensitive=case_insensitive,
            column_to_json_key_mappings=column_to_json_key_mappings,
            convert_dots_in_json_keys_to_underscores=convert_dots_in_json_keys_to_underscores,
        )

        return typing.cast(None, jsii.invoke(self, "putOpenXJsonSerDe", [value]))

    @jsii.member(jsii_name="resetHiveJsonSerDe")
    def reset_hive_json_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiveJsonSerDe", []))

    @jsii.member(jsii_name="resetOpenXJsonSerDe")
    def reset_open_x_json_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenXJsonSerDe", []))

    @builtins.property
    @jsii.member(jsii_name="hiveJsonSerDe")
    def hive_json_ser_de(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference, jsii.get(self, "hiveJsonSerDe"))

    @builtins.property
    @jsii.member(jsii_name="openXJsonSerDe")
    def open_x_json_ser_de(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference, jsii.get(self, "openXJsonSerDe"))

    @builtins.property
    @jsii.member(jsii_name="hiveJsonSerDeInput")
    def hive_json_ser_de_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe], jsii.get(self, "hiveJsonSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="openXJsonSerDeInput")
    def open_x_json_ser_de_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe], jsii.get(self, "openXJsonSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64701847d61fddd6bc57f9ff904f50fb0f97bb108eafaf8c8ac4f0429ab2b9bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__366b6fb3d362ce70a2be77fd6dcca309dc147af6f7a038d5c36177bfe7858b93)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeserializer")
    def put_deserializer(
        self,
        *,
        hive_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe, typing.Dict[builtins.str, typing.Any]]] = None,
        open_x_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hive_json_ser_de: hive_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hive_json_ser_de KinesisFirehoseDeliveryStream#hive_json_ser_de}
        :param open_x_json_ser_de: open_x_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#open_x_json_ser_de KinesisFirehoseDeliveryStream#open_x_json_ser_de}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(
            hive_json_ser_de=hive_json_ser_de, open_x_json_ser_de=open_x_json_ser_de
        )

        return typing.cast(None, jsii.invoke(self, "putDeserializer", [value]))

    @builtins.property
    @jsii.member(jsii_name="deserializer")
    def deserializer(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference, jsii.get(self, "deserializer"))

    @builtins.property
    @jsii.member(jsii_name="deserializerInput")
    def deserializer_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer], jsii.get(self, "deserializerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__165d7e2622c66a6bd311d4bb90289880c1d200a3d6199e4b84403880dd4a55dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration",
    jsii_struct_bases=[],
    name_mapping={"serializer": "serializer"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration:
    def __init__(
        self,
        *,
        serializer: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param serializer: serializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#serializer KinesisFirehoseDeliveryStream#serializer}
        '''
        if isinstance(serializer, dict):
            serializer = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(**serializer)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb9a4a866c6eebc773c33adbba42d4748e5e91cd0183a7cb1edb8d9b09aa637d)
            check_type(argname="argument serializer", value=serializer, expected_type=type_hints["serializer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "serializer": serializer,
        }

    @builtins.property
    def serializer(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer":
        '''serializer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#serializer KinesisFirehoseDeliveryStream#serializer}
        '''
        result = self._values.get("serializer")
        assert result is not None, "Required property 'serializer' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5ed7652d15d0ab2676497e82245768731b18caf67e331506ee4adbf6122284f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSerializer")
    def put_serializer(
        self,
        *,
        orc_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe", typing.Dict[builtins.str, typing.Any]]] = None,
        parquet_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param orc_ser_de: orc_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#orc_ser_de KinesisFirehoseDeliveryStream#orc_ser_de}
        :param parquet_ser_de: parquet_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parquet_ser_de KinesisFirehoseDeliveryStream#parquet_ser_de}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(
            orc_ser_de=orc_ser_de, parquet_ser_de=parquet_ser_de
        )

        return typing.cast(None, jsii.invoke(self, "putSerializer", [value]))

    @builtins.property
    @jsii.member(jsii_name="serializer")
    def serializer(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference", jsii.get(self, "serializer"))

    @builtins.property
    @jsii.member(jsii_name="serializerInput")
    def serializer_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer"], jsii.get(self, "serializerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c2bd34d3fd2bc05920699f6d629162c47361639bb8277c177477b536640e0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer",
    jsii_struct_bases=[],
    name_mapping={"orc_ser_de": "orcSerDe", "parquet_ser_de": "parquetSerDe"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer:
    def __init__(
        self,
        *,
        orc_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe", typing.Dict[builtins.str, typing.Any]]] = None,
        parquet_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param orc_ser_de: orc_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#orc_ser_de KinesisFirehoseDeliveryStream#orc_ser_de}
        :param parquet_ser_de: parquet_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parquet_ser_de KinesisFirehoseDeliveryStream#parquet_ser_de}
        '''
        if isinstance(orc_ser_de, dict):
            orc_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(**orc_ser_de)
        if isinstance(parquet_ser_de, dict):
            parquet_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(**parquet_ser_de)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae891e7dec21aa17cd81e339787be0c8d3359177aff16ab0e8e78a592e6e4a6)
            check_type(argname="argument orc_ser_de", value=orc_ser_de, expected_type=type_hints["orc_ser_de"])
            check_type(argname="argument parquet_ser_de", value=parquet_ser_de, expected_type=type_hints["parquet_ser_de"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if orc_ser_de is not None:
            self._values["orc_ser_de"] = orc_ser_de
        if parquet_ser_de is not None:
            self._values["parquet_ser_de"] = parquet_ser_de

    @builtins.property
    def orc_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe"]:
        '''orc_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#orc_ser_de KinesisFirehoseDeliveryStream#orc_ser_de}
        '''
        result = self._values.get("orc_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe"], result)

    @builtins.property
    def parquet_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"]:
        '''parquet_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parquet_ser_de KinesisFirehoseDeliveryStream#parquet_ser_de}
        '''
        result = self._values.get("parquet_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe",
    jsii_struct_bases=[],
    name_mapping={
        "block_size_bytes": "blockSizeBytes",
        "bloom_filter_columns": "bloomFilterColumns",
        "bloom_filter_false_positive_probability": "bloomFilterFalsePositiveProbability",
        "compression": "compression",
        "dictionary_key_threshold": "dictionaryKeyThreshold",
        "enable_padding": "enablePadding",
        "format_version": "formatVersion",
        "padding_tolerance": "paddingTolerance",
        "row_index_stride": "rowIndexStride",
        "stripe_size_bytes": "stripeSizeBytes",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe:
    def __init__(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        dictionary_key_threshold: typing.Optional[jsii.Number] = None,
        enable_padding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        format_version: typing.Optional[builtins.str] = None,
        padding_tolerance: typing.Optional[jsii.Number] = None,
        row_index_stride: typing.Optional[jsii.Number] = None,
        stripe_size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param bloom_filter_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_columns KinesisFirehoseDeliveryStream#bloom_filter_columns}.
        :param bloom_filter_false_positive_probability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_false_positive_probability KinesisFirehoseDeliveryStream#bloom_filter_false_positive_probability}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param dictionary_key_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dictionary_key_threshold KinesisFirehoseDeliveryStream#dictionary_key_threshold}.
        :param enable_padding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_padding KinesisFirehoseDeliveryStream#enable_padding}.
        :param format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#format_version KinesisFirehoseDeliveryStream#format_version}.
        :param padding_tolerance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#padding_tolerance KinesisFirehoseDeliveryStream#padding_tolerance}.
        :param row_index_stride: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#row_index_stride KinesisFirehoseDeliveryStream#row_index_stride}.
        :param stripe_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#stripe_size_bytes KinesisFirehoseDeliveryStream#stripe_size_bytes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4fd36fe2476bc4db7dace2331bed14c30397656c912440b953b125fba04105)
            check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
            check_type(argname="argument bloom_filter_columns", value=bloom_filter_columns, expected_type=type_hints["bloom_filter_columns"])
            check_type(argname="argument bloom_filter_false_positive_probability", value=bloom_filter_false_positive_probability, expected_type=type_hints["bloom_filter_false_positive_probability"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument dictionary_key_threshold", value=dictionary_key_threshold, expected_type=type_hints["dictionary_key_threshold"])
            check_type(argname="argument enable_padding", value=enable_padding, expected_type=type_hints["enable_padding"])
            check_type(argname="argument format_version", value=format_version, expected_type=type_hints["format_version"])
            check_type(argname="argument padding_tolerance", value=padding_tolerance, expected_type=type_hints["padding_tolerance"])
            check_type(argname="argument row_index_stride", value=row_index_stride, expected_type=type_hints["row_index_stride"])
            check_type(argname="argument stripe_size_bytes", value=stripe_size_bytes, expected_type=type_hints["stripe_size_bytes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if block_size_bytes is not None:
            self._values["block_size_bytes"] = block_size_bytes
        if bloom_filter_columns is not None:
            self._values["bloom_filter_columns"] = bloom_filter_columns
        if bloom_filter_false_positive_probability is not None:
            self._values["bloom_filter_false_positive_probability"] = bloom_filter_false_positive_probability
        if compression is not None:
            self._values["compression"] = compression
        if dictionary_key_threshold is not None:
            self._values["dictionary_key_threshold"] = dictionary_key_threshold
        if enable_padding is not None:
            self._values["enable_padding"] = enable_padding
        if format_version is not None:
            self._values["format_version"] = format_version
        if padding_tolerance is not None:
            self._values["padding_tolerance"] = padding_tolerance
        if row_index_stride is not None:
            self._values["row_index_stride"] = row_index_stride
        if stripe_size_bytes is not None:
            self._values["stripe_size_bytes"] = stripe_size_bytes

    @builtins.property
    def block_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.'''
        result = self._values.get("block_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bloom_filter_columns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_columns KinesisFirehoseDeliveryStream#bloom_filter_columns}.'''
        result = self._values.get("bloom_filter_columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bloom_filter_false_positive_probability(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_false_positive_probability KinesisFirehoseDeliveryStream#bloom_filter_false_positive_probability}.'''
        result = self._values.get("bloom_filter_false_positive_probability")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.'''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dictionary_key_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dictionary_key_threshold KinesisFirehoseDeliveryStream#dictionary_key_threshold}.'''
        result = self._values.get("dictionary_key_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_padding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_padding KinesisFirehoseDeliveryStream#enable_padding}.'''
        result = self._values.get("enable_padding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def format_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#format_version KinesisFirehoseDeliveryStream#format_version}.'''
        result = self._values.get("format_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_tolerance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#padding_tolerance KinesisFirehoseDeliveryStream#padding_tolerance}.'''
        result = self._values.get("padding_tolerance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def row_index_stride(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#row_index_stride KinesisFirehoseDeliveryStream#row_index_stride}.'''
        result = self._values.get("row_index_stride")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stripe_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#stripe_size_bytes KinesisFirehoseDeliveryStream#stripe_size_bytes}.'''
        result = self._values.get("stripe_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77f80109d423ba7901f8ef04fd83e4139b4f27cefb7de12ebddde3a4cc2e2579)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBlockSizeBytes")
    def reset_block_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockSizeBytes", []))

    @jsii.member(jsii_name="resetBloomFilterColumns")
    def reset_bloom_filter_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBloomFilterColumns", []))

    @jsii.member(jsii_name="resetBloomFilterFalsePositiveProbability")
    def reset_bloom_filter_false_positive_probability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBloomFilterFalsePositiveProbability", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetDictionaryKeyThreshold")
    def reset_dictionary_key_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDictionaryKeyThreshold", []))

    @jsii.member(jsii_name="resetEnablePadding")
    def reset_enable_padding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePadding", []))

    @jsii.member(jsii_name="resetFormatVersion")
    def reset_format_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormatVersion", []))

    @jsii.member(jsii_name="resetPaddingTolerance")
    def reset_padding_tolerance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingTolerance", []))

    @jsii.member(jsii_name="resetRowIndexStride")
    def reset_row_index_stride(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRowIndexStride", []))

    @jsii.member(jsii_name="resetStripeSizeBytes")
    def reset_stripe_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStripeSizeBytes", []))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytesInput")
    def block_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="bloomFilterColumnsInput")
    def bloom_filter_columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bloomFilterColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="bloomFilterFalsePositiveProbabilityInput")
    def bloom_filter_false_positive_probability_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bloomFilterFalsePositiveProbabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="dictionaryKeyThresholdInput")
    def dictionary_key_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dictionaryKeyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePaddingInput")
    def enable_padding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enablePaddingInput"))

    @builtins.property
    @jsii.member(jsii_name="formatVersionInput")
    def format_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingToleranceInput")
    def padding_tolerance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "paddingToleranceInput"))

    @builtins.property
    @jsii.member(jsii_name="rowIndexStrideInput")
    def row_index_stride_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowIndexStrideInput"))

    @builtins.property
    @jsii.member(jsii_name="stripeSizeBytesInput")
    def stripe_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stripeSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytes")
    def block_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockSizeBytes"))

    @block_size_bytes.setter
    def block_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f1fce1c08be3bc49571add75413ebd3811f7aed943161ce3f5b3031c0bae28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="bloomFilterColumns")
    def bloom_filter_columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bloomFilterColumns"))

    @bloom_filter_columns.setter
    def bloom_filter_columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41efc3a6a85411d1adab5cbe7308137caaf5bc98ad5ac67af5664c8f9ef1da82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bloomFilterColumns", value)

    @builtins.property
    @jsii.member(jsii_name="bloomFilterFalsePositiveProbability")
    def bloom_filter_false_positive_probability(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bloomFilterFalsePositiveProbability"))

    @bloom_filter_false_positive_probability.setter
    def bloom_filter_false_positive_probability(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9b46d017e34512be1ae8a276aa994ea0750f5ae715f7204dcc3aa99e2349dd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bloomFilterFalsePositiveProbability", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a69e6c431d4880aaa7f01977c00acf112a8e5abee32a492821a2ed6856e1e66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="dictionaryKeyThreshold")
    def dictionary_key_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dictionaryKeyThreshold"))

    @dictionary_key_threshold.setter
    def dictionary_key_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec5351973d737ce4e7698a7d0704265d7766f44286406a400014ffee3377f03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dictionaryKeyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="enablePadding")
    def enable_padding(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enablePadding"))

    @enable_padding.setter
    def enable_padding(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b76326f9e6450d06c1837fb5e57c0f676ccd1da4e036e2c85c5c5dd868268e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePadding", value)

    @builtins.property
    @jsii.member(jsii_name="formatVersion")
    def format_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formatVersion"))

    @format_version.setter
    def format_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da2e7fb2087338ecb654d6b938d13d97a7ff875ad79fd5337f7b3471098ca70c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="paddingTolerance")
    def padding_tolerance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "paddingTolerance"))

    @padding_tolerance.setter
    def padding_tolerance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba27aea00e12cf604dcf6bebd28ee88cc452b669e0937b1584db77a6e5951c85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingTolerance", value)

    @builtins.property
    @jsii.member(jsii_name="rowIndexStride")
    def row_index_stride(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowIndexStride"))

    @row_index_stride.setter
    def row_index_stride(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8356799cb9b8180e3cfb6deb9f59c2d997ad9059c63cba23e9d032a4ee6eb658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowIndexStride", value)

    @builtins.property
    @jsii.member(jsii_name="stripeSizeBytes")
    def stripe_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stripeSizeBytes"))

    @stripe_size_bytes.setter
    def stripe_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18cb825299ea43fd12a9f32edde0bcea7657bb43c27906c302cb4f79edfb55bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripeSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26a82ebed6337020038ccff90607c7038ae2d2c6e598baf40e68bd700f101cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0ccf329794c98d4bc787baa582ef94abc1861334f53428c51f9e6fd32dea3c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOrcSerDe")
    def put_orc_ser_de(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        dictionary_key_threshold: typing.Optional[jsii.Number] = None,
        enable_padding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        format_version: typing.Optional[builtins.str] = None,
        padding_tolerance: typing.Optional[jsii.Number] = None,
        row_index_stride: typing.Optional[jsii.Number] = None,
        stripe_size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param bloom_filter_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_columns KinesisFirehoseDeliveryStream#bloom_filter_columns}.
        :param bloom_filter_false_positive_probability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_false_positive_probability KinesisFirehoseDeliveryStream#bloom_filter_false_positive_probability}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param dictionary_key_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dictionary_key_threshold KinesisFirehoseDeliveryStream#dictionary_key_threshold}.
        :param enable_padding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_padding KinesisFirehoseDeliveryStream#enable_padding}.
        :param format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#format_version KinesisFirehoseDeliveryStream#format_version}.
        :param padding_tolerance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#padding_tolerance KinesisFirehoseDeliveryStream#padding_tolerance}.
        :param row_index_stride: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#row_index_stride KinesisFirehoseDeliveryStream#row_index_stride}.
        :param stripe_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#stripe_size_bytes KinesisFirehoseDeliveryStream#stripe_size_bytes}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(
            block_size_bytes=block_size_bytes,
            bloom_filter_columns=bloom_filter_columns,
            bloom_filter_false_positive_probability=bloom_filter_false_positive_probability,
            compression=compression,
            dictionary_key_threshold=dictionary_key_threshold,
            enable_padding=enable_padding,
            format_version=format_version,
            padding_tolerance=padding_tolerance,
            row_index_stride=row_index_stride,
            stripe_size_bytes=stripe_size_bytes,
        )

        return typing.cast(None, jsii.invoke(self, "putOrcSerDe", [value]))

    @jsii.member(jsii_name="putParquetSerDe")
    def put_parquet_ser_de(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_padding_bytes: typing.Optional[jsii.Number] = None,
        page_size_bytes: typing.Optional[jsii.Number] = None,
        writer_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param enable_dictionary_compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_dictionary_compression KinesisFirehoseDeliveryStream#enable_dictionary_compression}.
        :param max_padding_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#max_padding_bytes KinesisFirehoseDeliveryStream#max_padding_bytes}.
        :param page_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#page_size_bytes KinesisFirehoseDeliveryStream#page_size_bytes}.
        :param writer_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#writer_version KinesisFirehoseDeliveryStream#writer_version}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(
            block_size_bytes=block_size_bytes,
            compression=compression,
            enable_dictionary_compression=enable_dictionary_compression,
            max_padding_bytes=max_padding_bytes,
            page_size_bytes=page_size_bytes,
            writer_version=writer_version,
        )

        return typing.cast(None, jsii.invoke(self, "putParquetSerDe", [value]))

    @jsii.member(jsii_name="resetOrcSerDe")
    def reset_orc_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrcSerDe", []))

    @jsii.member(jsii_name="resetParquetSerDe")
    def reset_parquet_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetSerDe", []))

    @builtins.property
    @jsii.member(jsii_name="orcSerDe")
    def orc_ser_de(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference, jsii.get(self, "orcSerDe"))

    @builtins.property
    @jsii.member(jsii_name="parquetSerDe")
    def parquet_ser_de(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference", jsii.get(self, "parquetSerDe"))

    @builtins.property
    @jsii.member(jsii_name="orcSerDeInput")
    def orc_ser_de_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe], jsii.get(self, "orcSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetSerDeInput")
    def parquet_ser_de_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"], jsii.get(self, "parquetSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66832fd8b9a7ce143e3880fbba61048f7ae2400c0aee6514698772c6749bb1c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe",
    jsii_struct_bases=[],
    name_mapping={
        "block_size_bytes": "blockSizeBytes",
        "compression": "compression",
        "enable_dictionary_compression": "enableDictionaryCompression",
        "max_padding_bytes": "maxPaddingBytes",
        "page_size_bytes": "pageSizeBytes",
        "writer_version": "writerVersion",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe:
    def __init__(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_padding_bytes: typing.Optional[jsii.Number] = None,
        page_size_bytes: typing.Optional[jsii.Number] = None,
        writer_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param enable_dictionary_compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_dictionary_compression KinesisFirehoseDeliveryStream#enable_dictionary_compression}.
        :param max_padding_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#max_padding_bytes KinesisFirehoseDeliveryStream#max_padding_bytes}.
        :param page_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#page_size_bytes KinesisFirehoseDeliveryStream#page_size_bytes}.
        :param writer_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#writer_version KinesisFirehoseDeliveryStream#writer_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94f4a81e2a5a84e3f54816ada8e062d0817088c25e1c92ee85538036625123c)
            check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument enable_dictionary_compression", value=enable_dictionary_compression, expected_type=type_hints["enable_dictionary_compression"])
            check_type(argname="argument max_padding_bytes", value=max_padding_bytes, expected_type=type_hints["max_padding_bytes"])
            check_type(argname="argument page_size_bytes", value=page_size_bytes, expected_type=type_hints["page_size_bytes"])
            check_type(argname="argument writer_version", value=writer_version, expected_type=type_hints["writer_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if block_size_bytes is not None:
            self._values["block_size_bytes"] = block_size_bytes
        if compression is not None:
            self._values["compression"] = compression
        if enable_dictionary_compression is not None:
            self._values["enable_dictionary_compression"] = enable_dictionary_compression
        if max_padding_bytes is not None:
            self._values["max_padding_bytes"] = max_padding_bytes
        if page_size_bytes is not None:
            self._values["page_size_bytes"] = page_size_bytes
        if writer_version is not None:
            self._values["writer_version"] = writer_version

    @builtins.property
    def block_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.'''
        result = self._values.get("block_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.'''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_dictionary_compression(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_dictionary_compression KinesisFirehoseDeliveryStream#enable_dictionary_compression}.'''
        result = self._values.get("enable_dictionary_compression")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def max_padding_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#max_padding_bytes KinesisFirehoseDeliveryStream#max_padding_bytes}.'''
        result = self._values.get("max_padding_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def page_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#page_size_bytes KinesisFirehoseDeliveryStream#page_size_bytes}.'''
        result = self._values.get("page_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def writer_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#writer_version KinesisFirehoseDeliveryStream#writer_version}.'''
        result = self._values.get("writer_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b46209cfe193b37dccbb06f348ee4c2fcf6b21eb31f07a3d78051f89ab6308c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBlockSizeBytes")
    def reset_block_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockSizeBytes", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetEnableDictionaryCompression")
    def reset_enable_dictionary_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDictionaryCompression", []))

    @jsii.member(jsii_name="resetMaxPaddingBytes")
    def reset_max_padding_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPaddingBytes", []))

    @jsii.member(jsii_name="resetPageSizeBytes")
    def reset_page_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPageSizeBytes", []))

    @jsii.member(jsii_name="resetWriterVersion")
    def reset_writer_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriterVersion", []))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytesInput")
    def block_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDictionaryCompressionInput")
    def enable_dictionary_compression_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDictionaryCompressionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPaddingBytesInput")
    def max_padding_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPaddingBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="pageSizeBytesInput")
    def page_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pageSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="writerVersionInput")
    def writer_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytes")
    def block_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockSizeBytes"))

    @block_size_bytes.setter
    def block_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b66b4d447e66471523cc341d4ab13daa786c56d1cfac6d6e5a26bd2aa044260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41d0ae4a4d93d4e716171d9be2669329fb7c956d04f20191338806e8be330f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="enableDictionaryCompression")
    def enable_dictionary_compression(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDictionaryCompression"))

    @enable_dictionary_compression.setter
    def enable_dictionary_compression(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58574534c8af72e68605aaa0708dee0c5dde3221e09d8f52f93cdc865771f7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDictionaryCompression", value)

    @builtins.property
    @jsii.member(jsii_name="maxPaddingBytes")
    def max_padding_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPaddingBytes"))

    @max_padding_bytes.setter
    def max_padding_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8aaea54b882c268c2d4c5a141c921ba8d4a8dcf66d7fbab8dd2f8e32493d805)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPaddingBytes", value)

    @builtins.property
    @jsii.member(jsii_name="pageSizeBytes")
    def page_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pageSizeBytes"))

    @page_size_bytes.setter
    def page_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8f00bfa7db9196572f462a26090e1dcb42b27363561e301c9cb18268cccd832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pageSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="writerVersion")
    def writer_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writerVersion"))

    @writer_version.setter
    def writer_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed127e2e92c888aa3ea87f8dbc157d5163fba19830a1b4b6df15bf026fae0834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85f53519cec78a65a22c6432f91a0deef7eccc4efd69cbdffd8be42eb573f6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4f5a354e2711ececcbf613e80d1a24e9cb60c9c92ed57baa7ac99bfd7cc05e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInputFormatConfiguration")
    def put_input_format_configuration(
        self,
        *,
        deserializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param deserializer: deserializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#deserializer KinesisFirehoseDeliveryStream#deserializer}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(
            deserializer=deserializer
        )

        return typing.cast(None, jsii.invoke(self, "putInputFormatConfiguration", [value]))

    @jsii.member(jsii_name="putOutputFormatConfiguration")
    def put_output_format_configuration(
        self,
        *,
        serializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param serializer: serializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#serializer KinesisFirehoseDeliveryStream#serializer}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(
            serializer=serializer
        )

        return typing.cast(None, jsii.invoke(self, "putOutputFormatConfiguration", [value]))

    @jsii.member(jsii_name="putSchemaConfiguration")
    def put_schema_configuration(
        self,
        *,
        database_name: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#database_name KinesisFirehoseDeliveryStream#database_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#table_name KinesisFirehoseDeliveryStream#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#catalog_id KinesisFirehoseDeliveryStream#catalog_id}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#region KinesisFirehoseDeliveryStream#region}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(
            database_name=database_name,
            role_arn=role_arn,
            table_name=table_name,
            catalog_id=catalog_id,
            region=region,
            version_id=version_id,
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaConfiguration", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="inputFormatConfiguration")
    def input_format_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference, jsii.get(self, "inputFormatConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatConfiguration")
    def output_format_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference, jsii.get(self, "outputFormatConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="schemaConfiguration")
    def schema_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference", jsii.get(self, "schemaConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="inputFormatConfigurationInput")
    def input_format_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration], jsii.get(self, "inputFormatConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatConfigurationInput")
    def output_format_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration], jsii.get(self, "outputFormatConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaConfigurationInput")
    def schema_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration"], jsii.get(self, "schemaConfigurationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__5a0864054a0e236c32276e5a31b6318a22d175c8b3d44f3fee710712335133c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed90cc8bcb1fe89cd72ebafcc15caab823c7880a0d6a714d947347379d8b066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "role_arn": "roleArn",
        "table_name": "tableName",
        "catalog_id": "catalogId",
        "region": "region",
        "version_id": "versionId",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#database_name KinesisFirehoseDeliveryStream#database_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#table_name KinesisFirehoseDeliveryStream#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#catalog_id KinesisFirehoseDeliveryStream#catalog_id}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#region KinesisFirehoseDeliveryStream#region}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e723402de6be490a47ab6dc5828a6679ce255c958a9f380a620667de25409f8)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "role_arn": role_arn,
            "table_name": table_name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if region is not None:
            self._values["region"] = region
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#database_name KinesisFirehoseDeliveryStream#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#table_name KinesisFirehoseDeliveryStream#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#catalog_id KinesisFirehoseDeliveryStream#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#region KinesisFirehoseDeliveryStream#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.'''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f79a0f386ec6b96915d08da529312c22ae1d98d494f35dcbdf6f2f1c7c214f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetVersionId")
    def reset_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85eafbec27e10ac27c73bfdebf44981656349184c967abbf84a81f63f24f3afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b60bf1c7b4b9441e9d90a153bc611612cffac0e97fc7fa905e960b2954ec62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2102e426d296488d211bcc004ed2d0095d5cd0607d7dfbce02fbbb11703ed270)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3535e18441b6c87d13ba8f0eb467e8817fd9a9fc802ded10e66c1e52c43349fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b4a7baa2895e69450d8fb2c964a5e460252223e548439f8e9c5e3d2efd64bde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a31bf2c28c50ff29f369595c2f5db6fe11978b74de004a89d280da2605e522f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72fa1189c9e4c0d670cf186c8102885e53e059d42b969961b6f3b670606dece4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "retry_duration": "retryDuration"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f63a634b5239ba3078dcd3e9b73e52c413ae3be57c9689ab8aa876b50a688c)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__68c6c5e48581128edfc2f9b69141999928044fc27e50b3b4a0f3a4a35ee9e6bd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__15b20cb4e33f91e01089d3c70b9534b80527ea1ee31764093094962d55b0c515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d02ac1c449bf8c8d994cb5b821845a6604f4d4e7674deff6d57401158ff6d429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a030566b36aaa0928bd0642fdc654a74e0c8ec2a5f45d9f0c9b4b4f48ee22b46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5521d1ad307d36f19667d289ec2e5d168673d43c3c06ef97eda3d9885b2bfe0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putDataFormatConversionConfiguration")
    def put_data_format_conversion_configuration(
        self,
        *,
        input_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration, typing.Dict[builtins.str, typing.Any]],
        output_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration, typing.Dict[builtins.str, typing.Any]],
        schema_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration, typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param input_format_configuration: input_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#input_format_configuration KinesisFirehoseDeliveryStream#input_format_configuration}
        :param output_format_configuration: output_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#output_format_configuration KinesisFirehoseDeliveryStream#output_format_configuration}
        :param schema_configuration: schema_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#schema_configuration KinesisFirehoseDeliveryStream#schema_configuration}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(
            input_format_configuration=input_format_configuration,
            output_format_configuration=output_format_configuration,
            schema_configuration=schema_configuration,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putDataFormatConversionConfiguration", [value]))

    @jsii.member(jsii_name="putDynamicPartitioningConfiguration")
    def put_dynamic_partitioning_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(
            enabled=enabled, retry_duration=retry_duration
        )

        return typing.cast(None, jsii.invoke(self, "putDynamicPartitioningConfiguration", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putS3BackupConfiguration")
    def put_s3_backup_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BackupConfiguration", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetDataFormatConversionConfiguration")
    def reset_data_format_conversion_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFormatConversionConfiguration", []))

    @jsii.member(jsii_name="resetDynamicPartitioningConfiguration")
    def reset_dynamic_partitioning_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicPartitioningConfiguration", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetS3BackupConfiguration")
    def reset_s3_backup_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupConfiguration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatConversionConfiguration")
    def data_format_conversion_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference, jsii.get(self, "dataFormatConversionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPartitioningConfiguration")
    def dynamic_partitioning_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference, jsii.get(self, "dynamicPartitioningConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfiguration")
    def s3_backup_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference", jsii.get(self, "s3BackupConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatConversionConfigurationInput")
    def data_format_conversion_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration], jsii.get(self, "dataFormatConversionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPartitioningConfigurationInput")
    def dynamic_partitioning_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration], jsii.get(self, "dynamicPartitioningConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfigurationInput")
    def s3_backup_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"], jsii.get(self, "s3BackupConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__896428687302f3195799a180abc7d9ed2fd1cf1230d0f33b5c4588afc2817541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__192181385d781559e3064a4b243d6c1c176b4f22ce3a99896ca66e82b5894695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3580fc7281fac80842b1e556a8a1946f6f489f46331ae9d846fed5e9d2fd07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d529161ff95ce98cc8cd6865f3f5c731e86ecd65a1fa466460676f89991fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0bbe3f8c84e0adcd1a71661c100892915d29ba5d8fe590848b0b73eed911da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__175d9b78a41fd80acb52f2c7faa308ba9f348ef219d9fa4d859b32ffd778767d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8243dd6a97b1533a4f07b6f6219b907c378795634c07c15ece0ccce67651821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfde829d97aa28c829722bc36691aedc5fbd82457e7d4e815dadc9569258145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e341d5e81914cda36afe4ea18c67eec480dc11a2236b1d760a844e72ca8d0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24122826df8c0594ea6a154d8857ba5094718df0c195cc506791b819a5cc4efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd0457e17084e677c8bf5fb6654c2ed21e8068f709889a7a695d2700295c7b09)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0771ed52dd9572e6710f4dbaf5632bfab4c47ad0824bfbf46e1e219fd70f1bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b48c38f936094819940967f4af6344bf3c15425e0b84c276bfe338b48e68dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__49052177942bb73e716eb2f26b8f1a0eee94b00c6e112346824ad416ea67071c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3abef3633c5ec972cd20ea7a8f96d058448e716ef2e3708a873d388c6519b723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d551d14b392bce120ccd566885b46fb8babe3b8a610052a256904c314bb6a49a)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f96d5dc45d465606520728eaf2abb4a7a2e84a11245904d41b4479555ada2f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0a690af17a3fbe598805e979d166c79b948aafc4daa28828af79d9f65bb2b08)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e7b0d970730d3116597c003d389f716c6e85c43f74b91ae120d6f5d477c966f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d50151a35e2683415840a7dd8bf17604ebb418863ab08bc5f80b5cc36bc6216f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b454caaa6b5bc1dadeb112fe40035ab6d9252456b483fea752826e32ccf5e091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211af262acbcf0e4a114036d42af85f6ef5b1dc23408a31fbc8b51131b191ae6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78c9085c9ac32d6311accb256801b07b70e69a4549512de8ac7d3426c1fc7a73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c726370681a361c904a3ab45d85ca55cdda7c0d6bd0ca3137dd61a5e51bb57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d53f2a6af421375bf0d67abf1b8a2409566a6bf4934db6ef4ec73b6bd00c3b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc12b7d8c4b9d74cd0e0a40f1aefa6f7b25499481313229a1ff688f8e51f9fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aac13dce1835719cd2d2089733dc5f9c41b4426304f5bbe6f15f651e89db033)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__75cb82c9657df5bc47c6fd3214e1bc56782bacd443236373ad538ccbf4fd2352)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf43f8e772836d028610119b0572c5c79c02b25f75fbe0cb52c88c86ee46c22)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67fe600fc2514d6dffb82cfb3531a2f197270cbcfb48d20fd6949b9a2ef01211)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a73579366133c8a256245a3a0f0b1262aa0b37f10f077de3fd3e478235290802)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfbb39219d846ae6f660b374bdefc54c71aceef9d0845be6533722c8459902aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47948b53804f3c24afb84baa8892cccb9570cc0a8bf8435e00d7e465250ac377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__51380b813c8022efaa9ef4e39509b59128727e5ce3655828a5e818d0dc3cac59)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449693267986222e5ea2b4df32a13f184908be84f2970650de479fb4ec424e6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__567b5e4dd932ced9215da059e0c0d13505da51135dc50a4abac8ca76d1c97023)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceeaea6a0d4ab0cd6cfb053ba5f6dbbf2c0342d42a6a2f5789572c268985c9b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ae4487ad22fb4c897d0c4dcbef872d924edf4acadd01bc58eb2a91c3ed0ea8b)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959f218ad959a5ac08be3be3b93f796d27b0f7b3c204c4d9387c7787e4482bcf)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__004aae435582a833d36c84f41dcce1da8120cedf991ebc92b0946ae661cad63a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__8773d713a5532a396611c3d82dcdbae4b1445b818a9df236219d77b6a2b5aa53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb30593c2243537083dedb3637f6f4d720eb80ffcad51a98e06a251f47954aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39fd1c8ed27ea83b867e9ee40382ab03e6b163d10e3d40e76fecf72d546223de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73847219263c36129e4c132a1b9fe14e51b44414842087f5fb64fab72164d740)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c75c497245070483a0083d5e8b780e3bcc0bbe23ebdaaed8902e9b7c49f06c92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__33e56696e81ea0f2343b493b4daf13fe0551c94a36ad069fe0f0b25dc1e0e7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82eeef75ac8ee9f3f4fd1308bfc5382f87152ed76d7c5f89c83eef889c1e488e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712eb1e1286723e919776f106b9f20aa7c26001fef22e0400cc6c8818d9116a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b94bfaae7d8d976faca7768bf336edfed008746417fab829958d1952e2c7aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14d5c85062ddda295863e68f02daa62e85fa598062146c86fedf00a2105e8db9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1166bb7a9a192d250a62a5610ad3df3d68fcdb9c80c6abaf3c33c7de561e8fa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a26295a918a05fd75995a8f07468d77d19cf32ed078e598192ca86f019aec0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__630bb90eef04ac3c6529f322dbdaaf02b602663e4735c1433e45ddccc7411dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b70f99af6f86df76f139aba8cfba0a9273ef7089baaabc127318845abb26fffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "access_key": "accessKey",
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "name": "name",
        "processing_configuration": "processingConfiguration",
        "request_configuration": "requestConfiguration",
        "retry_duration": "retryDuration",
        "role_arn": "roleArn",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfiguration:
    def __init__(
        self,
        *,
        url: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        request_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        role_arn: typing.Optional[builtins.str] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#url KinesisFirehoseDeliveryStream#url}.
        :param access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#access_key KinesisFirehoseDeliveryStream#access_key}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param request_configuration: request_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#request_configuration KinesisFirehoseDeliveryStream#request_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(request_configuration, dict):
            request_configuration = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(**request_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab97d11afe8f8d15db68cc4b6b2faf37a63ca23f61829aa0d09099c1c66bddb2)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument request_configuration", value=request_configuration, expected_type=type_hints["request_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if name is not None:
            self._values["name"] = name
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if request_configuration is not None:
            self._values["request_configuration"] = request_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#url KinesisFirehoseDeliveryStream#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#access_key KinesisFirehoseDeliveryStream#access_key}.'''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def buffering_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.'''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.'''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"], result)

    @builtins.property
    def request_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"]:
        '''request_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#request_configuration KinesisFirehoseDeliveryStream#request_configuration}
        '''
        result = self._values.get("request_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__276a8ecc81e8a05da93c4198296bea13a5c4e781f17274d9234f834018e039ea)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af8b1b4da48a0214e2d7d379203b0fb60f275621cb04aeaa9d8cbc024b2c0793)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__1f0b9105eeca0fec1d12fddb903e8c4425870d66de0892dc8b84cde46037918e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3662003be96daf1ca1fd29b0791acad1fe4dffcda48cb8041f48eaa8dd053b49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e163379aa19717725001db217fd9f38218d20ec5d00ca3f3f8b58ff2c48860f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a08a7c90ab93ba2749dfa45f36b998e5e3486cc57abad221bc7a383f9f6894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4efb96be501548558036a70a585b352642f18fca50ddefc2beacdf431a3f661)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putRequestConfiguration")
    def put_request_configuration(
        self,
        *,
        common_attributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        content_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_attributes: common_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#common_attributes KinesisFirehoseDeliveryStream#common_attributes}
        :param content_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#content_encoding KinesisFirehoseDeliveryStream#content_encoding}.
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(
            common_attributes=common_attributes, content_encoding=content_encoding
        )

        return typing.cast(None, jsii.invoke(self, "putRequestConfiguration", [value]))

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetBufferingInterval")
    def reset_buffering_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingInterval", []))

    @jsii.member(jsii_name="resetBufferingSize")
    def reset_buffering_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRequestConfiguration")
    def reset_request_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="requestConfiguration")
    def request_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference", jsii.get(self, "requestConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingIntervalInput")
    def buffering_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingSizeInput")
    def buffering_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="requestConfigurationInput")
    def request_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"], jsii.get(self, "requestConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__297e2a6e62f99b8223c8e0b9bc6de624f37678d9f7b41f05bda1fa3f35d60a61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="bufferingInterval")
    def buffering_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingInterval"))

    @buffering_interval.setter
    def buffering_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b941876d9815af3eac08cdc90ccb00c6b22757b44e1cbd243409b5e27e221d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferingSize")
    def buffering_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingSize"))

    @buffering_size.setter
    def buffering_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfcdcbe4acdff883e59b5124b6b126be11d2497aa89b3d8c5a75124441c53af5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingSize", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33dbccd5c37d140578eec6e3d5607dad9b9ec57ab72d67ac0ed96717caaa684d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b26b7505126e9a9ad5b572db9586662cb00fadf6f60e0a360dc725f16c1d781e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fcf599645d4d9241cf09775ec64d2b28e64eb729cbbdf947243d5f2b8e6372b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba0e428b591aa60b6e53748b9bea48583dc22500f9fabaf043f171b7f0a30337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d629a052e1618c35be71ae5cffccbb61c06f93fdbd9f109ac3173c3bec294d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__549be67bd992e1a7b8a8dc0918343485d02f430f61502147ab760d6677392fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a2436a43702b988d0fe1962bacb2fa461c222052046faf8d3a9911abe6c7a7)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a9367a249778d2db4684c49762a35ed0a7848453df85cba59350fce1a038348)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85f0e67f0d76513b59a771da57ce06b023e0cffcafbe9e187e6dfa67940675f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f3acc0c33cf863e7e2034f12703dabe973bdc07ca1ccce2d41d66ce02e61774c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36975b3cb0d1f179fc49015de73a4acfaa6be4ae68ad233b210d78d796189f32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea1aca0b5c4e57f65b53a7a1c020911797909f7046c5f0efae91cb84d2e5c9f)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bea3e38229361bf8103b8d3a5f7f0a17a94e3c8fb55dbad6320d6187e8c74a43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e526698b308aa52437a2346a9b8421609141ddd97a76013595cfb90afcdbc2a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f900f08a89dffcb19094655d777c571328fe10631bb0a050667b828c92e10653)
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
            type_hints = typing.get_type_hints(_typecheckingstub__300c45d5d4d1938c27775063a823b2c4c0358e6fdb33f9bc7fcf5cc98c3a7414)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82204d3ea648bde84b1b1e79066d1cac90e6809983a3c86759d330d28cf9c280)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5149009d38881217132672170347029d0377751b0c648b9ba52c67d1d1addc28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fd9e5e2c6995946db393c867aa3a40536f6d642630d6afe2cac669d5dddcf8a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e969448550b14ef825122581706e2ef5a16e75c51af16a574fd362e609933529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36c5a071d44f67c44a8adaf00c216c5cc059d13306bbb892ba6a1fff62a2d0be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df87594efeb49206dce58f2d73789193f984efc0ade359027439e8c8bd2c110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b93c69d9c62bbb9cd1b07f2bc08f381716e3ede25cda75b916adbfa5414555)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e6a0a8faa3ed4a1f5d6d11c56db6d667d61a53231e9116d16e469bf7315c80c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8578a8c038af87e3e867c91daf5a2b138cfb44f78809d09f61e669f0929ac26)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c119ca67afd6bdabc65dd7693a35d4cdac310b44c545901e55ebf0b8bcaf3f5a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__26749795929b0c557c931c067e5e3570a238accab53243a38b7c43796b923f91)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3d475b3da6078f6ef4bd54517a0b59c0393e27b91e178c8f5a264df70807097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9992b5996a49f984f006441fc499fb37451bc2cc4ffc2638c375e75bf0699fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4647a85b6daad7d7da34a09dcd18b766dccfdf650948f6a482ac927cbf5eb4be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed2d949f842f2f5478e5ddb98baa9d1247fd650ffc02590bb9c63bd5c4a46455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e669cf7f173ba9d40b7f685abc0a4dbc22458ee637847ced7a936c8466d6851)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac32339aa44d3e5709db6bbcd3e3fdda662b9a44dae565d1d4a3fea2c5f95cd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "common_attributes": "commonAttributes",
        "content_encoding": "contentEncoding",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration:
    def __init__(
        self,
        *,
        common_attributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        content_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_attributes: common_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#common_attributes KinesisFirehoseDeliveryStream#common_attributes}
        :param content_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#content_encoding KinesisFirehoseDeliveryStream#content_encoding}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__873b74f491dc758661e8e613eea988106800d4861fe1027755f54f0cab8890a6)
            check_type(argname="argument common_attributes", value=common_attributes, expected_type=type_hints["common_attributes"])
            check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if common_attributes is not None:
            self._values["common_attributes"] = common_attributes
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding

    @builtins.property
    def common_attributes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes"]]]:
        '''common_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#common_attributes KinesisFirehoseDeliveryStream#common_attributes}
        '''
        result = self._values.get("common_attributes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes"]]], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#content_encoding KinesisFirehoseDeliveryStream#content_encoding}.'''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#value KinesisFirehoseDeliveryStream#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf79d1f59ca230a4299a2e0839704cc6116603727bc56020f2975af3bbe9640a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#value KinesisFirehoseDeliveryStream#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__588a0d1dcd78ed2a676536810efdef90c7d964513eede37659f4f97c45ae7612)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05def5ece8a709cb9a4f7e4e75704b6de98dde207da95890693816e02ec52da5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc9245a84ff86e2c5e0e6dc9d199d15e9a0577adb5d6aa729d7a88be24ee2a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__01b0518091a5f9f452dceb97701d412ed2a5550246122e035d206f9c1d345b20)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c5a722940fffde0b3154a0d8252855af9f0f139785d8930f59fd0212dbd2ce34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6bb9607c72d2514540bbe8d82ae974fa4062f37a2df41fc67c04766235a5668)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ce2e582df122ded5313b8d1a7bb4120107e82eb99a7fe0b9dcf1f6ecd6b1ced)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8b42655fad9216617f2ad0b16ecfd44c56aa78c935935bb1d2d507cb9e20af5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322c3bdbc7c4360fa83231110e6272f174977bd3395256af20dc031a1b0132bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d8fb27fcd201e4d9077490bc97cc432bffae160f061191a7dfd7f3f836637e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae8050069695a1f4e54d2d45dd5824ad39691847969fea9037bb325a67b1fcf4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCommonAttributes")
    def put_common_attributes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e37481e1a965d3a59aa83ee6193d857bb698fe0fd79757f8fcb1e7617e1061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCommonAttributes", [value]))

    @jsii.member(jsii_name="resetCommonAttributes")
    def reset_common_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonAttributes", []))

    @jsii.member(jsii_name="resetContentEncoding")
    def reset_content_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="commonAttributes")
    def common_attributes(
        self,
    ) -> KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList:
        return typing.cast(KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList, jsii.get(self, "commonAttributes"))

    @builtins.property
    @jsii.member(jsii_name="commonAttributesInput")
    def common_attributes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]], jsii.get(self, "commonAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="contentEncodingInput")
    def content_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="contentEncoding")
    def content_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentEncoding"))

    @content_encoding.setter
    def content_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638a9bb75a96c7cefd49dd77bb20c873a9a57ffa84f569c1a27eb63c7ff07389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28cea82141726abf06aa9d02b71304fbc225ff50a2f54b92054cb889a2a9ed8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamKinesisSourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kinesis_stream_arn": "kinesisStreamArn", "role_arn": "roleArn"},
)
class KinesisFirehoseDeliveryStreamKinesisSourceConfiguration:
    def __init__(
        self,
        *,
        kinesis_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param kinesis_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_stream_arn KinesisFirehoseDeliveryStream#kinesis_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00ab24caa823f43f686d6eedce372f264ce7c9d4eb5d38efccea075616466bb6)
            check_type(argname="argument kinesis_stream_arn", value=kinesis_stream_arn, expected_type=type_hints["kinesis_stream_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kinesis_stream_arn": kinesis_stream_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def kinesis_stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_stream_arn KinesisFirehoseDeliveryStream#kinesis_stream_arn}.'''
        result = self._values.get("kinesis_stream_arn")
        assert result is not None, "Required property 'kinesis_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamKinesisSourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__805d5c91f60af5d72d5306b61279c2447b9a067f8fd0ac37b4b3e9fd5fa04b65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamArnInput")
    def kinesis_stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kinesisStreamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kinesisStreamArn"))

    @kinesis_stream_arn.setter
    def kinesis_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bfb8b4844c773f1eb517d96d00370516281f710832d0cb7d2797284f9cd79be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisStreamArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af43f2f57e73cec1a068ace4f52377f39495406ba033ecb2799cdbd6d9a2410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e211dc508c66a7734bc12ee4c92bcb00c3bf35fbf3c445fe029641eeeef6434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_jdbcurl": "clusterJdbcurl",
        "data_table_name": "dataTableName",
        "password": "password",
        "role_arn": "roleArn",
        "username": "username",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "copy_options": "copyOptions",
        "data_table_columns": "dataTableColumns",
        "processing_configuration": "processingConfiguration",
        "retry_duration": "retryDuration",
        "s3_backup_configuration": "s3BackupConfiguration",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfiguration:
    def __init__(
        self,
        *,
        cluster_jdbcurl: builtins.str,
        data_table_name: builtins.str,
        password: builtins.str,
        role_arn: builtins.str,
        username: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        copy_options: typing.Optional[builtins.str] = None,
        data_table_columns: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_jdbcurl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_jdbcurl KinesisFirehoseDeliveryStream#cluster_jdbcurl}.
        :param data_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_name KinesisFirehoseDeliveryStream#data_table_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#password KinesisFirehoseDeliveryStream#password}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#username KinesisFirehoseDeliveryStream#username}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param copy_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#copy_options KinesisFirehoseDeliveryStream#copy_options}.
        :param data_table_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_columns KinesisFirehoseDeliveryStream#data_table_columns}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(s3_backup_configuration, dict):
            s3_backup_configuration = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(**s3_backup_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40eea6b09416a89c26f2ceedb1c9b938944c17b1c2baa52fe8a829bdaa459c3d)
            check_type(argname="argument cluster_jdbcurl", value=cluster_jdbcurl, expected_type=type_hints["cluster_jdbcurl"])
            check_type(argname="argument data_table_name", value=data_table_name, expected_type=type_hints["data_table_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument copy_options", value=copy_options, expected_type=type_hints["copy_options"])
            check_type(argname="argument data_table_columns", value=data_table_columns, expected_type=type_hints["data_table_columns"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_jdbcurl": cluster_jdbcurl,
            "data_table_name": data_table_name,
            "password": password,
            "role_arn": role_arn,
            "username": username,
        }
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if copy_options is not None:
            self._values["copy_options"] = copy_options
        if data_table_columns is not None:
            self._values["data_table_columns"] = data_table_columns
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if s3_backup_configuration is not None:
            self._values["s3_backup_configuration"] = s3_backup_configuration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def cluster_jdbcurl(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_jdbcurl KinesisFirehoseDeliveryStream#cluster_jdbcurl}.'''
        result = self._values.get("cluster_jdbcurl")
        assert result is not None, "Required property 'cluster_jdbcurl' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_name KinesisFirehoseDeliveryStream#data_table_name}.'''
        result = self._values.get("data_table_name")
        assert result is not None, "Required property 'data_table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#password KinesisFirehoseDeliveryStream#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#username KinesisFirehoseDeliveryStream#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def copy_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#copy_options KinesisFirehoseDeliveryStream#copy_options}.'''
        result = self._values.get("copy_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_table_columns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_columns KinesisFirehoseDeliveryStream#data_table_columns}.'''
        result = self._values.get("data_table_columns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3_backup_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"]:
        '''s3_backup_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        '''
        result = self._values.get("s3_backup_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4e9f96788ea4b45cd57e876b50a60d9b0e982b5f84718f2b2c5e1ea4dc176f)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee7c169d3b98e611435fde4bb5a4e51d341728b3daa594755d8fe315a462d481)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__cd5946e5700d8b9636f6524f48ffecb245c2c3f5764ea4abe64a16a5dd7f934a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e15fa2b1c2dd6479629a949c8105474a163e1296fbffe3f17379eb83764f0e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__effd60c4bc3409ad2fb27d2244306f6982fd71e711a656ddccd063278f8d078a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9a5d93f47ccaabbf4803740f587f3a6c990e0599635ccf972b8d1ce1cb1a1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__006d12f51d344a2ce65afe432f277c7e00936dfa9acc98181c435167866c7a72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putS3BackupConfiguration")
    def put_s3_backup_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BackupConfiguration", [value]))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCopyOptions")
    def reset_copy_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyOptions", []))

    @jsii.member(jsii_name="resetDataTableColumns")
    def reset_data_table_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataTableColumns", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetS3BackupConfiguration")
    def reset_s3_backup_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupConfiguration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfiguration")
    def s3_backup_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference", jsii.get(self, "s3BackupConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterJdbcurlInput")
    def cluster_jdbcurl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterJdbcurlInput"))

    @builtins.property
    @jsii.member(jsii_name="copyOptionsInput")
    def copy_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "copyOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTableColumnsInput")
    def data_table_columns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTableColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTableNameInput")
    def data_table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfigurationInput")
    def s3_backup_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"], jsii.get(self, "s3BackupConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterJdbcurl")
    def cluster_jdbcurl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterJdbcurl"))

    @cluster_jdbcurl.setter
    def cluster_jdbcurl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab16c44044cb9f57efe839a70339c7ba7b2eb68d3f14f60321faf93a307bc1de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterJdbcurl", value)

    @builtins.property
    @jsii.member(jsii_name="copyOptions")
    def copy_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "copyOptions"))

    @copy_options.setter
    def copy_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44c950d48f902bab62914fac66a46808ec6accd574bc473fad2053421c9a869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyOptions", value)

    @builtins.property
    @jsii.member(jsii_name="dataTableColumns")
    def data_table_columns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataTableColumns"))

    @data_table_columns.setter
    def data_table_columns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551b1625636403cef154c6db1f61c61d8aaa67150253effb03e3d884bad4b298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTableColumns", value)

    @builtins.property
    @jsii.member(jsii_name="dataTableName")
    def data_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataTableName"))

    @data_table_name.setter
    def data_table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34de3b4fb4c91b4b86d9b58f94214ac38180ec8fe3167020c6ccba8e3e4301b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTableName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__310d90a3a7aca345fb3a8980b6cdc6081963ea82b3363b4a508e87ce6a59b738)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb162187b604fcc07fba57165bcca3e100b661ccdd1db466b66e8833413ba073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b46c43e0e47dbd2a5d765b4093964dea661b24f998f645cb97f6220a72c73e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c080d5117c3add52390aaf761f42dce5fc4c7fecfa7749a1f0b3b2e9e959a3be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e43abb13f6bb454ce3fd119f4be0ce7faf40b289d25621aa2aec037a9daa72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2d74c4443eb32a4fd761c63d5b564027425139497e53907631e44031b4ce3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce391a624927f6104c57b129e0ed7ee41ee6327686ef4cbfcd856cfe4c45c2af)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4355d7c09120ece7155a43e87fbf877b75897cc3eed84aa904a34f993a29a2f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99c49b56ea80fe71a82ecc58035f00c075293f6b8224fff0b72d6364aa82aa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7feed419c6c6b99d1f5b8a02609cff707ae6e402fdd95a56a1cfc599f9b0fb2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__394f8f4be7a564752579a0f5ceb49c84b9d97cca9cc65b9459aa8cb8cddc989f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ec0d9ffb26b3ec266f44bdf0ea66b3273013e6bb8ee6041ede5fa7ee1b175f)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4fdde7d80ac6b7c80a9c75f36687d7fa60db5fc9b45c9b346a15532c92fcc86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92db7168c871ec692b311baff9bc1cd40f7df2158590a38fce71cdb085b4736b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f521cc40fae9a21d341e19d56928a64511e1cea1ae954e7058e71ddb0130e437)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c203f442f18f8ebb35dff68b0deffed587803654ca9ed9243e97f702e4b7d9d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f65eb9805153d8ab9b6f762f9ab2fdb76393081cba0c94c284bb5fdaad83fd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aeb8bc4097b8c7a63412b0ad9eb90f4c3668698a7859fab8921739c77c2cb87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__473bcd22fd403947e262eab8b0cb9556ef5bff6cf3c100e335481c63c6869f8a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa1726d1f14be4f25335d59c708f3c158997870ce758870c1f0808d0414f454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529c3d1ab6a770ed023eb854759d2b2f10c1e6800549e1fbe39921c9da0abbb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43250bc27f0e424f3febd5f812f299e7012236246da65866f1c95f6e11d511c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d17bb5ac5e75ed8278aec1b199dd522910b3fb1e80f2679b560d7951cfccade0)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cffc64f2f4529c1a57d7b6c6c4f73dbba704a64b0c373ee26fb5d141db7beb0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8687149352323c2d3d509e65ffbc480f4aff04363870b3c8ddc2285656867ac5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e569adabf9bbebf4f540bcb11e8755e129ac7a6a441aba96b0cf72548f500580)
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
            type_hints = typing.get_type_hints(_typecheckingstub__44f2389cd5a43ec01b87370b3874fd2fcc3ea00171294d1ff6e61be4d1f40640)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e844bd5fe4729c63e2a336b393559005ed83e825d5a97faf9dc69efd87daa54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a3723c69315b457600c2169b985dc616302f6e6fea3f4f01b3ea27fc3cf07e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec30e2ecb638a79db5bc22ad82adf264127bf7c5fee35664b3537888831dbefd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a2cefb06d3a83da4a3694edd65f4b2a86fed8eaa5e5d1426da16e09f17903d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d316e5f73537402e7c2489b82fcda8c768a406d9f6ab6df16066db886b84f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbda201b42a94b76925e95839bdb89623f73fdd493ea4372b2cb91531643b27d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea9c0e1408ba60f7446b36f188761b0bc1fe92b1d47a31fe574436b529e82037)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a43efc9f813a6aee004178da83ca334c5e0dfdbe96b62b537caf948da473edfe)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70246aa003f8e0d89671f4dc7cc80602d974244a5bcfdcec969ca2ce05b8cc28)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__559460daa2d988623159e37ac55afee7f56647ce142cee179570de6f669bc9d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6b391408ac3e4366eb89647116f00f07d83c246cbd945913c7054aa4a43fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1036ffaf34270cd208dbad782b82ed151ba41d9dc681135d93289e8eab19b1e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aad541551bccb8119b42fb2d5fac510d61b71286b3e802cd2a9950146948749)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__646cc416de69438990beabe925a15a63a4ee983e539b704eb4636a11420214c1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e92a79bcedc27045d1fcdad37a43136d28d79ffd8169d827fcf3adc4aa9e9d48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96e3f464243ac893cd5d7e917426c26e973dc02ed4d7687b7a8a9099a8461a95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d296efb79edfc7c225c6493e110381690e75b8cdec719e02423a9e064026c24d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8f8c34baacc1d84b1863063b0b7db2580c79748d1404b8f86f52a545c1f83a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1de0d3a25f3d6e777e4729f4099eb3b12cbc77d1d81083e62cf61e22305b78a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__382465c5baa491754a7d0f204437341acbe0f65f47d0934d1ed669594b309b1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab3e2ef6e0984e2449f79c496c301220d975cffdca428a04d9c11fe0ab2b2273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5e9f839b56b127a2bedebc97e9e8c17a5a4e4b2fe20a22fb72efca5cd91e74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b108e5ff75439dd42c4be7de8569ee7a7c24412a47f0c8b404d607883c557072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
    },
)
class KinesisFirehoseDeliveryStreamS3Configuration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__176d6d5ec99795618674f1503526e5bd5167e5f19989f17b426b787ada06d1fc)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd439410fbf4cd848d5177def05c4abcb9eaad479b20b034e3ec95b350877e30)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0602f8b9ea4db951e80c625b161f27e4bc1c96dc4bd2b52fdc38dd10bd9dec6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__54a487b73a1462972d87e65ff41c2b3d4e544313fbbc9e858d19d311a3ee4313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c975bc11c1d141b8272ef9a7f64c017cdec47576503901af0805c1e8562dd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbf982981c546a7424e035fddf4734f687a0ab6174746e42a7af6f20e14be344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bad78e6c5e50dcbdaadba6adebc88ea6f800a89c25a0bbe7d9de05c238f74c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d6d7aa571d67e708318d32f82346d41a24eebdc2dcacf56c94fc2dee4af3530)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__4fc471329e578811729ba3a215bc03a1c4701d015bfef752605666419e0f5465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9222e32047480861b1a4583929e29dfac78f62faf7b4897e8511437bdd383ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606ddb342b569e0ae59724e68a74f82d931ede9988bbf6f199b973d2455ee7e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__423ad31dcb1f4af90f36070ee3aa059005329cde79775554e2de46eaddac8804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04387fc689451142049400cb0467c4896e34bf4f0e7e8a7ebade87bbc5bf82cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c0a87369b0ac0aa60d9619ef5a68384f6be77b6b8db2f789339b4f06fb3099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab9034d35f7b000f07825ff6d491aa666003a5cc4d4ebbeba193a3d42f755fe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3447aadd8805388cbc40d8c5c7d48b6bb1993a28263da499fc79b9682867926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e2f8058eb04c71eb3402e2565f08ee2e34a6ef9d5e0315516090a03b16b4a90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamServerSideEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "key_arn": "keyArn", "key_type": "keyType"},
)
class KinesisFirehoseDeliveryStreamServerSideEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        key_arn: typing.Optional[builtins.str] = None,
        key_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_arn KinesisFirehoseDeliveryStream#key_arn}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_type KinesisFirehoseDeliveryStream#key_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c92d3ebc16b9a4f056f1eae995fd7460e94528e8cd57f511261e1513a1acfc42)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if key_arn is not None:
            self._values["key_arn"] = key_arn
        if key_type is not None:
            self._values["key_type"] = key_type

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_arn KinesisFirehoseDeliveryStream#key_arn}.'''
        result = self._values.get("key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_type KinesisFirehoseDeliveryStream#key_type}.'''
        result = self._values.get("key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamServerSideEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad9ceb3a8a3112467c474acc0c638305d8cb7a5748e8bdd36fc3600698e3fc27)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetKeyArn")
    def reset_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyArn", []))

    @jsii.member(jsii_name="resetKeyType")
    def reset_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyType", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keyArnInput")
    def key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d37b607372a2748521150abae05c1f025f17d4266a7936dd2b8cd11d8b9b1222)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyArn"))

    @key_arn.setter
    def key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3c363f9b85df68670dee0e653aa8fc17e6c16f4c8693529d3dc4c008cc0619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyArn", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4144668ea00436913ef97569008ba5fff5ad34a635e35e415e8cbf804a493ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74f2ac555f6dbc7fdd006aa939fcae2ee8db6772e9103cf61af0ee7bdb90c59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "hec_endpoint": "hecEndpoint",
        "hec_token": "hecToken",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "hec_acknowledgment_timeout": "hecAcknowledgmentTimeout",
        "hec_endpoint_type": "hecEndpointType",
        "processing_configuration": "processingConfiguration",
        "retry_duration": "retryDuration",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamSplunkConfiguration:
    def __init__(
        self,
        *,
        hec_endpoint: builtins.str,
        hec_token: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        hec_acknowledgment_timeout: typing.Optional[jsii.Number] = None,
        hec_endpoint_type: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hec_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint KinesisFirehoseDeliveryStream#hec_endpoint}.
        :param hec_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_token KinesisFirehoseDeliveryStream#hec_token}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param hec_acknowledgment_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_acknowledgment_timeout KinesisFirehoseDeliveryStream#hec_acknowledgment_timeout}.
        :param hec_endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint_type KinesisFirehoseDeliveryStream#hec_endpoint_type}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(**processing_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a69c6ee4d9a54ecdff2fef6d4104ac29c47d7e6bebcd61f188fb0da3a2f827)
            check_type(argname="argument hec_endpoint", value=hec_endpoint, expected_type=type_hints["hec_endpoint"])
            check_type(argname="argument hec_token", value=hec_token, expected_type=type_hints["hec_token"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument hec_acknowledgment_timeout", value=hec_acknowledgment_timeout, expected_type=type_hints["hec_acknowledgment_timeout"])
            check_type(argname="argument hec_endpoint_type", value=hec_endpoint_type, expected_type=type_hints["hec_endpoint_type"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hec_endpoint": hec_endpoint,
            "hec_token": hec_token,
        }
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if hec_acknowledgment_timeout is not None:
            self._values["hec_acknowledgment_timeout"] = hec_acknowledgment_timeout
        if hec_endpoint_type is not None:
            self._values["hec_endpoint_type"] = hec_endpoint_type
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def hec_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint KinesisFirehoseDeliveryStream#hec_endpoint}.'''
        result = self._values.get("hec_endpoint")
        assert result is not None, "Required property 'hec_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hec_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_token KinesisFirehoseDeliveryStream#hec_token}.'''
        result = self._values.get("hec_token")
        assert result is not None, "Required property 'hec_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def hec_acknowledgment_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_acknowledgment_timeout KinesisFirehoseDeliveryStream#hec_acknowledgment_timeout}.'''
        result = self._values.get("hec_acknowledgment_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hec_endpoint_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint_type KinesisFirehoseDeliveryStream#hec_endpoint_type}.'''
        result = self._values.get("hec_endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63212ccc96f5f69cd2f6ce255161ac43ec19d4a1b0e6f756b698ad93a3d202a)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4345fb3a103399328ad8aa00462b2904d122c0ac804a54eab638cf54e01a145)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d8add111b2dd0bee07297443dbd2b8827d9847d5231e6005d3f0205dbb48c56c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51f9784a0af873a2d7c036d737b67eff8f070c75897032d46eb0e66f746a6c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da72bc535c57c4688639f715432bbad067c263df0b18312e3fbb0782de82c2f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f248142371578b85d6bc9e345a2eaf326f98c6fa3111a079098a0230a0d94ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd40963c7a7e45e1b91876bfdee9c001e74f58b277ed443f645f8513d4d82241)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetHecAcknowledgmentTimeout")
    def reset_hec_acknowledgment_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHecAcknowledgmentTimeout", []))

    @jsii.member(jsii_name="resetHecEndpointType")
    def reset_hec_endpoint_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHecEndpointType", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="hecAcknowledgmentTimeoutInput")
    def hec_acknowledgment_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hecAcknowledgmentTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="hecEndpointInput")
    def hec_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hecEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="hecEndpointTypeInput")
    def hec_endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hecEndpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="hecTokenInput")
    def hec_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hecTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="hecAcknowledgmentTimeout")
    def hec_acknowledgment_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hecAcknowledgmentTimeout"))

    @hec_acknowledgment_timeout.setter
    def hec_acknowledgment_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2949f24a9ddf216d34f3d63e0d2210a37fd40a2945499d52763570b8d5b58626)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecAcknowledgmentTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="hecEndpoint")
    def hec_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hecEndpoint"))

    @hec_endpoint.setter
    def hec_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b77f60c85dea3eda738e6c8e4df10f6eafbd535bc1c865c632ac3170122f1cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="hecEndpointType")
    def hec_endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hecEndpointType"))

    @hec_endpoint_type.setter
    def hec_endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91bc8677716ccd14eaabefb4c9c6deabbbc6615e95c30d139cdb5ebaf9006d3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecEndpointType", value)

    @builtins.property
    @jsii.member(jsii_name="hecToken")
    def hec_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hecToken"))

    @hec_token.setter
    def hec_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e15be6763927fd3cfb65b79207e3bf12a90c1c9719d7398feba89e54a525804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecToken", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4925175c963be8d2b575aa13d0a42c0193fef5e64f7e373fe645032ab8a6973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81c0e2dc84395962add20047690e512e443c642b0afd1b73b0785aa2d5dc8ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75100b836a10239a3c88c1c00be97ea8a963171385c2da1d8707aa2f7a300537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dff2e1a32bc4becbcf409900ee331f9df198b0969f5c74d0d9c83b93332b0fbe)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__25b740c95690c5fd343a4dcb0f8dcf200ecf0389bc31ff268a7c599bd44192dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f403e784670c8fb8f174eebfc2acaf5bd57fc590e9452015a96243ee45ba2c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b4f276763e8523357a028c94ab1e66104ec1d6c6a7c099d28e730c482c840b97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d34644921efabdc8a64649bed19163d23decacf5c8e2bbe714163f2b12153e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__920a4265d0ce3be5dfc33c659355d4e5b791aa9c64279e9fac120f17ec5159e2)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdc0dceecbc88b036be34caef76dec39ba440d3cd2f771c2bf58d3e4eabcb593)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5577562320593889599d66d05257d9113856f032fab76283491eee57b504687)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c002e68aea84aba0009f09228206913e1a83c83c7467f3f20b10e63f08a58a72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0c6fb23cbe890beab08e062217909fd50c551d8aa9c1b2a49543f47d22f7e88)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd70333bcdf4bf02ade121296ff5584d0c8baa7d084e8f3dace41b1f6749c647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b530c4ce26c477a48057964b36d6649c4cf5d45049e9b83dba542ab0f9c3735)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd16556352116b65ed309b196e57b4e8a8afa890a4810b681c5366eac8905080)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__589034df89ea26afcc11cb9ff36181a65e15c461a849b2a0830c061b5ca304ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1792738440b08678e1c31e04803b3f0ef75fa9119797f5a140c584693e55376e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923cc0bd0da6d0453fc6279a38dbfd87cb8908bdc941605c4b913fffa059bac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f95e92c88974d1d6be7a5fa25d5d53f26db2fc7607ca28ca6ad0c5b42912a9)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86a1d818e62e2df4d5a723a9946c00f5c13013c8a5994a2bd50b74bc43b8f5be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea02ba6b4ea98d14da957e23a3149fe933df0c422182193fcba05d43ab6e86d7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa15eaff19bf3b83ef41230d187364a1e6ef052a3c4a442c5f8fa19d7db168ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3390784aa8b72adc3c01c4887fece7efafb90baffbb16083add6825375c5251)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e83bb3368b06db31a0d8a0c9e6ec4d730ff1d604268065e23f437888c6882a63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed450f70c6aebe079baf0a77e9c0c56cce8be8f7157b6ca04fabcc5bacfb5e7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab846656846d886e29e0139926d9f751fc0e2e43d7891c141b361bfa8d4f9358)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1a4d2289384cadb204a4599bf39283df5ffce3169b1013b176e7c562071672)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9f1225ead1f29ef5c31beb3b5c244106bf64ae8dcd6028e9e7d7ac89b2f33eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f655d2fd9068abcbed2a791a4b3e4878199afcc912085c017484d9bd48a3357e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KinesisFirehoseDeliveryStream",
    "KinesisFirehoseDeliveryStreamConfig",
    "KinesisFirehoseDeliveryStreamElasticsearchConfiguration",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3Configuration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfiguration",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamKinesisSourceConfiguration",
    "KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfiguration",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamS3Configuration",
    "KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamServerSideEncryption",
    "KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfiguration",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference",
]

publication.publish()

def _typecheckingstub__ffdcf760735fbc16c405ea45dbf955fb65ff581a35f23e6b0a8e2477a8b3e315(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    destination: builtins.str,
    name: builtins.str,
    arn: typing.Optional[builtins.str] = None,
    destination_id: typing.Optional[builtins.str] = None,
    elasticsearch_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    extended_s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    http_endpoint_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    kinesis_source_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    server_side_encryption: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamServerSideEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    splunk_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    version_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__77d717aa472bb0bb697868caf7939bfd9ca574ccdc157f2478624741e3e78a4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f897384a56d7ea48978028f45846c95c8189620fc6e97371b847a330da06aaf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e52a7c098dd6a8b5fd52df2799c43706d52938649f299d5fe9016dc1e74f67a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccdc63a0a7e294e7d2abe9c04b6bb75271725f397ffe122324f4a9e811f6caec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a814f9eb73145eee49a6fa244bbb06a4f7764aaf76c513e5b530764b7d920d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da0de7ed3801416d7c8322565af1305e49cc2b3e23c8a534b12c8656f6863cd5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63c2f356f452b0eedc3be2e274bf71f929285a2b03685b370991d386d4d6763(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd9815a47ac27ac5da5d08d6f66275808774c2614402e987d8cee2e2db8b3976(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a736472808234f4035e4a387d31ec5e97cdbcfc656c63f8110cf238cd6a606fd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    destination: builtins.str,
    name: builtins.str,
    arn: typing.Optional[builtins.str] = None,
    destination_id: typing.Optional[builtins.str] = None,
    elasticsearch_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    extended_s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    http_endpoint_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    kinesis_source_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamS3Configuration, typing.Dict[builtins.str, typing.Any]]] = None,
    server_side_encryption: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamServerSideEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    splunk_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3866b378b6c277628dba5accc5fa2b99cef532a15a985cd61580ea359299ce4(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    buffering_interval: typing.Optional[jsii.Number] = None,
    buffering_size: typing.Optional[jsii.Number] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    index_rotation_period: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_duration: typing.Optional[jsii.Number] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb959c80f91aba184d30429e40a63178ee3d103224ed6ed83bc3a32f4a8ccf98(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629392c0654a624dbeae5445bb17fe82100c9ea300ecaad14b85d848261263c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807c5e386f6c0b18e03b02cecf092ebdf2f4581f8c460246127a251ff34cdc15(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b860cb123ddf3ca2c30ef4f715ce5fe7cc1896ec961558e65be7e5d0e6d221a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c1317e693ea0ffcce77c8ff08e374a3ea31ec9238a76a5c3bb07934eac7a9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c75c72a973b4aca71d48ce5131132149e594f1a8ac6a0c404542d4b77b6b26(
    value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f70c891b5414a6758727dbeb952c887a877d60c5916d17a179054002219dead(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b544134facdfa9f389b3f9b0a662587188b68cb6389aaed59da1dba9a719821(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec6a4c2dc077ecfa9523b98645c5979674c3fd8036304d19abd112b154e02bf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd086d5a9c686077cdbcce2ca035a61e2ad217956c7da3c3a1ff5f1df85979b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee77a46698e9336d86abcf4371da47dd865ba5436237f157ff7833176dc6dde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70661cbcd138c9ceb3862a2ca4241ecb49a26c82627e17f9ab6632244e366d96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae1bc3cf812a73d809239dd275d35d263ca5a68d28790768410ecff8dc44b12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb5aec3116696eb280d4e907c78bf0579e840563c9032a89043fe92d0057365(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ee4264a27e253952a5e3f73c8b20a3f193245bcbe4b3beddd754aad8a9a6ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6851f333bb1a5d339ce0acd34602eb4a45823350f6abe1b8685bee407444365f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e391bc6098d5ab12f81cfb2cc872c74ddb95a5098f547326cdb66d80e33c635(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d7b8ab5d4348ce246c4e2d1359e0d81c7df0d7ed350fd43474c87516102b63(
    value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed5c7b6de9610f839d0e67e0db1ab7a0a2e0d8cc3bdb40b21d19135a2d8af22(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efd0834e37b7fec9d01915bb53980884c0ba57d56fc023b53e78ea2bfee74f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd59e0ed80fb7c9653fc9a92ea22007ef528617aa078928e9f7889c23acc843(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66652a3e164577763cb59585aa6aa3ce15acad14351be6b9e388f6e93356e46d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8007f3e90e42e14f046a890c3f3e0a8bec359300b9bc17c461e778aa02478f1(
    value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f078dd5c36fb5012c877043086669c1bd275c82e9742c579841db96bbe8d3adc(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc18ad20b86cb4d59faa2d2ee08d1cf83c9a2627c84172119cd64fa5a28e77c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5e382f8c5186853c01f934866079e08b21e3e6aadef02d5b3b8edd488d58c89(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0250f865b040c83ccf187a7b5a515937f03a6d6e4a468b9827d6636bfcae751(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a3f205bf9e1e13cc45b85e9f1d2076060ab2828d75e86b64343656f030dc5a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1016ff1ab0dd88a7b53a5b1e59100126a520f171f518e82650d984c4dca27685(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172a8c68559d3a68769af101a5b3763d24b8ca10f342af2870b8709ae1ed395d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f4f97ea0c5c9478b030c5ad1fb09a4344ebfbaa8897afa3926620472576394(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46aa47203522d0f1421fb81265ede36e1f5e52dcc45f9001ed4523ba036646a7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ad40870d157b5aa25ac715fd9ef8c2acafd8e995be4513b0f746b584532e5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31aee646a01d829978d0599eb871416baa8048354f7ae408edec2ffe01f00fee(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e49131a9cb6e94fbf2222f11d0554e61819f2bf9a9c8d6149162e9ede2ef5434(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8941d40f0470dea2b39f00672cb5a32e0db232855700340bd36167de46da33ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44b57b8e03755bdc58cc709ac7ab3b2b45c5ebab7eccd4eebd8d80d70a35984(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8b57727f64c6ee189fa0b5f9bf037bcd28ff4a7c5fb697c150b16087dab8d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec75ae2db6be93504c1b88b29ccbca04f434ec66179223cbb9adabc6e346e56(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dbc29506b0a88cc039007104f566d01c72e112307724e461f96b8bf83e157ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e18777486deb3c9618635ba6d7a3c4d2e4d370b6ac69d1abdf3c686cc7bb3c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5c6480ff526358c67faff32ac0b00ab20d327d48b43b0cd4b07e812ddfef58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93dcd8783e3dac05a76170f880e99545f7b8b8d7dd6be5670bcb1ea785bd413c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31830755bcd37f9c77de4db011cc1e5220942835ee094664bcf6952c4abc266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a1e6bb79bb584e3506f9c43f25975fa157d7599fd803a7a57750e2a3ef2923(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5386ff726cfa4cdc91d5027e76e96c1afd27b6d4d4dc1dd0df9f33535212d14e(
    *,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22213e42917531a1cdae6ec5fe3a5b6d8c330c56d84a37d9146076631d24b2d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d059c162f828932b54fb5329552790bdc2b5b49ac28d87ee3d047db0384c99f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41cb6ebaf054e037c6330c9a347308066355f706cf4d8b8ea6da6afc8970fa3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc98331fe1430e0eb44175ad26a1e51b868d09268fdb70a54247ef31e6939b4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d37bba539cdec8d294e9b447cb26cc2a5554481f338f62e02ec858bd2da96e(
    value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec2f226a4d4ed0cfc5737aa2a016c0c5a79be8a8e781e4698fb0da22976e817e(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffer_interval: typing.Optional[jsii.Number] = None,
    buffer_size: typing.Optional[jsii.Number] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    data_format_conversion_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    dynamic_partitioning_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_backup_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c9f5001b839cd714e1a69fde9d901e37703917fbe3dbd91ea56a07a2465916(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e47753cb92680f79f6535c3e0839e3c415d4c46cd421353cbdf5bb1cd581ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec9595ddcf30755005f844cd85565770efb67ca9a40b030573f62f29a1850f73(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c9e2e1ef05fc1c08ea3a75257bf66b7b64fe88784f703f11e5b7578774c08e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f90b6985cca27614d4d6b01fd688bd50d5d505a6efa2204f9caa4fa9bfca1331(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3352969c3cd0d9f470dda1ccb87be540f1042ba43a9bf6df6788b28d53c9f921(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca95e9a905a5b63cdf325df6dab92904400afea83ee79fc92cb190f168c44fff(
    *,
    input_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration, typing.Dict[builtins.str, typing.Any]],
    output_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration, typing.Dict[builtins.str, typing.Any]],
    schema_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a660e6465758728c098958c772cf523a222b6523eeb6d7937a178eac3d844ff(
    *,
    deserializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__930cfdb3a41aab46fcbdf9a0f58bfce6823164da0012e696d9c2afb1f322d416(
    *,
    hive_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe, typing.Dict[builtins.str, typing.Any]]] = None,
    open_x_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50387e96602d954019d17e39667153420a8ed8c7665670b0e0432c7776320143(
    *,
    timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__409d21892f711f8af586aba4366f9f98a5f3a395e451ce76ea3deaef82efe7f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8f36d0e1f5252e42bdec9bca7e8df471e3cf4ca4533412e4ae08e7f6aa7900(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f1c25b3407e383ecb5fb282b52a6400ca04affa73e18f723179efa052f88479(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590ada3fbb4229184dd0f4af77d57012dbe743b7404c04df81e5f6301d4da8d4(
    *,
    case_insensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    column_to_json_key_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365025d822af9986bf424aaa3d77ab0e417e4e9dc308d2ab1e211435f547b2c1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4b906f4503b7bffa587484f96175fdeda0ad9fc3f796a5de61222401e13fa1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0583faaef1b37d0b6a46f6d20312d98ae0a029edaafaf6d382d08872006bc88a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef6972ac56cb589844645be659c43b27741383e0f35fa6b638eaf946dce1a774(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1876743364208c9572630dbfc6d0fb399966a597a79a435434bfcdf6b945d811(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35a3cda55fec7cbf67eedb318e409b2edf7c63a6c91ddad7cec734f0358fae5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64701847d61fddd6bc57f9ff904f50fb0f97bb108eafaf8c8ac4f0429ab2b9bc(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366b6fb3d362ce70a2be77fd6dcca309dc147af6f7a038d5c36177bfe7858b93(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165d7e2622c66a6bd311d4bb90289880c1d200a3d6199e4b84403880dd4a55dc(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb9a4a866c6eebc773c33adbba42d4748e5e91cd0183a7cb1edb8d9b09aa637d(
    *,
    serializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ed7652d15d0ab2676497e82245768731b18caf67e331506ee4adbf6122284f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c2bd34d3fd2bc05920699f6d629162c47361639bb8277c177477b536640e0d(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae891e7dec21aa17cd81e339787be0c8d3359177aff16ab0e8e78a592e6e4a6(
    *,
    orc_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe, typing.Dict[builtins.str, typing.Any]]] = None,
    parquet_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4fd36fe2476bc4db7dace2331bed14c30397656c912440b953b125fba04105(
    *,
    block_size_bytes: typing.Optional[jsii.Number] = None,
    bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
    compression: typing.Optional[builtins.str] = None,
    dictionary_key_threshold: typing.Optional[jsii.Number] = None,
    enable_padding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    format_version: typing.Optional[builtins.str] = None,
    padding_tolerance: typing.Optional[jsii.Number] = None,
    row_index_stride: typing.Optional[jsii.Number] = None,
    stripe_size_bytes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f80109d423ba7901f8ef04fd83e4139b4f27cefb7de12ebddde3a4cc2e2579(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f1fce1c08be3bc49571add75413ebd3811f7aed943161ce3f5b3031c0bae28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41efc3a6a85411d1adab5cbe7308137caaf5bc98ad5ac67af5664c8f9ef1da82(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9b46d017e34512be1ae8a276aa994ea0750f5ae715f7204dcc3aa99e2349dd9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a69e6c431d4880aaa7f01977c00acf112a8e5abee32a492821a2ed6856e1e66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec5351973d737ce4e7698a7d0704265d7766f44286406a400014ffee3377f03(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76326f9e6450d06c1837fb5e57c0f676ccd1da4e036e2c85c5c5dd868268e51(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da2e7fb2087338ecb654d6b938d13d97a7ff875ad79fd5337f7b3471098ca70c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba27aea00e12cf604dcf6bebd28ee88cc452b669e0937b1584db77a6e5951c85(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8356799cb9b8180e3cfb6deb9f59c2d997ad9059c63cba23e9d032a4ee6eb658(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18cb825299ea43fd12a9f32edde0bcea7657bb43c27906c302cb4f79edfb55bc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26a82ebed6337020038ccff90607c7038ae2d2c6e598baf40e68bd700f101cf(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ccf329794c98d4bc787baa582ef94abc1861334f53428c51f9e6fd32dea3c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66832fd8b9a7ce143e3880fbba61048f7ae2400c0aee6514698772c6749bb1c1(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94f4a81e2a5a84e3f54816ada8e062d0817088c25e1c92ee85538036625123c(
    *,
    block_size_bytes: typing.Optional[jsii.Number] = None,
    compression: typing.Optional[builtins.str] = None,
    enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_padding_bytes: typing.Optional[jsii.Number] = None,
    page_size_bytes: typing.Optional[jsii.Number] = None,
    writer_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46209cfe193b37dccbb06f348ee4c2fcf6b21eb31f07a3d78051f89ab6308c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b66b4d447e66471523cc341d4ab13daa786c56d1cfac6d6e5a26bd2aa044260(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41d0ae4a4d93d4e716171d9be2669329fb7c956d04f20191338806e8be330f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58574534c8af72e68605aaa0708dee0c5dde3221e09d8f52f93cdc865771f7c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8aaea54b882c268c2d4c5a141c921ba8d4a8dcf66d7fbab8dd2f8e32493d805(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8f00bfa7db9196572f462a26090e1dcb42b27363561e301c9cb18268cccd832(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed127e2e92c888aa3ea87f8dbc157d5163fba19830a1b4b6df15bf026fae0834(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85f53519cec78a65a22c6432f91a0deef7eccc4efd69cbdffd8be42eb573f6b(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f5a354e2711ececcbf613e80d1a24e9cb60c9c92ed57baa7ac99bfd7cc05e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0864054a0e236c32276e5a31b6318a22d175c8b3d44f3fee710712335133c2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed90cc8bcb1fe89cd72ebafcc15caab823c7880a0d6a714d947347379d8b066(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e723402de6be490a47ab6dc5828a6679ce255c958a9f380a620667de25409f8(
    *,
    database_name: builtins.str,
    role_arn: builtins.str,
    table_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f79a0f386ec6b96915d08da529312c22ae1d98d494f35dcbdf6f2f1c7c214f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85eafbec27e10ac27c73bfdebf44981656349184c967abbf84a81f63f24f3afc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b60bf1c7b4b9441e9d90a153bc611612cffac0e97fc7fa905e960b2954ec62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2102e426d296488d211bcc004ed2d0095d5cd0607d7dfbce02fbbb11703ed270(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3535e18441b6c87d13ba8f0eb467e8817fd9a9fc802ded10e66c1e52c43349fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b4a7baa2895e69450d8fb2c964a5e460252223e548439f8e9c5e3d2efd64bde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a31bf2c28c50ff29f369595c2f5db6fe11978b74de004a89d280da2605e522f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72fa1189c9e4c0d670cf186c8102885e53e059d42b969961b6f3b670606dece4(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f63a634b5239ba3078dcd3e9b73e52c413ae3be57c9689ab8aa876b50a688c(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    retry_duration: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c6c5e48581128edfc2f9b69141999928044fc27e50b3b4a0f3a4a35ee9e6bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b20cb4e33f91e01089d3c70b9534b80527ea1ee31764093094962d55b0c515(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d02ac1c449bf8c8d994cb5b821845a6604f4d4e7674deff6d57401158ff6d429(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a030566b36aaa0928bd0642fdc654a74e0c8ec2a5f45d9f0c9b4b4f48ee22b46(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5521d1ad307d36f19667d289ec2e5d168673d43c3c06ef97eda3d9885b2bfe0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__896428687302f3195799a180abc7d9ed2fd1cf1230d0f33b5c4588afc2817541(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__192181385d781559e3064a4b243d6c1c176b4f22ce3a99896ca66e82b5894695(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3580fc7281fac80842b1e556a8a1946f6f489f46331ae9d846fed5e9d2fd07(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d529161ff95ce98cc8cd6865f3f5c731e86ecd65a1fa466460676f89991fb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0bbe3f8c84e0adcd1a71661c100892915d29ba5d8fe590848b0b73eed911da9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__175d9b78a41fd80acb52f2c7faa308ba9f348ef219d9fa4d859b32ffd778767d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8243dd6a97b1533a4f07b6f6219b907c378795634c07c15ece0ccce67651821(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfde829d97aa28c829722bc36691aedc5fbd82457e7d4e815dadc9569258145(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e341d5e81914cda36afe4ea18c67eec480dc11a2236b1d760a844e72ca8d0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24122826df8c0594ea6a154d8857ba5094718df0c195cc506791b819a5cc4efb(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd0457e17084e677c8bf5fb6654c2ed21e8068f709889a7a695d2700295c7b09(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0771ed52dd9572e6710f4dbaf5632bfab4c47ad0824bfbf46e1e219fd70f1bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b48c38f936094819940967f4af6344bf3c15425e0b84c276bfe338b48e68dc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49052177942bb73e716eb2f26b8f1a0eee94b00c6e112346824ad416ea67071c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3abef3633c5ec972cd20ea7a8f96d058448e716ef2e3708a873d388c6519b723(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d551d14b392bce120ccd566885b46fb8babe3b8a610052a256904c314bb6a49a(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f96d5dc45d465606520728eaf2abb4a7a2e84a11245904d41b4479555ada2f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a690af17a3fbe598805e979d166c79b948aafc4daa28828af79d9f65bb2b08(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e7b0d970730d3116597c003d389f716c6e85c43f74b91ae120d6f5d477c966f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50151a35e2683415840a7dd8bf17604ebb418863ab08bc5f80b5cc36bc6216f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b454caaa6b5bc1dadeb112fe40035ab6d9252456b483fea752826e32ccf5e091(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211af262acbcf0e4a114036d42af85f6ef5b1dc23408a31fbc8b51131b191ae6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c9085c9ac32d6311accb256801b07b70e69a4549512de8ac7d3426c1fc7a73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c726370681a361c904a3ab45d85ca55cdda7c0d6bd0ca3137dd61a5e51bb57(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d53f2a6af421375bf0d67abf1b8a2409566a6bf4934db6ef4ec73b6bd00c3b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc12b7d8c4b9d74cd0e0a40f1aefa6f7b25499481313229a1ff688f8e51f9fe(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aac13dce1835719cd2d2089733dc5f9c41b4426304f5bbe6f15f651e89db033(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75cb82c9657df5bc47c6fd3214e1bc56782bacd443236373ad538ccbf4fd2352(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf43f8e772836d028610119b0572c5c79c02b25f75fbe0cb52c88c86ee46c22(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67fe600fc2514d6dffb82cfb3531a2f197270cbcfb48d20fd6949b9a2ef01211(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73579366133c8a256245a3a0f0b1262aa0b37f10f077de3fd3e478235290802(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfbb39219d846ae6f660b374bdefc54c71aceef9d0845be6533722c8459902aa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47948b53804f3c24afb84baa8892cccb9570cc0a8bf8435e00d7e465250ac377(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51380b813c8022efaa9ef4e39509b59128727e5ce3655828a5e818d0dc3cac59(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449693267986222e5ea2b4df32a13f184908be84f2970650de479fb4ec424e6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567b5e4dd932ced9215da059e0c0d13505da51135dc50a4abac8ca76d1c97023(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceeaea6a0d4ab0cd6cfb053ba5f6dbbf2c0342d42a6a2f5789572c268985c9b1(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ae4487ad22fb4c897d0c4dcbef872d924edf4acadd01bc58eb2a91c3ed0ea8b(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffer_interval: typing.Optional[jsii.Number] = None,
    buffer_size: typing.Optional[jsii.Number] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959f218ad959a5ac08be3be3b93f796d27b0f7b3c204c4d9387c7787e4482bcf(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004aae435582a833d36c84f41dcce1da8120cedf991ebc92b0946ae661cad63a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8773d713a5532a396611c3d82dcdbae4b1445b818a9df236219d77b6a2b5aa53(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb30593c2243537083dedb3637f6f4d720eb80ffcad51a98e06a251f47954aa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39fd1c8ed27ea83b867e9ee40382ab03e6b163d10e3d40e76fecf72d546223de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73847219263c36129e4c132a1b9fe14e51b44414842087f5fb64fab72164d740(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75c497245070483a0083d5e8b780e3bcc0bbe23ebdaaed8902e9b7c49f06c92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e56696e81ea0f2343b493b4daf13fe0551c94a36ad069fe0f0b25dc1e0e7fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82eeef75ac8ee9f3f4fd1308bfc5382f87152ed76d7c5f89c83eef889c1e488e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712eb1e1286723e919776f106b9f20aa7c26001fef22e0400cc6c8818d9116a9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b94bfaae7d8d976faca7768bf336edfed008746417fab829958d1952e2c7aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14d5c85062ddda295863e68f02daa62e85fa598062146c86fedf00a2105e8db9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1166bb7a9a192d250a62a5610ad3df3d68fcdb9c80c6abaf3c33c7de561e8fa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a26295a918a05fd75995a8f07468d77d19cf32ed078e598192ca86f019aec0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630bb90eef04ac3c6529f322dbdaaf02b602663e4735c1433e45ddccc7411dce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70f99af6f86df76f139aba8cfba0a9273ef7089baaabc127318845abb26fffd(
    value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab97d11afe8f8d15db68cc4b6b2faf37a63ca23f61829aa0d09099c1c66bddb2(
    *,
    url: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    buffering_interval: typing.Optional[jsii.Number] = None,
    buffering_size: typing.Optional[jsii.Number] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    request_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_duration: typing.Optional[jsii.Number] = None,
    role_arn: typing.Optional[builtins.str] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__276a8ecc81e8a05da93c4198296bea13a5c4e781f17274d9234f834018e039ea(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8b1b4da48a0214e2d7d379203b0fb60f275621cb04aeaa9d8cbc024b2c0793(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f0b9105eeca0fec1d12fddb903e8c4425870d66de0892dc8b84cde46037918e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3662003be96daf1ca1fd29b0791acad1fe4dffcda48cb8041f48eaa8dd053b49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e163379aa19717725001db217fd9f38218d20ec5d00ca3f3f8b58ff2c48860f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a08a7c90ab93ba2749dfa45f36b998e5e3486cc57abad221bc7a383f9f6894(
    value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4efb96be501548558036a70a585b352642f18fca50ddefc2beacdf431a3f661(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297e2a6e62f99b8223c8e0b9bc6de624f37678d9f7b41f05bda1fa3f35d60a61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b941876d9815af3eac08cdc90ccb00c6b22757b44e1cbd243409b5e27e221d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcdcbe4acdff883e59b5124b6b126be11d2497aa89b3d8c5a75124441c53af5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33dbccd5c37d140578eec6e3d5607dad9b9ec57ab72d67ac0ed96717caaa684d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b26b7505126e9a9ad5b572db9586662cb00fadf6f60e0a360dc725f16c1d781e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fcf599645d4d9241cf09775ec64d2b28e64eb729cbbdf947243d5f2b8e6372b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba0e428b591aa60b6e53748b9bea48583dc22500f9fabaf043f171b7f0a30337(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d629a052e1618c35be71ae5cffccbb61c06f93fdbd9f109ac3173c3bec294d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__549be67bd992e1a7b8a8dc0918343485d02f430f61502147ab760d6677392fba(
    value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a2436a43702b988d0fe1962bacb2fa461c222052046faf8d3a9911abe6c7a7(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9367a249778d2db4684c49762a35ed0a7848453df85cba59350fce1a038348(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f0e67f0d76513b59a771da57ce06b023e0cffcafbe9e187e6dfa67940675f8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3acc0c33cf863e7e2034f12703dabe973bdc07ca1ccce2d41d66ce02e61774c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36975b3cb0d1f179fc49015de73a4acfaa6be4ae68ad233b210d78d796189f32(
    value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea1aca0b5c4e57f65b53a7a1c020911797909f7046c5f0efae91cb84d2e5c9f(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea3e38229361bf8103b8d3a5f7f0a17a94e3c8fb55dbad6320d6187e8c74a43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e526698b308aa52437a2346a9b8421609141ddd97a76013595cfb90afcdbc2a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f900f08a89dffcb19094655d777c571328fe10631bb0a050667b828c92e10653(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300c45d5d4d1938c27775063a823b2c4c0358e6fdb33f9bc7fcf5cc98c3a7414(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82204d3ea648bde84b1b1e79066d1cac90e6809983a3c86759d330d28cf9c280(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5149009d38881217132672170347029d0377751b0c648b9ba52c67d1d1addc28(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fd9e5e2c6995946db393c867aa3a40536f6d642630d6afe2cac669d5dddcf8a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e969448550b14ef825122581706e2ef5a16e75c51af16a574fd362e609933529(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c5a071d44f67c44a8adaf00c216c5cc059d13306bbb892ba6a1fff62a2d0be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df87594efeb49206dce58f2d73789193f984efc0ade359027439e8c8bd2c110(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b93c69d9c62bbb9cd1b07f2bc08f381716e3ede25cda75b916adbfa5414555(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e6a0a8faa3ed4a1f5d6d11c56db6d667d61a53231e9116d16e469bf7315c80c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8578a8c038af87e3e867c91daf5a2b138cfb44f78809d09f61e669f0929ac26(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c119ca67afd6bdabc65dd7693a35d4cdac310b44c545901e55ebf0b8bcaf3f5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26749795929b0c557c931c067e5e3570a238accab53243a38b7c43796b923f91(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d475b3da6078f6ef4bd54517a0b59c0393e27b91e178c8f5a264df70807097(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9992b5996a49f984f006441fc499fb37451bc2cc4ffc2638c375e75bf0699fa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4647a85b6daad7d7da34a09dcd18b766dccfdf650948f6a482ac927cbf5eb4be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed2d949f842f2f5478e5ddb98baa9d1247fd650ffc02590bb9c63bd5c4a46455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e669cf7f173ba9d40b7f685abc0a4dbc22458ee637847ced7a936c8466d6851(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac32339aa44d3e5709db6bbcd3e3fdda662b9a44dae565d1d4a3fea2c5f95cd4(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__873b74f491dc758661e8e613eea988106800d4861fe1027755f54f0cab8890a6(
    *,
    common_attributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    content_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf79d1f59ca230a4299a2e0839704cc6116603727bc56020f2975af3bbe9640a(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588a0d1dcd78ed2a676536810efdef90c7d964513eede37659f4f97c45ae7612(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05def5ece8a709cb9a4f7e4e75704b6de98dde207da95890693816e02ec52da5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc9245a84ff86e2c5e0e6dc9d199d15e9a0577adb5d6aa729d7a88be24ee2a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b0518091a5f9f452dceb97701d412ed2a5550246122e035d206f9c1d345b20(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a722940fffde0b3154a0d8252855af9f0f139785d8930f59fd0212dbd2ce34(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6bb9607c72d2514540bbe8d82ae974fa4062f37a2df41fc67c04766235a5668(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce2e582df122ded5313b8d1a7bb4120107e82eb99a7fe0b9dcf1f6ecd6b1ced(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b42655fad9216617f2ad0b16ecfd44c56aa78c935935bb1d2d507cb9e20af5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322c3bdbc7c4360fa83231110e6272f174977bd3395256af20dc031a1b0132bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d8fb27fcd201e4d9077490bc97cc432bffae160f061191a7dfd7f3f836637e7(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8050069695a1f4e54d2d45dd5824ad39691847969fea9037bb325a67b1fcf4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e37481e1a965d3a59aa83ee6193d857bb698fe0fd79757f8fcb1e7617e1061(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638a9bb75a96c7cefd49dd77bb20c873a9a57ffa84f569c1a27eb63c7ff07389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28cea82141726abf06aa9d02b71304fbc225ff50a2f54b92054cb889a2a9ed8e(
    value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00ab24caa823f43f686d6eedce372f264ce7c9d4eb5d38efccea075616466bb6(
    *,
    kinesis_stream_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__805d5c91f60af5d72d5306b61279c2447b9a067f8fd0ac37b4b3e9fd5fa04b65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bfb8b4844c773f1eb517d96d00370516281f710832d0cb7d2797284f9cd79be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af43f2f57e73cec1a068ace4f52377f39495406ba033ecb2799cdbd6d9a2410(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e211dc508c66a7734bc12ee4c92bcb00c3bf35fbf3c445fe029641eeeef6434(
    value: typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40eea6b09416a89c26f2ceedb1c9b938944c17b1c2baa52fe8a829bdaa459c3d(
    *,
    cluster_jdbcurl: builtins.str,
    data_table_name: builtins.str,
    password: builtins.str,
    role_arn: builtins.str,
    username: builtins.str,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    copy_options: typing.Optional[builtins.str] = None,
    data_table_columns: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_duration: typing.Optional[jsii.Number] = None,
    s3_backup_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4e9f96788ea4b45cd57e876b50a60d9b0e982b5f84718f2b2c5e1ea4dc176f(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7c169d3b98e611435fde4bb5a4e51d341728b3daa594755d8fe315a462d481(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5946e5700d8b9636f6524f48ffecb245c2c3f5764ea4abe64a16a5dd7f934a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e15fa2b1c2dd6479629a949c8105474a163e1296fbffe3f17379eb83764f0e60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__effd60c4bc3409ad2fb27d2244306f6982fd71e711a656ddccd063278f8d078a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9a5d93f47ccaabbf4803740f587f3a6c990e0599635ccf972b8d1ce1cb1a1d(
    value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006d12f51d344a2ce65afe432f277c7e00936dfa9acc98181c435167866c7a72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab16c44044cb9f57efe839a70339c7ba7b2eb68d3f14f60321faf93a307bc1de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44c950d48f902bab62914fac66a46808ec6accd574bc473fad2053421c9a869(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551b1625636403cef154c6db1f61c61d8aaa67150253effb03e3d884bad4b298(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34de3b4fb4c91b4b86d9b58f94214ac38180ec8fe3167020c6ccba8e3e4301b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__310d90a3a7aca345fb3a8980b6cdc6081963ea82b3363b4a508e87ce6a59b738(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb162187b604fcc07fba57165bcca3e100b661ccdd1db466b66e8833413ba073(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b46c43e0e47dbd2a5d765b4093964dea661b24f998f645cb97f6220a72c73e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c080d5117c3add52390aaf761f42dce5fc4c7fecfa7749a1f0b3b2e9e959a3be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e43abb13f6bb454ce3fd119f4be0ce7faf40b289d25621aa2aec037a9daa72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2d74c4443eb32a4fd761c63d5b564027425139497e53907631e44031b4ce3e(
    value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce391a624927f6104c57b129e0ed7ee41ee6327686ef4cbfcd856cfe4c45c2af(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4355d7c09120ece7155a43e87fbf877b75897cc3eed84aa904a34f993a29a2f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99c49b56ea80fe71a82ecc58035f00c075293f6b8224fff0b72d6364aa82aa6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7feed419c6c6b99d1f5b8a02609cff707ae6e402fdd95a56a1cfc599f9b0fb2d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__394f8f4be7a564752579a0f5ceb49c84b9d97cca9cc65b9459aa8cb8cddc989f(
    value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ec0d9ffb26b3ec266f44bdf0ea66b3273013e6bb8ee6041ede5fa7ee1b175f(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4fdde7d80ac6b7c80a9c75f36687d7fa60db5fc9b45c9b346a15532c92fcc86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92db7168c871ec692b311baff9bc1cd40f7df2158590a38fce71cdb085b4736b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f521cc40fae9a21d341e19d56928a64511e1cea1ae954e7058e71ddb0130e437(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c203f442f18f8ebb35dff68b0deffed587803654ca9ed9243e97f702e4b7d9d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f65eb9805153d8ab9b6f762f9ab2fdb76393081cba0c94c284bb5fdaad83fd8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aeb8bc4097b8c7a63412b0ad9eb90f4c3668698a7859fab8921739c77c2cb87(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473bcd22fd403947e262eab8b0cb9556ef5bff6cf3c100e335481c63c6869f8a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa1726d1f14be4f25335d59c708f3c158997870ce758870c1f0808d0414f454(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529c3d1ab6a770ed023eb854759d2b2f10c1e6800549e1fbe39921c9da0abbb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43250bc27f0e424f3febd5f812f299e7012236246da65866f1c95f6e11d511c4(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17bb5ac5e75ed8278aec1b199dd522910b3fb1e80f2679b560d7951cfccade0(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffc64f2f4529c1a57d7b6c6c4f73dbba704a64b0c373ee26fb5d141db7beb0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8687149352323c2d3d509e65ffbc480f4aff04363870b3c8ddc2285656867ac5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e569adabf9bbebf4f540bcb11e8755e129ac7a6a441aba96b0cf72548f500580(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f2389cd5a43ec01b87370b3874fd2fcc3ea00171294d1ff6e61be4d1f40640(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e844bd5fe4729c63e2a336b393559005ed83e825d5a97faf9dc69efd87daa54(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a3723c69315b457600c2169b985dc616302f6e6fea3f4f01b3ea27fc3cf07e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec30e2ecb638a79db5bc22ad82adf264127bf7c5fee35664b3537888831dbefd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a2cefb06d3a83da4a3694edd65f4b2a86fed8eaa5e5d1426da16e09f17903d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d316e5f73537402e7c2489b82fcda8c768a406d9f6ab6df16066db886b84f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbda201b42a94b76925e95839bdb89623f73fdd493ea4372b2cb91531643b27d(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea9c0e1408ba60f7446b36f188761b0bc1fe92b1d47a31fe574436b529e82037(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffer_interval: typing.Optional[jsii.Number] = None,
    buffer_size: typing.Optional[jsii.Number] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43efc9f813a6aee004178da83ca334c5e0dfdbe96b62b537caf948da473edfe(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70246aa003f8e0d89671f4dc7cc80602d974244a5bcfdcec969ca2ce05b8cc28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__559460daa2d988623159e37ac55afee7f56647ce142cee179570de6f669bc9d1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6b391408ac3e4366eb89647116f00f07d83c246cbd945913c7054aa4a43fba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1036ffaf34270cd208dbad782b82ed151ba41d9dc681135d93289e8eab19b1e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aad541551bccb8119b42fb2d5fac510d61b71286b3e802cd2a9950146948749(
    value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646cc416de69438990beabe925a15a63a4ee983e539b704eb4636a11420214c1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e92a79bcedc27045d1fcdad37a43136d28d79ffd8169d827fcf3adc4aa9e9d48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e3f464243ac893cd5d7e917426c26e973dc02ed4d7687b7a8a9099a8461a95(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d296efb79edfc7c225c6493e110381690e75b8cdec719e02423a9e064026c24d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f8c34baacc1d84b1863063b0b7db2580c79748d1404b8f86f52a545c1f83a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1de0d3a25f3d6e777e4729f4099eb3b12cbc77d1d81083e62cf61e22305b78a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382465c5baa491754a7d0f204437341acbe0f65f47d0934d1ed669594b309b1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab3e2ef6e0984e2449f79c496c301220d975cffdca428a04d9c11fe0ab2b2273(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5e9f839b56b127a2bedebc97e9e8c17a5a4e4b2fe20a22fb72efca5cd91e74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b108e5ff75439dd42c4be7de8569ee7a7c24412a47f0c8b404d607883c557072(
    value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__176d6d5ec99795618674f1503526e5bd5167e5f19989f17b426b787ada06d1fc(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffer_interval: typing.Optional[jsii.Number] = None,
    buffer_size: typing.Optional[jsii.Number] = None,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd439410fbf4cd848d5177def05c4abcb9eaad479b20b034e3ec95b350877e30(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0602f8b9ea4db951e80c625b161f27e4bc1c96dc4bd2b52fdc38dd10bd9dec6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a487b73a1462972d87e65ff41c2b3d4e544313fbbc9e858d19d311a3ee4313(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c975bc11c1d141b8272ef9a7f64c017cdec47576503901af0805c1e8562dd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbf982981c546a7424e035fddf4734f687a0ab6174746e42a7af6f20e14be344(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bad78e6c5e50dcbdaadba6adebc88ea6f800a89c25a0bbe7d9de05c238f74c8f(
    value: typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6d7aa571d67e708318d32f82346d41a24eebdc2dcacf56c94fc2dee4af3530(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fc471329e578811729ba3a215bc03a1c4701d015bfef752605666419e0f5465(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9222e32047480861b1a4583929e29dfac78f62faf7b4897e8511437bdd383ce(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606ddb342b569e0ae59724e68a74f82d931ede9988bbf6f199b973d2455ee7e7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__423ad31dcb1f4af90f36070ee3aa059005329cde79775554e2de46eaddac8804(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04387fc689451142049400cb0467c4896e34bf4f0e7e8a7ebade87bbc5bf82cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c0a87369b0ac0aa60d9619ef5a68384f6be77b6b8db2f789339b4f06fb3099(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab9034d35f7b000f07825ff6d491aa666003a5cc4d4ebbeba193a3d42f755fe7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3447aadd8805388cbc40d8c5c7d48b6bb1993a28263da499fc79b9682867926(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2f8058eb04c71eb3402e2565f08ee2e34a6ef9d5e0315516090a03b16b4a90(
    value: typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92d3ebc16b9a4f056f1eae995fd7460e94528e8cd57f511261e1513a1acfc42(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    key_arn: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad9ceb3a8a3112467c474acc0c638305d8cb7a5748e8bdd36fc3600698e3fc27(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d37b607372a2748521150abae05c1f025f17d4266a7936dd2b8cd11d8b9b1222(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c3c363f9b85df68670dee0e653aa8fc17e6c16f4c8693529d3dc4c008cc0619(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4144668ea00436913ef97569008ba5fff5ad34a635e35e415e8cbf804a493ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b74f2ac555f6dbc7fdd006aa939fcae2ee8db6772e9103cf61af0ee7bdb90c59(
    value: typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a69c6ee4d9a54ecdff2fef6d4104ac29c47d7e6bebcd61f188fb0da3a2f827(
    *,
    hec_endpoint: builtins.str,
    hec_token: builtins.str,
    cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    hec_acknowledgment_timeout: typing.Optional[jsii.Number] = None,
    hec_endpoint_type: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_duration: typing.Optional[jsii.Number] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63212ccc96f5f69cd2f6ce255161ac43ec19d4a1b0e6f756b698ad93a3d202a(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4345fb3a103399328ad8aa00462b2904d122c0ac804a54eab638cf54e01a145(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8add111b2dd0bee07297443dbd2b8827d9847d5231e6005d3f0205dbb48c56c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51f9784a0af873a2d7c036d737b67eff8f070c75897032d46eb0e66f746a6c72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da72bc535c57c4688639f715432bbad067c263df0b18312e3fbb0782de82c2f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f248142371578b85d6bc9e345a2eaf326f98c6fa3111a079098a0230a0d94ad(
    value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd40963c7a7e45e1b91876bfdee9c001e74f58b277ed443f645f8513d4d82241(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2949f24a9ddf216d34f3d63e0d2210a37fd40a2945499d52763570b8d5b58626(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b77f60c85dea3eda738e6c8e4df10f6eafbd535bc1c865c632ac3170122f1cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bc8677716ccd14eaabefb4c9c6deabbbc6615e95c30d139cdb5ebaf9006d3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e15be6763927fd3cfb65b79207e3bf12a90c1c9719d7398feba89e54a525804(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4925175c963be8d2b575aa13d0a42c0193fef5e64f7e373fe645032ab8a6973(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c0e2dc84395962add20047690e512e443c642b0afd1b73b0785aa2d5dc8ae4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75100b836a10239a3c88c1c00be97ea8a963171385c2da1d8707aa2f7a300537(
    value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff2e1a32bc4becbcf409900ee331f9df198b0969f5c74d0d9c83b93332b0fbe(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    processors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b740c95690c5fd343a4dcb0f8dcf200ecf0389bc31ff268a7c599bd44192dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f403e784670c8fb8f174eebfc2acaf5bd57fc590e9452015a96243ee45ba2c4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f276763e8523357a028c94ab1e66104ec1d6c6a7c099d28e730c482c840b97(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d34644921efabdc8a64649bed19163d23decacf5c8e2bbe714163f2b12153e9(
    value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__920a4265d0ce3be5dfc33c659355d4e5b791aa9c64279e9fac120f17ec5159e2(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdc0dceecbc88b036be34caef76dec39ba440d3cd2f771c2bf58d3e4eabcb593(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5577562320593889599d66d05257d9113856f032fab76283491eee57b504687(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c002e68aea84aba0009f09228206913e1a83c83c7467f3f20b10e63f08a58a72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c6fb23cbe890beab08e062217909fd50c551d8aa9c1b2a49543f47d22f7e88(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd70333bcdf4bf02ade121296ff5584d0c8baa7d084e8f3dace41b1f6749c647(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b530c4ce26c477a48057964b36d6649c4cf5d45049e9b83dba542ab0f9c3735(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd16556352116b65ed309b196e57b4e8a8afa890a4810b681c5366eac8905080(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589034df89ea26afcc11cb9ff36181a65e15c461a849b2a0830c061b5ca304ea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1792738440b08678e1c31e04803b3f0ef75fa9119797f5a140c584693e55376e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923cc0bd0da6d0453fc6279a38dbfd87cb8908bdc941605c4b913fffa059bac2(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f95e92c88974d1d6be7a5fa25d5d53f26db2fc7607ca28ca6ad0c5b42912a9(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a1d818e62e2df4d5a723a9946c00f5c13013c8a5994a2bd50b74bc43b8f5be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea02ba6b4ea98d14da957e23a3149fe933df0c422182193fcba05d43ab6e86d7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa15eaff19bf3b83ef41230d187364a1e6ef052a3c4a442c5f8fa19d7db168ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3390784aa8b72adc3c01c4887fece7efafb90baffbb16083add6825375c5251(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e83bb3368b06db31a0d8a0c9e6ec4d730ff1d604268065e23f437888c6882a63(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed450f70c6aebe079baf0a77e9c0c56cce8be8f7157b6ca04fabcc5bacfb5e7a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab846656846d886e29e0139926d9f751fc0e2e43d7891c141b361bfa8d4f9358(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1a4d2289384cadb204a4599bf39283df5ffce3169b1013b176e7c562071672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f1225ead1f29ef5c31beb3b5c244106bf64ae8dcd6028e9e7d7ac89b2f33eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f655d2fd9068abcbed2a791a4b3e4878199afcc912085c017484d9bd48a3357e(
    value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
