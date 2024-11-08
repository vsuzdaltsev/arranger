'''
# `aws_db_instance`

Refer to the Terraform Registory for docs: [`aws_db_instance`](https://www.terraform.io/docs/providers/aws/r/db_instance).
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


class DbInstance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbInstance.DbInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/db_instance aws_db_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        instance_class: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        backup_window: typing.Optional[builtins.str] = None,
        blue_green_update: typing.Optional[typing.Union["DbInstanceBlueGreenUpdate", typing.Dict[builtins.str, typing.Any]]] = None,
        ca_cert_identifier: typing.Optional[builtins.str] = None,
        character_set_name: typing.Optional[builtins.str] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        customer_owned_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_iam_instance_profile: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        delete_automated_backups: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        domain: typing.Optional[builtins.str] = None,
        domain_iam_role_name: typing.Optional[builtins.str] = None,
        enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identifier: typing.Optional[builtins.str] = None,
        identifier_prefix: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        license_model: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[builtins.str] = None,
        max_allocated_storage: typing.Optional[jsii.Number] = None,
        monitoring_interval: typing.Optional[jsii.Number] = None,
        monitoring_role_arn: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        nchar_character_set_name: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        option_group_name: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
        performance_insights_retention_period: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        replica_mode: typing.Optional[builtins.str] = None,
        replicate_source_db: typing.Optional[builtins.str] = None,
        restore_to_point_in_time: typing.Optional[typing.Union["DbInstanceRestoreToPointInTime", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_import: typing.Optional[typing.Union["DbInstanceS3Import", typing.Dict[builtins.str, typing.Any]]] = None,
        security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        storage_throughput: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DbInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/db_instance aws_db_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#instance_class DbInstance#instance_class}.
        :param allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#allocated_storage DbInstance#allocated_storage}.
        :param allow_major_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#allow_major_version_upgrade DbInstance#allow_major_version_upgrade}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#apply_immediately DbInstance#apply_immediately}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#auto_minor_version_upgrade DbInstance#auto_minor_version_upgrade}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#availability_zone DbInstance#availability_zone}.
        :param backup_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#backup_retention_period DbInstance#backup_retention_period}.
        :param backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#backup_window DbInstance#backup_window}.
        :param blue_green_update: blue_green_update block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#blue_green_update DbInstance#blue_green_update}
        :param ca_cert_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#ca_cert_identifier DbInstance#ca_cert_identifier}.
        :param character_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#character_set_name DbInstance#character_set_name}.
        :param copy_tags_to_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#copy_tags_to_snapshot DbInstance#copy_tags_to_snapshot}.
        :param customer_owned_ip_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#customer_owned_ip_enabled DbInstance#customer_owned_ip_enabled}.
        :param custom_iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#custom_iam_instance_profile DbInstance#custom_iam_instance_profile}.
        :param db_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#db_name DbInstance#db_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#db_subnet_group_name DbInstance#db_subnet_group_name}.
        :param delete_automated_backups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#delete_automated_backups DbInstance#delete_automated_backups}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#deletion_protection DbInstance#deletion_protection}.
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#domain DbInstance#domain}.
        :param domain_iam_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#domain_iam_role_name DbInstance#domain_iam_role_name}.
        :param enabled_cloudwatch_logs_exports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#enabled_cloudwatch_logs_exports DbInstance#enabled_cloudwatch_logs_exports}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#engine DbInstance#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#engine_version DbInstance#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#final_snapshot_identifier DbInstance#final_snapshot_identifier}.
        :param iam_database_authentication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#iam_database_authentication_enabled DbInstance#iam_database_authentication_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#id DbInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#identifier DbInstance#identifier}.
        :param identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#identifier_prefix DbInstance#identifier_prefix}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#iops DbInstance#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#kms_key_id DbInstance#kms_key_id}.
        :param license_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#license_model DbInstance#license_model}.
        :param maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#maintenance_window DbInstance#maintenance_window}.
        :param max_allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#max_allocated_storage DbInstance#max_allocated_storage}.
        :param monitoring_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#monitoring_interval DbInstance#monitoring_interval}.
        :param monitoring_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#monitoring_role_arn DbInstance#monitoring_role_arn}.
        :param multi_az: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#multi_az DbInstance#multi_az}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#name DbInstance#name}.
        :param nchar_character_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#nchar_character_set_name DbInstance#nchar_character_set_name}.
        :param network_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#network_type DbInstance#network_type}.
        :param option_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#option_group_name DbInstance#option_group_name}.
        :param parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#parameter_group_name DbInstance#parameter_group_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#password DbInstance#password}.
        :param performance_insights_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_enabled DbInstance#performance_insights_enabled}.
        :param performance_insights_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_kms_key_id DbInstance#performance_insights_kms_key_id}.
        :param performance_insights_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_retention_period DbInstance#performance_insights_retention_period}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#port DbInstance#port}.
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#publicly_accessible DbInstance#publicly_accessible}.
        :param replica_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#replica_mode DbInstance#replica_mode}.
        :param replicate_source_db: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#replicate_source_db DbInstance#replicate_source_db}.
        :param restore_to_point_in_time: restore_to_point_in_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#restore_to_point_in_time DbInstance#restore_to_point_in_time}
        :param s3_import: s3_import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#s3_import DbInstance#s3_import}
        :param security_group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#security_group_names DbInstance#security_group_names}.
        :param skip_final_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#skip_final_snapshot DbInstance#skip_final_snapshot}.
        :param snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#snapshot_identifier DbInstance#snapshot_identifier}.
        :param storage_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_encrypted DbInstance#storage_encrypted}.
        :param storage_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_throughput DbInstance#storage_throughput}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_type DbInstance#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#tags DbInstance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#tags_all DbInstance#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#timeouts DbInstance#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#timezone DbInstance#timezone}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#username DbInstance#username}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#vpc_security_group_ids DbInstance#vpc_security_group_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974b938e704a96b58ee5be2125171c90333b4ef887dbe3b5e7fc443438642914)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DbInstanceConfig(
            instance_class=instance_class,
            allocated_storage=allocated_storage,
            allow_major_version_upgrade=allow_major_version_upgrade,
            apply_immediately=apply_immediately,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            backup_retention_period=backup_retention_period,
            backup_window=backup_window,
            blue_green_update=blue_green_update,
            ca_cert_identifier=ca_cert_identifier,
            character_set_name=character_set_name,
            copy_tags_to_snapshot=copy_tags_to_snapshot,
            customer_owned_ip_enabled=customer_owned_ip_enabled,
            custom_iam_instance_profile=custom_iam_instance_profile,
            db_name=db_name,
            db_subnet_group_name=db_subnet_group_name,
            delete_automated_backups=delete_automated_backups,
            deletion_protection=deletion_protection,
            domain=domain,
            domain_iam_role_name=domain_iam_role_name,
            enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
            engine=engine,
            engine_version=engine_version,
            final_snapshot_identifier=final_snapshot_identifier,
            iam_database_authentication_enabled=iam_database_authentication_enabled,
            id=id,
            identifier=identifier,
            identifier_prefix=identifier_prefix,
            iops=iops,
            kms_key_id=kms_key_id,
            license_model=license_model,
            maintenance_window=maintenance_window,
            max_allocated_storage=max_allocated_storage,
            monitoring_interval=monitoring_interval,
            monitoring_role_arn=monitoring_role_arn,
            multi_az=multi_az,
            name=name,
            nchar_character_set_name=nchar_character_set_name,
            network_type=network_type,
            option_group_name=option_group_name,
            parameter_group_name=parameter_group_name,
            password=password,
            performance_insights_enabled=performance_insights_enabled,
            performance_insights_kms_key_id=performance_insights_kms_key_id,
            performance_insights_retention_period=performance_insights_retention_period,
            port=port,
            publicly_accessible=publicly_accessible,
            replica_mode=replica_mode,
            replicate_source_db=replicate_source_db,
            restore_to_point_in_time=restore_to_point_in_time,
            s3_import=s3_import,
            security_group_names=security_group_names,
            skip_final_snapshot=skip_final_snapshot,
            snapshot_identifier=snapshot_identifier,
            storage_encrypted=storage_encrypted,
            storage_throughput=storage_throughput,
            storage_type=storage_type,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            timezone=timezone,
            username=username,
            vpc_security_group_ids=vpc_security_group_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBlueGreenUpdate")
    def put_blue_green_update(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#enabled DbInstance#enabled}.
        '''
        value = DbInstanceBlueGreenUpdate(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putBlueGreenUpdate", [value]))

    @jsii.member(jsii_name="putRestoreToPointInTime")
    def put_restore_to_point_in_time(
        self,
        *,
        restore_time: typing.Optional[builtins.str] = None,
        source_db_instance_automated_backups_arn: typing.Optional[builtins.str] = None,
        source_db_instance_identifier: typing.Optional[builtins.str] = None,
        source_dbi_resource_id: typing.Optional[builtins.str] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param restore_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#restore_time DbInstance#restore_time}.
        :param source_db_instance_automated_backups_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_db_instance_automated_backups_arn DbInstance#source_db_instance_automated_backups_arn}.
        :param source_db_instance_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_db_instance_identifier DbInstance#source_db_instance_identifier}.
        :param source_dbi_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_dbi_resource_id DbInstance#source_dbi_resource_id}.
        :param use_latest_restorable_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#use_latest_restorable_time DbInstance#use_latest_restorable_time}.
        '''
        value = DbInstanceRestoreToPointInTime(
            restore_time=restore_time,
            source_db_instance_automated_backups_arn=source_db_instance_automated_backups_arn,
            source_db_instance_identifier=source_db_instance_identifier,
            source_dbi_resource_id=source_dbi_resource_id,
            use_latest_restorable_time=use_latest_restorable_time,
        )

        return typing.cast(None, jsii.invoke(self, "putRestoreToPointInTime", [value]))

    @jsii.member(jsii_name="putS3Import")
    def put_s3_import(
        self,
        *,
        bucket_name: builtins.str,
        ingestion_role: builtins.str,
        source_engine: builtins.str,
        source_engine_version: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#bucket_name DbInstance#bucket_name}.
        :param ingestion_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#ingestion_role DbInstance#ingestion_role}.
        :param source_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_engine DbInstance#source_engine}.
        :param source_engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_engine_version DbInstance#source_engine_version}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#bucket_prefix DbInstance#bucket_prefix}.
        '''
        value = DbInstanceS3Import(
            bucket_name=bucket_name,
            ingestion_role=ingestion_role,
            source_engine=source_engine,
            source_engine_version=source_engine_version,
            bucket_prefix=bucket_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Import", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#create DbInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#delete DbInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#update DbInstance#update}.
        '''
        value = DbInstanceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocatedStorage")
    def reset_allocated_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocatedStorage", []))

    @jsii.member(jsii_name="resetAllowMajorVersionUpgrade")
    def reset_allow_major_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMajorVersionUpgrade", []))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAutoMinorVersionUpgrade")
    def reset_auto_minor_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMinorVersionUpgrade", []))

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetBackupRetentionPeriod")
    def reset_backup_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRetentionPeriod", []))

    @jsii.member(jsii_name="resetBackupWindow")
    def reset_backup_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupWindow", []))

    @jsii.member(jsii_name="resetBlueGreenUpdate")
    def reset_blue_green_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlueGreenUpdate", []))

    @jsii.member(jsii_name="resetCaCertIdentifier")
    def reset_ca_cert_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCertIdentifier", []))

    @jsii.member(jsii_name="resetCharacterSetName")
    def reset_character_set_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCharacterSetName", []))

    @jsii.member(jsii_name="resetCopyTagsToSnapshot")
    def reset_copy_tags_to_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToSnapshot", []))

    @jsii.member(jsii_name="resetCustomerOwnedIpEnabled")
    def reset_customer_owned_ip_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerOwnedIpEnabled", []))

    @jsii.member(jsii_name="resetCustomIamInstanceProfile")
    def reset_custom_iam_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomIamInstanceProfile", []))

    @jsii.member(jsii_name="resetDbName")
    def reset_db_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbName", []))

    @jsii.member(jsii_name="resetDbSubnetGroupName")
    def reset_db_subnet_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbSubnetGroupName", []))

    @jsii.member(jsii_name="resetDeleteAutomatedBackups")
    def reset_delete_automated_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAutomatedBackups", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetDomainIamRoleName")
    def reset_domain_iam_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainIamRoleName", []))

    @jsii.member(jsii_name="resetEnabledCloudwatchLogsExports")
    def reset_enabled_cloudwatch_logs_exports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledCloudwatchLogsExports", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetFinalSnapshotIdentifier")
    def reset_final_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFinalSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetIamDatabaseAuthenticationEnabled")
    def reset_iam_database_authentication_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamDatabaseAuthenticationEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentifier")
    def reset_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifier", []))

    @jsii.member(jsii_name="resetIdentifierPrefix")
    def reset_identifier_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifierPrefix", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetLicenseModel")
    def reset_license_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseModel", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetMaxAllocatedStorage")
    def reset_max_allocated_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAllocatedStorage", []))

    @jsii.member(jsii_name="resetMonitoringInterval")
    def reset_monitoring_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringInterval", []))

    @jsii.member(jsii_name="resetMonitoringRoleArn")
    def reset_monitoring_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringRoleArn", []))

    @jsii.member(jsii_name="resetMultiAz")
    def reset_multi_az(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiAz", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNcharCharacterSetName")
    def reset_nchar_character_set_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNcharCharacterSetName", []))

    @jsii.member(jsii_name="resetNetworkType")
    def reset_network_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkType", []))

    @jsii.member(jsii_name="resetOptionGroupName")
    def reset_option_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionGroupName", []))

    @jsii.member(jsii_name="resetParameterGroupName")
    def reset_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterGroupName", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPerformanceInsightsEnabled")
    def reset_performance_insights_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceInsightsEnabled", []))

    @jsii.member(jsii_name="resetPerformanceInsightsKmsKeyId")
    def reset_performance_insights_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceInsightsKmsKeyId", []))

    @jsii.member(jsii_name="resetPerformanceInsightsRetentionPeriod")
    def reset_performance_insights_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceInsightsRetentionPeriod", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPubliclyAccessible")
    def reset_publicly_accessible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubliclyAccessible", []))

    @jsii.member(jsii_name="resetReplicaMode")
    def reset_replica_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicaMode", []))

    @jsii.member(jsii_name="resetReplicateSourceDb")
    def reset_replicate_source_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicateSourceDb", []))

    @jsii.member(jsii_name="resetRestoreToPointInTime")
    def reset_restore_to_point_in_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreToPointInTime", []))

    @jsii.member(jsii_name="resetS3Import")
    def reset_s3_import(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Import", []))

    @jsii.member(jsii_name="resetSecurityGroupNames")
    def reset_security_group_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupNames", []))

    @jsii.member(jsii_name="resetSkipFinalSnapshot")
    def reset_skip_final_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipFinalSnapshot", []))

    @jsii.member(jsii_name="resetSnapshotIdentifier")
    def reset_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetStorageEncrypted")
    def reset_storage_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEncrypted", []))

    @jsii.member(jsii_name="resetStorageThroughput")
    def reset_storage_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageThroughput", []))

    @jsii.member(jsii_name="resetStorageType")
    def reset_storage_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetVpcSecurityGroupIds")
    def reset_vpc_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcSecurityGroupIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenUpdate")
    def blue_green_update(self) -> "DbInstanceBlueGreenUpdateOutputReference":
        return typing.cast("DbInstanceBlueGreenUpdateOutputReference", jsii.get(self, "blueGreenUpdate"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionActual")
    def engine_version_actual(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersionActual"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="latestRestorableTime")
    def latest_restorable_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latestRestorableTime"))

    @builtins.property
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "replicas"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> "DbInstanceRestoreToPointInTimeOutputReference":
        return typing.cast("DbInstanceRestoreToPointInTimeOutputReference", jsii.get(self, "restoreToPointInTime"))

    @builtins.property
    @jsii.member(jsii_name="s3Import")
    def s3_import(self) -> "DbInstanceS3ImportOutputReference":
        return typing.cast("DbInstanceS3ImportOutputReference", jsii.get(self, "s3Import"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DbInstanceTimeoutsOutputReference":
        return typing.cast("DbInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allocatedStorageInput")
    def allocated_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocatedStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgradeInput")
    def allow_major_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowMajorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediatelyInput")
    def apply_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "applyImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgradeInput")
    def auto_minor_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoMinorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriodInput")
    def backup_retention_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="backupWindowInput")
    def backup_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenUpdateInput")
    def blue_green_update_input(self) -> typing.Optional["DbInstanceBlueGreenUpdate"]:
        return typing.cast(typing.Optional["DbInstanceBlueGreenUpdate"], jsii.get(self, "blueGreenUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertIdentifierInput")
    def ca_cert_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="characterSetNameInput")
    def character_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "characterSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshotInput")
    def copy_tags_to_snapshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "copyTagsToSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="customerOwnedIpEnabledInput")
    def customer_owned_ip_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "customerOwnedIpEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="customIamInstanceProfileInput")
    def custom_iam_instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customIamInstanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="dbNameInput")
    def db_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupNameInput")
    def db_subnet_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAutomatedBackupsInput")
    def delete_automated_backups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteAutomatedBackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="domainIamRoleNameInput")
    def domain_iam_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainIamRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledCloudwatchLogsExportsInput")
    def enabled_cloudwatch_logs_exports_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledCloudwatchLogsExportsInput"))

    @builtins.property
    @jsii.member(jsii_name="engineInput")
    def engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotIdentifierInput")
    def final_snapshot_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="iamDatabaseAuthenticationEnabledInput")
    def iam_database_authentication_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "iamDatabaseAuthenticationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierPrefixInput")
    def identifier_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceClassInput")
    def instance_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceClassInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseModelInput")
    def license_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseModelInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAllocatedStorageInput")
    def max_allocated_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAllocatedStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringIntervalInput")
    def monitoring_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monitoringIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringRoleArnInput")
    def monitoring_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitoringRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="multiAzInput")
    def multi_az_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "multiAzInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ncharCharacterSetNameInput")
    def nchar_character_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ncharCharacterSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkTypeInput")
    def network_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="optionGroupNameInput")
    def option_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterGroupNameInput")
    def parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsEnabledInput")
    def performance_insights_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "performanceInsightsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsKmsKeyIdInput")
    def performance_insights_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "performanceInsightsKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsRetentionPeriodInput")
    def performance_insights_retention_period_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "performanceInsightsRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessibleInput")
    def publicly_accessible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publiclyAccessibleInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaModeInput")
    def replica_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicaModeInput"))

    @builtins.property
    @jsii.member(jsii_name="replicateSourceDbInput")
    def replicate_source_db_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicateSourceDbInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreToPointInTimeInput")
    def restore_to_point_in_time_input(
        self,
    ) -> typing.Optional["DbInstanceRestoreToPointInTime"]:
        return typing.cast(typing.Optional["DbInstanceRestoreToPointInTime"], jsii.get(self, "restoreToPointInTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ImportInput")
    def s3_import_input(self) -> typing.Optional["DbInstanceS3Import"]:
        return typing.cast(typing.Optional["DbInstanceS3Import"], jsii.get(self, "s3ImportInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupNamesInput")
    def security_group_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="skipFinalSnapshotInput")
    def skip_final_snapshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipFinalSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifierInput")
    def snapshot_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEncryptedInput")
    def storage_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "storageEncryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="storageThroughputInput")
    def storage_throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

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
    ) -> typing.Optional[typing.Union["DbInstanceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DbInstanceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIdsInput")
    def vpc_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="allocatedStorage")
    def allocated_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocatedStorage"))

    @allocated_storage.setter
    def allocated_storage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174817fb47090258d0ea94f02ec3fc129ee2229caf56e54798d9e0ef90979191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedStorage", value)

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowMajorVersionUpgrade"))

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2fc318d42beddd9e588c6f74e83d67bcb6b68b5de25636f380c0e58bd9ace9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMajorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="applyImmediately")
    def apply_immediately(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "applyImmediately"))

    @apply_immediately.setter
    def apply_immediately(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a15a4fdce010abc86934015196b0fab26d9014ae10ae7491e32f3afb389bcf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyImmediately", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf4f7986ccdf722f0fb34637410de6e57762fdc583a2f3890c9be561ff8308cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9c291a2c6b074d5599da62796af2b1f8d84dc72537ce94190a2be4bb32849ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriod")
    def backup_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupRetentionPeriod"))

    @backup_retention_period.setter
    def backup_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0a1ae7e03f649630e3903cfff3cbd37b59548749014795c459037fed806c990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="backupWindow")
    def backup_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupWindow"))

    @backup_window.setter
    def backup_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddfcda28c661a9891a0e4dca715b689e986c1400e2019c2fe2f7438bab46077e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupWindow", value)

    @builtins.property
    @jsii.member(jsii_name="caCertIdentifier")
    def ca_cert_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCertIdentifier"))

    @ca_cert_identifier.setter
    def ca_cert_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7b5da042d495de3090acda33858903ca23ceb1a1f8d7775dffe66542be8310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="characterSetName")
    def character_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "characterSetName"))

    @character_set_name.setter
    def character_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd26c01f1013b2cb18b697b6ce6aff7d5dfa400cc6eaf749c09c9fbb7522541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "characterSetName", value)

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "copyTagsToSnapshot"))

    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff26a52435cec93e06cb69d7de41b05dddcc1dade47f8b0a8304ea47e93abaaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToSnapshot", value)

    @builtins.property
    @jsii.member(jsii_name="customerOwnedIpEnabled")
    def customer_owned_ip_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "customerOwnedIpEnabled"))

    @customer_owned_ip_enabled.setter
    def customer_owned_ip_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333f8d336d7685f93d4390249672e5d050411a0e045557a391519fb50198cf5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerOwnedIpEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="customIamInstanceProfile")
    def custom_iam_instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customIamInstanceProfile"))

    @custom_iam_instance_profile.setter
    def custom_iam_instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d996bdfaff3c91618093db1543e2764d4a839b458c59bece223084e43efa78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customIamInstanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48587c73a265ed06bd69bffed76fc2447631de6d4e52a636cc9e353343ece660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbb2a608c6a5d0c76a8f5a8d4ca8f8114df6e46d064c04a7016cfa50c4e4a10e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAutomatedBackups")
    def delete_automated_backups(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteAutomatedBackups"))

    @delete_automated_backups.setter
    def delete_automated_backups(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac29582a4353ab19e158e655a27faf2b2c86cef53a2cd94e429cc48b39e5e47f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAutomatedBackups", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f73db54eec5f0617783c449ed02cded22c971842e438cadb421a5cccbf4b936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367c3fd53045c64e0cc39bfd95adfc50f0e4d16223c397a7a1f3c897229fe07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="domainIamRoleName")
    def domain_iam_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainIamRoleName"))

    @domain_iam_role_name.setter
    def domain_iam_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fc3aa2372440c683ac62f87d150e129475d82374ae519e2383742a373f7abbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIamRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledCloudwatchLogsExports"))

    @enabled_cloudwatch_logs_exports.setter
    def enabled_cloudwatch_logs_exports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9ce3dcd91fb4a4111361d8799d8f3d8549078a31d97205b6a7fd077430f633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledCloudwatchLogsExports", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796d82bed1b26c5660d54a6fb2797bc151a216c82996a841b29bb36d66422bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4bbbe4b140f6c9a1c66919be00222f7bf7535b0f655eb760c62da90f97a5c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finalSnapshotIdentifier"))

    @final_snapshot_identifier.setter
    def final_snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab35f96f1c000f0b9ef1777510fdf864b068eb8285a2ccd7bd5f6d4889d1088c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "iamDatabaseAuthenticationEnabled"))

    @iam_database_authentication_enabled.setter
    def iam_database_authentication_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fafbda029b12f266d0c06dfab66b7099660237b5eb86a60a4b6f31161ab826c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamDatabaseAuthenticationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6a5964dce3299f04353296a54fb84bbad3215472ef3014298985d93f5b5354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ffd55f716b4289cd7b155908a81ea10d42853abc8fe7d5510b696828653bf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="identifierPrefix")
    def identifier_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifierPrefix"))

    @identifier_prefix.setter
    def identifier_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c426de9c2a38797b6597e1151f520386cc9866dbc99b6d60281d330afad91be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifierPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="instanceClass")
    def instance_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceClass"))

    @instance_class.setter
    def instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54aa5030f051921df653bf6f3522578f7908a898fc4190a030349ac81973fda0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c548dfe5eb53f54193d424bb4aeb482f2f412ab560538a7670cae69eb16b3c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c6eb38666d6ce29ec1094c8f10ee2a4e93d41d1a36099b896ad694c0594fdfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="licenseModel")
    def license_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseModel"))

    @license_model.setter
    def license_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c31fb794d038c8789c59013d680e2d0c9998dc10cefae4f8d745a72ad1b9d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseModel", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindow"))

    @maintenance_window.setter
    def maintenance_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3359d6335de4034b468f2b971762c755b0dc802508698d185f7510a4ca1da3f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="maxAllocatedStorage")
    def max_allocated_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAllocatedStorage"))

    @max_allocated_storage.setter
    def max_allocated_storage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e0e55fa849119d2aa89cc3f96ade4116c32ef6d7b396133316266e4ea6d37b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAllocatedStorage", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringInterval")
    def monitoring_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monitoringInterval"))

    @monitoring_interval.setter
    def monitoring_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19339b826c66414a49c7fd1e4418d5fe2aed1282e6520e07e91c4180c15ee617)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringInterval", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringRoleArn")
    def monitoring_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitoringRoleArn"))

    @monitoring_role_arn.setter
    def monitoring_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b116dc13403b86452669a0aaf34eea96d6e7b561257d19bfd803642e28a45853)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="multiAz")
    def multi_az(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "multiAz"))

    @multi_az.setter
    def multi_az(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af94c2f5fa7e6a873e1f80c12882b658117d0e2fb6cb8fa823abd6c358f6d590)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAz", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8a1b865887c8c415d3345033bd5d8f8c81bedbfcab4a55e112c2894fd0fa1a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ncharCharacterSetName")
    def nchar_character_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ncharCharacterSetName"))

    @nchar_character_set_name.setter
    def nchar_character_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777e819043303dd6e9a51bf75068013dd6b0736892ff156cf02150c228b179a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ncharCharacterSetName", value)

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a74358d8a2f526d641b9b05d6c75b67f7667fea6d7c4d094f808c60e19219770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value)

    @builtins.property
    @jsii.member(jsii_name="optionGroupName")
    def option_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optionGroupName"))

    @option_group_name.setter
    def option_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__413e2b9ab4f51ee13e8f7e9a3db51d7163e168217c0726321e2b74496ca602c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888a52706811ea93f6a80a69fb13d0bd07c5b3eb75d16a3f3ce1bbb59b84b0f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ca5d074b54a6183c458d4c28108558968a4d69055e66a3c4f35f94029f5fcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsEnabled")
    def performance_insights_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "performanceInsightsEnabled"))

    @performance_insights_enabled.setter
    def performance_insights_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__129f0e6803457d3e9d5af16e23ddd3ec1257b717a312e4e6158819effe3f997f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceInsightsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "performanceInsightsKmsKeyId"))

    @performance_insights_kms_key_id.setter
    def performance_insights_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cff63a4d351f6f63ca52f5b366e34940f04435e5a41573311bbfde7522c7719f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceInsightsKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "performanceInsightsRetentionPeriod"))

    @performance_insights_retention_period.setter
    def performance_insights_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a0d424fab1b5d501c90a7cc6f490751a76b45e0b9d568be1d936e07bb9e2c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceInsightsRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffb3270a754021169ec3146508514a7238c2ee81f8b09458adfbc0d1baaaa62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee48bc74d967806f3dd602b73a9896b11ffe338b1423ff8789bb3a9c9e376f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="replicaMode")
    def replica_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicaMode"))

    @replica_mode.setter
    def replica_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef45a4f119486ff3cbfb74c37078957f56d79e82b212eb147505a6b5b31af2c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaMode", value)

    @builtins.property
    @jsii.member(jsii_name="replicateSourceDb")
    def replicate_source_db(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicateSourceDb"))

    @replicate_source_db.setter
    def replicate_source_db(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a7e7eee068c0728be77e5d304039d274e279c1cfbe843bbd62145d6e530791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicateSourceDb", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupNames")
    def security_group_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupNames"))

    @security_group_names.setter
    def security_group_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__973a40fbaf8ff4eb29f98a3e5ed8f386ac00d74d123cb2a575a76148ae18c180)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupNames", value)

    @builtins.property
    @jsii.member(jsii_name="skipFinalSnapshot")
    def skip_final_snapshot(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "skipFinalSnapshot"))

    @skip_final_snapshot.setter
    def skip_final_snapshot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de6ea89e3b5d2f09065430e140526dd8864ac737be60afeb8623aa19797cdc25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipFinalSnapshot", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotIdentifier"))

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27262482bffd74224e036fd7fe6647c49112ecd9a2433d9f20cde8f84e754b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="storageEncrypted")
    def storage_encrypted(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "storageEncrypted"))

    @storage_encrypted.setter
    def storage_encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7545d67366a0fa8758af99bfca5eab7337c36a9cdf5a2119cf3fd29341bc32ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="storageThroughput")
    def storage_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageThroughput"))

    @storage_throughput.setter
    def storage_throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a19d70d94a4bebd6ec407a9f35c94728aeecc5a6ea22700a4f0d7b55ea90591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a1f0a0c9194321a2d4290335e6ba93e74013cf351d84ccde5b7494e7aebcc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ef4f2db37d4317462e6cdc5a079331b31359b273eabddd63ed0415a0fcbb1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d5da8c95aab5decc018b316cabbd063fdfb6307a9d4d9eb5c70402890b26f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07015002ac65a7db2a7cac6f24bf76681f521750611f475eba6b140dd980ce8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1708d499e7fa075cc085d3eb772bbea777856fa2608e57bb17c564acf6a2a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfa47d2bfce9362eca9f55d4b01b2229bb8be548af80d242ff60c4dd0c21b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="aws.dbInstance.DbInstanceBlueGreenUpdate",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class DbInstanceBlueGreenUpdate:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#enabled DbInstance#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61364c2c7a8cdc8fbaf8ebe4253b6a1307fc1d16385f0ce51f4a02a842026ca4)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#enabled DbInstance#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbInstanceBlueGreenUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbInstanceBlueGreenUpdateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbInstance.DbInstanceBlueGreenUpdateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__893470fef3e334188684d94cca942cdd76f87005e493cf405a5f13d2e7206373)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__941ec0e64d2dbf5e8913c7bd1562fd9c988f093fb4f8e5b952c5c21c4e6c4dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DbInstanceBlueGreenUpdate]:
        return typing.cast(typing.Optional[DbInstanceBlueGreenUpdate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DbInstanceBlueGreenUpdate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb3df096cc45087fe981d464aadb3f8bc839b4c871934a08c4beabb6781d8d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dbInstance.DbInstanceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_class": "instanceClass",
        "allocated_storage": "allocatedStorage",
        "allow_major_version_upgrade": "allowMajorVersionUpgrade",
        "apply_immediately": "applyImmediately",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "backup_retention_period": "backupRetentionPeriod",
        "backup_window": "backupWindow",
        "blue_green_update": "blueGreenUpdate",
        "ca_cert_identifier": "caCertIdentifier",
        "character_set_name": "characterSetName",
        "copy_tags_to_snapshot": "copyTagsToSnapshot",
        "customer_owned_ip_enabled": "customerOwnedIpEnabled",
        "custom_iam_instance_profile": "customIamInstanceProfile",
        "db_name": "dbName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "delete_automated_backups": "deleteAutomatedBackups",
        "deletion_protection": "deletionProtection",
        "domain": "domain",
        "domain_iam_role_name": "domainIamRoleName",
        "enabled_cloudwatch_logs_exports": "enabledCloudwatchLogsExports",
        "engine": "engine",
        "engine_version": "engineVersion",
        "final_snapshot_identifier": "finalSnapshotIdentifier",
        "iam_database_authentication_enabled": "iamDatabaseAuthenticationEnabled",
        "id": "id",
        "identifier": "identifier",
        "identifier_prefix": "identifierPrefix",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "license_model": "licenseModel",
        "maintenance_window": "maintenanceWindow",
        "max_allocated_storage": "maxAllocatedStorage",
        "monitoring_interval": "monitoringInterval",
        "monitoring_role_arn": "monitoringRoleArn",
        "multi_az": "multiAz",
        "name": "name",
        "nchar_character_set_name": "ncharCharacterSetName",
        "network_type": "networkType",
        "option_group_name": "optionGroupName",
        "parameter_group_name": "parameterGroupName",
        "password": "password",
        "performance_insights_enabled": "performanceInsightsEnabled",
        "performance_insights_kms_key_id": "performanceInsightsKmsKeyId",
        "performance_insights_retention_period": "performanceInsightsRetentionPeriod",
        "port": "port",
        "publicly_accessible": "publiclyAccessible",
        "replica_mode": "replicaMode",
        "replicate_source_db": "replicateSourceDb",
        "restore_to_point_in_time": "restoreToPointInTime",
        "s3_import": "s3Import",
        "security_group_names": "securityGroupNames",
        "skip_final_snapshot": "skipFinalSnapshot",
        "snapshot_identifier": "snapshotIdentifier",
        "storage_encrypted": "storageEncrypted",
        "storage_throughput": "storageThroughput",
        "storage_type": "storageType",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "timezone": "timezone",
        "username": "username",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class DbInstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        instance_class: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        backup_window: typing.Optional[builtins.str] = None,
        blue_green_update: typing.Optional[typing.Union[DbInstanceBlueGreenUpdate, typing.Dict[builtins.str, typing.Any]]] = None,
        ca_cert_identifier: typing.Optional[builtins.str] = None,
        character_set_name: typing.Optional[builtins.str] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        customer_owned_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_iam_instance_profile: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        delete_automated_backups: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        domain: typing.Optional[builtins.str] = None,
        domain_iam_role_name: typing.Optional[builtins.str] = None,
        enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identifier: typing.Optional[builtins.str] = None,
        identifier_prefix: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        license_model: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[builtins.str] = None,
        max_allocated_storage: typing.Optional[jsii.Number] = None,
        monitoring_interval: typing.Optional[jsii.Number] = None,
        monitoring_role_arn: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        nchar_character_set_name: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        option_group_name: typing.Optional[builtins.str] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
        performance_insights_retention_period: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        replica_mode: typing.Optional[builtins.str] = None,
        replicate_source_db: typing.Optional[builtins.str] = None,
        restore_to_point_in_time: typing.Optional[typing.Union["DbInstanceRestoreToPointInTime", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_import: typing.Optional[typing.Union["DbInstanceS3Import", typing.Dict[builtins.str, typing.Any]]] = None,
        security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        storage_throughput: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DbInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#instance_class DbInstance#instance_class}.
        :param allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#allocated_storage DbInstance#allocated_storage}.
        :param allow_major_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#allow_major_version_upgrade DbInstance#allow_major_version_upgrade}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#apply_immediately DbInstance#apply_immediately}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#auto_minor_version_upgrade DbInstance#auto_minor_version_upgrade}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#availability_zone DbInstance#availability_zone}.
        :param backup_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#backup_retention_period DbInstance#backup_retention_period}.
        :param backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#backup_window DbInstance#backup_window}.
        :param blue_green_update: blue_green_update block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#blue_green_update DbInstance#blue_green_update}
        :param ca_cert_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#ca_cert_identifier DbInstance#ca_cert_identifier}.
        :param character_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#character_set_name DbInstance#character_set_name}.
        :param copy_tags_to_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#copy_tags_to_snapshot DbInstance#copy_tags_to_snapshot}.
        :param customer_owned_ip_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#customer_owned_ip_enabled DbInstance#customer_owned_ip_enabled}.
        :param custom_iam_instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#custom_iam_instance_profile DbInstance#custom_iam_instance_profile}.
        :param db_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#db_name DbInstance#db_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#db_subnet_group_name DbInstance#db_subnet_group_name}.
        :param delete_automated_backups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#delete_automated_backups DbInstance#delete_automated_backups}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#deletion_protection DbInstance#deletion_protection}.
        :param domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#domain DbInstance#domain}.
        :param domain_iam_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#domain_iam_role_name DbInstance#domain_iam_role_name}.
        :param enabled_cloudwatch_logs_exports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#enabled_cloudwatch_logs_exports DbInstance#enabled_cloudwatch_logs_exports}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#engine DbInstance#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#engine_version DbInstance#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#final_snapshot_identifier DbInstance#final_snapshot_identifier}.
        :param iam_database_authentication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#iam_database_authentication_enabled DbInstance#iam_database_authentication_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#id DbInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#identifier DbInstance#identifier}.
        :param identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#identifier_prefix DbInstance#identifier_prefix}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#iops DbInstance#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#kms_key_id DbInstance#kms_key_id}.
        :param license_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#license_model DbInstance#license_model}.
        :param maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#maintenance_window DbInstance#maintenance_window}.
        :param max_allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#max_allocated_storage DbInstance#max_allocated_storage}.
        :param monitoring_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#monitoring_interval DbInstance#monitoring_interval}.
        :param monitoring_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#monitoring_role_arn DbInstance#monitoring_role_arn}.
        :param multi_az: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#multi_az DbInstance#multi_az}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#name DbInstance#name}.
        :param nchar_character_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#nchar_character_set_name DbInstance#nchar_character_set_name}.
        :param network_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#network_type DbInstance#network_type}.
        :param option_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#option_group_name DbInstance#option_group_name}.
        :param parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#parameter_group_name DbInstance#parameter_group_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#password DbInstance#password}.
        :param performance_insights_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_enabled DbInstance#performance_insights_enabled}.
        :param performance_insights_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_kms_key_id DbInstance#performance_insights_kms_key_id}.
        :param performance_insights_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_retention_period DbInstance#performance_insights_retention_period}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#port DbInstance#port}.
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#publicly_accessible DbInstance#publicly_accessible}.
        :param replica_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#replica_mode DbInstance#replica_mode}.
        :param replicate_source_db: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#replicate_source_db DbInstance#replicate_source_db}.
        :param restore_to_point_in_time: restore_to_point_in_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#restore_to_point_in_time DbInstance#restore_to_point_in_time}
        :param s3_import: s3_import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#s3_import DbInstance#s3_import}
        :param security_group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#security_group_names DbInstance#security_group_names}.
        :param skip_final_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#skip_final_snapshot DbInstance#skip_final_snapshot}.
        :param snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#snapshot_identifier DbInstance#snapshot_identifier}.
        :param storage_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_encrypted DbInstance#storage_encrypted}.
        :param storage_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_throughput DbInstance#storage_throughput}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_type DbInstance#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#tags DbInstance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#tags_all DbInstance#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#timeouts DbInstance#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#timezone DbInstance#timezone}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#username DbInstance#username}.
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#vpc_security_group_ids DbInstance#vpc_security_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(blue_green_update, dict):
            blue_green_update = DbInstanceBlueGreenUpdate(**blue_green_update)
        if isinstance(restore_to_point_in_time, dict):
            restore_to_point_in_time = DbInstanceRestoreToPointInTime(**restore_to_point_in_time)
        if isinstance(s3_import, dict):
            s3_import = DbInstanceS3Import(**s3_import)
        if isinstance(timeouts, dict):
            timeouts = DbInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf8196e485a24239cfd8c57a98adde3fda0ab73daac494da52c32e7569b0299a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_class", value=instance_class, expected_type=type_hints["instance_class"])
            check_type(argname="argument allocated_storage", value=allocated_storage, expected_type=type_hints["allocated_storage"])
            check_type(argname="argument allow_major_version_upgrade", value=allow_major_version_upgrade, expected_type=type_hints["allow_major_version_upgrade"])
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument backup_retention_period", value=backup_retention_period, expected_type=type_hints["backup_retention_period"])
            check_type(argname="argument backup_window", value=backup_window, expected_type=type_hints["backup_window"])
            check_type(argname="argument blue_green_update", value=blue_green_update, expected_type=type_hints["blue_green_update"])
            check_type(argname="argument ca_cert_identifier", value=ca_cert_identifier, expected_type=type_hints["ca_cert_identifier"])
            check_type(argname="argument character_set_name", value=character_set_name, expected_type=type_hints["character_set_name"])
            check_type(argname="argument copy_tags_to_snapshot", value=copy_tags_to_snapshot, expected_type=type_hints["copy_tags_to_snapshot"])
            check_type(argname="argument customer_owned_ip_enabled", value=customer_owned_ip_enabled, expected_type=type_hints["customer_owned_ip_enabled"])
            check_type(argname="argument custom_iam_instance_profile", value=custom_iam_instance_profile, expected_type=type_hints["custom_iam_instance_profile"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument delete_automated_backups", value=delete_automated_backups, expected_type=type_hints["delete_automated_backups"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument domain_iam_role_name", value=domain_iam_role_name, expected_type=type_hints["domain_iam_role_name"])
            check_type(argname="argument enabled_cloudwatch_logs_exports", value=enabled_cloudwatch_logs_exports, expected_type=type_hints["enabled_cloudwatch_logs_exports"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument final_snapshot_identifier", value=final_snapshot_identifier, expected_type=type_hints["final_snapshot_identifier"])
            check_type(argname="argument iam_database_authentication_enabled", value=iam_database_authentication_enabled, expected_type=type_hints["iam_database_authentication_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument identifier_prefix", value=identifier_prefix, expected_type=type_hints["identifier_prefix"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument license_model", value=license_model, expected_type=type_hints["license_model"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument max_allocated_storage", value=max_allocated_storage, expected_type=type_hints["max_allocated_storage"])
            check_type(argname="argument monitoring_interval", value=monitoring_interval, expected_type=type_hints["monitoring_interval"])
            check_type(argname="argument monitoring_role_arn", value=monitoring_role_arn, expected_type=type_hints["monitoring_role_arn"])
            check_type(argname="argument multi_az", value=multi_az, expected_type=type_hints["multi_az"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nchar_character_set_name", value=nchar_character_set_name, expected_type=type_hints["nchar_character_set_name"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument option_group_name", value=option_group_name, expected_type=type_hints["option_group_name"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument performance_insights_enabled", value=performance_insights_enabled, expected_type=type_hints["performance_insights_enabled"])
            check_type(argname="argument performance_insights_kms_key_id", value=performance_insights_kms_key_id, expected_type=type_hints["performance_insights_kms_key_id"])
            check_type(argname="argument performance_insights_retention_period", value=performance_insights_retention_period, expected_type=type_hints["performance_insights_retention_period"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument replica_mode", value=replica_mode, expected_type=type_hints["replica_mode"])
            check_type(argname="argument replicate_source_db", value=replicate_source_db, expected_type=type_hints["replicate_source_db"])
            check_type(argname="argument restore_to_point_in_time", value=restore_to_point_in_time, expected_type=type_hints["restore_to_point_in_time"])
            check_type(argname="argument s3_import", value=s3_import, expected_type=type_hints["s3_import"])
            check_type(argname="argument security_group_names", value=security_group_names, expected_type=type_hints["security_group_names"])
            check_type(argname="argument skip_final_snapshot", value=skip_final_snapshot, expected_type=type_hints["skip_final_snapshot"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument storage_throughput", value=storage_throughput, expected_type=type_hints["storage_throughput"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_class": instance_class,
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
        if allocated_storage is not None:
            self._values["allocated_storage"] = allocated_storage
        if allow_major_version_upgrade is not None:
            self._values["allow_major_version_upgrade"] = allow_major_version_upgrade
        if apply_immediately is not None:
            self._values["apply_immediately"] = apply_immediately
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if backup_window is not None:
            self._values["backup_window"] = backup_window
        if blue_green_update is not None:
            self._values["blue_green_update"] = blue_green_update
        if ca_cert_identifier is not None:
            self._values["ca_cert_identifier"] = ca_cert_identifier
        if character_set_name is not None:
            self._values["character_set_name"] = character_set_name
        if copy_tags_to_snapshot is not None:
            self._values["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if customer_owned_ip_enabled is not None:
            self._values["customer_owned_ip_enabled"] = customer_owned_ip_enabled
        if custom_iam_instance_profile is not None:
            self._values["custom_iam_instance_profile"] = custom_iam_instance_profile
        if db_name is not None:
            self._values["db_name"] = db_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if delete_automated_backups is not None:
            self._values["delete_automated_backups"] = delete_automated_backups
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if domain is not None:
            self._values["domain"] = domain
        if domain_iam_role_name is not None:
            self._values["domain_iam_role_name"] = domain_iam_role_name
        if enabled_cloudwatch_logs_exports is not None:
            self._values["enabled_cloudwatch_logs_exports"] = enabled_cloudwatch_logs_exports
        if engine is not None:
            self._values["engine"] = engine
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if final_snapshot_identifier is not None:
            self._values["final_snapshot_identifier"] = final_snapshot_identifier
        if iam_database_authentication_enabled is not None:
            self._values["iam_database_authentication_enabled"] = iam_database_authentication_enabled
        if id is not None:
            self._values["id"] = id
        if identifier is not None:
            self._values["identifier"] = identifier
        if identifier_prefix is not None:
            self._values["identifier_prefix"] = identifier_prefix
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if license_model is not None:
            self._values["license_model"] = license_model
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if max_allocated_storage is not None:
            self._values["max_allocated_storage"] = max_allocated_storage
        if monitoring_interval is not None:
            self._values["monitoring_interval"] = monitoring_interval
        if monitoring_role_arn is not None:
            self._values["monitoring_role_arn"] = monitoring_role_arn
        if multi_az is not None:
            self._values["multi_az"] = multi_az
        if name is not None:
            self._values["name"] = name
        if nchar_character_set_name is not None:
            self._values["nchar_character_set_name"] = nchar_character_set_name
        if network_type is not None:
            self._values["network_type"] = network_type
        if option_group_name is not None:
            self._values["option_group_name"] = option_group_name
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name
        if password is not None:
            self._values["password"] = password
        if performance_insights_enabled is not None:
            self._values["performance_insights_enabled"] = performance_insights_enabled
        if performance_insights_kms_key_id is not None:
            self._values["performance_insights_kms_key_id"] = performance_insights_kms_key_id
        if performance_insights_retention_period is not None:
            self._values["performance_insights_retention_period"] = performance_insights_retention_period
        if port is not None:
            self._values["port"] = port
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if replica_mode is not None:
            self._values["replica_mode"] = replica_mode
        if replicate_source_db is not None:
            self._values["replicate_source_db"] = replicate_source_db
        if restore_to_point_in_time is not None:
            self._values["restore_to_point_in_time"] = restore_to_point_in_time
        if s3_import is not None:
            self._values["s3_import"] = s3_import
        if security_group_names is not None:
            self._values["security_group_names"] = security_group_names
        if skip_final_snapshot is not None:
            self._values["skip_final_snapshot"] = skip_final_snapshot
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if storage_throughput is not None:
            self._values["storage_throughput"] = storage_throughput
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timezone is not None:
            self._values["timezone"] = timezone
        if username is not None:
            self._values["username"] = username
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

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
    def instance_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#instance_class DbInstance#instance_class}.'''
        result = self._values.get("instance_class")
        assert result is not None, "Required property 'instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#allocated_storage DbInstance#allocated_storage}.'''
        result = self._values.get("allocated_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#allow_major_version_upgrade DbInstance#allow_major_version_upgrade}.'''
        result = self._values.get("allow_major_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#apply_immediately DbInstance#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#auto_minor_version_upgrade DbInstance#auto_minor_version_upgrade}.'''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#availability_zone DbInstance#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#backup_retention_period DbInstance#backup_retention_period}.'''
        result = self._values.get("backup_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backup_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#backup_window DbInstance#backup_window}.'''
        result = self._values.get("backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def blue_green_update(self) -> typing.Optional[DbInstanceBlueGreenUpdate]:
        '''blue_green_update block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#blue_green_update DbInstance#blue_green_update}
        '''
        result = self._values.get("blue_green_update")
        return typing.cast(typing.Optional[DbInstanceBlueGreenUpdate], result)

    @builtins.property
    def ca_cert_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#ca_cert_identifier DbInstance#ca_cert_identifier}.'''
        result = self._values.get("ca_cert_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def character_set_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#character_set_name DbInstance#character_set_name}.'''
        result = self._values.get("character_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def copy_tags_to_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#copy_tags_to_snapshot DbInstance#copy_tags_to_snapshot}.'''
        result = self._values.get("copy_tags_to_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def customer_owned_ip_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#customer_owned_ip_enabled DbInstance#customer_owned_ip_enabled}.'''
        result = self._values.get("customer_owned_ip_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def custom_iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#custom_iam_instance_profile DbInstance#custom_iam_instance_profile}.'''
        result = self._values.get("custom_iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#db_name DbInstance#db_name}.'''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#db_subnet_group_name DbInstance#db_subnet_group_name}.'''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_automated_backups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#delete_automated_backups DbInstance#delete_automated_backups}.'''
        result = self._values.get("delete_automated_backups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#deletion_protection DbInstance#deletion_protection}.'''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#domain DbInstance#domain}.'''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_iam_role_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#domain_iam_role_name DbInstance#domain_iam_role_name}.'''
        result = self._values.get("domain_iam_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#enabled_cloudwatch_logs_exports DbInstance#enabled_cloudwatch_logs_exports}.'''
        result = self._values.get("enabled_cloudwatch_logs_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#engine DbInstance#engine}.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#engine_version DbInstance#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#final_snapshot_identifier DbInstance#final_snapshot_identifier}.'''
        result = self._values.get("final_snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_database_authentication_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#iam_database_authentication_enabled DbInstance#iam_database_authentication_enabled}.'''
        result = self._values.get("iam_database_authentication_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#id DbInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#identifier DbInstance#identifier}.'''
        result = self._values.get("identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#identifier_prefix DbInstance#identifier_prefix}.'''
        result = self._values.get("identifier_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#iops DbInstance#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#kms_key_id DbInstance#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_model(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#license_model DbInstance#license_model}.'''
        result = self._values.get("license_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#maintenance_window DbInstance#maintenance_window}.'''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#max_allocated_storage DbInstance#max_allocated_storage}.'''
        result = self._values.get("max_allocated_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitoring_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#monitoring_interval DbInstance#monitoring_interval}.'''
        result = self._values.get("monitoring_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitoring_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#monitoring_role_arn DbInstance#monitoring_role_arn}.'''
        result = self._values.get("monitoring_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#multi_az DbInstance#multi_az}.'''
        result = self._values.get("multi_az")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#name DbInstance#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nchar_character_set_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#nchar_character_set_name DbInstance#nchar_character_set_name}.'''
        result = self._values.get("nchar_character_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#network_type DbInstance#network_type}.'''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#option_group_name DbInstance#option_group_name}.'''
        result = self._values.get("option_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#parameter_group_name DbInstance#parameter_group_name}.'''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#password DbInstance#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def performance_insights_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_enabled DbInstance#performance_insights_enabled}.'''
        result = self._values.get("performance_insights_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def performance_insights_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_kms_key_id DbInstance#performance_insights_kms_key_id}.'''
        result = self._values.get("performance_insights_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def performance_insights_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#performance_insights_retention_period DbInstance#performance_insights_retention_period}.'''
        result = self._values.get("performance_insights_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#port DbInstance#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#publicly_accessible DbInstance#publicly_accessible}.'''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def replica_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#replica_mode DbInstance#replica_mode}.'''
        result = self._values.get("replica_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replicate_source_db(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#replicate_source_db DbInstance#replicate_source_db}.'''
        result = self._values.get("replicate_source_db")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_to_point_in_time(
        self,
    ) -> typing.Optional["DbInstanceRestoreToPointInTime"]:
        '''restore_to_point_in_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#restore_to_point_in_time DbInstance#restore_to_point_in_time}
        '''
        result = self._values.get("restore_to_point_in_time")
        return typing.cast(typing.Optional["DbInstanceRestoreToPointInTime"], result)

    @builtins.property
    def s3_import(self) -> typing.Optional["DbInstanceS3Import"]:
        '''s3_import block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#s3_import DbInstance#s3_import}
        '''
        result = self._values.get("s3_import")
        return typing.cast(typing.Optional["DbInstanceS3Import"], result)

    @builtins.property
    def security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#security_group_names DbInstance#security_group_names}.'''
        result = self._values.get("security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skip_final_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#skip_final_snapshot DbInstance#skip_final_snapshot}.'''
        result = self._values.get("skip_final_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#snapshot_identifier DbInstance#snapshot_identifier}.'''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_encrypted DbInstance#storage_encrypted}.'''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def storage_throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_throughput DbInstance#storage_throughput}.'''
        result = self._values.get("storage_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#storage_type DbInstance#storage_type}.'''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#tags DbInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#tags_all DbInstance#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DbInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#timeouts DbInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DbInstanceTimeouts"], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#timezone DbInstance#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#username DbInstance#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#vpc_security_group_ids DbInstance#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dbInstance.DbInstanceRestoreToPointInTime",
    jsii_struct_bases=[],
    name_mapping={
        "restore_time": "restoreTime",
        "source_db_instance_automated_backups_arn": "sourceDbInstanceAutomatedBackupsArn",
        "source_db_instance_identifier": "sourceDbInstanceIdentifier",
        "source_dbi_resource_id": "sourceDbiResourceId",
        "use_latest_restorable_time": "useLatestRestorableTime",
    },
)
class DbInstanceRestoreToPointInTime:
    def __init__(
        self,
        *,
        restore_time: typing.Optional[builtins.str] = None,
        source_db_instance_automated_backups_arn: typing.Optional[builtins.str] = None,
        source_db_instance_identifier: typing.Optional[builtins.str] = None,
        source_dbi_resource_id: typing.Optional[builtins.str] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param restore_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#restore_time DbInstance#restore_time}.
        :param source_db_instance_automated_backups_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_db_instance_automated_backups_arn DbInstance#source_db_instance_automated_backups_arn}.
        :param source_db_instance_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_db_instance_identifier DbInstance#source_db_instance_identifier}.
        :param source_dbi_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_dbi_resource_id DbInstance#source_dbi_resource_id}.
        :param use_latest_restorable_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#use_latest_restorable_time DbInstance#use_latest_restorable_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2edda118730a1a3ec74375346ba25535960c220769d77aad5faba67cc35db62)
            check_type(argname="argument restore_time", value=restore_time, expected_type=type_hints["restore_time"])
            check_type(argname="argument source_db_instance_automated_backups_arn", value=source_db_instance_automated_backups_arn, expected_type=type_hints["source_db_instance_automated_backups_arn"])
            check_type(argname="argument source_db_instance_identifier", value=source_db_instance_identifier, expected_type=type_hints["source_db_instance_identifier"])
            check_type(argname="argument source_dbi_resource_id", value=source_dbi_resource_id, expected_type=type_hints["source_dbi_resource_id"])
            check_type(argname="argument use_latest_restorable_time", value=use_latest_restorable_time, expected_type=type_hints["use_latest_restorable_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if restore_time is not None:
            self._values["restore_time"] = restore_time
        if source_db_instance_automated_backups_arn is not None:
            self._values["source_db_instance_automated_backups_arn"] = source_db_instance_automated_backups_arn
        if source_db_instance_identifier is not None:
            self._values["source_db_instance_identifier"] = source_db_instance_identifier
        if source_dbi_resource_id is not None:
            self._values["source_dbi_resource_id"] = source_dbi_resource_id
        if use_latest_restorable_time is not None:
            self._values["use_latest_restorable_time"] = use_latest_restorable_time

    @builtins.property
    def restore_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#restore_time DbInstance#restore_time}.'''
        result = self._values.get("restore_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_db_instance_automated_backups_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_db_instance_automated_backups_arn DbInstance#source_db_instance_automated_backups_arn}.'''
        result = self._values.get("source_db_instance_automated_backups_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_db_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_db_instance_identifier DbInstance#source_db_instance_identifier}.'''
        result = self._values.get("source_db_instance_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_dbi_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_dbi_resource_id DbInstance#source_dbi_resource_id}.'''
        result = self._values.get("source_dbi_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_latest_restorable_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#use_latest_restorable_time DbInstance#use_latest_restorable_time}.'''
        result = self._values.get("use_latest_restorable_time")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbInstanceRestoreToPointInTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbInstanceRestoreToPointInTimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbInstance.DbInstanceRestoreToPointInTimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a9226d819ebdbce9774bcedbbd62c9f65f079777958bc562e97f6f47a8ad8be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRestoreTime")
    def reset_restore_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreTime", []))

    @jsii.member(jsii_name="resetSourceDbInstanceAutomatedBackupsArn")
    def reset_source_db_instance_automated_backups_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDbInstanceAutomatedBackupsArn", []))

    @jsii.member(jsii_name="resetSourceDbInstanceIdentifier")
    def reset_source_db_instance_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDbInstanceIdentifier", []))

    @jsii.member(jsii_name="resetSourceDbiResourceId")
    def reset_source_dbi_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDbiResourceId", []))

    @jsii.member(jsii_name="resetUseLatestRestorableTime")
    def reset_use_latest_restorable_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLatestRestorableTime", []))

    @builtins.property
    @jsii.member(jsii_name="restoreTimeInput")
    def restore_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDbInstanceAutomatedBackupsArnInput")
    def source_db_instance_automated_backups_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDbInstanceAutomatedBackupsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDbInstanceIdentifierInput")
    def source_db_instance_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDbInstanceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDbiResourceIdInput")
    def source_dbi_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDbiResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useLatestRestorableTimeInput")
    def use_latest_restorable_time_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useLatestRestorableTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreTime")
    def restore_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreTime"))

    @restore_time.setter
    def restore_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ebb88b349853c5a0d446e7b5f1aeaa2fb09ff54eb6681db148a70f2dd140d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreTime", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDbInstanceAutomatedBackupsArn")
    def source_db_instance_automated_backups_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDbInstanceAutomatedBackupsArn"))

    @source_db_instance_automated_backups_arn.setter
    def source_db_instance_automated_backups_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40147406b7ab86aa7a95d2d6643deed2beebb6f98d2e9c37ee7494adfbff71e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDbInstanceAutomatedBackupsArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDbInstanceIdentifier")
    def source_db_instance_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDbInstanceIdentifier"))

    @source_db_instance_identifier.setter
    def source_db_instance_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4063a8fa9d9ba8cc4d666fc2843b5a7d65f14d12d5df2e395d6185f6fb200567)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDbInstanceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDbiResourceId")
    def source_dbi_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDbiResourceId"))

    @source_dbi_resource_id.setter
    def source_dbi_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d47e99cb3644bf4e23626e2ef87b7eb938cb4a45e21e1c3746b764e85e044b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDbiResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="useLatestRestorableTime")
    def use_latest_restorable_time(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useLatestRestorableTime"))

    @use_latest_restorable_time.setter
    def use_latest_restorable_time(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f46dd1d80ec5ae8600b138b070937a9203fbe64a1bff11f2fca1029981d043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLatestRestorableTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DbInstanceRestoreToPointInTime]:
        return typing.cast(typing.Optional[DbInstanceRestoreToPointInTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DbInstanceRestoreToPointInTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bdf7cf6b2b35ff047845e495b6840a74d0162e862fb5995f36e4f9fd24fb7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dbInstance.DbInstanceS3Import",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "ingestion_role": "ingestionRole",
        "source_engine": "sourceEngine",
        "source_engine_version": "sourceEngineVersion",
        "bucket_prefix": "bucketPrefix",
    },
)
class DbInstanceS3Import:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        ingestion_role: builtins.str,
        source_engine: builtins.str,
        source_engine_version: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#bucket_name DbInstance#bucket_name}.
        :param ingestion_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#ingestion_role DbInstance#ingestion_role}.
        :param source_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_engine DbInstance#source_engine}.
        :param source_engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_engine_version DbInstance#source_engine_version}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#bucket_prefix DbInstance#bucket_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50563dad1a123dc53482c816cc7f099f3429fbc531f7b076da5cb43a9a75d8d0)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument ingestion_role", value=ingestion_role, expected_type=type_hints["ingestion_role"])
            check_type(argname="argument source_engine", value=source_engine, expected_type=type_hints["source_engine"])
            check_type(argname="argument source_engine_version", value=source_engine_version, expected_type=type_hints["source_engine_version"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "ingestion_role": ingestion_role,
            "source_engine": source_engine,
            "source_engine_version": source_engine_version,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#bucket_name DbInstance#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ingestion_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#ingestion_role DbInstance#ingestion_role}.'''
        result = self._values.get("ingestion_role")
        assert result is not None, "Required property 'ingestion_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_engine(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_engine DbInstance#source_engine}.'''
        result = self._values.get("source_engine")
        assert result is not None, "Required property 'source_engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_engine_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#source_engine_version DbInstance#source_engine_version}.'''
        result = self._values.get("source_engine_version")
        assert result is not None, "Required property 'source_engine_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#bucket_prefix DbInstance#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbInstanceS3Import(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbInstanceS3ImportOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbInstance.DbInstanceS3ImportOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1f883554d713efd90219805f72cf54dddfbc4f165b395669de2ac6e8f3b8872)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="ingestionRoleInput")
    def ingestion_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingestionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEngineInput")
    def source_engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEngineVersionInput")
    def source_engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEngineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed38051f2263f461e62fb24f2e498de08158468008511f6e109616afa6745182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ebdf3a7f430bac99567c5abfac80f2b484dda6a21f658189038978ec3377b6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="ingestionRole")
    def ingestion_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ingestionRole"))

    @ingestion_role.setter
    def ingestion_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dc449af0c25106f4e9cc43271e5b7e953ae70e3f2811e0f7913481b8041044d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingestionRole", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEngine")
    def source_engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceEngine"))

    @source_engine.setter
    def source_engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05800cc8b6a8bc410d9405f7743221dfb5344b7de1b319abecda8275bb918d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEngine", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEngineVersion")
    def source_engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceEngineVersion"))

    @source_engine_version.setter
    def source_engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a7ae7a4e681f0a9cefccaa13b6be543e81a61713dd2629ef4ae1cd361750825)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEngineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DbInstanceS3Import]:
        return typing.cast(typing.Optional[DbInstanceS3Import], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DbInstanceS3Import]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748ab3f96907f47b73fec3fb88ccb9e1eab60ef7e3433b6887669872d579c759)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.dbInstance.DbInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DbInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#create DbInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#delete DbInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#update DbInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d42c0d0224ca20bea4953b59b88338f9c832643b4bb779e466eead4dde63d7d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#create DbInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#delete DbInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/db_instance#update DbInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DbInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DbInstanceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dbInstance.DbInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f46d10227c1a5c4bd497a2ed6d46a001258a6d8ee8b36646ae40d6e943d17b7a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__286b8e01dd7dd219a3fc430a6f08e6e837886317c732327444ead5ecb4ad192d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c0340da092c3f9a8a919802ca2117ee150c9e1c5f8d5e21107843ea3d84f7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__794933a21a63aaef20b15336d591d655b9f887025ef337e7de5f050e42566900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DbInstanceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DbInstanceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DbInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d4d0964ed443eb7ea8b0c0f42ae1bc4b33e55bef9d3f3c1ef54bc83c774723a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DbInstance",
    "DbInstanceBlueGreenUpdate",
    "DbInstanceBlueGreenUpdateOutputReference",
    "DbInstanceConfig",
    "DbInstanceRestoreToPointInTime",
    "DbInstanceRestoreToPointInTimeOutputReference",
    "DbInstanceS3Import",
    "DbInstanceS3ImportOutputReference",
    "DbInstanceTimeouts",
    "DbInstanceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__974b938e704a96b58ee5be2125171c90333b4ef887dbe3b5e7fc443438642914(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    instance_class: builtins.str,
    allocated_storage: typing.Optional[jsii.Number] = None,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    backup_window: typing.Optional[builtins.str] = None,
    blue_green_update: typing.Optional[typing.Union[DbInstanceBlueGreenUpdate, typing.Dict[builtins.str, typing.Any]]] = None,
    ca_cert_identifier: typing.Optional[builtins.str] = None,
    character_set_name: typing.Optional[builtins.str] = None,
    copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    customer_owned_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    custom_iam_instance_profile: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    delete_automated_backups: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    domain: typing.Optional[builtins.str] = None,
    domain_iam_role_name: typing.Optional[builtins.str] = None,
    enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    final_snapshot_identifier: typing.Optional[builtins.str] = None,
    iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    identifier: typing.Optional[builtins.str] = None,
    identifier_prefix: typing.Optional[builtins.str] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    license_model: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[builtins.str] = None,
    max_allocated_storage: typing.Optional[jsii.Number] = None,
    monitoring_interval: typing.Optional[jsii.Number] = None,
    monitoring_role_arn: typing.Optional[builtins.str] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    nchar_character_set_name: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    option_group_name: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
    performance_insights_retention_period: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    replica_mode: typing.Optional[builtins.str] = None,
    replicate_source_db: typing.Optional[builtins.str] = None,
    restore_to_point_in_time: typing.Optional[typing.Union[DbInstanceRestoreToPointInTime, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_import: typing.Optional[typing.Union[DbInstanceS3Import, typing.Dict[builtins.str, typing.Any]]] = None,
    security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    storage_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    storage_throughput: typing.Optional[jsii.Number] = None,
    storage_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DbInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__174817fb47090258d0ea94f02ec3fc129ee2229caf56e54798d9e0ef90979191(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2fc318d42beddd9e588c6f74e83d67bcb6b68b5de25636f380c0e58bd9ace9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a15a4fdce010abc86934015196b0fab26d9014ae10ae7491e32f3afb389bcf8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4f7986ccdf722f0fb34637410de6e57762fdc583a2f3890c9be561ff8308cf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9c291a2c6b074d5599da62796af2b1f8d84dc72537ce94190a2be4bb32849ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a1ae7e03f649630e3903cfff3cbd37b59548749014795c459037fed806c990(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddfcda28c661a9891a0e4dca715b689e986c1400e2019c2fe2f7438bab46077e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7b5da042d495de3090acda33858903ca23ceb1a1f8d7775dffe66542be8310(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd26c01f1013b2cb18b697b6ce6aff7d5dfa400cc6eaf749c09c9fbb7522541(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff26a52435cec93e06cb69d7de41b05dddcc1dade47f8b0a8304ea47e93abaaa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333f8d336d7685f93d4390249672e5d050411a0e045557a391519fb50198cf5b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d996bdfaff3c91618093db1543e2764d4a839b458c59bece223084e43efa78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48587c73a265ed06bd69bffed76fc2447631de6d4e52a636cc9e353343ece660(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbb2a608c6a5d0c76a8f5a8d4ca8f8114df6e46d064c04a7016cfa50c4e4a10e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac29582a4353ab19e158e655a27faf2b2c86cef53a2cd94e429cc48b39e5e47f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f73db54eec5f0617783c449ed02cded22c971842e438cadb421a5cccbf4b936(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367c3fd53045c64e0cc39bfd95adfc50f0e4d16223c397a7a1f3c897229fe07d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fc3aa2372440c683ac62f87d150e129475d82374ae519e2383742a373f7abbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9ce3dcd91fb4a4111361d8799d8f3d8549078a31d97205b6a7fd077430f633(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796d82bed1b26c5660d54a6fb2797bc151a216c82996a841b29bb36d66422bd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4bbbe4b140f6c9a1c66919be00222f7bf7535b0f655eb760c62da90f97a5c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab35f96f1c000f0b9ef1777510fdf864b068eb8285a2ccd7bd5f6d4889d1088c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafbda029b12f266d0c06dfab66b7099660237b5eb86a60a4b6f31161ab826c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6a5964dce3299f04353296a54fb84bbad3215472ef3014298985d93f5b5354(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ffd55f716b4289cd7b155908a81ea10d42853abc8fe7d5510b696828653bf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c426de9c2a38797b6597e1151f520386cc9866dbc99b6d60281d330afad91be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54aa5030f051921df653bf6f3522578f7908a898fc4190a030349ac81973fda0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c548dfe5eb53f54193d424bb4aeb482f2f412ab560538a7670cae69eb16b3c0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c6eb38666d6ce29ec1094c8f10ee2a4e93d41d1a36099b896ad694c0594fdfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c31fb794d038c8789c59013d680e2d0c9998dc10cefae4f8d745a72ad1b9d81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3359d6335de4034b468f2b971762c755b0dc802508698d185f7510a4ca1da3f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e0e55fa849119d2aa89cc3f96ade4116c32ef6d7b396133316266e4ea6d37b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19339b826c66414a49c7fd1e4418d5fe2aed1282e6520e07e91c4180c15ee617(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b116dc13403b86452669a0aaf34eea96d6e7b561257d19bfd803642e28a45853(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af94c2f5fa7e6a873e1f80c12882b658117d0e2fb6cb8fa823abd6c358f6d590(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a1b865887c8c415d3345033bd5d8f8c81bedbfcab4a55e112c2894fd0fa1a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777e819043303dd6e9a51bf75068013dd6b0736892ff156cf02150c228b179a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74358d8a2f526d641b9b05d6c75b67f7667fea6d7c4d094f808c60e19219770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__413e2b9ab4f51ee13e8f7e9a3db51d7163e168217c0726321e2b74496ca602c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888a52706811ea93f6a80a69fb13d0bd07c5b3eb75d16a3f3ce1bbb59b84b0f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ca5d074b54a6183c458d4c28108558968a4d69055e66a3c4f35f94029f5fcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129f0e6803457d3e9d5af16e23ddd3ec1257b717a312e4e6158819effe3f997f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff63a4d351f6f63ca52f5b366e34940f04435e5a41573311bbfde7522c7719f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a0d424fab1b5d501c90a7cc6f490751a76b45e0b9d568be1d936e07bb9e2c4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffb3270a754021169ec3146508514a7238c2ee81f8b09458adfbc0d1baaaa62(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee48bc74d967806f3dd602b73a9896b11ffe338b1423ff8789bb3a9c9e376f1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef45a4f119486ff3cbfb74c37078957f56d79e82b212eb147505a6b5b31af2c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a7e7eee068c0728be77e5d304039d274e279c1cfbe843bbd62145d6e530791(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__973a40fbaf8ff4eb29f98a3e5ed8f386ac00d74d123cb2a575a76148ae18c180(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6ea89e3b5d2f09065430e140526dd8864ac737be60afeb8623aa19797cdc25(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27262482bffd74224e036fd7fe6647c49112ecd9a2433d9f20cde8f84e754b18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7545d67366a0fa8758af99bfca5eab7337c36a9cdf5a2119cf3fd29341bc32ba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a19d70d94a4bebd6ec407a9f35c94728aeecc5a6ea22700a4f0d7b55ea90591(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a1f0a0c9194321a2d4290335e6ba93e74013cf351d84ccde5b7494e7aebcc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ef4f2db37d4317462e6cdc5a079331b31359b273eabddd63ed0415a0fcbb1c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d5da8c95aab5decc018b316cabbd063fdfb6307a9d4d9eb5c70402890b26f8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07015002ac65a7db2a7cac6f24bf76681f521750611f475eba6b140dd980ce8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1708d499e7fa075cc085d3eb772bbea777856fa2608e57bb17c564acf6a2a16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfa47d2bfce9362eca9f55d4b01b2229bb8be548af80d242ff60c4dd0c21b18(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61364c2c7a8cdc8fbaf8ebe4253b6a1307fc1d16385f0ce51f4a02a842026ca4(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893470fef3e334188684d94cca942cdd76f87005e493cf405a5f13d2e7206373(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941ec0e64d2dbf5e8913c7bd1562fd9c988f093fb4f8e5b952c5c21c4e6c4dcb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb3df096cc45087fe981d464aadb3f8bc839b4c871934a08c4beabb6781d8d8(
    value: typing.Optional[DbInstanceBlueGreenUpdate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8196e485a24239cfd8c57a98adde3fda0ab73daac494da52c32e7569b0299a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_class: builtins.str,
    allocated_storage: typing.Optional[jsii.Number] = None,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    backup_window: typing.Optional[builtins.str] = None,
    blue_green_update: typing.Optional[typing.Union[DbInstanceBlueGreenUpdate, typing.Dict[builtins.str, typing.Any]]] = None,
    ca_cert_identifier: typing.Optional[builtins.str] = None,
    character_set_name: typing.Optional[builtins.str] = None,
    copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    customer_owned_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    custom_iam_instance_profile: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    delete_automated_backups: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    domain: typing.Optional[builtins.str] = None,
    domain_iam_role_name: typing.Optional[builtins.str] = None,
    enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    final_snapshot_identifier: typing.Optional[builtins.str] = None,
    iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    identifier: typing.Optional[builtins.str] = None,
    identifier_prefix: typing.Optional[builtins.str] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    license_model: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[builtins.str] = None,
    max_allocated_storage: typing.Optional[jsii.Number] = None,
    monitoring_interval: typing.Optional[jsii.Number] = None,
    monitoring_role_arn: typing.Optional[builtins.str] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    nchar_character_set_name: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    option_group_name: typing.Optional[builtins.str] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
    performance_insights_retention_period: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    replica_mode: typing.Optional[builtins.str] = None,
    replicate_source_db: typing.Optional[builtins.str] = None,
    restore_to_point_in_time: typing.Optional[typing.Union[DbInstanceRestoreToPointInTime, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_import: typing.Optional[typing.Union[DbInstanceS3Import, typing.Dict[builtins.str, typing.Any]]] = None,
    security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    storage_encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    storage_throughput: typing.Optional[jsii.Number] = None,
    storage_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DbInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2edda118730a1a3ec74375346ba25535960c220769d77aad5faba67cc35db62(
    *,
    restore_time: typing.Optional[builtins.str] = None,
    source_db_instance_automated_backups_arn: typing.Optional[builtins.str] = None,
    source_db_instance_identifier: typing.Optional[builtins.str] = None,
    source_dbi_resource_id: typing.Optional[builtins.str] = None,
    use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9226d819ebdbce9774bcedbbd62c9f65f079777958bc562e97f6f47a8ad8be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ebb88b349853c5a0d446e7b5f1aeaa2fb09ff54eb6681db148a70f2dd140d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40147406b7ab86aa7a95d2d6643deed2beebb6f98d2e9c37ee7494adfbff71e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4063a8fa9d9ba8cc4d666fc2843b5a7d65f14d12d5df2e395d6185f6fb200567(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d47e99cb3644bf4e23626e2ef87b7eb938cb4a45e21e1c3746b764e85e044b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f46dd1d80ec5ae8600b138b070937a9203fbe64a1bff11f2fca1029981d043(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bdf7cf6b2b35ff047845e495b6840a74d0162e862fb5995f36e4f9fd24fb7f(
    value: typing.Optional[DbInstanceRestoreToPointInTime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50563dad1a123dc53482c816cc7f099f3429fbc531f7b076da5cb43a9a75d8d0(
    *,
    bucket_name: builtins.str,
    ingestion_role: builtins.str,
    source_engine: builtins.str,
    source_engine_version: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1f883554d713efd90219805f72cf54dddfbc4f165b395669de2ac6e8f3b8872(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed38051f2263f461e62fb24f2e498de08158468008511f6e109616afa6745182(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ebdf3a7f430bac99567c5abfac80f2b484dda6a21f658189038978ec3377b6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dc449af0c25106f4e9cc43271e5b7e953ae70e3f2811e0f7913481b8041044d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05800cc8b6a8bc410d9405f7743221dfb5344b7de1b319abecda8275bb918d63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a7ae7a4e681f0a9cefccaa13b6be543e81a61713dd2629ef4ae1cd361750825(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748ab3f96907f47b73fec3fb88ccb9e1eab60ef7e3433b6887669872d579c759(
    value: typing.Optional[DbInstanceS3Import],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d42c0d0224ca20bea4953b59b88338f9c832643b4bb779e466eead4dde63d7d(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f46d10227c1a5c4bd497a2ed6d46a001258a6d8ee8b36646ae40d6e943d17b7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286b8e01dd7dd219a3fc430a6f08e6e837886317c732327444ead5ecb4ad192d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c0340da092c3f9a8a919802ca2117ee150c9e1c5f8d5e21107843ea3d84f7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__794933a21a63aaef20b15336d591d655b9f887025ef337e7de5f050e42566900(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d4d0964ed443eb7ea8b0c0f42ae1bc4b33e55bef9d3f3c1ef54bc83c774723a(
    value: typing.Optional[typing.Union[DbInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
