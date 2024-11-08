'''
# `aws_dms_endpoint`

Refer to the Terraform Registory for docs: [`aws_dms_endpoint`](https://www.terraform.io/docs/providers/aws/r/dms_endpoint).
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


class DmsEndpoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint aws_dms_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        endpoint_id: builtins.str,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        elasticsearch_settings: typing.Optional[typing.Union["DmsEndpointElasticsearchSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kafka_settings: typing.Optional[typing.Union["DmsEndpointKafkaSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_settings: typing.Optional[typing.Union["DmsEndpointKinesisSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        mongodb_settings: typing.Optional[typing.Union["DmsEndpointMongodbSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        redis_settings: typing.Optional[typing.Union["DmsEndpointRedisSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift_settings: typing.Optional[typing.Union["DmsEndpointRedshiftSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_settings: typing.Optional[typing.Union["DmsEndpointS3Settings", typing.Dict[builtins.str, typing.Any]]] = None,
        secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        server_name: typing.Optional[builtins.str] = None,
        service_access_role: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsEndpointTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint aws_dms_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_id DmsEndpoint#endpoint_id}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_type DmsEndpoint#endpoint_type}.
        :param engine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#engine_name DmsEndpoint#engine_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#certificate_arn DmsEndpoint#certificate_arn}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#database_name DmsEndpoint#database_name}.
        :param elasticsearch_settings: elasticsearch_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#elasticsearch_settings DmsEndpoint#elasticsearch_settings}
        :param extra_connection_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extra_connection_attributes DmsEndpoint#extra_connection_attributes}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#id DmsEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka_settings: kafka_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kafka_settings DmsEndpoint#kafka_settings}
        :param kinesis_settings: kinesis_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kinesis_settings DmsEndpoint#kinesis_settings}
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kms_key_arn DmsEndpoint#kms_key_arn}.
        :param mongodb_settings: mongodb_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#mongodb_settings DmsEndpoint#mongodb_settings}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#password DmsEndpoint#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.
        :param redis_settings: redis_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redis_settings DmsEndpoint#redis_settings}
        :param redshift_settings: redshift_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redshift_settings DmsEndpoint#redshift_settings}
        :param s3_settings: s3_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#s3_settings DmsEndpoint#s3_settings}
        :param secrets_manager_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_access_role_arn DmsEndpoint#secrets_manager_access_role_arn}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_arn DmsEndpoint#secrets_manager_arn}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.
        :param service_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role DmsEndpoint#service_access_role}.
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_mode DmsEndpoint#ssl_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags DmsEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags_all DmsEndpoint#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timeouts DmsEndpoint#timeouts}
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#username DmsEndpoint#username}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9020f5b2b715532017afb2eb9f9a9a03e0b6e2ccdd73b3fb466ce55676bd3d89)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DmsEndpointConfig(
            endpoint_id=endpoint_id,
            endpoint_type=endpoint_type,
            engine_name=engine_name,
            certificate_arn=certificate_arn,
            database_name=database_name,
            elasticsearch_settings=elasticsearch_settings,
            extra_connection_attributes=extra_connection_attributes,
            id=id,
            kafka_settings=kafka_settings,
            kinesis_settings=kinesis_settings,
            kms_key_arn=kms_key_arn,
            mongodb_settings=mongodb_settings,
            password=password,
            port=port,
            redis_settings=redis_settings,
            redshift_settings=redshift_settings,
            s3_settings=s3_settings,
            secrets_manager_access_role_arn=secrets_manager_access_role_arn,
            secrets_manager_arn=secrets_manager_arn,
            server_name=server_name,
            service_access_role=service_access_role,
            ssl_mode=ssl_mode,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            username=username,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putElasticsearchSettings")
    def put_elasticsearch_settings(
        self,
        *,
        endpoint_uri: builtins.str,
        service_access_role_arn: builtins.str,
        error_retry_duration: typing.Optional[jsii.Number] = None,
        full_load_error_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_uri DmsEndpoint#endpoint_uri}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param error_retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#error_retry_duration DmsEndpoint#error_retry_duration}.
        :param full_load_error_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#full_load_error_percentage DmsEndpoint#full_load_error_percentage}.
        '''
        value = DmsEndpointElasticsearchSettings(
            endpoint_uri=endpoint_uri,
            service_access_role_arn=service_access_role_arn,
            error_retry_duration=error_retry_duration,
            full_load_error_percentage=full_load_error_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearchSettings", [value]))

    @jsii.member(jsii_name="putKafkaSettings")
    def put_kafka_settings(
        self,
        *,
        broker: builtins.str,
        include_control_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        message_max_bytes: typing.Optional[jsii.Number] = None,
        no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sasl_password: typing.Optional[builtins.str] = None,
        sasl_username: typing.Optional[builtins.str] = None,
        security_protocol: typing.Optional[builtins.str] = None,
        ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_password: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#broker DmsEndpoint#broker}.
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param message_max_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_max_bytes DmsEndpoint#message_max_bytes}.
        :param no_hex_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#no_hex_prefix DmsEndpoint#no_hex_prefix}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param sasl_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_password DmsEndpoint#sasl_password}.
        :param sasl_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_username DmsEndpoint#sasl_username}.
        :param security_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#security_protocol DmsEndpoint#security_protocol}.
        :param ssl_ca_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.
        :param ssl_client_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_certificate_arn DmsEndpoint#ssl_client_certificate_arn}.
        :param ssl_client_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_arn DmsEndpoint#ssl_client_key_arn}.
        :param ssl_client_key_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_password DmsEndpoint#ssl_client_key_password}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#topic DmsEndpoint#topic}.
        '''
        value = DmsEndpointKafkaSettings(
            broker=broker,
            include_control_details=include_control_details,
            include_null_and_empty=include_null_and_empty,
            include_partition_value=include_partition_value,
            include_table_alter_operations=include_table_alter_operations,
            include_transaction_details=include_transaction_details,
            message_format=message_format,
            message_max_bytes=message_max_bytes,
            no_hex_prefix=no_hex_prefix,
            partition_include_schema_table=partition_include_schema_table,
            sasl_password=sasl_password,
            sasl_username=sasl_username,
            security_protocol=security_protocol,
            ssl_ca_certificate_arn=ssl_ca_certificate_arn,
            ssl_client_certificate_arn=ssl_client_certificate_arn,
            ssl_client_key_arn=ssl_client_key_arn,
            ssl_client_key_password=ssl_client_key_password,
            topic=topic,
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaSettings", [value]))

    @jsii.member(jsii_name="putKinesisSettings")
    def put_kinesis_settings(
        self,
        *,
        include_control_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        stream_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#stream_arn DmsEndpoint#stream_arn}.
        '''
        value = DmsEndpointKinesisSettings(
            include_control_details=include_control_details,
            include_null_and_empty=include_null_and_empty,
            include_partition_value=include_partition_value,
            include_table_alter_operations=include_table_alter_operations,
            include_transaction_details=include_transaction_details,
            message_format=message_format,
            partition_include_schema_table=partition_include_schema_table,
            service_access_role_arn=service_access_role_arn,
            stream_arn=stream_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisSettings", [value]))

    @jsii.member(jsii_name="putMongodbSettings")
    def put_mongodb_settings(
        self,
        *,
        auth_mechanism: typing.Optional[builtins.str] = None,
        auth_source: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        docs_to_investigate: typing.Optional[builtins.str] = None,
        extract_doc_id: typing.Optional[builtins.str] = None,
        nesting_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_mechanism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_mechanism DmsEndpoint#auth_mechanism}.
        :param auth_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_source DmsEndpoint#auth_source}.
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.
        :param docs_to_investigate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#docs_to_investigate DmsEndpoint#docs_to_investigate}.
        :param extract_doc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extract_doc_id DmsEndpoint#extract_doc_id}.
        :param nesting_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#nesting_level DmsEndpoint#nesting_level}.
        '''
        value = DmsEndpointMongodbSettings(
            auth_mechanism=auth_mechanism,
            auth_source=auth_source,
            auth_type=auth_type,
            docs_to_investigate=docs_to_investigate,
            extract_doc_id=extract_doc_id,
            nesting_level=nesting_level,
        )

        return typing.cast(None, jsii.invoke(self, "putMongodbSettings", [value]))

    @jsii.member(jsii_name="putRedisSettings")
    def put_redis_settings(
        self,
        *,
        auth_type: builtins.str,
        port: jsii.Number,
        server_name: builtins.str,
        auth_password: typing.Optional[builtins.str] = None,
        auth_user_name: typing.Optional[builtins.str] = None,
        ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_security_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.
        :param auth_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_password DmsEndpoint#auth_password}.
        :param auth_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_user_name DmsEndpoint#auth_user_name}.
        :param ssl_ca_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.
        :param ssl_security_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_security_protocol DmsEndpoint#ssl_security_protocol}.
        '''
        value = DmsEndpointRedisSettings(
            auth_type=auth_type,
            port=port,
            server_name=server_name,
            auth_password=auth_password,
            auth_user_name=auth_user_name,
            ssl_ca_certificate_arn=ssl_ca_certificate_arn,
            ssl_security_protocol=ssl_security_protocol,
        )

        return typing.cast(None, jsii.invoke(self, "putRedisSettings", [value]))

    @jsii.member(jsii_name="putRedshiftSettings")
    def put_redshift_settings(
        self,
        *,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        '''
        value = DmsEndpointRedshiftSettings(
            bucket_folder=bucket_folder,
            bucket_name=bucket_name,
            encryption_mode=encryption_mode,
            server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
            service_access_role_arn=service_access_role_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshiftSettings", [value]))

    @jsii.member(jsii_name="putS3Settings")
    def put_s3_settings(
        self,
        *,
        add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        canned_acl_for_objects: typing.Optional[builtins.str] = None,
        cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
        cdc_min_file_size: typing.Optional[jsii.Number] = None,
        cdc_path: typing.Optional[builtins.str] = None,
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
        dict_page_size_limit: typing.Optional[jsii.Number] = None,
        enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        external_table_definition: typing.Optional[builtins.str] = None,
        ignore_header_rows: typing.Optional[jsii.Number] = None,
        ignore_headers_row: typing.Optional[jsii.Number] = None,
        include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parquet_version: typing.Optional[builtins.str] = None,
        preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        row_group_length: typing.Optional[jsii.Number] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        timestamp_column_name: typing.Optional[builtins.str] = None,
        use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param add_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#add_column_name DmsEndpoint#add_column_name}.
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param canned_acl_for_objects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#canned_acl_for_objects DmsEndpoint#canned_acl_for_objects}.
        :param cdc_inserts_and_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_and_updates DmsEndpoint#cdc_inserts_and_updates}.
        :param cdc_inserts_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_only DmsEndpoint#cdc_inserts_only}.
        :param cdc_max_batch_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_max_batch_interval DmsEndpoint#cdc_max_batch_interval}.
        :param cdc_min_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_min_file_size DmsEndpoint#cdc_min_file_size}.
        :param cdc_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_path DmsEndpoint#cdc_path}.
        :param compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#compression_type DmsEndpoint#compression_type}.
        :param csv_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_delimiter DmsEndpoint#csv_delimiter}.
        :param csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_no_sup_value DmsEndpoint#csv_no_sup_value}.
        :param csv_null_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_null_value DmsEndpoint#csv_null_value}.
        :param csv_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_row_delimiter DmsEndpoint#csv_row_delimiter}.
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_format DmsEndpoint#data_format}.
        :param data_page_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_page_size DmsEndpoint#data_page_size}.
        :param date_partition_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_delimiter DmsEndpoint#date_partition_delimiter}.
        :param date_partition_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_enabled DmsEndpoint#date_partition_enabled}.
        :param date_partition_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_sequence DmsEndpoint#date_partition_sequence}.
        :param dict_page_size_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#dict_page_size_limit DmsEndpoint#dict_page_size_limit}.
        :param enable_statistics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#enable_statistics DmsEndpoint#enable_statistics}.
        :param encoding_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encoding_type DmsEndpoint#encoding_type}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param external_table_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#external_table_definition DmsEndpoint#external_table_definition}.
        :param ignore_header_rows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_header_rows DmsEndpoint#ignore_header_rows}.
        :param ignore_headers_row: This setting has no effect, is deprecated, and will be removed in a future version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_headers_row DmsEndpoint#ignore_headers_row}
        :param include_op_for_full_load: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_op_for_full_load DmsEndpoint#include_op_for_full_load}.
        :param max_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#max_file_size DmsEndpoint#max_file_size}.
        :param parquet_timestamp_in_millisecond: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_timestamp_in_millisecond DmsEndpoint#parquet_timestamp_in_millisecond}.
        :param parquet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_version DmsEndpoint#parquet_version}.
        :param preserve_transactions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#preserve_transactions DmsEndpoint#preserve_transactions}.
        :param rfc4180: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#rfc_4180 DmsEndpoint#rfc_4180}.
        :param row_group_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#row_group_length DmsEndpoint#row_group_length}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param timestamp_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timestamp_column_name DmsEndpoint#timestamp_column_name}.
        :param use_csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_csv_no_sup_value DmsEndpoint#use_csv_no_sup_value}.
        :param use_task_start_time_for_full_load_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_task_start_time_for_full_load_timestamp DmsEndpoint#use_task_start_time_for_full_load_timestamp}.
        '''
        value = DmsEndpointS3Settings(
            add_column_name=add_column_name,
            bucket_folder=bucket_folder,
            bucket_name=bucket_name,
            canned_acl_for_objects=canned_acl_for_objects,
            cdc_inserts_and_updates=cdc_inserts_and_updates,
            cdc_inserts_only=cdc_inserts_only,
            cdc_max_batch_interval=cdc_max_batch_interval,
            cdc_min_file_size=cdc_min_file_size,
            cdc_path=cdc_path,
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
            dict_page_size_limit=dict_page_size_limit,
            enable_statistics=enable_statistics,
            encoding_type=encoding_type,
            encryption_mode=encryption_mode,
            external_table_definition=external_table_definition,
            ignore_header_rows=ignore_header_rows,
            ignore_headers_row=ignore_headers_row,
            include_op_for_full_load=include_op_for_full_load,
            max_file_size=max_file_size,
            parquet_timestamp_in_millisecond=parquet_timestamp_in_millisecond,
            parquet_version=parquet_version,
            preserve_transactions=preserve_transactions,
            rfc4180=rfc4180,
            row_group_length=row_group_length,
            server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
            service_access_role_arn=service_access_role_arn,
            timestamp_column_name=timestamp_column_name,
            use_csv_no_sup_value=use_csv_no_sup_value,
            use_task_start_time_for_full_load_timestamp=use_task_start_time_for_full_load_timestamp,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Settings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#create DmsEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#delete DmsEndpoint#delete}.
        '''
        value = DmsEndpointTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificateArn")
    def reset_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateArn", []))

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetElasticsearchSettings")
    def reset_elasticsearch_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchSettings", []))

    @jsii.member(jsii_name="resetExtraConnectionAttributes")
    def reset_extra_connection_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConnectionAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKafkaSettings")
    def reset_kafka_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKafkaSettings", []))

    @jsii.member(jsii_name="resetKinesisSettings")
    def reset_kinesis_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisSettings", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetMongodbSettings")
    def reset_mongodb_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodbSettings", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetRedisSettings")
    def reset_redis_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisSettings", []))

    @jsii.member(jsii_name="resetRedshiftSettings")
    def reset_redshift_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshiftSettings", []))

    @jsii.member(jsii_name="resetS3Settings")
    def reset_s3_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Settings", []))

    @jsii.member(jsii_name="resetSecretsManagerAccessRoleArn")
    def reset_secrets_manager_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerAccessRoleArn", []))

    @jsii.member(jsii_name="resetSecretsManagerArn")
    def reset_secrets_manager_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerArn", []))

    @jsii.member(jsii_name="resetServerName")
    def reset_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerName", []))

    @jsii.member(jsii_name="resetServiceAccessRole")
    def reset_service_access_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRole", []))

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

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> "DmsEndpointElasticsearchSettingsOutputReference":
        return typing.cast("DmsEndpointElasticsearchSettingsOutputReference", jsii.get(self, "elasticsearchSettings"))

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointArn"))

    @builtins.property
    @jsii.member(jsii_name="kafkaSettings")
    def kafka_settings(self) -> "DmsEndpointKafkaSettingsOutputReference":
        return typing.cast("DmsEndpointKafkaSettingsOutputReference", jsii.get(self, "kafkaSettings"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSettings")
    def kinesis_settings(self) -> "DmsEndpointKinesisSettingsOutputReference":
        return typing.cast("DmsEndpointKinesisSettingsOutputReference", jsii.get(self, "kinesisSettings"))

    @builtins.property
    @jsii.member(jsii_name="mongodbSettings")
    def mongodb_settings(self) -> "DmsEndpointMongodbSettingsOutputReference":
        return typing.cast("DmsEndpointMongodbSettingsOutputReference", jsii.get(self, "mongodbSettings"))

    @builtins.property
    @jsii.member(jsii_name="redisSettings")
    def redis_settings(self) -> "DmsEndpointRedisSettingsOutputReference":
        return typing.cast("DmsEndpointRedisSettingsOutputReference", jsii.get(self, "redisSettings"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSettings")
    def redshift_settings(self) -> "DmsEndpointRedshiftSettingsOutputReference":
        return typing.cast("DmsEndpointRedshiftSettingsOutputReference", jsii.get(self, "redshiftSettings"))

    @builtins.property
    @jsii.member(jsii_name="s3Settings")
    def s3_settings(self) -> "DmsEndpointS3SettingsOutputReference":
        return typing.cast("DmsEndpointS3SettingsOutputReference", jsii.get(self, "s3Settings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DmsEndpointTimeoutsOutputReference":
        return typing.cast("DmsEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettingsInput")
    def elasticsearch_settings_input(
        self,
    ) -> typing.Optional["DmsEndpointElasticsearchSettings"]:
        return typing.cast(typing.Optional["DmsEndpointElasticsearchSettings"], jsii.get(self, "elasticsearchSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointIdInput")
    def endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointTypeInput")
    def endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="engineNameInput")
    def engine_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineNameInput"))

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributesInput")
    def extra_connection_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraConnectionAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaSettingsInput")
    def kafka_settings_input(self) -> typing.Optional["DmsEndpointKafkaSettings"]:
        return typing.cast(typing.Optional["DmsEndpointKafkaSettings"], jsii.get(self, "kafkaSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSettingsInput")
    def kinesis_settings_input(self) -> typing.Optional["DmsEndpointKinesisSettings"]:
        return typing.cast(typing.Optional["DmsEndpointKinesisSettings"], jsii.get(self, "kinesisSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbSettingsInput")
    def mongodb_settings_input(self) -> typing.Optional["DmsEndpointMongodbSettings"]:
        return typing.cast(typing.Optional["DmsEndpointMongodbSettings"], jsii.get(self, "mongodbSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="redisSettingsInput")
    def redis_settings_input(self) -> typing.Optional["DmsEndpointRedisSettings"]:
        return typing.cast(typing.Optional["DmsEndpointRedisSettings"], jsii.get(self, "redisSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSettingsInput")
    def redshift_settings_input(self) -> typing.Optional["DmsEndpointRedshiftSettings"]:
        return typing.cast(typing.Optional["DmsEndpointRedshiftSettings"], jsii.get(self, "redshiftSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3SettingsInput")
    def s3_settings_input(self) -> typing.Optional["DmsEndpointS3Settings"]:
        return typing.cast(typing.Optional["DmsEndpointS3Settings"], jsii.get(self, "s3SettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerAccessRoleArnInput")
    def secrets_manager_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArnInput")
    def secrets_manager_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleInput")
    def service_access_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleInput"))

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
    ) -> typing.Optional[typing.Union["DmsEndpointTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DmsEndpointTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ab9d10796d8c84780b9609d9e2e79e579846f3b420869b7b74917ed3757c4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f1105d4acf2681438f01c6aaea591cfa0661c2828b0e5ec50dc3c18c85e2f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="endpointId")
    def endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointId"))

    @endpoint_id.setter
    def endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3acc89431bee22031596e0af9fb53c688c3bd846b01352e5e0db514b3e4aac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointId", value)

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a3109b9f7f561a1907fbfbcc3c654e53ee3d7ccc044dc8a0752a7ee5f17c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="engineName")
    def engine_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineName"))

    @engine_name.setter
    def engine_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e97a45287b20d7e3520484923249ab2564280d9cc5b6a875bd13463d9a8294d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineName", value)

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extraConnectionAttributes"))

    @extra_connection_attributes.setter
    def extra_connection_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c72e675ddcac8f72a59964dd4643c232cf54b86227cd1ff223b7fb5fcc078cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConnectionAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3894b9ce77ca22542e6df7f602448b2a758b6c256961986bc5f25edf42bad655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11902d7d4da539113fb941000f5d145e255c71d2d6ff2d0de1287777eb489286)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14905011025ee78d9802d79d660ce83c1a6a92f1714f11eb7b75cefecd6a7d88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e36e893488dbba48e700b44e4f01762e686e42335e98fe3a9312fdab412c64f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerAccessRoleArn"))

    @secrets_manager_access_role_arn.setter
    def secrets_manager_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89a3055baf1e6281c4e9c3c23cadf75650bb076bb9f6dd68c6b0487c7b9c4f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0844f6c8bcb8bf86cb1c179140275d548ae723df5e31bac5170c67e2baec9d2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerArn", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c505b6c299b903a23cd0438ac4e9d32d32c3b036e399a576664d9de324159b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRole")
    def service_access_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRole"))

    @service_access_role.setter
    def service_access_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9952c43668f9a3080316a4ce4206a3b2c8f1cb108b6c69b5d28d690caffb904a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRole", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d07a126353a15d177bc82bbb20db05378170e1802b159baeb26b0c680fb624e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__194ea8aeac0b23dd381129fca9ec3c2370fc99fdff6cef2243f54f67c62d1297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12976f18a4035e0306ee876893066bace5e11592ff9d78bd2c1162bb4d432a5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__100b2cbe2062e63d11faf836404cf3be9a6c95242f996e2ddfefde697aa0fedd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint_id": "endpointId",
        "endpoint_type": "endpointType",
        "engine_name": "engineName",
        "certificate_arn": "certificateArn",
        "database_name": "databaseName",
        "elasticsearch_settings": "elasticsearchSettings",
        "extra_connection_attributes": "extraConnectionAttributes",
        "id": "id",
        "kafka_settings": "kafkaSettings",
        "kinesis_settings": "kinesisSettings",
        "kms_key_arn": "kmsKeyArn",
        "mongodb_settings": "mongodbSettings",
        "password": "password",
        "port": "port",
        "redis_settings": "redisSettings",
        "redshift_settings": "redshiftSettings",
        "s3_settings": "s3Settings",
        "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
        "secrets_manager_arn": "secretsManagerArn",
        "server_name": "serverName",
        "service_access_role": "serviceAccessRole",
        "ssl_mode": "sslMode",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "username": "username",
    },
)
class DmsEndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint_id: builtins.str,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        elasticsearch_settings: typing.Optional[typing.Union["DmsEndpointElasticsearchSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kafka_settings: typing.Optional[typing.Union["DmsEndpointKafkaSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_settings: typing.Optional[typing.Union["DmsEndpointKinesisSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        mongodb_settings: typing.Optional[typing.Union["DmsEndpointMongodbSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        redis_settings: typing.Optional[typing.Union["DmsEndpointRedisSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        redshift_settings: typing.Optional[typing.Union["DmsEndpointRedshiftSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_settings: typing.Optional[typing.Union["DmsEndpointS3Settings", typing.Dict[builtins.str, typing.Any]]] = None,
        secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        server_name: typing.Optional[builtins.str] = None,
        service_access_role: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DmsEndpointTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_id DmsEndpoint#endpoint_id}.
        :param endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_type DmsEndpoint#endpoint_type}.
        :param engine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#engine_name DmsEndpoint#engine_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#certificate_arn DmsEndpoint#certificate_arn}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#database_name DmsEndpoint#database_name}.
        :param elasticsearch_settings: elasticsearch_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#elasticsearch_settings DmsEndpoint#elasticsearch_settings}
        :param extra_connection_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extra_connection_attributes DmsEndpoint#extra_connection_attributes}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#id DmsEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka_settings: kafka_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kafka_settings DmsEndpoint#kafka_settings}
        :param kinesis_settings: kinesis_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kinesis_settings DmsEndpoint#kinesis_settings}
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kms_key_arn DmsEndpoint#kms_key_arn}.
        :param mongodb_settings: mongodb_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#mongodb_settings DmsEndpoint#mongodb_settings}
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#password DmsEndpoint#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.
        :param redis_settings: redis_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redis_settings DmsEndpoint#redis_settings}
        :param redshift_settings: redshift_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redshift_settings DmsEndpoint#redshift_settings}
        :param s3_settings: s3_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#s3_settings DmsEndpoint#s3_settings}
        :param secrets_manager_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_access_role_arn DmsEndpoint#secrets_manager_access_role_arn}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_arn DmsEndpoint#secrets_manager_arn}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.
        :param service_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role DmsEndpoint#service_access_role}.
        :param ssl_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_mode DmsEndpoint#ssl_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags DmsEndpoint#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags_all DmsEndpoint#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timeouts DmsEndpoint#timeouts}
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#username DmsEndpoint#username}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(elasticsearch_settings, dict):
            elasticsearch_settings = DmsEndpointElasticsearchSettings(**elasticsearch_settings)
        if isinstance(kafka_settings, dict):
            kafka_settings = DmsEndpointKafkaSettings(**kafka_settings)
        if isinstance(kinesis_settings, dict):
            kinesis_settings = DmsEndpointKinesisSettings(**kinesis_settings)
        if isinstance(mongodb_settings, dict):
            mongodb_settings = DmsEndpointMongodbSettings(**mongodb_settings)
        if isinstance(redis_settings, dict):
            redis_settings = DmsEndpointRedisSettings(**redis_settings)
        if isinstance(redshift_settings, dict):
            redshift_settings = DmsEndpointRedshiftSettings(**redshift_settings)
        if isinstance(s3_settings, dict):
            s3_settings = DmsEndpointS3Settings(**s3_settings)
        if isinstance(timeouts, dict):
            timeouts = DmsEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32b717e212dfc67dcd7c8e9e1db55b361f64cca0c3f78247e879746c162f763)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument engine_name", value=engine_name, expected_type=type_hints["engine_name"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument elasticsearch_settings", value=elasticsearch_settings, expected_type=type_hints["elasticsearch_settings"])
            check_type(argname="argument extra_connection_attributes", value=extra_connection_attributes, expected_type=type_hints["extra_connection_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kafka_settings", value=kafka_settings, expected_type=type_hints["kafka_settings"])
            check_type(argname="argument kinesis_settings", value=kinesis_settings, expected_type=type_hints["kinesis_settings"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument mongodb_settings", value=mongodb_settings, expected_type=type_hints["mongodb_settings"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument redis_settings", value=redis_settings, expected_type=type_hints["redis_settings"])
            check_type(argname="argument redshift_settings", value=redshift_settings, expected_type=type_hints["redshift_settings"])
            check_type(argname="argument s3_settings", value=s3_settings, expected_type=type_hints["s3_settings"])
            check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
            check_type(argname="argument secrets_manager_arn", value=secrets_manager_arn, expected_type=type_hints["secrets_manager_arn"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument service_access_role", value=service_access_role, expected_type=type_hints["service_access_role"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_id": endpoint_id,
            "endpoint_type": endpoint_type,
            "engine_name": engine_name,
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
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if database_name is not None:
            self._values["database_name"] = database_name
        if elasticsearch_settings is not None:
            self._values["elasticsearch_settings"] = elasticsearch_settings
        if extra_connection_attributes is not None:
            self._values["extra_connection_attributes"] = extra_connection_attributes
        if id is not None:
            self._values["id"] = id
        if kafka_settings is not None:
            self._values["kafka_settings"] = kafka_settings
        if kinesis_settings is not None:
            self._values["kinesis_settings"] = kinesis_settings
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if mongodb_settings is not None:
            self._values["mongodb_settings"] = mongodb_settings
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if redis_settings is not None:
            self._values["redis_settings"] = redis_settings
        if redshift_settings is not None:
            self._values["redshift_settings"] = redshift_settings
        if s3_settings is not None:
            self._values["s3_settings"] = s3_settings
        if secrets_manager_access_role_arn is not None:
            self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
        if secrets_manager_arn is not None:
            self._values["secrets_manager_arn"] = secrets_manager_arn
        if server_name is not None:
            self._values["server_name"] = server_name
        if service_access_role is not None:
            self._values["service_access_role"] = service_access_role
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if username is not None:
            self._values["username"] = username

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
    def endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_id DmsEndpoint#endpoint_id}.'''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_type DmsEndpoint#endpoint_type}.'''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#engine_name DmsEndpoint#engine_name}.'''
        result = self._values.get("engine_name")
        assert result is not None, "Required property 'engine_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#certificate_arn DmsEndpoint#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#database_name DmsEndpoint#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch_settings(
        self,
    ) -> typing.Optional["DmsEndpointElasticsearchSettings"]:
        '''elasticsearch_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#elasticsearch_settings DmsEndpoint#elasticsearch_settings}
        '''
        result = self._values.get("elasticsearch_settings")
        return typing.cast(typing.Optional["DmsEndpointElasticsearchSettings"], result)

    @builtins.property
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extra_connection_attributes DmsEndpoint#extra_connection_attributes}.'''
        result = self._values.get("extra_connection_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#id DmsEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka_settings(self) -> typing.Optional["DmsEndpointKafkaSettings"]:
        '''kafka_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kafka_settings DmsEndpoint#kafka_settings}
        '''
        result = self._values.get("kafka_settings")
        return typing.cast(typing.Optional["DmsEndpointKafkaSettings"], result)

    @builtins.property
    def kinesis_settings(self) -> typing.Optional["DmsEndpointKinesisSettings"]:
        '''kinesis_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kinesis_settings DmsEndpoint#kinesis_settings}
        '''
        result = self._values.get("kinesis_settings")
        return typing.cast(typing.Optional["DmsEndpointKinesisSettings"], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#kms_key_arn DmsEndpoint#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mongodb_settings(self) -> typing.Optional["DmsEndpointMongodbSettings"]:
        '''mongodb_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#mongodb_settings DmsEndpoint#mongodb_settings}
        '''
        result = self._values.get("mongodb_settings")
        return typing.cast(typing.Optional["DmsEndpointMongodbSettings"], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#password DmsEndpoint#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redis_settings(self) -> typing.Optional["DmsEndpointRedisSettings"]:
        '''redis_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redis_settings DmsEndpoint#redis_settings}
        '''
        result = self._values.get("redis_settings")
        return typing.cast(typing.Optional["DmsEndpointRedisSettings"], result)

    @builtins.property
    def redshift_settings(self) -> typing.Optional["DmsEndpointRedshiftSettings"]:
        '''redshift_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#redshift_settings DmsEndpoint#redshift_settings}
        '''
        result = self._values.get("redshift_settings")
        return typing.cast(typing.Optional["DmsEndpointRedshiftSettings"], result)

    @builtins.property
    def s3_settings(self) -> typing.Optional["DmsEndpointS3Settings"]:
        '''s3_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#s3_settings DmsEndpoint#s3_settings}
        '''
        result = self._values.get("s3_settings")
        return typing.cast(typing.Optional["DmsEndpointS3Settings"], result)

    @builtins.property
    def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_access_role_arn DmsEndpoint#secrets_manager_access_role_arn}.'''
        result = self._values.get("secrets_manager_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_manager_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#secrets_manager_arn DmsEndpoint#secrets_manager_arn}.'''
        result = self._values.get("secrets_manager_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.'''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role DmsEndpoint#service_access_role}.'''
        result = self._values.get("service_access_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_mode DmsEndpoint#ssl_mode}.'''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags DmsEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#tags_all DmsEndpoint#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DmsEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timeouts DmsEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DmsEndpointTimeouts"], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#username DmsEndpoint#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointElasticsearchSettings",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_uri": "endpointUri",
        "service_access_role_arn": "serviceAccessRoleArn",
        "error_retry_duration": "errorRetryDuration",
        "full_load_error_percentage": "fullLoadErrorPercentage",
    },
)
class DmsEndpointElasticsearchSettings:
    def __init__(
        self,
        *,
        endpoint_uri: builtins.str,
        service_access_role_arn: builtins.str,
        error_retry_duration: typing.Optional[jsii.Number] = None,
        full_load_error_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param endpoint_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_uri DmsEndpoint#endpoint_uri}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param error_retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#error_retry_duration DmsEndpoint#error_retry_duration}.
        :param full_load_error_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#full_load_error_percentage DmsEndpoint#full_load_error_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__829ecfcde2f36b10857231c73c71910e447fbb09dbfc6efa0c6b4aa084f437d9)
            check_type(argname="argument endpoint_uri", value=endpoint_uri, expected_type=type_hints["endpoint_uri"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument error_retry_duration", value=error_retry_duration, expected_type=type_hints["error_retry_duration"])
            check_type(argname="argument full_load_error_percentage", value=full_load_error_percentage, expected_type=type_hints["full_load_error_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_uri": endpoint_uri,
            "service_access_role_arn": service_access_role_arn,
        }
        if error_retry_duration is not None:
            self._values["error_retry_duration"] = error_retry_duration
        if full_load_error_percentage is not None:
            self._values["full_load_error_percentage"] = full_load_error_percentage

    @builtins.property
    def endpoint_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#endpoint_uri DmsEndpoint#endpoint_uri}.'''
        result = self._values.get("endpoint_uri")
        assert result is not None, "Required property 'endpoint_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        assert result is not None, "Required property 'service_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#error_retry_duration DmsEndpoint#error_retry_duration}.'''
        result = self._values.get("error_retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def full_load_error_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#full_load_error_percentage DmsEndpoint#full_load_error_percentage}.'''
        result = self._values.get("full_load_error_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointElasticsearchSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointElasticsearchSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointElasticsearchSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eff79772d5d38902ed9844fa0c69858f584853beff64592c637b8fc735b469eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetErrorRetryDuration")
    def reset_error_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorRetryDuration", []))

    @jsii.member(jsii_name="resetFullLoadErrorPercentage")
    def reset_full_load_error_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullLoadErrorPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="endpointUriInput")
    def endpoint_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointUriInput"))

    @builtins.property
    @jsii.member(jsii_name="errorRetryDurationInput")
    def error_retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "errorRetryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="fullLoadErrorPercentageInput")
    def full_load_error_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fullLoadErrorPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointUri")
    def endpoint_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointUri"))

    @endpoint_uri.setter
    def endpoint_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8e149d0d374858a16e47ca80355d95253623e5f6eaf1823c6ce5b53ecc26e16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointUri", value)

    @builtins.property
    @jsii.member(jsii_name="errorRetryDuration")
    def error_retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorRetryDuration"))

    @error_retry_duration.setter
    def error_retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__985b416c422e48613e172d0505074e1698dcd48955b383e260881a97317235d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorRetryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullLoadErrorPercentage"))

    @full_load_error_percentage.setter
    def full_load_error_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51713df2853e488c1edc5c3c01f83fed373aa41f88af8a2a9fe747495550a436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullLoadErrorPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7154b7bfb390fcfcddf3b98ecdcffbf03b0a84778408b6da258525fd4edc9834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointElasticsearchSettings]:
        return typing.cast(typing.Optional[DmsEndpointElasticsearchSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointElasticsearchSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6867dc774d8eb07a2d63f162bb10c87ae36948efd8421b77217d3d8eb118be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointKafkaSettings",
    jsii_struct_bases=[],
    name_mapping={
        "broker": "broker",
        "include_control_details": "includeControlDetails",
        "include_null_and_empty": "includeNullAndEmpty",
        "include_partition_value": "includePartitionValue",
        "include_table_alter_operations": "includeTableAlterOperations",
        "include_transaction_details": "includeTransactionDetails",
        "message_format": "messageFormat",
        "message_max_bytes": "messageMaxBytes",
        "no_hex_prefix": "noHexPrefix",
        "partition_include_schema_table": "partitionIncludeSchemaTable",
        "sasl_password": "saslPassword",
        "sasl_username": "saslUsername",
        "security_protocol": "securityProtocol",
        "ssl_ca_certificate_arn": "sslCaCertificateArn",
        "ssl_client_certificate_arn": "sslClientCertificateArn",
        "ssl_client_key_arn": "sslClientKeyArn",
        "ssl_client_key_password": "sslClientKeyPassword",
        "topic": "topic",
    },
)
class DmsEndpointKafkaSettings:
    def __init__(
        self,
        *,
        broker: builtins.str,
        include_control_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        message_max_bytes: typing.Optional[jsii.Number] = None,
        no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sasl_password: typing.Optional[builtins.str] = None,
        sasl_username: typing.Optional[builtins.str] = None,
        security_protocol: typing.Optional[builtins.str] = None,
        ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_arn: typing.Optional[builtins.str] = None,
        ssl_client_key_password: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#broker DmsEndpoint#broker}.
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param message_max_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_max_bytes DmsEndpoint#message_max_bytes}.
        :param no_hex_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#no_hex_prefix DmsEndpoint#no_hex_prefix}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param sasl_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_password DmsEndpoint#sasl_password}.
        :param sasl_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_username DmsEndpoint#sasl_username}.
        :param security_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#security_protocol DmsEndpoint#security_protocol}.
        :param ssl_ca_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.
        :param ssl_client_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_certificate_arn DmsEndpoint#ssl_client_certificate_arn}.
        :param ssl_client_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_arn DmsEndpoint#ssl_client_key_arn}.
        :param ssl_client_key_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_password DmsEndpoint#ssl_client_key_password}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#topic DmsEndpoint#topic}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93f4322f019a539d3aab8c4abd761baf949fdd1af67936ae1a5c8fd11c1fc03a)
            check_type(argname="argument broker", value=broker, expected_type=type_hints["broker"])
            check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
            check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
            check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
            check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
            check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            check_type(argname="argument message_max_bytes", value=message_max_bytes, expected_type=type_hints["message_max_bytes"])
            check_type(argname="argument no_hex_prefix", value=no_hex_prefix, expected_type=type_hints["no_hex_prefix"])
            check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
            check_type(argname="argument sasl_password", value=sasl_password, expected_type=type_hints["sasl_password"])
            check_type(argname="argument sasl_username", value=sasl_username, expected_type=type_hints["sasl_username"])
            check_type(argname="argument security_protocol", value=security_protocol, expected_type=type_hints["security_protocol"])
            check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
            check_type(argname="argument ssl_client_certificate_arn", value=ssl_client_certificate_arn, expected_type=type_hints["ssl_client_certificate_arn"])
            check_type(argname="argument ssl_client_key_arn", value=ssl_client_key_arn, expected_type=type_hints["ssl_client_key_arn"])
            check_type(argname="argument ssl_client_key_password", value=ssl_client_key_password, expected_type=type_hints["ssl_client_key_password"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "broker": broker,
        }
        if include_control_details is not None:
            self._values["include_control_details"] = include_control_details
        if include_null_and_empty is not None:
            self._values["include_null_and_empty"] = include_null_and_empty
        if include_partition_value is not None:
            self._values["include_partition_value"] = include_partition_value
        if include_table_alter_operations is not None:
            self._values["include_table_alter_operations"] = include_table_alter_operations
        if include_transaction_details is not None:
            self._values["include_transaction_details"] = include_transaction_details
        if message_format is not None:
            self._values["message_format"] = message_format
        if message_max_bytes is not None:
            self._values["message_max_bytes"] = message_max_bytes
        if no_hex_prefix is not None:
            self._values["no_hex_prefix"] = no_hex_prefix
        if partition_include_schema_table is not None:
            self._values["partition_include_schema_table"] = partition_include_schema_table
        if sasl_password is not None:
            self._values["sasl_password"] = sasl_password
        if sasl_username is not None:
            self._values["sasl_username"] = sasl_username
        if security_protocol is not None:
            self._values["security_protocol"] = security_protocol
        if ssl_ca_certificate_arn is not None:
            self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
        if ssl_client_certificate_arn is not None:
            self._values["ssl_client_certificate_arn"] = ssl_client_certificate_arn
        if ssl_client_key_arn is not None:
            self._values["ssl_client_key_arn"] = ssl_client_key_arn
        if ssl_client_key_password is not None:
            self._values["ssl_client_key_password"] = ssl_client_key_password
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def broker(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#broker DmsEndpoint#broker}.'''
        result = self._values.get("broker")
        assert result is not None, "Required property 'broker' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_control_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.'''
        result = self._values.get("include_control_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_null_and_empty(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.'''
        result = self._values.get("include_null_and_empty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_partition_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.'''
        result = self._values.get("include_partition_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_table_alter_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.'''
        result = self._values.get("include_table_alter_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_transaction_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.'''
        result = self._values.get("include_transaction_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.'''
        result = self._values.get("message_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_max_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_max_bytes DmsEndpoint#message_max_bytes}.'''
        result = self._values.get("message_max_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_hex_prefix(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#no_hex_prefix DmsEndpoint#no_hex_prefix}.'''
        result = self._values.get("no_hex_prefix")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def partition_include_schema_table(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.'''
        result = self._values.get("partition_include_schema_table")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sasl_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_password DmsEndpoint#sasl_password}.'''
        result = self._values.get("sasl_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sasl_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#sasl_username DmsEndpoint#sasl_username}.'''
        result = self._values.get("sasl_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#security_protocol DmsEndpoint#security_protocol}.'''
        result = self._values.get("security_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.'''
        result = self._values.get("ssl_ca_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_certificate_arn DmsEndpoint#ssl_client_certificate_arn}.'''
        result = self._values.get("ssl_client_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_arn DmsEndpoint#ssl_client_key_arn}.'''
        result = self._values.get("ssl_client_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_key_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_client_key_password DmsEndpoint#ssl_client_key_password}.'''
        result = self._values.get("ssl_client_key_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#topic DmsEndpoint#topic}.'''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointKafkaSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointKafkaSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointKafkaSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__181e73d9b35a6df4a65ad9413fe9e71ed5bd9cad09639e6b06c61fb5b3b4663e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeControlDetails")
    def reset_include_control_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeControlDetails", []))

    @jsii.member(jsii_name="resetIncludeNullAndEmpty")
    def reset_include_null_and_empty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeNullAndEmpty", []))

    @jsii.member(jsii_name="resetIncludePartitionValue")
    def reset_include_partition_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludePartitionValue", []))

    @jsii.member(jsii_name="resetIncludeTableAlterOperations")
    def reset_include_table_alter_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTableAlterOperations", []))

    @jsii.member(jsii_name="resetIncludeTransactionDetails")
    def reset_include_transaction_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTransactionDetails", []))

    @jsii.member(jsii_name="resetMessageFormat")
    def reset_message_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageFormat", []))

    @jsii.member(jsii_name="resetMessageMaxBytes")
    def reset_message_max_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageMaxBytes", []))

    @jsii.member(jsii_name="resetNoHexPrefix")
    def reset_no_hex_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoHexPrefix", []))

    @jsii.member(jsii_name="resetPartitionIncludeSchemaTable")
    def reset_partition_include_schema_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionIncludeSchemaTable", []))

    @jsii.member(jsii_name="resetSaslPassword")
    def reset_sasl_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaslPassword", []))

    @jsii.member(jsii_name="resetSaslUsername")
    def reset_sasl_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaslUsername", []))

    @jsii.member(jsii_name="resetSecurityProtocol")
    def reset_security_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityProtocol", []))

    @jsii.member(jsii_name="resetSslCaCertificateArn")
    def reset_ssl_ca_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCaCertificateArn", []))

    @jsii.member(jsii_name="resetSslClientCertificateArn")
    def reset_ssl_client_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientCertificateArn", []))

    @jsii.member(jsii_name="resetSslClientKeyArn")
    def reset_ssl_client_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientKeyArn", []))

    @jsii.member(jsii_name="resetSslClientKeyPassword")
    def reset_ssl_client_key_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientKeyPassword", []))

    @jsii.member(jsii_name="resetTopic")
    def reset_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopic", []))

    @builtins.property
    @jsii.member(jsii_name="brokerInput")
    def broker_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "brokerInput"))

    @builtins.property
    @jsii.member(jsii_name="includeControlDetailsInput")
    def include_control_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeControlDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmptyInput")
    def include_null_and_empty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeNullAndEmptyInput"))

    @builtins.property
    @jsii.member(jsii_name="includePartitionValueInput")
    def include_partition_value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includePartitionValueInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperationsInput")
    def include_table_alter_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeTableAlterOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetailsInput")
    def include_transaction_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeTransactionDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="messageMaxBytesInput")
    def message_max_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "messageMaxBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="noHexPrefixInput")
    def no_hex_prefix_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noHexPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTableInput")
    def partition_include_schema_table_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "partitionIncludeSchemaTableInput"))

    @builtins.property
    @jsii.member(jsii_name="saslPasswordInput")
    def sasl_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saslPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="saslUsernameInput")
    def sasl_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saslUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityProtocolInput")
    def security_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArnInput")
    def ssl_ca_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslCaCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificateArnInput")
    def ssl_client_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyArnInput")
    def ssl_client_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyPasswordInput")
    def ssl_client_key_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientKeyPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="broker")
    def broker(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "broker"))

    @broker.setter
    def broker(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26bdb1301c7b6f476d29a78fa17ebab454f3f338de1a20db7efcdf1424529e8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "broker", value)

    @builtins.property
    @jsii.member(jsii_name="includeControlDetails")
    def include_control_details(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeControlDetails"))

    @include_control_details.setter
    def include_control_details(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a019b5a564e2d94039d56e2b20465df59d833fe776ac94d4cd17685420c6005d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeControlDetails", value)

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmpty")
    def include_null_and_empty(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeNullAndEmpty"))

    @include_null_and_empty.setter
    def include_null_and_empty(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce5aaf5c0c48cc24d0081c9459676f92a15e7d2ead9e83bc93f6da47a7fb13f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeNullAndEmpty", value)

    @builtins.property
    @jsii.member(jsii_name="includePartitionValue")
    def include_partition_value(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includePartitionValue"))

    @include_partition_value.setter
    def include_partition_value(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64c000b676dfab954f9c77b7f88ff2f33659198faee6ed5e2ebc63b2aeec9800)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includePartitionValue", value)

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperations")
    def include_table_alter_operations(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeTableAlterOperations"))

    @include_table_alter_operations.setter
    def include_table_alter_operations(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94ff0d81536fb64760035e79cc1e9ec4b4bed7cd947573eddb5cf6dd2c648343)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTableAlterOperations", value)

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetails")
    def include_transaction_details(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeTransactionDetails"))

    @include_transaction_details.setter
    def include_transaction_details(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3241e672687ed4fd0c1db44edf79df4c5265103192424e37bc6d72e9b8975351)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTransactionDetails", value)

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf8967511e6787e8f3ee71453103f57fb0c98637864d5c7465bded2d8b9fb45d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="messageMaxBytes")
    def message_max_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "messageMaxBytes"))

    @message_max_bytes.setter
    def message_max_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e65322b84aa072c4efcaecff767d5a88a39e93e7f10fd30ac7377fa58221f7e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageMaxBytes", value)

    @builtins.property
    @jsii.member(jsii_name="noHexPrefix")
    def no_hex_prefix(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noHexPrefix"))

    @no_hex_prefix.setter
    def no_hex_prefix(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51b39ae38321689fec46ef9c7f26fd8da6f706ea5ec781db875723778724269)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noHexPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTable")
    def partition_include_schema_table(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "partitionIncludeSchemaTable"))

    @partition_include_schema_table.setter
    def partition_include_schema_table(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__464a896b65fcbe33f884ccb3da01d0693a3be6884756816697b6302effc85ba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionIncludeSchemaTable", value)

    @builtins.property
    @jsii.member(jsii_name="saslPassword")
    def sasl_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saslPassword"))

    @sasl_password.setter
    def sasl_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__173e43f1b9256205377e21b8def71bd0671bc4742f320f895a74dfb9e4aecbd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saslPassword", value)

    @builtins.property
    @jsii.member(jsii_name="saslUsername")
    def sasl_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saslUsername"))

    @sasl_username.setter
    def sasl_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4a3c27eb8ec8fda883a02d0855af449569b209ecc9f437e0bbcbabcc580ec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saslUsername", value)

    @builtins.property
    @jsii.member(jsii_name="securityProtocol")
    def security_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityProtocol"))

    @security_protocol.setter
    def security_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be8d52e0e700da1eb2ce2bc9749a5a0e63b32ce23d7f6950eaa9ba652d2bf5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCaCertificateArn"))

    @ssl_ca_certificate_arn.setter
    def ssl_ca_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf68725f4cdf255960cc3b5421e401edf3dd246f77ab7a60cabe64046a063df9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCaCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificateArn")
    def ssl_client_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientCertificateArn"))

    @ssl_client_certificate_arn.setter
    def ssl_client_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24bc053cf9b5667b4708f0717cba5e57a4c76acd4ee625ec5eb70a2cb1121c31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyArn")
    def ssl_client_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientKeyArn"))

    @ssl_client_key_arn.setter
    def ssl_client_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ddfaf95a3b8c655a200b34467c188a87b720f27c6c17c99208fbf2e822762b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyPassword")
    def ssl_client_key_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientKeyPassword"))

    @ssl_client_key_password.setter
    def ssl_client_key_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f08a6504af217f67b76589ed36d9bb5f05b8a0dc7b130dda264c3d3974fa30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientKeyPassword", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20b85062a8f14656e8ddafe129d2fd2164a1d3dac6e99182e92e97cbf8fdf45a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointKafkaSettings]:
        return typing.cast(typing.Optional[DmsEndpointKafkaSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DmsEndpointKafkaSettings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1b99846cf6bfcd138917338a41ce45e0ad156ff285d5e854ca456493609b0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointKinesisSettings",
    jsii_struct_bases=[],
    name_mapping={
        "include_control_details": "includeControlDetails",
        "include_null_and_empty": "includeNullAndEmpty",
        "include_partition_value": "includePartitionValue",
        "include_table_alter_operations": "includeTableAlterOperations",
        "include_transaction_details": "includeTransactionDetails",
        "message_format": "messageFormat",
        "partition_include_schema_table": "partitionIncludeSchemaTable",
        "service_access_role_arn": "serviceAccessRoleArn",
        "stream_arn": "streamArn",
    },
)
class DmsEndpointKinesisSettings:
    def __init__(
        self,
        *,
        include_control_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_partition_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_transaction_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message_format: typing.Optional[builtins.str] = None,
        partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        stream_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param include_control_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.
        :param include_null_and_empty: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.
        :param include_partition_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.
        :param include_table_alter_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.
        :param include_transaction_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.
        :param partition_include_schema_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#stream_arn DmsEndpoint#stream_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f25d3ea96c7d920617d4d9bfb6a8840b807facd40dd9ac3e58875cae9cc4e0c3)
            check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
            check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
            check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
            check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
            check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if include_control_details is not None:
            self._values["include_control_details"] = include_control_details
        if include_null_and_empty is not None:
            self._values["include_null_and_empty"] = include_null_and_empty
        if include_partition_value is not None:
            self._values["include_partition_value"] = include_partition_value
        if include_table_alter_operations is not None:
            self._values["include_table_alter_operations"] = include_table_alter_operations
        if include_transaction_details is not None:
            self._values["include_transaction_details"] = include_transaction_details
        if message_format is not None:
            self._values["message_format"] = message_format
        if partition_include_schema_table is not None:
            self._values["partition_include_schema_table"] = partition_include_schema_table
        if service_access_role_arn is not None:
            self._values["service_access_role_arn"] = service_access_role_arn
        if stream_arn is not None:
            self._values["stream_arn"] = stream_arn

    @builtins.property
    def include_control_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_control_details DmsEndpoint#include_control_details}.'''
        result = self._values.get("include_control_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_null_and_empty(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_null_and_empty DmsEndpoint#include_null_and_empty}.'''
        result = self._values.get("include_null_and_empty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_partition_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_partition_value DmsEndpoint#include_partition_value}.'''
        result = self._values.get("include_partition_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_table_alter_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_table_alter_operations DmsEndpoint#include_table_alter_operations}.'''
        result = self._values.get("include_table_alter_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_transaction_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_transaction_details DmsEndpoint#include_transaction_details}.'''
        result = self._values.get("include_transaction_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#message_format DmsEndpoint#message_format}.'''
        result = self._values.get("message_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_include_schema_table(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#partition_include_schema_table DmsEndpoint#partition_include_schema_table}.'''
        result = self._values.get("partition_include_schema_table")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def service_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#stream_arn DmsEndpoint#stream_arn}.'''
        result = self._values.get("stream_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointKinesisSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointKinesisSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointKinesisSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea835d4a584df7ac6a58b523f329674ce9e8a7d1ea4edfc2f102acafa194e512)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeControlDetails")
    def reset_include_control_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeControlDetails", []))

    @jsii.member(jsii_name="resetIncludeNullAndEmpty")
    def reset_include_null_and_empty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeNullAndEmpty", []))

    @jsii.member(jsii_name="resetIncludePartitionValue")
    def reset_include_partition_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludePartitionValue", []))

    @jsii.member(jsii_name="resetIncludeTableAlterOperations")
    def reset_include_table_alter_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTableAlterOperations", []))

    @jsii.member(jsii_name="resetIncludeTransactionDetails")
    def reset_include_transaction_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTransactionDetails", []))

    @jsii.member(jsii_name="resetMessageFormat")
    def reset_message_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageFormat", []))

    @jsii.member(jsii_name="resetPartitionIncludeSchemaTable")
    def reset_partition_include_schema_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionIncludeSchemaTable", []))

    @jsii.member(jsii_name="resetServiceAccessRoleArn")
    def reset_service_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRoleArn", []))

    @jsii.member(jsii_name="resetStreamArn")
    def reset_stream_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamArn", []))

    @builtins.property
    @jsii.member(jsii_name="includeControlDetailsInput")
    def include_control_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeControlDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmptyInput")
    def include_null_and_empty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeNullAndEmptyInput"))

    @builtins.property
    @jsii.member(jsii_name="includePartitionValueInput")
    def include_partition_value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includePartitionValueInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperationsInput")
    def include_table_alter_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeTableAlterOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetailsInput")
    def include_transaction_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeTransactionDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTableInput")
    def partition_include_schema_table_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "partitionIncludeSchemaTableInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="streamArnInput")
    def stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="includeControlDetails")
    def include_control_details(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeControlDetails"))

    @include_control_details.setter
    def include_control_details(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd00e6e712afe7c7e5d6e54c39089516ab287f00056800fa1568246c9f600d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeControlDetails", value)

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmpty")
    def include_null_and_empty(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeNullAndEmpty"))

    @include_null_and_empty.setter
    def include_null_and_empty(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bfad3c12a72ba0a31931377ebdfafba41ec924c407a7225f34b1b5bc4237059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeNullAndEmpty", value)

    @builtins.property
    @jsii.member(jsii_name="includePartitionValue")
    def include_partition_value(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includePartitionValue"))

    @include_partition_value.setter
    def include_partition_value(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681f489eb344d58d881cdc97dcdc243448ae290f779aa3555c9caf24d843aece)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includePartitionValue", value)

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperations")
    def include_table_alter_operations(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeTableAlterOperations"))

    @include_table_alter_operations.setter
    def include_table_alter_operations(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ffe9c767a7708b8034c282ea9b004f27fd3be905e022bc4f8b32c21dab5251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTableAlterOperations", value)

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetails")
    def include_transaction_details(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeTransactionDetails"))

    @include_transaction_details.setter
    def include_transaction_details(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc0bea1bd05eb37e0f7296b1e167f812fc696d080d6c88ef78a07a22c674f8c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTransactionDetails", value)

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bcc68f69398c8efe39e70dbc799367394b79646481f83b2460d7d4424cc0c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTable")
    def partition_include_schema_table(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "partitionIncludeSchemaTable"))

    @partition_include_schema_table.setter
    def partition_include_schema_table(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c1b220db1f2994f4598f4f55c027436525645dfb245f5795845599db409763)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionIncludeSchemaTable", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70b8362e9adb5da12021a4f96972f777183b97339041f86e73c5baa2ab8e3dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @stream_arn.setter
    def stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a65b7071e771a63edca99856daf69beac8463e689cc233886b90d86b0d10ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointKinesisSettings]:
        return typing.cast(typing.Optional[DmsEndpointKinesisSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointKinesisSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__062d0680411f76628364864623d07977b64a4be155c5d86d56aa996174c74fbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointMongodbSettings",
    jsii_struct_bases=[],
    name_mapping={
        "auth_mechanism": "authMechanism",
        "auth_source": "authSource",
        "auth_type": "authType",
        "docs_to_investigate": "docsToInvestigate",
        "extract_doc_id": "extractDocId",
        "nesting_level": "nestingLevel",
    },
)
class DmsEndpointMongodbSettings:
    def __init__(
        self,
        *,
        auth_mechanism: typing.Optional[builtins.str] = None,
        auth_source: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        docs_to_investigate: typing.Optional[builtins.str] = None,
        extract_doc_id: typing.Optional[builtins.str] = None,
        nesting_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_mechanism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_mechanism DmsEndpoint#auth_mechanism}.
        :param auth_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_source DmsEndpoint#auth_source}.
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.
        :param docs_to_investigate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#docs_to_investigate DmsEndpoint#docs_to_investigate}.
        :param extract_doc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extract_doc_id DmsEndpoint#extract_doc_id}.
        :param nesting_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#nesting_level DmsEndpoint#nesting_level}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e81b82bce9a25e0171aac4f11eb6bda8a127d694de106046f57ebd1e4b9498a)
            check_type(argname="argument auth_mechanism", value=auth_mechanism, expected_type=type_hints["auth_mechanism"])
            check_type(argname="argument auth_source", value=auth_source, expected_type=type_hints["auth_source"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument docs_to_investigate", value=docs_to_investigate, expected_type=type_hints["docs_to_investigate"])
            check_type(argname="argument extract_doc_id", value=extract_doc_id, expected_type=type_hints["extract_doc_id"])
            check_type(argname="argument nesting_level", value=nesting_level, expected_type=type_hints["nesting_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth_mechanism is not None:
            self._values["auth_mechanism"] = auth_mechanism
        if auth_source is not None:
            self._values["auth_source"] = auth_source
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if docs_to_investigate is not None:
            self._values["docs_to_investigate"] = docs_to_investigate
        if extract_doc_id is not None:
            self._values["extract_doc_id"] = extract_doc_id
        if nesting_level is not None:
            self._values["nesting_level"] = nesting_level

    @builtins.property
    def auth_mechanism(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_mechanism DmsEndpoint#auth_mechanism}.'''
        result = self._values.get("auth_mechanism")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_source DmsEndpoint#auth_source}.'''
        result = self._values.get("auth_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.'''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docs_to_investigate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#docs_to_investigate DmsEndpoint#docs_to_investigate}.'''
        result = self._values.get("docs_to_investigate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extract_doc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#extract_doc_id DmsEndpoint#extract_doc_id}.'''
        result = self._values.get("extract_doc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nesting_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#nesting_level DmsEndpoint#nesting_level}.'''
        result = self._values.get("nesting_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointMongodbSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointMongodbSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointMongodbSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__291a70efb97717ad56ae254c574d4c9337d9868e4ad6abbf17d9041ebc9a73ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthMechanism")
    def reset_auth_mechanism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMechanism", []))

    @jsii.member(jsii_name="resetAuthSource")
    def reset_auth_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthSource", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetDocsToInvestigate")
    def reset_docs_to_investigate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocsToInvestigate", []))

    @jsii.member(jsii_name="resetExtractDocId")
    def reset_extract_doc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtractDocId", []))

    @jsii.member(jsii_name="resetNestingLevel")
    def reset_nesting_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNestingLevel", []))

    @builtins.property
    @jsii.member(jsii_name="authMechanismInput")
    def auth_mechanism_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMechanismInput"))

    @builtins.property
    @jsii.member(jsii_name="authSourceInput")
    def auth_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="docsToInvestigateInput")
    def docs_to_investigate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "docsToInvestigateInput"))

    @builtins.property
    @jsii.member(jsii_name="extractDocIdInput")
    def extract_doc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extractDocIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nestingLevelInput")
    def nesting_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nestingLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="authMechanism")
    def auth_mechanism(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMechanism"))

    @auth_mechanism.setter
    def auth_mechanism(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3132968cc4a9a225081518ccf2fe0c48423ee025bfa7ad7378e4b29806cd788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMechanism", value)

    @builtins.property
    @jsii.member(jsii_name="authSource")
    def auth_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authSource"))

    @auth_source.setter
    def auth_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e4d240ea1cfa367bd983eb3457fac058ebd0bc2403b6928441e52e7b9fcfc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authSource", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47c80f9f8ca5857d21d2844d9e368b9d82532f42266a95845bdd257745b4c418)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="docsToInvestigate")
    def docs_to_investigate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "docsToInvestigate"))

    @docs_to_investigate.setter
    def docs_to_investigate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3628323fc3e771a10aa61012a174924d3c9445412ee7c5966ff59936c0ad6f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "docsToInvestigate", value)

    @builtins.property
    @jsii.member(jsii_name="extractDocId")
    def extract_doc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extractDocId"))

    @extract_doc_id.setter
    def extract_doc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e8bb320332f7164efd86f43f6bf2541c1b906ed8b1e49a3dc455d3dfd5f9ff4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extractDocId", value)

    @builtins.property
    @jsii.member(jsii_name="nestingLevel")
    def nesting_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nestingLevel"))

    @nesting_level.setter
    def nesting_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a590689558e79c0e0345a7a5d653730c02178ef19075b3f99dd0354569a01f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nestingLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointMongodbSettings]:
        return typing.cast(typing.Optional[DmsEndpointMongodbSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointMongodbSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20133ad669cc328c27f9e37f471d784e99b08a744a9240bf3cf91f7cf2fdc51e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointRedisSettings",
    jsii_struct_bases=[],
    name_mapping={
        "auth_type": "authType",
        "port": "port",
        "server_name": "serverName",
        "auth_password": "authPassword",
        "auth_user_name": "authUserName",
        "ssl_ca_certificate_arn": "sslCaCertificateArn",
        "ssl_security_protocol": "sslSecurityProtocol",
    },
)
class DmsEndpointRedisSettings:
    def __init__(
        self,
        *,
        auth_type: builtins.str,
        port: jsii.Number,
        server_name: builtins.str,
        auth_password: typing.Optional[builtins.str] = None,
        auth_user_name: typing.Optional[builtins.str] = None,
        ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
        ssl_security_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.
        :param server_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.
        :param auth_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_password DmsEndpoint#auth_password}.
        :param auth_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_user_name DmsEndpoint#auth_user_name}.
        :param ssl_ca_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.
        :param ssl_security_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_security_protocol DmsEndpoint#ssl_security_protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d952cb6c7f730936242a69eb3b3feaa5a9b3943f1e14d107611147ce49574ab5)
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument auth_password", value=auth_password, expected_type=type_hints["auth_password"])
            check_type(argname="argument auth_user_name", value=auth_user_name, expected_type=type_hints["auth_user_name"])
            check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
            check_type(argname="argument ssl_security_protocol", value=ssl_security_protocol, expected_type=type_hints["ssl_security_protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_type": auth_type,
            "port": port,
            "server_name": server_name,
        }
        if auth_password is not None:
            self._values["auth_password"] = auth_password
        if auth_user_name is not None:
            self._values["auth_user_name"] = auth_user_name
        if ssl_ca_certificate_arn is not None:
            self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
        if ssl_security_protocol is not None:
            self._values["ssl_security_protocol"] = ssl_security_protocol

    @builtins.property
    def auth_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_type DmsEndpoint#auth_type}.'''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#port DmsEndpoint#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def server_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_name DmsEndpoint#server_name}.'''
        result = self._values.get("server_name")
        assert result is not None, "Required property 'server_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_password DmsEndpoint#auth_password}.'''
        result = self._values.get("auth_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#auth_user_name DmsEndpoint#auth_user_name}.'''
        result = self._values.get("auth_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_ca_certificate_arn DmsEndpoint#ssl_ca_certificate_arn}.'''
        result = self._values.get("ssl_ca_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_security_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ssl_security_protocol DmsEndpoint#ssl_security_protocol}.'''
        result = self._values.get("ssl_security_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointRedisSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointRedisSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointRedisSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32f8130cf3a02f024a001f19ea99a2bc2145d891928134b0ebb36035bf99b891)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthPassword")
    def reset_auth_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthPassword", []))

    @jsii.member(jsii_name="resetAuthUserName")
    def reset_auth_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthUserName", []))

    @jsii.member(jsii_name="resetSslCaCertificateArn")
    def reset_ssl_ca_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCaCertificateArn", []))

    @jsii.member(jsii_name="resetSslSecurityProtocol")
    def reset_ssl_security_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslSecurityProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="authPasswordInput")
    def auth_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authUserNameInput")
    def auth_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArnInput")
    def ssl_ca_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslCaCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sslSecurityProtocolInput")
    def ssl_security_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslSecurityProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="authPassword")
    def auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authPassword"))

    @auth_password.setter
    def auth_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78df6d6754426e7f4058a6ef63bfe665f53d957f553390b8678bb48883557deb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authPassword", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a11bcee90d6f3d07c4c2aa22c9f5bdc98d2b8c1d09147435a587aa47dfa4732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="authUserName")
    def auth_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authUserName"))

    @auth_user_name.setter
    def auth_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4cf9bfb6d31f0baa1f6dfef2eb8522c4d2b6cdd05438d3ac200f7b2c8a7a250)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authUserName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__135fcf83c3a9070165fa617290fe40f86317c94c622c0d8b4f7ac6515d8b3787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb85aa7c41b05cb5361915c39a28b1abf7d55c51ce92fcb62ac3e63f8b7447d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCaCertificateArn"))

    @ssl_ca_certificate_arn.setter
    def ssl_ca_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2538787695cf074cbc1594eb3e91366805033718675bb35bad5cd888e3b4747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCaCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="sslSecurityProtocol")
    def ssl_security_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslSecurityProtocol"))

    @ssl_security_protocol.setter
    def ssl_security_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4875dafac1e9920be1a777f84defd35473d28a7eaa740bd3589b9be1022f2805)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslSecurityProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointRedisSettings]:
        return typing.cast(typing.Optional[DmsEndpointRedisSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DmsEndpointRedisSettings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f36f1887e243324257abb44fcfe25020361d8758ec1f0c5640dd0c6a48c75db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointRedshiftSettings",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_folder": "bucketFolder",
        "bucket_name": "bucketName",
        "encryption_mode": "encryptionMode",
        "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
        "service_access_role_arn": "serviceAccessRoleArn",
    },
)
class DmsEndpointRedshiftSettings:
    def __init__(
        self,
        *,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e5f24d3bebf6ced27370aa335d61a8fdbcacfafa64379f7c4fec8a0485b189)
            check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
            check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_folder is not None:
            self._values["bucket_folder"] = bucket_folder
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if server_side_encryption_kms_key_id is not None:
            self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
        if service_access_role_arn is not None:
            self._values["service_access_role_arn"] = service_access_role_arn

    @builtins.property
    def bucket_folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.'''
        result = self._values.get("bucket_folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.'''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.'''
        result = self._values.get("server_side_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointRedshiftSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointRedshiftSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointRedshiftSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5da871bb4b89c62f7c22d206c83891dfab39aa54935299aa4689caca2c9abe62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketFolder")
    def reset_bucket_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketFolder", []))

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetEncryptionMode")
    def reset_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionMode", []))

    @jsii.member(jsii_name="resetServerSideEncryptionKmsKeyId")
    def reset_server_side_encryption_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionKmsKeyId", []))

    @jsii.member(jsii_name="resetServiceAccessRoleArn")
    def reset_service_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="bucketFolderInput")
    def bucket_folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketFolderInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionModeInput")
    def encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyIdInput")
    def server_side_encryption_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSideEncryptionKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @bucket_folder.setter
    def bucket_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__989a936398c7b0c4185ebc49e6463ce6ddd3722e1548af7de4dd06749055f036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketFolder", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d25a789674c5f4caf297dc4224a2f2125086234dcfc29b12d902f92c5a51831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9be566864e9aa73c45573f40af1f812310e38e7dfd03457212007838cbd92724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @server_side_encryption_kms_key_id.setter
    def server_side_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb1427d7501b072da395d7cd909b710fed6bf42928a9a6658c709b4597057ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2424227100b55f0f342adee4953dd6c3e69599bbe9328d40add8544ff426f0d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointRedshiftSettings]:
        return typing.cast(typing.Optional[DmsEndpointRedshiftSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DmsEndpointRedshiftSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__943a3f90464c7488b3f9e1f475585c1ee925488bdebe99a86e43684257c534c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointS3Settings",
    jsii_struct_bases=[],
    name_mapping={
        "add_column_name": "addColumnName",
        "bucket_folder": "bucketFolder",
        "bucket_name": "bucketName",
        "canned_acl_for_objects": "cannedAclForObjects",
        "cdc_inserts_and_updates": "cdcInsertsAndUpdates",
        "cdc_inserts_only": "cdcInsertsOnly",
        "cdc_max_batch_interval": "cdcMaxBatchInterval",
        "cdc_min_file_size": "cdcMinFileSize",
        "cdc_path": "cdcPath",
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
        "dict_page_size_limit": "dictPageSizeLimit",
        "enable_statistics": "enableStatistics",
        "encoding_type": "encodingType",
        "encryption_mode": "encryptionMode",
        "external_table_definition": "externalTableDefinition",
        "ignore_header_rows": "ignoreHeaderRows",
        "ignore_headers_row": "ignoreHeadersRow",
        "include_op_for_full_load": "includeOpForFullLoad",
        "max_file_size": "maxFileSize",
        "parquet_timestamp_in_millisecond": "parquetTimestampInMillisecond",
        "parquet_version": "parquetVersion",
        "preserve_transactions": "preserveTransactions",
        "rfc4180": "rfc4180",
        "row_group_length": "rowGroupLength",
        "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
        "service_access_role_arn": "serviceAccessRoleArn",
        "timestamp_column_name": "timestampColumnName",
        "use_csv_no_sup_value": "useCsvNoSupValue",
        "use_task_start_time_for_full_load_timestamp": "useTaskStartTimeForFullLoadTimestamp",
    },
)
class DmsEndpointS3Settings:
    def __init__(
        self,
        *,
        add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bucket_folder: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        canned_acl_for_objects: typing.Optional[builtins.str] = None,
        cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
        cdc_min_file_size: typing.Optional[jsii.Number] = None,
        cdc_path: typing.Optional[builtins.str] = None,
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
        dict_page_size_limit: typing.Optional[jsii.Number] = None,
        enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encoding_type: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        external_table_definition: typing.Optional[builtins.str] = None,
        ignore_header_rows: typing.Optional[jsii.Number] = None,
        ignore_headers_row: typing.Optional[jsii.Number] = None,
        include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parquet_version: typing.Optional[builtins.str] = None,
        preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        row_group_length: typing.Optional[jsii.Number] = None,
        server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        service_access_role_arn: typing.Optional[builtins.str] = None,
        timestamp_column_name: typing.Optional[builtins.str] = None,
        use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param add_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#add_column_name DmsEndpoint#add_column_name}.
        :param bucket_folder: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.
        :param canned_acl_for_objects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#canned_acl_for_objects DmsEndpoint#canned_acl_for_objects}.
        :param cdc_inserts_and_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_and_updates DmsEndpoint#cdc_inserts_and_updates}.
        :param cdc_inserts_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_only DmsEndpoint#cdc_inserts_only}.
        :param cdc_max_batch_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_max_batch_interval DmsEndpoint#cdc_max_batch_interval}.
        :param cdc_min_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_min_file_size DmsEndpoint#cdc_min_file_size}.
        :param cdc_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_path DmsEndpoint#cdc_path}.
        :param compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#compression_type DmsEndpoint#compression_type}.
        :param csv_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_delimiter DmsEndpoint#csv_delimiter}.
        :param csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_no_sup_value DmsEndpoint#csv_no_sup_value}.
        :param csv_null_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_null_value DmsEndpoint#csv_null_value}.
        :param csv_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_row_delimiter DmsEndpoint#csv_row_delimiter}.
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_format DmsEndpoint#data_format}.
        :param data_page_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_page_size DmsEndpoint#data_page_size}.
        :param date_partition_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_delimiter DmsEndpoint#date_partition_delimiter}.
        :param date_partition_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_enabled DmsEndpoint#date_partition_enabled}.
        :param date_partition_sequence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_sequence DmsEndpoint#date_partition_sequence}.
        :param dict_page_size_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#dict_page_size_limit DmsEndpoint#dict_page_size_limit}.
        :param enable_statistics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#enable_statistics DmsEndpoint#enable_statistics}.
        :param encoding_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encoding_type DmsEndpoint#encoding_type}.
        :param encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.
        :param external_table_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#external_table_definition DmsEndpoint#external_table_definition}.
        :param ignore_header_rows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_header_rows DmsEndpoint#ignore_header_rows}.
        :param ignore_headers_row: This setting has no effect, is deprecated, and will be removed in a future version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_headers_row DmsEndpoint#ignore_headers_row}
        :param include_op_for_full_load: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_op_for_full_load DmsEndpoint#include_op_for_full_load}.
        :param max_file_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#max_file_size DmsEndpoint#max_file_size}.
        :param parquet_timestamp_in_millisecond: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_timestamp_in_millisecond DmsEndpoint#parquet_timestamp_in_millisecond}.
        :param parquet_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_version DmsEndpoint#parquet_version}.
        :param preserve_transactions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#preserve_transactions DmsEndpoint#preserve_transactions}.
        :param rfc4180: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#rfc_4180 DmsEndpoint#rfc_4180}.
        :param row_group_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#row_group_length DmsEndpoint#row_group_length}.
        :param server_side_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.
        :param timestamp_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timestamp_column_name DmsEndpoint#timestamp_column_name}.
        :param use_csv_no_sup_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_csv_no_sup_value DmsEndpoint#use_csv_no_sup_value}.
        :param use_task_start_time_for_full_load_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_task_start_time_for_full_load_timestamp DmsEndpoint#use_task_start_time_for_full_load_timestamp}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785a8e5e6e17dd4d009a18afedf8822f1050b62d949a49e78cf751faeb1a610d)
            check_type(argname="argument add_column_name", value=add_column_name, expected_type=type_hints["add_column_name"])
            check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument canned_acl_for_objects", value=canned_acl_for_objects, expected_type=type_hints["canned_acl_for_objects"])
            check_type(argname="argument cdc_inserts_and_updates", value=cdc_inserts_and_updates, expected_type=type_hints["cdc_inserts_and_updates"])
            check_type(argname="argument cdc_inserts_only", value=cdc_inserts_only, expected_type=type_hints["cdc_inserts_only"])
            check_type(argname="argument cdc_max_batch_interval", value=cdc_max_batch_interval, expected_type=type_hints["cdc_max_batch_interval"])
            check_type(argname="argument cdc_min_file_size", value=cdc_min_file_size, expected_type=type_hints["cdc_min_file_size"])
            check_type(argname="argument cdc_path", value=cdc_path, expected_type=type_hints["cdc_path"])
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
            check_type(argname="argument dict_page_size_limit", value=dict_page_size_limit, expected_type=type_hints["dict_page_size_limit"])
            check_type(argname="argument enable_statistics", value=enable_statistics, expected_type=type_hints["enable_statistics"])
            check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
            check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
            check_type(argname="argument external_table_definition", value=external_table_definition, expected_type=type_hints["external_table_definition"])
            check_type(argname="argument ignore_header_rows", value=ignore_header_rows, expected_type=type_hints["ignore_header_rows"])
            check_type(argname="argument ignore_headers_row", value=ignore_headers_row, expected_type=type_hints["ignore_headers_row"])
            check_type(argname="argument include_op_for_full_load", value=include_op_for_full_load, expected_type=type_hints["include_op_for_full_load"])
            check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
            check_type(argname="argument parquet_timestamp_in_millisecond", value=parquet_timestamp_in_millisecond, expected_type=type_hints["parquet_timestamp_in_millisecond"])
            check_type(argname="argument parquet_version", value=parquet_version, expected_type=type_hints["parquet_version"])
            check_type(argname="argument preserve_transactions", value=preserve_transactions, expected_type=type_hints["preserve_transactions"])
            check_type(argname="argument rfc4180", value=rfc4180, expected_type=type_hints["rfc4180"])
            check_type(argname="argument row_group_length", value=row_group_length, expected_type=type_hints["row_group_length"])
            check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            check_type(argname="argument timestamp_column_name", value=timestamp_column_name, expected_type=type_hints["timestamp_column_name"])
            check_type(argname="argument use_csv_no_sup_value", value=use_csv_no_sup_value, expected_type=type_hints["use_csv_no_sup_value"])
            check_type(argname="argument use_task_start_time_for_full_load_timestamp", value=use_task_start_time_for_full_load_timestamp, expected_type=type_hints["use_task_start_time_for_full_load_timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_column_name is not None:
            self._values["add_column_name"] = add_column_name
        if bucket_folder is not None:
            self._values["bucket_folder"] = bucket_folder
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
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
        if dict_page_size_limit is not None:
            self._values["dict_page_size_limit"] = dict_page_size_limit
        if enable_statistics is not None:
            self._values["enable_statistics"] = enable_statistics
        if encoding_type is not None:
            self._values["encoding_type"] = encoding_type
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if external_table_definition is not None:
            self._values["external_table_definition"] = external_table_definition
        if ignore_header_rows is not None:
            self._values["ignore_header_rows"] = ignore_header_rows
        if ignore_headers_row is not None:
            self._values["ignore_headers_row"] = ignore_headers_row
        if include_op_for_full_load is not None:
            self._values["include_op_for_full_load"] = include_op_for_full_load
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
        if service_access_role_arn is not None:
            self._values["service_access_role_arn"] = service_access_role_arn
        if timestamp_column_name is not None:
            self._values["timestamp_column_name"] = timestamp_column_name
        if use_csv_no_sup_value is not None:
            self._values["use_csv_no_sup_value"] = use_csv_no_sup_value
        if use_task_start_time_for_full_load_timestamp is not None:
            self._values["use_task_start_time_for_full_load_timestamp"] = use_task_start_time_for_full_load_timestamp

    @builtins.property
    def add_column_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#add_column_name DmsEndpoint#add_column_name}.'''
        result = self._values.get("add_column_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def bucket_folder(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_folder DmsEndpoint#bucket_folder}.'''
        result = self._values.get("bucket_folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#bucket_name DmsEndpoint#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def canned_acl_for_objects(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#canned_acl_for_objects DmsEndpoint#canned_acl_for_objects}.'''
        result = self._values.get("canned_acl_for_objects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_inserts_and_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_and_updates DmsEndpoint#cdc_inserts_and_updates}.'''
        result = self._values.get("cdc_inserts_and_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cdc_inserts_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_inserts_only DmsEndpoint#cdc_inserts_only}.'''
        result = self._values.get("cdc_inserts_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cdc_max_batch_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_max_batch_interval DmsEndpoint#cdc_max_batch_interval}.'''
        result = self._values.get("cdc_max_batch_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_min_file_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_min_file_size DmsEndpoint#cdc_min_file_size}.'''
        result = self._values.get("cdc_min_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#cdc_path DmsEndpoint#cdc_path}.'''
        result = self._values.get("cdc_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compression_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#compression_type DmsEndpoint#compression_type}.'''
        result = self._values.get("compression_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_delimiter DmsEndpoint#csv_delimiter}.'''
        result = self._values.get("csv_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_no_sup_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_no_sup_value DmsEndpoint#csv_no_sup_value}.'''
        result = self._values.get("csv_no_sup_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_null_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_null_value DmsEndpoint#csv_null_value}.'''
        result = self._values.get("csv_null_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_row_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#csv_row_delimiter DmsEndpoint#csv_row_delimiter}.'''
        result = self._values.get("csv_row_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_format DmsEndpoint#data_format}.'''
        result = self._values.get("data_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_page_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#data_page_size DmsEndpoint#data_page_size}.'''
        result = self._values.get("data_page_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def date_partition_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_delimiter DmsEndpoint#date_partition_delimiter}.'''
        result = self._values.get("date_partition_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def date_partition_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_enabled DmsEndpoint#date_partition_enabled}.'''
        result = self._values.get("date_partition_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def date_partition_sequence(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#date_partition_sequence DmsEndpoint#date_partition_sequence}.'''
        result = self._values.get("date_partition_sequence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dict_page_size_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#dict_page_size_limit DmsEndpoint#dict_page_size_limit}.'''
        result = self._values.get("dict_page_size_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_statistics(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#enable_statistics DmsEndpoint#enable_statistics}.'''
        result = self._values.get("enable_statistics")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encoding_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encoding_type DmsEndpoint#encoding_type}.'''
        result = self._values.get("encoding_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#encryption_mode DmsEndpoint#encryption_mode}.'''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_table_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#external_table_definition DmsEndpoint#external_table_definition}.'''
        result = self._values.get("external_table_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_header_rows(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_header_rows DmsEndpoint#ignore_header_rows}.'''
        result = self._values.get("ignore_header_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_headers_row(self) -> typing.Optional[jsii.Number]:
        '''This setting has no effect, is deprecated, and will be removed in a future version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#ignore_headers_row DmsEndpoint#ignore_headers_row}
        '''
        result = self._values.get("ignore_headers_row")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def include_op_for_full_load(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#include_op_for_full_load DmsEndpoint#include_op_for_full_load}.'''
        result = self._values.get("include_op_for_full_load")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def max_file_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#max_file_size DmsEndpoint#max_file_size}.'''
        result = self._values.get("max_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parquet_timestamp_in_millisecond(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_timestamp_in_millisecond DmsEndpoint#parquet_timestamp_in_millisecond}.'''
        result = self._values.get("parquet_timestamp_in_millisecond")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def parquet_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#parquet_version DmsEndpoint#parquet_version}.'''
        result = self._values.get("parquet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_transactions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#preserve_transactions DmsEndpoint#preserve_transactions}.'''
        result = self._values.get("preserve_transactions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def rfc4180(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#rfc_4180 DmsEndpoint#rfc_4180}.'''
        result = self._values.get("rfc4180")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def row_group_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#row_group_length DmsEndpoint#row_group_length}.'''
        result = self._values.get("row_group_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#server_side_encryption_kms_key_id DmsEndpoint#server_side_encryption_kms_key_id}.'''
        result = self._values.get("server_side_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#service_access_role_arn DmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timestamp_column_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#timestamp_column_name DmsEndpoint#timestamp_column_name}.'''
        result = self._values.get("timestamp_column_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_csv_no_sup_value(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_csv_no_sup_value DmsEndpoint#use_csv_no_sup_value}.'''
        result = self._values.get("use_csv_no_sup_value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#use_task_start_time_for_full_load_timestamp DmsEndpoint#use_task_start_time_for_full_load_timestamp}.'''
        result = self._values.get("use_task_start_time_for_full_load_timestamp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointS3Settings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointS3SettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointS3SettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f85c72ebfa37f8299ce4be2db8097cf6f635e0239d3c834799515cd3192a8545)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddColumnName")
    def reset_add_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddColumnName", []))

    @jsii.member(jsii_name="resetBucketFolder")
    def reset_bucket_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketFolder", []))

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

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

    @jsii.member(jsii_name="resetExternalTableDefinition")
    def reset_external_table_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalTableDefinition", []))

    @jsii.member(jsii_name="resetIgnoreHeaderRows")
    def reset_ignore_header_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreHeaderRows", []))

    @jsii.member(jsii_name="resetIgnoreHeadersRow")
    def reset_ignore_headers_row(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreHeadersRow", []))

    @jsii.member(jsii_name="resetIncludeOpForFullLoad")
    def reset_include_op_for_full_load(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeOpForFullLoad", []))

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

    @jsii.member(jsii_name="resetServiceAccessRoleArn")
    def reset_service_access_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessRoleArn", []))

    @jsii.member(jsii_name="resetTimestampColumnName")
    def reset_timestamp_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestampColumnName", []))

    @jsii.member(jsii_name="resetUseCsvNoSupValue")
    def reset_use_csv_no_sup_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCsvNoSupValue", []))

    @jsii.member(jsii_name="resetUseTaskStartTimeForFullLoadTimestamp")
    def reset_use_task_start_time_for_full_load_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseTaskStartTimeForFullLoadTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="addColumnNameInput")
    def add_column_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "addColumnNameInput"))

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
    @jsii.member(jsii_name="externalTableDefinitionInput")
    def external_table_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalTableDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreHeaderRowsInput")
    def ignore_header_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ignoreHeaderRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreHeadersRowInput")
    def ignore_headers_row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ignoreHeadersRowInput"))

    @builtins.property
    @jsii.member(jsii_name="includeOpForFullLoadInput")
    def include_op_for_full_load_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeOpForFullLoadInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c6878224fdae339b155c36b64cd5677658583ee198d33f075fc9ad628a2c70cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @bucket_folder.setter
    def bucket_folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8073748d1fa24026daea67b9d778ec27bb2c1475c57a2310626bd11b538b54fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketFolder", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b031b1f6fe46ef3da822ca8efb45bd2db78cf3017e5b4330807f97ea27778c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAclForObjects"))

    @canned_acl_for_objects.setter
    def canned_acl_for_objects(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e876f609239b02941b48d0fb939108ddb52a4fb0da78583c5722d70cbc5b3ea4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__442583759bd928bc51d6651fb9cf4791ff6674201f96acb3cd5ee17b89e55016)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a82920d48f638f825a8c2dcdd9a7a96f97f1e72a5aa4a7ee1bfdc26496bce85c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcInsertsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMaxBatchInterval"))

    @cdc_max_batch_interval.setter
    def cdc_max_batch_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a13e503203b61bda61a875d33f777995f2f3d9311dcea2b99b19515022a62f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcMaxBatchInterval", value)

    @builtins.property
    @jsii.member(jsii_name="cdcMinFileSize")
    def cdc_min_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMinFileSize"))

    @cdc_min_file_size.setter
    def cdc_min_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeea94d3e63ae17c4d68e9adf68694a4d6b1cc7e454659b2a77475a4af0f6d5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcMinFileSize", value)

    @builtins.property
    @jsii.member(jsii_name="cdcPath")
    def cdc_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcPath"))

    @cdc_path.setter
    def cdc_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42019247978a0be8f097a1f83fdc9faf8463aea42ad41513de930f7960fc1361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcPath", value)

    @builtins.property
    @jsii.member(jsii_name="compressionType")
    def compression_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionType"))

    @compression_type.setter
    def compression_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e058033f8af54fb028f5e26e818929537767bd240e98f1ed8a999f632176b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionType", value)

    @builtins.property
    @jsii.member(jsii_name="csvDelimiter")
    def csv_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvDelimiter"))

    @csv_delimiter.setter
    def csv_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c205f417fae6702f0b1ad466558c5507d8f8622416829bf2bf664aefc5ac2277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="csvNoSupValue")
    def csv_no_sup_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNoSupValue"))

    @csv_no_sup_value.setter
    def csv_no_sup_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14ea8e282769ab0eb2bcc9f2f462787e97142b0253742b2f8afbf37743b21a26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvNoSupValue", value)

    @builtins.property
    @jsii.member(jsii_name="csvNullValue")
    def csv_null_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNullValue"))

    @csv_null_value.setter
    def csv_null_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124596b693a1270d80bd46c8c7d6a5ceb7389fb9d4cd04ecc46d65b1c166ac21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvNullValue", value)

    @builtins.property
    @jsii.member(jsii_name="csvRowDelimiter")
    def csv_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvRowDelimiter"))

    @csv_row_delimiter.setter
    def csv_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833fe683cd1ee86fbc26ec4ee70af2c50b67fb8893621c6c57b75a2ec77eac2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @data_format.setter
    def data_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e27f7f6f17cc22c47c1a916fcbda61f77ffb5e6061111575970490126377357)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFormat", value)

    @builtins.property
    @jsii.member(jsii_name="dataPageSize")
    def data_page_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataPageSize"))

    @data_page_size.setter
    def data_page_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869a0731e6dac4536b6d9afafb465353e8fec1597b639a81cc5c28c60ed95a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPageSize", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionDelimiter"))

    @date_partition_delimiter.setter
    def date_partition_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d6541a752711eed950622ba38b8e8d6df5a663f35b5dda7f4c438f13bb10c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b6abd6e0fa1dc2e2c1c89b682af0d3e643aea7c4e3c7e19ab5d8adfb21de6b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="datePartitionSequence")
    def date_partition_sequence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionSequence"))

    @date_partition_sequence.setter
    def date_partition_sequence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef9fa9beab1c04c6b69bdec6d2b4cc5d7d03736fbb54b08f69f70769fecc432b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datePartitionSequence", value)

    @builtins.property
    @jsii.member(jsii_name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dictPageSizeLimit"))

    @dict_page_size_limit.setter
    def dict_page_size_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0fef90efbd9b6b94f108dc141cfb673fe4a3ebfcb52b80e00357bc7a8965d7a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__24f59527071d2227cdd305f72093a83b7c49ee15ef6c8bd65419965389950c13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStatistics", value)

    @builtins.property
    @jsii.member(jsii_name="encodingType")
    def encoding_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encodingType"))

    @encoding_type.setter
    def encoding_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7a76878b73a5306b82799bdb747285aa2695212554f72f26cae68053207bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encodingType", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b56ea75085af4d6591bf8393442970da8f338b2a001f050ecbc45f63f55422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="externalTableDefinition")
    def external_table_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalTableDefinition"))

    @external_table_definition.setter
    def external_table_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a0a29c5135d432ddd45d7ec3f5424382864e8e7b6a4773ba27e26deea0298c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalTableDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreHeaderRows")
    def ignore_header_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreHeaderRows"))

    @ignore_header_rows.setter
    def ignore_header_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__552b048b68adc161549e40bf68fb67461d2fa319b71eab18178c022e3bca2d18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreHeaderRows", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreHeadersRow")
    def ignore_headers_row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreHeadersRow"))

    @ignore_headers_row.setter
    def ignore_headers_row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e3a0ec7708a2d41e5cc17cec4eb174892a634747e7eb23be7ea7dd604bea37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreHeadersRow", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__1e7f104fecdd9c644704bfe67248510755c24b93f0f044833baa5bd866bd0f93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeOpForFullLoad", value)

    @builtins.property
    @jsii.member(jsii_name="maxFileSize")
    def max_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFileSize"))

    @max_file_size.setter
    def max_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21728bcf6f7d6e7963b8fb555a2ebe625c1d8fb67d1a1841c8f061ea5fd25301)
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
            type_hints = typing.get_type_hints(_typecheckingstub__17358edb09754d4b0aebb3aade1a303ff73b7b678564745b202d2277dee82a85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parquetTimestampInMillisecond", value)

    @builtins.property
    @jsii.member(jsii_name="parquetVersion")
    def parquet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parquetVersion"))

    @parquet_version.setter
    def parquet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c00f910869f1775da51da521cec9fa44d3bcedd154a41414bf96da23707645)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1facdbd33737283ee5852bfdae1dd38c6610e38b114f5e4066b3d921862a2fbd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__69f54080ec38978fbb0f62437742e651d598cb347c0ccac3fc85a8cf5fb2c138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rfc4180", value)

    @builtins.property
    @jsii.member(jsii_name="rowGroupLength")
    def row_group_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowGroupLength"))

    @row_group_length.setter
    def row_group_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70b3cd17df2bbfe3398aae277f64f5664fd59feba9ccad51cc5e7f81246745a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowGroupLength", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @server_side_encryption_kms_key_id.setter
    def server_side_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a6f762e01493c457b15e23a93420eb76417d0040218b4aa4dc64d1d9637cd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66bb97ecdfde3bba38488d0bc9d9634eb7a348068767581fbad29fac802204ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="timestampColumnName")
    def timestamp_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timestampColumnName"))

    @timestamp_column_name.setter
    def timestamp_column_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e70238d9a0bd36f5b5f1251aa98b4519265943c50e7a60a68351333c8fc49e4a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b71d8808fe0c516353e050df4669d09d48fc4e4cdf112000e3c6e0ef3163adf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8c4c203a42cb66bb5bcec346d567953244b3844eedd1b5b97cbdebed5b0b1b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useTaskStartTimeForFullLoadTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DmsEndpointS3Settings]:
        return typing.cast(typing.Optional[DmsEndpointS3Settings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DmsEndpointS3Settings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7cb3748843e53d021faed2c678cf20c5f179c63e9da8ce1689f51374e5a780d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dmsEndpoint.DmsEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class DmsEndpointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#create DmsEndpoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#delete DmsEndpoint#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed7f9b77fc7b20687778df1562fb58fc382200093980dd7644cb63b611e0ce52)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#create DmsEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dms_endpoint#delete DmsEndpoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DmsEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DmsEndpointTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dmsEndpoint.DmsEndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66ed6a3e243f994a55e60ac576977102e7c83b5dc449ed04d0608bc3911da19b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__01ace3b92725542a56eae3f279081d00102d3c22b7d5856e4ce57342b404bd8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9495a60718d6faedb88de3462ee2d5c72f32be5e400efa7ee033e34defcf923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DmsEndpointTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DmsEndpointTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DmsEndpointTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c43b31f7fde61de4733fc0d58f618a379930e3ee1920c894b45aa87fbdb751c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DmsEndpoint",
    "DmsEndpointConfig",
    "DmsEndpointElasticsearchSettings",
    "DmsEndpointElasticsearchSettingsOutputReference",
    "DmsEndpointKafkaSettings",
    "DmsEndpointKafkaSettingsOutputReference",
    "DmsEndpointKinesisSettings",
    "DmsEndpointKinesisSettingsOutputReference",
    "DmsEndpointMongodbSettings",
    "DmsEndpointMongodbSettingsOutputReference",
    "DmsEndpointRedisSettings",
    "DmsEndpointRedisSettingsOutputReference",
    "DmsEndpointRedshiftSettings",
    "DmsEndpointRedshiftSettingsOutputReference",
    "DmsEndpointS3Settings",
    "DmsEndpointS3SettingsOutputReference",
    "DmsEndpointTimeouts",
    "DmsEndpointTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__9020f5b2b715532017afb2eb9f9a9a03e0b6e2ccdd73b3fb466ce55676bd3d89(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    endpoint_id: builtins.str,
    endpoint_type: builtins.str,
    engine_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    elasticsearch_settings: typing.Optional[typing.Union[DmsEndpointElasticsearchSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kafka_settings: typing.Optional[typing.Union[DmsEndpointKafkaSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_settings: typing.Optional[typing.Union[DmsEndpointKinesisSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    mongodb_settings: typing.Optional[typing.Union[DmsEndpointMongodbSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    redis_settings: typing.Optional[typing.Union[DmsEndpointRedisSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift_settings: typing.Optional[typing.Union[DmsEndpointRedshiftSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_settings: typing.Optional[typing.Union[DmsEndpointS3Settings, typing.Dict[builtins.str, typing.Any]]] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_arn: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    service_access_role: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DmsEndpointTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    username: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d0ab9d10796d8c84780b9609d9e2e79e579846f3b420869b7b74917ed3757c4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f1105d4acf2681438f01c6aaea591cfa0661c2828b0e5ec50dc3c18c85e2f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3acc89431bee22031596e0af9fb53c688c3bd846b01352e5e0db514b3e4aac0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a3109b9f7f561a1907fbfbcc3c654e53ee3d7ccc044dc8a0752a7ee5f17c72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e97a45287b20d7e3520484923249ab2564280d9cc5b6a875bd13463d9a8294d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c72e675ddcac8f72a59964dd4643c232cf54b86227cd1ff223b7fb5fcc078cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3894b9ce77ca22542e6df7f602448b2a758b6c256961986bc5f25edf42bad655(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11902d7d4da539113fb941000f5d145e255c71d2d6ff2d0de1287777eb489286(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14905011025ee78d9802d79d660ce83c1a6a92f1714f11eb7b75cefecd6a7d88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e36e893488dbba48e700b44e4f01762e686e42335e98fe3a9312fdab412c64f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89a3055baf1e6281c4e9c3c23cadf75650bb076bb9f6dd68c6b0487c7b9c4f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0844f6c8bcb8bf86cb1c179140275d548ae723df5e31bac5170c67e2baec9d2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c505b6c299b903a23cd0438ac4e9d32d32c3b036e399a576664d9de324159b8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9952c43668f9a3080316a4ce4206a3b2c8f1cb108b6c69b5d28d690caffb904a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d07a126353a15d177bc82bbb20db05378170e1802b159baeb26b0c680fb624e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__194ea8aeac0b23dd381129fca9ec3c2370fc99fdff6cef2243f54f67c62d1297(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12976f18a4035e0306ee876893066bace5e11592ff9d78bd2c1162bb4d432a5b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100b2cbe2062e63d11faf836404cf3be9a6c95242f996e2ddfefde697aa0fedd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32b717e212dfc67dcd7c8e9e1db55b361f64cca0c3f78247e879746c162f763(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    endpoint_id: builtins.str,
    endpoint_type: builtins.str,
    engine_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    elasticsearch_settings: typing.Optional[typing.Union[DmsEndpointElasticsearchSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kafka_settings: typing.Optional[typing.Union[DmsEndpointKafkaSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_settings: typing.Optional[typing.Union[DmsEndpointKinesisSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    mongodb_settings: typing.Optional[typing.Union[DmsEndpointMongodbSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    redis_settings: typing.Optional[typing.Union[DmsEndpointRedisSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    redshift_settings: typing.Optional[typing.Union[DmsEndpointRedshiftSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_settings: typing.Optional[typing.Union[DmsEndpointS3Settings, typing.Dict[builtins.str, typing.Any]]] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_arn: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    service_access_role: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DmsEndpointTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__829ecfcde2f36b10857231c73c71910e447fbb09dbfc6efa0c6b4aa084f437d9(
    *,
    endpoint_uri: builtins.str,
    service_access_role_arn: builtins.str,
    error_retry_duration: typing.Optional[jsii.Number] = None,
    full_load_error_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff79772d5d38902ed9844fa0c69858f584853beff64592c637b8fc735b469eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8e149d0d374858a16e47ca80355d95253623e5f6eaf1823c6ce5b53ecc26e16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985b416c422e48613e172d0505074e1698dcd48955b383e260881a97317235d0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51713df2853e488c1edc5c3c01f83fed373aa41f88af8a2a9fe747495550a436(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7154b7bfb390fcfcddf3b98ecdcffbf03b0a84778408b6da258525fd4edc9834(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6867dc774d8eb07a2d63f162bb10c87ae36948efd8421b77217d3d8eb118be(
    value: typing.Optional[DmsEndpointElasticsearchSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f4322f019a539d3aab8c4abd761baf949fdd1af67936ae1a5c8fd11c1fc03a(
    *,
    broker: builtins.str,
    include_control_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_partition_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_transaction_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message_format: typing.Optional[builtins.str] = None,
    message_max_bytes: typing.Optional[jsii.Number] = None,
    no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sasl_password: typing.Optional[builtins.str] = None,
    sasl_username: typing.Optional[builtins.str] = None,
    security_protocol: typing.Optional[builtins.str] = None,
    ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_client_key_arn: typing.Optional[builtins.str] = None,
    ssl_client_key_password: typing.Optional[builtins.str] = None,
    topic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181e73d9b35a6df4a65ad9413fe9e71ed5bd9cad09639e6b06c61fb5b3b4663e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26bdb1301c7b6f476d29a78fa17ebab454f3f338de1a20db7efcdf1424529e8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a019b5a564e2d94039d56e2b20465df59d833fe776ac94d4cd17685420c6005d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce5aaf5c0c48cc24d0081c9459676f92a15e7d2ead9e83bc93f6da47a7fb13f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64c000b676dfab954f9c77b7f88ff2f33659198faee6ed5e2ebc63b2aeec9800(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94ff0d81536fb64760035e79cc1e9ec4b4bed7cd947573eddb5cf6dd2c648343(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3241e672687ed4fd0c1db44edf79df4c5265103192424e37bc6d72e9b8975351(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf8967511e6787e8f3ee71453103f57fb0c98637864d5c7465bded2d8b9fb45d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e65322b84aa072c4efcaecff767d5a88a39e93e7f10fd30ac7377fa58221f7e3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51b39ae38321689fec46ef9c7f26fd8da6f706ea5ec781db875723778724269(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464a896b65fcbe33f884ccb3da01d0693a3be6884756816697b6302effc85ba0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__173e43f1b9256205377e21b8def71bd0671bc4742f320f895a74dfb9e4aecbd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4a3c27eb8ec8fda883a02d0855af449569b209ecc9f437e0bbcbabcc580ec5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be8d52e0e700da1eb2ce2bc9749a5a0e63b32ce23d7f6950eaa9ba652d2bf5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf68725f4cdf255960cc3b5421e401edf3dd246f77ab7a60cabe64046a063df9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24bc053cf9b5667b4708f0717cba5e57a4c76acd4ee625ec5eb70a2cb1121c31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ddfaf95a3b8c655a200b34467c188a87b720f27c6c17c99208fbf2e822762b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f08a6504af217f67b76589ed36d9bb5f05b8a0dc7b130dda264c3d3974fa30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20b85062a8f14656e8ddafe129d2fd2164a1d3dac6e99182e92e97cbf8fdf45a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1b99846cf6bfcd138917338a41ce45e0ad156ff285d5e854ca456493609b0d(
    value: typing.Optional[DmsEndpointKafkaSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25d3ea96c7d920617d4d9bfb6a8840b807facd40dd9ac3e58875cae9cc4e0c3(
    *,
    include_control_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_partition_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_transaction_details: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message_format: typing.Optional[builtins.str] = None,
    partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    stream_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea835d4a584df7ac6a58b523f329674ce9e8a7d1ea4edfc2f102acafa194e512(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd00e6e712afe7c7e5d6e54c39089516ab287f00056800fa1568246c9f600d7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bfad3c12a72ba0a31931377ebdfafba41ec924c407a7225f34b1b5bc4237059(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681f489eb344d58d881cdc97dcdc243448ae290f779aa3555c9caf24d843aece(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ffe9c767a7708b8034c282ea9b004f27fd3be905e022bc4f8b32c21dab5251(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc0bea1bd05eb37e0f7296b1e167f812fc696d080d6c88ef78a07a22c674f8c1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bcc68f69398c8efe39e70dbc799367394b79646481f83b2460d7d4424cc0c2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c1b220db1f2994f4598f4f55c027436525645dfb245f5795845599db409763(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b8362e9adb5da12021a4f96972f777183b97339041f86e73c5baa2ab8e3dfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a65b7071e771a63edca99856daf69beac8463e689cc233886b90d86b0d10ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062d0680411f76628364864623d07977b64a4be155c5d86d56aa996174c74fbd(
    value: typing.Optional[DmsEndpointKinesisSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e81b82bce9a25e0171aac4f11eb6bda8a127d694de106046f57ebd1e4b9498a(
    *,
    auth_mechanism: typing.Optional[builtins.str] = None,
    auth_source: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    docs_to_investigate: typing.Optional[builtins.str] = None,
    extract_doc_id: typing.Optional[builtins.str] = None,
    nesting_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__291a70efb97717ad56ae254c574d4c9337d9868e4ad6abbf17d9041ebc9a73ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3132968cc4a9a225081518ccf2fe0c48423ee025bfa7ad7378e4b29806cd788(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e4d240ea1cfa367bd983eb3457fac058ebd0bc2403b6928441e52e7b9fcfc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47c80f9f8ca5857d21d2844d9e368b9d82532f42266a95845bdd257745b4c418(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3628323fc3e771a10aa61012a174924d3c9445412ee7c5966ff59936c0ad6f09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e8bb320332f7164efd86f43f6bf2541c1b906ed8b1e49a3dc455d3dfd5f9ff4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a590689558e79c0e0345a7a5d653730c02178ef19075b3f99dd0354569a01f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20133ad669cc328c27f9e37f471d784e99b08a744a9240bf3cf91f7cf2fdc51e(
    value: typing.Optional[DmsEndpointMongodbSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d952cb6c7f730936242a69eb3b3feaa5a9b3943f1e14d107611147ce49574ab5(
    *,
    auth_type: builtins.str,
    port: jsii.Number,
    server_name: builtins.str,
    auth_password: typing.Optional[builtins.str] = None,
    auth_user_name: typing.Optional[builtins.str] = None,
    ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_security_protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f8130cf3a02f024a001f19ea99a2bc2145d891928134b0ebb36035bf99b891(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78df6d6754426e7f4058a6ef63bfe665f53d957f553390b8678bb48883557deb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a11bcee90d6f3d07c4c2aa22c9f5bdc98d2b8c1d09147435a587aa47dfa4732(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4cf9bfb6d31f0baa1f6dfef2eb8522c4d2b6cdd05438d3ac200f7b2c8a7a250(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__135fcf83c3a9070165fa617290fe40f86317c94c622c0d8b4f7ac6515d8b3787(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb85aa7c41b05cb5361915c39a28b1abf7d55c51ce92fcb62ac3e63f8b7447d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2538787695cf074cbc1594eb3e91366805033718675bb35bad5cd888e3b4747(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4875dafac1e9920be1a777f84defd35473d28a7eaa740bd3589b9be1022f2805(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f36f1887e243324257abb44fcfe25020361d8758ec1f0c5640dd0c6a48c75db(
    value: typing.Optional[DmsEndpointRedisSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e5f24d3bebf6ced27370aa335d61a8fdbcacfafa64379f7c4fec8a0485b189(
    *,
    bucket_folder: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5da871bb4b89c62f7c22d206c83891dfab39aa54935299aa4689caca2c9abe62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__989a936398c7b0c4185ebc49e6463ce6ddd3722e1548af7de4dd06749055f036(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d25a789674c5f4caf297dc4224a2f2125086234dcfc29b12d902f92c5a51831(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be566864e9aa73c45573f40af1f812310e38e7dfd03457212007838cbd92724(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb1427d7501b072da395d7cd909b710fed6bf42928a9a6658c709b4597057ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2424227100b55f0f342adee4953dd6c3e69599bbe9328d40add8544ff426f0d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943a3f90464c7488b3f9e1f475585c1ee925488bdebe99a86e43684257c534c5(
    value: typing.Optional[DmsEndpointRedshiftSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785a8e5e6e17dd4d009a18afedf8822f1050b62d949a49e78cf751faeb1a610d(
    *,
    add_column_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    canned_acl_for_objects: typing.Optional[builtins.str] = None,
    cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
    cdc_min_file_size: typing.Optional[jsii.Number] = None,
    cdc_path: typing.Optional[builtins.str] = None,
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
    dict_page_size_limit: typing.Optional[jsii.Number] = None,
    enable_statistics: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    external_table_definition: typing.Optional[builtins.str] = None,
    ignore_header_rows: typing.Optional[jsii.Number] = None,
    ignore_headers_row: typing.Optional[jsii.Number] = None,
    include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parquet_version: typing.Optional[builtins.str] = None,
    preserve_transactions: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rfc4180: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    row_group_length: typing.Optional[jsii.Number] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    timestamp_column_name: typing.Optional[builtins.str] = None,
    use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85c72ebfa37f8299ce4be2db8097cf6f635e0239d3c834799515cd3192a8545(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6878224fdae339b155c36b64cd5677658583ee198d33f075fc9ad628a2c70cc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8073748d1fa24026daea67b9d778ec27bb2c1475c57a2310626bd11b538b54fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b031b1f6fe46ef3da822ca8efb45bd2db78cf3017e5b4330807f97ea27778c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e876f609239b02941b48d0fb939108ddb52a4fb0da78583c5722d70cbc5b3ea4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442583759bd928bc51d6651fb9cf4791ff6674201f96acb3cd5ee17b89e55016(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82920d48f638f825a8c2dcdd9a7a96f97f1e72a5aa4a7ee1bfdc26496bce85c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a13e503203b61bda61a875d33f777995f2f3d9311dcea2b99b19515022a62f2a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeea94d3e63ae17c4d68e9adf68694a4d6b1cc7e454659b2a77475a4af0f6d5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42019247978a0be8f097a1f83fdc9faf8463aea42ad41513de930f7960fc1361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e058033f8af54fb028f5e26e818929537767bd240e98f1ed8a999f632176b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c205f417fae6702f0b1ad466558c5507d8f8622416829bf2bf664aefc5ac2277(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ea8e282769ab0eb2bcc9f2f462787e97142b0253742b2f8afbf37743b21a26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124596b693a1270d80bd46c8c7d6a5ceb7389fb9d4cd04ecc46d65b1c166ac21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833fe683cd1ee86fbc26ec4ee70af2c50b67fb8893621c6c57b75a2ec77eac2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e27f7f6f17cc22c47c1a916fcbda61f77ffb5e6061111575970490126377357(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869a0731e6dac4536b6d9afafb465353e8fec1597b639a81cc5c28c60ed95a60(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d6541a752711eed950622ba38b8e8d6df5a663f35b5dda7f4c438f13bb10c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b6abd6e0fa1dc2e2c1c89b682af0d3e643aea7c4e3c7e19ab5d8adfb21de6b6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef9fa9beab1c04c6b69bdec6d2b4cc5d7d03736fbb54b08f69f70769fecc432b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0fef90efbd9b6b94f108dc141cfb673fe4a3ebfcb52b80e00357bc7a8965d7a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f59527071d2227cdd305f72093a83b7c49ee15ef6c8bd65419965389950c13(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7a76878b73a5306b82799bdb747285aa2695212554f72f26cae68053207bd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b56ea75085af4d6591bf8393442970da8f338b2a001f050ecbc45f63f55422(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a0a29c5135d432ddd45d7ec3f5424382864e8e7b6a4773ba27e26deea0298c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552b048b68adc161549e40bf68fb67461d2fa319b71eab18178c022e3bca2d18(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e3a0ec7708a2d41e5cc17cec4eb174892a634747e7eb23be7ea7dd604bea37(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e7f104fecdd9c644704bfe67248510755c24b93f0f044833baa5bd866bd0f93(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21728bcf6f7d6e7963b8fb555a2ebe625c1d8fb67d1a1841c8f061ea5fd25301(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17358edb09754d4b0aebb3aade1a303ff73b7b678564745b202d2277dee82a85(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c00f910869f1775da51da521cec9fa44d3bcedd154a41414bf96da23707645(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1facdbd33737283ee5852bfdae1dd38c6610e38b114f5e4066b3d921862a2fbd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f54080ec38978fbb0f62437742e651d598cb347c0ccac3fc85a8cf5fb2c138(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b3cd17df2bbfe3398aae277f64f5664fd59feba9ccad51cc5e7f81246745a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6f762e01493c457b15e23a93420eb76417d0040218b4aa4dc64d1d9637cd64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66bb97ecdfde3bba38488d0bc9d9634eb7a348068767581fbad29fac802204ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70238d9a0bd36f5b5f1251aa98b4519265943c50e7a60a68351333c8fc49e4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b71d8808fe0c516353e050df4669d09d48fc4e4cdf112000e3c6e0ef3163adf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c4c203a42cb66bb5bcec346d567953244b3844eedd1b5b97cbdebed5b0b1b6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7cb3748843e53d021faed2c678cf20c5f179c63e9da8ce1689f51374e5a780d(
    value: typing.Optional[DmsEndpointS3Settings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7f9b77fc7b20687778df1562fb58fc382200093980dd7644cb63b611e0ce52(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ed6a3e243f994a55e60ac576977102e7c83b5dc449ed04d0608bc3911da19b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ace3b92725542a56eae3f279081d00102d3c22b7d5856e4ce57342b404bd8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9495a60718d6faedb88de3462ee2d5c72f32be5e400efa7ee033e34defcf923(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c43b31f7fde61de4733fc0d58f618a379930e3ee1920c894b45aa87fbdb751c(
    value: typing.Optional[typing.Union[DmsEndpointTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
