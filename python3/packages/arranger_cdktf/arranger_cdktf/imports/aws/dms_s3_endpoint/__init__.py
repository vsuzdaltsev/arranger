'''
# `aws_dms_s3_endpoint`

Refer to the Terraform Registory for docs: [`aws_dms_s3_endpoint`](https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint).
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


class DmsS3Endpoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsS3Endpoint.DmsS3Endpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint aws_dms_s3_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket_name: builtins.str,
        endpoint_id: builtins.str,
        endpoint_type: builtins.str,
        service_access_role_arn: builtins.str,
        add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        add_trailing_padding_character: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bucket_folder: typing.Optional[builtins.str] = None,
        canned_acl_for_objects: typing.Optional[builtins.str] = None,
        cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
        cdc_min_file_size: typing.Optional[jsii.Number] = None,
        cdc_path: typing.Optional[builtins.str] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        compression_type: typing.Optional[builtins.str] = None,
        csv_delimiter: typing.Optional[builtins.str] = None,
        csv_no_sup_value: typing.Optional[builtins.str] = None,
        csv_null_value: typing.Optional[builtins.str] = None,
        csv_row_delimiter: typing.Optional[builtins.str] = None,
        data_format: typing.Optional[builtins.str] = None,
        data_page_size: typing.Optional[jsii.Number] = None,
        date_partition_delimiter: typing.Optional[builtins.str] = None,
        date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        date_partition_sequence: typing.Optional[builtins.str] = None,
        date_partition_timezone: typing.Optional[builtins.str] = None,
        dict_page_size_limit: typing.Optional[jsii.Number] = None,
        enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        external_table_definition: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_header_rows: typing.Optional[jsii.Number] = None,
        include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parquet_version: typing.Optional[builtins.str] = None,
        preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        row_group_length: typing.Optional[jsii.Number] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsS3EndpointTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timestamp_column_name: typing.Optional[builtins.str] = None,
        use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint aws_dms_s3_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#bucket_name DmsS3Endpoint#bucket_name}.
        :param endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#endpoint_id DmsS3Endpoint#endpoint_id}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#endpoint_type DmsS3Endpoint#endpoint_type}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#service_access_role_arn DmsS3Endpoint#service_access_role_arn}.
        :param add_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#add_column_name DmsS3Endpoint#add_column_name}.
        :param add_trailing_padding_character: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#add_trailing_padding_character DmsS3Endpoint#add_trailing_padding_character}.
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#bucket_folder DmsS3Endpoint#bucket_folder}.
        :param canned_acl_for_objects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#canned_acl_for_objects DmsS3Endpoint#canned_acl_for_objects}.
        :param cdc_inserts_and_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_inserts_and_updates DmsS3Endpoint#cdc_inserts_and_updates}.
        :param cdc_inserts_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_inserts_only DmsS3Endpoint#cdc_inserts_only}.
        :param cdc_max_batch_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_max_batch_interval DmsS3Endpoint#cdc_max_batch_interval}.
        :param cdc_min_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_min_file_size DmsS3Endpoint#cdc_min_file_size}.
        :param cdc_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_path DmsS3Endpoint#cdc_path}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#certificate_arn DmsS3Endpoint#certificate_arn}.
        :param compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#compression_type DmsS3Endpoint#compression_type}.
        :param csv_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_delimiter DmsS3Endpoint#csv_delimiter}.
        :param csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_no_sup_value DmsS3Endpoint#csv_no_sup_value}.
        :param csv_null_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_null_value DmsS3Endpoint#csv_null_value}.
        :param csv_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_row_delimiter DmsS3Endpoint#csv_row_delimiter}.
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#data_format DmsS3Endpoint#data_format}.
        :param data_page_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#data_page_size DmsS3Endpoint#data_page_size}.
        :param date_partition_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_delimiter DmsS3Endpoint#date_partition_delimiter}.
        :param date_partition_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_enabled DmsS3Endpoint#date_partition_enabled}.
        :param date_partition_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_sequence DmsS3Endpoint#date_partition_sequence}.
        :param date_partition_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_timezone DmsS3Endpoint#date_partition_timezone}.
        :param dict_page_size_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#dict_page_size_limit DmsS3Endpoint#dict_page_size_limit}.
        :param enable_statistics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#enable_statistics DmsS3Endpoint#enable_statistics}.
        :param encoding_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#encoding_type DmsS3Endpoint#encoding_type}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#encryption_mode DmsS3Endpoint#encryption_mode}.
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#expected_bucket_owner DmsS3Endpoint#expected_bucket_owner}.
        :param external_table_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#external_table_definition DmsS3Endpoint#external_table_definition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#id DmsS3Endpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_header_rows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#ignore_header_rows DmsS3Endpoint#ignore_header_rows}.
        :param include_op_for_full_load: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#include_op_for_full_load DmsS3Endpoint#include_op_for_full_load}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#kms_key_arn DmsS3Endpoint#kms_key_arn}.
        :param max_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#max_file_size DmsS3Endpoint#max_file_size}.
        :param parquet_timestamp_in_millisecond: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#parquet_timestamp_in_millisecond DmsS3Endpoint#parquet_timestamp_in_millisecond}.
        :param parquet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#parquet_version DmsS3Endpoint#parquet_version}.
        :param preserve_transactions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#preserve_transactions DmsS3Endpoint#preserve_transactions}.
        :param rfc4180: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#rfc_4180 DmsS3Endpoint#rfc_4180}.
        :param row_group_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#row_group_length DmsS3Endpoint#row_group_length}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#server_side_encryption_kms_key_id DmsS3Endpoint#server_side_encryption_kms_key_id}.
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#ssl_mode DmsS3Endpoint#ssl_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#tags DmsS3Endpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#tags_all DmsS3Endpoint#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#timeouts DmsS3Endpoint#timeouts}
        :param timestamp_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#timestamp_column_name DmsS3Endpoint#timestamp_column_name}.
        :param use_csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#use_csv_no_sup_value DmsS3Endpoint#use_csv_no_sup_value}.
        :param use_task_start_time_for_full_load_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#use_task_start_time_for_full_load_timestamp DmsS3Endpoint#use_task_start_time_for_full_load_timestamp}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0ad512742cdf6d04997d55f7ea2a98c2b216abd382b1182d64a744a132c6f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsS3EndpointConfig(
            bucket_name=bucket_name,
            endpoint_id=endpoint_id,
            endpoint_type=endpoint_type,
            service_access_role_arn=service_access_role_arn,
            add_column_name=add_column_name,
            add_trailing_padding_character=add_trailing_padding_character,
            bucket_folder=bucket_folder,
            canned_acl_for_objects=canned_acl_for_objects,
            cdc_inserts_and_updates=cdc_inserts_and_updates,
            cdc_inserts_only=cdc_inserts_only,
            cdc_max_batch_interval=cdc_max_batch_interval,
            cdc_min_file_size=cdc_min_file_size,
            cdc_path=cdc_path,
            certificate_arn=certificate_arn,
            compression_type=compression_type,
            csv_delimiter=csv_delimiter,
            csv_no_sup_value=csv_no_sup_value,
            csv_null_value=csv_null_value,
            csv_row_delimiter=csv_row_delimiter,
            data_format=data_format,
            data_page_size=data_page_size,
            date_partition_delimiter=date_partition_delimiter,
            date_partition_enabled=date_partition_enabled,
            date_partition_sequence=date_partition_sequence,
            date_partition_timezone=date_partition_timezone,
            dict_page_size_limit=dict_page_size_limit,
            enable_statistics=enable_statistics,
            encoding_type=encoding_type,
            encryption_mode=encryption_mode,
            expected_bucket_owner=expected_bucket_owner,
            external_table_definition=external_table_definition,
            id=id,
            ignore_header_rows=ignore_header_rows,
            include_op_for_full_load=include_op_for_full_load,
            kms_key_arn=kms_key_arn,
            max_file_size=max_file_size,
            parquet_timestamp_in_millisecond=parquet_timestamp_in_millisecond,
            parquet_version=parquet_version,
            preserve_transactions=preserve_transactions,
            rfc4180=rfc4180,
            row_group_length=row_group_length,
            server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
            ssl_mode=ssl_mode,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            timestamp_column_name=timestamp_column_name,
            use_csv_no_sup_value=use_csv_no_sup_value,
            use_task_start_time_for_full_load_timestamp=use_task_start_time_for_full_load_timestamp,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#create DmsS3Endpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#delete DmsS3Endpoint#delete}.
        '''
        value = DmsS3EndpointTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAddColumnName")
    def reset_add_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddColumnName", []))

    @jsii.member(jsii_name="resetAddTrailingPaddingCharacter")
    def reset_add_trailing_padding_character(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddTrailingPaddingCharacter", []))

    @jsii.member(jsii_name="resetBucketFolder")
    def reset_bucket_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketFolder", []))

    @jsii.member(jsii_name="resetCannedAclForObjects")
    def reset_canned_acl_for_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAclForObjects", []))

    @jsii.member(jsii_name="resetCdcInsertsAndUpdates")
    def reset_cdc_inserts_and_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcInsertsAndUpdates", []))

    @jsii.member(jsii_name="resetCdcInsertsOnly")
    def reset_cdc_inserts_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcInsertsOnly", []))

    @jsii.member(jsii_name="resetCdcMaxBatchInterval")
    def reset_cdc_max_batch_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcMaxBatchInterval", []))

    @jsii.member(jsii_name="resetCdcMinFileSize")
    def reset_cdc_min_file_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcMinFileSize", []))

    @jsii.member(jsii_name="resetCdcPath")
    def reset_cdc_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdcPath", []))

    @jsii.member(jsii_name="resetCertificateArn")
    def reset_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateArn", []))

    @jsii.member(jsii_name="resetCompressionType")
    def reset_compression_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionType", []))

    @jsii.member(jsii_name="resetCsvDelimiter")
    def reset_csv_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvDelimiter", []))

    @jsii.member(jsii_name="resetCsvNoSupValue")
    def reset_csv_no_sup_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvNoSupValue", []))

    @jsii.member(jsii_name="resetCsvNullValue")
    def reset_csv_null_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvNullValue", []))

    @jsii.member(jsii_name="resetCsvRowDelimiter")
    def reset_csv_row_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvRowDelimiter", []))

    @jsii.member(jsii_name="resetDataFormat")
    def reset_data_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFormat", []))

    @jsii.member(jsii_name="resetDataPageSize")
    def reset_data_page_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataPageSize", []))

    @jsii.member(jsii_name="resetDatePartitionDelimiter")
    def reset_date_partition_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionDelimiter", []))

    @jsii.member(jsii_name="resetDatePartitionEnabled")
    def reset_date_partition_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionEnabled", []))

    @jsii.member(jsii_name="resetDatePartitionSequence")
    def reset_date_partition_sequence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionSequence", []))

    @jsii.member(jsii_name="resetDatePartitionTimezone")
    def reset_date_partition_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatePartitionTimezone", []))

    @jsii.member(jsii_name="resetDictPageSizeLimit")
    def reset_dict_page_size_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDictPageSizeLimit", []))

    @jsii.member(jsii_name="resetEnableStatistics")
    def reset_enable_statistics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableStatistics", []))

    @jsii.member(jsii_name="resetEncodingType")
    def reset_encoding_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncodingType", []))

    @jsii.member(jsii_name="resetEncryptionMode")
    def reset_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionMode", []))

    @jsii.member(jsii_name="resetExpectedBucketOwner")
    def reset_expected_bucket_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedBucketOwner", []))

    @jsii.member(jsii_name="resetExternalTableDefinition")
    def reset_external_table_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalTableDefinition", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreHeaderRows")
    def reset_ignore_header_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreHeaderRows", []))

    @jsii.member(jsii_name="resetIncludeOpForFullLoad")
    def reset_include_op_for_full_load(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeOpForFullLoad", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetMaxFileSize")
    def reset_max_file_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFileSize", []))

    @jsii.member(jsii_name="resetParquetTimestampInMillisecond")
    def reset_parquet_timestamp_in_millisecond(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetTimestampInMillisecond", []))

    @jsii.member(jsii_name="resetParquetVersion")
    def reset_parquet_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetVersion", []))

    @jsii.member(jsii_name="resetPreserveTransactions")
    def reset_preserve_transactions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveTransactions", []))

    @jsii.member(jsii_name="resetRfc4180")
    def reset_rfc4180(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRfc4180", []))

    @jsii.member(jsii_name="resetRowGroupLength")
    def reset_row_group_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRowGroupLength", []))

    @jsii.member(jsii_name="resetServerSideEncryptionKmsKeyId")
    def reset_server_side_encryption_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionKmsKeyId", []))

    @jsii.member(jsii_name="resetSslMode")
    def reset_ssl_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslMode", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimestampColumnName")
    def reset_timestamp_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestampColumnName", []))

    @jsii.member(jsii_name="resetUseCsvNoSupValue")
    def reset_use_csv_no_sup_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCsvNoSupValue", []))

    @jsii.member(jsii_name="resetUseTaskStartTimeForFullLoadTimestamp")
    def reset_use_task_start_time_for_full_load_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseTaskStartTimeForFullLoadTimestamp", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointArn"))

    @builtins.property
    @jsii.member(jsii_name="engineDisplayName")
    def engine_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineDisplayName"))

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DmsS3EndpointTimeoutsOutputReference":
        return typing.cast("DmsS3EndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="addColumnNameInput")
    def add_column_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "addColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="addTrailingPaddingCharacterInput")
    def add_trailing_padding_character_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "addTrailingPaddingCharacterInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketFolderInput")
    def bucket_folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketFolderInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAclForObjectsInput")
    def canned_acl_for_objects_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclForObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsAndUpdatesInput")
    def cdc_inserts_and_updates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cdcInsertsAndUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsOnlyInput")
    def cdc_inserts_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cdcInsertsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcMaxBatchIntervalInput")
    def cdc_max_batch_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cdcMaxBatchIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcMinFileSizeInput")
    def cdc_min_file_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cdcMinFileSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cdcPathInput")
    def cdc_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcPathInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionTypeInput")
    def compression_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="csvDelimiterInput")
    def csv_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="csvNoSupValueInput")
    def csv_no_sup_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvNoSupValueInput"))

    @builtins.property
    @jsii.member(jsii_name="csvNullValueInput")
    def csv_null_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvNullValueInput"))

    @builtins.property
    @jsii.member(jsii_name="csvRowDelimiterInput")
    def csv_row_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "csvRowDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatInput")
    def data_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="dataPageSizeInput")
    def data_page_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataPageSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionDelimiterInput")
    def date_partition_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datePartitionDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionEnabledInput")
    def date_partition_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "datePartitionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionSequenceInput")
    def date_partition_sequence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datePartitionSequenceInput"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionTimezoneInput")
    def date_partition_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datePartitionTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="dictPageSizeLimitInput")
    def dict_page_size_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dictPageSizeLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="enableStatisticsInput")
    def enable_statistics_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableStatisticsInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingTypeInput")
    def encoding_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionModeInput")
    def encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointIdInput")
    def endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointTypeInput")
    def endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwnerInput")
    def expected_bucket_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedBucketOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="externalTableDefinitionInput")
    def external_table_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalTableDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreHeaderRowsInput")
    def ignore_header_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ignoreHeaderRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeOpForFullLoadInput")
    def include_op_for_full_load_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeOpForFullLoadInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFileSizeInput")
    def max_file_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFileSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetTimestampInMillisecondInput")
    def parquet_timestamp_in_millisecond_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "parquetTimestampInMillisecondInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetVersionInput")
    def parquet_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parquetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveTransactionsInput")
    def preserve_transactions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "preserveTransactionsInput"))

    @builtins.property
    @jsii.member(jsii_name="rfc4180Input")
    def rfc4180_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rfc4180Input"))

    @builtins.property
    @jsii.member(jsii_name="rowGroupLengthInput")
    def row_group_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowGroupLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyIdInput")
    def server_side_encryption_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideEncryptionKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslModeInput")
    def ssl_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslModeInput"))

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
    ) -> typing.Optional[typing.Union["DmsS3EndpointTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DmsS3EndpointTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampColumnNameInput")
    def timestamp_column_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timestampColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCsvNoSupValueInput")
    def use_csv_no_sup_value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useCsvNoSupValueInput"))

    @builtins.property
    @jsii.member(jsii_name="useTaskStartTimeForFullLoadTimestampInput")
    def use_task_start_time_for_full_load_timestamp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useTaskStartTimeForFullLoadTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="addColumnName")
    def add_column_name(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "addColumnName"))

    @add_column_name.setter
    def add_column_name(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__223bfc34faec9736d6a8c2eae75b4a938c738e090257be141e95ef97ee1086d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="addTrailingPaddingCharacter")
    def add_trailing_padding_character(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "addTrailingPaddingCharacter"))

    @add_trailing_padding_character.setter
    def add_trailing_padding_character(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a3cebe7f98d4f5c3b64f9cb4f9e79f25d8a7b26d8a70530e5b1abb65c95d399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addTrailingPaddingCharacter", value)

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @bucket_folder.setter
    def bucket_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1862d645c90f686cc0463dcf6b893f29d374a43f502e9a9f26eaf7934ce9f674)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketFolder", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b02d18bd3e8fc2e889570f9119c7440141541dd70170ca718e7a6c99619949b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAclForObjects"))

    @canned_acl_for_objects.setter
    def canned_acl_for_objects(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1cd311db2285a0957aaca4dda3bad948e35ef7b83f64e84676fa54f4849b94a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAclForObjects", value)

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cdcInsertsAndUpdates"))

    @cdc_inserts_and_updates.setter
    def cdc_inserts_and_updates(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec42a83b6d803b7aa2ce062844f6ea2c09e77d62f4977df76d8eedad76e76f06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcInsertsAndUpdates", value)

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsOnly")
    def cdc_inserts_only(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cdcInsertsOnly"))

    @cdc_inserts_only.setter
    def cdc_inserts_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eca876369f1d8d19716e525bf9017f709c5886866af930d51948d172a651bfa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcInsertsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMaxBatchInterval"))

    @cdc_max_batch_interval.setter
    def cdc_max_batch_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df5010645cc8442c3ac44e707ba8054ab7b8f9655d4db686c0f91b0ff54db8df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcMaxBatchInterval", value)

    @builtins.property
    @jsii.member(jsii_name="cdcMinFileSize")
    def cdc_min_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMinFileSize"))

    @cdc_min_file_size.setter
    def cdc_min_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2d3d4edd3da34211dde7a4ef4cc3eb057bfbdfed4f59c9cb9968047c3b17ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcMinFileSize", value)

    @builtins.property
    @jsii.member(jsii_name="cdcPath")
    def cdc_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcPath"))

    @cdc_path.setter
    def cdc_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48ba4748e962ed9d5944a4b94d09e597b718d303478118894f2f8b1027779a6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcPath", value)

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10e153dfa79ebb8eb3c744b7c42176e7252f1faeb231e1775462de86bbee60f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="compressionType")
    def compression_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionType"))

    @compression_type.setter
    def compression_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc2c7ba4774d6568a5da30ae241866712ab701d10d9db894a13a15349e111b35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionType", value)

    @builtins.property
    @jsii.member(jsii_name="csvDelimiter")
    def csv_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvDelimiter"))

    @csv_delimiter.setter
    def csv_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd8fea8380458418c92927ba8a3e4c5733833e8042a2862aab7026c0543a121f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="csvNoSupValue")
    def csv_no_sup_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNoSupValue"))

    @csv_no_sup_value.setter
    def csv_no_sup_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bb18c29cb52b1815cee66771222699cf8c565d82849df8f166ada1e6919b855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvNoSupValue", value)

    @builtins.property
    @jsii.member(jsii_name="csvNullValue")
    def csv_null_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNullValue"))

    @csv_null_value.setter
    def csv_null_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ee66e32bd1d481053e0e180e2d39356f5a5f33ca2384735d6de57adee03c8f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvNullValue", value)

    @builtins.property
    @jsii.member(jsii_name="csvRowDelimiter")
    def csv_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvRowDelimiter"))

    @csv_row_delimiter.setter
    def csv_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0f618326c6dc6414a203de16b337fdef6b3658733172651050e1b422898fe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @data_format.setter
    def data_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4a4805d3c093f709705c0a82ca4a39f43b2593d28f743b8168df1f393efcb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFormat", value)

    @builtins.property
    @jsii.member(jsii_name="dataPageSize")
    def data_page_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataPageSize"))

    @data_page_size.setter
    def data_page_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f9de80258d6c0126cbbbdd5f396fe0c2803d4dd1fe7501ee83351e72ff9433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPageSize", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionDelimiter"))

    @date_partition_delimiter.setter
    def date_partition_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa5a415dba2445f77643154d090f60a1d6954e5bb5d6003f666a2698e8526d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionEnabled")
    def date_partition_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "datePartitionEnabled"))

    @date_partition_enabled.setter
    def date_partition_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4df73931e7233b3a2eb960bc66dade27f60129e8c0509a77fef36b25601386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionSequence")
    def date_partition_sequence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionSequence"))

    @date_partition_sequence.setter
    def date_partition_sequence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3999f6e6cc5fa46fbc593e283643c603aa064bb1b538976d441a4639318f7eda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionSequence", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionTimezone")
    def date_partition_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionTimezone"))

    @date_partition_timezone.setter
    def date_partition_timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf6e1f3c41f37cb4d8a3457b724d708075da630559f0006af7d6547714e6dc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dictPageSizeLimit"))

    @dict_page_size_limit.setter
    def dict_page_size_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84eb97b90426517c0c0a55a116bdf5f65e9f796e52d90b3df74a22e59c8be04d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dictPageSizeLimit", value)

    @builtins.property
    @jsii.member(jsii_name="enableStatistics")
    def enable_statistics(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableStatistics"))

    @enable_statistics.setter
    def enable_statistics(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a041b52d6a1c36213a0fb80dade5112caec6b5bf5174ea8a37e3a9981a16a055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStatistics", value)

    @builtins.property
    @jsii.member(jsii_name="encodingType")
    def encoding_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encodingType"))

    @encoding_type.setter
    def encoding_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5f397ecc9b52997e58ec55c6b320baf514bd3d844bd3a59adba189f98bb92f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encodingType", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c095d781b2210679235640e26fdb21ba48511b971a3bec68f80278a14c1a7f2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="endpointId")
    def endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointId"))

    @endpoint_id.setter
    def endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01f4fcdf36fccba8297d97b8bee0114e05667dcf523e54c3620707e0947c7db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointId", value)

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f93c8d1129b49dd71f8b52ff8bf2dec5f504f9a550e0d44623d6bf070ecfec0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwner")
    def expected_bucket_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expectedBucketOwner"))

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534410624eaeb48cc6a627dabe5f8227158a55de93599a74c3d62e506d92afad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedBucketOwner", value)

    @builtins.property
    @jsii.member(jsii_name="externalTableDefinition")
    def external_table_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalTableDefinition"))

    @external_table_definition.setter
    def external_table_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61bbe2b8b2eef183755389a4a13d441e5b83bc6dad0b07f73f9c27b4f24c03b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalTableDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594491ba89cb7c9896bffcee581c8f35b59e6d2b681274d0c9b48ba9d94b4b33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreHeaderRows")
    def ignore_header_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreHeaderRows"))

    @ignore_header_rows.setter
    def ignore_header_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__539b27c985ac7c9defa698d0860f9bf117334e93efb6fefcad5d622208832818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreHeaderRows", value)

    @builtins.property
    @jsii.member(jsii_name="includeOpForFullLoad")
    def include_op_for_full_load(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeOpForFullLoad"))

    @include_op_for_full_load.setter
    def include_op_for_full_load(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e030899118b442e6cd798869b26d7013e55f2a92b332883e655471aec6216d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeOpForFullLoad", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d6e15589ac7efd82d2ba684b78ec0c98493aad94660e476303976144b9b3dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="maxFileSize")
    def max_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFileSize"))

    @max_file_size.setter
    def max_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b76306355a5608dc7309af0be479fa696a43d6f7c319835632652705fca4c238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFileSize", value)

    @builtins.property
    @jsii.member(jsii_name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "parquetTimestampInMillisecond"))

    @parquet_timestamp_in_millisecond.setter
    def parquet_timestamp_in_millisecond(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26e8b02d3c767771419f813b1905f46820863bec8b50a5e8753c115d77a236f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parquetTimestampInMillisecond", value)

    @builtins.property
    @jsii.member(jsii_name="parquetVersion")
    def parquet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parquetVersion"))

    @parquet_version.setter
    def parquet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8df1e8b92ed077e7bacbff4cb0fc88fdc5365a8e8017a098acadcc2bdc8fecf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parquetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="preserveTransactions")
    def preserve_transactions(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "preserveTransactions"))

    @preserve_transactions.setter
    def preserve_transactions(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__263984e5bcfe97f48086a56eedc317ea0e47f31d56e26b6e2cc90fd8311b096f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveTransactions", value)

    @builtins.property
    @jsii.member(jsii_name="rfc4180")
    def rfc4180(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rfc4180"))

    @rfc4180.setter
    def rfc4180(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ec7031975730bf38050d5c7ed7ac0a222a00c37468631fb680a2f6f5628fa27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rfc4180", value)

    @builtins.property
    @jsii.member(jsii_name="rowGroupLength")
    def row_group_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowGroupLength"))

    @row_group_length.setter
    def row_group_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ce40a8e58aa241409200df68c2265f104687eb15ca302fd96db9c29cea07e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowGroupLength", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @server_side_encryption_kms_key_id.setter
    def server_side_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da42ddf4e0c09c27b4f75e5bb3b2458a6a836383dca578e4643a538961695408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73235174d3df4f0191f995297984de07131b19b4edb6ccc42501a25285b3a3d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb8cedf2615d0816883b7ceabde88f573d4258e7826b023d81a368e4532698e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c552065b19e587595c382a9336d681325ca409d16add5dfd068519cbc235299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace82955e40deb149c49397bc79788873c56564ba4459b80dd43ee5008bd32e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="timestampColumnName")
    def timestamp_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timestampColumnName"))

    @timestamp_column_name.setter
    def timestamp_column_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e20515a8c0c9ded570a71a87785bf43a4001f3dc192505b7317c6e7a243598ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timestampColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="useCsvNoSupValue")
    def use_csv_no_sup_value(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useCsvNoSupValue"))

    @use_csv_no_sup_value.setter
    def use_csv_no_sup_value(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7b44ba70dac8bf03507cc393d3725ca80ee45ad48682053384b639e9398012a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCsvNoSupValue", value)

    @builtins.property
    @jsii.member(jsii_name="useTaskStartTimeForFullLoadTimestamp")
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useTaskStartTimeForFullLoadTimestamp"))

    @use_task_start_time_for_full_load_timestamp.setter
    def use_task_start_time_for_full_load_timestamp(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49be1b6d4a5224d9be853fa2b5a5686be8c139c28549478070bb056230a897bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useTaskStartTimeForFullLoadTimestamp", value)


@jsii.data_type(
    jsii_type="aws.dmsS3Endpoint.DmsS3EndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket_name": "bucketName",
        "endpoint_id": "endpointId",
        "endpoint_type": "endpointType",
        "service_access_role_arn": "serviceAccessRoleArn",
        "add_column_name": "addColumnName",
        "add_trailing_padding_character": "addTrailingPaddingCharacter",
        "bucket_folder": "bucketFolder",
        "canned_acl_for_objects": "cannedAclForObjects",
        "cdc_inserts_and_updates": "cdcInsertsAndUpdates",
        "cdc_inserts_only": "cdcInsertsOnly",
        "cdc_max_batch_interval": "cdcMaxBatchInterval",
        "cdc_min_file_size": "cdcMinFileSize",
        "cdc_path": "cdcPath",
        "certificate_arn": "certificateArn",
        "compression_type": "compressionType",
        "csv_delimiter": "csvDelimiter",
        "csv_no_sup_value": "csvNoSupValue",
        "csv_null_value": "csvNullValue",
        "csv_row_delimiter": "csvRowDelimiter",
        "data_format": "dataFormat",
        "data_page_size": "dataPageSize",
        "date_partition_delimiter": "datePartitionDelimiter",
        "date_partition_enabled": "datePartitionEnabled",
        "date_partition_sequence": "datePartitionSequence",
        "date_partition_timezone": "datePartitionTimezone",
        "dict_page_size_limit": "dictPageSizeLimit",
        "enable_statistics": "enableStatistics",
        "encoding_type": "encodingType",
        "encryption_mode": "encryptionMode",
        "expected_bucket_owner": "expectedBucketOwner",
        "external_table_definition": "externalTableDefinition",
        "id": "id",
        "ignore_header_rows": "ignoreHeaderRows",
        "include_op_for_full_load": "includeOpForFullLoad",
        "kms_key_arn": "kmsKeyArn",
        "max_file_size": "maxFileSize",
        "parquet_timestamp_in_millisecond": "parquetTimestampInMillisecond",
        "parquet_version": "parquetVersion",
        "preserve_transactions": "preserveTransactions",
        "rfc4180": "rfc4180",
        "row_group_length": "rowGroupLength",
        "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
        "ssl_mode": "sslMode",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "timestamp_column_name": "timestampColumnName",
        "use_csv_no_sup_value": "useCsvNoSupValue",
        "use_task_start_time_for_full_load_timestamp": "useTaskStartTimeForFullLoadTimestamp",
    },
)
class DmsS3EndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket_name: builtins.str,
        endpoint_id: builtins.str,
        endpoint_type: builtins.str,
        service_access_role_arn: builtins.str,
        add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        add_trailing_padding_character: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bucket_folder: typing.Optional[builtins.str] = None,
        canned_acl_for_objects: typing.Optional[builtins.str] = None,
        cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
        cdc_min_file_size: typing.Optional[jsii.Number] = None,
        cdc_path: typing.Optional[builtins.str] = None,
        certificate_arn: typing.Optional[builtins.str] = None,
        compression_type: typing.Optional[builtins.str] = None,
        csv_delimiter: typing.Optional[builtins.str] = None,
        csv_no_sup_value: typing.Optional[builtins.str] = None,
        csv_null_value: typing.Optional[builtins.str] = None,
        csv_row_delimiter: typing.Optional[builtins.str] = None,
        data_format: typing.Optional[builtins.str] = None,
        data_page_size: typing.Optional[jsii.Number] = None,
        date_partition_delimiter: typing.Optional[builtins.str] = None,
        date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        date_partition_sequence: typing.Optional[builtins.str] = None,
        date_partition_timezone: typing.Optional[builtins.str] = None,
        dict_page_size_limit: typing.Optional[jsii.Number] = None,
        enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        external_table_definition: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_header_rows: typing.Optional[jsii.Number] = None,
        include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parquet_version: typing.Optional[builtins.str] = None,
        preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        row_group_length: typing.Optional[jsii.Number] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsS3EndpointTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timestamp_column_name: typing.Optional[builtins.str] = None,
        use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#bucket_name DmsS3Endpoint#bucket_name}.
        :param endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#endpoint_id DmsS3Endpoint#endpoint_id}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#endpoint_type DmsS3Endpoint#endpoint_type}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#service_access_role_arn DmsS3Endpoint#service_access_role_arn}.
        :param add_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#add_column_name DmsS3Endpoint#add_column_name}.
        :param add_trailing_padding_character: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#add_trailing_padding_character DmsS3Endpoint#add_trailing_padding_character}.
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#bucket_folder DmsS3Endpoint#bucket_folder}.
        :param canned_acl_for_objects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#canned_acl_for_objects DmsS3Endpoint#canned_acl_for_objects}.
        :param cdc_inserts_and_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_inserts_and_updates DmsS3Endpoint#cdc_inserts_and_updates}.
        :param cdc_inserts_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_inserts_only DmsS3Endpoint#cdc_inserts_only}.
        :param cdc_max_batch_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_max_batch_interval DmsS3Endpoint#cdc_max_batch_interval}.
        :param cdc_min_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_min_file_size DmsS3Endpoint#cdc_min_file_size}.
        :param cdc_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_path DmsS3Endpoint#cdc_path}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#certificate_arn DmsS3Endpoint#certificate_arn}.
        :param compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#compression_type DmsS3Endpoint#compression_type}.
        :param csv_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_delimiter DmsS3Endpoint#csv_delimiter}.
        :param csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_no_sup_value DmsS3Endpoint#csv_no_sup_value}.
        :param csv_null_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_null_value DmsS3Endpoint#csv_null_value}.
        :param csv_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_row_delimiter DmsS3Endpoint#csv_row_delimiter}.
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#data_format DmsS3Endpoint#data_format}.
        :param data_page_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#data_page_size DmsS3Endpoint#data_page_size}.
        :param date_partition_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_delimiter DmsS3Endpoint#date_partition_delimiter}.
        :param date_partition_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_enabled DmsS3Endpoint#date_partition_enabled}.
        :param date_partition_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_sequence DmsS3Endpoint#date_partition_sequence}.
        :param date_partition_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_timezone DmsS3Endpoint#date_partition_timezone}.
        :param dict_page_size_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#dict_page_size_limit DmsS3Endpoint#dict_page_size_limit}.
        :param enable_statistics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#enable_statistics DmsS3Endpoint#enable_statistics}.
        :param encoding_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#encoding_type DmsS3Endpoint#encoding_type}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#encryption_mode DmsS3Endpoint#encryption_mode}.
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#expected_bucket_owner DmsS3Endpoint#expected_bucket_owner}.
        :param external_table_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#external_table_definition DmsS3Endpoint#external_table_definition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#id DmsS3Endpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_header_rows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#ignore_header_rows DmsS3Endpoint#ignore_header_rows}.
        :param include_op_for_full_load: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#include_op_for_full_load DmsS3Endpoint#include_op_for_full_load}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#kms_key_arn DmsS3Endpoint#kms_key_arn}.
        :param max_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#max_file_size DmsS3Endpoint#max_file_size}.
        :param parquet_timestamp_in_millisecond: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#parquet_timestamp_in_millisecond DmsS3Endpoint#parquet_timestamp_in_millisecond}.
        :param parquet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#parquet_version DmsS3Endpoint#parquet_version}.
        :param preserve_transactions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#preserve_transactions DmsS3Endpoint#preserve_transactions}.
        :param rfc4180: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#rfc_4180 DmsS3Endpoint#rfc_4180}.
        :param row_group_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#row_group_length DmsS3Endpoint#row_group_length}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#server_side_encryption_kms_key_id DmsS3Endpoint#server_side_encryption_kms_key_id}.
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#ssl_mode DmsS3Endpoint#ssl_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#tags DmsS3Endpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#tags_all DmsS3Endpoint#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#timeouts DmsS3Endpoint#timeouts}
        :param timestamp_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#timestamp_column_name DmsS3Endpoint#timestamp_column_name}.
        :param use_csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#use_csv_no_sup_value DmsS3Endpoint#use_csv_no_sup_value}.
        :param use_task_start_time_for_full_load_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#use_task_start_time_for_full_load_timestamp DmsS3Endpoint#use_task_start_time_for_full_load_timestamp}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DmsS3EndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e36ce69983330d40250ae09c4bb802251f957a6c1e48ebeb120896e568ca912)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument add_column_name", value=add_column_name, expected_type=type_hints["add_column_name"])
            check_type(argname="argument add_trailing_padding_character", value=add_trailing_padding_character, expected_type=type_hints["add_trailing_padding_character"])
            check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
            check_type(argname="argument canned_acl_for_objects", value=canned_acl_for_objects, expected_type=type_hints["canned_acl_for_objects"])
            check_type(argname="argument cdc_inserts_and_updates", value=cdc_inserts_and_updates, expected_type=type_hints["cdc_inserts_and_updates"])
            check_type(argname="argument cdc_inserts_only", value=cdc_inserts_only, expected_type=type_hints["cdc_inserts_only"])
            check_type(argname="argument cdc_max_batch_interval", value=cdc_max_batch_interval, expected_type=type_hints["cdc_max_batch_interval"])
            check_type(argname="argument cdc_min_file_size", value=cdc_min_file_size, expected_type=type_hints["cdc_min_file_size"])
            check_type(argname="argument cdc_path", value=cdc_path, expected_type=type_hints["cdc_path"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument compression_type", value=compression_type, expected_type=type_hints["compression_type"])
            check_type(argname="argument csv_delimiter", value=csv_delimiter, expected_type=type_hints["csv_delimiter"])
            check_type(argname="argument csv_no_sup_value", value=csv_no_sup_value, expected_type=type_hints["csv_no_sup_value"])
            check_type(argname="argument csv_null_value", value=csv_null_value, expected_type=type_hints["csv_null_value"])
            check_type(argname="argument csv_row_delimiter", value=csv_row_delimiter, expected_type=type_hints["csv_row_delimiter"])
            check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
            check_type(argname="argument data_page_size", value=data_page_size, expected_type=type_hints["data_page_size"])
            check_type(argname="argument date_partition_delimiter", value=date_partition_delimiter, expected_type=type_hints["date_partition_delimiter"])
            check_type(argname="argument date_partition_enabled", value=date_partition_enabled, expected_type=type_hints["date_partition_enabled"])
            check_type(argname="argument date_partition_sequence", value=date_partition_sequence, expected_type=type_hints["date_partition_sequence"])
            check_type(argname="argument date_partition_timezone", value=date_partition_timezone, expected_type=type_hints["date_partition_timezone"])
            check_type(argname="argument dict_page_size_limit", value=dict_page_size_limit, expected_type=type_hints["dict_page_size_limit"])
            check_type(argname="argument enable_statistics", value=enable_statistics, expected_type=type_hints["enable_statistics"])
            check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
            check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
            check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
            check_type(argname="argument external_table_definition", value=external_table_definition, expected_type=type_hints["external_table_definition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_header_rows", value=ignore_header_rows, expected_type=type_hints["ignore_header_rows"])
            check_type(argname="argument include_op_for_full_load", value=include_op_for_full_load, expected_type=type_hints["include_op_for_full_load"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
            check_type(argname="argument parquet_timestamp_in_millisecond", value=parquet_timestamp_in_millisecond, expected_type=type_hints["parquet_timestamp_in_millisecond"])
            check_type(argname="argument parquet_version", value=parquet_version, expected_type=type_hints["parquet_version"])
            check_type(argname="argument preserve_transactions", value=preserve_transactions, expected_type=type_hints["preserve_transactions"])
            check_type(argname="argument rfc4180", value=rfc4180, expected_type=type_hints["rfc4180"])
            check_type(argname="argument row_group_length", value=row_group_length, expected_type=type_hints["row_group_length"])
            check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timestamp_column_name", value=timestamp_column_name, expected_type=type_hints["timestamp_column_name"])
            check_type(argname="argument use_csv_no_sup_value", value=use_csv_no_sup_value, expected_type=type_hints["use_csv_no_sup_value"])
            check_type(argname="argument use_task_start_time_for_full_load_timestamp", value=use_task_start_time_for_full_load_timestamp, expected_type=type_hints["use_task_start_time_for_full_load_timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "endpoint_id": endpoint_id,
            "endpoint_type": endpoint_type,
            "service_access_role_arn": service_access_role_arn,
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
        if add_column_name is not None:
            self._values["add_column_name"] = add_column_name
        if add_trailing_padding_character is not None:
            self._values["add_trailing_padding_character"] = add_trailing_padding_character
        if bucket_folder is not None:
            self._values["bucket_folder"] = bucket_folder
        if canned_acl_for_objects is not None:
            self._values["canned_acl_for_objects"] = canned_acl_for_objects
        if cdc_inserts_and_updates is not None:
            self._values["cdc_inserts_and_updates"] = cdc_inserts_and_updates
        if cdc_inserts_only is not None:
            self._values["cdc_inserts_only"] = cdc_inserts_only
        if cdc_max_batch_interval is not None:
            self._values["cdc_max_batch_interval"] = cdc_max_batch_interval
        if cdc_min_file_size is not None:
            self._values["cdc_min_file_size"] = cdc_min_file_size
        if cdc_path is not None:
            self._values["cdc_path"] = cdc_path
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if compression_type is not None:
            self._values["compression_type"] = compression_type
        if csv_delimiter is not None:
            self._values["csv_delimiter"] = csv_delimiter
        if csv_no_sup_value is not None:
            self._values["csv_no_sup_value"] = csv_no_sup_value
        if csv_null_value is not None:
            self._values["csv_null_value"] = csv_null_value
        if csv_row_delimiter is not None:
            self._values["csv_row_delimiter"] = csv_row_delimiter
        if data_format is not None:
            self._values["data_format"] = data_format
        if data_page_size is not None:
            self._values["data_page_size"] = data_page_size
        if date_partition_delimiter is not None:
            self._values["date_partition_delimiter"] = date_partition_delimiter
        if date_partition_enabled is not None:
            self._values["date_partition_enabled"] = date_partition_enabled
        if date_partition_sequence is not None:
            self._values["date_partition_sequence"] = date_partition_sequence
        if date_partition_timezone is not None:
            self._values["date_partition_timezone"] = date_partition_timezone
        if dict_page_size_limit is not None:
            self._values["dict_page_size_limit"] = dict_page_size_limit
        if enable_statistics is not None:
            self._values["enable_statistics"] = enable_statistics
        if encoding_type is not None:
            self._values["encoding_type"] = encoding_type
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if expected_bucket_owner is not None:
            self._values["expected_bucket_owner"] = expected_bucket_owner
        if external_table_definition is not None:
            self._values["external_table_definition"] = external_table_definition
        if id is not None:
            self._values["id"] = id
        if ignore_header_rows is not None:
            self._values["ignore_header_rows"] = ignore_header_rows
        if include_op_for_full_load is not None:
            self._values["include_op_for_full_load"] = include_op_for_full_load
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if max_file_size is not None:
            self._values["max_file_size"] = max_file_size
        if parquet_timestamp_in_millisecond is not None:
            self._values["parquet_timestamp_in_millisecond"] = parquet_timestamp_in_millisecond
        if parquet_version is not None:
            self._values["parquet_version"] = parquet_version
        if preserve_transactions is not None:
            self._values["preserve_transactions"] = preserve_transactions
        if rfc4180 is not None:
            self._values["rfc4180"] = rfc4180
        if row_group_length is not None:
            self._values["row_group_length"] = row_group_length
        if server_side_encryption_kms_key_id is not None:
            self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timestamp_column_name is not None:
            self._values["timestamp_column_name"] = timestamp_column_name
        if use_csv_no_sup_value is not None:
            self._values["use_csv_no_sup_value"] = use_csv_no_sup_value
        if use_task_start_time_for_full_load_timestamp is not None:
            self._values["use_task_start_time_for_full_load_timestamp"] = use_task_start_time_for_full_load_timestamp

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
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#bucket_name DmsS3Endpoint#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#endpoint_id DmsS3Endpoint#endpoint_id}.'''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#endpoint_type DmsS3Endpoint#endpoint_type}.'''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#service_access_role_arn DmsS3Endpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        assert result is not None, "Required property 'service_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_column_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#add_column_name DmsS3Endpoint#add_column_name}.'''
        result = self._values.get("add_column_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def add_trailing_padding_character(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#add_trailing_padding_character DmsS3Endpoint#add_trailing_padding_character}.'''
        result = self._values.get("add_trailing_padding_character")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def bucket_folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#bucket_folder DmsS3Endpoint#bucket_folder}.'''
        result = self._values.get("bucket_folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def canned_acl_for_objects(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#canned_acl_for_objects DmsS3Endpoint#canned_acl_for_objects}.'''
        result = self._values.get("canned_acl_for_objects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_inserts_and_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_inserts_and_updates DmsS3Endpoint#cdc_inserts_and_updates}.'''
        result = self._values.get("cdc_inserts_and_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cdc_inserts_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_inserts_only DmsS3Endpoint#cdc_inserts_only}.'''
        result = self._values.get("cdc_inserts_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cdc_max_batch_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_max_batch_interval DmsS3Endpoint#cdc_max_batch_interval}.'''
        result = self._values.get("cdc_max_batch_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_min_file_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_min_file_size DmsS3Endpoint#cdc_min_file_size}.'''
        result = self._values.get("cdc_min_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#cdc_path DmsS3Endpoint#cdc_path}.'''
        result = self._values.get("cdc_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#certificate_arn DmsS3Endpoint#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compression_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#compression_type DmsS3Endpoint#compression_type}.'''
        result = self._values.get("compression_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_delimiter DmsS3Endpoint#csv_delimiter}.'''
        result = self._values.get("csv_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_no_sup_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_no_sup_value DmsS3Endpoint#csv_no_sup_value}.'''
        result = self._values.get("csv_no_sup_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_null_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_null_value DmsS3Endpoint#csv_null_value}.'''
        result = self._values.get("csv_null_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_row_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#csv_row_delimiter DmsS3Endpoint#csv_row_delimiter}.'''
        result = self._values.get("csv_row_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#data_format DmsS3Endpoint#data_format}.'''
        result = self._values.get("data_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_page_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#data_page_size DmsS3Endpoint#data_page_size}.'''
        result = self._values.get("data_page_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def date_partition_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_delimiter DmsS3Endpoint#date_partition_delimiter}.'''
        result = self._values.get("date_partition_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def date_partition_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_enabled DmsS3Endpoint#date_partition_enabled}.'''
        result = self._values.get("date_partition_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def date_partition_sequence(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_sequence DmsS3Endpoint#date_partition_sequence}.'''
        result = self._values.get("date_partition_sequence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def date_partition_timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#date_partition_timezone DmsS3Endpoint#date_partition_timezone}.'''
        result = self._values.get("date_partition_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dict_page_size_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#dict_page_size_limit DmsS3Endpoint#dict_page_size_limit}.'''
        result = self._values.get("dict_page_size_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_statistics(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#enable_statistics DmsS3Endpoint#enable_statistics}.'''
        result = self._values.get("enable_statistics")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encoding_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#encoding_type DmsS3Endpoint#encoding_type}.'''
        result = self._values.get("encoding_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#encryption_mode DmsS3Endpoint#encryption_mode}.'''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#expected_bucket_owner DmsS3Endpoint#expected_bucket_owner}.'''
        result = self._values.get("expected_bucket_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_table_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#external_table_definition DmsS3Endpoint#external_table_definition}.'''
        result = self._values.get("external_table_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#id DmsS3Endpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_header_rows(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#ignore_header_rows DmsS3Endpoint#ignore_header_rows}.'''
        result = self._values.get("ignore_header_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def include_op_for_full_load(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#include_op_for_full_load DmsS3Endpoint#include_op_for_full_load}.'''
        result = self._values.get("include_op_for_full_load")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#kms_key_arn DmsS3Endpoint#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_file_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#max_file_size DmsS3Endpoint#max_file_size}.'''
        result = self._values.get("max_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parquet_timestamp_in_millisecond(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#parquet_timestamp_in_millisecond DmsS3Endpoint#parquet_timestamp_in_millisecond}.'''
        result = self._values.get("parquet_timestamp_in_millisecond")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def parquet_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#parquet_version DmsS3Endpoint#parquet_version}.'''
        result = self._values.get("parquet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_transactions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#preserve_transactions DmsS3Endpoint#preserve_transactions}.'''
        result = self._values.get("preserve_transactions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def rfc4180(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#rfc_4180 DmsS3Endpoint#rfc_4180}.'''
        result = self._values.get("rfc4180")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def row_group_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#row_group_length DmsS3Endpoint#row_group_length}.'''
        result = self._values.get("row_group_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#server_side_encryption_kms_key_id DmsS3Endpoint#server_side_encryption_kms_key_id}.'''
        result = self._values.get("server_side_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#ssl_mode DmsS3Endpoint#ssl_mode}.'''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#tags DmsS3Endpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#tags_all DmsS3Endpoint#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DmsS3EndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#timeouts DmsS3Endpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DmsS3EndpointTimeouts"], result)

    @builtins.property
    def timestamp_column_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#timestamp_column_name DmsS3Endpoint#timestamp_column_name}.'''
        result = self._values.get("timestamp_column_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_csv_no_sup_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#use_csv_no_sup_value DmsS3Endpoint#use_csv_no_sup_value}.'''
        result = self._values.get("use_csv_no_sup_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#use_task_start_time_for_full_load_timestamp DmsS3Endpoint#use_task_start_time_for_full_load_timestamp}.'''
        result = self._values.get("use_task_start_time_for_full_load_timestamp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsS3EndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dmsS3Endpoint.DmsS3EndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class DmsS3EndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#create DmsS3Endpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#delete DmsS3Endpoint#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c779ad8d33743d5eb9268b9d621e3b3fc416d58b6b2865202bfd92a47f61df8)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#create DmsS3Endpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_s3_endpoint#delete DmsS3Endpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsS3EndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsS3EndpointTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsS3Endpoint.DmsS3EndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46060b072417010b035929e24ba096cf9a190f412cfa1658c5950a71be5edb02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee82e6e32a239d65e0087f6bd03564874ddba0eee246dacd3b06fc63f8f7ffb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c430273b46ff2a4cbc310dc5fd6cf3aaafb99a02371e10aa6c6447b2924a2233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DmsS3EndpointTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DmsS3EndpointTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DmsS3EndpointTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e920cd96489a0376cf7442942fbe567d2976c293916cf527f92a3313d3a8155b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DmsS3Endpoint",
    "DmsS3EndpointConfig",
    "DmsS3EndpointTimeouts",
    "DmsS3EndpointTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__8e0ad512742cdf6d04997d55f7ea2a98c2b216abd382b1182d64a744a132c6f4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket_name: builtins.str,
    endpoint_id: builtins.str,
    endpoint_type: builtins.str,
    service_access_role_arn: builtins.str,
    add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    add_trailing_padding_character: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    canned_acl_for_objects: typing.Optional[builtins.str] = None,
    cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
    cdc_min_file_size: typing.Optional[jsii.Number] = None,
    cdc_path: typing.Optional[builtins.str] = None,
    certificate_arn: typing.Optional[builtins.str] = None,
    compression_type: typing.Optional[builtins.str] = None,
    csv_delimiter: typing.Optional[builtins.str] = None,
    csv_no_sup_value: typing.Optional[builtins.str] = None,
    csv_null_value: typing.Optional[builtins.str] = None,
    csv_row_delimiter: typing.Optional[builtins.str] = None,
    data_format: typing.Optional[builtins.str] = None,
    data_page_size: typing.Optional[jsii.Number] = None,
    date_partition_delimiter: typing.Optional[builtins.str] = None,
    date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    date_partition_sequence: typing.Optional[builtins.str] = None,
    date_partition_timezone: typing.Optional[builtins.str] = None,
    dict_page_size_limit: typing.Optional[jsii.Number] = None,
    enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    external_table_definition: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ignore_header_rows: typing.Optional[jsii.Number] = None,
    include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parquet_version: typing.Optional[builtins.str] = None,
    preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    row_group_length: typing.Optional[jsii.Number] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DmsS3EndpointTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timestamp_column_name: typing.Optional[builtins.str] = None,
    use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__223bfc34faec9736d6a8c2eae75b4a938c738e090257be141e95ef97ee1086d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3cebe7f98d4f5c3b64f9cb4f9e79f25d8a7b26d8a70530e5b1abb65c95d399(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1862d645c90f686cc0463dcf6b893f29d374a43f502e9a9f26eaf7934ce9f674(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b02d18bd3e8fc2e889570f9119c7440141541dd70170ca718e7a6c99619949b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1cd311db2285a0957aaca4dda3bad948e35ef7b83f64e84676fa54f4849b94a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec42a83b6d803b7aa2ce062844f6ea2c09e77d62f4977df76d8eedad76e76f06(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eca876369f1d8d19716e525bf9017f709c5886866af930d51948d172a651bfa5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df5010645cc8442c3ac44e707ba8054ab7b8f9655d4db686c0f91b0ff54db8df(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2d3d4edd3da34211dde7a4ef4cc3eb057bfbdfed4f59c9cb9968047c3b17ee(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48ba4748e962ed9d5944a4b94d09e597b718d303478118894f2f8b1027779a6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e153dfa79ebb8eb3c744b7c42176e7252f1faeb231e1775462de86bbee60f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2c7ba4774d6568a5da30ae241866712ab701d10d9db894a13a15349e111b35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8fea8380458418c92927ba8a3e4c5733833e8042a2862aab7026c0543a121f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb18c29cb52b1815cee66771222699cf8c565d82849df8f166ada1e6919b855(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee66e32bd1d481053e0e180e2d39356f5a5f33ca2384735d6de57adee03c8f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0f618326c6dc6414a203de16b337fdef6b3658733172651050e1b422898fe5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4a4805d3c093f709705c0a82ca4a39f43b2593d28f743b8168df1f393efcb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f9de80258d6c0126cbbbdd5f396fe0c2803d4dd1fe7501ee83351e72ff9433(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa5a415dba2445f77643154d090f60a1d6954e5bb5d6003f666a2698e8526d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4df73931e7233b3a2eb960bc66dade27f60129e8c0509a77fef36b25601386(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3999f6e6cc5fa46fbc593e283643c603aa064bb1b538976d441a4639318f7eda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf6e1f3c41f37cb4d8a3457b724d708075da630559f0006af7d6547714e6dc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84eb97b90426517c0c0a55a116bdf5f65e9f796e52d90b3df74a22e59c8be04d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a041b52d6a1c36213a0fb80dade5112caec6b5bf5174ea8a37e3a9981a16a055(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5f397ecc9b52997e58ec55c6b320baf514bd3d844bd3a59adba189f98bb92f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c095d781b2210679235640e26fdb21ba48511b971a3bec68f80278a14c1a7f2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01f4fcdf36fccba8297d97b8bee0114e05667dcf523e54c3620707e0947c7db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f93c8d1129b49dd71f8b52ff8bf2dec5f504f9a550e0d44623d6bf070ecfec0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534410624eaeb48cc6a627dabe5f8227158a55de93599a74c3d62e506d92afad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61bbe2b8b2eef183755389a4a13d441e5b83bc6dad0b07f73f9c27b4f24c03b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594491ba89cb7c9896bffcee581c8f35b59e6d2b681274d0c9b48ba9d94b4b33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539b27c985ac7c9defa698d0860f9bf117334e93efb6fefcad5d622208832818(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e030899118b442e6cd798869b26d7013e55f2a92b332883e655471aec6216d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d6e15589ac7efd82d2ba684b78ec0c98493aad94660e476303976144b9b3dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76306355a5608dc7309af0be479fa696a43d6f7c319835632652705fca4c238(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26e8b02d3c767771419f813b1905f46820863bec8b50a5e8753c115d77a236f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df1e8b92ed077e7bacbff4cb0fc88fdc5365a8e8017a098acadcc2bdc8fecf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263984e5bcfe97f48086a56eedc317ea0e47f31d56e26b6e2cc90fd8311b096f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec7031975730bf38050d5c7ed7ac0a222a00c37468631fb680a2f6f5628fa27(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ce40a8e58aa241409200df68c2265f104687eb15ca302fd96db9c29cea07e3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da42ddf4e0c09c27b4f75e5bb3b2458a6a836383dca578e4643a538961695408(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73235174d3df4f0191f995297984de07131b19b4edb6ccc42501a25285b3a3d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb8cedf2615d0816883b7ceabde88f573d4258e7826b023d81a368e4532698e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c552065b19e587595c382a9336d681325ca409d16add5dfd068519cbc235299(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace82955e40deb149c49397bc79788873c56564ba4459b80dd43ee5008bd32e6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e20515a8c0c9ded570a71a87785bf43a4001f3dc192505b7317c6e7a243598ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7b44ba70dac8bf03507cc393d3725ca80ee45ad48682053384b639e9398012a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49be1b6d4a5224d9be853fa2b5a5686be8c139c28549478070bb056230a897bb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e36ce69983330d40250ae09c4bb802251f957a6c1e48ebeb120896e568ca912(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket_name: builtins.str,
    endpoint_id: builtins.str,
    endpoint_type: builtins.str,
    service_access_role_arn: builtins.str,
    add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    add_trailing_padding_character: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    canned_acl_for_objects: typing.Optional[builtins.str] = None,
    cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
    cdc_min_file_size: typing.Optional[jsii.Number] = None,
    cdc_path: typing.Optional[builtins.str] = None,
    certificate_arn: typing.Optional[builtins.str] = None,
    compression_type: typing.Optional[builtins.str] = None,
    csv_delimiter: typing.Optional[builtins.str] = None,
    csv_no_sup_value: typing.Optional[builtins.str] = None,
    csv_null_value: typing.Optional[builtins.str] = None,
    csv_row_delimiter: typing.Optional[builtins.str] = None,
    data_format: typing.Optional[builtins.str] = None,
    data_page_size: typing.Optional[jsii.Number] = None,
    date_partition_delimiter: typing.Optional[builtins.str] = None,
    date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    date_partition_sequence: typing.Optional[builtins.str] = None,
    date_partition_timezone: typing.Optional[builtins.str] = None,
    dict_page_size_limit: typing.Optional[jsii.Number] = None,
    enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    external_table_definition: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ignore_header_rows: typing.Optional[jsii.Number] = None,
    include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parquet_version: typing.Optional[builtins.str] = None,
    preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    row_group_length: typing.Optional[jsii.Number] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DmsS3EndpointTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timestamp_column_name: typing.Optional[builtins.str] = None,
    use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c779ad8d33743d5eb9268b9d621e3b3fc416d58b6b2865202bfd92a47f61df8(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46060b072417010b035929e24ba096cf9a190f412cfa1658c5950a71be5edb02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee82e6e32a239d65e0087f6bd03564874ddba0eee246dacd3b06fc63f8f7ffb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c430273b46ff2a4cbc310dc5fd6cf3aaafb99a02371e10aa6c6447b2924a2233(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e920cd96489a0376cf7442942fbe567d2976c293916cf527f92a3313d3a8155b(
    value: typing.Optional[typing.Union[DmsS3EndpointTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
