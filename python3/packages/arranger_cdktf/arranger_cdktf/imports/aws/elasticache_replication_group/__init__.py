'''
# `aws_elasticache_replication_group`

Refer to the Terraform Registory for docs: [`aws_elasticache_replication_group`](https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group).
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


class ElasticacheReplicationGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group aws_elasticache_replication_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        replication_group_id: builtins.str,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[builtins.str] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_mode: typing.Optional[typing.Union["ElasticacheReplicationGroupClusterMode", typing.Dict[builtins.str, typing.Any]]] = None,
        data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        global_replication_group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_delivery_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticacheReplicationGroupLogDeliveryConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        maintenance_window: typing.Optional[builtins.str] = None,
        multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        node_type: typing.Optional[builtins.str] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        number_cache_clusters: typing.Optional[jsii.Number] = None,
        num_cache_clusters: typing.Optional[jsii.Number] = None,
        num_node_groups: typing.Optional[jsii.Number] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_cache_cluster_azs: typing.Optional[typing.Sequence[builtins.str]] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
        replication_group_description: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ElasticacheReplicationGroupTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group aws_elasticache_replication_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param replication_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replication_group_id ElasticacheReplicationGroup#replication_group_id}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#apply_immediately ElasticacheReplicationGroup#apply_immediately}.
        :param at_rest_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#at_rest_encryption_enabled ElasticacheReplicationGroup#at_rest_encryption_enabled}.
        :param auth_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#auth_token ElasticacheReplicationGroup#auth_token}.
        :param automatic_failover_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#automatic_failover_enabled ElasticacheReplicationGroup#automatic_failover_enabled}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#auto_minor_version_upgrade ElasticacheReplicationGroup#auto_minor_version_upgrade}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#availability_zones ElasticacheReplicationGroup#availability_zones}.
        :param cluster_mode: cluster_mode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#cluster_mode ElasticacheReplicationGroup#cluster_mode}
        :param data_tiering_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#data_tiering_enabled ElasticacheReplicationGroup#data_tiering_enabled}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#description ElasticacheReplicationGroup#description}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#engine ElasticacheReplicationGroup#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#engine_version ElasticacheReplicationGroup#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#final_snapshot_identifier ElasticacheReplicationGroup#final_snapshot_identifier}.
        :param global_replication_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#global_replication_group_id ElasticacheReplicationGroup#global_replication_group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#id ElasticacheReplicationGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#kms_key_id ElasticacheReplicationGroup#kms_key_id}.
        :param log_delivery_configuration: log_delivery_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_delivery_configuration ElasticacheReplicationGroup#log_delivery_configuration}
        :param maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#maintenance_window ElasticacheReplicationGroup#maintenance_window}.
        :param multi_az_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#multi_az_enabled ElasticacheReplicationGroup#multi_az_enabled}.
        :param node_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#node_type ElasticacheReplicationGroup#node_type}.
        :param notification_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#notification_topic_arn ElasticacheReplicationGroup#notification_topic_arn}.
        :param number_cache_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#number_cache_clusters ElasticacheReplicationGroup#number_cache_clusters}.
        :param num_cache_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_cache_clusters ElasticacheReplicationGroup#num_cache_clusters}.
        :param num_node_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_node_groups ElasticacheReplicationGroup#num_node_groups}.
        :param parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#parameter_group_name ElasticacheReplicationGroup#parameter_group_name}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#port ElasticacheReplicationGroup#port}.
        :param preferred_cache_cluster_azs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#preferred_cache_cluster_azs ElasticacheReplicationGroup#preferred_cache_cluster_azs}.
        :param replicas_per_node_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replicas_per_node_group ElasticacheReplicationGroup#replicas_per_node_group}.
        :param replication_group_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replication_group_description ElasticacheReplicationGroup#replication_group_description}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#security_group_ids ElasticacheReplicationGroup#security_group_ids}.
        :param security_group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#security_group_names ElasticacheReplicationGroup#security_group_names}.
        :param snapshot_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_arns ElasticacheReplicationGroup#snapshot_arns}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_name ElasticacheReplicationGroup#snapshot_name}.
        :param snapshot_retention_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_retention_limit ElasticacheReplicationGroup#snapshot_retention_limit}.
        :param snapshot_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_window ElasticacheReplicationGroup#snapshot_window}.
        :param subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#subnet_group_name ElasticacheReplicationGroup#subnet_group_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#tags ElasticacheReplicationGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#tags_all ElasticacheReplicationGroup#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#timeouts ElasticacheReplicationGroup#timeouts}
        :param transit_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#transit_encryption_enabled ElasticacheReplicationGroup#transit_encryption_enabled}.
        :param user_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#user_group_ids ElasticacheReplicationGroup#user_group_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05ea70d7fd705c24106460c79b86111b36bd4de6297121bade25532950bab4a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElasticacheReplicationGroupConfig(
            replication_group_id=replication_group_id,
            apply_immediately=apply_immediately,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            auth_token=auth_token,
            automatic_failover_enabled=automatic_failover_enabled,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zones=availability_zones,
            cluster_mode=cluster_mode,
            data_tiering_enabled=data_tiering_enabled,
            description=description,
            engine=engine,
            engine_version=engine_version,
            final_snapshot_identifier=final_snapshot_identifier,
            global_replication_group_id=global_replication_group_id,
            id=id,
            kms_key_id=kms_key_id,
            log_delivery_configuration=log_delivery_configuration,
            maintenance_window=maintenance_window,
            multi_az_enabled=multi_az_enabled,
            node_type=node_type,
            notification_topic_arn=notification_topic_arn,
            number_cache_clusters=number_cache_clusters,
            num_cache_clusters=num_cache_clusters,
            num_node_groups=num_node_groups,
            parameter_group_name=parameter_group_name,
            port=port,
            preferred_cache_cluster_azs=preferred_cache_cluster_azs,
            replicas_per_node_group=replicas_per_node_group,
            replication_group_description=replication_group_description,
            security_group_ids=security_group_ids,
            security_group_names=security_group_names,
            snapshot_arns=snapshot_arns,
            snapshot_name=snapshot_name,
            snapshot_retention_limit=snapshot_retention_limit,
            snapshot_window=snapshot_window,
            subnet_group_name=subnet_group_name,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            transit_encryption_enabled=transit_encryption_enabled,
            user_group_ids=user_group_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putClusterMode")
    def put_cluster_mode(
        self,
        *,
        num_node_groups: typing.Optional[jsii.Number] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_node_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_node_groups ElasticacheReplicationGroup#num_node_groups}.
        :param replicas_per_node_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replicas_per_node_group ElasticacheReplicationGroup#replicas_per_node_group}.
        '''
        value = ElasticacheReplicationGroupClusterMode(
            num_node_groups=num_node_groups,
            replicas_per_node_group=replicas_per_node_group,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterMode", [value]))

    @jsii.member(jsii_name="putLogDeliveryConfiguration")
    def put_log_delivery_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticacheReplicationGroupLogDeliveryConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed946685cc984161a0ea9f4711015a86807fe92ec6a22cf579de10f14b344abb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogDeliveryConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#create ElasticacheReplicationGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#delete ElasticacheReplicationGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#update ElasticacheReplicationGroup#update}.
        '''
        value = ElasticacheReplicationGroupTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAtRestEncryptionEnabled")
    def reset_at_rest_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAtRestEncryptionEnabled", []))

    @jsii.member(jsii_name="resetAuthToken")
    def reset_auth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthToken", []))

    @jsii.member(jsii_name="resetAutomaticFailoverEnabled")
    def reset_automatic_failover_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticFailoverEnabled", []))

    @jsii.member(jsii_name="resetAutoMinorVersionUpgrade")
    def reset_auto_minor_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMinorVersionUpgrade", []))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetClusterMode")
    def reset_cluster_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterMode", []))

    @jsii.member(jsii_name="resetDataTieringEnabled")
    def reset_data_tiering_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataTieringEnabled", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetFinalSnapshotIdentifier")
    def reset_final_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFinalSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetGlobalReplicationGroupId")
    def reset_global_replication_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalReplicationGroupId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetLogDeliveryConfiguration")
    def reset_log_delivery_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDeliveryConfiguration", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetMultiAzEnabled")
    def reset_multi_az_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiAzEnabled", []))

    @jsii.member(jsii_name="resetNodeType")
    def reset_node_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeType", []))

    @jsii.member(jsii_name="resetNotificationTopicArn")
    def reset_notification_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationTopicArn", []))

    @jsii.member(jsii_name="resetNumberCacheClusters")
    def reset_number_cache_clusters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberCacheClusters", []))

    @jsii.member(jsii_name="resetNumCacheClusters")
    def reset_num_cache_clusters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumCacheClusters", []))

    @jsii.member(jsii_name="resetNumNodeGroups")
    def reset_num_node_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumNodeGroups", []))

    @jsii.member(jsii_name="resetParameterGroupName")
    def reset_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterGroupName", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPreferredCacheClusterAzs")
    def reset_preferred_cache_cluster_azs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredCacheClusterAzs", []))

    @jsii.member(jsii_name="resetReplicasPerNodeGroup")
    def reset_replicas_per_node_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicasPerNodeGroup", []))

    @jsii.member(jsii_name="resetReplicationGroupDescription")
    def reset_replication_group_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationGroupDescription", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSecurityGroupNames")
    def reset_security_group_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupNames", []))

    @jsii.member(jsii_name="resetSnapshotArns")
    def reset_snapshot_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotArns", []))

    @jsii.member(jsii_name="resetSnapshotName")
    def reset_snapshot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotName", []))

    @jsii.member(jsii_name="resetSnapshotRetentionLimit")
    def reset_snapshot_retention_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotRetentionLimit", []))

    @jsii.member(jsii_name="resetSnapshotWindow")
    def reset_snapshot_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotWindow", []))

    @jsii.member(jsii_name="resetSubnetGroupName")
    def reset_subnet_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetGroupName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransitEncryptionEnabled")
    def reset_transit_encryption_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitEncryptionEnabled", []))

    @jsii.member(jsii_name="resetUserGroupIds")
    def reset_user_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserGroupIds", []))

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
    @jsii.member(jsii_name="clusterEnabled")
    def cluster_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "clusterEnabled"))

    @builtins.property
    @jsii.member(jsii_name="clusterMode")
    def cluster_mode(self) -> "ElasticacheReplicationGroupClusterModeOutputReference":
        return typing.cast("ElasticacheReplicationGroupClusterModeOutputReference", jsii.get(self, "clusterMode"))

    @builtins.property
    @jsii.member(jsii_name="configurationEndpointAddress")
    def configuration_endpoint_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionActual")
    def engine_version_actual(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersionActual"))

    @builtins.property
    @jsii.member(jsii_name="logDeliveryConfiguration")
    def log_delivery_configuration(
        self,
    ) -> "ElasticacheReplicationGroupLogDeliveryConfigurationList":
        return typing.cast("ElasticacheReplicationGroupLogDeliveryConfigurationList", jsii.get(self, "logDeliveryConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="memberClusters")
    def member_clusters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "memberClusters"))

    @builtins.property
    @jsii.member(jsii_name="primaryEndpointAddress")
    def primary_endpoint_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="readerEndpointAddress")
    def reader_endpoint_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readerEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ElasticacheReplicationGroupTimeoutsOutputReference":
        return typing.cast("ElasticacheReplicationGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediatelyInput")
    def apply_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "applyImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabledInput")
    def at_rest_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "atRestEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticFailoverEnabledInput")
    def automatic_failover_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "automaticFailoverEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgradeInput")
    def auto_minor_version_upgrade_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoMinorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterModeInput")
    def cluster_mode_input(
        self,
    ) -> typing.Optional["ElasticacheReplicationGroupClusterMode"]:
        return typing.cast(typing.Optional["ElasticacheReplicationGroupClusterMode"], jsii.get(self, "clusterModeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTieringEnabledInput")
    def data_tiering_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "dataTieringEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

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
    @jsii.member(jsii_name="globalReplicationGroupIdInput")
    def global_replication_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logDeliveryConfigurationInput")
    def log_delivery_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticacheReplicationGroupLogDeliveryConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticacheReplicationGroupLogDeliveryConfiguration"]]], jsii.get(self, "logDeliveryConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="multiAzEnabledInput")
    def multi_az_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "multiAzEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeInput")
    def node_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArnInput")
    def notification_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="numberCacheClustersInput")
    def number_cache_clusters_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberCacheClustersInput"))

    @builtins.property
    @jsii.member(jsii_name="numCacheClustersInput")
    def num_cache_clusters_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numCacheClustersInput"))

    @builtins.property
    @jsii.member(jsii_name="numNodeGroupsInput")
    def num_node_groups_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numNodeGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterGroupNameInput")
    def parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredCacheClusterAzsInput")
    def preferred_cache_cluster_azs_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredCacheClusterAzsInput"))

    @builtins.property
    @jsii.member(jsii_name="replicasPerNodeGroupInput")
    def replicas_per_node_group_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasPerNodeGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationGroupDescriptionInput")
    def replication_group_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationGroupDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationGroupIdInput")
    def replication_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupNamesInput")
    def security_group_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotArnsInput")
    def snapshot_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotRetentionLimitInput")
    def snapshot_retention_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotWindowInput")
    def snapshot_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetGroupNameInput")
    def subnet_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetGroupNameInput"))

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
    ) -> typing.Optional[typing.Union["ElasticacheReplicationGroupTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ElasticacheReplicationGroupTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabledInput")
    def transit_encryption_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "transitEncryptionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupIdsInput")
    def user_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userGroupIdsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e69fec3d94d3e189578b0252053ad73681e657e7e45b0a5df61f7fcd3864151b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyImmediately", value)

    @builtins.property
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "atRestEncryptionEnabled"))

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cdbba326ad40fe190ad6e2dbddca4fa9b4751334200bb12aee592cc35e54da0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a210cf11c2e43c8e9ada7789d697b3e2d1c1cf4b5590df07b7f822252682cf43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="automaticFailoverEnabled")
    def automatic_failover_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "automaticFailoverEnabled"))

    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f94af344a944c7ed3de186569e5a8fa1f8a115dd100589ddc5a6cb6ad3209a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticFailoverEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9946ca3a0cdaa6277eb01532dcc56fecd3254d8acadd3d12e1bf3e50cd5c224c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a9bd4fd08eba2c7a3330d74c8afcec66eeeaa9cf8c319f76103ed5db62916ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="dataTieringEnabled")
    def data_tiering_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "dataTieringEnabled"))

    @data_tiering_enabled.setter
    def data_tiering_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22532caf69c7947057cdc59e6e397c09ca331ac469c87d009a0fbf6d141edb85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTieringEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f468087e7caa99dbfb1f0f0fcd240bd5a1a842f8277312d8acb28d943f1775c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a8b2bdd49028693cc2c9c83a384da832c51c12d8fd282a25536ab45ee37a0c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14f7137b2de79963f5db534f791700efaa706b509aedeb8363dbf87930df4fac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finalSnapshotIdentifier"))

    @final_snapshot_identifier.setter
    def final_snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83dc52d401c49cad9ffc48353ea792942147ee7107787d4ff8baa0d066ee9ca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupId")
    def global_replication_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalReplicationGroupId"))

    @global_replication_group_id.setter
    def global_replication_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1185a779eefa4a13636d26a255fa38b1e8f56d68283a298bfeaabe3d0d5164ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalReplicationGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d329670610fd30bb47ed96a5ef1094efe8ae2f9abf8d68894f5768a65625b496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e08f003ee8568236132ac8b8d6a364ad24ade081b01fad908ab954810777b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindow"))

    @maintenance_window.setter
    def maintenance_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9af9c2cefb30ab5295370fc4e67fff1f0ab64b289923d3db5ae2caab11dff1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="multiAzEnabled")
    def multi_az_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "multiAzEnabled"))

    @multi_az_enabled.setter
    def multi_az_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6ebf68762164d999175912f153a2648e28e6a63f275a1deacb0073c3583d01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAzEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca8cc3e3d1f78231ff5a1b01930ce5dd1cd5fd69640dde460fe1603c76ab680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d84f1335b137e2ebfe77accf6b0bb9a7648d24f48ac737132c0cf6517ac0c0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="numberCacheClusters")
    def number_cache_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberCacheClusters"))

    @number_cache_clusters.setter
    def number_cache_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6d54f22f4a9adfacd2fdb3deb3ee6771c968cbe63d9cdd20bc8106f6559e20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberCacheClusters", value)

    @builtins.property
    @jsii.member(jsii_name="numCacheClusters")
    def num_cache_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numCacheClusters"))

    @num_cache_clusters.setter
    def num_cache_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a129e8196d6475951ccd2eae707c09ac07767faa5c5a22ad14f06d85a8e832ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numCacheClusters", value)

    @builtins.property
    @jsii.member(jsii_name="numNodeGroups")
    def num_node_groups(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numNodeGroups"))

    @num_node_groups.setter
    def num_node_groups(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f5297a5ae2244c483816981969d3134d08fc93c4ec3a65aec969d48ff2c2e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numNodeGroups", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

    @parameter_group_name.setter
    def parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99261d56d49ad86ba1806b8ded69f5cf4f8c210520d2cc0950f65f93b5a14832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3570395f11326ad001b641c814a08d497e208abeaa6536d7e470ba9b23e48804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredCacheClusterAzs")
    def preferred_cache_cluster_azs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "preferredCacheClusterAzs"))

    @preferred_cache_cluster_azs.setter
    def preferred_cache_cluster_azs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4f193a7adeb70bfeff9e9c209bc5ce37dd75c91797e82976a4a2a60dadc025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredCacheClusterAzs", value)

    @builtins.property
    @jsii.member(jsii_name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicasPerNodeGroup"))

    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57e9b3ff7a8ecc72c38c8c105251a6a280c6a71c715c67d1a4cdc9fcaf1b2c9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicasPerNodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="replicationGroupDescription")
    def replication_group_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationGroupDescription"))

    @replication_group_description.setter
    def replication_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab208c6b695692c759c9fcf158b97bbede5f72e707e4a8ec36a375b1bf7b71c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="replicationGroupId")
    def replication_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationGroupId"))

    @replication_group_id.setter
    def replication_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9835b136b72a6915612dce56ea3bb6dcb25f8ff42a163d091217e451f1f8f17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd277ae68be3dcace1ab4b1a485d1394ffceffe9672772a66be74c1a49f7503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupNames")
    def security_group_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupNames"))

    @security_group_names.setter
    def security_group_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0999a4549564991de6c0b8419778ae0f5129b051687db4425b875680a3abbb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupNames", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotArns")
    def snapshot_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "snapshotArns"))

    @snapshot_arns.setter
    def snapshot_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9441942c4847a665ae91e07bd40e1e69109c6338b80ebacc2a6e8a2237391c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArns", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baf8b66cb809fe621582550bd73baa3d80ed89486fba12336e05760b8ea8289b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c7c4d3ac6fffa7239a313499ef9e8abe1a9fb315642fc711457c572ff12b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotWindow")
    def snapshot_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotWindow"))

    @snapshot_window.setter
    def snapshot_window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646f5373b5c73cc5474397f1ab7e54237233d6e73cd5353576e3f8c1c1fd139f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotWindow", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f96df803484b106f544b3090589e2467da421e4e5a10438da0607d8fae65e5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473dd80cbda23603397a1e18fbf71d31ddb6f3b272ea6548f2989e5f0c5a1dcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdda69ca97fa32f86fffa133b967d5c6f8206973aaf4878ce7b44b8fb0b6206a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75cb61ee1ddeb81949fb7f1a147f256288e9ac5b70b4603135906a9f1502abd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryptionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="userGroupIds")
    def user_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "userGroupIds"))

    @user_group_ids.setter
    def user_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da4208cf3b32435e8809b6c7648eb222c84221ad6ab4b46241fa6b71c25b6a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupIds", value)


@jsii.data_type(
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupClusterMode",
    jsii_struct_bases=[],
    name_mapping={
        "num_node_groups": "numNodeGroups",
        "replicas_per_node_group": "replicasPerNodeGroup",
    },
)
class ElasticacheReplicationGroupClusterMode:
    def __init__(
        self,
        *,
        num_node_groups: typing.Optional[jsii.Number] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param num_node_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_node_groups ElasticacheReplicationGroup#num_node_groups}.
        :param replicas_per_node_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replicas_per_node_group ElasticacheReplicationGroup#replicas_per_node_group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1392afe960e4f346cd42271383314164bc2b98edc5d1c46013711b6547888c)
            check_type(argname="argument num_node_groups", value=num_node_groups, expected_type=type_hints["num_node_groups"])
            check_type(argname="argument replicas_per_node_group", value=replicas_per_node_group, expected_type=type_hints["replicas_per_node_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if num_node_groups is not None:
            self._values["num_node_groups"] = num_node_groups
        if replicas_per_node_group is not None:
            self._values["replicas_per_node_group"] = replicas_per_node_group

    @builtins.property
    def num_node_groups(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_node_groups ElasticacheReplicationGroup#num_node_groups}.'''
        result = self._values.get("num_node_groups")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replicas_per_node_group(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replicas_per_node_group ElasticacheReplicationGroup#replicas_per_node_group}.'''
        result = self._values.get("replicas_per_node_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticacheReplicationGroupClusterMode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticacheReplicationGroupClusterModeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupClusterModeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd90a5fb04477fe3fb37e1abb9a9ffc4dfe7ade811140c90c6d714174c01e11b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNumNodeGroups")
    def reset_num_node_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumNodeGroups", []))

    @jsii.member(jsii_name="resetReplicasPerNodeGroup")
    def reset_replicas_per_node_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicasPerNodeGroup", []))

    @builtins.property
    @jsii.member(jsii_name="numNodeGroupsInput")
    def num_node_groups_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numNodeGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="replicasPerNodeGroupInput")
    def replicas_per_node_group_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasPerNodeGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="numNodeGroups")
    def num_node_groups(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numNodeGroups"))

    @num_node_groups.setter
    def num_node_groups(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a86991ff2a4aa732671fd9a079cf4bd7dad9ea34c5e3ff7a1af6a2be97c1c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numNodeGroups", value)

    @builtins.property
    @jsii.member(jsii_name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicasPerNodeGroup"))

    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac9dba6afcc8a7e01ce558aa382dd8946020c6aa8467d77628db195f038a62e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicasPerNodeGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticacheReplicationGroupClusterMode]:
        return typing.cast(typing.Optional[ElasticacheReplicationGroupClusterMode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticacheReplicationGroupClusterMode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dec1f2b7f43e84f66a4ae6b77893770d5f9e7c6f0d1c6056c2d6fd65042eb05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "replication_group_id": "replicationGroupId",
        "apply_immediately": "applyImmediately",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "auth_token": "authToken",
        "automatic_failover_enabled": "automaticFailoverEnabled",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zones": "availabilityZones",
        "cluster_mode": "clusterMode",
        "data_tiering_enabled": "dataTieringEnabled",
        "description": "description",
        "engine": "engine",
        "engine_version": "engineVersion",
        "final_snapshot_identifier": "finalSnapshotIdentifier",
        "global_replication_group_id": "globalReplicationGroupId",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "log_delivery_configuration": "logDeliveryConfiguration",
        "maintenance_window": "maintenanceWindow",
        "multi_az_enabled": "multiAzEnabled",
        "node_type": "nodeType",
        "notification_topic_arn": "notificationTopicArn",
        "number_cache_clusters": "numberCacheClusters",
        "num_cache_clusters": "numCacheClusters",
        "num_node_groups": "numNodeGroups",
        "parameter_group_name": "parameterGroupName",
        "port": "port",
        "preferred_cache_cluster_azs": "preferredCacheClusterAzs",
        "replicas_per_node_group": "replicasPerNodeGroup",
        "replication_group_description": "replicationGroupDescription",
        "security_group_ids": "securityGroupIds",
        "security_group_names": "securityGroupNames",
        "snapshot_arns": "snapshotArns",
        "snapshot_name": "snapshotName",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "snapshot_window": "snapshotWindow",
        "subnet_group_name": "subnetGroupName",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "transit_encryption_enabled": "transitEncryptionEnabled",
        "user_group_ids": "userGroupIds",
    },
)
class ElasticacheReplicationGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        replication_group_id: builtins.str,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[builtins.str] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_mode: typing.Optional[typing.Union[ElasticacheReplicationGroupClusterMode, typing.Dict[builtins.str, typing.Any]]] = None,
        data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        global_replication_group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_delivery_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticacheReplicationGroupLogDeliveryConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        maintenance_window: typing.Optional[builtins.str] = None,
        multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        node_type: typing.Optional[builtins.str] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        number_cache_clusters: typing.Optional[jsii.Number] = None,
        num_cache_clusters: typing.Optional[jsii.Number] = None,
        num_node_groups: typing.Optional[jsii.Number] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_cache_cluster_azs: typing.Optional[typing.Sequence[builtins.str]] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
        replication_group_description: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ElasticacheReplicationGroupTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param replication_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replication_group_id ElasticacheReplicationGroup#replication_group_id}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#apply_immediately ElasticacheReplicationGroup#apply_immediately}.
        :param at_rest_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#at_rest_encryption_enabled ElasticacheReplicationGroup#at_rest_encryption_enabled}.
        :param auth_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#auth_token ElasticacheReplicationGroup#auth_token}.
        :param automatic_failover_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#automatic_failover_enabled ElasticacheReplicationGroup#automatic_failover_enabled}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#auto_minor_version_upgrade ElasticacheReplicationGroup#auto_minor_version_upgrade}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#availability_zones ElasticacheReplicationGroup#availability_zones}.
        :param cluster_mode: cluster_mode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#cluster_mode ElasticacheReplicationGroup#cluster_mode}
        :param data_tiering_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#data_tiering_enabled ElasticacheReplicationGroup#data_tiering_enabled}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#description ElasticacheReplicationGroup#description}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#engine ElasticacheReplicationGroup#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#engine_version ElasticacheReplicationGroup#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#final_snapshot_identifier ElasticacheReplicationGroup#final_snapshot_identifier}.
        :param global_replication_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#global_replication_group_id ElasticacheReplicationGroup#global_replication_group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#id ElasticacheReplicationGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#kms_key_id ElasticacheReplicationGroup#kms_key_id}.
        :param log_delivery_configuration: log_delivery_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_delivery_configuration ElasticacheReplicationGroup#log_delivery_configuration}
        :param maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#maintenance_window ElasticacheReplicationGroup#maintenance_window}.
        :param multi_az_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#multi_az_enabled ElasticacheReplicationGroup#multi_az_enabled}.
        :param node_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#node_type ElasticacheReplicationGroup#node_type}.
        :param notification_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#notification_topic_arn ElasticacheReplicationGroup#notification_topic_arn}.
        :param number_cache_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#number_cache_clusters ElasticacheReplicationGroup#number_cache_clusters}.
        :param num_cache_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_cache_clusters ElasticacheReplicationGroup#num_cache_clusters}.
        :param num_node_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_node_groups ElasticacheReplicationGroup#num_node_groups}.
        :param parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#parameter_group_name ElasticacheReplicationGroup#parameter_group_name}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#port ElasticacheReplicationGroup#port}.
        :param preferred_cache_cluster_azs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#preferred_cache_cluster_azs ElasticacheReplicationGroup#preferred_cache_cluster_azs}.
        :param replicas_per_node_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replicas_per_node_group ElasticacheReplicationGroup#replicas_per_node_group}.
        :param replication_group_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replication_group_description ElasticacheReplicationGroup#replication_group_description}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#security_group_ids ElasticacheReplicationGroup#security_group_ids}.
        :param security_group_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#security_group_names ElasticacheReplicationGroup#security_group_names}.
        :param snapshot_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_arns ElasticacheReplicationGroup#snapshot_arns}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_name ElasticacheReplicationGroup#snapshot_name}.
        :param snapshot_retention_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_retention_limit ElasticacheReplicationGroup#snapshot_retention_limit}.
        :param snapshot_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_window ElasticacheReplicationGroup#snapshot_window}.
        :param subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#subnet_group_name ElasticacheReplicationGroup#subnet_group_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#tags ElasticacheReplicationGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#tags_all ElasticacheReplicationGroup#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#timeouts ElasticacheReplicationGroup#timeouts}
        :param transit_encryption_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#transit_encryption_enabled ElasticacheReplicationGroup#transit_encryption_enabled}.
        :param user_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#user_group_ids ElasticacheReplicationGroup#user_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cluster_mode, dict):
            cluster_mode = ElasticacheReplicationGroupClusterMode(**cluster_mode)
        if isinstance(timeouts, dict):
            timeouts = ElasticacheReplicationGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12c0f3fb2c3dd5d1139bf1f64a1a12c0edcdb29d1fd7ec3690f28b8867efc630)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument replication_group_id", value=replication_group_id, expected_type=type_hints["replication_group_id"])
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument at_rest_encryption_enabled", value=at_rest_encryption_enabled, expected_type=type_hints["at_rest_encryption_enabled"])
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument automatic_failover_enabled", value=automatic_failover_enabled, expected_type=type_hints["automatic_failover_enabled"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument cluster_mode", value=cluster_mode, expected_type=type_hints["cluster_mode"])
            check_type(argname="argument data_tiering_enabled", value=data_tiering_enabled, expected_type=type_hints["data_tiering_enabled"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument final_snapshot_identifier", value=final_snapshot_identifier, expected_type=type_hints["final_snapshot_identifier"])
            check_type(argname="argument global_replication_group_id", value=global_replication_group_id, expected_type=type_hints["global_replication_group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_delivery_configuration", value=log_delivery_configuration, expected_type=type_hints["log_delivery_configuration"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument multi_az_enabled", value=multi_az_enabled, expected_type=type_hints["multi_az_enabled"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument notification_topic_arn", value=notification_topic_arn, expected_type=type_hints["notification_topic_arn"])
            check_type(argname="argument number_cache_clusters", value=number_cache_clusters, expected_type=type_hints["number_cache_clusters"])
            check_type(argname="argument num_cache_clusters", value=num_cache_clusters, expected_type=type_hints["num_cache_clusters"])
            check_type(argname="argument num_node_groups", value=num_node_groups, expected_type=type_hints["num_node_groups"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_cache_cluster_azs", value=preferred_cache_cluster_azs, expected_type=type_hints["preferred_cache_cluster_azs"])
            check_type(argname="argument replicas_per_node_group", value=replicas_per_node_group, expected_type=type_hints["replicas_per_node_group"])
            check_type(argname="argument replication_group_description", value=replication_group_description, expected_type=type_hints["replication_group_description"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument security_group_names", value=security_group_names, expected_type=type_hints["security_group_names"])
            check_type(argname="argument snapshot_arns", value=snapshot_arns, expected_type=type_hints["snapshot_arns"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument snapshot_retention_limit", value=snapshot_retention_limit, expected_type=type_hints["snapshot_retention_limit"])
            check_type(argname="argument snapshot_window", value=snapshot_window, expected_type=type_hints["snapshot_window"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transit_encryption_enabled", value=transit_encryption_enabled, expected_type=type_hints["transit_encryption_enabled"])
            check_type(argname="argument user_group_ids", value=user_group_ids, expected_type=type_hints["user_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_group_id": replication_group_id,
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
        if apply_immediately is not None:
            self._values["apply_immediately"] = apply_immediately
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if automatic_failover_enabled is not None:
            self._values["automatic_failover_enabled"] = automatic_failover_enabled
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if cluster_mode is not None:
            self._values["cluster_mode"] = cluster_mode
        if data_tiering_enabled is not None:
            self._values["data_tiering_enabled"] = data_tiering_enabled
        if description is not None:
            self._values["description"] = description
        if engine is not None:
            self._values["engine"] = engine
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if final_snapshot_identifier is not None:
            self._values["final_snapshot_identifier"] = final_snapshot_identifier
        if global_replication_group_id is not None:
            self._values["global_replication_group_id"] = global_replication_group_id
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_delivery_configuration is not None:
            self._values["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if multi_az_enabled is not None:
            self._values["multi_az_enabled"] = multi_az_enabled
        if node_type is not None:
            self._values["node_type"] = node_type
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn
        if number_cache_clusters is not None:
            self._values["number_cache_clusters"] = number_cache_clusters
        if num_cache_clusters is not None:
            self._values["num_cache_clusters"] = num_cache_clusters
        if num_node_groups is not None:
            self._values["num_node_groups"] = num_node_groups
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name
        if port is not None:
            self._values["port"] = port
        if preferred_cache_cluster_azs is not None:
            self._values["preferred_cache_cluster_azs"] = preferred_cache_cluster_azs
        if replicas_per_node_group is not None:
            self._values["replicas_per_node_group"] = replicas_per_node_group
        if replication_group_description is not None:
            self._values["replication_group_description"] = replication_group_description
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if security_group_names is not None:
            self._values["security_group_names"] = security_group_names
        if snapshot_arns is not None:
            self._values["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            self._values["snapshot_window"] = snapshot_window
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled
        if user_group_ids is not None:
            self._values["user_group_ids"] = user_group_ids

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
    def replication_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replication_group_id ElasticacheReplicationGroup#replication_group_id}.'''
        result = self._values.get("replication_group_id")
        assert result is not None, "Required property 'replication_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#apply_immediately ElasticacheReplicationGroup#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#at_rest_encryption_enabled ElasticacheReplicationGroup#at_rest_encryption_enabled}.'''
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#auth_token ElasticacheReplicationGroup#auth_token}.'''
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#automatic_failover_enabled ElasticacheReplicationGroup#automatic_failover_enabled}.'''
        result = self._values.get("automatic_failover_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_minor_version_upgrade(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#auto_minor_version_upgrade ElasticacheReplicationGroup#auto_minor_version_upgrade}.'''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#availability_zones ElasticacheReplicationGroup#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cluster_mode(self) -> typing.Optional[ElasticacheReplicationGroupClusterMode]:
        '''cluster_mode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#cluster_mode ElasticacheReplicationGroup#cluster_mode}
        '''
        result = self._values.get("cluster_mode")
        return typing.cast(typing.Optional[ElasticacheReplicationGroupClusterMode], result)

    @builtins.property
    def data_tiering_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#data_tiering_enabled ElasticacheReplicationGroup#data_tiering_enabled}.'''
        result = self._values.get("data_tiering_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#description ElasticacheReplicationGroup#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#engine ElasticacheReplicationGroup#engine}.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#engine_version ElasticacheReplicationGroup#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#final_snapshot_identifier ElasticacheReplicationGroup#final_snapshot_identifier}.'''
        result = self._values.get("final_snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_replication_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#global_replication_group_id ElasticacheReplicationGroup#global_replication_group_id}.'''
        result = self._values.get("global_replication_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#id ElasticacheReplicationGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#kms_key_id ElasticacheReplicationGroup#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticacheReplicationGroupLogDeliveryConfiguration"]]]:
        '''log_delivery_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_delivery_configuration ElasticacheReplicationGroup#log_delivery_configuration}
        '''
        result = self._values.get("log_delivery_configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticacheReplicationGroupLogDeliveryConfiguration"]]], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#maintenance_window ElasticacheReplicationGroup#maintenance_window}.'''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_az_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#multi_az_enabled ElasticacheReplicationGroup#multi_az_enabled}.'''
        result = self._values.get("multi_az_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def node_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#node_type ElasticacheReplicationGroup#node_type}.'''
        result = self._values.get("node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#notification_topic_arn ElasticacheReplicationGroup#notification_topic_arn}.'''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_cache_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#number_cache_clusters ElasticacheReplicationGroup#number_cache_clusters}.'''
        result = self._values.get("number_cache_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_cache_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_cache_clusters ElasticacheReplicationGroup#num_cache_clusters}.'''
        result = self._values.get("num_cache_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_node_groups(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#num_node_groups ElasticacheReplicationGroup#num_node_groups}.'''
        result = self._values.get("num_node_groups")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#parameter_group_name ElasticacheReplicationGroup#parameter_group_name}.'''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#port ElasticacheReplicationGroup#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_cache_cluster_azs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#preferred_cache_cluster_azs ElasticacheReplicationGroup#preferred_cache_cluster_azs}.'''
        result = self._values.get("preferred_cache_cluster_azs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def replicas_per_node_group(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replicas_per_node_group ElasticacheReplicationGroup#replicas_per_node_group}.'''
        result = self._values.get("replicas_per_node_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replication_group_description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#replication_group_description ElasticacheReplicationGroup#replication_group_description}.'''
        result = self._values.get("replication_group_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#security_group_ids ElasticacheReplicationGroup#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#security_group_names ElasticacheReplicationGroup#security_group_names}.'''
        result = self._values.get("security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_arns ElasticacheReplicationGroup#snapshot_arns}.'''
        result = self._values.get("snapshot_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_name ElasticacheReplicationGroup#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_retention_limit ElasticacheReplicationGroup#snapshot_retention_limit}.'''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#snapshot_window ElasticacheReplicationGroup#snapshot_window}.'''
        result = self._values.get("snapshot_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#subnet_group_name ElasticacheReplicationGroup#subnet_group_name}.'''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#tags ElasticacheReplicationGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#tags_all ElasticacheReplicationGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ElasticacheReplicationGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#timeouts ElasticacheReplicationGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ElasticacheReplicationGroupTimeouts"], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#transit_encryption_enabled ElasticacheReplicationGroup#transit_encryption_enabled}.'''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#user_group_ids ElasticacheReplicationGroup#user_group_ids}.'''
        result = self._values.get("user_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticacheReplicationGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupLogDeliveryConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "destination_type": "destinationType",
        "log_format": "logFormat",
        "log_type": "logType",
    },
)
class ElasticacheReplicationGroupLogDeliveryConfiguration:
    def __init__(
        self,
        *,
        destination: builtins.str,
        destination_type: builtins.str,
        log_format: builtins.str,
        log_type: builtins.str,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#destination ElasticacheReplicationGroup#destination}.
        :param destination_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#destination_type ElasticacheReplicationGroup#destination_type}.
        :param log_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_format ElasticacheReplicationGroup#log_format}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_type ElasticacheReplicationGroup#log_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450da7b116d8a05223f258b3e4a72c38b3ede28b6312f1a2dad419ebf29090a6)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "destination_type": destination_type,
            "log_format": log_format,
            "log_type": log_type,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#destination ElasticacheReplicationGroup#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#destination_type ElasticacheReplicationGroup#destination_type}.'''
        result = self._values.get("destination_type")
        assert result is not None, "Required property 'destination_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_format ElasticacheReplicationGroup#log_format}.'''
        result = self._values.get("log_format")
        assert result is not None, "Required property 'log_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#log_type ElasticacheReplicationGroup#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticacheReplicationGroupLogDeliveryConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticacheReplicationGroupLogDeliveryConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupLogDeliveryConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f030f7f023fe15b68fb3c81cf6b68cff36c0c818354d16fb02ca31565685b77)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElasticacheReplicationGroupLogDeliveryConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e2c1ef051cdeb48170d98693704f0c6c48a410b09a23ad468cbf46410010b5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElasticacheReplicationGroupLogDeliveryConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a1864a3587baad5a14af73dc855f41d8cae89fd0c80008f5f24bd2828743a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e3f596aa7cd420cde26e1bbd4bf48de683d6c23c546b8998f1c803438dd5cce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7addbad6587e97e230eea59cf019104ff3e14549ffd0fc7413e067ba5f31f723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticacheReplicationGroupLogDeliveryConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticacheReplicationGroupLogDeliveryConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticacheReplicationGroupLogDeliveryConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf37c305c1c13acdf87703778b0fff0320e055ed0bcadf6ee0ee8356bceb6a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticacheReplicationGroupLogDeliveryConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupLogDeliveryConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70ea1f1a12a47b1f24bdacd5806732aad467da0db5af9a8cdc7fed13fc29b811)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationTypeInput")
    def destination_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="logFormatInput")
    def log_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691f102864ebc35ac0e3f55649ecbaac5379de77b44e09a54b1f2b193c78598c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="destinationType")
    def destination_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationType"))

    @destination_type.setter
    def destination_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e847e1ddfa8eb60ba63aba154fea3250ca96f19e5b8f0f1e970ecdfbc501afe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationType", value)

    @builtins.property
    @jsii.member(jsii_name="logFormat")
    def log_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logFormat"))

    @log_format.setter
    def log_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172ad2b25b1fe3fd230272a954603dab1b8a5340f69a90eb4f2ab5dd557caa3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logFormat", value)

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c5a5cc78ea61476bc19a74fc3cb94c968e16b2ae99ab94c8791bdeaa2f5fbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7305a2283bfe2116ecc2b8488d579b4329c5a4d0a31c574d9b9ee36cd01093c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ElasticacheReplicationGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#create ElasticacheReplicationGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#delete ElasticacheReplicationGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#update ElasticacheReplicationGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__277521aa655a20cd7dec1f0a08c0ac4c6337ebc04ee70c906eb400fc53dc1486)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#create ElasticacheReplicationGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#delete ElasticacheReplicationGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group#update ElasticacheReplicationGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticacheReplicationGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticacheReplicationGroupTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticacheReplicationGroup.ElasticacheReplicationGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb1d746594748b9ca088c7bee60654cc7a9b24ee160750c40800cd23ea5f7dfb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3269f7d554c47cdca896b0c6687b2c9f0b5a2c933868db43404c600cceadac53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d355af6b8d31e68aaf27249c7641041b4d7f40b4501ccf05cebeff6517be5ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff829c848b3e5032642dc360a80562cb793892aeae26f918a850264899f4555)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticacheReplicationGroupTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticacheReplicationGroupTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticacheReplicationGroupTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ec25d4b4ea18cdfab2e710f8764531e60827bbc32c0d461999f64aef96d0314)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElasticacheReplicationGroup",
    "ElasticacheReplicationGroupClusterMode",
    "ElasticacheReplicationGroupClusterModeOutputReference",
    "ElasticacheReplicationGroupConfig",
    "ElasticacheReplicationGroupLogDeliveryConfiguration",
    "ElasticacheReplicationGroupLogDeliveryConfigurationList",
    "ElasticacheReplicationGroupLogDeliveryConfigurationOutputReference",
    "ElasticacheReplicationGroupTimeouts",
    "ElasticacheReplicationGroupTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__05ea70d7fd705c24106460c79b86111b36bd4de6297121bade25532950bab4a5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    replication_group_id: builtins.str,
    apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auth_token: typing.Optional[builtins.str] = None,
    automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_minor_version_upgrade: typing.Optional[builtins.str] = None,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    cluster_mode: typing.Optional[typing.Union[ElasticacheReplicationGroupClusterMode, typing.Dict[builtins.str, typing.Any]]] = None,
    data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    final_snapshot_identifier: typing.Optional[builtins.str] = None,
    global_replication_group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_delivery_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    maintenance_window: typing.Optional[builtins.str] = None,
    multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    node_type: typing.Optional[builtins.str] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    number_cache_clusters: typing.Optional[jsii.Number] = None,
    num_cache_clusters: typing.Optional[jsii.Number] = None,
    num_node_groups: typing.Optional[jsii.Number] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_cache_cluster_azs: typing.Optional[typing.Sequence[builtins.str]] = None,
    replicas_per_node_group: typing.Optional[jsii.Number] = None,
    replication_group_description: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ElasticacheReplicationGroupTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__ed946685cc984161a0ea9f4711015a86807fe92ec6a22cf579de10f14b344abb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69fec3d94d3e189578b0252053ad73681e657e7e45b0a5df61f7fcd3864151b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cdbba326ad40fe190ad6e2dbddca4fa9b4751334200bb12aee592cc35e54da0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a210cf11c2e43c8e9ada7789d697b3e2d1c1cf4b5590df07b7f822252682cf43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f94af344a944c7ed3de186569e5a8fa1f8a115dd100589ddc5a6cb6ad3209a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9946ca3a0cdaa6277eb01532dcc56fecd3254d8acadd3d12e1bf3e50cd5c224c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9bd4fd08eba2c7a3330d74c8afcec66eeeaa9cf8c319f76103ed5db62916ac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22532caf69c7947057cdc59e6e397c09ca331ac469c87d009a0fbf6d141edb85(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f468087e7caa99dbfb1f0f0fcd240bd5a1a842f8277312d8acb28d943f1775c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a8b2bdd49028693cc2c9c83a384da832c51c12d8fd282a25536ab45ee37a0c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f7137b2de79963f5db534f791700efaa706b509aedeb8363dbf87930df4fac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83dc52d401c49cad9ffc48353ea792942147ee7107787d4ff8baa0d066ee9ca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1185a779eefa4a13636d26a255fa38b1e8f56d68283a298bfeaabe3d0d5164ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d329670610fd30bb47ed96a5ef1094efe8ae2f9abf8d68894f5768a65625b496(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e08f003ee8568236132ac8b8d6a364ad24ade081b01fad908ab954810777b10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9af9c2cefb30ab5295370fc4e67fff1f0ab64b289923d3db5ae2caab11dff1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6ebf68762164d999175912f153a2648e28e6a63f275a1deacb0073c3583d01(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca8cc3e3d1f78231ff5a1b01930ce5dd1cd5fd69640dde460fe1603c76ab680(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d84f1335b137e2ebfe77accf6b0bb9a7648d24f48ac737132c0cf6517ac0c0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6d54f22f4a9adfacd2fdb3deb3ee6771c968cbe63d9cdd20bc8106f6559e20(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a129e8196d6475951ccd2eae707c09ac07767faa5c5a22ad14f06d85a8e832ed(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f5297a5ae2244c483816981969d3134d08fc93c4ec3a65aec969d48ff2c2e9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99261d56d49ad86ba1806b8ded69f5cf4f8c210520d2cc0950f65f93b5a14832(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3570395f11326ad001b641c814a08d497e208abeaa6536d7e470ba9b23e48804(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4f193a7adeb70bfeff9e9c209bc5ce37dd75c91797e82976a4a2a60dadc025(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57e9b3ff7a8ecc72c38c8c105251a6a280c6a71c715c67d1a4cdc9fcaf1b2c9b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab208c6b695692c759c9fcf158b97bbede5f72e707e4a8ec36a375b1bf7b71c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9835b136b72a6915612dce56ea3bb6dcb25f8ff42a163d091217e451f1f8f17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd277ae68be3dcace1ab4b1a485d1394ffceffe9672772a66be74c1a49f7503(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0999a4549564991de6c0b8419778ae0f5129b051687db4425b875680a3abbb6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9441942c4847a665ae91e07bd40e1e69109c6338b80ebacc2a6e8a2237391c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf8b66cb809fe621582550bd73baa3d80ed89486fba12336e05760b8ea8289b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c7c4d3ac6fffa7239a313499ef9e8abe1a9fb315642fc711457c572ff12b26(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646f5373b5c73cc5474397f1ab7e54237233d6e73cd5353576e3f8c1c1fd139f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f96df803484b106f544b3090589e2467da421e4e5a10438da0607d8fae65e5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473dd80cbda23603397a1e18fbf71d31ddb6f3b272ea6548f2989e5f0c5a1dcc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdda69ca97fa32f86fffa133b967d5c6f8206973aaf4878ce7b44b8fb0b6206a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75cb61ee1ddeb81949fb7f1a147f256288e9ac5b70b4603135906a9f1502abd1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da4208cf3b32435e8809b6c7648eb222c84221ad6ab4b46241fa6b71c25b6a8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1392afe960e4f346cd42271383314164bc2b98edc5d1c46013711b6547888c(
    *,
    num_node_groups: typing.Optional[jsii.Number] = None,
    replicas_per_node_group: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd90a5fb04477fe3fb37e1abb9a9ffc4dfe7ade811140c90c6d714174c01e11b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a86991ff2a4aa732671fd9a079cf4bd7dad9ea34c5e3ff7a1af6a2be97c1c6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac9dba6afcc8a7e01ce558aa382dd8946020c6aa8467d77628db195f038a62e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dec1f2b7f43e84f66a4ae6b77893770d5f9e7c6f0d1c6056c2d6fd65042eb05(
    value: typing.Optional[ElasticacheReplicationGroupClusterMode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c0f3fb2c3dd5d1139bf1f64a1a12c0edcdb29d1fd7ec3690f28b8867efc630(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    replication_group_id: builtins.str,
    apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auth_token: typing.Optional[builtins.str] = None,
    automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_minor_version_upgrade: typing.Optional[builtins.str] = None,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    cluster_mode: typing.Optional[typing.Union[ElasticacheReplicationGroupClusterMode, typing.Dict[builtins.str, typing.Any]]] = None,
    data_tiering_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    final_snapshot_identifier: typing.Optional[builtins.str] = None,
    global_replication_group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_delivery_configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    maintenance_window: typing.Optional[builtins.str] = None,
    multi_az_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    node_type: typing.Optional[builtins.str] = None,
    notification_topic_arn: typing.Optional[builtins.str] = None,
    number_cache_clusters: typing.Optional[jsii.Number] = None,
    num_cache_clusters: typing.Optional[jsii.Number] = None,
    num_node_groups: typing.Optional[jsii.Number] = None,
    parameter_group_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_cache_cluster_azs: typing.Optional[typing.Sequence[builtins.str]] = None,
    replicas_per_node_group: typing.Optional[jsii.Number] = None,
    replication_group_description: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_retention_limit: typing.Optional[jsii.Number] = None,
    snapshot_window: typing.Optional[builtins.str] = None,
    subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ElasticacheReplicationGroupTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450da7b116d8a05223f258b3e4a72c38b3ede28b6312f1a2dad419ebf29090a6(
    *,
    destination: builtins.str,
    destination_type: builtins.str,
    log_format: builtins.str,
    log_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f030f7f023fe15b68fb3c81cf6b68cff36c0c818354d16fb02ca31565685b77(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e2c1ef051cdeb48170d98693704f0c6c48a410b09a23ad468cbf46410010b5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a1864a3587baad5a14af73dc855f41d8cae89fd0c80008f5f24bd2828743a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3f596aa7cd420cde26e1bbd4bf48de683d6c23c546b8998f1c803438dd5cce(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7addbad6587e97e230eea59cf019104ff3e14549ffd0fc7413e067ba5f31f723(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf37c305c1c13acdf87703778b0fff0320e055ed0bcadf6ee0ee8356bceb6a39(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticacheReplicationGroupLogDeliveryConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ea1f1a12a47b1f24bdacd5806732aad467da0db5af9a8cdc7fed13fc29b811(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691f102864ebc35ac0e3f55649ecbaac5379de77b44e09a54b1f2b193c78598c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e847e1ddfa8eb60ba63aba154fea3250ca96f19e5b8f0f1e970ecdfbc501afe1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172ad2b25b1fe3fd230272a954603dab1b8a5340f69a90eb4f2ab5dd557caa3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c5a5cc78ea61476bc19a74fc3cb94c968e16b2ae99ab94c8791bdeaa2f5fbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7305a2283bfe2116ecc2b8488d579b4329c5a4d0a31c574d9b9ee36cd01093c1(
    value: typing.Optional[typing.Union[ElasticacheReplicationGroupLogDeliveryConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277521aa655a20cd7dec1f0a08c0ac4c6337ebc04ee70c906eb400fc53dc1486(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1d746594748b9ca088c7bee60654cc7a9b24ee160750c40800cd23ea5f7dfb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3269f7d554c47cdca896b0c6687b2c9f0b5a2c933868db43404c600cceadac53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d355af6b8d31e68aaf27249c7641041b4d7f40b4501ccf05cebeff6517be5ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff829c848b3e5032642dc360a80562cb793892aeae26f918a850264899f4555(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ec25d4b4ea18cdfab2e710f8764531e60827bbc32c0d461999f64aef96d0314(
    value: typing.Optional[typing.Union[ElasticacheReplicationGroupTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
